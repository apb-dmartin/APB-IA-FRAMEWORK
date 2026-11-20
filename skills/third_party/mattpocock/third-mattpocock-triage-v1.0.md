---
id: "third-mattpocock-triage-v1.0"
name: "Skill: Issue Triage (mattpocock/skills)"
description: "Adaptación de la skill triage del repositorio público mattpocock/skills (MIT): mueve issues y pull requests externos por una máquina de estados de triaje, asignando etiquetas de categoría (bug/enhancement) y de estado (needs-triage, needs-info, ready-for-agent, ready-for-human, wontfix), verificando afirmaciones, recabando contexto faltante y produciendo briefs listos para agente o notas de handoff a humano."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "pm"
autonomy_level: 1
source_repo: "https://github.com/mattpocock/skills"
source_license: "MIT"
source_commit: "272f99b22574f50e4266791c86b9302682970e23"
created_date: "2026-07-04"
review_date: "2026-07-04"
---

# Skill: Issue Triage (mattpocock/skills)

---

## Descripción

Adaptación de la skill `skills/engineering/triage/` del repositorio público `mattpocock/skills`
(MIT). Orquesta issues y PRs externos por una **máquina de estados de triaje**:

- **Etiquetas de categoría:** `bug` / `enhancement`.
- **Etiquetas de estado:** `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`,
  `wontfix`.
- Verifica las afirmaciones del reporte, recaba el contexto que falta mediante preguntas
  guiadas, y produce un **brief agent-ready** o una **nota de handoff a humano** para mover el
  trabajo.

## Nota de gobernanza y encaje APB

- **Gap real:** el catálogo carecía de una skill de triaje de issues como máquina de estados;
  la más cercana (`third-mattpocock-grill-prd-issues-v1.0`) va de requisitos→PRD→issues nuevos,
  no de **clasificar y enrutar** issues entrantes.
- Encaja con el flujo Jira APB (`prov-atlassian-v1.0`) — el mapeo de etiquetas a los estados
  reales del tablero Jira de cada equipo se define al pasar a `candidate`.
- Complementa a [[apb-agent-quality-compliance-v1.0]] (dedup contra Jira) y a los agentes de
  incidencias/soporte.

## Human Review

| Fase | Responsable | Tipo de revisión |
|------|-------------|------------------|
| Post-triaje | Product Owner / responsable del tablero | Validar categoría/estado antes de asignar o cerrar (`wontfix`) |

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-04 | Arquitectura APB | Incorporación (Sesión 19, punto #27) — candidata no duplicada del monorepo mattpocock |

---
*Registrado en APB AI Framework. Requiere revisión humana antes de aprobación.*
