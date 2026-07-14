# Evaluación de preparación — ¿puede arrancar la transformación de SÒSTRAT? (v5, tras cierre de los 24 dossiers + corrección de specs)

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.
> **v3 (2026-07-11, mismo día)**: extendido el cierre de la v2 (que cubría solo Fase 0-1) a las 14 aplicaciones de Fase 0-4. Fase 5 (Escalas) se trata aparte por naturaleza distinta — ver `migration-readiness-fase5.md`.
> **v4 (2026-07-13) — CORRECCIÓN IMPORTANTE**: la v3 afirmaba "todo lo que se podía cerrar sin personas ya está cerrado". Era **prematuro**. Una auditoría de cobertura (`coverage-audit.md`), ejecutada tras una pregunta directa sobre si el backlog migraba el 100% de la funcionalidad real, encontró que el análisis original cubría solo **~78% de las 1135 rutas Struts reales** de SÒSTRAT — el resto vivía en paquetes de código sin ticket Jira de módulo asociado, por lo que nunca entró en el alcance analizado. Se han añadido 6 bounded contexts nuevos y sigue habiendo un residuo real (~150-180 rutas) sin clasificar. La respuesta directa de abajo queda **sustituida** por la de esta versión.
> **v5 (2026-07-14) — cierre de los 24 dossiers de aplicación final + corrección de 9 specs/documentos**: se completaron los 24 dossiers (23 apps + migración de Escalas), incluidos los 6 BCs nuevos de la auditoría de cobertura, cada uno re-verificado campo a campo contra el código real (no solo generado). Se corrigieron después, contra el checkout real: `dead-code-register.md` (2 falsos positivos retirados, 6 candidatos nuevos añadidos), y 9 specs/documentos con entidades equivocadas, nombres de campo incorrectos o campos faltantes (`openapi-aduanas-contenedores`, `openapi-buques`, `openapi-servicios-auxiliares-cruceros` + 3 docs asociados, `openapi-inspeccion-scpp`, `openapi-tramites-cliente`, `openapi-suministro-electrico-buques`, `openapi-operadores-portuarios`, `coverage-audit.md`). **Esto mejora la calidad/exactitud de lo ya documentado — no cierra el residuo de cobertura del punto 0 de abajo**, que sigue siendo el mismo tipo de trabajo pendiente (105 rutas de paquete raíz sin BC, 100 batch jobs sin auditar job a job, 3 gaps SOAP). Ver `discovery/CONTINUIDAD_PROYECTO.md` Sesión 30 para el detalle completo de esta corrección.

## Respuesta directa (v4)

**No, no todo lo analizable sin personas estaba cerrado — quedaba trabajo de análisis de código real por hacer, y una parte sigue pendiente.** Lo que sí es cierto ahora: el trabajo de análisis adicional posible (identificar qué código corresponde a qué bounded context, o marcarlo como código muerto) se ha hecho hasta ~84% de cobertura medible (BC + infraestructura clasificada), con un ~16% restante explícitamente nombrado como pendiente (no oculto). Ver `coverage-audit.md` para el detalle completo y las cifras. Los specs/testing/threat-model de las Fases 0-4 (§ más abajo) siguen siendo válidos **para lo que cubren** — pero no se puede seguir afirmando que cubren "toda" la Fase 0-4 hasta cerrar ese residuo. Sobre validación humana: sigue siendo necesaria, pero ya no es el único bloqueo — hay trabajo de IA real todavía pendiente (ver Recomendación de secuencia, punto 0).

## Lo que SÍ está — completo para Fase 0-4 (14 aplicaciones) + Fase 6 (6 BCs nuevos, dossiers propios 2026-07-13/14)

- Mapa de dominios/bounded contexts reparentado contra el catálogo real de APB (`catalog-comparison.md`).
- Roadmap de 6 fases con orden de extracción justificado por acoplamiento real de código (`decomposition-roadmap.md`).
- 16 épicas con historias de usuario, criterios de aceptación grounded, tareas técnicas (`jira-backlog.md`).
- Catálogo de 41 eventos con payload grounded (`events-catalog.md`).
- Superficie de recursos REST por fase (`api-surface-by-phase.md`).
- ~45 pantallas con componentes DevExtreme concretos (`ui-screens-backlog.md`).
- **`specs/` — 14 OpenAPI 3.0.3 + 4 AsyncAPI 2.6, uno por fase**, con JSON Schema, ejemplos, RFC 7807, seguridad OAuth2/EntraID, reglas de negocio y manejo de errores por evento. Cubren Datos Maestros de Equipamiento, Ferrocarril, Mano de Estiba, Depotsis, PPS, MARPOL, Aguada (provisional, ver gap), Marinas y Pesca, Transporte Terrestre, MMPP, PIF, Manifiestos, Aduanas/Control de Contenedores, Concesiones, Facturación y Liquidaciones.
- **Testing strategy y threat model completos para las 14 apps** (`testing-strategy-fase0-1.md` + `testing-strategy-fase2-4.md`; `threat-model-fase0-1.md` + `threat-model-fase2-4.md`, 16 amenazas STRIDE identificadas en total).
- **Fase 5 (Escalas)**: tratada por separado en `migration-readiness-fase5.md` — no es una extracción a servicio nuevo, es una migración hacia ARGOS, no le corresponde un OpenAPI de "servicio nuevo".

## Lo que FALTA — y ya no se puede cerrar con más trabajo autónomo

### 1. Validación humana — sigue siendo el único bloqueo real
Todo el árbol de `discovery/ddd-sostrat-mj8/` es `[IA-GEN]`, `status: "discovered"`. Ningún domain expert ni Arquitectura APB lo ha revisado. Varios hallazgos cambian el alcance real del trabajo (Escalas ya no es una extracción, Concesiones/Facturación van separados, Mano de Estiba y Clavegueram tienen dominio propio). **Sin este paso, cualquier equipo que empiece a construir sobre esta base puede estar construyendo sobre una hipótesis equivocada.**

### 2. Gaps de evidencia — 1 de 4 sigue sin cerrar
- ~~DTO de PIF~~, ~~DTO de conciliación de terminales~~ — ✅ cerrados 2026-07-11.
- **DTO fuente real de Aguada** (`SaSolicitud`/`SaRegistreSuministre`) — sigue sin cerrar, no existe en el checkout; requiere recuperar el fuente de IN2, no una relectura de código. `specs/openapi-aguada.yaml` es explícitamente provisional por este motivo.
- Confirmación de MILL/INTDBPRO como sistemas reales o etiquetas obsoletas — requiere confirmación de negocio.

### 3. Decisión pendiente con un equipo externo a SÒSTRAT (Fase 5)
La migración de Escalas hacia ARGOS necesita una sesión formal con el equipo de ARGOS/AOM (ver `migration-readiness-fase5.md`) — no se puede planificar solo desde el lado SÒSTRAT. No bloquea el arranque de las Fases 0-4.

### 4. Lo que ningún artefacto generado puede sustituir
- Capacidad real de equipo y estimación validada (story points ilustrativos, no producto de planning poker real).
- Infraestructura detallada ejecutable (namespaces de Service Bus, pipelines CI/CD, provisioning de Container Apps) — están como tareas en EPIC-00, no como runbook.
- Validación de negocio de los ~15 campos/enums marcados `"dominio de valores no confirmado"` en las specs (p.ej. estados de MARPOL 2-7, PIF, `idestattitol`) — son hipótesis razonables sobre nombres, no confirmaciones.

## ¿Deberían crearse specs nuevas? (verificado 2026-07-14)

**No.** Las 23 apps con extracción real (todas menos Escalas, que es migración hacia ARGOS) ya tienen su OpenAPI propio en `specs/` (14 OpenAPI + 4 AsyncAPI de Fase 0-4, más `openapi-buques`/`openapi-operadores-portuarios`/`openapi-servicios-auxiliares-cruceros`/`openapi-inspeccion-scpp`/`openapi-tramites-cliente`/`openapi-suministro-electrico-buques` de Fase 6 = 20 OpenAPI + 4 AsyncAPI, verificado por listado de `specs/`). Dos casos que parecen "sin spec" son correctos por diseño, no gaps:
- **Efficiency Network** (`bc-efficiency-network-v1`) — no tiene ni debe tener spec propio: `EmpresaBC extends Usuari` (herencia real de clase), se modela como extensión del agregado `PortOperator` (Operadores Portuarios), no como microservicio independiente (dossier-22 §6).
- **Escalas** (`dossier-00`) — es una migración de maestría de dato hacia ARGOS, no una extracción a servicio nuevo; no le corresponde un contrato OpenAPI de "servicio nuevo" (ver `migration-readiness-fase5.md`).

Lo que sí falta, verificado en la corrección de 2026-07-14: 9 correcciones puntuales sobre specs ya existentes (entidad equivocada, nombres de campo, campos faltantes) — **ya aplicadas** en esta misma sesión, ver `CONTINUIDAD_PROYECTO.md` Sesión 30.

## Verificación de solapamiento de dominio (2026-07-14)

Cruzados los 6 BCs de Fase 6 contra los 21 dominios de `apb-domain-catalog` y los 21 BCs de Fase 0-4 (`catalog-comparison.md §D`, ya actualizado 2026-07-13): **ninguno duplica un dominio existente** — todos anidan bajo dominios ya propuestos. Un hallazgo no capturado hasta ahora: **`bc-tramites-cliente-v1` → `dom-administracion-electronica-v1` tiene un desajuste semántico sin resolver** — el `domain.md` de ese dominio define su alcance en torno a integración con la AGE (GEISER/Notifica/FACe/Portafirmas/PLACSP), mientras que Trámites de Cliente es sobre gestiones que un operador portuario inicia ante el propio APB, no ante el Estado. Necesita confirmación explícita de Arquitectura APB antes de dar el `parent_domain` por bueno (añadido a `PLAN_FASES_FUTURAS.md` #93).

## Verificación de cobertura de dominio en el lote de 33 apps de QA (2026-07-14)

Cruzados los 33 códigos de aplicación de `planes de pruebas\` contra `apb-domain-catalog` (`related_systems`) y `discovery/ddd-sostrat-mj8/repo-domain-coverage.md` (auditoría previa de 69 repos, 2026-07-11): **26/33 tienen dominio identificado** con confianza razonable. **7/33 no**: `DGT`, `MPS`, `MPT`, `NTA` (ya trackeados como "sin dominio, prioridad baja" en `repo-domain-coverage.md`) y `ADV`, `FLU`/`APB.API.FIL`, `RCF` (**hallazgo nuevo** — ni siquiera entraron en la auditoría de 69 repos porque no están clonados en `GitHub-Repos\otros\`; tienen plan de pruebas pero cero investigación DDD). No es bloqueante para arrancar la transformación de SÒSTRAT (son apps distintas del monolito), pero sí un gap de cobertura del catálogo de dominios a nivel de todo APB.

## Recomendación de secuencia (v4)

0. **NUEVO, antes que nada — cerrar el residuo de `coverage-audit.md`**: investigar los ~150-180 elementos aún sin clasificar (en particular `efficiencyNetwork`, 18 rutas, y el residuo de 105 rutas del paquete raíz de Struts), completar la auditoría de los 100 jobs batch (no hecha job a job), y cerrar los 3 gaps SOAP. Esto es trabajo de IA/análisis de código todavía posible, no bloqueado por personas — no debería tratarse como "ya hecho".
1. **Checkpoint de validación humana** con Arquitectura APB y domain experts sobre `catalog-comparison.md`, `discovery-summary.md` §5 **y `coverage-audit.md`** — incluye ahora también validar los 6 bounded contexts nuevos de la auditoría de cobertura, en particular la decisión de dominio pendiente para `efficiencyNetwork`.
2. En paralelo: recuperar el código fuente real de Aguada con IN2 (bloquea solo esa pieza).
3. Sesión formal con el equipo de ARGOS sobre Escalas (bloquea solo la Fase 5, no el resto).
4. **Una vez cerrados los puntos 0 y 1**: sprint planning real con el equipo, usando `jira-backlog.md` + `specs/` + `testing-strategy-*.md` + `threat-model-*.md` como base de referencia — completos para lo que cubren hoy (~78-84% de la superficie real medida), no para el 100%.
5. Separar la lógica de liquidación de `EscalaAction.java` (única pieza de Fase 5 ejecutable ya, no depende de la sesión con ARGOS).

**En una frase**: sí queda trabajo de análisis de código pendiente para Fase 0-4 (punto 0) — la afirmación anterior de que "no quedaba" era prematura. Una vez cerrado ese residuo, el resto de la recomendación se mantiene: validación humana y sprint planning. Fase 5 tiene su propio camino, distinto por naturaleza (migración, no extracción).
