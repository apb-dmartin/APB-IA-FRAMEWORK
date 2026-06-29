---
id: "prov-confluence-v1.0"
name: "Provider: Atlassian Confluence REST API"
description: "Proveedor de acción para operaciones estructurales directas sobre Atlassian Confluence: crear, actualizar y mover páginas, gestionar espacios, adjuntar archivos y controlar metadatos. Diferente de Rovo (AI-driven): este provider ofrece acceso estructural programático."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
provider_type: "action"
access_mode: "read-write"
created_date: "2026-06-29"
review_date: "2026-06-29"
---

# Provider: Atlassian Confluence REST API

## Descripción

Proveedor de acceso estructural directo a Atlassian Confluence mediante la REST API v2. A diferencia de Rovo (capa AI-driven de Atlassian), este provider opera a nivel de páginas, espacios y adjuntos de forma programática y determinista. Es el mecanismo para que agentes del framework publiquen documentación técnica, ADRs, runbooks y post-mortems directamente en los espacios Confluence de APB.

## Casos de Uso

- **Publicación de artefactos:** publicar documentación generada (ADRs, runbooks, informes de RCA, post-mortems) en el espacio Confluence correspondiente.
- **Actualización de wikis:** mantener actualizada la documentación técnica del framework sin intervención manual.
- **Gestión de espacios:** crear sub-páginas bajo una estructura de espacio predefinida.
- **Adjuntar evidencias:** subir archivos de evidencia (logs, capturas, informes) a páginas de incidencias o auditoría.

## Configuración

```json
{
  "provider_id": "prov-confluence-v1.0",
  "type": "action",
  "base_url": "AKV://confluence-base-url",
  "api_version": "v2",
  "auth_method": "oauth2",
  "oauth2_client_id": "AKV://confluence-oauth-client-id",
  "oauth2_client_secret": "AKV://confluence-oauth-client-secret",
  "auth_fallback": "api_token",
  "api_token": "AKV://confluence-api-token",
  "user_email": "AKV://confluence-service-account-email",
  "default_space_key": "APB",
  "rate_limit": "200 req/min (Atlassian Cloud standard)"
}
```

> **Nota de aprovisionamiento:**
> 1. Crear una OAuth 2.0 App en el Atlassian Developer Console con scopes: `read:confluence-content.all`, `write:confluence-content`, `read:confluence-space.summary`.
> 2. El API token es fallback para entornos sin OAuth2 configurado.
> 3. El `base_url` varía entre instancia cloud (`https://apb.atlassian.net/wiki`) y on-prem.
> 4. Todos los valores se almacenan en Azure Key Vault (`prov-akv-v1.0`).

## Acciones Disponibles

| Acción | Descripción | Permiso requerido |
|--------|-------------|-------------------|
| `get_page` | Obtiene el contenido de una página por ID o título | Read |
| `create_page` | Crea una página nueva en un espacio y padre especificados | Write |
| `update_page` | Actualiza el contenido de una página existente (por ID) | Write |
| `move_page` | Mueve una página a otro padre o espacio | Write |
| `delete_page` | Elimina una página (requiere confirmación humana) | Admin |
| `get_space` | Obtiene metadatos de un espacio Confluence | Read |
| `list_children` | Lista las páginas hijas de una página | Read |
| `attach_file` | Adjunta un archivo a una página | Write |
| `get_attachments` | Lista los adjuntos de una página | Read |
| `add_label` | Añade una etiqueta a una página | Write |

## Inputs

- `action`: nombre de la acción
- `page_id`: ID numérico de la página (para `get_page`, `update_page`, `move_page`, `delete_page`)
- `space_key`: clave del espacio Confluence (p. ej. `APB`, `TI`, `GOV`)
- `parent_id`: ID de la página padre (para `create_page`)
- `title`: título de la página (para `create_page` y `update_page`)
- `content`: contenido en formato Confluence Storage Format o Markdown (para `create_page` y `update_page`)
- `file_path`: ruta del fichero a adjuntar (para `attach_file`)
- `labels`: array de etiquetas (para `add_label`)

## Outputs

- `get_page`: objeto `{id, title, space_key, content, version, last_modified}`
- `create_page` / `update_page`: objeto `{id, title, url, version}`
- `list_children`: array de `{id, title, url}`
- `attach_file`: objeto `{attachment_id, filename, url}`

## Dependencias

- `prov-akv-v1.0` — todos los secretos de configuración se leen de Azure Key Vault
- `apb-agent-documentation-v1.0` — agente principal consumidor para publicación de artefactos
- apb-agent-knowledge-manager-v1.0 (planificado) — gestión de base de conocimiento en Confluence

## Restricciones

- Todos los secretos se leen de Azure Key Vault; nunca en texto plano en ningún fichero.
- `delete_page` requiere confirmación humana explícita antes de ejecutarse (autonomía nivel 1).
- El provider no puede gestionar permisos de espacio ni usuarios (fuera de su scope).
- El contenido publicado debe respetar las políticas de clasificación de información APB (no publicar datos personales ni credenciales en Confluence).
- Las páginas generadas por IA deben incluir la marca `ia-generado` como etiqueta Confluence.

## Ejemplo de Uso

```
Invocar: prov-confluence-v1.0
Action: create_page
SpaceKey: APB
ParentId: 123456
Title: "Post-Mortem INC-2026-0615 — Caída servicio de pagos"
Content: "[contenido en Confluence Storage Format]"
Labels: ["ia-generado", "post-mortem", "operaciones"]
→ {id: "789012", title: "Post-Mortem INC-2026-0615...", url: "https://apb.atlassian.net/wiki/..."}
```

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto publicado mediante este provider debe incluir marca de origen IA:

- **Páginas Confluence**: etiqueta `ia-generado` + nota al inicio de la página: *"Contenido generado por APB AI Framework — pendiente validación humana."*
- **Documentos Markdown** intermedios:
  > ⚠️ **Borrador generado por IA** (APB AI Framework — prov-confluence-v1.0) — pendiente validación humana. No distribuir sin revisión.
- **Commits**: prefijo `[ai-gen]` + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`.

---
*Documento generado por el APB AI Framework. Requiere revisión humana antes de aprobación.*
