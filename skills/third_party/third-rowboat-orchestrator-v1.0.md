---
id: "third-rowboat-orchestrator-v1.0"
name: "Skill: Agent Orchestrator (Rowboat)"
description: "Orquestador de agentes multi-runtime con soporte para planificación dinámica, balanceo de carga y resolución de conflictos entre agentes."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
source_repo: "https://github.com/rowboatlabs/rowboat"
source_license: "Apache 2.0"
source_commit: "unverified"
verified_date: "2026-06-23"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Skill: Agent Orchestrator (Rowboat)

---

## Descripción
Orquestador de agentes multi-runtime con soporte para planificación dinámica, balanceo de carga y resolución de conflictos entre agentes.

## Capacidades
- Orquestación multi-agente con grafo de dependencias
- Balanceo de carga entre agentes
- Resolución de conflictos de recursos
- Monitorización de estado de ejecución

## Inputs
- `workflow_definition`: definición del workflow
- `agent_pool`: pool de agentes disponibles
- `execution_context`: contexto de ejecución

## Outputs
- `orchestration_plan.md`
- `execution_trace.md`
- `resource_allocation.md`

## Restricciones
- Requiere infraestructura de orquestación
- Apache 2.0: compatible con uso comercial
- No gestiona secretos ni credenciales

## Adaptaciones APB
- Integración con workflows APB
- Mapeo a agentes y subagentes existentes
- Logging para auditoría de gobierno

## Ejemplo de Uso
```
Invocar: third-rowboat-orchestrator-v1.0
Input: { workflow: "apb-wf-sdd-full-v1.0", agents: [...] }
Output: orchestration_plan.md con asignaciones optimizadas
```

---
*Adaptado por APB AI Framework. Licencia Apache 2.0 original respetada.*
