# Plan de Fases Futuras — Pendiente de Ejecución

> Este documento lista **solo lo que queda genuinamente pendiente**, verificado
> contra el repo real (no contra lo que este mismo documento decía antes de
> comprobarlo).
>
> 📁 **Lo ya ejecutado vive en [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md)**
> — incluye, con fecha 2026-07-06, el histórico íntegro que antes ocupaba este
> fichero (2311 líneas), movido tras una auditoría de verificación de
> completitud (no solo existencia) de 7 rondas contra el código real.
>
> 🚀 **El trabajo de puesta en producción real (Plataforma, Arquitectura,
> Ciberseguridad, admins M365/Atlassian) vive en
> [`HANDOFF_TECNICOS.md`](HANDOFF_TECNICOS.md)** — no se duplica aquí.
>
> **Regla de mantenimiento (obligatoria al cierre de cada sesión):**
> 1. Verificar **completitud** de cualquier entregable citado como cerrado
>    (no solo que el fichero existe — comprobar que cubre lo prometido,
>    dimensión por dimensión) antes de darlo por bueno.
> 2. Mover el histórico verificado, **íntegro** (sin resumir), a
>    `PLAN_FASES_COMPLETADAS.md`.
> 3. Cualquier tarea nueva de producción real va a `HANDOFF_TECNICOS.md`.
>    Cualquier tarea que Claude pueda ejecutar sin más insumos va a la
>    Sección B de aquí. Cualquier decisión de negocio/alcance de Débora (o
>    conjunta con Plataforma) va a la Sección A.
> 4. No crear documentos de handoff/resumen/estado sueltos — se integran en
>    estos 3 documentos canónicos (`PLAN_FASES_FUTURAS.md`,
>    `PLAN_FASES_COMPLETADAS.md`, `HANDOFF_TECNICOS.md`). Si algo necesita
>    vida propia por volumen (una auditoría de una aplicación externa, un
>    runbook operativo), se archiva con puntero desde estos tres, nunca queda
>    huérfano en `discovery/`.

---

## A. Decisiones pendientes de Débora (o Débora + Plataforma)

| # | Decisión necesaria | Desbloquea | Urgencia |
|---|---|---|---|
| #77/#80 | **Motor de orquestación de agentes** — elegir entre (A) Azure Durable Functions [recomendado: ya en stack APB, alto soporte], (B) LangGraph [bajo coste, escalabilidad limitada], (C) Temporal.io [máximo control, nueva infraestructura]. PoC de pausas humanas ya entregada y funcionando (`scripts/orchestrate_checkpoint_gate.py`, `.github/workflows/human-checkpoint-poc.yml`). Decisión conjunta Débora + Plataforma. | Capa de coreografía por eventos, `prov-orchestration-engine-v1.0`, memoria compartida inter-sesiones (#80, ligado a esta misma decisión), `apb-agent-orchestrator-v1.0` | 🔴 Mes 1 |
| #49 | Mecanismo de distribución del Design System: npm privado (Azure Artifacts) / git submodule versionado / CDN corporativo | Sesión 22 — propagación automática a apps APB | 🟡 Mes 1 |
| #23 (parte) | Confirmar si se prioriza la conversión a `.docx` de la documentación (borradores Markdown ya listos: `docs/guia-funcional.md`, `docs/manual-arquitectura.md`, `docs/informe-direccion.md`) y con qué plantilla corporativa | Sesión 14 | 🟡 Mes 1 |
| #6 | Ejemplos reales de plantillas Word/Excel corporativas | Sesión 14 (plantillas ofimáticas) | 🟡 Mes 1 |
| #52 | Email/cola de Jira oficial de Arquitectura (para sustituir referencias a contacto personal en toda la documentación) | Corrección documental transversal | 🟡 Mes 1 |
| #36 | Briefing de los agentes de licitación LCSP: qué documentos concretos deben generar/revisar | Sesión 20 | 🟡 Mes 2 |
| ~~#8~~ | ~~Horas históricas reales de la organización para calibrar conversión puntos↔horas~~ — 🟡 **Aportado 2026-07-08** (12 meses de datos reales de Jira + 3 documentos de metodología). Ver `PLAN_FASES_COMPLETADAS.md §Gap #8`. Categorías con confianza ⚠️/❌ (<50 tickets) siguen indicativas, no concluyentes — histórico sigue creciendo vía `apb-agent-valoracion-tecnica-v1.0` | Calibración `apb-disc-cosmic-v1.0` v2.0.0 + `apb-pm-jira-estimation-review-v1.0` v1.1.0 | 🟢 En progreso continuo |
| #79 | URL/organización exacta de "Fine Skills" (único resto abierto del bloque de terceros #79, ya resuelto en el resto) | Evaluación de incorporación | 🟢 Mes 2-3 |
| #87 | Pasos concretos del proceso de evaluación/migración a Cloud definidos por APB | Reescritura de `apb-wf-cloud-migration-v1.0` con el proceso real (no el genérico de industria actual) | 🟡 Cuando Débora lo aporte |
| N8 | **Runtime de agentes en producción** — qué asistente de IA concreto ejecuta cada agente cuando un empleado lo usa en el día a día (Claude Code, GitHub Copilot, Rovo, M365 Copilot). Hoy el campo `runtime:` del frontmatter es declarativo/aspiracional; no hay mecanismo de invocación real por runtime salvo `scripts/invoke_agent.py` (uso interno Claude). **Distinta de #77** (que es el motor de orquestación de flujos multi-agente, no el runtime de un agente individual). **Mecanismo propuesto (2026-07-07):** MCP Server APB Agents — ver `PLAN_MCP_SERVER_APB.md`, Fase 0 ejecutable ya (Sección B de aquí), Fases 1+ bloqueadas por MCP-1 a MCP-4 abajo | Estrategia de despliegue real a usuarios finales | 🟡 Mes 2 |
| MCP-1 | **MCP Server APB Agents — Fase 1 (auth + despliegue Azure Container Apps):** verificar con prototipo si la autenticación de plataforma de Container Apps es compatible con el flujo de autorización MCP (desafío `401`/PRM), y definir los grupos de Entra ID concretos para los scopes `apb-mcp.read`/`apb-mcp.execute`. Ver `PLAN_MCP_SERVER_APB.md` Fase 1 | Despliegue real del MCP server a Claude Code/Copilot (resuelve N8) | 🔴 Cuando Arquitectura decida avanzar más allá del MVP local |
| MCP-2 | Confirmar orden de prioridad de skills/workflows a exponer en la Fase 3 del MCP Server (`list_skills`/`get_skill_definition`/`list_workflows`) — propuesta sin confirmar: `development` primero, luego `governance` | Ampliación del catálogo del MCP server más allá de las 3 tools del MVP | 🟡 Mes 2 |
| MCP-3 | Verificar contra un tenant real de Atlassian si Forge/Rovo puede consumir este MCP server como tool externa, o si la única vía sigue siendo REST/webhook (`forge/manifest.yml`). Ligado a **#78** (tagging `runtime: rovo`) | Decide si la Fase 5 (Rovo) es extensión del MCP server o arquitectura REST paralela | 🟡 Cuando Débora tenga acceso al tenant |
| MCP-4 | Identificar un caso de uso real de routing a un LLM específico por skill (Fase 6 del MCP Server) — sin caso confirmado hoy, no construir el motor de routing especulativamente | Activación de la Fase 6 del MCP server | 🟢 Sin urgencia, solo si aparece un caso concreto |
| #93 | **5 bloqueantes de decisión DDD SÒSTRAT** (Sesión 30, 2026-07-14, ampliado en la continuación de la misma sesión): (a) fusión PIF (#11) + SCPP (#19) en un único bounded context — evidencia de código a favor, recomienda evaluar también Posicionament en el mismo movimiento; (b) `parent_domain` compartido de Operadores Portuarios (#23) y Efficiency Network (#22) — `EmpresaBC extends Usuari`, resolver uno resuelve el otro; (c) conflicto de planificación Clavegueram (#16) — `jira-backlog.md` EPIC-15 lo trata como extracción independiente, EPIC-13B lo despliega dentro de Facturación, evidencia de código (4 puntos de acoplamiento real) favorece EPIC-13B pero es decisión de producto; (d) gap de evidencia de Aguada (#07) — modelo transaccional de escritura no existe en el checkout auditado, requiere checkout más completo o acceso al equipo IN2 (proveedor); (e) **nuevo, verificado 2026-07-14**: `bc-tramites-cliente-v1` (#20) → `dom-administracion-electronica-v1` tiene un desajuste semántico sin resolver — el dominio real está definido en `domain-catalog` en torno a integración AGE (GEISER/Notifica/FACe/Portafirmas/PLACSP), mientras que Trámites de Cliente es sobre gestiones de un operador portuario ante el propio APB, no ante el Estado; no se ha encontrado ningún otro dominio candidato mejor en el catálogo actual. Detalle completo: `discovery/ddd-sostrat-mj8/app-dossiers/INDEX.md §3`, `readiness-assessment.md` | Continuación del roadmap de descomposición SÒSTRAT (Fases 3 y 6) | 🟡 Mes 1-2 |
| #98 | **9 consumidores/desarrollos externos reales de SÒSTRAT descubiertos 2026-07-14, no contemplados por ningún dossier** — auditoría completa en `discovery/ddd-sostrat-mj8/EXTERNAL_CONSUMERS_AUDIT.md`. Requiere confirmación con cada equipo propietario + decisión de estrategia de convivencia antes de ejecutar (no solo documentar) cualquiera de las extracciones afectadas: (a) `APB.API.CPR` escribe en `INSPECCIO` (SCPP); (b) `APB.API.IPB` escribe en 15+ tablas de Transporte Terrestre/MARPOL (`PESATGE`/`CAMIO`/`CONTENIDOR`...); (c) `APB.API.CTS`/`APB.APP.CTA` lee ~50 tablas de Manifiestos+Aduanas+MMPP+Buques+Ferrocarril; (d) `APB.API.AUT` lee+escribe `AUTORITZACIO` de PPS en tiempo real (tótems físicos); (e) `APB.API.REB`+`apb.p51` leen/escriben `Rebut` de Facturación, P51 incluso crea recibos en SÒSTRAT vía SOAP; (f) `APB.API.LRT` lee Buques y **escribe** en Escalas (triple escritor con ARGOS); (g) `APB.API.OPS` es un puente DWH de solo lectura sobre Suministro Eléctrico, requiere decidir si el nuevo servicio lo alimenta o si se retira; (h) el ecosistema `APB.API.CRE`/`APB.APP.CRE`/`APB.API.VXL`/`APB.API.SLC` ya ES la implementación real de `bc-cruceros-v1` (dossier de aplicación final todavía sin escribir) | Antes de ejecutar cualquier extracción de Transporte Terrestre, PPS, Facturación, Buques, Escalas, Suministro Eléctrico, SCPP, Manifiestos, Aduanas o Cruceros | 🔴 Crítico — bloquea desarrollo, no bloquea documentación |
| #99 | ✅ **Cerrado 2026-07-14** — **Carencia en `agents/apb-agent-ddd-v1.0.md` corregida**: añadida **Fase 0 — Rastreo de consumidores externos** (bump a v1.1.0), con 4 pasos (inventariar repos relacionados, rastrear acceso directo a la fuente de datos, clasificar lectura/escritura, incorporar al mapa de dominios candidatos antes de concluir "sin solapamiento"), nuevo output `external-consumers-audit.md` y nueva restricción explícita de no concluir "sin acoplamiento externo" sin haberla ejecutado | Mejora del propio `apb-agent-ddd-v1.0`, aplicable a cualquier futura descomposición de monolito | ✅ Completado |
| #96 | **Checkpoint de validación humana de toda la serie DDD SÒSTRAT** (24 dossiers + specs + backlog) — sigue siendo, según el propio `readiness-assessment.md` v5 (2026-07-14), el único bloqueo real para empezar sprint planning: todo el árbol de `discovery/ddd-sostrat-mj8/` sigue en `status: "discovered"`, sin revisión de Arquitectura APB ni de ningún domain expert, pese a que varios hallazgos cambian el alcance real del trabajo (Escalas ya no es extracción, Concesiones/Facturación van separados, 6 BCs de Fase 6 nuevos) | Sprint planning real de la transformación SÒSTRAT | 🔴 Antes de cualquier sprint planning |
| #97 | **7 apps del lote de 33 planes de pruebas sin dominio identificado en `apb-domain-catalog`**: `DGT`/`MPS`/`MPT`/`NTA` (ya trackeados como pendientes en `repo-domain-coverage.md`, prioridad baja) y `ADV`/`FLU` (`APB.API.FIL`)/`RCF` (hallazgo nuevo 2026-07-14 — ni siquiera clonados localmente, nunca entraron en la auditoría de 69 repos de `repo-domain-coverage.md`). No bloquea la transformación de SÒSTRAT (son apps distintas del monolito) — gap de cobertura del catálogo de dominios a nivel de todo APB | Cobertura completa de `apb-domain-catalog` | 🟢 Sin urgencia |
| #94 | **Decisión de publicación de la serie DDD SÒSTRAT** — el trabajo de los 24 dossiers (commits `c631fc2`, `c6dd4fe`, `5513c72`) contiene información de negocio real de SÒSTRAT (estructura de datos, integraciones externas no documentadas, volúmenes de fan-out) y sigue solo en commits locales; `apb-dmartin/APB-IA-FRAMEWORK` es un repositorio **público** en GitHub. Débora debe decidir destino de publicación antes de cualquier `git push` de estos commits | Visibilidad pública de contenido confidencial de negocio | 🔴 Antes de cualquier push |
| #95 | **Bump del submodule `domain-catalog`** — sigue apuntando a `c90668d`, 4 commits por detrás de `origin/main` (`e753d3e`) desde la Sesión DDD del 2026-07-11 (ver `discovery/ddd-sostrat-mj8/session-retro-2026-07-11.md`); requiere `git submodule update --remote domain-catalog` + revisión de diff + commit explícito, deliberadamente no ejecutado sin confirmación | Cualquier sesión futura que use `apb-agent-ddd-v1.0` sobre `apb-domain-catalog` como fuente de verdad | 🟡 Antes de la próxima sesión DDD |
| #100 | ✅ **Cerrado 2026-07-14** — **Re-derivación desde código de la serie DDD SÒSTRAT completada: 24/24 dossiers** (Sesión 30.8+30.9+30.10). Un intento inicial de auditar los 24 dossiers con 8 agentes en paralelo falló a mitad de ejecución por un límite de sesión de la API; el usuario eligió proceder directamente (sin subagentes), y en tres rondas se verificaron los 24 dossiers en profundidad, encontrando y corrigiendo **7 inconsistencias reales** (ninguna de tipo "dato inventado" — ver `INFORME_EJECUTIVO.md §3/§4`): payload de evento incompleto (dossier-16), checklist obsoleto (dossier-23), recuento de rutas interno inconsistente y comparación de PK incorrecta (dossier-19, 2 errores), campo mal tipado en spec REST (dossier-01), nota obsoleta sobre nombres de estado propagada en 6 ficheros (dossier-06), y recuento de rutas de Escalas nunca cruzado contra `coverage-audit.md` (dossier-00). 17 de 24 dossiers no tenían ningún error | Cierre definitivo de la calidad de la serie DDD SÒSTRAT antes de sprint planning | ✅ Completado |
| #101 | ✅ **Cerrado 2026-07-14** — **Residuo de `coverage-audit.md` cerrado**: los 105 elementos del paquete raíz sin clasificar, los 8 módulos pequeños de §1.2, los 3 gaps SOAP y los 90 jobs de Spring Batch (recuento exacto, no la estimación previa de "100") — todos clasificados con evidencia de código real (import de servicio/DTO), no por nombre de fichero. Detalle completo en `coverage-audit.md §8`. Residuo final: **1 sola ruta genuinamente sin clasificar** (`DatosBasicos`) | Cobertura funcional completa de SÒSTRAT antes de dar el catálogo por definitivo | ✅ Completado |
| #102 | **Hallazgo nuevo del cierre de #101 — `Posicionament` es una capacidad de negocio real sin bounded context propuesto**: 19 rutas Struts (`Posicionament*`, `Incidencia*`) + 2 jobs batch (`posicionamientoEDI`, `avisosIncidencias`) + el servicio `CN_Posicionament_Impl.java` (1.873 líneas, ya citado en `dossier-19-inspeccion-scpp.md §7` por su acoplamiento síncrono con SCPP) no tienen ningún `proposals/bc-posicionament-v1.md`. Requiere una sesión de investigación dedicada (mismo alcance que cualquiera de los 24 dossiers existentes: agregados, PK, campos, eventos) antes de poder enviarse al catálogo de dominios. Ver `coverage-audit.md §8.2` | Completar el mapa de bounded contexts de SÒSTRAT antes del checkpoint de validación humana (#96) | 🟡 Mes 1-2, no bloqueante para #96 |
| #103 | **Diseño de arquitectura de eventos para la mensajería EDI/Ventanilla Única completado (2026-07-15), materialización parcial** — a petición explícita del usuario, se analizó la transformación de la mensajería EDI/VUA a arquitectura de eventos (`discovery/ddd-sostrat-mj8/edi-event-architecture-analysis.md`) y se crearon 3 propuestas de bounded context nuevas (`proposals/bc-integracion-edi-portic-v1.md`, `bc-vua-sapl-v1.md`, `bc-dms-emswe-v1.md`). Queda pendiente, diferido explícitamente por decisión del usuario (alcance de esa misma sesión): (a) añadir los eventos nuevos a `events-catalog.md` para los 5 BCs de negocio afectados (Aduanas/Contenedores: `OperacionTerminalRegistrada`/`ConciliacionCoarriProcesada`; Cruceros: `ListaPasajerosDeclarada`/`ListaPasajerosConfirmada`; Transporte Terrestre: `PreavisoCodecoProcesado`/`PreavisoCopinoRespondido` — cierra el gap ya conocido `MensajeCodecoProcesado`; Manifiestos: `PartidaManifestadaViaEdi`; futuro bc-escalas-v1: `MercanciaAsociadaAEscalaRegistrada`/BERMAN); (b) actualizar los proposals existentes `bc-aduanas-contenedores-v1.md`/`bc-cruceros-v1.md`/`bc-transporte-terrestre-v1.md`/`bc-manifiestos-v1.md` con esos eventos; (c) nuevo `specs/asyncapi-integraciones-edi.yaml` + cerrar el placeholder de `MensajeCodecoProcesado` en `asyncapi-fase2.yaml:90`; (d) corregir `catalog-comparison.md:44` (cerrar la divergencia EDI dominio-propio-vs-repartido, referenciando este análisis) y `coverage-audit.md` (fila `coarri`); (e) preparar localmente (sin push, mismo patrón que #101) los 3 bounded contexts nuevos en el submodule `domain-catalog` + corregir `domain-catalog/domains/integraciones-edi/domain.md` (hoy describe VUA como si fuera la EMSWe europea — es incorrecto, el circuito FAL/EMSWe real es DMS) y poblar `bounded_contexts` en `inspeccion-control/domain.md`/`operaciones-maritimas/domain.md` | Completar la transformación de la mensajería EDI/VUA antes de enviar esos bounded contexts al catálogo de dominios real | 🟡 Mes 1-2, no bloqueante para #96 |
| N9 | **Configurar Obsidian** — definir con Débora: ¿vault sobre `discovery/` (o todo el repo)?, ¿qué plugins (grafo de enlaces `[[...]]` ya usado en memoria, Dataview, Kanban)?, ¿uso personal o compartido con el equipo? Sin estas respuestas no es ejecutable — no es un componente del framework, es tooling personal de Débora | Flujo de trabajo personal de Débora sobre la documentación del framework | 🟢 Cuando Débora lo defina |

---

## B. Backlog ejecutable — pendiente de planificación, no de insumos externos

Trabajo que Claude puede ejecutar en cualquier sesión sin depender de una
decisión o dato externo. Sigue siendo trabajo **pendiente** — solo pendiente
de que se le asigne turno, no de que alguien lo desbloquee.

| Ítem | Qué es | Origen |
|---|---|---|
| **Construir MVP local del MCP Server APB Agents (Fase 0)** | Servidor MCP stateless con exactamente 3 tools (`list_agents`, `get_agent_instructions`, `get_apb_knowledge`), transporte `streamable-http`, Python + SDK oficial `mcp`, contenedor Docker con el repo montado read-only (`/repo`), sin auth ni telemetría (explícitamente fuera de alcance v1). Resuelve de raíz el gap **N8** (no hay hoy mecanismo de invocación real por runtime, solo el simulador `scripts/invoke_agent.py`). Checklist de "hecho" y detalle completo (incluidas Fases 1-7, todas con blocantes propios — ver tabla MCP-1 a MCP-4 en Sección A) en [`PLAN_MCP_SERVER_APB.md`](PLAN_MCP_SERVER_APB.md) | Sesión de arquitectura con Débora, 2026-07-07 |
| ~~Wiring de 5 subagentes~~ **— ✅ VERIFICADO (2026-07-07)** | Ya estaban correctamente wireados en ambos sentidos en el repo real — ver detalle en [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md#wiring-de-5-subagentes--verificado-2026-07-07) | R2 (revisión 360° 2026-06-29) |
| Sincronizar cifras de componentes en `HANDOFF_TECNICOS.md` | Regenerar catálogo y corregir las 3 menciones desfasadas (345/347/341 → cifra real) | BUG-07 (ya definido, no ejecutado) |
| Ampliar `apb-gov-org-risk-report-v1.0` | 2 de 7 marcos normativos (LCSP, RGPD-adjacent WCAG) están mencionados sin checklist operativo propio — desarrollar criterios de evaluación igual que ENS/ISO/NIST/RGPD/OWASP | Hallazgo de esta auditoría (2026-07-06) |
| Cerrar 3 de 4 gaps de enforcement de autonomía | Timeout policy, loop detection, hardcoded limits por nivel (el 4º, async messaging vía Service Bus/Kafka, requiere infraestructura → en `HANDOFF_TECNICOS.md`) | #41 / análisis de autonomía 2026-07-06 |
| Formalizar loops / Goal-Driven Execution | Documentar como skill/estándar una vez el motor de orquestación esté decidido (#77) — el diseño conceptual ya existe, falta materializarlo | #12, #24, #29 |
| Capa formal de `capabilities/` | Carpeta con descriptores de capacidades de negocio (Generar Especificaciones, Revisar Código, Diseñar Arquitectura...) | E-T4 |
| Caching de outputs de agentes | Caching por hash de input para workflows que reprocesan el mismo artefacto | E-T5 |
| SBOM automatizado + supply-chain CI | Extender `generate_catalog.py` con sección SBOM; GitHub Action de verificación de SHA de origen; auditoría semanal de dependencias (`pip-audit`/`safety`) | E-S1, E-S2, E-S3 |
| Storybook para APB-DESIGN-SYSTEM | Sustituir/complementar `visual-reference.html` con addon a11y (WCAG 2.1 AA) | E-DX2 |
| Wrapper de credenciales desde repositorio central | Provider de secretos (Key Vault) + patrón de captura/reutilización de `storage_state` para que el agente QA no requiera login manual cada vez | Derivado de #82 (Débora, 2026-07-02) |
| ~~Escribir los 32 scripts k6 reales (uno por app del lote QA-continuación)~~ | ✅ **Hecho (2026-07-10):** auditados los 33 planes buscando su bloque de rendimiento → **15/33 ESCRIBIBLE** (script `{APP}-smoke.js` generado en `planes de pruebas\{APP}\k6\`, sintaxis verificada con `k6 archive`), **4/33 NO_APLICA** (rendimiento no-HTTP o carpeta legacy superseded), **14/33 BLOQUEADO** (sin endpoint documentado — falta info de Dev, no se fabricó ningún dato). Detalle completo por app: `planes de pruebas\K6_SMOKE_SCRIPTS_ESTADO.md`. Entorno local resuelto vía Docker (`infra/azure-qa-runtime/k6/`, imagen `apb-qa-k6-runtime:local` construida y verificada) en vez de instalación nativa — corrección de Débora en vivo tras fallo de descarga nativa de Playwright por el proxy corporativo (ver `EJECUCION_LOCAL.md`, nota pendiente de añadir sobre preferir Docker). Sigue pendiente: ejecutar estos scripts contra PRE con credencial real (requiere login asistido de una persona, `QA2-1`) y ampliar cobertura de las 14 apps bloqueadas cuando Dev aporte el endpoint real. | Auditoría de infraestructura de ejecución, 2026-07-10 (Débora) |
| ~~Confirmar qué apps del lote de 32 tienen project key registrado en Sonar~~ | ✅ **Hecho (2026-07-10):** cruce real vía `GET /api/projects/search?ps=500` (224 proyectos reales, no 100 — la cifra previa estaba truncada por paginación) contra los 33 códigos del lote → 28/33 con key confirmado, 3 candidatos a confirmar con Dev (AOM, SISPEM, SOJA), 2 sin match (AOM_ARGOS-MDE no aplica, SOSTRAT sin key propia). Detalle: `planes de pruebas\SONAR_PROJECT_KEYS_MAPEO.md`; resumen en `HANDOFF_TECNICOS.md` QA3-3. | Auditoría de infraestructura de ejecución, 2026-07-10 (Débora) |
| Desarrollar guía de clasificación de dominios + campos obligatorios | #85(b) descripción estructurada por dominio (tipo de elementos/datos/actividades) y #85(c) guía de criterios de frontera para dominios nuevos — no dependen de la aprobación de Arquitectura de los 21 dominios existentes | #85(b)/(c) |
| Construir skill de ingesta de histórico Jira | La construcción de la skill es ejecutable ya; el acceso real al histórico Jira para probarla es el bloqueante (→ `HANDOFF_TECNICOS.md`) | #37 |
| Reejecutar los 76 casos restantes de TruckCenter | Requiere reabrir la sesión con Playwright MCP cargado desde el inicio (mecánico, no bloqueado por terceros) + corregir H1/H5 localmente donde aplique | #88 |
| ~~**Agente de soporte técnico para analistas funcionales**~~ **— ✅ CREADO (2026-07-06)** | Agente [`apb-agent-functional-technical-support-v1.0`](../agents/apb-agent-functional-technical-support-v1.0.md) + skill nueva [`apb-pm-jira-estimation-review-v1.0`](../skills/apb-owned/pm/apb-pm-jira-estimation-review-v1.0.md). Decisiones tomadas por Débora al crear el componente: **(a)** catálogo de referencias en el repo — [`discovery/ESTIMATION_REFERENCES.md`](ESTIMATION_REFERENCES.md), complemento de la consulta en vivo a Jira hasta reunir ≥20 entradas por categoría, no sustituto; **(b)** unidad de estimación en **horas** (no story points); **(c)** acceso a Jira vía `prov-atlassian-v1.0` (REST, JQL/`search_issues` — no MCP ni Rovo; provider único desde la fusión con `prov-jira-software-v1.0`, ver `PLAN_FASES_COMPLETADAS.md` #91/#92); **(d)** regla de contrapropuesta: se activa si la valoración del ticket supera en **más de un 25%** la media de precedentes comparables, con argumentos citados. **Bloqueante que persiste:** acceso real a histórico Jira (→ `HANDOFF_TECNICOS.md` ACC1) — el componente ya es operativo, falta el aprovisionamiento de credenciales para probarlo en runtime real. **Cruce verificado:** no existe ningún `apb-dev-estimation-*` en el repo (grep completo) — no había nada que reutilizar. | Solicitud de Débora (2026-07-06); creado en la misma sesión |
| **Agente de análisis de logs técnicos (diagnóstico + predicción de incidencias)** | Agente `apb-agent-log-analyst-v1.0` (dominio `operation`): correlaciona logs de múltiples fuentes de infraestructura (Azure Monitor, IIS/Apache/Tomcat, Oracle, K8s/AKS, red, Service Bus, Rancher, Container Apps — orquestando los 8 subagentes de diagnóstico por tecnología ya existentes: `apb-sub-ops-azure/oracle/k8s/iis-apache/network/servicebus/rancher/aca-v1.0`), detecta patrones anómalos y **predice** degradaciones (tendencias, umbrales, correlación temporal) antes de que se conviertan en incidencia — no solo diagnostica a posteriori. Se apoya también en `apb-ops-perf-bottleneck-v1.0` y `apb-ops-incident-diagnose-v1.0`. **Prioridad alta** — pedido explícitamente 3 veces por Débora en la misma sesión. | Solicitud de Débora (2026-07-06), gap analysis |
| **Onboarding para nuevos miembros de SSI** (Departamento de Sistemas de Información) | Skill/guía de onboarding específica para nuevas incorporaciones del propio departamento IT de APB: qué es el framework APB-IA-FRAMEWORK y cómo usarlo, mapa de sistemas propios (SÒSTRAT, GIS, OSMA...), políticas IT de obligado cumplimiento. Distinta de `apb-doc-onboarding-v1.0` (genérica, para onboarding de cualquier producto/cliente). | Solicitud de Débora (2026-07-06) |
| **Plan de validación agente-a-agente antes de producción** | Nuevo documento `discovery/PLAN_VALIDACION_PRODUCCION.md`: checklist por componente (38 agentes, 35 subagentes, 17 workflows) con entrada de prueba mínima, salida esperada, criterio de aceptación humano y quién lo ejecuta (Débora vs Claude). Distinto de QA-3 (testing funcional de TruckCenter, no del framework mismo). | Solicitud de Débora (2026-07-06) |
| **Tagging de agentes que pueden apoyarse en Rovo (Atlassian)** | Revisar los 38 agentes y añadir `"rovo"` a `runtime:` en los que dependan de `prov-atlassian-v1.0` (fusionado con `prov-jira-software-v1.0` el 2026-07-06)/`prov-confluence-v1.0` (incident-support, problem-manager, change-manager, pm, business-analyst, documentation, risk-exception, compliance-audit, vendor-manager, functional-technical-support...). Verificado por grep: **0 agentes tienen hoy `"rovo"`** pese a que el provider ya existe. Nota: "Rovo" aquí es `adapter-rovo-v1.0` (capa de IA, pendiente de activación julio 2026) — no confundir con el transporte REST de los providers Atlassian. | Solicitud de Débora (2026-07-06) |
| **Agente de documentación de licitaciones públicas** | Nuevo agente `apb-agent-tender-writer-v1.0` (dominio `governance`/`pm`): redacta/revisa pliego técnico (PPT), apoya el pliego administrativo (PCAP, con Jurídica), justificación de la necesidad, y evalúa ofertas técnicas de licitadores contra criterios del pliego. Distinto de `apb-wf-vendor-procurement-v1.0` (gestiona el proceso, no redacta contenido) y de `apb-gov-lcsp-check-v1.0` (valida cumplimiento LCSP, no redacta). Cruza con la decisión pendiente **#36** (briefing LCSP). | Solicitud de Débora (2026-07-06) |

| ~~Corrección de 9 specs DDD SÒSTRAT ya publicadas~~ | ✅ **Hecho (2026-07-14, continuación de Sesión 30)** — las 9 correcciones aplicadas y verificadas: `openapi-aduanas-contenedores`+`events-catalog.md` (`TrasllatContenidor` real, no `MovimientoContenedor`), `openapi-buques.yaml` (68/68 campos, tipos verificados contra `Vaixell.java`), `openapi-servicios-auxiliares-cruceros.yaml`+3 docs (remodelado sobre `CreuerBus`/`CreuerVigilanciaPunt` reales), `openapi-inspeccion-scpp.yaml`+3 docs (PK compuesta real), `openapi-tramites-cliente.yaml`+2 docs (nombres de campo reales), `openapi-suministro-electrico-buques.yaml`+`events-catalog.md` (`idestat` añadido, `navinternacional` corregido), `openapi-operadores-portuarios.yaml` (`CompteBancari` añadido, `eseffnetwork` corregido), `dead-code-register.md` (3 falsos positivos corregidos + 6 candidatos nuevos), `coverage-audit.md` (89→56 rutas Transporte Terrestre). Detalle completo: `CONTINUIDAD_PROYECTO.md` Sesión 30.5 | Sesión 30 (2026-07-14) |
| Formalizar skill "dossier de aplicación" | El formato de los 24 dossiers SÒSTRAT (17 secciones: funcional/técnico/datos/arquitectura/pantallas/APIs/eventos/convivencia/testing/seguridad/riesgos/estimación/checklist) se sintetizó combinando `apb-disc-spec-gen-v1.0` + `apb-pm-product-analysis-v1.0` + `apb-arch-c4-model-v1.0` + `apb-arch-decompose-v1.0`, sin skill dedicada. Formalizar solo si el formato se reutiliza en una segunda descomposición de monolito | Sesión 30 (2026-07-14), INDEX.md §5.4 |

### B.2 — Candidatos del gap analysis 2026-07-06 (cobertura total dpto. IT)

> Respuesta a "¿qué agentes, skills, flujos, MCP, utilidades nos faltarían
> para dar apoyo de IA a cualquier tarea de un departamento IT?". El
> catálogo actual (362 componentes) cubre con profundidad el ciclo de vida
> del software y el ITIL técnico; los huecos están en todo lo que un
> departamento IT hace además de construir software. Ningún ítem tiene
> descriptor creado — son candidatos sin priorizar por Débora.

**Agentes/skills sin cubrir:**

| # | Hueco | Detalle | Prioridad |
|---|---|---|---|
| G1 | Service Desk / soporte a usuario final (request fulfillment ITIL) | Triage de solicitudes no-IT, autoservicio, KB para usuarios finales. Lo existente es incidencia técnica, no solicitud de servicio | Alta |
| G2 | Identidades y accesos: JML + recertificación | Alta/traslado/baja de empleados; revisión periódica de accesos (ENS). `apb-sub-ops-entra` es solo diagnóstico | Alta |
| G3 | ITAM/SAM: activos y licencias | Inventario HW/SW, reconciliación CMDB, renovaciones con avisos proactivos | Media |
| G4 | Ingeniería de datos / BI de negocio | Pipelines ETL, calidad de datos, informes al negocio (distinto de los dashboards del propio framework) | Media |
| G5 | Gestión de la demanda / portfolio IT | Petición de negocio → business case con ROI → cartera anual. `apb-pm-*` es nivel proyecto | Media |
| G6 | ENI (Esquema Nacional de Interoperabilidad) | Hay ENS/LCSP/RGPD; ENI → 0 resultados en el repo | Media |
| G7 | Adopción y cambio organizativo (OCM) | Formación, comunicados, planes de adopción (p. ej. M365 Copilot). El change-manager actual es ITIL técnico | Baja |
| G8 | Actas y seguimiento de reuniones | Skill sobre `prov-ms365-v1.0` (transcripciones Teams → actas + acciones). Quick win: provider ya catalogado | Alta |
| G9 | Puesto de trabajo digital (Intune/endpoint) | Diagnóstico y políticas de dispositivos. 1 mención incidental en todo el repo | Baja |
| G10 | Descubrimiento de oportunidades de automatización | Meta-agente que entrevista a un equipo/proceso y mapea qué componentes aplican | Baja |
| G11 | Gestión documental / expedientes | Clasificación, retención, extracción de datos de PDFs/facturas | Media |

**Workflows sin cubrir:**

| # | Workflow | Detalle | Prioridad |
|---|---|---|---|
| W1 | `apb-wf-employee-onboarding` (JML) | Alta/baja extremo a extremo: Entra ID, licencias M365, accesos, activos | Alta |
| W2 | `apb-wf-access-recertification` | Campaña periódica de revisión de accesos con evidencias (ENS) | Alta |
| W3 | `apb-wf-request-fulfillment` | Solicitud de servicio: catálogo → aprobación → provisión → cierre | Alta |
| W4 | `apb-wf-license-renewal` | Renovaciones de licencias/contratos, periódico tipo `apb-wf-finops-review` | Media |
| W5 | `apb-wf-audit-preparation` | Preparación de auditoría ENS/ISO: recolección orquestada de evidencias (skills ya existen) | Media |
| W6 | `apb-wf-demand-intake` | Petición de negocio → business case → priorización de cartera | Media |
| W7 | `apb-wf-dr-drill` | Simulacro de continuidad/DR (la skill `apb-ops-service-continuity` existe; el flujo no) | Baja |

**Providers/MCP sin cubrir:**

| # | Provider | Para qué | Prioridad |
|---|---|---|---|
| P1 | `prov-jira-service-management` | JSM (requests, colas, SLAs) — prerequisito de G1/W3 | Alta |
| P2 | `prov-intune` (Endpoint Manager vía Graph) | Puesto de trabajo digital (G9) | Baja |
| P3 | `prov-powerbi-rest` | Publicar/refrescar los dashboards ya generados por script | Media |
| P4 | `prov-azure-backup` | Backup/restore: hoy 0 cobertura real | Baja |
| P5 | `prov-doc-intelligence` (Azure AI Document Intelligence/OCR) | Procesar PDFs/facturas/expedientes — habilita G11 | Media |
| P6 | `prov-power-automate` / Logic Apps | Automatización no-código que IT ofrece a otros departamentos | Evaluar |

**Utilidades del propio framework sin cubrir:**

| # | Utilidad | Detalle | Prioridad |
|---|---|---|---|
| U1 | `scripts/new_component.py` (scaffolder) | Crear skill/agente/workflow desde template con frontmatter válido — hoy se copia a mano | Alta |
| U2 | Runner de evaluación continua de agentes | `tests/golden_output_tests.md`/`test_agent_behavior.md` son documentos, no ejecución automatizada | Media |
| U3 | Programación de workflows periódicos | finops-review, W2, W4 necesitan ejecución recurrente. Interino con cron GitHub Actions ya ejecutable | Media |

**No se propone de nuevo** (ya cubierto o ya en este plan): orquestador
(#77), functional-technical-support, LCSP (#36), continuidad de servicio
(skill), dashboards (#39/#40), ingesta Jira (#37), telemetría (HANDOFF
TEL), caching de outputs, SBOM/supply-chain, capabilities/.

**MCP Server APB Agents:** plan completo (Fases 0-7) consolidado — ver
[`PLAN_MCP_SERVER_APB.md`](PLAN_MCP_SERVER_APB.md). Fase 0 ejecutable ya
(Sección B de arriba, resuelve N8); Fases 1-7 bloqueadas por MCP-1 a MCP-4
(Sección A). **Skill de terceros añadida en la misma sesión (2026-07-07), sin
relación con el MCP server:**
[`third-roboflow-supervision-v1.0`](../skills/third_party/roboflow/third-roboflow-supervision-v1.0.md)
(visión artificial — Roboflow `supervision`, MIT) — sin caso de uso APB
confirmado, `consumed_by` vacío, no wirear a ningún agente sin que Arquitectura
documente antes un caso de uso real.

**Estrategia de optimización de tokens:** ya resuelta — ver
[`ESTRATEGIA_OPTIMIZACION_TOKENS_2026-07-06.md`](ESTRATEGIA_OPTIMIZACION_TOKENS_2026-07-06.md)
(10 estrategias, roadmap 3 fases, ahorro estimado 30-50%). No requiere
trabajo nuevo.

---

## C. Trabajo de producción real y estado de QA-3

Todo el trabajo que requiere una acción humana de un equipo externo
(Plataforma, Arquitectura, Ciberseguridad, administradores M365/Atlassian)
para poner el framework en producción real está consolidado en
**[`HANDOFF_TECNICOS.md`](HANDOFF_TECNICOS.md)** — no se duplica aquí.

**Estado QA-3 (ejecución funcional TruckCenter, resumen):** 55/120 casos con
algún estado registrado (2026-07-03), hallazgos H1-H7 documentados en
`docs/qa/examples/QA_TRU_TruckCenter_UNIFICADO.md` v1.6. Bloqueantes conocidos:
F3 PRE sin dataset anonimizado, formulario de Alta con timeout >45s, acceso
EntraID asistido de Débora para la próxima ejecución. Ver
`HANDOFF_TECNICOS.md` (bloque QA) para el detalle de qué debe aportar cada
equipo.
