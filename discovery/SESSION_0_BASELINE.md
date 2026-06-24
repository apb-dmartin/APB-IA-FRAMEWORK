# Sesión 0 — Línea Base de Validación

> Generado automáticamente al cierre de la Sesión 0, ejecutando el validador
> corregido (`scripts/validate_repo.py`) sobre el estado del repositorio
> heredado, antes de cualquier corrección de contenido.

## Resumen

| Métrica | Valor |
|---|---|
| Errores | 274 |
| Warnings | 3 |
| Infos | 57 |
| Componentes con ID detectado correctamente | 8 de ~170 |

## Desglose por tipo de error

| Tipo de error | Ocurrencias |
|---|---|
| Frontmatter YAML ausente o malformado | 121 |
| Campo obligatorio común ausente | 126 |
| Campo obligatorio específico del tipo ausente | 21 |
| `source_commit: "HEAD"` no permitido | 4 |
| Carpeta recomendada no encontrada | 2 |
| ID duplicado entre dos archivos | 1 |

## Interpretación

Esta línea base confirma, con evidencia ejecutable y no solo inspección manual,
el diagnóstico de la auditoría inicial:

1. **El 100% de `agents/`, `subagents/`, `workflows/`, `providers/`, `wrappers/`
   y `adapters/` carece de frontmatter YAML** y usa en su lugar texto markdown
   libre (`> **ID:** ...`). Hasta que la Sesión 2 normalice estos archivos, el
   validador seguirá reportando estos 121 casos como error — es el
   comportamiento esperado y correcto, no un fallo del validador.
2. Solo las **skills** mejor gobernadas (mayoritariamente algunas `apb-owned`
   recientes y los descriptores `third_party`) ya cumplen el esquema y pasan
   sin error.
3. El **ID duplicado capturado** (`apb-dev-code-base-v1.0`, presente en dos
   archivos distintos) confirma el hallazgo manual de la auditoría: el
   validador ahora detecta automáticamente este tipo de problema, que antes
   pasaba inadvertido porque el script ni siquiera podía ejecutarse.
4. Los `source_commit: "HEAD"` detectados corresponden a los wrappers de
   terceros que se corregirán en la Sesión 5 (gobernanza de terceros).

Este documento se conserva como evidencia histórica del punto de partida.
No se actualiza retroactivamente; cada sesión posterior genera su propio
informe de progreso.
