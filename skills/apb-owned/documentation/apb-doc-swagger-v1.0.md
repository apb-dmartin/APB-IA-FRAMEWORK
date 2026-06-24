---
id: "apb-doc-swagger-v1.0"
name: "Generación de Documentación Swagger/OpenAPI"
description: "Generar documentación OpenAPI 3.0 (Swagger) a partir de especificaciones, código fuente o descripciones de API. Incluye schemas, ejemplos, códigos de respuesta, autenticación y validación contra estándares de diseño de API de APB."
version: "1.0.0"
status: "draft"
owner: "Desarrollo APB <arquitectura@portdebarcelona.cat>"
domain: "documentation"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Generación de Documentación Swagger/OpenAPI

## Propósito
Generar documentación OpenAPI 3.0 (Swagger) a partir de especificaciones, código fuente o descripciones de API. Incluye schemas, ejemplos, códigos de respuesta, autenticación y validación contra estándares de diseño de API de APB.

## Contexto de Uso
- Generación de specs OpenAPI para nuevas APIs.
- Actualización de documentación OpenAPI tras cambios en la API.
- Validación de que el código implementado cumple con el spec OpenAPI.
- Integración con pipelines CI/CD para generación automática de docs.

## Entradas Requeridas
| Entrada | Tipo | Descripción | Obligatorio |
|---------|------|-------------|-------------|
| `api_description` | Texto / Markdown | Descripción de la API, endpoints y funcionalidad | ✅ |
| `source_code` | Código / Texto | Código fuente de controllers/DTOs (para generación desde código) | ❌ |
| `existing_spec` | JSON / YAML | Spec OpenAPI existente a actualizar | ❌ |
| `auth_scheme` | Enum | `none`, `api-key`, `oauth2`, `bearer-jwt` | ❌ (default: bearer-jwt) |

## Flujo de Trabajo (Pasos)
1. **Análisis de la API**: Identificar recursos, endpoints, métodos HTTP, parámetros y responses.
2. **Diseño de schemas**: Definir modelos de datos con tipos, validaciones y ejemplos.
3. **Documentación de endpoints**: Para cada endpoint:
   - Path, método, tags, summary, description.
   - Parámetros: path, query, header, body.
   - Responses: códigos HTTP, schemas, ejemplos.
   - Seguridad: esquema de autenticación requerido.
4. **Generación de spec**: Crear archivo OpenAPI 3.0 en JSON o YAML.
5. **Validación de estándares**: Verificar que el spec cumple estándares de API de APB:
   - Versionado en path (`/api/v1/...`).
   - Uso consistente de HTTP verbs.
   - Códigos de error estandarizados.
   - Paginación, filtering, sorting documentados.
6. **Generación de ejemplos**: Incluir ejemplos de request/response para cada endpoint.
7. **Documentación adicional**: Descripción de flujos de autenticación, rate limiting, errores comunes.
8. **Registro de evidencia**: Metadatos para gobierno.

## Salida Esperada
### Archivos Generados
```
docs/api/
├── openapi.yaml (o openapi.json)
├── examples/
│   ├── request-examples.json
│   └── response-examples.json
└── README-api.md
```

### Estructura del README
```markdown
# Documentación API — [Nombre API]
> Versión: [X.Y.Z] | OpenAPI: 3.0.3 | Autor: Documentation Agent

## 1. Introducción
## 2. Autenticación
## 3. Endpoints
## 4. Schemas
## 5. Códigos de Error
## 6. Rate Limiting
## 7. Ejemplos
## 8. Changelog
## 9. Evidencia y Metadatos
```

## Criterios de Calidad
- [ ] Todos los endpoints documentados con métodos, parámetros y responses.
- [ ] Schemas con tipos, validaciones y ejemplos.
- [ ] Esquema de autenticación documentado.
- [ ] Códigos de error estandarizados y documentados.
- [ ] El spec es válido según OpenAPI 3.0 (puede validarse con Swagger Editor).
- [ ] El spec cumple estándares de diseño de API de APB.
- [ ] El README es comprensible para desarrolladores consumidores de la API.

## Stack y Tecnologías
- OpenAPI 3.0.3, Swagger UI, ReDoc
- Generación desde código: Swashbuckle (.NET), NSwag
- Validación: Swagger Editor, Spectral
- Formatos: YAML, JSON, Markdown

## Dependencias
- `apb-dev-api-standard-v1.0` — para estándares de diseño de API
- `apb-disc-spec-gen-v1.0` — para especificaciones funcionales
- `apb-gov-evidence-v1.0` — para evidencia de documentación

## Ejemplo de Uso
**Prompt de invocación:**
```
Genera la documentación OpenAPI para nuestro API de gestión de expedientes:
- Endpoints: GET /api/v1/expedientes, POST /api/v1/expedientes, GET /api/v1/expedientes/{id}, PUT /api/v1/expedientes/{id}, DELETE /api/v1/expedientes/{id}
- Auth: Bearer JWT (Azure AD)
- Schemas: Expediente, Documento, HistorialEstado
- Features: paginación, filtrado por estado, ordenación por fecha
- Ejemplos: incluir ejemplos de request/response en español
```

## Notas y Advertencias
- **Nivel 1**: El agente genera specs y documentación; no despliega Swagger UI ni modifica código.
- **Revisión humana obligatoria** antes de publicar la documentación como oficial.
- Los specs generados desde código requieren que el código esté actualizado y compilable.
- El agente no tiene acceso a entornos de ejecución; los ejemplos son ilustrativos.

## Historial de Cambios
| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-20 | Arquitectura APB | Creación inicial |
