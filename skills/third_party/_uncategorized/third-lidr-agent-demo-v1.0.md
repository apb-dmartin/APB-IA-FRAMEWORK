---
id: "third-lidr-agent-demo-v1.0"
name: "Skill: Agent Demo — Ticket to Deployment (LIDR Academy)"
description: "Demostración completa de pipeline de agente IA desde la recepción de un ticket hasta el despliegue automatizado. Incluye planificación, implementación, testing y release."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
source_repo: "https://github.com/LIDR-academy/lidr-agent-demo"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Skill: Agent Demo — Ticket to Deployment (LIDR Academy)

---

## Descripción
Demostración completa de pipeline de agente IA desde la recepción de un ticket hasta el despliegue automatizado. Incluye planificación, implementación, testing y release.

## Capacidades
- Procesamiento de tickets de Jira/GitHub Issues
- Generación de plan de implementación
- Desarrollo iterativo con feedback
- Despliegue automatizado con validación

## Inputs
- `ticket_id`: identificador del ticket
- `ticket_description`: descripción del requerimiento
- `repository_url`: URL del repositorio

## Outputs
- `implementation_plan.md`
- `code_changes.diff`
- `test_results.md`
- `deployment_report.md`

## Restricciones
- Uso demostrativo/piloto únicamente
- Requiere supervisión humana en cada fase
- No autorizado para producción sin aprobación

## Adaptaciones APB
- Integración con workflows APB existentes
- Alineación con `apb-wf-sdd-full-v1.0`
- Metadatos de gobierno y evidencia

## Ejemplo de Uso
```
Invocar: third-lidr-agent-demo-v1.0
Input: { ticket_id: "PROJ-123", description: "Añadir campo X", repo: "..." }
Output: Pipeline completo ticket → deploy
```

---
*Adaptado por APB AI Framework. Licencia MIT original respetada.*
