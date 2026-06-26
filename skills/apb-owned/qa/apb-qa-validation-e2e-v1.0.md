---
id: "apb-qa-validation-e2e-v1.0"
name: "Qa Validation"
description: "Validaci\xF3n de calidad y generaci\xF3n de tests E2E para arquitecturas orientadas\
  \ a eventos. Usar para verificar que features implementadas cumplen requisitos y\
  \ flujos de eventos funcionan end-to-end."
version: "1.0.0"
status: "draft"
owner: "QA APB <arquitectura@portdebarcelona.cat>"
domain: "qa"
autonomy_level: 1
consumed_by:
  - "apb-agent-qa-auto-v1.0"
created_date: "2026-06-20"
review_date: "2026-06-24"
---

> Procedencia: Adaptado de bmad-method (bmad-qa-generate-e2e-tests) + apb:testing-strategy (licencia MIT). Contenido adaptado y
> generalizado para el APB AI Framework.

# APB QA Validation: Validación de Calidad para Event-Driven

## Visión General

Generar y ejecutar tests de validación para features implementadas en arquitecturas orientadas a eventos. Enfocado en verificar que los flujos de eventos funcionan correctamente end-to-end, no solo en unit tests.

**Rol:** QA Automation Engineer especializado en event-driven testing.

## Cuándo Usar

- Después de completar implementación de una feature
- Antes de merge a main
- Cuando se necesita validar un flujo de eventos completo
- Para regresión de features existentes
- Cuando el usuario dice "validar calidad" o "generar tests E2E"

## El Proceso

### Paso 1: Análisis de la Feature

Revisar los artefactos de la feature:

```markdown
### Feature: [Nombre]

#### Eventos Involucrados
| Evento | Productor | Consumidor(es) | Schema |
|--------|-----------|---------------|--------|
| [Evento A] | [Servicio] | [Servicios] | [Versión] |
| [Evento B] | [Servicio] | [Servicios] | [Versión] |

#### Flujo de Negocio
1. [Actor] realiza [acción]
2. [Servicio] publica [Evento A]
3. [Servicio] consume [Evento A] y publica [Evento B]
4. ...

#### Criterios de Aceptación
- [CA 1]: [Descripción]
- [CA 2]: [Descripción]
- [CA 3]: [Descripción]

#### Casos de Error
- [Error 1]: [Descripción + comportamiento esperado]
- [Error 2]: [Descripción + comportamiento esperado]
```

### Paso 2: Generación de Tests E2E

#### Plantilla de Test E2E para Event-Driven

```javascript
// tests/e2e/[feature-name].e2e.test.js
describe('E2E: [Nombre del Feature]', () => {
  let serviceBusClient;
  let apiClient;
  let eventMonitor;

  beforeAll(async () => {
    serviceBusClient = new ServiceBusClient(process.env.SERVICEBUS_TEST_CONNECTION);
    apiClient = createApiClient(process.env.API_BASE_URL);
    eventMonitor = new EventMonitor(serviceBusClient);
    await eventMonitor.start();
  });

  // ====================
  // Happy Path
  // ====================
  test('flujo completo: [descripción]', async () => {
    // 1. Ejecutar acción inicial
    const result = await apiClient.post('/[endpoint]', {
      // datos de prueba
    });
    expect(result.status).toBe(201);

    // 2. Esperar y verificar eventos intermedios
    const eventA = await eventMonitor.waitForEvent(
      'com.ejemplo.[evento-a].v1',
      { timeout: 10000, filter: (e) => e.data.[id] === result.id }
    );
    expect(eventA).toBeDefined();
    expect(eventA.data).toMatchObject({ /* expected */ });

    // 3. Esperar eventos subsiguientes
    const eventB = await eventMonitor.waitForEvent(
      'com.ejemplo.[evento-b].v1',
      { timeout: 15000, filter: (e) => e.data.[relatedId] === eventA.data.[id] }
    );
    expect(eventB).toBeDefined();

    // 4. Verificar estado final
    const finalState = await apiClient.get(`/[resource]/${result.id}`);
    expect(finalState.status).toBe('[estado-final]');

    // 5. Verificar que no hay eventos inesperados
    const unexpectedEvents = eventMonitor.getEventsSince(startTime)
      .filter(e => !expectedEventTypes.includes(e.type));
    expect(unexpectedEvents).toHaveLength(0);
  });

  // ====================
  // Idempotencia
  // ====================
  test('evento duplicado no causa efectos secundarios', async () => {
    const testId = `idempotency-${Date.now()}`;

    // 1. Crear evento
    const event = createTestEvent('[evento]', { testId });

    // 2. Publicar dos veces
    await publishEvent(event);
    await publishEvent(event);

    // 3. Esperar procesamiento
    await waitFor(() => eventMonitor.getProcessedCount(testId) >= 1, { timeout: 10000 });

    // 4. Verificar que solo se procesó una vez
    const processedCount = await getProcessedEventCount(testId);
    expect(processedCount).toBe(1);

    // 5. Verificar estado final consistente
    const state = await apiClient.get(`/[resource]?testId=${testId}`);
    expect(state).toHaveLength(1);
  });

  // ====================
  // Compensación (Saga)
  // ====================
  test('compensación: [escenario de fallo]', async () => {
    // 1. Iniciar flujo
    const result = await apiClient.post('/[endpoint]', { /* datos */ });

    // 2. Simular fallo en paso intermedio
    mockServiceFailure('[servicio]');

    // 3. Esperar evento de compensación
    const compensationEvent = await eventMonitor.waitForEvent(
      'com.ejemplo.[compensacion].v1',
      { timeout: 30000 }
    );
    expect(compensationEvent).toBeDefined();

    // 4. Verificar que compensación se ejecutó
    const compensatedState = await apiClient.get(`/[resource]/${result.id}`);
    expect(compensatedState.status).toBe('compensated');

    // 5. Verificar estado de recursos liberados
    const resource = await apiClient.get('/[resource]/[id]');
    expect(resource.status).toBe('available');
  });

  // ====================
  // Dead Letter Queue
  // ====================
  test('mensaje con error persistente va a DLQ', async () => {
    // 1. Configurar handler para fallar siempre
    await configurePersistentFailure('[handler]');

    // 2. Enviar evento
    const event = createTestEvent('[evento]', { poison: true });
    await publishEvent(event);

    // 3. Esperar a que se mueva a DLQ
    const dlqMessage = await waitForDLQMessage(
      '[topic]', '[subscription]',
      { timeout: 60000, filter: (m) => m.body.id === event.id }
    );
    expect(dlqMessage).toBeDefined();
    expect(dlqMessage.deliveryCount).toBeGreaterThanOrEqual(10);

    // 4. Verificar que el mensaje tiene información de error
    expect(dlqMessage.deadLetterReason).toBeDefined();
    expect(dlqMessage.deadLetterErrorDescription).toBeDefined();
  });

  // ====================
  // Performance
  // ====================
  test('throughput: procesa [N] eventos en [T] segundos', async () => {
    const eventCount = 1000;
    const maxTime = 30000; // 30 segundos

    const startTime = Date.now();

    // 1. Publicar eventos en paralelo
    const events = Array.from({ length: eventCount }, (_, i) =>
      createTestEvent('[evento]', { sequence: i })
    );
    await Promise.all(events.map(e => publishEvent(e)));

    // 2. Esperar procesamiento completo
    await waitFor(
      () => eventMonitor.getProcessedCount() >= eventCount,
      { timeout: maxTime }
    );

    const elapsed = Date.now() - startTime;
    const throughput = eventCount / (elapsed / 1000);

    expect(elapsed).toBeLessThan(maxTime);
    expect(throughput).toBeGreaterThan(30); // > 30 eventos/segundo
  });

  // ====================
  // Ordenamiento (Sessions)
  // ====================
  test('ordenamiento: eventos del mismo sessionId en orden', async () => {
    const sessionId = `session-${Date.now()}`;
    const eventCount = 5;

    // 1. Publicar eventos en orden inverso
    for (let i = eventCount - 1; i >= 0; i--) {
      await publishEvent({
        ...createTestEvent('[evento]', { sequence: i }),
        sessionId
      });
    }

    // 2. Esperar procesamiento
    const processed = await waitForOrderedProcessing(sessionId, eventCount, { timeout: 15000 });

    // 3. Verificar orden
    const sequences = processed.map(e => e.data.sequence);
    expect(sequences).toEqual([0, 1, 2, 3, 4]);
  });

  afterAll(async () => {
    await eventMonitor.stop();
    await serviceBusClient.close();
  });
});
```

### Paso 3: Ejecución y Reporte

```bash
# Ejecutar tests E2E
npm run test:e2e -- --feature=[nombre-feature]

# Generar reporte
npm run test:e2e:report
```

**Reporte de QA:**

```markdown
## QA Validation Report: [Feature]

### Resumen
- **Tests ejecutados:** [N]
- **Pasaron:** [N]
- **Fallaron:** [N]
- **Skipped:** [N]

### Cobertura de Eventos
| Evento | Happy Path | Idempotencia | Error | Performance |
|--------|-----------|-------------|-------|-------------|
| [Evento A] | ✅ | ✅ | ✅ | ✅ |
| [Evento B] | ✅ | ✅ | ☐ | ✅ |

### Issues Encontrados
| Severidad | Descripción | Test Fallido |
|-----------|-------------|-------------|
| [Critical/High/Medium/Low] | [Descripción] | [Nombre del test] |

### Recomendación
[Ready for merge / Needs fixes / Blocked]
```

## Integración con el Flujo APB

```
apb:subagent-dev → [implementación completa] → apb:qa-validation → [reporte QA] → apb:code-review
```


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-qa-validation-e2e-v1.0) - pendiente validacion humana. No distribuir sin revision.
