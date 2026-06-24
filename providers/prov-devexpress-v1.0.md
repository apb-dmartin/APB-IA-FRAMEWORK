---
id: "prov-devexpress-v1.0"
name: "Provider: DevExpress MCP"
description: "Proveedor de conocimiento para documentación de componentes DevExpress (DevExtreme, Blazor, XAF). Acceso a guías de uso, API reference y ejemplos de implementación."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
provider_type: "knowledge"
access_mode: "read-write"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Provider: DevExpress MCP

---

## Descripción
Proveedor de conocimiento para documentación de componentes DevExpress (DevExtreme, Blazor, XAF). Acceso a guías de uso, API reference y ejemplos de implementación.

## Capacidades
- Búsqueda en documentación DevExpress
- Recuperación de API reference por componente
- Ejemplos de código por escenario
- Notas de versión y breaking changes

## Configuración
```json
{
  "provider_id": "prov-devexpress-v1.0",
  "type": "knowledge",
  "endpoint": "https://docs.devexpress.com/api/",
  "auth": "api_key",
  "api_key_ref": "AKV://devExpress-docs-key",
  "rate_limit": "500 req/day",
  "cache_ttl": "12h"
}
```

## Inputs
- `component`: nombre del componente (ej: DataGrid, Chart)
- `framework`: framework objetivo (js, blazor, xaf)
- `query`: consulta específica

## Outputs
- `documentation`: documentación relevante
- `code_examples`: ejemplos de código
- `version_notes`: notas de versión

## Dependencias
- `apb-sub-dev-devexpress-v1.0` (consumidor principal)
- `apb-dev-devexpress-front-v1.0` (skill consumidora)

## Restricciones
- Requiere suscripción activa DevExpress
- API key gestionada en Azure Key Vault
- No descarga componentes, solo documentación

## Ejemplo de Uso
```
Invocar: prov-devexpress-v1.0
Input: { component: "DataGrid", framework: "js", query: "virtual scrolling" }
Output: Documentación y ejemplos de virtual scrolling
```

---
*Registrado en APB AI Framework.*
