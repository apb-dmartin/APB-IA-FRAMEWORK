---
id: "third-superclaude-framework-v1.0"
name: "Skill: SuperClaude Framework"
description: "Framework de orquestación de agentes Claude con capacidades avanzadas de planificación, memoria a largo plazo y ejecución de tareas complejas."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
source_repo: "https://github.com/SuperClaude-Org/SuperClaude_Framework"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Skill: SuperClaude Framework

---

## Descripción
Framework de orquestación de agentes Claude con capacidades avanzadas de planificación, memoria a largo plazo y ejecución de tareas complejas.

## Capacidades
- Planificación jerárquica de tareas (Hierarchical Task Planning)
- Memoria contextual persistente entre sesiones
- Delegación automática a subagentes especializados
- Recuperación de errores y reintentos inteligentes

## Inputs
- `mission`: misión principal a ejecutar
- `constraints`: restricciones operativas
- `available_agents`: catálogo de agentes disponibles

## Outputs
- `execution_plan.md`
- `agent_assignments.md`
- `execution_log.md`

## Restricciones
- Diseñado para runtime Claude
- Requiere adaptación para otros runtimes
- Memoria persistente gestionada externamente

## Adaptaciones APB
- Mapeo a agentes APB existentes
- Integración con `adapter-claude-v1.0`
- Workflow `apb-wf-sdd-full-v1.0`

## Ejemplo de Uso
```
Invocar: third-superclaude-framework-v1.0
Input: { mission: "Modernizar módulo de facturación", available_agents: [...] }
Output: execution_plan.md con asignaciones a agentes APB
```

---
*Adaptado por APB AI Framework. Licencia MIT original respetada.*
