---
id: "apb-orch-multi-agent-v1.0"
name: "Multi-Agent Orchestration"
description: "Coordinación entre agentes del APB AI Framework cuando varios trabajan en paralelo sobre el mismo proyecto: contexto compartido, resolución de conflictos de archivo/dependencia, y trazabilidad de tracks de trabajo. Complementa a los workflows (orquestación secuencial) cubriendo el caso de trabajo paralelo."
version: "2.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "orchestration"
autonomy_level: 1
consumed_by:
  - "apb-agent-governance-v1.0"
created_date: "2026-06-20"
review_date: "2026-06-24"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

> **Nota de procedencia (Sesión 8):** la versión 1.0.0 de esta skill se
> incorporó al repositorio con un modelo de roles inventado ("PM Agent",
> "Architect Agent", "Conductor Directory") que no correspondía a ningún
> agente real del framework — heredado de una fuente de terceros
> (`wshobson/agents`) sin adaptar. La Sesión 1.5a ya había decidido no
> incorporar este contenido por ese motivo, pero llegó al repositorio de
> todas formas con el `id` renombrado al esquema correcto. Esta versión
> 2.0.0 reescribe el contenido desde cero, usando los 19 agentes reales de
> `agents/` y los 7 workflows reales de `workflows/`. Ningún agente real
> referenciaba la v1.0.0 (`consumed_by` vacío) — no se necesita migración.

# Multi-Agent Orchestration


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

---

## Por qué esta skill, si ya existen workflows

Los 7 workflows del framework (`apb-wf-sdd-full-v1.0`, `apb-wf-code-review-v1.0`,
etc.) orquestan agentes en **secuencia lineal**, con `human_checkpoints`
explícitos entre fases. Esta skill cubre un caso distinto: **qué pasa cuando
dos o más agentes trabajan en paralelo** sobre el mismo proyecto o el mismo
artefacto, dentro de una misma fase de un workflow o de forma independiente
a cualquier workflow formal.

## Cuándo Usar

- Varios agentes trabajan simultáneamente en distintos módulos de un mismo
  proyecto (p. ej. `apb-agent-technical-architect-v1.0` diseñando la
  topología de Service Bus mientras `apb-agent-security-architect-v1.0`
  evalúa amenazas sobre el mismo sistema)
- Necesitas un registro de qué agente hizo qué y cuándo, dentro de un
  proyecto con múltiples frentes abiertos
- Dos agentes proponen cambios sobre el mismo artefacto y hay que decidir
  cuál prevalece o cómo se reconcilian

## Agentes del Framework (referencia)

Esta skill no inventa roles propios — coordina los agentes reales
existentes en `agents/`. Consultar `scripts/invoke_agent.py --list` para el
listado siempre actualizado (19 agentes a la fecha de esta revisión):
`apb-agent-business-analyst-v1.0`, `apb-agent-spec-engineer-v1.0`,
`apb-agent-domain-architect-v1.0`, `apb-agent-technical-architect-v1.0`,
`apb-agent-security-architect-v1.0`, `apb-agent-cloud-architect-v1.0`,
`apb-agent-modernization-v1.0`, `apb-agent-implementer-v1.0`,
`apb-agent-code-reviewer-v1.0`, `apb-agent-qa-auto-v1.0`,
`apb-agent-platform-engineer-v1.0`, `apb-agent-sre-v1.0`,
`apb-agent-release-manager-v1.0`, `apb-agent-documentation-v1.0`,
`apb-agent-governance-v1.0`, `apb-agent-finops-v1.0`,
`apb-agent-risk-exception-v1.0`, `apb-agent-catalog-manager-v1.0`,
`apb-agent-tech-discovery-v1.0`.

## Artefacto de Contexto Compartido: Track

Un **track** es el registro de una unidad de trabajo que varios agentes
tocan a lo largo de su ciclo de vida. No sustituye a Jira (fuente de verdad
funcional, ver `proyecto.md` §3) — es un artefacto técnico interno del
framework para que un agente sepa qué hicieron otros agentes antes que él
sobre el mismo trabajo.

```yaml
# context/apb/tracks/YYYY-MM-DD-[feature].md
---
track:
  id: "TRACK-001"
  name: "Diseño técnico del módulo de facturación de escalas"
  status: in-progress
  created: "2026-06-24"

  steps:
    - agent: "apb-agent-business-analyst-v1.0"
      status: completed
      artifacts:
        - "docs/apb/discovery/business-brief.md"
    - agent: "apb-agent-spec-engineer-v1.0"
      status: completed
      artifacts:
        - "docs/apb/specs/facturacion-escalas-spec.md"
    - agent: "apb-agent-technical-architect-v1.0"
      status: in-progress
      artifacts: []
    - agent: "apb-agent-security-architect-v1.0"
      status: in-progress
      artifacts: []
      note: "Trabajando en paralelo con Technical Architect sobre el mismo sistema"

  dependencies: []
---
```

### Reglas de Contexto

1. Cada agente lee el track antes de actuar, para saber qué se ha hecho ya
2. Cada agente actualiza su propio paso al completar su parte
3. Ningún agente modifica el paso de otro agente sin coordinación explícita
4. Los cambios al track se commitean junto con los artefactos que genera

## Resolución de Conflictos

### Conflicto: Dos agentes proponen cambios incompatibles sobre el mismo artefacto

Ejemplo real: `apb-agent-technical-architect-v1.0` propone una topología de
Service Bus y `apb-agent-security-architect-v1.0` identifica que esa
topología no cumple con un requisito ENS.

```
Resolución:
1. El conflicto se documenta en el track (campo `note`)
2. Se invoca a apb-agent-governance-v1.0 si el conflicto involucra
   incumplimiento de un estándar corporativo (no es una preferencia de
   diseño, es una regla)
3. Si es una preferencia de diseño sin incumplimiento normativo, se eleva
   a validación humana (Tech Lead / Arquitecto) — ningún agente decide
   unilateralmente sobre el trabajo de otro agente
4. La decisión final y su justificación se registran como ADR
   (apb-doc-adr-v1.0, vía apb-agent-documentation-v1.0)
```

### Conflicto: Dependencia circular entre tracks

```
Resolución:
1. Identificar qué artefacto causa la circularidad (p. ej. Track A necesita
   un contrato de API que Track B todavía no ha definido, y viceversa)
2. Romper la dependencia introduciendo un contrato provisional versionado,
   o secuenciando explícitamente uno antes que el otro
3. Actualizar el campo `dependencies` de ambos tracks
4. Re-planificar con apb-agent-spec-engineer-v1.0 si afecta al backlog
```

## Estrategias de Descomposición de Trabajo Paralelo

### Por Dominio de Negocio

Coherente con DDD (ver `apb-arch-ddd-v1.0`): cada track se alinea con un
bounded context, minimizando dependencias cruzadas entre agentes.

### Por Capa Técnica

```
Track 1: Contratos de API (Technical Architect)
Track 2: Infraestructura cloud (Cloud Architect)
Track 3: Implementación de servicios (Implementer)
Track 4: Seguridad y cumplimiento (Security Architect)
```

Usar con precaución: genera más puntos de coordinación que la
descomposición por dominio, porque varios agentes tocan el mismo sistema
desde ángulos distintos simultáneamente — requiere el mecanismo de
resolución de conflictos de la sección anterior con más frecuencia.

## Integración con el Flujo APB

```
[proyecto con múltiples frentes] → apb:multi-agent-orchestration → [tracks creados] → [agentes coordinados, conflictos resueltos por gobernanza o validación humana]
```

Esta skill no reemplaza ningún workflow existente — se invoca *dentro* de
una fase de un workflow (p. ej. durante la fase de implementación de
`apb-wf-sdd-full-v1.0`, si varios subagentes de `apb-agent-implementer-v1.0`
trabajan en paralelo) o de forma independiente cuando varios agentes
colaboran fuera de un workflow formal.


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-orch-multi-agent-v1.0) - pendiente validacion humana. No distribuir sin revision.
