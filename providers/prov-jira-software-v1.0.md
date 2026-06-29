---
id: "prov-jira-software-v1.0"
name: "Provider: Jira Software REST API"
description: "Proveedor de acción para Jira Software (proyectos de desarrollo de software): gestión de epics, historias, sprints y backlog. Diferente de prov-atlassian-v1.0 que cubre Jira Service Management (incidencias y service desk). Usado por agentes de desarrollo y gestión de proyectos."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
provider_type: "action"
access_mode: "read-write"
created_date: "2026-06-29"
review_date: "2026-06-29"
---

# Provider: Jira Software REST API

## Descripción

Proveedor de acceso a Jira Software mediante la Atlassian REST API v3. Cubre proyectos Jira Software (tableros Scrum/Kanban, backlog, sprints, epics, historias, subtareas) para proyectos de desarrollo de software. **No debe confundirse con `prov-atlassian-v1.0`**, que cubre Jira Service Management (gestión de incidencias, service desk, tickets de operaciones). Este provider es para el ciclo de vida de desarrollo de software: planificación de sprints, gestión del backlog y seguimiento de epics.

## Casos de Uso

- **Gestión de backlog de desarrollo:** crear y priorizar historias de usuario a partir de requisitos capturados por agentes del framework.
- **Seguimiento de epics:** crear epics para nuevas iniciativas identificadas en sesiones DDD o análisis de deuda técnica.
- **Planificación de sprints:** consultar el backlog y proponer ítems para el próximo sprint.
- **Vinculación de issues:** enlazar bugs, subtareas y dependencias entre proyectos de desarrollo.

## Configuración

```json
{
  "provider_id": "prov-jira-software-v1.0",
  "type": "action",
  "base_url": "AKV://jira-base-url",
  "api_version": "v3",
  "auth_method": "api_token",
  "api_token": "AKV://jira-api-token",
  "user_email": "AKV://jira-service-account-email",
  "default_project_key": "APB",
  "rate_limit": "300 req/min (Atlassian Cloud standard)"
}
```

> **Nota de aprovisionamiento:**
> 1. Crear una cuenta de servicio dedicada en Atlassian Cloud con rol de **Project Member** en los proyectos Jira Software relevantes.
> 2. Generar un API token desde la cuenta de servicio en `id.atlassian.com` → Security → API tokens.
> 3. El `base_url` es `https://apb.atlassian.net` para instancia cloud.
> 4. Todos los valores se almacenan en Azure Key Vault (`prov-akv-v1.0`).

## Acciones Disponibles

| Acción | Descripción | Gate humano |
|--------|-------------|-------------|
| `get_issue` | Obtiene el detalle de una historia, epic o subtarea por clave | No |
| `create_issue` | Crea una historia, epic, bug o subtarea en un proyecto | No |
| `update_issue` | Actualiza campos de una issue (summary, description, priority, labels) | No |
| `transition_issue` | Mueve una issue a otro estado del workflow (To Do → In Progress → Done) | No |
| `get_backlog` | Obtiene el backlog de un proyecto con filtros de tipo y prioridad | No |
| `get_sprint` | Obtiene el contenido del sprint activo de un proyecto | No |
| `add_to_sprint` | Mueve una issue al sprint especificado | **Sí** |
| `link_issues` | Crea un link entre dos issues (bloquea/es bloqueado por, relacionado con) | No |
| `add_comment` | Añade un comentario a una issue | No |
| `search_issues` | Busca issues mediante JQL (Jira Query Language) | No |

## Inputs

- `action`: nombre de la acción
- `issue_key`: clave de la issue (p. ej. `APB-123`) — para acciones sobre issues existentes
- `project_key`: clave del proyecto Jira (para `create_issue`, `get_backlog`)
- `issue_type`: tipo de issue (`Story`, `Epic`, `Bug`, `Subtask`, `Task`) — para `create_issue`
- `summary`: título de la issue — para `create_issue` y `update_issue`
- `description`: descripción en formato Atlassian Document Format (ADF) o texto plano
- `priority`: prioridad (`Highest`, `High`, `Medium`, `Low`, `Lowest`)
- `labels`: array de etiquetas
- `jql`: query JQL para `search_issues` (p. ej. `project = APB AND type = Story AND sprint in openSprints()`)
- `sprint_id`: ID del sprint — para `add_to_sprint`
- `link_type`: tipo de link (`blocks`, `is blocked by`, `relates to`) — para `link_issues`

## Outputs

- `get_issue`: objeto completo con `{key, summary, description, status, assignee, priority, labels, epic, sprint}`
- `create_issue` / `update_issue`: objeto `{key, id, url}`
- `get_backlog`: array de `{key, summary, type, priority, storyPoints, epic}`
- `search_issues`: array de issues con los campos seleccionados
- `get_sprint`: objeto `{id, name, state, startDate, endDate, issues[]}`

## Dependencias

- `prov-akv-v1.0` — todos los secretos de configuración se leen de Azure Key Vault
- `prov-atlassian-v1.0` — cubre Jira Service Management (incidencias y service desk) — no usar este provider para esos casos
- `apb-agent-tech-debt-v1.0` — registra deuda técnica identificada como issues en Jira Software

## Restricciones

- No puede gestionar proyectos Jira Service Management (JSM) — para eso usar `prov-atlassian-v1.0`.
- `add_to_sprint` requiere confirmación humana para no alterar la planificación del sprint sin aprobación del equipo.
- Las issues creadas por IA deben incluir la etiqueta `ia-generado` y estar en estado `To Do` — nunca directamente en progreso.
- No puede modificar el workflow de estados (configuración de proyecto) — operación reservada al Jira Admin.

## Ejemplo de Uso

```
Invocar: prov-jira-software-v1.0
Action: create_issue
ProjectKey: APB
IssueType: Story
Summary: "Implementar endpoint GET /atraques/{id} con paginación"
Description: "Como consumidor de la API de atraques, necesito obtener el detalle de un atraque por ID..."
Priority: High
Labels: ["ia-generado", "api", "ddd-atraques"]
→ {key: "APB-456", url: "https://apb.atlassian.net/browse/APB-456"}
```

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto creado mediante este provider debe incluir marca de origen IA:

- **Tickets Jira**: etiqueta `ia-generado` + footer en la descripción: *"Generado por APB AI Framework (prov-jira-software-v1.0) — pendiente revisión humana antes de planificar."*
- **Commits**: prefijo `[ai-gen]` + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`.

---
*Documento generado por el APB AI Framework. Requiere revisión humana antes de aprobación.*
