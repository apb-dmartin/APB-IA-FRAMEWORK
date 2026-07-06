---
id: "prov-atlassian-v1.0"
name: "Provider: Atlassian Jira (Software + Service Management) + Compass"
description: "Proveedor de acción unificado para Jira: Jira Software (backlog/epics/sprints de desarrollo, búsqueda JQL) y Jira Service Management (incidencias/service desk), más soporte ligero de Compass (catálogo de componentes). Fusiona lo que antes eran dos providers solapados (prov-atlassian-v1.0 + prov-jira-software-v1.0, ahora deprecado). Para Confluence, usar prov-confluence-v1.0 (dedicado, más completo). Distinto de adapter-rovo-v1.0 (capa de IA de Rovo — pendiente de activación en APB, julio 2026)."
version: "2.1.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
provider_type: "action"
access_mode: "read-write"
created_date: "2026-06-20"
review_date: "2026-07-06"
---

# Provider: Atlassian Jira (Software + JSM) + Compass

---

> **Nota de fusión (v2.0.0, 2026-07-06, a petición de Débora):** este provider
> absorbe `prov-jira-software-v1.0`, que quedaba **deprecado** (ver ese fichero).
> Los dos existían por separado desde el 2026-06-20/29 con capacidades solapadas
> — uno para JSM/Confluence/Compass, otro específicamente para Jira Software con
> mejor detalle de acciones (JQL). A petición de Débora se fusionan de verdad en
> un único provider. Ningún componente del framework usa MCP ni Rovo como
> transporte de este provider — es REST puro. La integración real de Rovo (capa
> de IA, búsqueda semántica, Rovo Agents) es `adapters/rovo/adapter-rovo-v1.0.md`,
> un componente aparte, pendiente de activación en el tenant Atlassian de APB
> (previsto julio 2026) — ver `## Relación con otros componentes Atlassian`.
>
> **Corrección v2.1.0 (misma sesión):** la v2.0.0 incluía también una tabla de
> acciones de Confluence, duplicando sin necesidad `prov-confluence-v1.0`
> (REST v2, OAuth2, ya existente desde el 2026-06-29 con acciones mucho más
> completas: `move_page`, `delete_page`, `get_space`, `list_children`,
> `attach_file`, `get_attachments`, `add_label`). Corregido: este provider ya no
> reclama Confluence — se delega enteramente en `prov-confluence-v1.0`.

## Descripción

Proveedor de acción unificado para integración REST con:
- **Jira Software** — backlog, epics, sprints, historias de desarrollo, búsqueda JQL
  (tableros Scrum/Kanban de proyectos de desarrollo, p. ej. `ARQ`).
- **Jira Service Management (JSM)** — incidencias, service desk, tickets de operaciones.
- **Compass** — soporte ligero de consulta/actualización de catálogo de componentes
  (`TENDER_APPS_PORTAL_DOCKS_v2.0.md`: "herramienta corporativa de gobierno técnico y
  catálogo de componentes"). No hay provider dedicado — se mantiene aquí mientras el
  uso real sea puntual; si crece, se puede separar en `prov-compass-v1.0` (pendiente) siguiendo el
  mismo patrón que `prov-confluence-v1.0`.

**Para Confluence, usar [`prov-confluence-v1.0`](prov-confluence-v1.0.md)** — provider
dedicado, con acciones más completas (páginas, espacios, adjuntos) que las que este
provider ofrecía antes de la corrección v2.1.0.

## Capacidades

### Jira (Software y Service Management)

| Acción | Descripción | Gate humano |
|--------|-------------|-------------|
| `get_issue` | Obtiene el detalle de una historia, epic, incidencia o subtarea por clave | No |
| `create_issue` | Crea una historia, epic, bug, incidencia o subtarea en un proyecto | No |
| `update_issue` | Actualiza campos de una issue (summary, description, priority, labels) | No |
| `transition_issue` | Mueve una issue a otro estado del workflow | No |
| `get_backlog` | Obtiene el backlog de un proyecto Jira Software con filtros de tipo/prioridad | No |
| `get_sprint` | Obtiene el contenido del sprint activo de un proyecto Jira Software | No |
| `add_to_sprint` | Mueve una issue al sprint especificado | **Sí** |
| `link_issues` | Crea un link entre dos issues (bloquea/es bloqueado por, relacionado con) | No |
| `add_comment` | Añade un comentario a una issue | No |
| `search_issues` | Busca issues mediante JQL (Jira Query Language) | No |

### Compass (ligero)

| Acción | Descripción | Gate humano |
|--------|-------------|-------------|
| `get_catalog_entry` | Consulta metadatos de un componente en el catálogo Compass | No |
| `update_catalog_entry` | Actualiza metadatos de un componente en el catálogo Compass | No |

## Relación con otros componentes Atlassian

| Componente | Qué hace | Cuándo usarlo |
|-----------|----------|---------------|
| `prov-atlassian-v1.0` (este) | CRUD REST + JQL sobre Jira (Software y JSM); Compass ligero | Gestionar tickets/incidencias/backlog, buscar precedentes con JQL |
| `prov-confluence-v1.0` | CRUD REST v2 sobre Confluence (páginas, espacios, adjuntos) — más completo | Publicar/actualizar documentación, ADRs, runbooks, post-mortems |
| `adapter-rovo-v1.0` | Capa de IA de Rovo: búsqueda semántica, resúmenes, Rovo Agents conversacionales | Razonar sobre contenido Atlassian, o exponer agentes del framework dentro de Jira/Confluence — **pendiente de activación en APB (julio 2026)** |

## Configuración

```json
{
  "provider_id": "prov-atlassian-v1.0",
  "type": "action",
  "base_url": "AKV://atlassian-base-url",
  "api_version": "v3",
  "auth_method": "api_token",
  "api_token": "AKV://atlassian-api-token",
  "user_email": "AKV://atlassian-service-account-email",
  "default_project_key": "APB",
  "rate_limit": "300 req/min (Atlassian Cloud standard — ajustar según plan)"
}
```

> **Nota de aprovisionamiento:**
> 1. Crear una cuenta de servicio dedicada en Atlassian Cloud con rol de **Project Member**
>    en los proyectos Jira relevantes.
> 2. Generar un API token desde la cuenta de servicio en `id.atlassian.com` → Security → API tokens.
> 3. El `base_url` es `https://apb.atlassian.net` para la instancia cloud de APB.
> 4. Todos los valores se almacenan en Azure Key Vault (`prov-akv-v1.0`).
> 5. **Runtime Claude Code:** si el tenant APB expone un servidor MCP de Atlassian, el
>    adapter de Claude puede invocar este provider a través de él en vez de REST directo
>    — ver `adapters/claude/adapter-claude-v1.0.md`. Ninguna de las dos vías cambia el
>    contrato de acciones documentado aquí.

## Inputs

- `action`: nombre de la acción (tabla de Capacidades)
- `issue_key`: clave de la issue (p. ej. `APB-123`, `ARQ-3684`) — para acciones sobre issues existentes
- `project_key`: clave del proyecto Jira (para `create_issue`, `get_backlog`)
- `issue_type`: tipo de issue (`Story`, `Epic`, `Bug`, `Subtask`, `Task`, `Incident`) — para `create_issue`
- `summary` / `description`: título y descripción (ADF o texto plano) — para `create_issue`/`update_issue`
- `priority`: `Highest`, `High`, `Medium`, `Low`, `Lowest`
- `labels`: array de etiquetas
- `jql`: query JQL para `search_issues` (p. ej. `project = ARQ AND type = Story AND sprint in openSprints()`)
- `sprint_id`: ID del sprint — para `add_to_sprint`
- `link_type`: `blocks`, `is blocked by`, `relates to` — para `link_issues`
- `component_id`: para acciones de Compass

## Outputs

- `get_issue`: `{key, summary, description, status, assignee, priority, labels, epic, sprint}`
- `create_issue` / `update_issue`: `{key, id, url}`
- `get_backlog`: array de `{key, summary, type, priority, storyPoints, epic}`
- `search_issues`: array de issues con los campos seleccionados
- `get_sprint`: `{id, name, state, startDate, endDate, issues[]}`
- `get_catalog_entry` / `update_catalog_entry`: metadatos del componente Compass

## Dependencias

- `prov-akv-v1.0` — todos los secretos de configuración se leen de Azure Key Vault
- `apb-gov-jira-evidence-v1.0` (skill)
- `apb-wf-sdd-full-v1.0` (workflow)
- `apb-agent-tech-debt-v1.0` (agente) — registra deuda técnica identificada como issues en Jira
- `apb-pm-jira-estimation-review-v1.0` (skill) — `search_issues`/JQL para precedentes de estimación

## Restricciones

- Token gestionado en Azure Key Vault (`prov-akv-v1.0`).
- Permisos limitados por proyecto.
- No elimina datos, solo crea/actualiza.
- Auditoría completa de cambios.
- `add_to_sprint` requiere confirmación humana para no alterar la planificación del sprint sin aprobación del equipo.
- Las issues creadas por IA deben incluir la etiqueta `ia-generado` y estar en estado `To Do` — nunca directamente en progreso.
- No puede modificar el workflow de estados (configuración de proyecto) — operación reservada al Jira Admin.
- No gestiona Confluence — usar `prov-confluence-v1.0`.

## Ejemplo de Uso

```
Invocar: prov-atlassian-v1.0
Action: search_issues
JQL: "project = ARQ AND type = Story AND status = Done ORDER BY resolved DESC"
→ [{key: "ARQ-3601", summary: "...", storyPoints: 5, ...}, ...]
```

```
Invocar: prov-atlassian-v1.0
Action: create_issue
ProjectKey: APB
IssueType: Task
Summary: "..."
→ { key: "APB-456", url: "https://apb.atlassian.net/browse/APB-456" }
```

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto creado mediante este provider debe incluir marca de origen IA:

- **Tickets Jira**: etiqueta `ia-generado` + footer en la descripción/comentario: *"Generado por APB AI Framework (prov-atlassian-v1.0) — pendiente revisión humana antes de planificar."*
- **Commits**: prefijo `[ai-gen]` + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-20 | Arquitectura APB | Creación inicial ("Atlassian Rovo MCP") |
| 1.1.0 | 2026-07-06 | Claude (Anthropic), a petición de Débora | Renombrado a "Atlassian REST API (JSM + Confluence + Compass)" — el nombre original inducía a confusión con MCP/Rovo sin relación real. Tabla de diferenciación con `prov-jira-software-v1.0` |
| 2.0.0 | 2026-07-06 | Claude (Anthropic), a petición de Débora | **Fusión** con `prov-jira-software-v1.0` (ahora deprecado): absorbe todas sus acciones (`get_issue`, `search_issues`/JQL, `add_to_sprint`, `link_issues`, etc.) |
| 2.1.0 | 2026-07-06 | Claude (Anthropic) | Corregido: la v2.0.0 duplicaba capacidades de Confluence ya cubiertas — mejor y de forma más completa — por `prov-confluence-v1.0` (existente desde el 2026-06-29). Este provider queda acotado a Jira (Software + JSM) + Compass ligero |

---
*Registrado en APB AI Framework.*
