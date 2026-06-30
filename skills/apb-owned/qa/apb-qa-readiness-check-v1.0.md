---
id: "apb-qa-readiness-check-v1.0"
name: "Readiness Check"
description: "Validar que PRD, arquitectura, specs y stories est\xE1n completos y alineados antes\
  \ de iniciar implementaci\xF3n. Gate de preparaci\xF3n con verificaciones espec\xED\
  ficas de event-driven."
version: "1.0.0"
status: "draft"
owner: "QA APB <arquitectura@portdebarcelona.cat>"
domain: "qa"
autonomy_level: 1
consumed_by:
  - "apb-agent-qa-auto-v1.0"
created_date: "2026-06-20"
review_date: "2026-06-24"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

> Procedencia: Adaptado de bmad-method (bmad-check-implementation-readiness) (licencia MIT). Contenido adaptado y
> generalizado para el APB AI Framework.

# APB Readiness Check: Verificación de Preparación


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Visión General

Validar que todos los artefactos de planificación están completos y alineados antes de que la implementación comience. Este skill actúa como gate final entre diseño y desarrollo.

**Principio fundamental:** Implementar sin preparación completa = retrabajo garantizado.

## Cuándo Usar

**Obligatorio:**
- Después de completar `apb:architecture-design` y antes de `apb:planning`
- Cuando se unen múltiples specs de diferentes agentes
- Antes de iniciar cualquier sprint de desarrollo
- Cuando el usuario dice "¿estamos listos para implementar?"

## El Proceso de Verificación

### Paso 1: Inventario de Artefactos

Verificar que existen los siguientes documentos:

| # | Artefacto | Ubicación Esperada | Estado |
|---|-----------|-------------------|--------|
| 1 | Product Brief | `docs/apb/product/product-brief.md` | ☐ |
| 2 | System Architecture | `docs/apb/architecture/system-architecture.md` | ☐ |
| 3 | Event Catalog | `docs/apb/architecture/event-catalog.md` | ☐ |
| 4 | Service Bus Topology | `docs/apb/architecture/service-bus-topology.md` | ☐ |
| 5 | Spec Técnico | `docs/apb/specs/YYYY-MM-DD-feature-design.md` | ☐ |
| 6 | Plan de Implementación | `docs/apb/plans/YYYY-MM-DD-feature-plan.md` | ☐ |
| 7 | Stories/Epics | `docs/apb/stories/` | ☐ |
| 8 | AsyncAPI Spec | `docs/apb/asyncapi.yaml` | ☐ |

### Paso 2: Verificación de Trazabilidad

#### Product Brief → Architecture

```
¿Cada evento de negocio del product brief tiene:
  ├── Un topic en Service Bus definido?
  ├── Un schema CloudEvents documentado?
  ├── Productor y consumidor identificados?
  └── Métricas de éxito asociadas?
```

#### Architecture → Spec Técnico

```
¿Cada decisión arquitectónica del system architecture tiene:
  ├── Justificación documentada (ADR)?
  ├── Implicaciones en el spec técnico?
  ├── Riesgos identificados y mitigados?
  └── Alternativas consideradas?
```

#### Spec Técnico → Plan de Implementación

```
¿Cada requisito del spec técnico tiene:
  ├── Al menos una tarea en el plan?
  ├── Tests definidos?
  ├── Criterios de aceptación claros?
  └── Owner asignado?
```

#### Plan → Stories

```
¿Cada tarea del plan tiene:
  ├── Una story correspondiente?
  ├── Estimación de esfuerzo?
  ├── Dependencias identificadas?
  └── Definition of Done?
```

### Paso 3: Verificación de Event-Driven

#### Checklist de Preparación de Eventos

| # | Verificación | Criterio de Aceptación |
|---|-------------|----------------------|
| 1 | **Event Catalog completo** | Todos los eventos tienen type, schema, productor, consumidor |
| 2 | **Schemas validados** | Todos los schemas pasan validación CloudEvents 1.0 |
| 3 | **Topología definida** | Topics, subscriptions, rules documentados en AsyncAPI |
| 4 | **Idempotencia planificada** | Cada consumidor tiene estrategia de deduplicación definida |
| 5 | **Compensaciones definidas** | Cada saga tiene acciones compensatorias documentadas |
| 6 | **DLQ configurada** | Cada subscription tiene DLQ con retry policy |
| 7 | **Observabilidad planificada** | Métricas, logs, tracing definidos por evento |
| 8 | **Versionado de schemas** | Estrategia de versionado documentada |
| 9 | **Performance validada** | Throughput y latencia validados contra requisitos |
| 10 | **Seguridad revisada** | AuthN/AuthZ de Service Bus definido |

### Paso 4: Verificación de Dependencias

```
┌─────────────────────────────────────────────────────────────┐
│              Grafo de Dependencias                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Product Brief ──> System Architecture ──> Spec Técnico │
│        │                  │                      │          │
│        ▼                  ▼                      ▼          │
│   Event Catalog ──> Service Bus Topology ──> Plan         │
│        │                  │                      │          │
│        └──────────────────┴──────────────────────┘          │
│                            │                                │
│                            ▼                                │
│                        Stories                              │
│                                                             │
│   Verificar: NO hay ciclos, NO hay dependencias faltantes   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Paso 5: Revisión por Subagente

Despachar revisor de preparación:

```
Subagente (general-purpose):
  description: "Revisar preparación para implementación"
  prompt: |
    Revisa la preparación de este proyecto para implementación.

    ## Artefactos a Revisar
    - Product Brief: [ruta]
    - System Architecture: [ruta]
    - Event Catalog: [ruta]
    - Service Bus Topology: [ruta]
    - Spec Técnico: [ruta]
    - Plan de Implementación: [ruta]
    - Stories: [ruta]

    ## Verificaciones
    1. ¿Todos los artefactos existen y están completos?
    2. ¿Hay trazabilidad entre artefactos (sin gaps)?
    3. ¿Los eventos están completamente definidos?
    4. ¿La topología de Service Bus es coherente?
    5. ¿Hay riesgos no mitigados?
    6. ¿El plan es realista y construible?
    7. ¿Las stories tienen Definition of Done clara?

    ## Formato de Salida
    ## Readiness Review

    **Estado:** Ready | Not Ready | Ready with Warnings

    **Bloqueadores:**
    - [Descripción] — [Por qué bloquea]

    **Advertencias:**
    - [Descripción] — [Riesgo]

    **Recomendaciones:**
    - [Sugerencia]
```

### Paso 6: Reporte de Preparación

Presentar al usuario:

```
## Readiness Check Report

**Estado:** [Ready / Not Ready / Ready with Warnings]

**Artefactos:** [X/8 completos]
**Trazabilidad:** [X% de cobertura]
**Event-Driven Checklist:** [X/10 pasan]

### Bloqueadores (si los hay)
[Lista]

### Advertencias (si las hay)
[Lista]

### Próximo Paso
[Si Ready → apb:planning]
[Si Not Ready → corregir artefactos faltantes]
```

## Integración con el Flujo APB

```
apb:architecture-design → [system architecture] → apb:readiness-check → [ready] → apb:planning
                              ↓ not ready
                        [corregir artefactos]
```


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-qa-readiness-check-v1.0) - pendiente validacion humana. No distribuir sin revision.
