---
id: "prov-github-v1.0"
name: "Provider: GitHub MCP"
description: "Proveedor de acción para interactuar con repositorios GitHub. Permite leer código, crear PRs, revisar issues y gestionar workflows."
version: "1.1.0"
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

## Acciones de lectura (evidencia automática)

Las consumen los agentes y skills que antes pedían al usuario el diff, el código
o el estado del CI (ver `context/apb/standards/EXTERNAL_EVIDENCE_STANDARD.md`).
No tienen gate humano: no modifican nada.

| Acción | Descripción |
|--------|-------------|
| `get_pull_request` / `get_pull_request_diff` | Metadatos, ficheros cambiados y diff de un PR |
| `read_file` / `list_directory` | Contenido y árbol de un repo en una rama o SHA |
| `list_commits` / `compare_refs` | Commits y diferencias entre dos refs (p. ej. entre tags de release) |
| `list_workflows` / `list_workflow_runs` | Definición y último estado del CI/CD (`.github/workflows/`) |

Las escrituras (`create_pr`, `comment`, ejecutar workflow) conservan su gate humano.

## Mecanismo en Claude Code

Servidor MCP remoto `github` registrado en `.mcp.json`
(`https://api.githubcopilot.com/mcp/`), con el token en la variable de usuario
`GITHUB_PERSONAL_ACCESS_TOKEN` (referencia `${...}`, nunca el valor en el repo).
Recomendado un PAT fine-grained de **solo lectura** sobre los repos APB. Si el
token no alcanza un repo, el componente consumidor declara la evidencia como no
disponible (regla R3 del estándar), no falla.

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

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-20 | Arquitectura APB | Creación inicial |
| 1.1.0 | 2026-11-20 | Claude (Anthropic), a petición de Débora | Acciones de lectura para evidencia automática y mecanismo MCP real en Claude Code (`.mcp.json`, PAT por variable de entorno) |

---
*Registrado en APB AI Framework.*
