---
id: "prov-apb-knowledge-v1.0"
name: "Provider: Knowledge APB"
description: >
  Proveedor de conocimiento corporativo APB. Indexa y sirve dos capas de conocimiento:
  (1) estándares, políticas, plantillas y ADRs del framework DOCKS; y
  (2) contexto de negocio, funcional y tecnológico (incluyendo legacy) de la organización
  APB (context/apb/knowledge/APB_KNOWLEDGE_BASE.md). Los agentes deben usar la capa (2)
  para entender dominios y terminología, pero NUNCA para prescribir tecnologías no aprobadas.
version: "1.1.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
provider_type: "knowledge"
access_mode: "read-only"
created_date: "2026-06-20"
review_date: "2026-06-30"
knowledge_sources:
  framework:
    - "context/apb/standards/"
    - "context/apb/policies/"
    - "context/apb/templates/"
  business_context:
    - "context/apb/knowledge/APB_KNOWLEDGE_BASE.md"
---

# Provider: Knowledge APB

---

## Descripción

Proveedor de conocimiento corporativo APB. Indexa y sirve **dos capas de conocimiento** diferenciadas:

| Capa | Ruta | Uso |
|------|------|-----|
| **Framework / Estándares** | `context/apb/standards/`, `context/apb/policies/`, `context/apb/templates/` | Estándares aprobados, políticas obligatorias, plantillas — fuente de verdad para artefactos generados |
| **Contexto Corporativo** | `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` | Negocio portuario, sistemas existentes (incluyendo legacy), terminología, equipos, integraciones — solo contexto, nunca prescripción tecnológica |

> ⚠️ **Guardrail:** El contexto corporativo describe sistemas legacy (SÒSTRAT/Java/Oracle/CAS/Alfresco) para que los agentes entiendan tickets e integraciones. **Ningún agente puede usar ese contexto para recomendar o generar artefactos con tecnologías no aprobadas.**

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
