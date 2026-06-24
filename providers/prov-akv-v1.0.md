---
id: "prov-akv-v1.0"
name: "Provider: Azure Key Vault"
description: "Proveedor de secretos (tipo secret) para gestión centralizada de credenciales, claves y certificados. Es el único mecanismo autorizado para referenciar secretos desde skills, agentes y catálogos del framework — nunca en texto plano."
version: "1.0.0"
status: "draft"
owner: "Ciberseguridad <arquitectura@portdebarcelona.cat>"
domain: "security"
provider_type: "secret"
access_mode: "read-only"
created_date: "2026-06-24"
review_date: "2026-06-24"
---

# Provider: Azure Key Vault

---

## Descripción
Proveedor de secretos (tipo `secret`) para gestión centralizada de credenciales,
cadenas de conexión, claves de API y certificados usados por el framework. Es el
mecanismo autorizado por el Principio Fundamental #9 (`README.md`) para que skills,
agentes y wrappers referencien secretos sin incluirlos nunca en prompts, archivos
de catálogo o frontmatter.

> **Nota de gobernanza:** este provider cubre un gap de catálogo identificado en la
> Sesión 7. `apb-agent-business-analyst-v1.0` y el provider `prov-azure-v1.0` ya
> citaban `prov-akv-v1.0` como referencia antes de que existiera como componente
> formal.

## Capacidades
- Almacenamiento y rotación de secretos, claves y certificados
- Resolución de referencias `AKV://<secret-name>` en tiempo de ejecución
- Auditoría de accesos a secretos (quién, cuándo, qué secreto)
- Integración con Managed Identity de Azure (sin credenciales embebidas)

## Configuración
```json
{
  "provider_id": "prov-akv-v1.0",
  "type": "secret",
  "endpoint": "https://<vault-name>.vault.azure.net",
  "auth": "managed_identity",
  "scope": "read-only",
  "rate_limit": "2000 req/hour"
}
```

## Inputs
- `secret_reference`: nombre lógico del secreto (p. ej. `AKV://db-connection-string`)
- `action`: operación a ejecutar (`get_secret`, `list_versions`)

## Outputs
- `secret_value`: valor resuelto (nunca persistido fuera de la sesión de ejecución)
- `version`: versión del secreto recuperada
- `audit_entry`: registro de auditoría del acceso

## Dependencias
- `apb-agent-business-analyst-v1.0` (consumidor — referencia a secretos)
- `apb-agent-implementer-v1.0` (consumidor — configuración sensible en código)
- `prov-azure-v1.0` (relacionado — mismo entorno cloud)

## Restricciones
- Scope **read-only** por defecto; no crea ni elimina secretos desde el framework
- Ningún componente puede incluir el valor resuelto de un secreto en su salida
  persistida (markdown, catálogo, logs) — solo la referencia simbólica
- Acceso exclusivamente vía Managed Identity; no se admiten claves estáticas
- Toda resolución de secreto queda registrada en auditoría (Trazabilidad §3.4
  del proyecto)

## Ejemplo de Uso
```
Invocar: prov-akv-v1.0
Input: { secret_reference: "AKV://azure-sql-connection-string", action: "get_secret" }
Output: Valor resuelto en memoria de ejecución, no persistido; audit_entry registrado
```

---
*Registrado en APB AI Framework.*
