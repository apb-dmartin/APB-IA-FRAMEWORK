# Evaluación de preparación — ¿puede arrancar la transformación de SÒSTRAT? (v3, todas las fases)

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.
> **v3 (2026-07-11, mismo día)**: extendido el cierre de la v2 (que cubría solo Fase 0-1) a las 14 aplicaciones de Fase 0-4. Fase 5 (Escalas) se trata aparte por naturaleza distinta — ver `migration-readiness-fase5.md`.

## Respuesta directa

**Todo lo que se podía cerrar sin personas ya está cerrado, para las 14 aplicaciones de Fase 0-4.** Lo único que queda pendiente es, en su totalidad, **validación humana real** (Arquitectura APB, domain experts, equipo de ARGOS) — no hay más análisis de código, más specs ni más documentación que pueda sustituirla.

## Lo que SÍ está — completo para Fase 0-4 (14 aplicaciones)

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

## Recomendación de secuencia (final)

1. **Checkpoint de validación humana** con Arquitectura APB y domain experts sobre `catalog-comparison.md` y `discovery-summary.md` §5 — **el único bloqueo real que queda para Fase 0-4**.
2. En paralelo: recuperar el código fuente real de Aguada con IN2 (bloquea solo esa pieza).
3. Sesión formal con el equipo de ARGOS sobre Escalas (bloquea solo la Fase 5, no el resto).
4. **Una vez validado el punto 1**: sprint planning real con el equipo, usando `jira-backlog.md` + `specs/` + `testing-strategy-*.md` + `threat-model-*.md` como base de referencia — ya completa para las 14 apps de Fase 0-4.
5. Separar la lógica de liquidación de `EscalaAction.java` (única pieza de Fase 5 ejecutable ya, no depende de la sesión con ARGOS).

**En una frase**: no queda trabajo de análisis de código, diseño de contratos, testing ni seguridad pendiente para Fase 0-4 — lo único que falta es que personas reales revisen y decidan. Fase 5 tiene su propio camino, distinto por naturaleza (migración, no extracción).
