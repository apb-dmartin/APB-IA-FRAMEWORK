---
id: "apb-dev-implementation-patterns-v1.0"
name: "Implementation Patterns"
description: "Cat\xE1logo de patrones de implementaci\xF3n para microservicios orientados a eventos\
  \ con Azure Service Bus, CloudEvents y DevExpress. Usar como referencia durante\
  \ implementaci\xF3n."
version: "1.0.0"
status: "draft"
owner: "Desarrollo APB <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 1
consumed_by:
  - "apb-agent-implementer-v1.0"
created_date: "2026-06-20"
review_date: "2026-06-24"
---

> Procedencia: Adaptado de obra/superpowers (coding patterns) + wshobson/agents (microservices-patterns, backend-development) (licencia MIT).

# APB Implementation Patterns: Patrones de Implementación

## Visión General

Catálogo de patrones probados para implementar microservicios orientados a eventos dentro del APB AI Framework. Usar como referencia durante `apb:subagent-dev` o implementación manual.

**Stack:** Azure Service Bus | CloudEvents 1.0 + JSON | DevExpress + JavaScript puro

---

## Patrón 1: Event Producer (Productor de Eventos)

### Descripción
Publicar eventos de forma confiable usando outbox pattern.

### Implementación

```javascript
// src/orders/producers/order-created-producer.js
const { ServiceBusClient } = require('@azure/service-bus');
const { CloudEvent } = require('cloudevents');

class OrderCreatedProducer {
  constructor(connectionString, topicName, outboxRepository) {
    this.client = new ServiceBusClient(connectionString);
    this.sender = this.client.createSender(topicName);
    this.outboxRepository = outboxRepository;
  }

  async publish(orderData) {
    // 1. Crear evento CloudEvents
    const event = new CloudEvent({
      type: 'com.ejemplo.ordenes.order-created.v1',
      source: '/servicios/order-service',
      id: generateUUID(),
      time: new Date().toISOString(),
      datacontenttype: 'application/json',
      data: {
        orderId: orderData.id,
        customerId: orderData.customerId,
        items: orderData.items,
        total: orderData.total
      }
    });

    // 2. Guardar en outbox (misma transacción que guardar orden)
    await this.outboxRepository.save({
      id: event.id,
      type: event.type,
      payload: event.toJSON(),
      status: 'pending',
      createdAt: new Date()
    });

    return event;
  }

  async flushOutbox() {
    // 3. Publicar eventos pendientes de outbox
    const pendingEvents = await this.outboxRepository.getPending();

    for (const outboxEvent of pendingEvents) {
      try {
        await this.sender.sendMessages({
          body: outboxEvent.payload,
          contentType: 'application/cloudevents+json',
          applicationProperties: {
            'ce-specversion': '1.0',
            'ce-type': outboxEvent.type
          }
        });

        await this.outboxRepository.markAsPublished(outboxEvent.id);
      } catch (error) {
        console.error(`Error publicando evento ${outboxEvent.id}:`, error);
        // No marcar como publicado — se reintentará
      }
    }
  }

  async close() {
    await this.sender.close();
    await this.client.close();
  }
}
```

### Cuándo Usar
- Cualquier servicio que necesite publicar eventos
- Cuando se requiere garantía de entrega at-least-once

### Variantes
- **Immediate publish:** Sin outbox (solo para eventos no críticos)
- **Batch publish:** Agrupar múltiples eventos para mejor throughput

---

## Patrón 2: Event Consumer (Consumidor de Eventos)

### Descripción
Procesar eventos de forma idempotente con manejo de errores.

### Implementación

```javascript
// src/inventory/handlers/order-created-handler.js
const { ServiceBusClient, ProcessErrorArgs } = require('@azure/service-bus');

class OrderCreatedHandler {
  constructor(connectionString, topicName, subscriptionName, inventoryRepository, processedEventRepository) {
    this.client = new ServiceBusClient(connectionString);
    this.receiver = this.client.createReceiver(topicName, subscriptionName);
    this.inventoryRepository = inventoryRepository;
    this.processedEventRepository = processedEventRepository;
  }

  async start() {
    this.receiver.subscribe({
      processMessage: async (message) => {
        try {
          await this.handleMessage(message);
          await message.complete();
        } catch (error) {
          console.error('Error procesando mensaje:', error);

          if (this.isTransientError(error)) {
            await message.abandon();
          } else {
            await message.deadLetter({
              deadLetterReason: error.name,
              deadLetterErrorDescription: error.message
            });
          }
        }
      },
      processError: async (args) => {
        console.error('Error en el receptor:', args.error);
      }
    });
  }

  async handleMessage(message) {
    const event = JSON.parse(message.body);
    const eventId = event.id;

    // 1. Verificar idempotencia
    const alreadyProcessed = await this.processedEventRepository.exists(eventId);
    if (alreadyProcessed) {
      console.log(`Evento ${eventId} ya procesado, ignorando`);
      return;
    }

    // 2. Validar schema
    this.validateSchema(event);

    // 3. Procesar lógica de negocio
    await this.processBusinessLogic(event.data);

    // 4. Marcar como procesado
    await this.processedEventRepository.save({
      eventId,
      processedAt: new Date(),
      handler: 'OrderCreatedHandler'
    });
  }

  validateSchema(event) {
    const required = ['specversion', 'type', 'source', 'id', 'time'];
    for (const field of required) {
      if (!event[field]) {
        throw new Error(`Campo CloudEvents obligatorio faltante: ${field}`);
      }
    }

    if (event.specversion !== '1.0') {
      throw new Error(`Versión CloudEvents no soportada: ${event.specversion}`);
    }
  }

  async processBusinessLogic(data) {
    for (const item of data.items) {
      await this.inventoryRepository.reserve(item.productId, item.quantity);
    }
  }

  isTransientError(error) {
    // Errores transitorios: timeout, connection lost, etc.
    return error.code === 'ETIMEDOUT' || 
           error.code === 'ECONNRESET' ||
           error.message.includes('timeout');
  }

  async stop() {
    await this.receiver.close();
    await this.client.close();
  }
}
```

### Cuándo Usar
- Cualquier servicio que necesite consumir eventos
- Cuando se requiere procesamiento idempotente

### Variantes
- **Session consumer:** Para ordenamiento garantizado
- **Batch consumer:** Para mejor throughput

---

## Patrón 3: Saga Orchestrator (Orquestador de Saga)

### Descripción
Coordinar transacciones distribuidas con acciones compensatorias.

### Implementación

```javascript
// src/sagas/order-saga-orchestrator.js
class OrderSagaOrchestrator {
  constructor(eventPublisher, sagaRepository) {
    this.eventPublisher = eventPublisher;
    this.sagaRepository = sagaRepository;
  }

  async start(orderData) {
    const saga = await this.sagaRepository.create({
      id: generateUUID(),
      status: 'started',
      orderId: orderData.id,
      steps: [
        { name: 'reserve-inventory', status: 'pending', compensation: 'release-inventory' },
        { name: 'process-payment', status: 'pending', compensation: 'refund-payment' },
        { name: 'create-shipment', status: 'pending', compensation: 'cancel-shipment' }
      ],
      createdAt: new Date()
    });

    try {
      await this.executeStep(saga, 'reserve-inventory', orderData);
      await this.executeStep(saga, 'process-payment', orderData);
      await this.executeStep(saga, 'create-shipment', orderData);

      await this.sagaRepository.complete(saga.id);

      // Publicar evento de saga completada
      await this.eventPublisher.publish({
        type: 'com.ejemplo.sagas.order-saga-completed.v1',
        source: '/sagas/order-saga',
        data: { sagaId: saga.id, orderId: orderData.id }
      });
    } catch (error) {
      await this.compensate(saga);
      throw error;
    }

    return saga;
  }

  async executeStep(saga, stepName, data) {
    const step = saga.steps.find(s => s.name === stepName);

    // Publicar comando para ejecutar paso
    await this.eventPublisher.publish({
      type: `com.ejemplo.sagas.${stepName}.v1`,
      source: `/sagas/order-saga`,
      data: { sagaId: saga.id, orderId: data.id, ...data }
    });

    // Esperar respuesta (con timeout)
    const completed = await this.waitForStepCompletion(saga.id, stepName, { timeout: 30000 });

    if (!completed) {
      throw new Error(`Timeout en paso ${stepName} de saga ${saga.id}`);
    }

    await this.sagaRepository.updateStep(saga.id, stepName, 'completed');
  }

  async compensate(saga) {
    const completedSteps = saga.steps
      .filter(s => s.status === 'completed')
      .reverse(); // Compensar en orden inverso

    for (const step of completedSteps) {
      try {
        await this.eventPublisher.publish({
          type: `com.ejemplo.sagas.${step.compensation}.v1`,
          source: `/sagas/order-saga`,
          data: { sagaId: saga.id }
        });

        await this.sagaRepository.updateStep(saga.id, step.name, 'compensated');
      } catch (error) {
        console.error(`Error en compensación ${step.compensation}:`, error);
        // Las compensaciones DEBEN ser idempotentes y siempre exitosas
        // Si fallan, requiere intervención manual
      }
    }

    await this.sagaRepository.updateStatus(saga.id, 'compensated');
  }
}
```

### Cuándo Usar
- Transacciones distribuidas que requieren all-or-nothing
- Procesos de negocio multi-paso (reservas, pagos, envíos)

### Variantes
- **Choreography saga:** Sin orquestador central, eventos coordinan entre sí
- **Hybrid saga:** Orquestador + coreografía combinados

---

## Patrón 4: Circuit Breaker para Consumidores

### Descripción
Proteger el sistema de cascadas de fallos cuando un servicio downstream falla.

### Implementación

```javascript
// src/shared/circuit-breaker.js
class CircuitBreaker {
  constructor(options = {}) {
    this.failureThreshold = options.failureThreshold || 5;
    this.resetTimeout = options.resetTimeout || 30000;
    this.halfOpenMaxCalls = options.halfOpenMaxCalls || 3;

    this.state = 'CLOSED'; // CLOSED, OPEN, HALF_OPEN
    this.failures = 0;
    this.lastFailureTime = null;
    this.halfOpenCalls = 0;
  }

  async execute(operation) {
    if (this.state === 'OPEN') {
      if (Date.now() - this.lastFailureTime > this.resetTimeout) {
        this.state = 'HALF_OPEN';
        this.halfOpenCalls = 0;
        console.log('Circuit breaker: HALF_OPEN');
      } else {
        throw new Error('Circuit breaker is OPEN');
      }
    }

    try {
      const result = await operation();
      this.onSuccess();
      return result;
    } catch (error) {
      this.onFailure();
      throw error;
    }
  }

  onSuccess() {
    if (this.state === 'HALF_OPEN') {
      this.halfOpenCalls++;
      if (this.halfOpenCalls >= this.halfOpenMaxCalls) {
        this.state = 'CLOSED';
        this.failures = 0;
        console.log('Circuit breaker: CLOSED');
      }
    } else {
      this.failures = 0;
    }
  }

  onFailure() {
    this.failures++;
    this.lastFailureTime = Date.now();

    if (this.state === 'HALF_OPEN' || this.failures >= this.failureThreshold) {
      this.state = 'OPEN';
      console.log('Circuit breaker: OPEN');
    }
  }

  getState() {
    return {
      state: this.state,
      failures: this.failures,
      lastFailureTime: this.lastFailureTime
    };
  }
}

// Uso en consumidor
class ResilientConsumer {
  constructor(handler, circuitBreaker) {
    this.handler = handler;
    this.circuitBreaker = circuitBreaker;
  }

  async handle(message) {
    return this.circuitBreaker.execute(() => this.handler.handle(message));
  }
}
```

### Cuándo Usar
- Consumidores que llaman a servicios externos
- Cuando fallos transitorios pueden causar cascada

---

## Patrón 5: Read Model Projection (CQRS)

### Descripción
Mantener modelos de lectura optimizados a partir de eventos de dominio.

### Implementación

```javascript
// src/orders/projections/order-summary-projection.js
class OrderSummaryProjection {
  constructor(readModelRepository) {
    this.readModelRepository = readModelRepository;
  }

  async handle(event) {
    switch (event.type) {
      case 'com.ejemplo.ordenes.order-created.v1':
        await this.onOrderCreated(event.data);
        break;
      case 'com.ejemplo.ordenes.order-confirmed.v1':
        await this.onOrderConfirmed(event.data);
        break;
      case 'com.ejemplo.ordenes.order-cancelled.v1':
        await this.onOrderCancelled(event.data);
        break;
      case 'com.ejemplo.pagos.payment-completed.v1':
        await this.onPaymentCompleted(event.data);
        break;
    }
  }

  async onOrderCreated(data) {
    await this.readModelRepository.create({
      orderId: data.orderId,
      customerId: data.customerId,
      status: 'pending',
      total: data.total,
      itemCount: data.items.length,
      createdAt: new Date()
    });
  }

  async onOrderConfirmed(data) {
    await this.readModelRepository.update(data.orderId, {
      status: 'confirmed',
      confirmedAt: new Date()
    });
  }

  async onOrderCancelled(data) {
    await this.readModelRepository.update(data.orderId, {
      status: 'cancelled',
      cancelledAt: new Date(),
      cancellationReason: data.reason
    });
  }

  async onPaymentCompleted(data) {
    await this.readModelRepository.update(data.orderId, {
      paymentStatus: 'completed',
      paymentMethod: data.paymentMethod,
      paidAt: new Date()
    });
  }
}
```

### Cuándo Usar
- Queries complejas que no se pueden satisfacer con el event store
- Reportes y dashboards
- Búsquedas con múltiples criterios

---

## Patrón 6: DevExpress Event Grid (UI)

### Descripción
Mostrar eventos en tiempo real usando DevExpress DataGrid con JavaScript puro.

### Implementación

```javascript
// src/ui/event-monitor-grid.js
class EventMonitorGrid {
  constructor(containerId) {
    this.containerId = containerId;
    this.grid = null;
    this.eventSource = new EventSource('/api/events/stream');
  }

  init() {
    this.grid = $(`#${this.containerId}`).dxDataGrid({
      dataSource: [],
      columns: [
        { dataField: 'time', caption: 'Timestamp', dataType: 'datetime', format: 'yyyy-MM-dd HH:mm:ss' },
        { dataField: 'type', caption: 'Event Type', groupIndex: 0 },
        { dataField: 'source', caption: 'Source' },
        { dataField: 'status', caption: 'Status', 
          cellTemplate: (container, options) => {
            const color = options.value === 'processed' ? 'green' : 
                          options.value === 'failed' ? 'red' : 'orange';
            container.append(`<span style="color:${color}">${options.value}</span>`);
          }
        },
        { dataField: 'deliveryCount', caption: 'Retries' },
        { dataField: 'data', caption: 'Payload', 
          cellTemplate: (container, options) => {
            container.append(`<pre>${JSON.stringify(options.value, null, 2)}</pre>`);
          }
        }
      ],
      grouping: { autoExpandAll: false },
      sorting: { mode: 'multiple' },
      filterRow: { visible: true },
      searchPanel: { visible: true },
      paging: { pageSize: 50 },
      scrolling: { mode: 'virtual' }
    }).dxDataGrid('instance');

    this.eventSource.onmessage = (event) => {
      const data = JSON.parse(event.data);
      this.addEvent(data);
    };
  }

  addEvent(eventData) {
    const store = this.grid.getDataSource().store();
    store.insert(eventData);
    this.grid.refresh();
  }

  destroy() {
    this.eventSource.close();
  }
}
```

### Cuándo Usar
- Monitoreo de eventos en tiempo real
- Debugging de flujos de eventos
- Dashboards operacionales

---

## Anti-Patrones a Evitar

| Anti-Patrón | Problema | Solución |
|-------------|----------|----------|
| **Synchronous event publishing** | Bloquea el hilo de ejecución | Usar outbox + async flush |
| **No error handling in consumer** | Mensajes se pierden silenciosamente | Siempre try/catch + DLQ |
| **Tight coupling via shared DB** | Rompe autonomía de microservicios | Cada servicio tiene su propia DB |
| **Event payload too large** > 256KB | Límites de Service Bus | Referencias + API para detalles |
| **No schema validation** | Eventos corruptos rompen consumidores | Validar CloudEvents en handler |
| **Missing correlation IDs** | Imposible tracear transacciones | Incluir traceparent en cada evento |

## Integración con el Flujo APB

```
apb:subagent-dev → [necesita patrón] → apb:implementation-patterns → [referencia] → implementar
```


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Codigo generado** - primera linea del bloque: `// [IA-GEN] Generado por APB AI Framework (apb-dev-implementation-patterns-v1.0) - pendiente revision humana`
- **Commit** - prefijo `[ai-gen]` en el mensaje + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`
- **PR asociado** - label `ai-generated` en GitHub + footer en descripcion del PR
