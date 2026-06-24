---
id: "apb-arch-api-contract-v1.0"
name: "Diseño de Contratos API"
description: "Diseñar contratos API RESTful y de eventos que sean claros, versionados, seguros y alineados con los estándares corporativos de APB. Incluye definición de recursos, operaciones, esquemas, códigos de error y políticas de rate limiting."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "architecture"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Diseño de Contratos API

---

## 🎯 Propósito

Diseñar contratos API RESTful y de eventos que sean claros, versionados, seguros y alineados con los estándares corporativos de APB. Incluye definición de recursos, operaciones, esquemas, códigos de error y políticas de rate limiting.

---

## ⚡ Trigger

Al crear una nueva API, modificar una existente, o definir contratos de integración entre sistemas/microservicios.

---

## 📥 Input

- Requisitos funcionales del dominio
- Modelo de dominio (entities, aggregates)
- Consumidores conocidos de la API
- Requisitos de seguridad (autenticación, autorización)
- Requisitos de rendimiento (throughput, latencia)
- Estándares corporativos de API vigentes

---

## 📤 Output

- Especificación OpenAPI 3.0+ completa
- Esquemas de request/response con ejemplos
- Matriz de códigos de estado HTTP y errores
- Política de versioning
- Estrategia de autenticación/autorización
- Documentación de rate limits y throttling
- Contratos de eventos asociados (si aplica)

---

## 🔄 Proceso

1. **Identificación de recursos**: Mapear entidades de dominio a recursos REST (plurales, sustantivos).
2. **Definición de operaciones**: CRUD + operaciones específicas de dominio. Usar métodos HTTP semánticos.
3. **Diseño de URLs**: Estructura jerárquica, versionado en path (/v1/), filtros en query params.
4. **Diseño de esquemas**: Definir request/response bodies con JSON Schema. Incluir ejemplos válidos e inválidos.
5. **Manejo de errores**: Estandarizar formato de error (RFC 7807 Problem Details). Definir códigos por escenario.
6. **Seguridad**: Definir mecanismo de auth (OAuth 2.0, API Keys, MSI). Documentar scopes/roles.
7. **Versioning**: Estrategia (URL path vs header). Política de deprecación.
8. **Rate limiting**: Definir límites por consumidor, estrategia de throttling.
9. **Validación**: Revisar contra estándares APB. Verificar consistencia con otros APIs del ecosistema.
10. **Documentación**: Generar OpenAPI spec, markdown de referencia.

---

## 📋 Reglas y Constraints

- URLs en minúsculas, kebab-case, recursos en plural: `/api/v1/customer-orders`.
- NO usar verbos en URLs: `/api/v1/orders` (GET) en lugar de `/api/v1/getOrders`.
- Content-Type siempre `application/json` salvo casos específicos (file upload).
- Todos los errores deben seguir RFC 7807 (type, title, status, detail, instance).
- Campos de fecha en ISO 8601 (YYYY-MM-DDTHH:mm:ssZ).
- Paginación con cursor-based preferido sobre offset-based para grandes volúmenes.
- Incluir `X-Request-Id` en headers para trazabilidad.
- Versionado obligatorio en URL: `/api/v{major}/`.
- Documentar breaking changes y política de deprecación (mínimo 6 meses de aviso).
- Las APIs internas (microservicios) también deben tener contrato documentado.

---

## 🛠 Stack Tecnológico Relevante

- OpenAPI 3.0+
- JSON Schema
- Azure API Management
- OAuth 2.0 / Entra ID
- .NET 8/9 (Swashbuckle / NSwag)
- CloudEvents 1.0 (eventos asociados)

---

## 💡 Ejemplos de Uso

**Ejemplo 1 — API de Pedidos:**
> GET /api/v1/orders?status=pending&pageSize=20&cursor=abc123
> Response 200: { data: [...], pagination: { nextCursor: "xyz789", hasMore: true } }
> Error 404: { type: "https://api.apb.es/errors/order-not-found", title: "Order not found", status: 404, detail: "Order ID 12345 does not exist", instance: "/api/v1/orders/12345" }

**Ejemplo 2 — Evento asociado:**
> POST /api/v1/orders (crea pedido) → Emite evento `com.apb.orders.order-created.v1`
> El contrato del evento está vinculado al contrato de la API mediante correlation ID.

---

## 🔗 Dependencias

- `apb-dev-api-standard-v1.0` (estándares de implementación)
- `apb-arch-event-driven-v1.0` (eventos asociados)
- `apb-doc-swagger-v1.0` (documentación)
- `apb-sec-owasp-v1.0

---

## 📝 Notas

- Mantener un API catalog centralizado (Azure API Management) para descubrimiento.
- Para APIs públicas, considerar developer portal con sandbox.
- Revisar contratos con consumer-driven contract testing (Pact) cuando haya múltiples consumidores.

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*
