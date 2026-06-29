---
id: "apb-pm-parallel-execution-v1.0"
name: "Parallel Execution"
description: "Ejecuci\xF3n paralela de agentes para features independientes en arquitecturas orientadas\
  \ a eventos. Estrategias de file ownership, contratos de interfaz, y integraci\xF3\
  n de resultados."
version: "1.0.0"
status: "draft"
owner: "PMO APB <arquitectura@portdebarcelona.cat>"
domain: "pm"
autonomy_level: 1
consumed_by:
  - "apb-agent-spec-engineer-v1.0"
  - "apb-agent-pm-v1.0"
created_date: "2026-06-20"
review_date: "2026-06-24"
---

> Procedencia: Adaptado de wshobson/agents (parallel-feature-development + task-coordination-strategies) (licencia MIT). Contenido adaptado y
> generalizado para el APB AI Framework.

# APB Parallel Execution: Ejecución Paralela de Agentes

## Visión General

Ejecutar múltiples agentes en paralelo para acelerar el desarrollo de features independientes en arquitecturas orientadas a eventos. Cada agente trabaja en su propio contexto aislado con file ownership claro.

**Principio fundamental:** Paralelismo donde sea posible, secuencial donde sea necesario.

## Cuándo Usar

- Features que tocan servicios/microservicios independientes
- Tareas que no comparten estado ni dependencias
- Desarrollo de handlers de eventos para diferentes consumidores
- Implementación de proyecciones de read model (CQRS)
- Cuando el usuario dice "trabajar en paralelo" o "acelerar desarrollo"

## Cuándo NO Usar Paralelismo

- **Mismo servicio:** Dos agentes no pueden modificar el mismo microservicio
- **Mismo evento:** Productor y consumidor del mismo evento deben coordinarse
- **Saga compartida:** Pasos de saga dependen secuencialmente
- **Schema compartido:** Cambios de schema requieren consenso
- **Infraestructura compartida:** Configuración de Service Bus requiere coordinación

## Estrategias de File Ownership

### Por Servicio (Recomendada)

```
Agente 1: order-service/
  ├── src/
  │   ├── events/
  │   ├── handlers/
  │   ├── producers/
  │   └── services/
  └── tests/

Agente 2: inventory-service/
  ├── src/
  │   ├── events/
  │   ├── handlers/
  │   ├── producers/
  │   └── services/
  └── tests/

Agente 3: payment-service/
  ├── src/
  │   ├── events/
  │   ├── handlers/
  │   ├── producers/
  │   └── services/
  └── tests/
```

**Regla:** Cada servicio tiene un solo owner. No hay archivos compartidos entre servicios.

### Por Evento

```
Agente 1: OrderCreated (productor en order-service)
Agente 2: OrderCreated (consumidor en inventory-service)
Agente 3: OrderCreated (consumidor en payment-service)
```

**Regla:** El productor del evento es owner del schema. Los consumidores solo implementan handlers.

### Por Capa (Vertical Slice)

```
Agente 1: Feature "Reporte de órdenes"
  ├── order-query-service/ (endpoint + proyección)
  ├── DevExpress UI/ (grid + filtros)
  └── tests/

Agente 2: Feature "Notificaciones"
  ├── notification-service/ (handler + email)
  ├── DevExpress UI/ (panel de notificaciones)
  └── tests/
```

**Regla:** Cada feature es un vertical slice completo (backend + frontend + tests).

## Contratos de Interfaz

### Contrato de Evento (Schema)

Antes de que los agentes trabajen en paralelo, DEBEN acordar el schema:

```yaml
# conductor/contracts/order-created-v1.yaml
contract:
  event: "orders.order-created.v1"
  status: "frozen"  # frozen | draft | deprecated
  owner: "order-service"
  agreed_by: ["inventory-service", "payment-service", "shipping-service"]

  schema:
    specversion: "1.0"
    type: "com.ejemplo.ordenes.order-created.v1"
    data:
      orderId: { type: "string", required: true }
      customerId: { type: "string", required: true }
      items: { type: "array", required: true }
      total: { type: "number", required: true }
      timestamp: { type: "string", format: "date-time", required: true }

  constraints:
    - "items.length > 0"
    - "total > 0"
    - "timestamp <= now()"

  changes:
    - version: "v1.0"
      date: "2026-06-20"
      author: "Agente 1"
      description: "Versión inicial"
```

**Regla:** El schema se "congela" (frozen) antes de que los consumidores implementen. Cualquier cambio requiere renegociación.

### Contrato de API (REST)

```yaml
# conductor/contracts/order-api-v1.yaml
contract:
  service: "order-service"
  endpoint: "POST /orders"
  status: "frozen"
  owner: "order-service"
  consumers: ["frontend", "mobile-app"]

  request:
    customerId: { type: "string", required: true }
    items: { type: "array", required: true }
    idempotencyKey: { type: "string", required: true }

  response:
    201:
      body:
        orderId: { type: "string" }
        status: { type: "string", enum: ["pending"] }
        eventId: { type: "string", description: "ID del evento OrderCreated" }
    409:
      body:
        error: { type: "string" }
        code: { type: "string", enum: ["DUPLICATE_IDEMPOTENCY_KEY"] }
```

## Proceso de Ejecución Paralela

### Paso 1: Identificar Independencia

```
¿Pueden trabajar en paralelo?
  ├── ¿Tocan el mismo servicio? → NO
  ├── ¿Comparten schema sin acuerdo? → NO
  ├── ¿Son pasos de la misma saga? → NO
  ├── ¿Comparten infraestructura? → NO (con coordinación)
  └── SÍ → Paralelismo permitido
```

### Paso 2: Definir Contratos

```
Agente 1 (Productor) ←── Schema ──→ Agente 2 (Consumidor)
       ↓                                ↓
  [Implementa schema]           [Implementa handler]
  [Publica evento]              [Consume evento]
```

### Paso 3: Ejecutar en Paralelo

```
┌─────────────────────────────────────────────────────────────┐
│              Ejecución Paralela de Agentes                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Tiempo ──>                                                 │
│                                                             │
│  Agente 1:  [Schema]──[Productor]──[Tests]──[Commit]       │
│  Agente 2:  [Schema]──[Handler]──[Tests]──[Commit]         │
│  Agente 3:  [Schema]──[Handler]──[Tests]──[Commit]         │
│                                                             │
│  Leyenda:                                                   │
│  [Schema] = Lee contrato de schema (bloqueante, corto)     │
│  [Productor/Handler] = Implementación (paralelo)           │
│  [Tests] = Tests de integración (paralelo)                 │
│  [Commit] = Commit a rama compartida (secuencial)          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Paso 4: Integración

```bash
# Agente 1 commitea
 git add src/order-service/
 git commit -m "feat: implement OrderCreated producer"

 # Agente 2 commitea
 git add src/inventory-service/
 git commit -m "feat: implement OrderCreated consumer"

 # Agente 3 commitea
 git add src/payment-service/
 git commit -m "feat: implement OrderCreated consumer"

 # Integración
 git merge --no-ff agente-1
 git merge --no-ff agente-2
 git merge --no-ff agente-3

 # Tests de integración end-to-end
 npm run test:integration
```

## Conflictos y Resolución

### Conflicto de Schema

```
Agente 1 quiere añadir campo "priority" a OrderCreated
Agente 2 no esperaba ese campo

Resolución:
1. Congelar schema actual
2. Agente 1 propone cambio en conductor/contracts/
3. Agente 2 revisa impacto
4. Si aprobado: crear versión v1.1 del schema
5. Agente 2 actualiza handler para manejar v1.1
```

### Conflicto de Infraestructura

```
Agente 1 quiere crear topic "topic-orders-v2"
Agente 2 quiere modificar subscription "sub-inventory-service"

Resolución:
1. `apb-agent-platform-engineer-v1.0` (o humano) coordina cambios
2. Cambios se aplican en orden: topics primero, subscriptions después
3. Verificar que no hay downtime
```

## Métricas de Paralelismo

| Métrica | Objetivo | Cómo Medir |
|---------|----------|-----------|
| Speedup | > 1.5x vs secuencial | Tiempo secuencial / Tiempo paralelo |
| Conflictos | < 5% de archivos | Archivos con conflictos / Total archivos |
| Re-trabajo | < 10% de esfuerzo | Esfuerzo de corrección / Esfuerzo total |
| Integración | < 30 min | Tiempo desde último commit hasta tests verdes |

## Integración con el Flujo APB

```
[feature grande] → apb:task-breakdown → [tareas independientes] → apb:parallel-execution → [agentes en paralelo] → [integración]
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
  > **Borrador generado por IA** (APB AI Framework - apb-pm-parallel-execution-v1.0) - pendiente validacion humana. No distribuir sin revision.
