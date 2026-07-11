# Retro de sesión — errores en el uso de agentes/skills DDD (2026-07-11)

> **Nota interna de proceso**, no un artefacto DDD. Objetivo: que la próxima sesión que use `apb-agent-ddd-v1.0` (u otro agente que consuma `apb-domain-catalog` como submodule) no repita estos errores.

## Qué pasó

Durante el análisis DDD de SÒSTRAT (`SOSTRAT-Sostrat-MJ8`), se generaron 28 propuestas de dominio/bounded context asumiendo que `apb-domain-catalog` estaba vacío y que la estructura de ficheros destino era la que sugerían los templates locales (`scaffolding/templates/`). Ambas cosas eran incorrectas, y no se detectó hasta que el usuario preguntó explícitamente "¿estás leyendo los dominios del repositorio independiente?".

## Errores concretos

1. **Submodule leído sin `git fetch` previo.** `domain-catalog/catalog/DOMAINS.md` se leyó de la copia local del submodule, que estaba 4 commits por detrás del remoto (`c90668d` local vs. `e753d3e` en `origin/main`). El remoto tenía **21 dominios de negocio ya `proposed`**, de una sesión de análisis previa top-down. Conclusión errónea: "el catálogo está vacío, no hay riesgo de duplicado" → se inventaron 6 dominios nuevos que solapaban/competían con 13 de los 21 ya existentes.
2. **Estructura de ficheros destino asumida, no verificada.** `pr-instructions.md` (v1/v2) describía una estructura plana (`domains/dom-*.md`, `bounded-contexts/bc-*.md`) que no existe — la real (`domains/<nombre>/domain.md` + `domains/<nombre>/contexts/<contexto>.md`) estaba documentada en el `README.md` del propio `apb-domain-catalog`, no leído hasta la tercera pasada.
3. **Valor de `status` incorrecto.** Los 28 ficheros se marcaron `status: "proposed"` cuando `GOVERNANCE.md` define ese valor como asignado "al abrir PR" — el valor correcto para un hallazgo de agente sin PR todavía es `"discovered"`. El propio template lo indicaba en un comentario y aun así se generó mal.
4. **Recuento inconsistente.** Se dijo "19 bounded contexts" varias veces en el chat cuando el recuento real era 22 (luego 21 tras retirar duplicados) — no se hizo una verificación mecánica (`ls | wc -l`) contra lo afirmado en prosa.

## Causa raíz común

En los 4 casos: se generó contenido basándose en **supuestos plausibles sobre un sistema externo** (el catálogo, su estructura, su gobernanza) en lugar de **leer el estado real de ese sistema externo** antes de generar. El framework ya tenía la instrucción correcta ("consulta el catálogo antes de proponer", en `apb-agent-ddd-v1.0.md`), pero no especificaba *cómo* verificar que esa consulta reflejaba el estado actual, no una copia potencialmente obsoleta.

## Medidas mitigadoras aplicadas

1. **Parche a `agents/apb-agent-ddd-v1.0.md`**: la Fase 1 ("Consulta al catálogo") ahora especifica explícitamente `git fetch` + comparación local vs. `origin/<rama>` antes de leer cualquier submodule como fuente de verdad, y añade una restricción nueva sobre no asumir estructura de ficheros de un repo externo sin leer su propio README/GOVERNANCE/schemas.
2. **Memoria guardada** (`feedback_verificar_repos_externos_antes_generar.md`) para que futuras sesiones en este proyecto apliquen la misma verificación sin depender de que el usuario la pida.
3. Este documento, como registro de qué específicamente falló y por qué, para revisión de Arquitectura APB si se decide auditar el proceso de generación de propuestas DDD.

## Qué NO se hizo (deliberadamente fuera de alcance)

No se ha corregido automáticamente el puntero del submodule `domain-catalog` en `APB-IA-FRAMEWORK` (sigue apuntando a `c90668d`, desactualizado) — es un cambio de estado (commit) que requiere confirmación explícita del usuario, no una corrección de contenido de análisis. Se recomienda como acción de seguimiento: `git submodule update --remote domain-catalog` desde la raíz de `APB-IA-FRAMEWORK`, revisar el diff, y commitear el bump.
