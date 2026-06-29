---
id: "apb-arch-event-driven-master-v1.0"
name: "Event Driven"
description: "Skill maestro para arquitecturas orientadas a eventos con Azure Service Bus, CloudEvents\
  \ y microservicios. Usar al dise\xF1ar, implementar o refactorizar cualquier componente\
  \ event-driven."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "architecture"
autonomy_level: 1
consumed_by:
  - "apb-agent-technical-architect-v1.0"
created_date: "2026-06-20"
review_date: "2026-06-24"
---

> Procedencia: Creado desde cero + adaptado de wshobson/agents (microservices-patterns, saga-orchestration, cqrs-implementation, event-store-design) (licencia MIT).

# APB Event-Driven Architecture

Guía maestra para diseñar, implementar y operar arquitecturas orientadas a eventos dentro del APB AI Framework.

## Stack Tecnológico del APB

| Componente | Tecnología | Alternativas Rechazadas |
|------------|-----------|------------------------|
| **Broker de eventos** | Azure Service Bus | RabbitMQ, Kafka, AWS SQS |
| **Formato de schemas** | JSON + CloudEvents 1.0 | Avro, Protobuf, custom XML |
| **UI Framework** | DevExpress con JavaScript puro | React, TypeScript, Angular |
| **Patrón de comunicación** | Async (pub/sub) | Sync (REST/gRPC) como default |

## Cuándo Usar Este Skill

- Diseñar nuevos flujos de eventos
- Implementar productores o consumidores de eventos
- Configurar topología de Service Bus
- Diseñar sagas distribuidas
- Implementar CQRS con event sourcing
- Manejar dead letters y reintentos
- Versionar schemas de eventos
- Optimizar throughput y latencia

## Patrones Fundamentales

### 1. CloudEvents Specification

Todo evento DEBE seguir CloudEvents 1.0:

```json
{
  "specversion": "1.0",
  "type": "com.ejemplo.ordenes.order-created.v1",
  "source": "/servicios/orden-service",
  "id": "a89b...",
  "time": "2026-06-20T10:00:00Z",
  "datacontenttype": "application/json",
  "data": {
    "orderId": "ord-123",
    "customerId": "cust-456",
    "items": [...]
  }
}
```

**Campos obligatorios:**
- `specversion`: "1.0"
- `type`: namespace reverse + entidad + acción + versión
- `source`: URI que identifica el origen
- `id`: UUID único global
- `time`: timestamp ISO 8601

**Campos recomendados:**
- `datacontenttype`: "application/json"
- `traceparent`: para distributed tracing
- `correlationid`: para correlación de sagas

### 2. Topología de Azure Service Bus

```
Namespace: sb-apb-prod.servicebus.windows.net
│
├── Topics
│   ├── topic-orders
│   │   ├── sub-inventory-service (rule: type = 'orders.*')
│   │   ├── sub-payment-service   (rule: type = 'orders.order-created.*')
│   │   └── sub-shipping-service  (rule: type = 'orders.order-confirmed.*')
│   ├── topic-payments
│   │   ├── sub-order-service     (rule: type = 'payments.payment-completed.*')
│   │   └── sub-billing-service
│   └── topic-inventory
│       ├── sub-order-service     (rule: type = 'inventory.reservation-confirmed.*')
│       └── sub-alerting-service
│
└── Queues
    ├── q-orders-deadletter
    ├── q-payments-deadletter
    └── q-inventory-deadletter
```

**Configuración por Subscription:**
- Lock duration: 30s (default) o 5min para procesamiento largo
- Max delivery count: 10 (después → DLQ)
- Enable dead lettering on filter evaluation exceptions: true
- Enable dead lettering on message expiration: true
- Session: habilitar SOLO si se requiere ordenamiento estricto

### 3. Outbox Pattern

```javascript
// ✅ Implementación correcta del Outbox Pattern
async function createOrder(orderData) {
  const transaction = await db.beginTransaction();

  try {
    // 1. Guardar orden en DB
    const order = await orderRepository.create(orderData, { transaction });

    // 2. Guardar evento en outbox (misma transacción)
    await outboxRepository.create({
      id: generateUUID(),
      type: 'orders.order-created.v1',
      payload: {
        orderId: order.id,
        customerId: order.customerId,
        items: order.items
      },
      status: 'pending',
      createdAt: new Date()
    }, { transaction });

    await transaction.commit();

    // 3. Publicar evento (después del commit)
    await eventPublisher.publishFromOutbox();

    return order;
  } catch (error) {
    await transaction.rollback();
    throw error;
  }
}
```

**Anti-patrón:** Publicar evento ANTES de guardar en DB → riesgo de inconsistencia.

### 4. Idempotencia en Consumidores

```javascript
// ✅ Consumidor idempotente
class OrderCreatedHandler {
  async handle(event) {
    const eventId = event.id;

    // 1. Verificar si ya procesado
    const alreadyProcessed = await processedEventsRepository.exists(eventId);
    if (alreadyProcessed) {
      console.log(`Evento ${eventId} ya procesado, ignorando`);
      return; // Idempotencia: no hacer nada
    }

    // 2. Procesar evento
    await this.processBusinessLogic(event.data);

    // 3. Marcar como procesado (atomico con el procesamiento)
    await processedEventsRepository.save({
      eventId,
      processedAt: new Date(),
      handler: 'OrderCreatedHandler'
    });
  }
}
```

**Mecanismos de deduplicación:**
- **Tabla de eventos procesados**: más flexible, permite re-procesamiento controlado
- **Duplicate detection de Service Bus**: a nivel de broker, 5 minutos window
- **Idempotency key en payload**: el productor genera clave única de operación

### 5. Saga Patterns

#### Coreografía (Event Choreography)

```
OrderService          InventoryService      PaymentService
    |                       |                      |
    |-- OrderCreated ------> |                      |
    |                       |-- InventoryReserved -> |
    |                       |                      |-- PaymentProcessed
    |<-- OrderConfirmed -----|<-- PaymentCompleted -|
```

**Cuándo usar:** Flujos simples, pocos participantes, baja necesidad de visibilidad

#### Orquestación (Saga Orchestrator)

```javascript
class OrderSagaOrchestrator {
  async execute(orderData) {
    const saga = await this.sagaRepository.create({
      id: generateUUID(),
      status: 'started',
      steps: [
        { name: 'reserve-inventory', status: 'pending', compensation: 'release-inventory' },
        { name: 'process-payment', status: 'pending', compensation: 'refund-payment' },
        { name: 'create-shipment', status: 'pending', compensation: 'cancel-shipment' }
      ]
    });

    try {
      // Step 1
      await this.executeStep(saga, 'reserve-inventory', orderData);

      // Step 2
      await this.executeStep(saga, 'process-payment', orderData);

      // Step 3
      await this.executeStep(saga, 'create-shipment', orderData);

      await this.sagaRepository.complete(saga.id);
    } catch (error) {
      await this.compensate(saga);
      throw error;
    }
  }

  async compensate(saga) {
    const completedSteps = saga.steps
      .filter(s => s.status === 'completed')
      .reverse(); // Compensar en orden inverso

    for (const step of completedSteps) {
      await this.executeCompensation(saga, step);
    }
  }
}
```

**Cuándo usar:** Flujos complejos, muchos participantes, necesidad de visibilidad centralizada

### 6. Dead Letter Handling

```javascript
// ✅ Estrategia de manejo de DLQ
class DeadLetterHandler {
  async processDeadLetter(message) {
    const deadLetter = JSON.parse(message.body);

    // 1. Clasificar error
    const errorType = this.classifyError(deadLetter.error);

    switch (errorType) {
      case 'TRANSIENT':
        // Reintentar con backoff
        await this.scheduleRetry(deadLetter, { delay: this.calculateBackoff(deadLetter.deliveryCount) });
        break;

      case 'POISON':
        // Mensaje corrupto, alertar y archivar
        await this.alertPoisonMessage(deadLetter);
        await this.archiveMessage(deadLetter);
        break;

      case 'BUSINESS_LOGIC':
        // Error de negocio, requiere intervención manual
        await this.escalateToOperations(deadLetter);
        break;

      case 'SCHEMA_MISMATCH':
        // Versión de schema incompatible
        await this.handleSchemaMismatch(deadLetter);
        break;
    }
  }

  calculateBackoff(deliveryCount) {
    // Backoff exponencial: 1s, 2s, 4s, 8s, 16s, 32s, 64s, 128s, 256s, 512s
    return Math.min(Math.pow(2, deliveryCount) * 1000, 60000);
  }
}
```

### 7. Versionado de Schemas

**Estrategia: Event Type Versioning**

```
orders.order-created.v1   → Versión inicial
orders.order-created.v2   → Añade campo "priority"
orders.order-created.v3   → Cambia "items" de array a objeto
```

**Reglas de compatibilidad:**
- **Backward compatible**: consumidores viejos pueden leer eventos nuevos
- **Forward compatible**: consumidores nuevos pueden leer eventos viejos
- **Breaking change**: requiere nueva versión de evento

```javascript
// ✅ Schema con versionado
const OrderCreatedV2 = {
  specversion: "1.0",
  type: "com.ejemplo.ordenes.order-created.v2",
  // ... campos obligatorios CloudEvents
  data: {
    orderId: { type: "string", required: true },
    customerId: { type: "string", required: true },
    items: { type: "array", required: true },
    priority: { type: "string", enum: ["low", "normal", "high"], default: "normal" }, // Nuevo en v2
    // ...
  }
};

// Handler compatible con múltiples versiones
class OrderCreatedHandler {
  async handle(event) {
    const version = this.extractVersion(event.type); // "v2"

    switch (version) {
      case 'v1':
        return this.handleV1(event);
      case 'v2':
        return this.handleV2(event);
      default:
        throw new Error(`Versión no soportada: ${version}`);
    }
  }
}
```

### 8. Session Management (Ordenamiento)

```javascript
// ✅ Uso de sessions para ordenamiento garantizado
const receiver = serviceBusClient.createReceiver(topicName, subscriptionName, {
  receiveMode: "peekLock"
});

// El productor DEBE establecer sessionId
const message = {
  body: eventData,
  sessionId: event.data.customerId, // Ordenar por customer
  applicationProperties: {
    "traceparent": traceContext.traceparent
  }
};

await sender.sendMessages(message);
```

**Cuándo usar sessions:**
- Procesamiento ordenado por entidad (ej: orden de mensajes por customer)
- FIFO garantizado dentro de una session
- **Costo**: throughput limitado por session (un consumer por session)

### 9. CQRS con Event Sourcing

```javascript
// ✅ CQRS: Separación de comandos y queries
class OrderCommandHandler {
  async handleCreateOrder(command) {
    // 1. Validar comando
    await this.validateCommand(command);

    // 2. Generar eventos de dominio
    const event = new OrderCreatedEvent({
      orderId: command.orderId,
      customerId: command.customerId,
      items: command.items
    });

    // 3. Guardar en event store
    await this.eventStore.append(event);

    // 4. Publicar evento de integración
    await this.eventPublisher.publish(event.toCloudEvent());
  }
}

class OrderQueryHandler {
  async getOrderSummary(orderId) {
    // Leer de proyección optimizada (read model)
    return await this.orderProjectionRepository.get(orderId);
  }

  async getCustomerOrders(customerId) {
    // Query optimizada por índice
    return await this.orderProjectionRepository.findByCustomer(customerId);
  }
}
```

## Anti-Patrones Comunes

| Anti-Patrón | Problema | Solución |
|-------------|----------|----------|
| **Eventos como RPC** | Usar eventos para request/response síncrono | Usar REST/gRPC para sync, eventos solo para async |
| **Eventos gigantes** | Payloads > 256KB | Referencias a datos + API para detalles |
| **Sin idempotencia** | Procesamiento duplicado causa inconsistencia | Siempre implementar deduplicación |
| **Sin compensación** | Saga falla, datos quedan inconsistentes | Definir acciones compensatorias por cada paso |
| **Schema sin versión** | Cambios rompen consumidores | Versionar eventos (v1, v2, v3) |
| **DLQ ignorada** | Mensajes fallan silenciosamente | Monitorear DLQ, alertar, reintentar |
| **Sessions para todo** | Throughput severamente limitado | Usar sessions SOLO donde se requiere orden |
| **Outbox omitido** | Evento publicado pero DB falló | Siempre usar outbox pattern |


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-arch-event-driven-master-v1.0) - pendiente validacion humana. No distribuir sin revision.
