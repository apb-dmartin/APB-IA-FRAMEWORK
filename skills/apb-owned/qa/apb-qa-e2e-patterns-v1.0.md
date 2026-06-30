---
id: "apb-qa-e2e-patterns-v1.0"
name: "E2E Test Patterns"
description: "Plantillas y patrones de tests E2E para arquitecturas orientadas a eventos. Proporciona plantillas Playwright/Jest para flujos de eventos, casos de idempotencia, saga de compensacion y DLQ. Usar junto a apb-sub-qa-e2e-v1.0 (ejecutor) para generar la suite de tests de un feature concreto."
version: "1.0.0"
status: "draft"
owner: "QA APB <arquitectura@portdebarcelona.cat>"
domain: "qa"
autonomy_level: 1
consumed_by:
  - "apb-agent-qa-auto-v1.0"
replaces: "apb-qa-validation-e2e-v1.0"
created_date: "2026-06-30"
review_date: "2026-09-30"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

> ⚠️ Borrador generado por IA (APB AI Framework — apb-qa-e2e-patterns-v1.0) — pendiente validacion humana. No distribuir sin revision.

# APB E2E Test Patterns: Plantillas de Tests para Event-Driven


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Visión General

Proporcionar plantillas reutilizables para la generación de tests E2E en arquitecturas orientadas a eventos de APB. Esta skill ofrece los **patrones**; para la ejecución automatizada sobre un feature concreto, usar `apb-sub-qa-e2e-v1.0`.

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

### Paso 2: Selección de Plantilla

#### Plantilla A — Happy Path (flujo completo)

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

  test('flujo completo: [descripción]', async () => {
    const result = await apiClient.post('/[endpoint]', { /* datos */ });
    expect(result.status).toBe(201);

    const eventA = await eventMonitor.waitForEvent(
      'com.apb.[evento-a].v1',
      { timeout: 10000, filter: (e) => e.data.id === result.id }
    );
    expect(eventA).toBeDefined();
    expect(eventA.data).toMatchObject({ /* expected */ });

    const finalState = await apiClient.get(`/[resource]/${result.id}`);
    expect(finalState.status).toBe('[estado-final]');
  });

  afterAll(async () => {
    await eventMonitor.stop();
    await serviceBusClient.close();
  });
});
```

#### Plantilla B — Idempotencia

```javascript
test('evento duplicado no causa efectos secundarios', async () => {
  const testId = `idempotency-${Date.now()}`;
  const event = createTestEvent('[evento]', { testId });

  await publishEvent(event);
  await publishEvent(event); // duplicado intencional

  await waitFor(() => eventMonitor.getProcessedCount(testId) >= 1, { timeout: 10000 });

  const processedCount = await getProcessedEventCount(testId);
  expect(processedCount).toBe(1);

  const state = await apiClient.get(`/[resource]?testId=${testId}`);
  expect(state).toHaveLength(1);
});
```

#### Plantilla C — Compensación (Saga)

```javascript
test('compensación: [escenario de fallo]', async () => {
  const result = await apiClient.post('/[endpoint]', { /* datos */ });

  mockServiceFailure('[servicio]');

  const compensationEvent = await eventMonitor.waitForEvent(
    'com.apb.[compensacion].v1',
    { timeout: 30000 }
  );
  expect(compensationEvent).toBeDefined();

  const compensatedState = await apiClient.get(`/[resource]/${result.id}`);
  expect(compensatedState.status).toBe('compensated');
});
```

#### Plantilla D — Dead Letter Queue

```javascript
test('mensaje con error persistente va a DLQ', async () => {
  await configurePersistentFailure('[handler]');

  const event = createTestEvent('[evento]', { poison: true });
  await publishEvent(event);

  const dlqMessage = await waitForDLQMessage(
    '[topic]', '[subscription]',
    { timeout: 60000, filter: (m) => m.body.id === event.id }
  );
  expect(dlqMessage).toBeDefined();
  expect(dlqMessage.deliveryCount).toBeGreaterThanOrEqual(10);
  expect(dlqMessage.deadLetterReason).toBeDefined();
});
```

### Paso 3: Ejecución y Reporte

```bash
npm run test:e2e -- --feature=[nombre-feature]
npm run test:e2e:report
```

## Integración con el Flujo APB

```
apb-sub-dev → [impl. completa] → apb-qa-e2e-patterns-v1.0 (plantilla) + apb-sub-qa-e2e-v1.0 (ejecución) → apb:code-review
```

## ⚠️ Comportamiento ante inputs incompletos

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-qa-e2e-patterns-v1.0) - pendiente validacion humana. No distribuir sin revision.
