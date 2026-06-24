---
id: "prov-apb-knowledge-v1.0"
name: "Provider: Knowledge APB"
description: "Proveedor de conocimiento corporativo APB. Indexa y sirve estándares, políticas, plantillas, ADRs y documentación interna del framework."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
provider_type: "knowledge"
access_mode: "read-write"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Provider: Knowledge APB

---

## Descripción
Proveedor de conocimiento corporativo APB. Indexa y sirve estándares, políticas, plantillas, ADRs y documentación interna del framework.

## Capacidades
- Indexación de documentos corporativos
- Búsqueda semántica en estándares APB
- Recuperación de plantillas y políticas
- Grafos de conocimiento de relaciones entre componentes

## Configuración
```json
{
  "provider_id": "prov-apb-knowledge-v1.0",
  "type": "knowledge",
  "endpoint": "internal://apb-knowledge-base",
  "auth": "managed_identity",
  "index_path": "context/apb/",
  "rate_limit": "unlimited",
  "cache_ttl": "1h"
}
```

## Inputs
- `query`: consulta en lenguaje natural
- `category`: categoría (standards, policies, templates, adrs)
- `version`: versión del documento (opcional)

## Outputs
- `documents`: documentos relevantes
- `relationships`: relaciones entre componentes
- `version_history`: historial de versiones

## Dependencias
- `third-lightrag-knowledge-v1.0` (motor RAG)
- `apb-agent-catalog-manager-v1.0` (gestor)
- `apb-agent-governance-v1.0` (consumidor)

## Restricciones
- Solo documentos aprobados o en draft
- Datos clasificados requieren permisos adicionales
- Auditoría completa de consultas

## Ejemplo de Uso
```
Invocar: prov-apb-knowledge-v1.0
Input: { query: "estándar de nombres de microservicios", category: "standards" }
Output: Estándar APB de nomenclatura con ejemplos
```

---
*Registrado en APB AI Framework.*
