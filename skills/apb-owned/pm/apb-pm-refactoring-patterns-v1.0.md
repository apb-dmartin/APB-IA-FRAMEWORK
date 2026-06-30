---
id: "apb-pm-refactoring-patterns-v1.0"
name: "Refactoring"
description: "Usar al refactorizar c\xF3digo en arquitecturas orientadas a eventos. Incluye refactorizaci\xF3\
  n de sagas, handlers de eventos, y migraci\xF3n de schemas."
version: "1.0.0"
status: "draft"
owner: "Desarrollo APB <arquitectura@portdebarcelona.cat>"
domain: "pm"
autonomy_level: 1
consumed_by:
  - "apb-agent-implementer-v1.0"
  - "apb-agent-pm-v1.0"
created_date: "2026-06-20"
review_date: "2026-06-24"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

> Procedencia: Adaptado de obra/superpowers (refactoring patterns) + wshobson/agents (code-refactoring) (licencia MIT). Contenido adaptado y
> generalizado para el APB AI Framework.

# APB Refactoring: Refactorización en Arquitecturas de Eventos


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Visión General

Refactorizar código en sistemas orientados a eventos requiere cuidado especial: los eventos son contratos públicos, los consumidores son muchos, y los cambios pueden romper flujos de negocio críticos.

**Principio fundamental:** Los eventos son contratos. Los contratos no se rompen sin plan.

## Cuándo Refactorizar

**Refactorizar cuando:**
- El código duplica lógica entre handlers de eventos
- Un servicio ha crecido demasiado (god service)
- Los schemas de eventos necesitan evolucionar
- La saga tiene pasos innecesarios o mal ordenados
- El throughput es insuficiente y requiere optimización
- Se migra de un patrón a otro (ej: coreografía → orquestación)

**NO refactorizar cuando:**
- Hay un bug activo en producción (arreglar primero)
- No hay tests de integración que cubran los eventos afectados
- No se ha comunicado el cambio a los equipos consumidores
- Es viernes por la tarde (regla de oro)

## Tipos de Refactorización en Event-Driven

### 1. Refactorización de Handlers de Eventos

#### Problema: Handler God Object

```javascript
// ❌ ANTES: Handler que hace demasiado
class OrderEventHandler {
  async handle(event) {
    // Validar
    // Guardar en DB
    // Publicar otros eventos
    // Enviar email
    // Actualizar cache
    // Escribir logs
    // ... 200 líneas más
  }
}
```

#### Solución: Pipeline de Procesamiento

```javascript
// ✅ DESPUÉS: Pipeline con pasos separados
class OrderEventHandler {
  constructor(pipeline) {
    this.pipeline = pipeline;
  }

  async handle(event) {
    const context = { event, metadata: {} };

    for (const step of this.pipeline) {
      await step.execute(context);
    }
  }
}

// Pasos individuales
class ValidationStep {
  execute(context) {
    validateSchema(context.event);
    validateBusinessRules(context.event.data);
  }
}

class PersistenceStep {
  async execute(context) {
    context.metadata.entity = await this.repository.save(context.event.data);
  }
}

class EventPublishingStep {
  async execute(context) {
    const followUpEvents = this.generateEvents(context.metadata.entity);
    for (const evt of followUpEvents) {
      await this.eventPublisher.publish(evt);
    }
  }
}

class NotificationStep {
  async execute(context) {
    await this.notificationService.send(context.event);
  }
}
```

### 2. Refactorización de Schemas de Eventos

#### Estrategia: Expand-Contract (Paralelo)

```javascript
// Paso 1: EXPAND — Añadir nuevo campo manteniendo compatibilidad
// Schema v1.1 (backward compatible)
const OrderCreatedV1_1 = {
  specversion: "1.0",
  type: "com.ejemplo.ordenes.order-created.v1",
  data: {
    orderId: { type: "string", required: true },
    customerId: { type: "string", required: true },
    items: { type: "array", required: true },
    priority: { type: "string", default: "normal" } // NUEVO — opcional
  }
};

// Productor publica v1.1 (consumidores v1.0 ignoran priority)
// Todos los consumidores siguen funcionando

// Paso 2: MIGRAR — Actualizar consumidores uno por uno
// Consumidor A actualizado para usar priority
// Consumidor B actualizado para usar priority
// ...

// Paso 3: CONTRACT — Hacer priority obligatorio (v2.0)
const OrderCreatedV2 = {
  specversion: "1.0",
  type: "com.ejemplo.ordenes.order-created.v2", // NUEVA VERSIÓN
  data: {
    orderId: { type: "string", required: true },
    customerId: { type: "string", required: true },
    items: { type: "array", required: true },
    priority: { type: "string", required: true } // AHORA OBLIGATORIO
  }
};
```

#### Reglas de Migración de Schemas

1. **Nunca modificar un evento ya publicado** — crear nueva versión
2. **Mantener consumidores de múltiples versiones** durante transición
3. **Documentar timeline de deprecación** (ej: "v1 deprecado en 3 meses")
4. **Monitorear consumidores que aún usan versiones viejas**

### 3. Refactorización de Sagas

#### Problema: Saga con pasos acoplados

```javascript
// ❌ ANTES: Saga con lógica de negocio mezclada
class OrderSaga {
  async execute(orderData) {
    const inventory = await this.reserveInventory(orderData);
    if (!inventory.success) {
      await this.releaseInventory(orderData); // Compensación inline
      throw new Error('Inventory unavailable');
    }

    const payment = await this.processPayment(orderData);
    if (!payment.success) {
      await this.releaseInventory(orderData); // Duplicado!
      await this.refundPayment(orderData); // Duplicado!
      throw new Error('Payment failed');
    }
    // ... más duplicación
  }
}
```

#### Solución: Saga con pasos declarativos

```javascript
// ✅ DESPUÉS: Saga con definición declarativa de pasos
class OrderSaga {
  constructor() {
    this.steps = [
      {
        name: 'reserve-inventory',
        action: () => this.inventoryService.reserve(orderData),
        compensation: () => this.inventoryService.release(orderData),
        retryPolicy: { maxRetries: 3, backoff: 'exponential' }
      },
      {
        name: 'process-payment',
        action: () => this.paymentService.process(orderData),
        compensation: () => this.paymentService.refund(orderData),
        retryPolicy: { maxRetries: 5, backoff: 'fixed' }
      },
      {
        name: 'create-shipment',
        action: () => this.shippingService.create(orderData),
        compensation: () => this.shippingService.cancel(orderData),
        retryPolicy: { maxRetries: 2, backoff: 'exponential' }
      }
    ];
  }

  async execute(orderData) {
    const completedSteps = [];

    try {
      for (const step of this.steps) {
        await this.executeWithRetry(step, orderData);
        completedSteps.push(step);
      }
    } catch (error) {
      await this.compensate(completedSteps.reverse(), orderData);
      throw error;
    }
  }

  async executeWithRetry(step, data) {
    // Lógica de retry centralizada
  }

  async compensate(steps, data) {
    for (const step of steps) {
      await step.compensation(data); // Centralizado, no duplicado
    }
  }
}
```

### 4. Refactorización de Topología de Service Bus

#### Problema: Un solo topic para todo

```
❌ ANTES: topic-all-events
  ├── sub-inventory (recibe TODO, filtra localmente)
  ├── sub-payment (recibe TODO, filtra localmente)
  └── sub-shipping (recibe TODO, filtra localmente)
```

#### Solución: Topics por dominio con filtros de Service Bus

```
✅ DESPUÉS: 
  topic-orders
  ├── sub-inventory-service (rule: type = 'orders.order-created.*')
  ├── sub-payment-service (rule: type = 'orders.order-confirmed.*')
  └── sub-shipping-service (rule: type = 'orders.order-paid.*')

  topic-payments
  ├── sub-order-service (rule: type = 'payments.payment-completed.*')
  └── sub-billing-service (rule: type = 'payments.payment-failed.*')
```

**Beneficios:**
- Menor tráfico de red (subscriptions reciben solo lo relevante)
- Mejor aislamiento de dominios
- Escalabilidad independiente por topic

### 5. Refactorización de DevExpress UI

#### Problema: Grid con lógica de eventos mezclada

```javascript
// ❌ ANTES: UI con lógica de negocio
$("#grid").dxDataGrid({
  onRowClick: (e) => {
    // Validar
    // Llamar API
    // Publicar evento
    // Actualizar grid
    // Mostrar notificación
  }
});
```

#### Solución: Separación de concerns

```javascript
// ✅ DESPUÉS: UI pura, lógica en servicio
class OrderGridController {
  constructor(orderService, eventBus) {
    this.orderService = orderService;
    this.eventBus = eventBus;
  }

  initGrid(containerId) {
    $(`#${containerId}`).dxDataGrid({
      onRowClick: (e) => this.handleRowClick(e.data)
    });
  }

  async handleRowClick(orderData) {
    try {
      await this.orderService.processOrder(orderData);
      this.eventBus.publish('ui.order-processed', { orderId: orderData.id });
    } catch (error) {
      this.eventBus.publish('ui.order-error', { error: error.message });
    }
  }
}

// Componente UI puro
class OrderGridView {
  constructor(controller) {
    this.controller = controller;
    this.eventBus.subscribe('ui.order-processed', (e) => {
      DevExpress.ui.notify(`Orden ${e.orderId} procesada`, 'success');
    });
    this.eventBus.subscribe('ui.order-error', (e) => {
      DevExpress.ui.notify(`Error: ${e.error}`, 'error');
    });
  }
}
```

## Checklist de Refactorización Segura

### Antes de Empezar
- [ ] Todos los tests de integración pasan
- [ ] Hay backup de la base de datos de eventos
- [ ] Se comunicó el cambio a equipos consumidores
- [ ] Se creó plan de rollback

### Durante la Refactorización
- [ ] Un cambio a la vez
- [ ] Tests verdes después de cada cambio
- [ ] No se modifican eventos ya publicados
- [ ] Se mantiene backward compatibility

### Después de la Refactorización
- [ ] Todos los tests pasan (unit + integration)
- [ ] Eventos fluyen correctamente end-to-end
- [ ] DLQ está limpia
- [ ] Performance no degradó
- [ ] Se actualizó documentación (AsyncAPI, diagrams)

## Integración con el Flujo APB

```
[detectar código que huele mal] → apb:refactoring → [plan de refactorización] → apb:subagent-dev
```



## Prompt de Sistema

```
Eres el skill "Refactoring" (apb-pm-refactoring-patterns-v1.0) del APB AI Framework,
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
Usar al refactorizar c\xF3digo en arquitecturas orientadas a eventos. Incluye refactorizaci\xF3\

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
  > **Borrador generado por IA** (APB AI Framework - apb-pm-refactoring-patterns-v1.0) - pendiente validacion humana. No distribuir sin revision.
