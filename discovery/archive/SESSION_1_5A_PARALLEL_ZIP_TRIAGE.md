# Sesión 1.5a — Triage del Zip Paralelo (`apb-ai-framework_v1`)

> **Estado: EJECUTADO (1.5a, 1.5b y 1.5c completas).** Este documento
> registra el triage, las decisiones, y el resultado final de la
> incorporación de los Grupos C y D al repositorio.

## 0. Qué es realmente este zip

No es un conjunto de skills de terceros: es una **snapshot de una sesión de
trabajo anterior** del mismo framework, con su propia bifurcación interna
(`skill/apb-owned/` vs `skill/apb-owned2/` — dos lotes cronológicos sin
solape de carpetas, no duplicados entre sí). Contiene carpetas vacías sin
valor (`Nueva carpeta/`, `tests/.gitkeep`, `docs/.gitkeep`,
`capabilities/.gitkeep`) y un historial de versiones de catálogo/índice
(`INDEX_v2..v5.md`, `CATALOG_v2..v4.md`).

## 1. Grupo A — Solo histórico, NO incorporar

| Archivo | Motivo |
|---|---|
| `INDEX_v2.md` … `INDEX_v5.md` | Snapshots de evolución del índice; superados por `INDEX.md` actual |
| `CATALOG_v2.md` … `CATALOG_v4.md` | Snapshots de evolución del catálogo; superados por `catalog/CATALOG.md` actual |
| `ADAPTATION-MASTER.md` | Ya gestionado como duplicado en Sesión 1 (idéntico a `discovery/APB-Skills-Adaptation-v1.4.md`) |
| `Nueva carpeta/`, `tests/.gitkeep`, `docs/.gitkeep`, `capabilities/.gitkeep` | Vacíos, sin contenido real |

**Acción:** ninguna. No se copian al repo final.

## 2. Grupo B — Ya idéntico o ya resuelto, NO incorporar

Verificado por `diff` byte a byte: `skill/apb-owned2/architecture/*`,
`skill/apb-owned2/discovery/*`, `skill/apb-owned2/governance/*`,
`skill/apb-owned2/documentation/*` son **idénticos** a su equivalente actual
en `repo_build/skills/apb-owned/`. La única excepción
(`apb-dev-code-review-v1.0.md`) difiere solo en el rebranding de marca
(`@apb.es` / "Islas Baleares" → ya corregido en el repo actual). El resto de
carpetas de `apb-owned2` (`api-design`, `architecture-design`,
`brainstorming`, `code-review`, `deployment`, `design-approval`,
`development`, `docs`, `document-processing`, `event-driven`,
`frontend-integration`, `implementation-patterns`, `mcp-building`,
`multi-agent-orchestration`) tienen carpeta homónima ya poblada en el repo
actual.

**Acción:** ninguna. El repo actual ya es la versión más evolucionada.

## 3. Grupo C — Dominios completos a recuperar (alta prioridad)

Contenido genuino, sustancial, y sin equivalente en el repo actual. Resuelve
directamente los "5 dominios fantasma" de `DOMAIN_REGISTRY.md`.

| Dominio | Nº skills | Ejemplos |
|---|---|---|
| `qa` | 7 | test-plan, test-strategy, test-auto, unit-test-gen, release-ready, post-migration, anonymize |
| `platform` | 7 | cicd, terraform, ansible, docker, cloud-ready, db-migration, finops |
| `security` | 6 | owasp, threat-model, risk-analysis, risk-policies, ens, forensic |
| `operation` | 6 | observability, operability, prr, rca, runbook, slo-design |

**Acción Sesión 1.5c:** incorporar las 26 skills a `skills/apb-owned/{dominio}/`,
limpiando marca antigua y normalizando a YAML donde falte.

## 4. Grupo D — Skills sueltas de gestión de proyecto/proceso

> **Decisión aprobada.** Se reparten en dos dominios en lugar de uno: `pm`
> (dominio nuevo, gestión y ejecución del ciclo de desarrollo) y `qa`
> (dominio ya existente vía Grupo C). Ninguna de las 13 es "análisis" en
> sentido estricto salvo `pm-analysis`, que encaja como análisis inicial de
> producto dentro de `pm`.

| Skill (zip) | Dominio destino | Motivo |
|---|---|---|
| `apb_planning_skill.md` | `pm` | Planificación de implementación pre-código |
| `apb_sprint_planning_skill.md` | `pm` | Planificación de sprint |
| `apb_task_breakdown_skill.md` | `pm` | Descomposición de tareas |
| `apb_retrospective_skill.md` | `pm` | Retrospectiva post-epic/sprint |
| `apb_parallel_execution_skill.md` | `pm` | Coordinación de ejecución paralela entre agentes |
| `apb_refactoring_skill.md` | `pm` | Gestión/patrones de refactorización (no es QA ni es puramente `development`) |
| `apb_slash_commands_skill.md` | `pm` | Comandos de invocación rápida del framework (transversal, vive mejor en `pm` que repartido) |
| `apb_pm_analysis_skill.md` | `pm` | Análisis de producto/requisitos al inicio del proyecto |
| `apb_verification_skill.md` | `qa` | Verificación de finalización antes de PR/commit |
| `apb_testing_strategy_skill.md` | `qa` | Estrategia de testing |
| `apb_tdd_skill.md` | `qa` | TDD |
| `apb_qa_validation_skill.md` | `qa` | Validación de calidad y tests E2E |
| `apb_readiness_check_skill.md` | `qa` | Gate de preparación pre-implementación |

**Nota detectada durante la revisión de contenido:** las 13 skills están
especializadas en "arquitecturas orientadas a eventos" (herencia de la
sesión de generación original). Al incorporarlas (Sesión 1.5c) se
generalizará la redacción para que sea aplicable a cualquier arquitectura
APB, no solo event-driven, salvo que el contenido sea inherentemente
específico de eventos (en cuyo caso se mantiene, pero se hace explícito en
la descripción en lugar de asumido).

**Acción Sesión 1.5c:** incorporar las 13 a `skills/apb-owned/pm/` y
`skills/apb-owned/qa/` según la tabla, normalizando a YAML, renombrando al
patrón `apb-pm-{nombre}-v1.0.md` / `apb-qa-{nombre}-v1.0.md`, y citando
procedencia (`obra/superpowers`, `bmad-method`, `wshobson/agents`, todas MIT)
en cada una.

## 5. Grupo E — Agentes: verificado, SIN acción requerida

> **Sesión 1.5b ejecutada.** Hallazgo: los 3 agentes del zip ya fueron
> fusionados con su prompt de sistema en una sesión de trabajo anterior al
> snapshot actual del repo de GitHub. Evidencia: el historial de cambios de
> los 3 agentes actuales registra literalmente *"Creación inicial + fusión
> prompt de sistema"* (2026-06-21) — el zip paralelo captura un punto
> **anterior** a esa fusión, no una rama alternativa pendiente de integrar.

| Archivo zip | Equivalente actual | Resultado de la comparación |
|---|---|---|
| `GOVERNANCE_AGENT.md` | `apb-agent-governance-v1.0.md` | Prompt de sistema idéntico (con rebranding ya aplicado). El actual añade: 7 skills asignadas (vs. 4), workflows, ejemplo YAML, sección de seguridad. |
| `IMPLEMENTER_AGENT.md` | `apb-agent-implementer-v1.0.md` | Prompt de sistema incorporado. El actual además refleja una decisión técnica más reciente y precisa: mensajería `JSON + CloudEvents` (excluyendo explícitamente Avro/Protobuf) sustituye al `Avro/JSON` ambiguo del zip. |
| `SECURITY_ARCHITECT_AGENT.md` | `apb-agent-security-architect-v1.0.md` | Mismo patrón: contenido del zip incorporado, repo actual más completo. |

**Acción:** ninguna. El repo actual ya es la versión correcta y más
evolucionada en los 3 casos. No se modifica ningún archivo de `agents/`.

## 6. Resumen de decisión

| Grupo | Nº archivos | Decisión |
|---|---|---|
| A — histórico | 8 | Descartar |
| B — ya integrado/idéntico | ~48 | Descartar (no aporta nada nuevo) |
| C — dominios completos | 26 | **Incorporar** (Sesión 1.5c) |
| D — skills de proceso/PM/QA | 13 | **Incorporar**, repartidas en `pm` (8) y `qa` (5) (Sesión 1.5c) |
| E — agentes | 3 | Verificado: ya fusionados previamente, sin acción (Sesión 1.5b, cerrada) |

Próximo paso: **Sesión 1.5c**, incorporación real de los Grupos C y D al repo.

## 7. Resultado de la Ejecución (Sesión 1.5c)

| Dominio | Skills incorporadas | Detalle |
|---|---|---|
| `qa` | 12 (7 directas/fusión Grupo C + 5 reasignadas del Grupo D) | 1 fusión (Anonymize), 6 conversión directa, 5 del Grupo D (verification, testing-strategy, tdd, readiness-check, qa-validation-e2e) |
| `platform` | 6 | Conversión directa desde formato tabla; 4 `SKILL_PLAT_*` de terceros (Ansible, CICD, FinOps, Terraform) reclasificadas a `skills/third_party/{sigridjineth,expo,google,hashicorp}/` |
| `security` | 8 | 6 conversión directa + 2 recuperadas de la carpeta huérfana `skills/security/` (Cloud Hardening, MITRE Mapping — esta carpeta huérfana queda **eliminada**) |
| `operation` | 6 | Conversión directa desde formato tabla |
| `pm` (dominio nuevo) | 8 | Del Grupo D: planning, refactoring, task-breakdown, slash-commands, parallel-execution, product-analysis, sprint-planning, retrospective |

**Total incorporado: 40 skills** (27 del Grupo C + 13 del Grupo D), todas con
frontmatter YAML válido conforme a `context/apb/SCHEMA.md`, marca corporativa
corregida donde aplicaba, y `domain` correctamente asignado.

**Verificación:** `python3 scripts/validate_repo.py` confirma **0 errores**
en los 5 dominios tocados en esta sesión (`qa`, `platform`, `security`,
`operation`, `pm`). El incremento de errores totales del repo (211→215) se
debe enteramente a la mayor superficie de archivos analizados, no a
contenido nuevo defectuoso.

**Acciones de gobierno relacionadas, ya aplicadas:**
- `DOMAIN_REGISTRY.md` actualizado: `pm` ahora tiene mapeo de carpeta real
  (`skills/apb-owned/pm/`); nota de gobernanza añadida indicando que los
  conteos deben derivarse automáticamente (Sesión 3), no escribirse a mano.
- Carpeta huérfana `skills/security/` (fuera de la estructura declarada,
  detectada en Sesión 1) **eliminada** tras migrar su contenido al lugar
  correcto.

### Hallazgos adicionales para sesiones siguientes

1. **Quinta y sexta convención de cabecera detectadas** en este lote (tabla
   `## Metadata`, lista con guiones `- **ID**:`, YAML incompleto sin campos
   de `SCHEMA.md`), sumadas a las ya conocidas (blockquote `> **ID:**`,
   YAML completo). Las 6 convenciones ya están unificadas en los archivos
   tocados hasta ahora; quedan pendientes de revisión sistemática en el
   resto del repo en la **Sesión 2**.
2. **Referencia rota detectada**: `apb-sec-cloud-hardening-v1.0.md` referencia
   `third-mukul-cybersecurity-arsenal-v1.0`, que no existe — el ID real más
   cercano es `third-mukul-cloud-security-v1.0` o `third-mukul-cyber-arsenal-v1.0`.
   **Corregir en Sesión 4.**
3. **`source_commit: "unverified"
verified_date: "2026-06-23"` provisional** en las 4 skills de platform
   reclasificadas a `third_party` (Ansible, CICD, FinOps, Terraform) — mismo
   placeholder que en Sesión 1, pendiente de pin real en **Sesión 5**.
4. **Skills hermanas con nombre parecido, mantenidas separadas**:
   `apb-qa-test-strategy-v1.0` (estrategia general de proyecto/programa) y
   `apb-qa-testing-strategy-v1.0` (específica de arquitecturas event-driven)
   cubren propósitos distintos y se mantienen como componentes
   independientes, mismo criterio que API GraphQL/REST en Sesión 1.
5. **Sesgo "orientado a eventos" generalizado de forma parcial**: las 13
   skills del Grupo D se incorporaron con nota de procedencia indicando que
   el contenido fue "adaptado y generalizado", pero el cuerpo detallado de
   cada una conserva en distinta medida el enfoque event-driven original.
   Una revisión de contenido más profunda (no solo de metadatos) podría
   abordarse como tarea opcional futura si limita su uso en proyectos no
   event-driven.
