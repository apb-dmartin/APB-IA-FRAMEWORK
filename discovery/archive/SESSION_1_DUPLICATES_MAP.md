# Sesión 1 — Mapa de Duplicados y Huérfanos (repo principal)

> **Estado: EJECUTADO.** Este documento se mantiene como registro de las
> decisiones tomadas y las acciones aplicadas sobre `skills/apb-owned/development/`
> y `skills/third_party/`.

## 1. Duplicado literal exacto — ELIMINAR sin debate

| Archivo a conservar | Archivo a eliminar | Evidencia |
|---|---|---|
| `skills/apb-owned/development/apb-dev-code-base-v1.0.md` | `skills/apb-owned/development/APB-IA-SKILL-DEV-CODE-BASE-v1.0.md` | Mismo `id` interno (`apb-dev-code-base-v1.0`), contenido idéntico salvo `review_date` y una línea de changelog. Es un re-guardado accidental, no una versión distinta. |
| `discovery/APB-Skills-Adaptation-v1.4.md` | `skills/apb-owned/docs/ADAPTATION-MASTER.md` | Diff = 0 líneas. Conservar en `discovery/` porque es donde corresponde semánticamente (documento de proceso de adaptación, no una skill). |

**Acción Sesión 2:** borrar los 2 archivos de la columna derecha. Sin pérdida de información.

---

## 2. Falsos "duplicados" — en realidad son skills hermanas mal etiquetadas

Hallazgo más importante de esta sesión: **los 6 pares restantes `SKILL_DEV_*` / `apb-dev-*` NO son duplicados**. Cada `SKILL_DEV_*` es una **adaptación de una fuente de terceros distinta**, y cada `apb-dev-*` es un estándar **propio** de APB sobre un tema relacionado pero no idéntico. Coincidieron en mi detección automática solo porque comparten palabra clave de dominio.

| Par detectado | `SKILL_DEV_*` (adaptación de terceros) | `apb-dev-*` (estándar propio APB) | ¿Mismo concepto? |
|---|---|---|---|
| API | `SKILL_DEV_API_STANDARD.md` ← `apollographql/skills` (GraphQL/Apollo) | `apb-dev-api-standard-v1.0.md` (estándar REST propio) | No — GraphQL vs REST |
| Frontend | `SKILL_DEV_DEVEXPRESS_FRONT.md` ← `google-labs-code/stitch-skills` (React/TS general) | `apb-dev-devexpress-front-v1_0.md` (DevExpress específico) | No — React genérico vs librería concreta |
| Implementación | `SKILL_DEV_IMPLEMENT.md` ← `NeoLabHQ/context-engineering-kit` (SDD) | `apb-dev-implement-v1_0.md` (implementación propia) | Solape parcial — fusionar recomendado |
| Microservicios | `SKILL_DEV_MICRO_BASE.md` ← `NeoLabHQ` (DDD+SDD consolidado) | `apb-dev-micro-base-v1.0.md` (base propia) | Solape parcial — fusionar recomendado |
| Code Review | `SKILL_DEV_REVIEW_ADVANCED.md` ← `NeoLabHQ` (análisis avanzado/seguridad) | `apb-dev-review-advanced-v1_0.md` (revisión avanzada propia) | Solape alto — fusionar recomendado |
| Review TL | `SKILL_DEV_REVIEW_TL.md` ← `garrytan/gstack` (perspectiva Tech Lead) | `apb-dev-review-tl-v1_0.md` (revisión TL propia) | Solape alto — fusionar recomendado |
| SQL | `SKILL_DEV_SQL_FIX.md` ← `sanjay3290/ai-skills` (Postgres/MySQL/MSSQL) | `apb-dev-sql-fix-v1_0.md` (autocorrección SQL propia) | Solape alto — fusionar recomendado |

**Problema de gobernanza real, no de duplicación:** los 7 archivos `SKILL_DEV_*` están ubicados en
`skills/apb-owned/development/`, pero por declarar `source_adaptation` de un repo de terceros
(Apollo, Stitch, NeoLabHQ, gstack, sanjay3290), según `GOVERNANCE.md` §4.2 **deberían vivir en
`skills/third_party/{fuente}/`** con descriptor completo (`source_repo`, `source_license`,
`source_commit` real), no mezclados en `apb-owned` sin esa metadata homogénea.

**Recomendación para Sesión 1.5c / Sesión 2 (a decidir contigo):**
- **API, Frontend, Implement**: mantener como dos componentes separados (cubren cosas distintas), pero mover el `SKILL_DEV_*` a `skills/third_party/{fuente}/` con el ID y esquema correctos.
- **Review Advanced, Review TL, SQL Fix, Micro Base**: el solape de propósito es alto. Propongo **fusionar** lo mejor de cada `SKILL_DEV_*` (más detalle técnico) dentro del `apb-dev-*` correspondiente (que ya tiene gobernanza correcta), y mover el original de terceros a `third_party` solo como referencia archivada — evita mantener dos skills que un agente podría invocar de forma ambigua para la misma tarea.

➡️ Esta fusión de contenido (no solo de archivo) es trabajo de **Sesión 2**, no de hoy. Hoy solo dejamos la decisión tomada.

---

## 3. Huérfanos estructurales

| Elemento | Problema | Recomendación |
|---|---|---|
| `skills/security/` (2 archivos) | Carpeta fuera de la estructura declarada (`README.md`/`SYSTEM.md` exigen todo bajo `skills/apb-owned/{dominio}/`) | Mover a `skills/apb-owned/security/` (Sesión 1.5c, junto con los dominios recuperados del zip paralelo, ya que `security/` es justo uno de los dominios que llegan de ahí) |
| `fix-apb-brand.sh` / `fix-apb-brand.ps1` (raíz) | Script puntual de una corrección de marca ya aplicada; sin valor permanente en la raíz | Mover a `scripts/archive/` como evidencia histórica, o eliminar (Sesión 7) |
| `DOMAIN_REGISTRY.md` declara 5 dominios sin carpeta (`qa`, `platform`, `security`, `operation`, `orchestration`) | Ya resuelto conceptualmente: estos dominios existen en el zip paralelo | Se resuelve en Sesión 1.5c, no aquí |

## 4. Falsos positivos descartados (no requieren acción)

- `GOVERNANCE.md` vs `agents/apb-agent-governance-v1.0.md`: la política y el agente que la ejecuta son cosas distintas por diseño, no duplican contenido.
- `README.md` y los 8 `README.md` de `context/apb/policies/*/`: cada uno es un índice de su propia subcarpeta, contenido distinto en cada caso (verificado por tamaño).

---

## 5. Resumen de acciones para Sesión 2

1. Eliminar 2 archivos duplicados literales (sección 1).
2. Mover/reclasificar 7 archivos `SKILL_DEV_*` a `skills/third_party/` con esquema correcto (sección 2).
3. Fusionar contenido relevante de 4 de esos 7 dentro de su `apb-dev-*` hermano (Review Advanced, Review TL, SQL Fix, Micro Base).
4. Mover `skills/security/*` (en combinación con Sesión 1.5c).

## 6. Resultado de la Ejecución (este documento, actualizado)

| Acción | Resultado |
|---|---|
| Eliminar 2 duplicados literales | ✅ Hecho |
| Fusionar Review TL (`apb-dev-review-tl-v1.0`) | ✅ Hecho — incorpora dimensiones de evaluación, formato de feedback y checklist de `gstack` |
| Fusionar Review Advanced (`apb-dev-review-advanced-v1.0`) | ✅ Hecho — incorpora checklists de 6 áreas de análisis y scoring de `NeoLabHQ` |
| Fusionar SQL Fix (`apb-dev-sql-fix-v1.0`) | ✅ Hecho — incorpora análisis de performance/índices/migración de `sanjay3290/ai-skills` |
| Fusionar Micro Base (`apb-dev-micro-base-v1.0`) | ✅ Hecho — incorpora diseño estratégico DDD/microservicios de `NeoLabHQ` sobre el scaffold .NET propio |
| Fusionar Autocorrect (`apb-dev-autocorrect-v1.0`, **renombrado** desde `apb-dev-autocorrect-test-v1.0`) | ✅ Hecho — incorpora reflexión general (`NeoLabHQ` plugin `reflexion`) + modo dirigido por test propio |
| Reclasificar API (`third-apollographql-api-design-v1.0`) | ✅ Movido a `skills/third_party/apollographql/` |
| Reclasificar Frontend (`third-google-labs-code-react-patterns-v1.0`) | ✅ Movido a `skills/third_party/google-labs-code/` |
| Reclasificar Implement (`third-neolabhq-sdd-implement-v1.0`) | ✅ Movido a `skills/third_party/neolabhq/` |
| Reclasificar Code Base terceros (`third-neolabhq-ddd-clean-architecture-v1.0`) | ✅ Movido a `skills/third_party/neolabhq/` — al revisar contenido completo, resultó ser un estándar de codificación multi-lenguaje sin solape real con `apb-dev-code-base-v1.0` (que analiza codebases legacy existentes), así que se reclasificó en vez de fusionar |

### Hallazgos adicionales detectados durante la ejecución (pendientes para sesiones siguientes)

1. **Referencias rotas al ID renombrado** `apb-dev-autocorrect-test-v1.0` →
   ahora `apb-dev-autocorrect-v1.0`, encontradas en
   `skills/third_party/obra/third-obra-superpowers-method-v1.0.md` y
   `agents/apb-agent-implementer-v1.0.md`. **Corregir en Sesión 4** (el
   validador de referencias cruzadas las detectará automáticamente).
2. **Doble convención de nombre ya existente dentro de `third_party` antes de
   esta sesión**: subcarpetas `anthropic/` y `mukul975/` ya mezclaban
   `third-{fuente}-{nombre}-v1.0.md` (correcto) con `third_{fuente}_{nombre}
   _v1.0.md` (guion bajo, antiguo). **Normalizar en Sesión 2** junto con el
   resto de nomenclatura.
3. **`source_commit` provisional** (`"main"`) asignado a las 4 skills
   reclasificadas en esta sesión. No es un pin real todavía — se resolverá
   con un commit/tag fijo en la **Sesión 5** (gobernanza de terceros).
4. Pendiente aún de resolver en `skills/apb-owned/development/`: archivos con
   sufijo `_v1_0` (guion bajo) en lugar de `.0` — normalización de nomenclatura
   general, **Sesión 2**.

