# Sesión 4 — Validador Completo y Robusto

> Estado: EJECUTADO. La base del validador ya se construyó en la Sesión 0
> y se reforzó en las Sesiones 1-3; esta sesión añade las validaciones de
> integridad que solo eran detectables con el corpus ya normalizado.

## Validaciones nuevas añadidas a `scripts/validate_repo.py`

1. **Referencias rotas en el cuerpo del documento** (no solo en frontmatter)
   — escanea cualquier mención `` `id-con-version` `` en el cuerpo markdown
   y la contrasta contra los 203 IDs reales. Severidad `WARNING` (no
   `ERROR`) a propósito: algunas roturas son gaps de catálogo genuinos que
   requieren una decisión humana (crear el componente o reformular el
   texto), no solo una corrección mecánica de ID.
2. **Coherencia bidireccional agente↔subagente** — si un agente lista un
   subagent en `subagents:`, ese subagent debe declarar el ID (no el
   nombre legible) de ese agente en `parent_agent`. Severidad `ERROR`.
3. **Dependencias circulares en `depends_on`** — detecta pares A↔B que se
   declaran mutuamente como dependencia. `depends_on` representa
   prerrequisito de ejecución y no debe ser simétrico; relaciones
   complementarias genuinas deben documentarse en el cuerpo, no en este
   campo. Severidad `ERROR`.

## Correcciones aplicadas durante esta sesión

| Hallazgo | Corrección |
|---|---|
| `apb-arch-ddd-discovery-v1.0` (ID inventado, no existe) en `apb-dev-code-base-v1.0.md` | → `apb-arch-ddd-v1.0` (real) |
| `apb-arch-api-design-v1.0` (no existe) en `apb-dev-api-standard-v1.0.md` | → `apb-arch-api-contract-v1.0` (equivalente real más cercano) |
| `apb-qa-validation-v1.0` (sufijo perdido) en `apb-qa-test-strategy-v1.0.md` | → `apb-qa-validation-e2e-v1.0` |
| `apb-agent-qa-engineer-v1.0` (no existe) en 2 archivos de `qa/` | → `apb-agent-qa-auto-v1.0` (agente real) |
| `apb-dev-unit-test-gen-v1.0` / `apb-dev-verification-v1.0` (dominio incorrecto) en `apb-sub-dev-parallel-v1.0.md` | → `apb-qa-unit-test-gen-v1.0` / `apb-qa-verification-before-completion-v1.0` |
| 12 subagentes con `parent_agent` en formato nombre legible en vez de ID | Normalizados a ID real (p. ej. "Governance Agent" → `apb-agent-governance-v1.0`) |
| Dependencia circular `apb-dev-review-tl-v1.0` ↔ `apb-dev-review-advanced-v1.0` | Eliminada la dirección incorrecta; la relación real es unidireccional (TL depende de Advanced). Documentada como "relacionada" en el cuerpo de Advanced. |

## Gaps de catálogo detectados, NO corregidos (requieren decisión, no son errores de tipeo)

| Referencia | Dónde aparece | Naturaleza del gap |
|---|---|---|
| `apb-agent-code-reviewer-v1.0` | `apb-dev-api-standard-v1.0.md`, `apb-dev-code-review-v1.0.md` | No existe ningún agente de revisión de código dedicado; el más cercano es `apb-agent-implementer-v1.0`, que incluye code review entre sus skills pero no es un agente especializado en ello. Heredado del contenido original de terceros (Apollo, NeoLabHQ) que asumía un agente que este framework no tiene. |
| `prov-akv-v1.0` | `apb-agent-business-analyst-v1.0.md` | No existe ningún provider dedicado a Azure Key Vault; los 9 providers reales no cubren gestión de secretos como tal. |

**Recomendación:** evaluar en una sesión futura si conviene (a) crear estos
2 componentes formalmente, o (b) reformular el texto que los menciona para
no asumir su existencia. No se decide en esta sesión porque excede el
alcance de "validador" hacia "completar catálogo".

## Verificación final

- `python3 scripts/validate_repo.py`: **4 errores** (los 4 `source_commit:
  "HEAD"`, diferidos a Sesión 5), **5 warnings** (2 carpetas `tests/`/`docs/`
  diferidas a Sesión 7, y los 2 gaps de catálogo de arriba más uno ya resuelto).
- `python3 scripts/generate_catalog.py --check`: sin drift, exit 0.
