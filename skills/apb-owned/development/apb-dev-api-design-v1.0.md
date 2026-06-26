---
id: "apb-dev-api-design-v1.0"
name: "Api Design"
description: "Dise\xF1o de APIs REST y de eventos para microservicios del APB AI Framework. Incluye\
  \ dise\xF1o de endpoints, contratos de eventos, y documentaci\xF3n OpenAPI/AsyncAPI."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 1
consumed_by:
  - "apb-agent-technical-architect-v1.0"
created_date: "2026-06-20"
review_date: "2026-06-24"
---

> Procedencia: Adaptado de anthropics/skills (claude-api + frontend-design patterns) (licencia MIT).

# APB API Design: Diseño de APIs y Contratos de Eventos

## Visión General

Diseño de APIs REST para microservicios y contratos de eventos para arquitecturas orientadas a eventos. Incluye documentación OpenAPI para APIs síncronas y AsyncAPI para eventos asíncronos.

## Cuándo Usar

- Diseñar nuevos endpoints REST para microservicios
- Definir contratos de eventos (schemas CloudEvents)
- Documentar APIs existentes
- Revisar diseños de API propuestos
- Cuando el usuario dice "diseñar API" o "definir contrato de evento"

## Principios de Diseño de API

### 1. APIs REST para Comandos

```yaml
# openapi.yaml — API de OrderService
openapi: 3.0.3
info:
  title: APB Order Service API
  version: 1.0.0
  description: API REST para gestión de órdenes

paths:
  /orders:
    post:
      summary: Crear orden
      description: |
        Crea una nueva orden y publica evento OrderCreated.
        Usa outbox pattern para garantizar consistencia.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateOrderRequest'
      responses:
        '201':
          description: Orden creada exitosamente
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrderResponse'
          headers:
            X-Event-ID:
              description: ID del evento OrderCreated publicado
              schema:
                type: string
        '400':
          description: Request inválido
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '409':
          description: Conflicto (idempotencia key duplicado)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'

  /orders/{orderId}:
    get:
      summary: Obtener orden
      description: Lee de proyección de read model (CQRS)
      parameters:
        - name: orderId
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Orden encontrada
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrderResponse'
        '404':
          description: Orden no encontrada

    put:
      summary: Actualizar orden
      description: |
        Actualiza orden y publica evento OrderUpdated.
        Versión optimista con ETag.
      parameters:
        - name: orderId
          in: path
          required: true
          schema:
            type: string
        - name: If-Match
          in: header
          required: true
          description: ETag de la versión actual
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateOrderRequest'
      responses:
        '200':
          description: Orden actualizada
        '412':
          description: Precondition failed (versión obsoleta)

  /orders/{orderId}/cancel:
    post:
      summary: Cancelar orden
      description: |
        Inicia compensación de saga.
        Publica evento OrderCancelled.
      parameters:
        - name: orderId
          in: path
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                reason:
                  type: string
      responses:
        '202':
          description: Cancelación aceptada (procesamiento asíncrono)
          content:
            application/json:
              schema:
                type: object
                properties:
                  sagaId:
                    type: string
                    description: ID de la saga de compensación

components:
  schemas:
    CreateOrderRequest:
      type: object
      required: [customerId, items]
      properties:
        customerId:
          type: string
          description: ID del cliente
        items:
          type: array
          items:
            type: object
            properties:
              productId:
                type: string
              quantity:
                type: integer
                minimum: 1
        idempotencyKey:
          type: string
          description: Clave de idempotencia (UUID v4)

    OrderResponse:
      type: object
      properties:
        id:
          type: string
        customerId:
          type: string
        status:
          type: string
          enum: [pending, confirmed, paid, shipped, delivered, cancelled]
        items:
          type: array
          items:
            $ref: '#/components/schemas/OrderItem'
        total:
          type: number
        createdAt:
          type: string
          format: date-time
        version:
          type: integer
          description: Versión optimista para concurrencia

    ErrorResponse:
      type: object
      properties:
        error:
          type: string
        code:
          type: string
        details:
          type: string
        traceId:
          type: string
```

### 2. AsyncAPI para Eventos

```yaml
# asyncapi.yaml — Contratos de Eventos
asyncapi: 2.6.0
info:
  title: APB Event Contracts
  version: 1.0.0
  description: Contratos de eventos del APB AI Framework

servers:
  production:
    url: sb-apb-prod.servicebus.windows.net
    protocol: servicebus
    protocolVersion: "1.0"
    description: Azure Service Bus Production

channels:
  orders/order-created:
    publish:
      message:
        $ref: '#/components/messages/OrderCreated'
    subscribe:
      message:
        $ref: '#/components/messages/OrderCreated'
    bindings:
      servicebus:
        topic: topic-orders
        subscription: sub-inventory-service

  orders/order-confirmed:
    publish:
      message:
        $ref: '#/components/messages/OrderConfirmed'

  inventory/reservation-confirmed:
    publish:
      message:
        $ref: '#/components/messages/InventoryReserved'

  payments/payment-completed:
    publish:
      message:
        $ref: '#/components/messages/PaymentCompleted'

components:
  messages:
    OrderCreated:
      name: OrderCreated
      contentType: application/cloudevents+json
      payload:
        $ref: '#/components/schemas/CloudEvent'
      examples:
        - payload:
            specversion: "1.0"
            type: "com.ejemplo.ordenes.order-created.v1"
            source: "/servicios/order-service"
            id: "a89b..."
            time: "2026-06-20T10:00:00Z"
            datacontenttype: "application/json"
            data:
              orderId: "ord-123"
              customerId: "cust-456"
              items:
                - productId: "prod-1"
                  quantity: 2
              total: 199.99

    OrderConfirmed:
      name: OrderConfirmed
      contentType: application/cloudevents+json
      payload:
        $ref: '#/components/schemas/CloudEvent'

    InventoryReserved:
      name: InventoryReserved
      contentType: application/cloudevents+json
      payload:
        $ref: '#/components/schemas/CloudEvent'

    PaymentCompleted:
      name: PaymentCompleted
      contentType: application/cloudevents+json
      payload:
        $ref: '#/components/schemas/CloudEvent'

  schemas:
    CloudEvent:
      type: object
      required: [specversion, type, source, id, time]
      properties:
        specversion:
          type: string
          enum: ["1.0"]
        type:
          type: string
          pattern: "^[a-zA-Z0-9]+\.[a-zA-Z0-9]+\.[a-zA-Z0-9-]+\.v[0-9]+$"
        source:
          type: string
          format: uri
        id:
          type: string
          format: uuid
        time:
          type: string
          format: date-time
        datacontenttype:
          type: string
          default: "application/json"
        data:
          type: object
        traceparent:
          type: string
          description: W3C Trace Context
        correlationid:
          type: string
          description: ID de correlación de saga
```

### 3. Diseño de Endpoints para Queries (CQRS)

```yaml
# openapi-queries.yaml — API de lectura (Read Model)
openapi: 3.0.3
info:
  title: APB Query API
  version: 1.0.0
  description: API de consulta optimizada para lectura

paths:
  /orders:
    get:
      summary: Listar órdenes
      description: Query optimizada con filtros y paginación
      parameters:
        - name: customerId
          in: query
          schema:
            type: string
        - name: status
          in: query
          schema:
            type: string
            enum: [pending, confirmed, paid, shipped, delivered, cancelled]
        - name: fromDate
          in: query
          schema:
            type: string
            format: date
        - name: toDate
          in: query
          schema:
            type: string
            format: date
        - name: page
          in: query
          schema:
            type: integer
            default: 1
        - name: pageSize
          in: query
          schema:
            type: integer
            default: 20
            maximum: 100
      responses:
        '200':
          description: Lista de órdenes
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/OrderSummary'
                  pagination:
                    $ref: '#/components/schemas/Pagination'

  /orders/{orderId}/timeline:
    get:
      summary: Timeline de eventos de orden
      description: Historial de eventos que afectaron la orden
      parameters:
        - name: orderId
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Timeline de eventos
          content:
            application/json:
              schema:
                type: object
                properties:
                  orderId:
                    type: string
                  events:
                    type: array
                    items:
                      type: object
                      properties:
                        timestamp:
                          type: string
                          format: date-time
                        type:
                          type: string
                        source:
                          type: string
                        data:
                          type: object

components:
  schemas:
    OrderSummary:
      type: object
      properties:
        id:
          type: string
        customerName:
          type: string
        status:
          type: string
        total:
          type: number
        itemCount:
          type: integer
        createdAt:
          type: string
          format: date-time
        lastEventAt:
          type: string
          format: date-time

    Pagination:
      type: object
      properties:
        page:
          type: integer
        pageSize:
          type: integer
        totalItems:
          type: integer
        totalPages:
          type: integer
        hasNext:
          type: boolean
        hasPrevious:
          type: boolean
```

## Convenciones de Naming

### Eventos CloudEvents

```
[empresa].[dominio].[accion].v[version]

Ejemplos:
- com.ejemplo.ordenes.order-created.v1
- com.ejemplo.pagos.payment-completed.v1
- com.ejemplo.inventario.reservation-confirmed.v1
- com.ejemplo.envios.shipment-created.v1
```

### Endpoints REST

```
/[recurso]          → Colección
/[recurso]/{id}     → Recurso específico
/[recurso]/{id}/[accion] → Acción sobre recurso

Ejemplos:
POST   /orders              → Crear orden
GET    /orders/{id}         → Obtener orden
PUT    /orders/{id}         → Actualizar orden
POST   /orders/{id}/cancel  → Cancelar orden
GET    /orders/{id}/timeline → Timeline de eventos
```

## Versionado de APIs

```yaml
# Estrategia de versionado

# URL Path (recomendada para major versions)
/api/v1/orders
/api/v2/orders

# Header (para minor versions)
Accept: application/json;version=1.1

# Deprecación
responses:
  '200':
    headers:
      Sunset:
        description: Fecha de deprecación
        schema:
          type: string
          example: "Sat, 31 Dec 2026 23:59:59 GMT"
      Deprecation:
        description: Versión deprecada
        schema:
          type: string
          example: "true"
```

## Integración con el Flujo APB

```
[diseño de feature] → apb:api-design → [openapi.yaml + asyncapi.yaml] → apb:document-processing
```


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **YAML generado** — primera línea: `# [IA-GEN] Generado por APB AI Framework (apb-dev-api-design-v1.0) — pendiente revisión humana`
- **Campo OpenAPI**: `info.x-ai-generated: true` + `info.x-ai-skill: "apb-dev-api-design-v1.0"`
- **Commit** — prefijo `[ai-gen]` + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`
- **PR asociado** — label `ai-generated` en GitHub
