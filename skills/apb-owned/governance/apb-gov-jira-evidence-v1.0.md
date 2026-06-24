---
id: "apb-gov-jira-evidence-v1.0"
name: "Registro de Evidencias en Jira"
description: "Integrar la generación de evidencias del framework APB con Jira, creando tickets, comentarios y attachments que vinculen automáticamente las evidencias generadas con los proyectos y épicas correspondientes. Facilita el tracking de compliance y la trazabilidad en el SDLC."
version: "1.0.0"
status: "draft"
owner: "Gobierno TI APB <arquitectura@portdebarcelona.cat>"
domain: "governance"
autonomy_level: 2
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Registro de Evidencias en Jira

## Propósito
Integrar la generación de evidencias del framework APB con Jira, creando tickets, comentarios y attachments que vinculen automáticamente las evidencias generadas con los proyectos y épicas correspondientes. Facilita el tracking de compliance y la trazabilidad en el SDLC.

## Contexto de Uso
- Creación de tickets Jira para tareas de gobierno, QA o arquitectura.
- Registro de evidencias como attachments o comentarios en tickets existentes.
- Actualización de estado de tickets basado en resultados de skills (pass/fail/pending).
- Integración con workflows de release y excepciones de riesgo.

## Entradas Requeridas
| Entrada | Tipo | Descripción | Obligatorio |
|---------|------|-------------|-------------|
| `jira_project_key` | Texto | Clave del proyecto Jira (ej. `APB`, `ARCH`, `QA`) | ✅ |
| `issue_type` | Enum | `Task`, `Story`, `Bug`, `Epic`, `Sub-task`, `Risk` | ✅ |
| `evidence_content` | Texto / Markdown | Contenido de la evidencia a registrar | ✅ |
| `parent_issue` | Texto | Clave del ticket padre (para sub-tareas o vinculación) | ❌ |
| `labels` | Lista | Etiquetas Jira para categorización | ❌ |
| `assignee` | Texto | Usuario Jira asignado | ❌ |

## Flujo de Trabajo (Pasos)
1. **Validación de proyecto**: Verificar que el proyecto Jira existe y el usuario tiene permisos.
2. **Generación de ticket**: Crear issue en Jira con título, descripción y campos personalizados.
3. **Vinculación de evidencia**: Adjuntar contenido de evidencia como descripción estructurada o attachment.
4. **Actualización de campos personalizados**:
   - `Evidence ID` — ID único de la evidencia.
   - `Compliance Framework` — ENS, OWASP, etc.
   - `Review Status` — Pending / In Review / Approved / Rejected.
   - `Agent Source` — Skill/agente que generó la evidencia.
5. **Vinculación a tickets relacionados**: Link a épicas, historias de usuario o tickets de riesgo.
6. **Notificación**: Opcionalmente notificar a stakeholders vía comentario @mention.
7. **Registro de metadatos**: Almacenar ID de ticket Jira en metadatos de la evidencia para trazabilidad bidireccional.

## Salida Esperada
### Estructura del Ticket Jira
```
Título: [GOV-EVI-YYYY-NNNN] Evidencia — [Tipo] — [Título]
Descripción:
  - Resumen de la evidencia
  - Enlace a documento fuente
  - Hallazgos / Decisiones
  - Estado de revisión
  - Trazabilidad a commits/specs
Attachment: evidencia.md (o PDF)
Custom Fields:
  - Evidence ID: GOV-EVI-YYYY-NNNN
  - Framework: [compliance_framework]
  - Agent: [agent_id]
  - Skill: [skill_id]
```

## Criterios de Calidad
- [ ] Ticket creado con todos los campos obligatorios poblados.
- [ ] Evidencia adjunta en formato legible (markdown o PDF).
- [ ] Trazabilidad bidireccional: ticket referencia evidencia y evidencia referencia ticket.
- [ ] Labels y campos personalizados consistentes con estándares de Jira corporativo.
- [ ] No se incluyen secretos ni datos sensibles en la descripción del ticket.
- [ ] El ticket es searchable y reportable en dashboards de Jira.

## Stack y Tecnologías
- Jira Cloud / Data Center (REST API v3)
- Atlassian Rovo MCP (provider `prov-atlassian-v1.0`)
- Autenticación: API Token o OAuth 2.0 (nunca en código; referencia a Azure Key Vault)
- Formatos: Markdown, JSON para API

## Dependencias
- `apb-gov-evidence-v1.0` — para generación de contenido de evidencia
- `apb-gov-catalog-v1.0` — para registro en catálogo
- `prov-atlassian-v1.0` — para conectividad con Jira

## Ejemplo de Uso
**Prompt de invocación:**
```
Registra en Jira la evidencia de revisión de código del PR #342:
- Proyecto: APB
- Issue type: Task
- Parent: ARCH-2042 (Épica de modernización)
- Evidencia: [contenido markdown de apb-dev-code-review-v1.0]
- Labels: code-review, security, sprint-24
- Assignee: tech.lead@portdebarcelona.cat
```

## Notas y Advertencias
- **Nivel 2**: El agente puede crear y actualizar tickets Jira mediante API; requiere permisos y tokens configurados.
- **Revisión humana obligatoria** antes de que el ticket se considere aprobado.
- Los tokens de API de Jira nunca se almacenan en skills; se obtienen de Azure Key Vault en runtime.
- Las actualizaciones masivas de tickets requieren confirmación previa para evitar spam.
- El agente respeta los workflows de Jira configurados; no transiciona estados no permitidos.

## Historial de Cambios
| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-20 | Arquitectura APB | Creación inicial |
