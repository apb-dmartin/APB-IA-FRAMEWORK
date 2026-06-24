---
id: "apb-pm-sprint-planning-v1.0"
name: "Sprint Planning"
description: "Planificaci\xF3n de sprints especializada en historias orientadas a eventos. Genera\
  \ sprint-status.yaml con tracking de stories, eventos y dependencias entre microservicios."
version: "1.0.0"
status: "draft"
owner: "PMO APB <arquitectura@portdebarcelona.cat>"
domain: "pm"
autonomy_level: 1
consumed_by:
  - "apb-agent-spec-engineer-v1.0"
created_date: "2026-06-20"
review_date: "2026-06-24"
---

> Procedencia: Adaptado de bmad-method (bmad-sprint-planning) (licencia MIT). Contenido adaptado y
> generalizado para el APB AI Framework.

# APB Sprint Planning: Planificación de Sprints Orientados a Eventos

## Visión General

Planificación de sprints que organiza el trabajo en historias orientadas a eventos, con tracking de dependencias entre microservicios y visibilidad del flujo de eventos.

**Rol:** Developer / Scrum Master especializado en event-driven.

## Cuándo Usar

- Al inicio de cada sprint
- Cuando se necesita reorganizar prioridades
- Para tracking de progreso durante el sprint
- Cuando el usuario dice "planificar sprint" o "sprint planning"

## El Proceso

### Paso 1: Inventario de Stories

Analizar epics y extraer stories pendientes:

```yaml
# sprint-planning-input.yaml
epics:
  - id: EPIC-001
    name: "Flujo de orden completo"
    status: in-progress
    stories:
      - id: STORY-001
        name: "Publicar evento OrderCreated"
        status: completed
        event: "orders.order-created.v1"
        service: "order-service"
        points: 3
      - id: STORY-002
        name: "Consumir OrderCreated en InventoryService"
        status: in-progress
        event: "orders.order-created.v1"
        service: "inventory-service"
        points: 5
        depends_on: [STORY-001]
      - id: STORY-003
        name: "Publicar evento InventoryReserved"
        status: pending
        event: "inventory.reservation-confirmed.v1"
        service: "inventory-service"
        points: 3
        depends_on: [STORY-002]
      - id: STORY-004
        name: "Consumir InventoryReserved en PaymentService"
        status: pending
        event: "inventory.reservation-confirmed.v1"
        service: "payment-service"
        points: 5
        depends_on: [STORY-003]
```

### Paso 2: Detección de Dependencias

```
┌─────────────────────────────────────────────────────────────┐
│              Grafo de Dependencias de Stories                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   STORY-001 ──> STORY-002 ──> STORY-003 ──> STORY-004      │
│   (Productor)  (Consumidor)  (Productor)   (Consumidor)   │
│                                                             │
│   Reglas de dependencia:                                    │
│   - Productor debe completarse ANTES que consumidor       │
│   - Schema debe definirse ANTES que productor              │
│   - Infraestructura (topic) debe existir ANTES            │
│                                                             │
│   Ciclos detectados: [Ninguno / Listar ciclos]            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Paso 3: Asignación al Sprint

#### Criterios de Prioridad

1. **Dependencias:** Stories sin dependencias pendientes primero
2. **Valor de negocio:** Flujos críticos primero
3. **Riesgo técnico:** Stories con incertidumbre alta primero (fail fast)
4. **Eventos bloqueantes:** Eventos que bloquean a otros equipos primero

#### Capacidad del Sprint

```
Capacidad del equipo: [N] story points
Stories propuestas: [N] story points

Ajuste: [Añadir/Quitar stories para ajustar capacidad]
```

### Paso 4: Generación de Sprint Status

```yaml
# sprint-status.yaml
sprint:
  number: 3
  name: "Sprint 3: Flujo de orden y pago"
  start_date: "2026-06-20"
  end_date: "2026-07-03"
  capacity: 40
  committed: 38

  stories:
    - id: STORY-002
      name: "Consumir OrderCreated en InventoryService"
      status: in-progress
      assignee: "[developer]"
      points: 5
      event: "orders.order-created.v1"
      service: "inventory-service"
      depends_on: [STORY-001]
      blocked_by: []
      definition_of_done:
        - Handler implementado
        - Idempotencia funciona
        - Tests de integración pasan
        - DLQ configurada

    - id: STORY-003
      name: "Publicar evento InventoryReserved"
      status: pending
      assignee: "[developer]"
      points: 3
      event: "inventory.reservation-confirmed.v1"
      service: "inventory-service"
      depends_on: [STORY-002]
      blocked_by: [STORY-002]
      definition_of_done:
        - Schema CloudEvents definido
        - Productor implementado (outbox)
        - Tests de integración pasan

    - id: STORY-004
      name: "Consumir InventoryReserved en PaymentService"
      status: pending
      assignee: "[developer]"
      points: 5
      event: "inventory.reservation-confirmed.v1"
      service: "payment-service"
      depends_on: [STORY-003]
      blocked_by: [STORY-003]
      definition_of_done:
        - Handler implementado
        - Saga step definido
        - Compensación implementada
        - Tests de saga pasan

  metrics:
    total_events: 4
    events_completed: 1
    events_in_progress: 1
    events_pending: 2
    services_involved: ["order-service", "inventory-service", "payment-service"]

  risks:
    - description: "STORY-002 puede bloquear sprint si idempotencia es compleja"
      mitigation: "Spike técnico de 1 día antes de estimar"
      owner: "[tech-lead]"
```

### Paso 5: Visualización del Flujo

```
Sprint Board: Flujo de Eventos

┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   TO DO     │────>│  IN PROGRESS│────>│   REVIEW    │────>│    DONE     │
├─────────────┤     ├─────────────┤     ├─────────────┤     ├─────────────┤
│ STORY-003   │     │ STORY-002   │     │             │     │ STORY-001   │
│ (blocked)   │     │ (evento:    │     │             │     │ (evento:    │
│             │     │  OrderCreated│     │             │     │  OrderCreated│
│ STORY-004   │     │  en InvSvc) │     │             │     │  en OrdSvc) │
│ (blocked)   │     │             │     │             │     │             │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
       ▲                                            │
       └──────────── dependencias ──────────────────┘
```

### Paso 6: Métricas del Sprint

| Métrica | Objetivo | Actual |
|---------|----------|--------|
| Velocity | [N] pts/sprint | [N] pts |
| Event throughput | [N] msg/s | [N] msg/s |
| Test coverage | > 80% | [N]% |
| DLQ incidents | 0 | [N] |
| Sprint completion | 100% | [N]% |

## Integración con el Flujo APB

```
[epics definidos] → apb:sprint-planning → [sprint-status.yaml] → apb:subagent-dev
```
