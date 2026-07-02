# FEATURES.md — Feature List machine-readable (plantilla)

> ⚠️ **Borrador generado por IA** (APB AI Framework — scaffold harness-ready) — pendiente validación humana.
>
> **Plantilla.** Primitivas de control (SYSTEM.md §10.5): cada funcionalidad tiene
> **estructura triple** — comportamiento + comando de verificación + estado.
> **Pass-State Gating** (GOVERNANCE.md §8.1): solo el harness, tras ejecutar el
> comando de verificación con éxito, cambia el estado a `passing`. El agente NUNCA.
>
> Estados válidos: `not_started` · `active` · `blocked` · `passing`

| ID | Comportamiento esperado | Comando de verificación | Estado | Evidencia |
|----|------------------------|-------------------------|--------|-----------|
| F-001 | {Qué hace la funcionalidad, observable desde fuera} | `{comando exacto, p. ej. pytest tests/test_f001.py}` | `not_started` | — |
| F-002 | {…} | `{…}` | `not_started` | — |

## Reglas

1. **WIP=1:** como máximo una fila en estado `active`.
2. `blocked` exige indicar el bloqueador en Evidencia (y reflejarlo en `PROGRESS.md`).
3. `passing` exige en Evidencia: fecha + salida resumida del comando de verificación.
4. Un `passing` que vuelve a fallar en regresión se degrada a `active` inmediatamente.
