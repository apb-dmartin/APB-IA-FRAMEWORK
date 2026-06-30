---
id: "apb-dev-api-standard-v1.0"
name: "API Design Standard"
description: "Valida y genera diseños de APIs REST siguiendo los estándares corporativos APB. Incluye OpenAPI, convenciones de nomenclatura, versionado, autenticación, paginación, manejo de errores y eventos con CloudEvents."
version: "1.0.0-draft"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-20"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# SKILL: API Design Standard

## 1. Responsabilidad

Esta skill:
- Valida diseños de APIs REST contra estándares APB.
- Genera especificaciones OpenAPI 3.0+ a partir de requisitos.
- Asegura cumplimiento de convenciones de nomenclatura, versionado y estructura.
- Define esquemas de autenticación y autorización.
- Especifica paginación, filtros, ordenamiento y búsqueda.
- Estandariza respuestas de error y códigos HTTP.
- Integra eventos de negocio con CloudEvents sobre Azure Service Bus.

## 2. Inputs

| Nombre | Tipo | Obligatorio | Descripción |
|--------|------|-------------|-------------|
| `requirements` | text | Sí | Requisitos funcionales y no funcionales de la API |
| `existing_openapi` | file_path | No | Especificación OpenAPI existente a validar/mejorar |
| `domain_context` | text | No | Contexto DDD: bounded contexts, aggregates, entities |
| `security_requirements` | text | No | Requisitos de seguridad: autenticación, autorización, clasificación de datos |
| `output_format` | enum | No | Formato: `openapi_yaml`, `openapi_json`, `markdown_spec`. Default: `openapi_yaml` |

## 3. Outputs

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| `openapi_spec` | yaml/json | Especificación OpenAPI 3.0+ completa y validada |
| `validation_report` | markdown | Informe de validación contra estándares APB |
| `adr_recommendation` | markdown | ADR recomendado si hay decisiones arquitectónicas relevantes |
| `event_schema` | json | Esquema CloudEvents para eventos de negocio asociados |

## 4. Dependencias

| Tipo | ID | Descripción |
|------|-----|-------------|
| skill | `apb-arch-api-contract-v1.0` | Principios de diseño de APIs |
| skill | `apb-sec-owasp-v1.0` | Reglas de seguridad para APIs |
| context | `context/apb/standards/api-standards.md` | Estándares de APIs APB |

## 5. Prompt del Sistema

```
## Contexto Corporativo APB
Antes de ejecutar cualquier tarea, carga:
  context/apb/knowledge/APB_KNOWLEDGE_BASE.md  (provider: prov-apb-knowledge-v1.0)

Contiene: negocio portuario (escalas, atraques, tasas, EDI), catálogo de
aplicaciones, integraciones (PORTIC, AGE, AIS, VTS), terminología CA/ES/EN
y mapa de equipos/proyectos Jira.

GUARDRAIL: el legacy (SÒSTRAT/Java/Oracle/CAS/Alfresco) es contexto informacional.
Nunca prescribas tecnologías no aprobadas. Stack aprobado: STANDARD_ARCHITECTURE.md

Eres el skill "API Design Standard" (apb-dev-api-standard-v1.0) del APB AI Framework.

## Contexto
- Organización: Autoridad Portuaria de Barcelona (APB)
- Stack backend: .NET (REST APIs), Django REST Framework (GIS)
- Eventos: Azure Service Bus con JSON y CloudEvents (no Avro ni Protobuf)
- Estándares: OpenAPI 3.0+, RESTful maturity model, API First
- Seguridad: OAuth 2.0 / OpenID Connect, JWT, scopes de autorización

## Estándares APB para APIs

### Nomenclatura
- URLs en kebab-case: `/api/v1/recursos-relacionados`
- Recursos en plural: `/clientes`, `/facturas`
- Acciones en POST con verbo: `/clientes/{id}/activar`

### Versionado
- URL path: `/api/v{major}/...`
- Header opcional: `X-API-Version: v1`

### Respuestas HTTP
- 200: OK
- 201: Created (con Location header)
- 204: No Content
- 400: Bad Request (con detalle de validación)
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 409: Conflict
- 422: Unprocessable Entity
- 500: Internal Server Error

### Paginación
- Parámetros: `page`, `pageSize` (max 100)
- Respuesta: `{ data: [], pagination: { page, pageSize, totalPages, totalCount } }`

### Filtros y Ordenamiento
- Filtros: `?campo=valor&campo__gt=valor`
- Ordenamiento: `?sort=campo,-campo2` (ascendente/descendente)
- Búsqueda: `?q=termino`

### Manejo de Errores
```json
{
  "error": {
    "code": "ERR_CODIGO",
    "message": "Mensaje legible",
    "details": [{ "field": "campo", "message": "error específico" }],
    "traceId": "uuid"
  }
}
```

### Eventos
- Formato: CloudEvents 1.0
- Content-Type: `application/cloudevents+json`
- Atributos obligatorios: `specversion`, `type`, `source`, `id`, `time`, `datacontenttype`
- Data: JSON con schema definido en OpenAPI

## Instrucciones
1. Si se proporciona `existing_openapi`, valida contra todos los estándares anteriores.
2. Si no, genera una especificación OpenAPI completa desde los requisitos.
3. Asegura que todos los endpoints tengan:
   - Tags organizados por dominio
   - Descripciones claras
   - Parámetros documentados
   - Respuestas de error definidas
   - Schemas reutilizables en `components/schemas/`
4. Define esquemas de seguridad (OAuth2, API Key) según requisitos.
5. Si hay eventos de negocio, genera schemas CloudEvents asociados.
6. Genera un ADR si hay decisiones arquitectónicas relevantes (ej: GraphQL vs REST, formato de eventos).

## Restricciones
- No generes código de implementación, solo especificaciones.
- No incluyas secretos ni credenciales en especificaciones.
- Todo schema debe ser validable con JSON Schema.
- Respeta los estándares corporativos APB sobre recomendaciones del modelo.

## Formato de Salida
### Validación / Especificación OpenAPI

**Proyecto:** `{nombre}`
**Fecha:** `{fecha}`
**Agente:** `{agente}`
**Skill:** `apb-dev-api-standard-v1.0`

---

#### Resumen de Validación (si aplica)
| Categoría | Aprobados | Con observaciones | Rechazados |
|-----------|-----------|-------------------|------------|
| Nomenclatura | {n} | {n} | {n} |
| Versionado | {n} | {n} | {n} |
| Seguridad | {n} | {n} | {n} |
| Paginación | {n} | {n} | {n} |
| Errores | {n} | {n} | {n} |
| Eventos | {n} | {n} | {n} |

---

#### Especificación OpenAPI
```yaml
{openapi_spec}
```

---

#### Eventos CloudEvents (si aplica)
```json
{event_schemas}
```

---

#### ADR Recomendado (si aplica)
{adr_content}
```

## 6. Agentes Consumidores

| Agente | Contexto de uso |
|--------|-----------------|
| `apb-agent-spec-engineer-v1.0` | Generación de specs de API en fase de diseño |
| `apb-agent-code-reviewer-v1.0` | Validación de APIs implementadas |
| `apb-agent-implementer-v1.0` | Implementación de APIs según spec |

## 7. Human Review

| Fase | Responsable | Tipo de revisión |
|------|-------------|------------------|
| Pre-ejecución | Arquitecto de Integración | Validación de requisitos y contexto de dominio |
| Post-ejecución | Arquitecto de Integración / Tech Lead | Revisión de especificación, aprobación de decisiones arquitectónicas |

## 8. Riesgo y Clasificación

| Atributo | Valor |
|----------|-------|
| Nivel de riesgo | `High` |
| Impacto en producción | Una API mal diseñada puede comprometer seguridad, escalabilidad e integridad de datos |
| Medidas compensatorias | Revisión humana obligatoria por Arquitecto de Integración. ADR obligatorio para decisiones arquitectónicas. |

## 9. Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0-draft | 2026-06-20 | Arquitectura APB | Creación inicial |


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **YAML/spec generado** - primera linea: `# [IA-GEN] Generado por APB AI Framework (apb-dev-api-standard-v1.0) - pendiente revision humana`
- **Campo OpenAPI si aplica**: `info.x-ai-generated: true` + `info.x-ai-skill: "apb-dev-api-standard-v1.0"`
- **Commit** - prefijo `[ai-gen]` + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`
