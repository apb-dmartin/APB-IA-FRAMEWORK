---
id: "apb-qa-tdd-v1.0"
name: "Tdd"
description: "Usar al implementar cualquier feature o bugfix, antes de escribir c\xF3digo de implementaci\xF3\
  n. Especializado en testing de sistemas orientados a eventos."
version: "1.0.0"
status: "draft"
owner: "QA / Desarrollo APB <arquitectura@portdebarcelona.cat>"
domain: "qa"
autonomy_level: 1
consumed_by:
  - "apb-agent-qa-auto-v1.0"
created_date: "2026-06-20"
review_date: "2026-06-24"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

> Procedencia: Adaptado de obra/superpowers (test-driven-development) + wshobson/agents (tdd-workflows) (licencia MIT). Contenido adaptado y
> generalizado para el APB AI Framework.

# APB Test-Driven Development (TDD)


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Visión General

Escribe el test primero. Velo fallar. Escribe código mínimo para pasar.

**Principio fundamental:** Si no viste el test fallar, no sabes si testea lo correcto.

**Violar la letra de las reglas es violar el espíritu de las reglas.**

## Cuándo Usar

**Siempre:**
- Nuevas features
- Bug fixes
- Refactoring
- Cambios de comportamiento

**Excepciones (preguntar a tu partner humano):**
- Prototipos descartables
- Código generado
- Archivos de configuración

Pensando "salto TDD solo esta vez"? Detente. Eso es racionalización.

## La Ley de Hierro

```
NO CÓDIGO DE PRODUCCIÓN SIN UN TEST FALLANDO PRIMERO
```

¿Escribiste código antes del test? Bórralo. Empieza de nuevo.

**Sin excepciones:**
- No lo guardes como "referencia"
- No lo "adaptes" mientras escribes tests
- No lo mires
- Borrar significa borrar

Implementa fresco desde los tests. Punto.

## Ciclo Red-Green-Refactor

```
RED    → Escribe test fallando
VERIFY → Confirma que falla correctamente
GREEN  → Código mínimo para pasar
VERIFY → Confirma que pasa
REFACTOR → Limpia el código
VERIFY → Confirma que sigue pasando
```

### RED — Escribir Test Fallando

Escribe un test mínimo mostrando qué debería pasar.

**Requisitos:**
- Un comportamiento
- Nombre claro
- Código real (no mocks a menos que sea inevitable)

### Testing Específico de Event-Driven

#### Tests de Productor de Eventos

```javascript
// ✅ BUENO: Testea comportamiento real
test('publica OrderCreated con datos correctos cuando se crea orden', async () => {
  const orderService = new OrderService(eventBus);
  const order = await orderService.create({ productId: '123', quantity: 2 });

  const publishedEvents = await eventBus.getPublishedEvents();
  expect(publishedEvents).toHaveLength(1);
  expect(publishedEvents[0].type).toBe('orders.order-created.v1');
  expect(publishedEvents[0].data.orderId).toBe(order.id);
  expect(publishedEvents[0].specversion).toBe('1.0');
});

// ❌ MALO: Testea mocks, no código real
test('event bus publish is called', async () => {
  const mockPublish = jest.fn();
  const orderService = new OrderService({ publish: mockPublish });
  await orderService.create({ productId: '123' });
  expect(mockPublish).toHaveBeenCalled();
});
```

#### Tests de Consumidor de Eventos

```javascript
// ✅ BUENO: Testea comportamiento real del handler
test('procesa OrderCreated y actualiza inventario', async () => {
  const event = createCloudEvent('orders.order-created.v1', {
    orderId: 'ord-123',
    productId: 'prod-456',
    quantity: 2
  });

  await inventoryHandler.handle(event);

  const inventory = await inventoryRepository.get('prod-456');
  expect(inventory.quantity).toBe(originalQuantity - 2);
});
```

#### Tests de Idempotencia

```javascript
test('procesa evento duplicado sin efectos secundarios', async () => {
  const event = createCloudEvent('orders.order-created.v1', { orderId: 'ord-123' });

  await handler.handle(event);
  await handler.handle(event); // Mismo evento, segundo intento

  const processedCount = await eventStore.getProcessedCount('ord-123');
  expect(processedCount).toBe(1);
});
```

#### Tests de Saga (Compensación)

```javascript
test('compensa reserva de inventario cuando pago falla', async () => {
  // Setup: reserva exitosa
  await saga.executeStep('reserve-inventory', { productId: '123', qty: 2 });

  // Simular fallo de pago
  paymentService.mockFailure();

  // Ejecutar compensación
  await saga.compensate('reserve-inventory');

  const inventory = await inventoryRepository.get('123');
  expect(inventory.quantity).toBe(originalQuantity); // Restaurado
});
```

#### Tests de Dead Letter Queue

```javascript
test('mueve evento a DLQ después de máximo reintentos', async () => {
  const event = createCloudEvent('orders.invalid-event.v1', { badData: true });
  handler.mockPersistentFailure();

  // Simular reintentos con backoff
  for (let i = 0; i < MAX_RETRIES; i++) {
    await expect(handler.handle(event)).rejects.toThrow();
  }

  const dlqMessages = await deadLetterQueue.peek();
  expect(dlqMessages).toHaveLength(1);
  expect(dlqMessages[0].deliveryCount).toBe(MAX_RETRIES);
});
```

### Verify RED — Velo Fallar

**OBLIGATORIO. Nunca saltar.**

```bash
npm test path/to/test.test.js
```

Confirmar:
- Test falla (no errores)
- Mensaje de fallo es el esperado
- Falla porque falta feature (no typos)

**¿El test pasa?** Estás testeando comportamiento existente. Arregla el test.

**¿El test tiene errores?** Arregla el error, re-ejecuta hasta que falle correctamente.

### GREEN — Código Mínimo

Escribe la cantidad mínima de código para que el test pase.

**Reglas:**
- No anticipar features
- No refactorizar todavía
- Código feo está bien temporalmente
- Si necesitas cambiar el test para que pase, hazlo — pero vuelve a RED primero

### REFACTOR — Limpia

Con tests verdes, limpia el código:
- Elimina duplicación
- Mejora nombres
- Simplifica lógica
- Extrae funciones
- Añade tipos (si aplica)

**Restricciones:**
- Tests deben seguir pasando
- No añadir comportamiento nuevo
- Un cambio a la vez, verificar verdes

## Anti-Patrón: Mock-itis en Event-Driven

```javascript
// ❌ MALO: Todo mocks, nada real
test('handler processes event', async () => {
  const mockRepo = { update: jest.fn() };
  const mockBus = { publish: jest.fn() };
  const handler = new Handler(mockRepo, mockBus);
  await handler.handle(mockEvent);
  expect(mockRepo.update).toHaveBeenCalled();
  expect(mockBus.publish).toHaveBeenCalled();
});

// ✅ BUENO: Test con infraestructura real (test containers)
test('handler processes event end-to-end', async () => {
  const { eventBus, repository } = await setupTestInfrastructure();
  const handler = new Handler(repository, eventBus);

  await handler.handle(realEvent);

  const entity = await repository.get(realEvent.data.id);
  expect(entity.status).toBe('processed');
});
```


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Codigo generado** - primera linea del bloque: `// [IA-GEN] Generado por APB AI Framework (apb-qa-tdd-v1.0) - pendiente revision humana`
- **Commit** - prefijo `[ai-gen]` en el mensaje + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`
- **PR asociado** - label `ai-generated` en GitHub + footer en descripcion del PR
