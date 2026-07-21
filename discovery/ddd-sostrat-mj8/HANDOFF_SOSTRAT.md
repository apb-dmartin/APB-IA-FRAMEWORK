# Handoff Técnico SÒSTRAT — Pendientes específicos de la descomposición DDD

> ⚠️ Borrador generado por IA (Claude, Anthropic) — pendiente de validación por Arquitectura APB.
> **Para:** Equipo técnico APB (Arquitectura, equipo SÒSTRAT, Ciberseguridad, domain experts por dominio)
> **De:** Arquitectura APB — Débora Martín
> **Creado:** 2026-07-21 (separado de `discovery/HANDOFF_TECNICOS.md` a petición explícita del
> usuario: el handoff del framework y el de SÒSTRAT deben vivir en documentos distintos, mientras
> que `PLAN_FASES_FUTURAS.md`/`PLAN_FASES_COMPLETADAS.md` siguen unificados framework+SÒSTRAT).
> **Alcance de este documento:** solo tareas manuales de producción real específicas de la
> descomposición DDD de SÒSTRAT (coordinación con equipos propietarios de aplicaciones externas,
> revisión/push de bounded contexts, decisiones de publicación, acceso al código fuente del
> monolito). Los pendientes del framework APB-IA-FRAMEWORK en general (bugs, gobernanza de
> componentes, integraciones M365/Rovo, Design System, telemetría, QA de otras aplicaciones como
> TruckCenter) viven en [`discovery/HANDOFF_TECNICOS.md`](../HANDOFF_TECNICOS.md) — no se
> duplican aquí. Las decisiones/insumos de negocio que Débora/Dirección deben aportar viven en
> `discovery/PLAN_FASES_FUTURAS.md` Sección A (framework y SÒSTRAT unificados ahí).
>
> **Nota de proceso:** no crear documentos de handoff sueltos adicionales para SÒSTRAT — cualquier
> hallazgo nuevo de esta categoría se añade aquí. Los IDs (`DC*`, `S9`, `ACC2`) se conservan tal
> como estaban en `HANDOFF_TECNICOS.md` antes de la separación (principio de conservación de ID,
> mismo criterio que el check #21 de `validate_repo.py`) — no se han renumerado para no romper
> referencias cruzadas ya existentes en el repo.

---

## Pendientes de la serie DDD SÒSTRAT (`discovery/ddd-sostrat-mj8/`)

> Repositorio: `APB-DOMAIN-CATALOG` (submodule `domain-catalog`) — bounded contexts de SÒSTRAT
> modelados sobre código real (2026-07-11 a 2026-07-21). Ver
> [`discovery/HANDOFF_TECNICOS.md` §6](../HANDOFF_TECNICOS.md) para el proceso general de
> gobernanza del catálogo de dominios (DC1/DC2, aplicable a cualquier dominio, no solo SÒSTRAT).

| # | Tarea | Prerrequisito | Estado |
|---|-------|--------------|--------|
| DC4 | **Validación humana de toda la serie DDD SÒSTRAT** (24 dossiers, 27 bc-*.md, specs, backlog) — según `readiness-assessment.md` v6, sigue siendo uno de los bloqueos reales antes de sprint planning; todo el árbol sigue en `status: "discovered"`. Ver `discovery/ddd-sostrat-mj8/INFORME_EJECUTIVO.md` para la síntesis completa | Arquitectura APB + domain experts por dominio | ⬜ Pendiente |
| DC5 | Confirmar `parent_domain` de `bc-tramites-cliente-v1` — desajuste semántico detectado 2026-07-14 entre el dominio real `dom-administracion-electronica-v1` (integración AGE) y el alcance de Trámites de Cliente (gestiones ante APB, no ante el Estado) | Arquitectura APB | ⬜ Pendiente |
| DC6 | Identificar dominio de 7 apps del lote de 33 planes de pruebas sin cobertura en `apb-domain-catalog`: `ADV`, `DGT`, `FLU`(`APB.API.FIL`), `MPS`, `MPT`, `NTA`, `RCF` — 4 ya trackeadas en `discovery/ddd-sostrat-mj8/repo-domain-coverage.md`, 3 (`ADV`/`FLU`/`RCF`) nunca auditadas (ni clonadas localmente) | Análisis DDD dedicado o confirmación de negocio | ⬜ Pendiente, sin urgencia |
| DC7 | **Coordinar con los equipos propietarios de 9 aplicaciones reales con dependencia directa no documentada sobre datos de SÒSTRAT** (`APB.API.CPR`, `APB.API.IPB`, `APB.API.CTS`/`APB.APP.CTA`, `APB.API.AUT`, `APB.API.REB`, `apb.p51`, `APB.API.LRT`/`LRG`, `APB.API.OPS`, `APB.API.CRE`/`APB.APP.CRE`/`APB.API.VXL`/`APB.API.SLC`) — detalle completo y evidencia en `discovery/ddd-sostrat-mj8/EXTERNAL_CONSUMERS_AUDIT.md`. **Bloqueante crítico** antes de ejecutar (no solo documentar) cualquier extracción de Transporte Terrestre, PPS, Facturación, Buques, Escalas, Suministro Eléctrico, SCPP, Manifiestos, Aduanas o Cruceros — 3 de los 9 escriben directamente en tablas Oracle de SÒSTRAT | Arquitectura APB + equipos propietarios de cada app | 🔴 Pendiente, crítico |
| DC8 | ✅ **Cerrado 2026-07-14** — Re-derivación desde código completada para las 24/24 dossiers SÒSTRAT (Sesión 30.8+30.9+30.10) — 7 correcciones puntuales encontradas y aplicadas en total, ninguna de tipo "dato inventado". Ver `PLAN_FASES_FUTURAS.md` #100 e `INFORME_EJECUTIVO.md §3/§4` | — | ✅ Completado |
| DC9 | ✅ **Cerrado 2026-07-14** — Residuo de `coverage-audit.md` cerrado (105→1 rutas sin clasificar, 90 jobs batch clasificados, 3 gaps SOAP resueltos). Hallazgo nuevo, no crítico: `Posicionament` es una capacidad real sin bounded context propio (`PLAN_FASES_FUTURAS.md` #102) | — | ✅ Completado |
| DC10 | **Revisar y empujar el catálogo de dominios preparado localmente** — 27 bounded contexts commiteados en `domain-catalog` (rama `feat/sostrat-bounded-contexts`, `status: "proposed"`, sin push; 24 de la serie DDD original + 3 de la capa EDI/VUA añadidos en DC11). Débora debe revisar el diff y decidir cuándo hacer `git push` + abrir el PR — el agente no lo hace por sí mismo (`autonomy_level 1` de `apb-agent-ddd-v1.0`) | Débora Martín | ⬜ Pendiente de revisión |
| DC11 | ✅ **Cerrado 2026-07-21** — **Materializado el resto del diseño de arquitectura de eventos EDI/VUA** (`PLAN_FASES_FUTURAS.md` #103): eventos nuevos en `events-catalog.md` (§1, §2, §8, §12, §16 — `OperacionTerminalRegistrada`/`ConciliacionCoarriProcesada`/`ListaPasajerosDeclarada`/`ListaPasajerosConfirmada`/`PreavisoCodecoProcesado`/`PreavisoCopinoRespondido`/`PartidaManifestadaViaEdi`/nota `MercanciaAsociadaAEscalaRegistrada`), los 4 proposals actualizados (`bc-aduanas-contenedores-v1`/`bc-cruceros-v1`/`bc-transporte-terrestre-v1`/`bc-manifiestos-v1`), nuevo `specs/asyncapi-integraciones-edi.yaml` + placeholder `MensajeCodecoProcesado` cerrado en `asyncapi-fase2.yaml`, `catalog-comparison.md:44`/`coverage-audit.md` (fila `coarri`) corregidos, y los 3 bounded contexts nuevos preparados en `domain-catalog` (VUA≠EMSWe corregido — ver DC10) | Equipo SÒSTRAT / Arquitectura APB | ✅ Completado (pendiente validación humana, igual que el resto de la serie #96) |

## Seguridad y publicación

| # | Tarea | Urgencia | Responsable |
|---|-------|---------|-------------|
| S9 | **Decidir destino de publicación de la serie DDD SÒSTRAT** (Sesión 30, 2026-07-14) — 24 dossiers + specs con información de negocio real (estructura de datos interna, integraciones externas no documentadas, volúmenes de fan-out) siguen solo en commits locales (`c631fc2`, `c6dd4fe`, `5513c72`); `apb-dmartin/APB-IA-FRAMEWORK` es un repositorio **público**. No pushear sin decisión explícita de Débora sobre repo destino (privado/interno vs. público actual) | Crítica — antes de cualquier `git push` de estos commits | Débora |

## Acceso al código fuente

| # | Qué se necesita | Desbloquea | Responsable |
|---|---|---|---|
| ACC2 | **Reabierto 2026-07-21** — Acceso al código del monolito SÒSTRAT (Java/Oracle → DOCKS), necesario de nuevo para cerrar 5 residuos concretos. El checkout que se usó del 2026-07-11 al 2026-07-14 (Sesión 30, ver `CONTINUIDAD_PROYECTO.md`) **no persiste entre sesiones** — no está ni ha estado nunca dentro de este repositorio (confirmado 2026-07-21, 0 ficheros `.java` en todo `APB-IA-FRAMEWORK`), así que cualquier lectura adicional de código requiere que Plataforma/equipo SÒSTRAT vuelva a facilitar acceso. Residuos concretos que este acceso desbloquearía, de menor a mayor esfuerzo: **(a)** confirmar la columna BBDD real de `Garantia.exprovisional` (javadoc ambiguo/duplicado, `events-catalog.md §7`); **(b)** volcar campo a campo las ~25 clases de segmento EDIFACT de `codeco/`/`copino/` (`CodecoTT.java`/`MissatgeEdiCodecoTT.java`, ya localizadas en `dossier-09-transporte-terrestre.md §5`, solo falta el detalle) para ampliar `PreavisoCodecoProcesado`/`PreavisoCopinoRespondido`; **(c)** escribir un dossier dedicado a `service/coarri/` (nunca auditado por ninguno de los 24 dossiers) para fundamentar `OperacionTerminalRegistrada`/`ConciliacionCoarriProcesada`; **(d)** recuperar el DTO real de PAXLST (`CN_Escala_PAXLST_Impl.java`, nunca localizado, posible candidato: repo hermano `SOSTRAT-Sostrat-JEE`) para `ListaPasajerosDeclarada`/`ListaPasajerosConfirmada`; **(e, ya conocido)** Aguada (`SaSolicitud`/`SaRegistreSuministre`, `PLAN_FASES_FUTURAS.md` #93(d)) — su DTO real ni siquiera estaba en el checkout de 2026-07 (solo compilado en `sostrat.jar`), es el único de los 5 que no se resuelve solo con reabrir el mismo checkout | Plataforma / equipo SÒSTRAT |
