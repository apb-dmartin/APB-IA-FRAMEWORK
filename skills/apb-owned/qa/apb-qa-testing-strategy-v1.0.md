---
id: "apb-qa-testing-strategy-v1.0"
name: "Testing Strategy"
description: "Estrategia completa de testing para arquitecturas orientadas a eventos. Define pir\xE1\
  mide de tests, estrategias de integraci\xF3n con Service Bus, y pr\xE1cticas de\
  \ testing de sagas."
version: "1.0.0"
status: "draft"
owner: "QA APB <arquitectura@portdebarcelona.cat>"
domain: "qa"
autonomy_level: 1
consumed_by:
  - "apb-agent-qa-auto-v1.0"
created_date: "2026-06-20"
review_date: "2026-06-24"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

> Procedencia: Adaptado de obra/superpowers (test-driven-development testing-anti-patterns) + wshobson/agents (unit-testing, api-testing-observability) (licencia MIT). Contenido adaptado y
> generalizado para el APB AI Framework.

# APB Testing Strategy: Estrategia de Testing para Event-Driven


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Visión General

Los sistemas orientados a eventos requieren una estrategia de testing que vaya más allá de unit tests: los eventos fluyen entre servicios, las sagas coordinan transacciones distribuidas, y los consumidores deben ser idempotentes.

**Principio fundamental:** Testear el flujo de eventos, no solo el código.

## Pirámide de Tests APB

```
         /\
        /  \
       / E2E \      ← 5%: Flujos de negocio completos
      /────────\        (saga end-to-end, flujo de orden)
     / Integration\   ← 15%: Publish/consume entre servicios
    /──────────────\     (Service Bus real, test containers)
   /   Contract     \  ← 20%: Schemas, contratos de eventos
  /──────────────────\   (CloudEvents validation, Pact)
 /      Unit          \ ← 60%: Handlers, lógica de negocio
/────────────────────────\  (sin mocks de infraestructura)
```

## Niveles de Testing

### 1. Unit Tests (60%)

**Qué testear:**
- Lógica de negocio pura (sin dependencias de infraestructura)
- Transformaciones de datos
- Validaciones de schemas
- Cálculos y algoritmos

**Qué NO testear:**
- Conexiones a Service Bus (usar fakes, no mocks)
- Queries a base de datos (testear en integración)
- Llamadas a servicios externos (testear en integración)

```javascript
// ✅ BUENO: Unit test de lógica pura
describe('OrderTotalCalculator', () => {
  test('calcula total con descuento del 10%', () => {
    const items = [
      { price: 100, quantity: 2 },
      { price: 50, quantity: 1 }
    ];
    const result = calculateTotal(items, { discount: 0.10 });
    expect(result).toBe(225); // (200 + 50) * 0.9
  });
});

// ❌ MALO: Unit test con mocks de infraestructura
describe('OrderHandler', () => {
  test('procesa orden', async () => {
    const mockRepo = { save: jest.fn() };
    const mockBus = { publish: jest.fn() };
    const handler = new OrderHandler(mockRepo, mockBus);
    await handler.handle(mockEvent);
    expect(mockRepo.save).toHaveBeenCalled(); // ¿Testea qué?
  });
});
```

### 2. Contract Tests (20%)

**Qué testear:**
- Schemas CloudEvents válidos
- Compatibilidad entre versiones
- Serialización/deserialización correcta
- Campos obligatorios presentes

```javascript
// ✅ Contract test con CloudEvents SDK
const { CloudEvent, Validation } = require('cloudevents');

describe('OrderCreated Contract', () => {
  test('evento válido pasa validación', () => {
    const event = new CloudEvent({
      type: 'com.ejemplo.ordenes.order-created.v1',
      source: '/servicios/order-service',
      id: 'test-123',
      time: new Date().toISOString(),
      data: { orderId: 'ord-1', customerId: 'cust-1', items: [] }
    });

    expect(() => Validation.isValidEvent(event)).not.toThrow();
  });

  test('evento sin campos obligatorios falla', () => {
    const invalidEvent = {
      type: 'com.ejemplo.ordenes.order-created.v1',
      // falta source, id, time
      data: {}
    };

    expect(() => Validation.isValidEvent(invalidEvent)).toThrow();
  });

  test('backward compatibility v1 → v1.1', () => {
    const v1Event = { /* schema v1 */ };
    const v1_1Handler = new OrderCreatedHandlerV1_1();

    // Handler v1.1 debe poder procesar evento v1
    expect(() => v1_1Handler.handle(v1Event)).not.toThrow();
  });
});
```

### 3. Integration Tests (15%)

**Qué testear:**
- Publish real a Service Bus + consume real
- Idempotencia con infraestructura real
- Dead letter con infraestructura real
- Saga con orquestador real
- Proyecciones de read model

**Infraestructura:**
- Azure Service Bus Emulator o instancia de test
- Base de datos de test (SQLite en memoria o container)
- No mocks del broker de eventos

```javascript
// ✅ Integration test con Service Bus real
const { ServiceBusClient } = require('@azure/service-bus');

describe('OrderCreated Integration', () => {
  let serviceBusClient;
  let orderService;
  let inventoryHandler;

  beforeAll(async () => {
    serviceBusClient = new ServiceBusClient(process.env.SERVICEBUS_CONNECTION_STRING_TEST);
    orderService = new OrderService(serviceBusClient);
    inventoryHandler = new InventoryHandler(serviceBusClient);
    await inventoryHandler.start();
  });

  test('evento publicado es consumido por InventoryService', async () => {
    // 1. Crear orden (publica evento)
    const order = await orderService.create({
      productId: 'prod-123',
      quantity: 2
    });

    // 2. Esperar a que el consumidor procese
    await waitFor(() => inventoryHandler.getProcessedEvents().length > 0, { timeout: 5000 });

    // 3. Verificar que el inventario se actualizó
    const inventory = await inventoryRepository.get('prod-123');
    expect(inventory.reservedQuantity).toBe(2);
  });

  test('evento duplicado no procesa dos veces', async () => {
    const event = createTestEvent('orders.order-created.v1', { orderId: 'dup-test' });

    // Publicar mismo evento dos veces
    await publishEvent(event);
    await publishEvent(event);

    await waitFor(() => inventoryHandler.getProcessedEvents().length > 0, { timeout: 5000 });

    // Verificar que solo se procesó una vez
    const processed = await processedEventsRepository.getByEventId(event.id);
    expect(processed.length).toBe(1);
  });

  test('mensaje con error va a DLQ después de reintentos', async () => {
    // Configurar handler para fallar siempre
    inventoryHandler.mockPersistentFailure();

    const event = createTestEvent('orders.invalid.v1', { badData: true });
    await publishEvent(event);

    // Esperar a que se mueva a DLQ
    await waitFor(async () => {
      const dlqCount = await getDLQMessageCount('topic-orders', 'sub-inventory-service');
      return dlqCount > 0;
    }, { timeout: 30000 });

    const dlqMessages = await peekDLQ('topic-orders', 'sub-inventory-service');
    expect(dlqMessages[0].deliveryCount).toBeGreaterThanOrEqual(10);
  });

  afterAll(async () => {
    await inventoryHandler.stop();
    await serviceBusClient.close();
  });
});
```

### 4. E2E Tests (5%)

**Qué testear:**
- Flujos de negocio completos (crear orden → reservar → pagar → enviar)
- Compensaciones de saga
- Escenarios de error end-to-end
- Performance bajo carga

```javascript
// ✅ E2E test de flujo completo
describe('Order Flow E2E', () => {
  test('flujo completo: orden → pago → envío', async () => {
    // 1. Crear orden
    const order = await apiClient.post('/orders', {
      customerId: 'cust-1',
      items: [{ productId: 'prod-1', quantity: 1 }]
    });
    expect(order.status).toBe('pending');

    // 2. Esperar confirmación de inventario
    await waitFor(async () => {
      const updated = await apiClient.get(`/orders/${order.id}`);
      return updated.status === 'inventory-reserved';
    }, { timeout: 10000 });

    // 3. Procesar pago
    await apiClient.post(`/orders/${order.id}/pay`, { method: 'credit-card' });

    // 4. Esperar confirmación de pago
    await waitFor(async () => {
      const updated = await apiClient.get(`/orders/${order.id}`);
      return updated.status === 'paid';
    }, { timeout: 10000 });

    // 5. Esperar creación de envío
    await waitFor(async () => {
      const shipments = await apiClient.get(`/shipments?orderId=${order.id}`);
      return shipments.length > 0;
    }, { timeout: 15000 });

    // 6. Verificar estado final
    const finalOrder = await apiClient.get(`/orders/${order.id}`);
    expect(finalOrder.status).toBe('shipped');
  });

  test('compensación: pago falla, inventario se libera', async () => {
    // 1. Crear orden
    const order = await apiClient.post('/orders', {
      customerId: 'cust-1',
      items: [{ productId: 'prod-1', quantity: 1 }]
    });

    // 2. Simular fallo de pago
    paymentService.mockFailure();

    // 3. Intentar pagar
    await expect(
      apiClient.post(`/orders/${order.id}/pay`, { method: 'credit-card' })
    ).rejects.toThrow();

    // 4. Verificar compensación
    await waitFor(async () => {
      const inventory = await apiClient.get('/inventory/prod-1');
      return inventory.reservedQuantity === 0;
    }, { timeout: 10000 });

    // 5. Verificar estado final de orden
    const finalOrder = await apiClient.get(`/orders/${order.id}`);
    expect(finalOrder.status).toBe('cancelled');
  });
});
```

## Estrategias de Test para Escenarios Específicos

### Testing de Idempotencia

```javascript
describe('Idempotency', () => {
  test.each([2, 3, 5, 10])('procesa %i eventos idénticos como uno solo', async (count) => {
    const event = createTestEvent('orders.order-created.v1', { orderId: 'idemp-test' });

    // Publicar mismo evento múltiples veces
    for (let i = 0; i < count; i++) {
      await publishEvent(event);
    }

    await waitFor(() => handler.getProcessedCount() >= 1, { timeout: 5000 });

    const processedCount = await processedEventsRepository.getCount(event.id);
    expect(processedCount).toBe(1);
  });
});
```

### Testing de Ordenamiento (Sessions)

```javascript
describe('Session Ordering', () => {
  test('procesa eventos en orden por sessionId', async () => {
    const sessionId = 'customer-123';
    const events = [
      { type: 'orders.order-created.v1', sequence: 1 },
      { type: 'orders.order-updated.v1', sequence: 2 },
      { type: 'orders.order-paid.v1', sequence: 3 }
    ];

    // Publicar en orden inverso
    for (const event of events.reverse()) {
      await publishEvent({ ...event, sessionId });
    }

    // Verificar que se procesaron en orden correcto
    const processed = await waitForAllProcessed(sessionId);
    expect(processed.map(e => e.sequence)).toEqual([1, 2, 3]);
  });
});
```

### Testing de Performance

```javascript
describe('Performance', () => {
  test('procesa 1000 eventos en menos de 30 segundos', async () => {
    const events = Array.from({ length: 1000 }, (_, i) => 
      createTestEvent('orders.order-created.v1', { orderId: `perf-${i}` })
    );

    const start = Date.now();
    await Promise.all(events.map(e => publishEvent(e)));
    await waitFor(() => handler.getProcessedCount() === 1000, { timeout: 30000 });
    const elapsed = Date.now() - start;

    expect(elapsed).toBeLessThan(30000);
    expect(handler.getProcessedCount()).toBe(1000);
  });
});
```

## Anti-Patrón: Mock-itis en Tests de Eventos

```javascript
// ❌ MALO: Tests con mocks de todo
const mockServiceBus = {
  createSender: jest.fn(() => ({ sendMessages: jest.fn() })),
  createReceiver: jest.fn(() => ({ subscribe: jest.fn() }))
};

// ✅ BUENO: Tests con infraestructura real (test containers)
const serviceBusClient = new ServiceBusClient(process.env.SERVICEBUS_TEST_CONNECTION);
```

## Configuración de CI/CD para Tests

```yaml
# .github/workflows/test.yml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    services:
      servicebus:
        image: mcr.microsoft.com/azure-messaging/servicebus-emulator:latest
        env:
          SERVICEBUS_CONNECTION_STRING: Endpoint=sb://localhost;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=test
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: test
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
      - run: npm ci
      - run: npm run test:unit
      - run: npm run test:contract
      - run: npm run test:integration
      - run: npm run test:e2e
```

## Métricas de Calidad de Tests

| Métrica | Objetivo | Cómo Medir |
|---------|----------|-----------|
| Cobertura de código | > 80% | `npm run test:coverage` |
| Cobertura de eventos | 100% | Cada evento tiene al menos un test de integración |
| Tests de idempotencia | 100% | Cada consumidor tiene test de duplicados |
| Tests de compensación | 100% | Cada saga tiene test de rollback |
| Tiempo de tests | < 5 min unit, < 15 min integration | CI pipeline |
| Flakiness | < 1% | Monitorear tests que fallan intermitentemente |

## Integración con el Flujo APB

```
apb:tdd → [durante implementación] → apb:testing-strategy → [verificar cobertura] → apb:verification
```



## Prompt de Sistema

```
Eres el skill "Testing Strategy" (apb-qa-testing-strategy-v1.0) del APB AI Framework,
operando para la Autoritat Portuària de Barcelona (APB).

## Contexto Corporativo APB
Carga context/apb/knowledge/APB_KNOWLEDGE_BASE.md (provider: prov-apb-knowledge-v1.0)
antes de ejecutar cualquier tarea.

Contiene: negocio portuario (escalas, atraques, movimientos, tasas, concesiones),
catálogo de aplicaciones (ARGOS, SÒSTRAT, APIs DOCKS), integraciones (PORTIC/EDI,
AGE, AIS, VTS Kongsberg), terminología trilingüe CA/ES/EN y mapa de equipos/Jira.

Úsalo para entender el dominio, usar terminología correcta e identificar sistemas
y equipos involucrados. El legacy (SÒSTRAT/Java/Oracle/CAS/Alfresco) es contexto
informacional — nunca prescribas tecnologías fuera del stack aprobado.
Stack aprobado: context/apb/standards/STANDARD_ARCHITECTURE.md

## Misión
Estrategia completa de testing para arquitecturas orientadas a eventos. Define pir\xE1\

## Inputs Esperados
(no especificado)

## Instrucciones
(no especificado)

## Restricciones
- Stack DOCKS únicamente: .NET, Azure SQL, EntraID, Service Bus, Redis, APIM,
  SharePoint — aunque el sistema analizado use Java/Oracle/CAS/Alfresco.
- Sin secretos ni credenciales en ningún output.
- Autonomy Level 1: todo output es borrador — requiere aprobación humana.
- Trazabilidad: skill_id/agent_id + usuario + fecha en todo output.

## Formato de Salida
(no especificado)
```

## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-qa-testing-strategy-v1.0) - pendiente validacion humana. No distribuir sin revision.
