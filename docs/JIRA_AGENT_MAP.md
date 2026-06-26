# Mapa Agente ↔ Tipo de Ticket Jira APB

> **Audiencia:** Equipos de desarrollo y operaciones APB  
> **Última actualización:** 2026-06-26  
> **Sistemas:** Jira Software + Jira Service Management (JSM)

---

## Resumen rápido

| Agente APB | Tipo de ticket Jira generado | Proyecto |
|-----------|------------------------------|---------|
| `apb-agent-business-analyst-v1.0` | Epic / Story / Spike | Jira Software |
| `apb-agent-spec-engineer-v1.0` | Story + subtareas técnicas | Jira Software |
| `apb-agent-technical-architect-v1.0` | Epic técnico + ADR | Jira Software |
| `apb-agent-cloud-architect-v1.0` | Task (infra) + ADR | Jira Software |
| `apb-agent-domain-architect-v1.0` | Epic + Story (DDD) | Jira Software |
| `apb-agent-implementer-v1.0` | Task / Subtarea de Story | Jira Software |
| `apb-agent-code-reviewer-v1.0` | Comentario en PR + Task (defectos) | Jira Software |
| `apb-agent-qa-auto-v1.0` | Bug / Task (QA gate) | Jira Software |
| `apb-agent-documentation-v1.0` | Task (documentación) | Jira Software |
| `apb-agent-security-architect-v1.0` | Security Vulnerability / Task | Jira Software |
| `apb-agent-compliance-audit-v1.0` | Task (auditoría) + Risk | Jira Software |
| `apb-agent-risk-exception-v1.0` | Risk + Change Request | Jira Software |
| `apb-agent-governance-v1.0` | Task (gobernanza) | Jira Software |
| `apb-agent-platform-engineer-v1.0` | Task (infra/DevOps) + Change | JSM |
| `apb-agent-release-manager-v1.0` | Release + Change Request | JSM |
| `apb-agent-incident-support-v1.0` | Incidencia (INC-) | JSM |
| `apb-agent-observability-v1.0` | Task (monitorización) + Alert | JSM |
| `apb-agent-sre-v1.0` | Incidencia + Problem (PRB-) | JSM |
| `apb-agent-tech-discovery-v1.0` | Spike + Epic técnico | Jira Software |
| `apb-agent-tech-debt-v1.0` | Technical Debt / Improvement | Jira Software |
| `apb-agent-modernization-v1.0` | Epic (modernización) + Migration Task | Jira Software |
| `apb-agent-ux-mockup-v1.0` | Task (diseño) + Story (UX) | Jira Software |
| `apb-agent-finops-v1.0` | Task (optimización costes) | Jira Software |
| `apb-agent-meta-builder-v1.0` | Task (framework interno) | Jira Software |
| `apb-agent-catalog-manager-v1.0` | Task (catálogo) | Jira Software |

---

## Campos mínimos por tipo de ticket

### Epic

| Campo | Valor generado por el agente |
|-------|------------------------------|
| Resumen | `[DOMINIO] {título del épico}` |
| Descripción | Contexto de negocio + objetivo + criterios de éxito |
| Componente | Componente APB afectado |
| Etiquetas | `apb-ia-framework`, `{dominio}` |
| Estimación | Story points (si hay calibración COSMIC) |

### Story / User Story

| Campo | Valor generado por el agente |
|-------|------------------------------|
| Resumen | `Como {rol}, quiero {acción} para {valor}` |
| Descripción | Contexto + reglas de negocio + escenarios de aceptación (Given/When/Then) |
| Epic Link | Epic padre |
| Subtareas | Desglose técnico (generado por `apb-agent-implementer-v1.0`) |
| Etiquetas | `apb-ia-framework`, `{dominio}` |

### Task técnica

| Campo | Valor generado por el agente |
|-------|------------------------------|
| Resumen | `[TECH] {descripción concisa de la tarea}` |
| Descripción | Objetivo técnico + criterios de done + referencias a ADR/SDD |
| Componente | Componente APB afectado |
| Etiquetas | `apb-ia-framework`, `{tipo}` (p.ej. `infra`, `devops`, `arquitectura`) |

### Incidencia JSM (INC-)

| Campo | Valor generado por `apb-agent-incident-support-v1.0` |
|-------|------------------------------------------------------|
| Resumen | `[P{prioridad}] {síntoma principal}` |
| Descripción | Síntoma, sistema afectado, impacto estimado, pasos reproducción |
| Prioridad | P1 / P2 / P3 / P4 (según matriz ITIL) |
| Categoría | Azure / Oracle / IIS / Apache / Red / DNS / Firewall / Aplicación |
| Causa raíz | Rellena al cierre |
| Resolución | Rellena al cierre |
| SLA | Asignado automáticamente según prioridad |

### Change Request JSM

| Campo | Valor generado por el agente |
|-------|------------------------------|
| Resumen | `[CHG] {descripción del cambio}` |
| Descripción | Justificación + impacto + plan de rollback + ventana de mantenimiento |
| Tipo | Normal / Estándar / Emergencia |
| Riesgo | Bajo / Medio / Alto |
| Aprobadores | Definidos según tipo de cambio y riesgo |

### Problem JSM (PRB-)

| Campo | Valor generado por `apb-agent-sre-v1.0` |
|-------|------------------------------------------|
| Resumen | `[PRB] {patrón de incidencias recurrentes}` |
| Descripción | Incidencias relacionadas + análisis de causa raíz + workaround conocido |
| Incidencias vinculadas | INC- relacionadas |
| Estado | Under Investigation / Known Error / Resolved |

---

## Flujo de creación de tickets por fase

```
DISCOVERY
  apb-agent-business-analyst → Epic + Stories en Jira Software
  apb-agent-tech-discovery   → Spike en Jira Software

DISEÑO
  apb-agent-technical-architect → Epic técnico + ADR en Confluence (link en Jira)
  apb-agent-security-architect  → Security Review Task

IMPLEMENTACIÓN
  apb-agent-implementer  → Subtareas de Story
  apb-agent-code-reviewer → Defectos como Bug (si procede)

QA / DESPLIEGUE
  apb-agent-qa-auto         → Task de QA gate + Bugs (si hay defectos)
  apb-agent-release-manager → Release + Change Request en JSM

OPERACIÓN
  apb-agent-incident-support → INC- en JSM
  apb-agent-sre              → PRB- en JSM (si es recurrente)
  apb-agent-platform-engineer → Change Request en JSM (cambios infra)
```

---

## Etiquetas estándar APB para todos los tickets generados por IA

| Etiqueta | Significado |
|----------|-------------|
| `apb-ia-framework` | Ticket generado o asistido por el APB AI Framework |
| `ia-reviewed` | Output del agente revisado por técnico APB |
| `ia-pending-review` | Output del agente pendiente de revisión humana |
| `autonomy-{nivel}` | Nivel de autonomía del agente que lo generó |

---

*Documento generado por el APB AI Framework — Sesión 13. Requiere revisión humana antes de distribución.*
