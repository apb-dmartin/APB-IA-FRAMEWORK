---
id: "apb-plat-mcp-building-v1.0"
name: "Mcp Building"
description: "Gu\xEDa para construir MCP servers que expongan herramientas de monitoreo y operaci\xF3\
  n del APB AI Framework: m\xE9tricas de eventos, estado de Service Bus, gesti\xF3\
  n de DLQ, y control de sagas."
version: "1.0.0"
status: "draft"
owner: "Platform Engineering APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
consumed_by:
  - "apb-agent-platform-engineer-v1.0"
created_date: "2026-06-20"
review_date: "2026-06-24"
---

> Procedencia: Adaptado de anthropics/skills (mcp-builder) (licencia MIT).

# APB MCP Building: MCP Servers para Operaciones de Eventos

## Visión General

Construir MCP (Model Context Protocol) servers que expongan herramientas para monitorear y operar el APB AI Framework. Estos MCP servers permiten a los agentes del framework interactuar con Azure Service Bus, consultar métricas de eventos, gestionar dead letter queues, y controlar sagas.

**Principio fundamental:** Un buen MCP server mide su calidad por qué tan bien permite a los agentes realizar tareas operacionales del framework.

## Cuándo Usar

- Construir herramientas de monitoreo para operadores del framework
- Crear interfaces de gestión de eventos para agentes
- Implementar control de sagas vía MCP
- Desarrollar dashboards operacionales accesibles por agentes
- Cuando el usuario dice "crear MCP server" o "herramienta de monitoreo"

## MCP Servers del APB

### 1. MCP Server: Event Monitor

**Propósito:** Monitorear el flujo de eventos en tiempo real.

#### Herramientas (Tools)

```typescript
// tools/list-topics.ts
{
  name: "apb_list_topics",
  description: "Lista todos los topics de Azure Service Bus en el namespace APB",
  inputSchema: {
    type: "object",
    properties: {
      namespace: { type: "string", description: "Namespace de Service Bus (default: sb-apb-prod)" }
    }
  },
  handler: async ({ namespace = "sb-apb-prod" }) => {
    const topics = await serviceBusAdmin.listTopics(namespace);
    return {
      content: [{ type: "text", text: JSON.stringify(topics, null, 2) }]
    };
  }
}

// tools/get-subscription-metrics.ts
{
  name: "apb_get_subscription_metrics",
  description: "Obtiene métricas de una subscription: active messages, dead letter count, transfer count",
  inputSchema: {
    type: "object",
    properties: {
      topic: { type: "string", description: "Nombre del topic" },
      subscription: { type: "string", description: "Nombre de la subscription" },
      namespace: { type: "string", default: "sb-apb-prod" }
    },
    required: ["topic", "subscription"]
  },
  handler: async ({ topic, subscription, namespace }) => {
    const metrics = await serviceBusAdmin.getSubscriptionMetrics(namespace, topic, subscription);
    return {
      content: [{ type: "text", text: JSON.stringify(metrics, null, 2) }]
    };
  }
}

// tools/peek-dead-letter.ts
{
  name: "apb_peek_dead_letter",
  description: "Inspecciona mensajes en la dead letter queue sin eliminarlos",
  inputSchema: {
    type: "object",
    properties: {
      topic: { type: "string" },
      subscription: { type: "string" },
      maxMessages: { type: "number", default: 10 }
    },
    required: ["topic", "subscription"]
  },
  handler: async ({ topic, subscription, maxMessages }) => {
    const messages = await serviceBusAdmin.peekDeadLetterMessages(topic, subscription, maxMessages);
    return {
      content: [{ type: "text", text: JSON.stringify(messages, null, 2) }]
    };
  }
}

// tools/retry-dead-letter.ts
{
  name: "apb_retry_dead_letter",
  description: "Reintenta un mensaje de la dead letter queue (lo mueve de vuelta a la cola principal)",
  inputSchema: {
    type: "object",
    properties: {
      topic: { type: "string" },
      subscription: { type: "string" },
      messageId: { type: "string", description: "ID del mensaje a reintentar" }
    },
    required: ["topic", "subscription", "messageId"]
  },
  handler: async ({ topic, subscription, messageId }) => {
    await serviceBusAdmin.retryDeadLetterMessage(topic, subscription, messageId);
    return {
      content: [{ type: "text", text: `Mensaje ${messageId} reintentado exitosamente` }]
    };
  }
}
```

#### Recursos (Resources)

```typescript
// resources/event-catalog.ts
{
  uri: "apb://events/catalog",
  name: "Catálogo de Eventos APB",
  description: "Lista completa de eventos CloudEvents registrados en el framework",
  mimeType: "application/json",
  handler: async () => {
    const catalog = await eventCatalogService.getAllEvents();
    return {
      contents: [{ uri: "apb://events/catalog", mimeType: "application/json", text: JSON.stringify(catalog) }]
    };
  }
}

// resources/asyncapi-spec.ts
{
  uri: "apb://specs/asyncapi",
  name: "Especificación AsyncAPI",
  description: "Spec AsyncAPI completo de la arquitectura de eventos",
  mimeType: "application/yaml",
  handler: async () => {
    const spec = await asyncApiService.getSpec();
    return {
      contents: [{ uri: "apb://specs/asyncapi", mimeType: "application/yaml", text: spec }]
    };
  }
}
```

### 2. MCP Server: Saga Controller

**Propósito:** Controlar y monitorear sagas distribuidas.

#### Herramientas

```typescript
// tools/list-active-sagas.ts
{
  name: "apb_list_active_sagas",
  description: "Lista sagas activas con su estado actual",
  inputSchema: {
    type: "object",
    properties: {
      sagaType: { type: "string", description: "Filtrar por tipo de saga (opcional)" },
      status: { type: "string", enum: ["started", "completed", "compensating", "compensated", "failed"] }
    }
  },
  handler: async ({ sagaType, status }) => {
    const sagas = await sagaRepository.findActive({ sagaType, status });
    return {
      content: [{ type: "text", text: JSON.stringify(sagas, null, 2) }]
    };
  }
}

// tools/get-saga-details.ts
{
  name: "apb_get_saga_details",
  description: "Obtiene detalle completo de una saga incluyendo todos sus pasos",
  inputSchema: {
    type: "object",
    properties: {
      sagaId: { type: "string", description: "ID de la saga" }
    },
    required: ["sagaId"]
  },
  handler: async ({ sagaId }) => {
    const saga = await sagaRepository.getById(sagaId);
    return {
      content: [{ type: "text", text: JSON.stringify(saga, null, 2) }]
    };
  }
}

// tools/trigger-compensation.ts
{
  name: "apb_trigger_compensation",
  description: "Fuerza la compensación de una saga (uso de emergencia)",
  inputSchema: {
    type: "object",
    properties: {
      sagaId: { type: "string" },
      reason: { type: "string", description: "Razón de la compensación forzada" }
    },
    required: ["sagaId", "reason"]
  },
  handler: async ({ sagaId, reason }) => {
    await sagaOrchestrator.forceCompensate(sagaId, reason);
    return {
      content: [{ type: "text", text: `Compensación iniciada para saga ${sagaId}` }]
    };
  }
}
```

### 3. MCP Server: Schema Validator

**Propósito:** Validar schemas CloudEvents y detectar incompatibilidades.

#### Herramientas

```typescript
// tools/validate-event.ts
{
  name: "apb_validate_event",
  description: "Valida un evento contra el schema CloudEvents registrado",
  inputSchema: {
    type: "object",
    properties: {
      event: { type: "object", description: "Evento CloudEvents a validar" },
      strict: { type: "boolean", default: false, description: "Validación estricta (todos los campos requeridos)" }
    },
    required: ["event"]
  },
  handler: async ({ event, strict }) => {
    const result = await schemaValidator.validate(event, { strict });
    return {
      content: [{ type: "text", text: JSON.stringify(result, null, 2) }]
    };
  }
}

// tools/check-compatibility.ts
{
  name: "apb_check_schema_compatibility",
  description: "Verifica compatibilidad entre dos versiones de un schema",
  inputSchema: {
    type: "object",
    properties: {
      eventType: { type: "string" },
      fromVersion: { type: "string" },
      toVersion: { type: "string" }
    },
    required: ["eventType", "fromVersion", "toVersion"]
  },
  handler: async ({ eventType, fromVersion, toVersion }) => {
    const result = await schemaValidator.checkCompatibility(eventType, fromVersion, toVersion);
    return {
      content: [{ type: "text", text: JSON.stringify(result, null, 2) }]
    };
  }
}
```

## Principios de Diseño de MCP para APB

### Naming Convention

```
apb_[dominio]_[accion]_[objeto]

Ejemplos:
- apb_list_topics
- apb_get_subscription_metrics
- apb_peek_dead_letter
- apb_retry_dead_letter
- apb_list_active_sagas
- apb_trigger_compensation
- apb_validate_event
- apb_check_schema_compatibility
```

### Context Management

- Las herramientas DEBEN retornar datos estructurados (JSON)
- Incluir metadatos de paginación cuando aplique
- Limitar resultados por defecto (max 50 items)
- Soportar filtros para reducir datos

### Error Messages

```typescript
// ✅ BUENO: Error con contexto y sugerencia
{
  content: [{
    type: "text",
    text: JSON.stringify({
      error: "Subscription not found",
      details: "Topic 'topic-orders' does not have subscription 'sub-invalid'",
      suggestion: "Use apb_list_topics to see available topics and subscriptions",
      availableSubscriptions: ["sub-inventory-service", "sub-payment-service"]
    })
  }]
}

// ❌ MALO: Error genérico
{
  content: [{ type: "text", text: "Error: not found" }]
}
```

## Integración con el Flujo APB

```
[operador necesita información] → apb:mcp-building → [MCP server] → [agente consulta métricas]
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
  > **Borrador generado por IA** (APB AI Framework - apb-plat-mcp-building-v1.0) - pendiente validacion humana. No distribuir sin revision.
