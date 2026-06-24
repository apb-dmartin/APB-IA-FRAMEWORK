---
id: "prov-github-v1.0"
name: "Provider: GitHub MCP"
description: "Proveedor de acción para interactuar con repositorios GitHub. Permite leer código, crear PRs, revisar issues y gestionar workflows."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
provider_type: "action"
access_mode: "read-write"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Provider: GitHub MCP

---

## Descripción
Proveedor de acción para interactuar con repositorios GitHub. Permite leer código, crear PRs, revisar issues y gestionar workflows.

## Capacidades
- Lectura de archivos y directorios de repositorios
- Creación y actualización de Pull Requests
- Comentarios en issues y PRs
- Ejecución de workflows de GitHub Actions
- Listado de commits y branches

## Configuración
```json
{
  "provider_id": "prov-github-v1.0",
  "type": "action",
  "endpoint": "https://api.github.com",
  "auth": "token",
  "token_ref": "AKV://github-token",
  "permissions": ["repo:read", "pull_requests:write", "issues:write"],
  "rate_limit": "5000 req/hour"
}
```

## Inputs
- `repo`: repositorio objetivo
- `action`: acción a ejecutar (read, create_pr, comment, etc.)
- `params`: parámetros específicos de la acción

## Outputs
- `result`: resultado de la acción
- `url`: URL al recurso creado/modificado
- `status`: estado de la operación

## Dependencias
- `apb-agent-implementer-v1.0` (consumidor)
- `apb-wf-code-review-v1.0` (workflow)
- `apb-sub-plat-ghactions-v1.0` (subagente)

## Restricciones
- Permisos read-only por defecto
- Escritura requiere aprobación explícita
- No accede a repositorios privados sin autorización
- Token gestionado en Azure Key Vault

## Ejemplo de Uso
```
Invocar: prov-github-v1.0
Input: { repo: "APB/legacy-app", action: "read_file", params: { path: "README.md" } }
Output: Contenido del archivo README.md
```

---
*Registrado en APB AI Framework.*
