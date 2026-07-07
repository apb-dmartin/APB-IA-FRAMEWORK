# Plan de Fases — Temas Ejecutados (bitácora)

> Este documento es la **bitácora de ejecución** del framework: recoge los
> bloques y puntos ya realizados que antes vivían en
> [`PLAN_FASES_FUTURAS.md`](PLAN_FASES_FUTURAS.md). Se separa para que el plan
> de futuras quede acotado a lo **no ejecutado**.
>
> Regla de mantenimiento (aplicar antes de cerrar cada sesión): cuando un tema
> se ejecuta, su registro se mueve aquí y en FUTURAS queda solo un puntero.
> Contenido ordenado cronológicamente por sesión/fecha.

---

## Sesión Auditoría + Cobertura de Huecos — ✅ EJECUTADA (2026-07-04)

**Encargo de Débora:** (A) auditar todo lo pendiente para detectar el desfase real plan↔repo;
(B) buscar y cubrir huecos nuevos. Origen: pidió "abordar" Sesión 16/21/#30/#39-40, que resultaron
**ya construidas** (mi resumen inicial las listó "abiertas" por error — índice de memoria
desactualizado, corregido).

**Parte A — Auditoría (`discovery/AUDITORIA_DESFASE_PLAN_REPO.md`, MD + HTML corporativo):**
Verificación estructural del 100% del catálogo + muestreo dirigido de entregables. **Hallazgo
central: el desfase es de MADUREZ, no de existencia.** Sesiones 15/16/17/21 marcadas «CERRADA»
entregaron sus componentes, pero **313/359 en `draft`, 0 componentes apb-owned funcionales
aprobados** (los 37 `approved` = 36 skills de terceros verificadas + `prov-apb-knowledge-v1.0`).
**0 DRIFT-repo** (≠ precedente #56–#76). Corregidas 2 notas obsoletas (DRIFT-plan): #39/#40 y M365
(§D.2/§G). Vocabulario de madurez adoptado: **CONSTRUIDO (draft) → VALIDADO (`human_validated_by`
+ prueba real #51) → APROBADO (gobernanza)**. Hallazgo metodológico: el `Glob` con patrón relativo
da falsos negativos en esta workspace (ruta con espacios) → verificar existencia con `ls`/`grep`.

**Parte B — 5 componentes nuevos (`draft`, cableados bidireccionalmente):**
1. `apb-ops-incident-analyze-visual-v1.0` (operation) — análisis multimodal de incidencias (capturas/diálogos de error/gráficos de métricas). Cierra hueco #15. → `apb-agent-incident-support-v1.0`.
2. `apb-qa-markdown-validate-v1.0` (qa) — validación de contenido Markdown (completitud/tono/marcado IA/políticas). Cierra parte de #34. → `apb-agent-qa-auto-v1.0`.
3. `apb-plat-ci-qa-gate-v1.0` (platform) — gate QA pre-despliegue GO/NO-GO (incluye Markdown desplegado). Cierra resto de #34. → `apb-agent-qa-auto-v1.0`.
4. `apb-dev-sql-explain-plan-v1.0` (development) — interpretación de planes de ejecución SQL + profiling. Amplía #33. → `apb-agent-db-v1.0`.
5. `prov-otel-v1.0` (provider) — instrumentación OpenTelemetry, cubre el gap diferido en Sesión 17 (#39/#40). → `apb-ops-telemetry-emit-v1.0`.

**#30 MCP Graph — inicialmente marcado bloqueado, corregido el mismo día** (ver sesión de
seguimiento más abajo: la parte no bloqueada de #30 sí se ejecutó, quedando pendiente solo la
app registration Entra ID de Plataforma).

**Anti-repetición (check #26):** `validate_plan_deliverables_exist` en `scripts/validate_repo.py`
— verifica que los entregables (IDs con versión) declarados en filas «CERRADA» del plan existen en
el repo; ERROR si no. Evita reincidir en el desfase #56–#76. +5 tests (`TestPlanDeliverablesExist`).

**Cierre:** catálogo regenerado, **`--strict` exit 0 (359 componentes)**, **55/55** tests
(`test_validate_repo`) + 5/5 (`test_behavior_coverage`), plan y memoria actualizados.

---

## Sesión de seguimiento (3 tareas accionables) — ✅ EJECUTADA (2026-07-04, misma fecha)

Tras la Sesión Auditoría anterior, Débora preguntó qué más había pendiente sin abordar los 3
frentes grandes (ciclo de aprobación, QA-3, #77+#80). De los 4 puntos ACCIONABLE sin bloqueo
(§6 de `AUDITORIA_DESFASE_PLAN_REPO.md`), eligió 3 — dejando fuera el push de los 2 commits de
la sesión anterior.

**Tarea 1 — #85(K)(a)/(d), en `GitHub-Repos/APB-DOMAIN-CATALOG` (clon real, no el submódulo):**
- **Aclaración de ruta:** el submódulo `APB-IA-FRAMEWORK/domain-catalog` está anclado a `main` en
  su commit inicial vacío; los 21 `domains/<nombre>/domain.md` reales viven en el clon
  independiente `GitHub-Repos/APB-DOMAIN-CATALOG`, rama `feat/carga-inicial-dominios-apim`
  (2 commits, ya empujada a `origin`, sin PR mergeado a `main`).
- Nuevo `scaffolding/scripts/generate_domain_catalog_html.py` — genera `catalog/DOMAINS.html`
  (autocontenido, listado + búsqueda/filtro por nombre/id/estado/equipo + ficha por dominio) leyendo
  `domains/*/domain.md` directamente. Modo `--check` para detectar drift sin auto-commit.
  Verificado: genera 21 fichas, filtro probado en navegador (preview), drift provocado
  deliberadamente y detectado correctamente (exit 1).
- **Nuevo `.github/workflows/validate.yml`** — primer CI de este repo (antes no tenía ninguno,
  pese a que `validate_catalog.py` ya existía sin estar conectado). Corre en push/PR a `main`:
  `validate_catalog.py` + `generate_domain_catalog_html.py --check`. Sin auto-commit (mismo
  principio que `generate_catalog.py --check` en APB-IA-FRAMEWORK, GOVERNANCE.md: ningún proceso
  automático modifica un PR sin revisión humana).
- Nuevo `scaffolding/reference/dominios-tipicos-referencia.md` — catálogos de dominios típicos
  de empresa genérica y de entorno portuario, con contraste frente a los 21 dominios reales
  (huecos aparentes señalados, no decididos: Compras, Jurídico, Gobierno de Datos podrían estar
  diluidos en `dom-corporativo-v1`/`dom-transversal-arq-v1`).
- Commit local `617ae1f` en `feat/carga-inicial-dominios-apim` (mismo repo/clon). **Sin push** —
  pendiente de confirmación de Débora, igual que el resto de esa rama.
- (b)/(c) de #85(K) siguen fuera de alcance (dependen de la aprobación de Arquitectura de los 21
  dominios).

**Tarea 2 — re-identificación de los 10 SHAs `unverified` de terceros restantes** (en
`APB-IA-FRAMEWORK`, vía API pública de GitHub):
- **Resueltos con evidencia real (2):**
  - `third-ccusage-analytics-v1.0` — `source_repo` solo apuntaba al org sin repo; repo real
    `ccusage/ccusage`, SHA `f3a8eaba59448a8718a75bb178bd54600020d54e`, MIT confirmado (el
    clasificador de GitHub lo marca "Other" por un problema de detección, el fichero LICENSE es
    MIT estándar).
  - `wrap-mukul-cyber-v1.0` — `mukul975/cybersecurity-arsenal` **no existe**; el repo real es
    `mukul975/Anthropic-Cybersecurity-Skills` (Apache-2.0, no MIT), SHA
    `673da1f3b0b7be34ffc9624ef3858fe45f1c3bed` — ya usado correctamente en el descriptor hermano
    `third-mukul-cyber-arsenal-v1.0.md`, ahora consistentes entre sí.
- **Documentados como no resolubles hoy (8), sin fabricar SHA/URL de sustitución** (norma "no
  inventar sin evidencia"):
  - `third-hashicorp-cloud-patterns-v1.0` — `hashicorp/terraform-search-import` no existe;
    "Terraform Search & Import" es un nombre de producto de HCP Terraform, no un repo.
  - `third-openai-threat-model-v1.0` — `openai/security-threat-model` no existe ni aparece en
    el org `openai`.
  - `third-neondatabase-db-migration-v1.0` — `neondatabase/neon-postgres` no existe; candidatos
    plausibles sin confirmar: `neondatabase/neon` o `neondatabase/agent-skills`.
  - `third-composio-sonar-v1.0` + `wrap-composio-v1.0` — `ComposioHQ` es solo el org; Composio es
    SaaS, sin repo público de origen identificado.
  - `third-graphify-visual-v1.0` — `graphify.net` es SaaS propietario, no aplica `source_commit`.
  - `third-skills-sh-frontend-v1.0` + `wrap-skills-sh-v1.0` — `skills.sh` es una plataforma, no
    una organización de GitHub; no aplica `source_commit`.

**Tarea 3 — reevaluar Understand-Anything (`third-lum1104-knowledge-graph-v1.0`):**
- Corregida contradicción interna en `PLAN_FASES_FUTURAS.md`: la fila resumen del punto #14
  decía "descartado, eliminado del repo" pese a que el detalle del mismo punto (resuelto en
  Sesión 19) ya decía "licencia MIT confirmada, en `draft`". Ambas partes del fichero ahora
  coinciden: el componente existe, `draft`, sin consumidores.
- Recomendación (no decisión) añadida para cuando Débora reevalúe el uso: candidato natural
  `apb-agent-ddd-v1.0`/`apb-sub-ddd-interview-v1.0`.

**Cierre:** apéndice §9 añadido a `AUDITORIA_DESFASE_PLAN_REPO.md` (+ HTML regenerado); catálogo
regenerado, `validate_repo.py --strict` **exit 0 (359 componentes, 10 warnings exentos** — antes
11, bajó por las 2 re-identificaciones), tests verdes, plan y memoria actualizados. **Push
confirmado y ejecutado** en ambos repos (`APB-IA-FRAMEWORK` commit `b7d2225`,
`APB-DOMAIN-CATALOG` commit `617ae1f`), ninguno con PR abierto a `main` todavía.

## Cierre del #30 MCP Graph (mismo día, tras el push anterior)

Al preguntar Débora si quedaban más pendientes, se detectó que **#30 nunca se había ejecutado**
pese a estar marcado como cubierto en la sesión de Auditoría original: `.mcp.json` solo tenía
`playwright`, sin entrada de Microsoft Graph. Corregido:

- Identificado `@softeria/ms-365-mcp-server` (paquete npm real y verificado) como servidor MCP —
  no `@microsoft/graph-mcp-server`, que no existe.
- **El clasificador de seguridad de auto-mode bloqueó el primer intento** de wiring por ser un
  paquete de terceros elegido por el propio agente sin aprobación nombrada — se detuvo, se
  explicó el motivo a Débora y se pidió su aprobación explícita del paquete concreto.
- Con su OK: cableado en `.mcp.json` (`ms365`, modo device-code, sin credenciales) +
  `prov-ms365-v1.0.md` actualizado con la config real y las variables de entorno para el flujo
  headless de producción (`MS365_MCP_CLIENT_ID`/`TENANT_ID`/`KEYVAULT_URL`), pendiente de que
  Plataforma registre la app en Entra ID.
- Apéndice §10 añadido a `AUDITORIA_DESFASE_PLAN_REPO.md` (+ HTML regenerado). `validate_repo.py
  --strict` exit 0 (359 componentes).

---

## Sesión QA-2 — ✅ CERRADA (2026-07-02): planes de pruebas (#82) + navegación agéntica (#84)

**Puntos:** #82 (metodología/plantilla de planes de pruebas) + #84 (navegación agéntica).

1. ✅ **Estándar y plantilla corporativos:** `context/apb/standards/TEST_PLAN_STANDARD.md`
   (orden de fuentes con degradación, procedencia múltiple obligatoria, unificación sin duplicados,
   detección de plan previo + actualización incremental, 12 secciones obligatorias, gobernanza del cambio,
   almacenamiento en el repo de la app, evidencias ZIP/Jira seleccionables, no-regresión de rendimiento) +
   plantilla `context/apb/templates/TEST_PLAN.md`.
2. ✅ **Skill `apb-qa-test-plan-v1.0` → v1.2.0:** interactiva (pregunta por los inputs), ingesta de planes
   aportados por el usuario en **cualquier formato** (vía `apb-plat-doc-to-markdown`), procedencia múltiple,
   inputs nuevos (`provided_plans`, `sources`, `previous_plan`, `app_repo`, `performance_baseline`,
   `evidence_destination`).
3. ✅ **Ejemplo unificado TruckCenter:** `docs/qa/examples/QA_TRU_TruckCenter_UNIFICADO.md` — fusión sin
   duplicados de las 3 visiones (A Rovo/Jira 38 · B Rovo/Jira+AF 112 · C Copilot/código 112) → **112 casos**,
   procedencia por prueba (herramienta + origen), columna «Desde» y mapeo A→unificado. Fuentes archivadas en
   `docs/qa/examples/sources/`.
4. ✅ **#84 navegación agéntica:** `providers/prov-browser-agent-v1.0.md` (agnóstico) +
   `skills/apb-owned/qa/apb-qa-exploratory-nav-v1.0.md` (exploratorio vs scriptado), cableados a
   `apb-agent-qa-auto-v1.0` y `apb-wf-qa-evidence-v1.0`.
5. ✅ **Ejecución real sobre TruckCenter PRE** (login EntraID asistido, rol MANAGE): 4 PASS
   (TRU-T77 login, T26 título pestaña, T15 columnas añadibles, T16 columnas auditoría), 1 no evaluable
   (T13, GRID vacío sin criterio), 2 hallazgos (F1 GRID no autocarga; F2 form Alta con carga prolongada).
   Evidencias empaquetadas (ZIP con informe MD+HTML+log) y camino Jira definido; 0 datos modificados en PRE.
6. ✅ **Validador:** check #20 (`validate_test_plan_methodology`) — las skills de plan de pruebas deben
   referenciar `TEST_PLAN_STANDARD`. Tests nuevos (`TestTestPlanMethodologyCheck`, 2 casos) → 40/40 suite.
7. ✅ **Cierre:** catálogo regenerado, `--strict` exit 0 (345 componentes), 40/40 tests, docs actualizadas.

**Pendiente derivado (Débora):** el agente de pruebas funcionales debe consultar credenciales desde un
**repositorio central** (Azure Key Vault, `GOVERNANCE.md §5`) + captura/reutilización de `storage_state`,
para ejecutar de forma autónoma. Ver HANDOFF y #82 en FUTURAS.

### Continuación E-bis (2026-07-02): cobertura completa de los 112 + hallazgos

A petición de Débora se amplió la ejecución para **cubrir los 112 casos** (no 5), en **solo lectura**, con
informe de estado por caso (en OneDrive: `…/Proyectos/SDD - Framework.../QA_TruckCenter_evidencias/INFORME_EJECUCION_112.md`).
**Verificado (MANAGE):** 8 PASS (login, título, selector de columnas, columnas de auditoría, acciones MANAGE,
TLS, health-checks API/web) + 8 parciales. **Hallazgos clave:**
- **F3** — PRE **sin datos** de Truck Center (GRID y maestro vacíos) → ~45 casos NO EVALUABLES/REQUIERE ESCRITURA en solo lectura.
- **F2** — formulario de Alta principal no carga (>45 s) → bloquea ~18 casos (lupas, desplegable, alta).
- **F4** — API LGP responde ~9,3 s (lenta) → indicador de rendimiento.
- **F5** — discrepancia AF↔código: el maestro Tipos de Vehículo es **multiidioma CA/ES/EN** (no un único `DESCRIPCIO`); el código (Copilot) era correcto.

**Decisiones Débora (E-bis):** solo lectura; 2ª pasada USER_READ, rendimiento, seguridad y **evidencia visual
(PNG/vídeo)** → **Sesión QA-3** (las capturas del navegador MCP no persisten como fichero en este entorno; se
harán con Playwright). Registrada QA-3 en FUTURAS. **0 datos modificados en PRE.**

---

## Sesión QA — ✅ CERRADA (ejecutada post-Sesión 12)

Debora decidió que la auditoría de testing/Playwright (#17) y el
solapamiento detectado entre `APB-IA-FRAMEWORK` y el repositorio
`apb-ai-skills` merecen una **sesión propia de QA**, no una sub-tarea de la
Sesión 8. Contenido confirmado de esta sesión:

1. ✅ **Auditoría completa de `apb-ai-skills.zip`** (subido en Sesión QA,
   no Sesión 8 — el zip no había persistido entre sesiones, hubo que
   re-subirlo). Verificado: 10 skills propias APB ✓, 10 externas ✓
   (incluidas las de Playwright), agente `qa-orchestrator` + 5 subagentes
   ✓ — todos coinciden con lo descrito. **Hallazgo no anticipado:** existe
   además una carpeta `skills/_spec-driven/` con 3 skills más
   (`spec-to-api-contract`, `spec-to-e2e-flows`, `spec-to-test-plan`) que
   no estaba contabilizada en la descripción original de la Sesión 8.

2. ✅ **Solapamiento resuelto — 4 fusiones, no 1.** El solapamiento real
   encontrado fue mayor que el único caso anticipado
   (`apb-qa-anonymize-v1.0` vs `apb-test-data-rgpd`). Se detectaron y
   fusionaron **4 pares**, decisión de Debora: "fusionar e incorporar al
   repo de APB-IA-FRAMEWORK" en todos los casos:
   - `apb-qa-unit-test-gen-v1.0` ← `apb-unit-test-generator` (ampliado a
     JS/TS, ejemplos de código, eventos, vínculo RGPD) → v1.1.0
   - `apb-qa-test-plan-v1.0` ← `apb-test-plan-lcsp` (marco normativo
     LCSP/ENS/RGPD/WCAG, tabla de criterios de éxito cuantificados,
     contexto contractual de licitación) → v1.1.0
   - `apb-sec-ens-v1.0` ← `apb-ens-security-audit` (tablas operativas de
     controles concretos por nivel Alto/Medio, cruce OWASP, formato de
     informe de hallazgos con severidad) → v1.1.0
   - `apb-qa-anonymize-v1.0` ← `apb-test-data-rgpd` (tabla de dominios
     ficticios APB con vocabulario portuario específico — IMO de buques,
     código de atraque —, fixtures concretos Oracle/TypeScript/Cosmos
     DB/PostGIS/.NET) → v1.2.0

3. ✅ **Frontera de responsabilidad resuelta: `apb-ai-skills` queda
   DEPRECADO** (decisión de Debora). Todo desarrollo futuro de
   skills/agentes/subagentes de QA vive exclusivamente en
   `APB-IA-FRAMEWORK`. El orquestador `qa-orchestrator` y 3 subagentes
   (`dotnet-backend-agent`, `data-persistence-agent`, `django-gis-agent`)
   referencian las 4 skills ahora fusionadas por su nombre antiguo —
   **estas referencias no se han corregido ni se ha tocado nada del
   repositorio `apb-ai-skills`**, por decisión explícita de Debora ("no
   toques nada de apb-ai-skills, quédate solo con la decisión verbal").
   El repo tiene 2 GitHub Actions activos (`sync-skills.yml`,
   `validate-skills.yml`) que seguirán ejecutándose normalmente — Debora
   fue informada de esto y decidió no actuar sobre ello en esta sesión.

## Sesión Frontend — ✅ CERRADA (ejecutada 2026-06-24)

Inicialmente agrupada con la Sesión QA por compartir la guía de estilo como
insumo común; Debora pidió explícitamente separarlas — QA trata pruebas,
Frontend trata construcción de interfaz. Contenido:

1. ✅ **(Punto #20)** `apb-agent-ux-mockup-v1.0` creado (dominio `architecture`).
   Agente para perfiles funcionales: traduce descripción en lenguaje natural a mockup
   estructurado con componentes DevExtreme. Base: WidgetsGallery + ThemeBuilder.
   Guía de estilos APB (PDFs) diferida — se añadirá en sesión futura.
2. ✅ **(Punto #21)** Cubierto: `apb-dev-devexpress-front-v1.0` actualizado (v1.1 efectivo)
   para referenciar `apb-dev-devexpress-selector-v1.0` como predecesor cuando no hay
   mockup funcional, y aceptar output de `apb-agent-ux-mockup-v1.0` como input directo.
   Stack ya existente (`apb-sub-dev-devexpress-v1.0`, `apb-agent-implementer-v1.0`)
   cubre el flujo de generación de código real.
3. ✅ **(Skill nueva)** `apb-dev-devexpress-selector-v1.0` creado — catálogo de
   componentes DevExtreme con árbol de decisión, patrones de layout APB y guía de
   theming ThemeBuilder. Usada por el agente de mockups y el subagente de desarrollo.
4. **(Punto #22 — pendiente, sesión futura)** Analizar si APB necesita un catálogo
   formal de componentes / design system más allá de la guía de estilo en PDF.

**Componentes entregados en Sesión Frontend:**
- `apb-dev-devexpress-selector-v1.0` (skill, domain: development)
- `apb-agent-ux-mockup-v1.0` (agent, domain: architecture)
- `apb-dev-devexpress-front-v1.0` actualizado (referencias a selector y agente de mockups)

**Documentos ya disponibles para Sesión QA y Sesión Frontend** (en
`/mnt/project/`, subidos por Debora antes de la Sesión 8):
- `Guía_Estilos__Port_de_Barcelona__2022__v1.pdf` — "Rediseño componentes -
  Port de Barcelona" — la guía de estilo UI/UX confirmada (punto #13
  original). Insumo principal de Sesión Frontend.
- `GISPEM__Guía_de_estilos.pdf` — guía de estilo relacionada (a confirmar
  alcance exacto: ¿específica de GIS/GISPEM, o complementaria a la
  anterior?).
- `ManualUsuario_WidgetsLayout_v1.pdf` — manual de usuario de widgets y
  layout, octubre 2022, autoría APB — candidato a referencia técnica de
  componentes DevExpress/DevExtreme reales en uso.
- `apb-ai-skills.zip` — insumo principal de Sesión QA.

---

## Punto #42 — Hallazgo de formato: comillas mal cerradas en sección "Dependencias" ✅ RESUELTO

**Detectado durante preparación de Sesión 11, corregido el mismo día por decisión explícita
de Debora** ("Arregla el tema de las comillas"). 19 archivos de skills (dominios
`development`, `discovery`, `qa`) tenían un patrón de error sistemático en la sección
"🔗 Dependencias" del cuerpo del documento: backtick de apertura sin cierre o mezclado con
comilla doble, p. ej. `` `apb-dev-code-review-v1.0" `` en lugar de
`` `apb-dev-code-review-v1.0` ``. No afectaba al frontmatter YAML (los IDs declarados ahí
eran correctos) — era puramente cosmético en Markdown del cuerpo.

**Archivos corregidos (19, 47 líneas en total):** `apb-dev-pr-doc-v1.0`,
`apb-dev-openspec-review-v1.0`, `apb-dev-legacy-mapper-v1.0`, `apb-dev-sonar-clean-v1.0`,
`apb-dev-devexpress-front-v1.0`, `apb-dev-gis-django-v1.0`, `apb-disc-backlog-v1.0`,
`apb-disc-adversarial-v1.0`, `apb-disc-ddd-legacy-v1.0`, `apb-disc-reverse-doc-v1.0`,
`apb-disc-enrich-req-v1.0`, `apb-disc-epic-mono-v1.0`, `apb-disc-reverse-code-v1.0`,
`apb-disc-cosmic-v1.0`, `apb-disc-business-v1.0`, `apb-disc-spec-gen-v1.0`,
`apb-qa-release-ready-v1.0`, `apb-qa-unit-test-gen-v1.0`, `apb-qa-post-migration-v1.0`,
`apb-qa-test-auto-v1.0`. Corrección puramente sintáctica (cierre de backtick), sin tocar
ningún otro contenido de los archivos. Validado: `scripts/validate_repo.py --strict` sigue
en 0 errores tras el cambio.

---

## Sesión Enriquecimiento A — ✅ EJECUTADA (2026-06-27)

**Estado de ejecución — Sesión Enriquecimiento A (2026-06-27):**

| Bloque | Descripción | Estado |
|---|---|---|
| Bloque 1 — Rewirings (punto #55) | 44 conexiones aplicadas en 19 agentes. Corrección: ID real es `third-google-finops-multicloud-v1.0` (p, no b). validate_repo.py --strict → 0 errores. INDEX.md regenerado. | ✅ COMPLETADO |
| Bloque 2 — skills nuevas (ops×1 alerting-design + sec×4 + gov×1 audit) | sec: sast, dast, supply-chain, patch-management. gov: framework-audit. ops: alerting-design (sesión anterior). validate_repo.py 0 errores. | ✅ COMPLETADO |
| Bloque 3 — 3 agentes nuevos (Change Manager, Problem Manager, Data Governance) | change-manager, problem-manager, data-governance. ITIL + RGPD/ENS/NIS2. validate_repo.py 0 errores. | ✅ COMPLETADO |
| Bloque 4 — 5 subagentes nuevos (k8s, ACA, Rancher, ServiceBus, FinOps Azure) | k8s, aca, rancher, servicebus, finops-azure. System prompts incluidos. validate_repo.py 0 errores. | ✅ COMPLETADO |
| Bloque 5 — Prompts de sistema en iis-apache, network, oracle + qa-e2e | System prompts añadidos en 4 subagentes existentes. Stack APB detallado en cada uno. | ✅ COMPLETADO |

### 55. ✅ Rewirings: skills/subagentes existentes sin conectar a sus agentes correctos (costo cero, impacto inmediato)

> **EJECUTADO** — Sesión Enriquecimiento A, 2026-06-27. 44 rewirings aplicados en 19 agentes. validate_repo.py --strict → 0 errores. INDEX.md regenerado.

El análisis detecta ~20 conexiones faltantes entre skills ya creadas y los agentes que deberían usarlas. No requieren crear nada nuevo — solo añadir la referencia en el frontmatter del agente correspondiente y ejecutar `validate_repo.py --strict`.

**Lista completa de rewirings pendientes:**

| Skill/subagente a conectar | Agente destino | Justificación |
|---|---|---|
| `apb-sub-dev-parallel-v1.0` | `apb-agent-implementer-v1.0` | El subagente de despacho paralelo existe pero no está en la lista del Implementer — impide implementación paralela en el agente principal |
| `apb-dev-frontend-devexpress-events-v1.0` | `apb-agent-implementer-v1.0` | Skill de DevExtreme para eventos, no conectada |
| `apb-dev-implementation-patterns-v1.0` | `apb-agent-implementer-v1.0` | Catálogo de patrones, no conectado al Implementer principal |
| `apb-dev-sql-gen-v1.0` | `apb-agent-implementer-v1.0` | `apb-dev-sql-fix-v1.0` sí está, pero no la de generación |
| `apb-disc-brainstorming-v1.0` | `apb-agent-business-analyst-v1.0` | Obligatoria antes de cualquier trabajo creativo — gap inconsistente con "grill before code" |
| `apb-disc-adversarial-v1.0` | `apb-agent-business-analyst-v1.0` | El BA debe hacer devil's advocate sobre los requisitos que recoge |
| `apb-pm-product-analysis-v1.0` | `apb-agent-business-analyst-v1.0` | Análisis de producto complementa al BA |
| `apb-disc-brainstorming-v1.0` | `apb-agent-spec-engineer-v1.0` | Fase exploratoria previa a generación de spec |
| `apb-disc-design-approval-v1.0` | `apb-agent-spec-engineer-v1.0` | Gate de aprobación de diseño, existe pero no conectada |
| `apb-disc-brainstorming-v1.0` | `apb-agent-domain-architect-v1.0` | Fase exploratoria antes de modelar |
| `apb-disc-brainstorming-v1.0` | `apb-agent-tech-discovery-v1.0` | Exploración inicial en evaluación de tecnologías |
| `apb-gov-standards-v1.0` | `apb-agent-tech-discovery-v1.0` | Verificar que la tecnología evaluada cumple los estándares APB |
| `apb-sec-mitre-mapping-v1.0` | `apb-agent-security-architect-v1.0` | Existe en catálogo pero no conectada al Security Architect |
| `apb-sec-cloud-hardening-v1.0` | `apb-agent-security-architect-v1.0` | CIS Benchmark hardening, existe pero no conectada |
| `apb-arch-event-driven-master-v1.0` | `apb-agent-technical-architect-v1.0` | Skill maestro de eventos, más profunda que la básica ya conectada |
| `apb-arch-dotnet-base-v1.0` | `apb-agent-technical-architect-v1.0` | Reglas obligatorias para proyectos .NET, no conectada |
| `apb-arch-design-events-v1.0` | `apb-agent-technical-architect-v1.0` | Diseño de microservicios orientados a eventos, no conectada |
| `apb-arch-event-driven-master-v1.0` | `apb-agent-cloud-architect-v1.0` | Skill maestro de eventos no conectada al Cloud Architect |
| `apb-plat-deployment-finish-v1.0` | `apb-agent-release-manager-v1.0` | La skill de cierre de deployment existe exactamente para esto pero no está aquí |
| `apb-plat-ms-notify-v1.0` | `apb-agent-release-manager-v1.0` | Notificación post-release a stakeholders |
| `apb-gov-jira-evidence-v1.0` | `apb-agent-risk-exception-v1.0` | El agente de excepciones no puede crear tickets de excepción |
| `apb-gov-evidence-v1.0` | `apb-agent-risk-exception-v1.0` | Generación de evidencias para expediente de excepción |
| `apb-plat-ms-notify-v1.0` | `apb-agent-risk-exception-v1.0` | Notificación a validadores de excepción |
| `apb-qa-tdd-v1.0` | `apb-agent-qa-auto-v1.0` | TDD existe pero no está en el QA Agent |
| `apb-qa-readiness-check-v1.0` | `apb-agent-qa-auto-v1.0` | Gate de readiness antes de implementar |
| `apb-qa-testing-strategy-v1.0` | `apb-agent-qa-auto-v1.0` | Estrategia de testing para eventos, no conectada |
| `apb-qa-pipeline-v1.0` | `apb-agent-qa-auto-v1.0` | Evaluación de calidad del pipeline CI/CD |
| `apb-qa-framework-v1.0` | `apb-agent-meta-builder-v1.0` | El meta-builder debería auto-validar los componentes que genera |
| `apb-sub-ops-azure-v1.0` | `apb-agent-observability-v1.0` | Es la fuente de datos principal (APBFrameworkTelemetry_CL) pero el subagente solo está en SRE |
| `apb-ops-slo-design-v1.0` | `apb-agent-observability-v1.0` | Monitoring sin SLOs no tiene objetivo |
| `apb-gov-spec-sync-v1.0` | `apb-agent-governance-v1.0` | Gobernanza implica que las specs estén sincronizadas |
| `apb-plat-db-migration-v1.0` | `apb-agent-modernization-v1.0` | La modernización sin migración de BD es incompleta |
| `apb-disc-reverse-doc-v1.0` | `apb-agent-modernization-v1.0` | Análisis de documentación del legacy, complementa reverse-code |
| `apb-dev-review-tl-v1.0` | `apb-agent-code-reviewer-v1.0` | Perspectiva de Tech Lead, complementa al review básico |
| `apb-dev-impact-analysis-v1.0` | `apb-agent-code-reviewer-v1.0` | ¿Qué rompe este PR? Esencial en un reviewer |
| `apb-dev-surgical-changes-v1.0` | `apb-agent-code-reviewer-v1.0` | Detectar scope creep en un PR es función del reviewer |
| `apb-dev-gis-django-v1.0` | `apb-agent-code-reviewer-v1.0` | Review de código Python/Django |
| `apb-doc-event-specs-v1.0` | `apb-agent-documentation-v1.0` | Specs CloudEvents/AsyncAPI, existe pero no conectada |
| `apb-doc-generate-ppt-v1.0` | `apb-agent-documentation-v1.0` | Skill de generación de PPT sin agente asignado |
| `apb-doc-generate-word-v1.0` | `apb-agent-documentation-v1.0` | Skill de generación de Word sin agente asignado |
| `third-google-finobs-multicloud-v1.0` | `apb-agent-finops-v1.0` | Ya aprobada en catálogo, no está conectada al FinOps Agent |
| `apb-ops-dependency-audit-v1.0` | `apb-agent-finops-v1.0` | Detectar recursos huérfanos (sin proyecto asignado) |
| `third-nextlevel-ux-v1.0` | `apb-agent-ux-mockup-v1.0` | Skill de UX aprobada, existe pero no conectada al agente |

**Sesión asignada:** Sesión Enriquecimiento A — primera acción (sin bloqueantes, costo cero).

---

## Revisión integral del framework — 2026-06-29

> Revisión ejecutada post-Sesión Enriquecimiento B. Cuatro dimensiones: estructura/consistencia, funcional, seguridad/implementación, cobertura de pruebas. Fuente: validate_repo.py + 3 agentes de análisis paralelo.
> **Nota (registro histórico):** los hallazgos "Pendiente" de esta revisión y las "Sesiones propuestas" derivadas se ejecutaron o reasignaron en sesiones posteriores; su estado vivo se sigue en las secciones §H/§I de `PLAN_FASES_FUTURAS.md`. Este bloque se conserva como fotografía fechada de la auditoría.

### Resultados por dimensión

#### Dimensión 1 — Estructura y consistencia

| Hallazgo | Severidad | Estado |
|---|---|---|
| 26 de 29 agentes sin `## Marcado IA obligatorio (POLICY_AI_USAGE §6)` | 🔴 Crítico | Pendiente |
| 19 subagentes sin System Prompt (esqueletos sin instrucciones al LLM) | 🔴 Crítico | Pendiente |
| validate_repo.py no comprueba Marcado IA en `agents/` (condición `skills/apb-owned` excluye la carpeta agents) | 🔴 Crítico (bug validador) | Pendiente |
| 4 skills nuevas (sec×3 + gov×1) no referenciadas en ningún agente | 🟡 Medio | Pendiente |
| Dominio `orchestration`: solo 1 skill (`apb-orch-multi-agent-v1.0`), sin agente dedicado | 🟡 Medio | Pendiente |
| Dominio `design`: solo 2 skills, sin agente dedicado de diseño | 🟡 Bajo | Pendiente |
| 59 warnings de `source_commit: unverified` en skills de terceros | ⚪ Info | Deliberado (política GOVERNANCE.md §4.2) |

#### Dimensión 2 — Funcional

| Hallazgo | Severidad | Descripción |
|---|---|---|
| `apb-wf-incident-l1-v1.0` orquesta skills directamente, NO usa `apb-agent-incident-support-v1.0` como agente padre | 🟡 Medio | El workflow y el agente están desacoplados — debería referenciar al agente |
| Workflow `apb-wf-cloud-migration-v1.0`: 9 agentes en cadena sin formato de output inter-agente definido | 🟡 Medio | Platform Engineer → SRE: no hay contrato de datos entre pasos |
| Solapamiento funcional: `apb-ops-incident-diagnose-v1.0` vs `apb-ops-rca-v1.0` | 🟡 Medio | Ambas producen "causa raíz"; diagnose es táctico/inmediato, rca es post-incidente. Diferencia no documentada claramente |
| Solapamiento parcial: `apb-sec-threat-model-v1.0` (STRIDE) vs `apb-sec-risk-analysis-v1.0` (ISO 27005) | 🟢 Bajo | Diferencia real (táctico vs. estratégico) pero no explicada en los propios documentos |
| `apb-agent-finops-v1.0` requiere "catálogo de precios Azure" sin que ninguna skill tenga ese output | 🟡 Medio | Gap de input no cubierto en la cadena |
| Todos los agentes críticos tienen autonomy_level 1 | ✅ Correcto | |
| `apb-agent-compliance-audit-v1.0` respeta gates humanos correctamente | ✅ Correcto | |

#### Dimensión 3 — Seguridad e implementación

| Hallazgo | Severidad | Descripción |
|---|---|---|
| Sin credenciales hardcodeadas detectadas en ningún fichero | ✅ Seguro | Patrones detectados por validate_repo.py línea 102-108 |
| Máximo autonomy_level en producción: 2. Nivel 4 no usado (declarado en AUTONOMY_LEVELS.md) | ✅ Correcto | |
| Skills de seguridad con instrucciones defensivas, sin instrucciones de ataque | ✅ Correcto | |
| `apb-ops-incident-diagnose-v1.0` (nivel 2) propone `ALTER SYSTEM KILL SESSION` Oracle | 🟡 Bajo | Requiere "confirmación humana" en texto pero el framework no lo bloquea mecánicamente |
| SCHEMA.md y validate_repo.py están sincronizados en campos obligatorios | ✅ Correcto | |
| CI/CD `.github/workflows/validate.yml` usa `--strict`, no auto-commitea catálogo | ✅ Correcto | |
| validate_repo.py línea 346: condición `"skills/apb-owned" in rel_path` excluye comprobación Marcado IA en agentes | 🔴 Bug | Requiere corrección |

#### Dimensión 4 — Cobertura de pruebas

| Hallazgo | Severidad | Descripción |
|---|---|---|
| `tests/test_validate_repo.py`: 19 tests unitarios sobre validate_repo.py | ✅ Existe | Cubre YAML, secretos, refs rotas, circularidades |
| ~85% de skills tienen sección "Ejemplo de Uso" con casos concretos | ✅ Bueno | |
| ~90% de criterios de calidad son verificables objetivamente (checkboxes, porcentajes) | ✅ Bueno | |
| Solo ~40% de skills documentan casos de error / edge cases en los ejemplos | 🟡 Medio | La mayoría asume inputs válidos |
| ~30% de skills no documentan qué hace el agente si el input está incompleto | 🟡 Medio | Comportamiento ante entrada nula no especificado |
| Workflows documentan happy path y gates, pero NO fallos en cascada ni iteraciones | 🟡 Medio | ¿Qué ocurre si falla el paso 3 de 8? No documentado |
| Tests de comportamiento de agentes: AUSENTES | 🔴 Gap crítico | No existe suite que valide "dado prompt X → output Y esperado" |
| Self-testing: `apb-qa-framework-v1.0` solo valida estructura, no comportamiento | 🟡 Medio | Pendiente extensión semántica |

### Sesiones propuestas resultado de la revisión

#### Sesión Correcciones Urgentes (estimado: 2-3h)

**Objetivo:** Corregir los 3 hallazgos críticos de estructura antes de continuar añadiendo componentes.

| Tarea | Detalle |
|---|---|
| C1 — Corregir validate_repo.py línea 346 | Extender condición para incluir directorio `agents/` en comprobación de Marcado IA |
| C2 — Marcado IA en 26 agentes | Añadir sección `## Marcado IA obligatorio (POLICY_AI_USAGE §6)` a los 26 agentes sin ella. Patrón: los 3 creados en Sesión Enriquecimiento B son la referencia |
| C3 — Rewiring 4 skills huérfanas | `apb-sec-sast`, `apb-sec-dast`, `apb-sec-supply-chain` → `apb-agent-security-architect-v1.0`; `apb-gov-framework-audit` → `apb-agent-governance-v1.0` |

#### Sesión Enriquecimiento C — Subagentes + Funcional (estimado: 4-6h)

**Objetivo:** System prompts en 19 subagentes prioritarios + correcciones funcionales detectadas.

| Bloque | Tareas |
|---|---|
| C-Bloque 1 — System prompts prioritarios (9 subagentes) | `apb-sub-dev-net`, `apb-sub-dev-devexpress`, `apb-sub-dev-django`, `apb-sub-dev-sql`, `apb-sub-obs-grafana`, `apb-sub-obs-powerbi`, `apb-sub-sec-ens`, `apb-sub-gov-standards`, `apb-sub-ops-azure` |
| C-Bloque 2 — System prompts secundarios (10 subagentes) | `apb-sub-ddd-*` (×5), `apb-sub-dev-parallel`, `apb-sub-plat-ghactions`, `apb-sub-plat-jenkins`, `apb-sub-qa-unit`, `apb-sub-qa-security` |
| C-Bloque 3 — Correcciones funcionales | (1) Añadir `apb-agent-incident-support-v1.0` como orquestador en `apb-wf-incident-l1-v1.0`. (2) Documentar diferencia diagnose vs RCA en ambas skills. (3) Definir formato de output inter-agente en `apb-wf-cloud-migration-v1.0` (contrato Platform Engineer → SRE). (4) Identificar cómo cubre el framework el input "catálogo de precios Azure" para FinOps |

#### Sesión Calidad de Pruebas (estimado: 3-4h)

**Objetivo:** Mejorar cobertura de casos de error y crear base de tests de comportamiento.

| Tarea | Detalle |
|---|---|
| Q1 — Edge cases en skills críticas | Añadir sección "Comportamiento ante inputs incompletos" en las 20 skills más usadas (operation, security, governance). Documenta: qué pregunta el agente, qué devuelve si falta input obligatorio |
| Q2 — Fallos en cascada en workflows | Añadir sección `## Manejo de fallos` en los 3 workflows más complejos (cloud-migration, sdd-full, incident-l1): qué ocurre si falla cada paso y cómo se recupera |
| Q3 — Extender apb-qa-framework-v1.0 | Añadir validaciones semánticas: presencia de ejemplos de error, criterios cuantificables, sección de comportamiento ante inputs nulos |
| Q4 — Primer test de comportamiento (piloto) | Crear `tests/test_agent_behavior.md`: 3-5 casos de prueba documentados para `apb-agent-incident-support-v1.0` con prompt de entrada, output esperado y criterios de evaluación. Base para futura automatización |

#### Sesión Power BI / Framework Metrics (sesión separada, bloqueante: datos reales)

> Ya planificada anteriormente. Pipeline: GitHub Action → Azure Storage → Power BI dinámico. No iniciar hasta tener al menos 30 días de uso real del framework con datos registrados.

### Backlog de mejoras detectadas — M1–M6 ✅ RESUELTOS (2026-06-29)

| ID | Mejora | Prioridad | Sesión candidata |
|---|---|---|---|
| ~~M1~~ | ~~Dominio `orchestration`: añadir 2-3 skills de coordinación multi-agente~~ | Baja | ✅ RESUELTO (2026-06-29) — `apb-orch-context-handoff-v1.0` (transferencia secuencial) + `apb-orch-human-checkpoint-v1.0` (protocolo aprobación humana) creadas |
| ~~M2~~ | ~~Dominio `design`: añadir agente UX/IA design y 2-3 skills de design system~~ | Baja | ✅ RESUELTO (2026-06-29) — `apb-design-frontend-design-system-v1.0` añadida a `apb-agent-ux-mockup-v1.0` (gap crítico corregido) + `apb-design-wcag-v1.0` creada (obligatoria por RD 1112/2018) |
| ~~M3~~ | ~~Documentar diferencia STRIDE vs ISO 27005 en las propias skills (cuándo usar cada una)~~ | Baja | ✅ RESUELTO (2026-06-29) — callout diferenciador añadido en `apb-sec-threat-model-v1.0` y `apb-sec-risk-analysis-v1.0` |
| ~~M4~~ | ~~`apb-ops-incident-diagnose-v1.0`: añadir nota sobre relación con `apb-ops-rca-v1.0`~~ | Baja | ✅ RESUELTO (verificado) — ya estaba documentado en ambas skills en sesión anterior |
| ~~M5~~ | ~~Agente PM dedicado para las 7 skills de gestión de proyecto huérfanas~~ | Media | ✅ RESUELTO (2026-06-29) — `apb-agent-pm-v1.0` creado con 8 skills PM; `consumed_by: apb-agent-pm-v1.0` añadido en las 8 skills |
| ~~M6~~ | ~~Encoding workflows: verificar que todos los .md están guardados UTF-8 sin BOM~~ | Baja | ✅ RESUELTO (2026-06-29) — `grep -rl $'\xef\xbb\xbf' workflows/` → sin BOM detectado |

---

## Puntos individuales ejecutados (extraídos de FUTURAS)

> Puntos numerados cuyo tema ya está resuelto con componente en el repo. Se
> retiran de `PLAN_FASES_FUTURAS.md` (queda un puntero) para que allí solo
> figure lo pendiente.

### #17 — Auditoría de skills/agentes de testing Playwright ✅
Material recibido en Sesión 8 (`apb-ai-skills.zip`); cobertura Playwright confirmada
(3 skills externas). Promovido y resuelto en la **Sesión QA — CERRADA** (ver arriba).

### #20 — Agente de mockups para perfiles funcionales ✅
Resuelto en **Sesión Frontend — CERRADA**: `apb-agent-ux-mockup-v1.0` creado (dominio `architecture`).

### #21 — Agente/skill de generación de frontend para desarrolladores ✅
Resuelto en **Sesión Frontend — CERRADA**: `apb-dev-devexpress-front-v1.0` actualizado +
`apb-dev-devexpress-selector-v1.0` nuevo.

### #22 — Catálogo de componentes / Sistema de diseño ✅
Resuelto en **Sesión Design System — CERRADA (2026-06-26, v1.3.0)**: repo `APB-DESIGN-SYSTEM`
creado (tokens CSS + componentes compuestos corporativos). Skills/agentes de diseño en
`APB-IA-FRAMEWORK`; artefactos CSS/JS en el repo propio.
Pendiente derivado vivo (queda en FUTURAS): **#53** (prueba e2e de que el agente de mockups
usa exclusivamente el Design System).

### #24 — Enfoque `multica-ai/andrej-karpathy-skills` ✅
Incorporado en Sesión 10/11: `apb-dev-simplicity-first-v1.0` y `apb-dev-surgical-changes-v1.0`
creadas (principios 2 "Simplicity First" y 3 "Surgical Changes"). Los principios 1
"Think Before Coding" y 4 "Goal-Driven Execution" se tratan como principio transversal
(referenciados en las propias skills; relacionados con el Principio Fundamental #8 "No vibe
coding" y con el punto #12 de loops). Repositorio MIT que condensa 4 principios operacionales
para agentes de codificación derivados de observaciones de Andrej Karpathy.

### #25 — Agente de análisis de deuda técnica y remediación ✅
Creado `apb-agent-tech-debt-v1.0`. Analiza sobre un repo/proyecto APB: deuda técnica,
vulnerabilidades, dependencias obsoletas, actualizaciones pendientes, cuellos de botella de
rendimiento e incumplimientos de políticas APB (LCSP, ENS, RGPD, WCAG 2.1 AA). Salida: plan
priorizado + apertura de tickets Jira (el agente propone, un humano decide — sin
auto-aprobación, `proyecto.md` §3.6).

### #31 — Skill de conversión universal a Markdown ✅
Creada `apb-plat-doc-to-markdown-v1.0` (dominio `platform`). Normaliza cualquier adjunto
(Office/PDF/etc.) a Markdown antes de ser consumido por agentes/skills/subagentes, bajo el
principio de que todos los componentes trabajan internamente en Markdown por eficiencia.

---

## Sesión #78 + #83 — Estándar de Prompting + Harness Engineering ✅ CERRADA (2026-07-02)

Decisión de Débora: sesión combinada (ambos puntos tocan plantillas + validador) y
**retrofit completo de una vez** (no por lotes), ejecutada ANTES del Enriquecimiento
#56–#76 para que los +69 componentes futuros nazcan conformes (anti-retrabajo).

### #78 — Estándar de prompting para TODOS los componentes ✅

La especificación de los 10 ejes vive ahora de forma permanente en
[`context/apb/standards/PROMPTING_STANDARD.md`](../context/apb/standards/PROMPTING_STANDARD.md)
(no se duplica aquí). Ejecutado:

- **Estándar canónico** `PROMPTING_STANDARD.md`: 10 ejes (razonar→plan→aceptación→ejecutar,
  objetivo verificable, autocrítica, ejemplos, formato, qué-NO-hacer, ejemplo E/S,
  separación SISTEMA/USUARIO); sección "Qué NO hacer" con 4 mínimos + **7 prohibiciones
  adicionales** (no declarar completado sin verificación, no auto-aprobarse, preguntar
  ante ambigüedad, no exceder alcance, no exponer secretos, anti-inyección, citar fuentes);
  ejemplo completo entrada→salida (caso `apb-dev-sonar-clean`); bloque canónico
  machine-checkable con 6 headings literales.
- **6 plantillas actualizadas** (`AGENT`, `SUBAGENT`, `SKILL_APB`, `SKILL_THIRD_PARTY`
  —capa wrapper—, `ADAPTER`, `WORKFLOW`) con el bloque + ítem de checklist.
- **Retrofit completo: 244 componentes** (35 agentes + 33 subagentes + 176 skills APB)
  vía `scripts/retrofit_prompting.py` (idempotente, deriva el contenido de lo que cada
  componente ya declara — referencia sus propias secciones, sin inventar capacidades).
- **Check #18 en `validate_repo.py`**: bloque canónico obligatorio (sección 🧭 + 6 headings
  literales) en skills APB, agentes y subagentes. Activado en **ERROR** tras el retrofit
  (anti-repetición: ningún componente nuevo puede nacer sin él). 3 tests unitarios.

### #83 — Harness Engineering agnóstico de LLM ✅

La especificación normativa vive ahora en **`SYSTEM.md §10`** (5 subsistemas, System of
Record + ACID, routing files 50–200 líneas, WIP=1 + Bootstrap Contract, Feature Lists) y
**`GOVERNANCE.md §8`** (Pass-State Gating, validación 3 capas, mensajes "bolígrafo rojo",
Clean State Handoff 5 dimensiones, bucle de limpieza, separación Planner/Generator/Evaluator
como insumo para #77). Ejecutado:

- **Gobernanza**: SYSTEM.md §10 (nuevo, Referencias renumeradas a §11) + GOVERNANCE.md §8
  (nuevo, Referencias renumeradas a §9). Todo agnóstico de LLM y herramienta (Principio #1):
  `AGENTS.md` como routing file canónico del que derivan las vistas por runtime, scripts
  portables en Python.
- **Scaffolding `repo-scaffold/harness-ready/`**: `AGENTS.md` (routing file plantilla),
  `PROGRESS.md` (Contrato de Bootstrap + registro de sesiones), `FEATURES.md` (Feature List
  con estructura triple y Pass-State Gating), `init_check.py` (inicialización dedicada,
  Python portable sin dependencias).
- **Check #19 en `validate_repo.py`** (`validate_harness_cold_start`): Cold-Start Test
  (las 5 preguntas → README/INDEX/SYSTEM/validador/CONTINUIDAD), secciones de gobernanza
  del harness presentes, scaffold completo. Nivel ERROR. 2 tests unitarios.
- **No implementado aquí** (dentro de lo previsto): telemetría OTel §83.7 (cruza con
  Sesión 17), arquitectura de 3 agentes ejecutable (→ #77 orquestación, bloqueada por
  decisión de runtime).

### Verificación de cierre

`generate_catalog.py` OK (INDEX actualizado) · `validate_repo.py --strict` **exit 0**
(0 errores; 60 warnings exentos de `source_commit`) · **38/38 tests** (33 validador
incl. 5 nuevos + 5 behavior) · contador del retrofit: 244 → 0.

---

## Enriquecimiento #56–#76 — ✅ EJECUTADO (Enriq. B/C/D) · reconciliado 2026-07-02

El bloque de construcción del análisis de enriquecimiento (`discovery/analisis-enriquecimiento-framework.md`)
se ejecutó a lo largo de las Sesiones Enriquecimiento B/C/D (posteriores a la A, que cubrió
#55 + primeros componentes). El plan `PLAN_FASES_FUTURAS.md` describía #56–#76 como "pendiente"
porque **no se había reconciliado**; el discovery del repo (2026-07-02) confirma que está creado
y cableado.

**Verificado en repo (2026-07-02):**

| Bloque | Propuesto | Creado | IDs |
|---|---|---|---|
| Agentes #56–#63 | 8 | **7** | change-manager, problem-manager, data-governance, accessibility-auditor, vendor-manager, knowledge-manager, api-product-manager |
| Subagentes #65 | 8 | **8** | ops-k8s, ops-servicebus, finops-azure, doc-confluence, sec-sast, qa-performance, gov-data, ops-entra |
| Skills #66–#72 | 43 | **43** | operation (+6), security (+4), governance (+8), platform+FinOps (+7), qa (+3), documentation (+4), architecture (+3), discovery (+4), pm (+3), design (+1) |
| Providers #73 | 5 | **5** | azure-cost, confluence, entra-id, sentinel, jira-software |
| Workflows #74 | 9 | **9** | change-management, problem-management, accessibility-audit, api-lifecycle, data-governance, finops-review, incident-l2, security-patch, vendor-procurement |

Todos verificados como ficheros reales (no stubs): frontmatter completo, prompt de sistema,
skills cableadas a agentes destino y `validate_repo.py --strict` exit 0. Además, todos quedaron
retrofitados al Estándar de Prompting (check #18) en la sesión #78+#83.

**No construido (por decisión, no por olvido):**

- **#59 `apb-agent-incident-l2`** — no se creó agente dedicado; la capacidad L2 la cubren
  `apb-agent-incident-support-v1.0` + `apb-agent-sre-v1.0` vía `apb-wf-incident-l2-v1.0`
  (+ subagentes ops k8s/servicebus/oracle). Mantener así salvo decisión de separarlo.
- **#64 `apb-agent-capacity-planner`** — diferido: requiere ≥12 meses de datos Azure.
- **#64 `apb-agent-portfolio-it`** — diferido: requiere datos reales de uso del framework.
- **#75 / #76** (calidad por agente / priorización) — aplicados como guía durante Enriq.;
  gaps de calidad residuales se rastrean vía check #18 y §H del plan.

**Pendiente de gobernanza (no de construcción):** los 7 agentes y sus skills están en `draft` —
requieren el ciclo de aprobación (validador humano nombrado) para pasar a `approved`.

---

## Fase G — TEST_PLAN_STANDARD v1.2.0: ID canónico + gobernanza por app + entrega dual MD/HTML — ✅ EJECUTADO 2026-07-03

Tras la corrección de conservación íntegra (Fase E-ter), Débora pidió cuatro mejoras adicionales
sobre la metodología de planes de pruebas, todas ejecutadas y commiteadas (`29b9799`):

- **Plantilla restaurada:** `context/apb/templates/TEST_PLAN.md` reescrita con las 16 secciones
  del ejemplo canónico (incluidas las que se habían perdido en la unificación original).
- **ID canónico con crecimiento:** esquema `{APP}-B{NN}-T{NN}` (§3.2 del estándar) — bloque y
  secuencia append-only, IDs nunca se renumeran ni se reutilizan. Los 112 casos de TruckCenter
  renumerados con columna "Legado" para no romper la trazabilidad con el informe ya emitido.
- **Gobernanza por aplicación (§6.1):** reutiliza `GOVERNANCE.md §2.1` (owner QA Lead/Analista
  Funcional) y §3 (ciclo `draft`→`candidate`→`approved`) — no se creó mecanismo paralelo.
- **Entrega dual Markdown + HTML (§7.1):** script nuevo `scripts/generate_test_plan_html.py`
  (sin CDN ni DevExpress) — cabecera azul corporativa + logo APB, acordeón nativo `<details>`,
  nav lateral. Verificado visualmente vía preview.
- Check #21 ampliado con la parte (c) (patrón de ID canónico) + 1 test nuevo.

`validate_repo.py --strict` exit 0 · 38/38 tests en ese momento.

---

## Fase H — AGENTS.md: routing raíz agnóstico de LLM y herramienta — ✅ EJECUTADO 2026-07-03

Débora corrigió una respuesta sobre "¿usamos OpenCode?" señalando el punto de fondo: **el
framework debe ser agnóstico al LLM y a la herramienta** — hoy Claude Code + GitHub, mañana
puede ser otra cosa. El principio ya estaba declarado (`SYSTEM.md §4.3`, §9, §10, `README.md`
principio #1) y la arquitectura de `adapters/`+`providers/` ya lo soportaba, pero se encontró
una grieta concreta que lo contradecía: el propio `SYSTEM.md §10.1` exige un routing file raíz
`AGENTS.md` del que deriven las vistas por runtime (`CLAUDE.md`, adapters) — pero ese `AGENTS.md`
no existía; el único fichero raíz era `CLAUDE.md`, específico de Claude Code, invirtiendo la
regla que el propio estándar exige.

**Ejecutado:**

- **`AGENTS.md`** (nuevo, raíz, 99 líneas): fuente única de las reglas antes duplicadas en
  `CLAUDE.md` (marcado IA, autonomía nivel 1, sin secretos, proceso de skill nueva, contexto
  corporativo obligatorio, formato de commits), con lenguaje agnóstico de LLM/herramienta.
- **`CLAUDE.md`** reescrito como fichero delgado que remite a `AGENTS.md` (Claude Code sigue
  auto-leyéndolo, pero ya no es la fuente).
- **`.github/copilot-instructions.md`** (nuevo): el mecanismo real que GitHub Copilot auto-lee
  en VS Code/Visual Studio — antes solo existía como configuración hipotética dentro del
  adapter `draft`, ahora está cableado de verdad. Débora señaló explícitamente **GitHub Copilot**
  como la alternativa concreta de "día después" a registrar (no un VCS distinto).
- `adapters/claude/adapter-claude-v1.0.md` y `adapters/copilot/adapter-copilot-v1.0.md` → v1.1.0,
  aclarando que documentan mapeo de *capacidades*, no reglas (que viven en `AGENTS.md`).
- `SYSTEM.md §4.1/§4.2/§10.1` actualizado: ya no describe un estado aspiracional, describe lo
  implementado.
- **Check #22** (`validate_agnostic_root_routing`) en `scripts/validate_repo.py`: `AGENTS.md`
  debe existir; `CLAUDE.md` y `.github/copilot-instructions.md` deben existir y referenciar
  `AGENTS.md` (anti-deriva — ninguna vista por runtime puede duplicar reglas de forma
  independiente). +3 tests en `tests/test_validate_repo.py`.

`generate_catalog.py` sin cambios (345 componentes; los ficheros de routing no son componentes
catalogables) · `validate_repo.py --strict` exit 0 · **41/41 tests**.

**Pendiente (fuera de esta sesión, registrado como futuro):** `providers/` solo tiene
`prov-github-v1.0.md` para control de versiones — si Débora diversifica de GitHub como
proveedor de VCS/CI (no de LLM/herramienta), haría falta un provider equivalente para la
alternativa elegida.

---

## Fase I — Roles, autorización del informe, ejecución local/CI/Azure-QA, SDD spec + fix-loop — ✅ EJECUTADO 2026-07-03

**Origen:** Débora detectó 7 huecos que hacían la metodología de planes de pruebas incompleta frente a un
uso real en APB. Tres exploraciones paralelas confirmaron la infraestructura ya existente (provider AKV
`draft`, roles por app en el ejemplo, workflow SDD, `prov-jira-software`, `apb-dev-pr-doc`, generador HTML)
y localizaron los huecos. Decisiones de Débora: (1) aprobar el **informe** — no el PR — con acta persistida
(Funcional + Desarrollador), sin exigir firma criptográfica; (2) **diseñar ya el provider Azure QA** en
`draft`; (3) **nuevo sub-workflow reutilizable** para el bucle fallo→PR→Jira.

**Ejecutado (`TEST_PLAN_STANDARD` v1.2.0 → v1.3.0; skill `apb-qa-test-plan` v1.3.0 → v1.4.0):**

- **Req 1 — Roles + usuario de ejecución:** §9.2 (matriz de roles + columna «Rol requerido» por caso;
  usuario por referencia **AKV** `prov-akv-v1.0` o aportado en runtime, **nunca en fichero**). Plantilla
  `TEST_PLAN.md` con la columna y la nota de usuario. Ejemplo TruckCenter (v1.3): §1.6 con «Bloques que lo
  requieren» + columna «Rol requerido» en las 12 tablas (112 casos, rol EntraID por bloque).
- **Req 2 — Informe corporativo:** §7.1 explícito para el informe; el HTML renderiza el **Acta de
  aprobación** como tabla de firmantes con estados en badge de color.
- **Req 3 — Autorización del informe:** §6.2 «Acta de aprobación del informe» (Funcional + Desarrollador,
  decisión + fecha, persistida en el `.md` **y** en Jira; sign-off no criptográfico; el agente no se
  autoaprueba). Plantilla §14bis. `generate_test_plan_html.py` con badges de estado.
- **Req 4 — Dónde corren Playwright/k6:** §9.1 «Destino de ejecución» (`local` / `ci-runner` / `azure-qa`;
  k6 nunca desde el portátil contra infra compartida).
- **Req 5 — Instalación local guiada:** nuevo `docs/qa/EJECUCION_LOCAL.md` (Node/Playwright/k6, Windows
  first, captura de `storageState`); la skill guía la instalación si falta tooling.
- **Req 6 — SDD:** §1 añade `spec` como fuente funcional autoritativa; skill con input `spec`;
  `apb-wf-sdd-full` Fase 6 pasa la spec a la skill. Bucle fallo→PR→Jira: nuevo subagente
  **`apb-sub-qa-fix-loop-v1.0`** (`draft`, parent `apb-agent-qa-auto-v1.0`) que **propone PR** (`apb-dev-pr-doc`)
  y **anota Jira** (`prov-jira-software`) — **nunca mergea**; cableado en `apb-wf-qa-evidence` y `apb-wf-sdd-full`.
- **Req 7 — Azure QA:** nuevo **`providers/prov-azure-qa-runtime-v1.0.md`** (`draft`): job efímero en la
  suscripción QA con Playwright+k6 pre-instalados, Managed Identity → AKV, sin instalar nada local.
  Implementaciones de referencia (ACA job / Container Instances / Azure Load Testing / MS Playwright
  Testing). **Diseño**; el despliegue real es QA-3. (Nota: los providers no se registran en `SYSTEM.md §4.2`
  — esa tabla es solo de adaptadores; el registro es el catálogo.)
- **Check #23** (`validate_execution_and_approval_methodology`): verifica que estándar, plantilla y ejemplo
  conservan las secciones obligatorias de Fase I (roles/«Rol requerido», acta de aprobación, destino de
  ejecución). +3 tests.

`generate_catalog.py` → **347 componentes** (345 + `apb-sub-qa-fix-loop-v1.0` + `prov-azure-qa-runtime-v1.0`,
ambos `draft`) · `validate_repo.py --strict` **exit 0** (0 errores, 60 warnings exentos) · **49/49 tests**.

**Pendiente (registrado, fuera de esta sesión):** despliegue real del entorno Azure QA (nombrar
suscripción/entorno + autorizar) → **QA-3**; ejecución funcional completa de TruckCenter con dataset,
rendimiento k6 y seguridad SonarQube/OWASP ZAP → **QA-3**.

**Fase I — corrección post-entrega (2026-07-03, feedback de Débora):**

- **Cobertura de tipos de prueba:** el plan carecía de bloques propios de **rendimiento** y **unitarias**
  (solo un caso aislado de fluidez en B06). Añadidos **Bloque B13 — Rendimiento (k6, 4 casos)** y
  **Bloque B14 — Pruebas Unitarias (xUnit, repo `APB.TRU`, 4 casos)**, append-only (§3.2). Total del
  ejemplo: **112 → 120 casos**. Unificado a **v1.4**.
- **Legibilidad:** varias secciones mezclaban información en un párrafo con separadores «·», difícil de
  leer (p. ej. §1.3 Integración con ARQ Docks, §1.7 Integraciones, §2.1 lógica ENTRADA/SALIDA, §2.2.1
  columnas/características del GRID). Reformateadas a **tabla**, mismo contenido (§3.1: sin pérdida).
- **`scripts/generate_test_plan_html.py`:** el título de la cabecera se renderizaba en gris oscuro sobre
  fondo azul (el selector global `h1{color}` pisaba el blanco heredado del `header`) — corregido con
  `color:#fff` explícito en `header.apb-header h1`; padding izquierdo alineado con el del contenido (32px).
- **Confirmado a Débora:** el informe de ejecución usa la **misma maquetación corporativa** que el plan
  (mismo script, cabecera azul + logo, menú, acordeones) — es agnóstico al tipo de documento, no una
  plantilla distinta.

`validate_repo.py --strict` exit 0 · **49/49 tests** (sin cambio de componentes catalogables — es
contenido de ejemplo y CSS, no un componente nuevo).

---

## Sesión QA TruckCenter — Ejecución real en PRE con el agente de navegación — ✅ CERRADA (2026-07-03)

**Origen:** Débora pidió ejecutar el plan de pruebas unificado de TruckCenter (`QA_TRU_TruckCenter_UNIFICADO.md`,
120 casos) con el agente del framework, con navegador real (login EntraID asistido por ella) e incluyendo
casos de **escritura** (no solo lectura), sobre el entorno PRE.

**Ejecutado:**

- **Sesión de navegación agéntica** (`apb-qa-exploratory-nav-v1.0` conducida vía extensión Chrome, provider
  `prov-browser-agent-v1.0`): **44 de 120 casos** con evidencia directa (lectura y escritura real en PRE) —
  bloques B02 (GRID), B03 (Alta, incluyendo el flujo completo de duplicado con confirmar/cancelar), B04
  (Modificación/Baja), B05 (Lupas), B06 (asignación de terminal), B07 (Tabla Maestra) y el E2E completo
  alta→modificar→salir del parking (`TRU-B12-T06`/T112).
- **2 hallazgos críticos en B07** (Tabla Maestra de Vehículos): **H1** — se pudo eliminar el tipo "Cisterna"
  sin ningún bloqueo pese a tener 4 expedientes dependientes (sin integridad referencial); **H2** — el
  maestro real tiene 9 tipos de vehículo, no los 5 documentados en el AF/plan (desactualización). H3/H4
  (auto-recuperación de tipo no disparada; pantalla de Auditoría `Forbidden` con el rol usado) registrados
  como no bloqueantes/limitación de alcance.
- **Plan unificado → v1.5:** matriz (§5) con columna Estado actualizada por caso ejecutado, checklist (§9)
  marcado, nueva **§15 Resultados de ejecución** con los 4 hallazgos y pendientes, histórico/aprobados
  (§13/§14) actualizados. HTML regenerado.

**Corrección de proceso (feedback de Débora tras la primera entrega del informe):** el informe de ejecución
se había generado solo en `.md`, sin listar por ID los casos NO ejecutados (solo un recuento agregado), y
con un GIF de la extensión Claude-in-Chrome (tope de 50 fotogramas) presentado como evidencia de sesión
completa sin verificar su cobertura real. Corregido y **codificado en el framework** para que no se repita:

- **`TEST_PLAN_STANDARD` v1.3.0 → v1.4.0:** nuevo **§5.15 Casos NO ejecutados/bloqueados** (obligatorio
  listar por ID canónico + motivo, no solo recuento); nuevo **§7.2 Evidencia visual: vídeo real, no GIF**
  (preferencia por vídeo nativo — p. ej. Playwright MCP `video:'on'` — o, en su defecto, GIF **segmentado
  por bloque** con la limitación declarada); refuerzo de §7.1 (entrega dual nunca solo `.md` en el informe).
  3 ítems nuevos en el checklist §10.
- **`apb-qa-exploratory-nav-v1.0` v1.0.0 → v1.1.0:** alineada — informe siempre MD+HTML, casos no
  ejecutados listados, evidencia vídeo real o GIF segmentado.
- **Check #24** (`validate_execution_report_evidence_methodology`): verifica que el estándar y la skill de
  navegación exploratoria no pierdan en silencio estas tres obligaciones. +3 tests.
- **Activación real de Playwright MCP** (para vídeo nativo en la próxima ejecución): `.mcp.json` de
  **proyecto** (versionado en el repo, no solo sesión de usuario) con el servidor oficial `@playwright/mcp`;
  `providers/prov-playwright-v1.0.md` v1.0.0 → v1.1.0 con la configuración real verificada (sustituye el
  placeholder conceptual `local://playwright`). **Norma general fijada por Débora**: al activar de verdad
  cualquier MCP conceptual del framework, seguir el mismo patrón (proyecto + doc actualizada), no solo este
  caso de Playwright.

`generate_catalog.py` → **347 componentes** (sin cambio — no se creó ningún componente nuevo, solo se
editaron existentes) · `validate_repo.py --strict` **exit 0** (0 errores, 60 warnings exentos) ·
**47/47 tests**.

**Pendiente (registrado, fuera de esta sesión):**
- Reiniciar/reabrir la sesión de Claude Code sobre el repo para que las herramientas de Playwright MCP
  queden disponibles (el `.mcp.json` no se carga en caliente).
- Confirmar el commit de `.mcp.json` + `prov-playwright-v1.0.md` (pendiente de OK de Débora).
- **Corregir H1** en TruckCenter (integridad referencial de Tipos de Vehículo) — prioridad alta, ya
  materializado en PRE.
- **Reejecutar el plan completo de TruckCenter** con vídeo real por bloque (Playwright MCP), cubriendo los
  76 casos restantes (B01, B08/B09/B10 completos con un segundo rol, B11/B13/B14 fuera de navegador).

### Continuación — Sesión II (misma fecha, 2026-07-03) — ⚠️ punto #88 NO seguido, queda abierto

**Origen:** Débora pidió continuar la ejecución del plan de TruckCenter en la misma jornada. El punto #88
(arriba) ya dejaba especificado reabrir Claude Code con Playwright MCP cargado + segundo usuario/rol antes
de retomar — no se consultó ese punto antes de empezar esta sesión II.

**Ejecutado:**
- **+11 casos netos** adicionales (vs. los 44 de la sesión I) + reconfirmación en vivo de H1/H2/H4.
  **Total acumulado: 55/120 casos con algún estado registrado, 65 siguen `Pendiente` sin tocar.**
- **3 hallazgos nuevos:** **H5** — el sistema rechaza un NIF de empresa manual no existente en Sòstrat
  ("Ese nif no se corresponde con ninguna Empresa de Transporte"), no permite el alta libre que describe
  §2.2.3/§2.2.5; **H6** — Nombre Conductor mapeado como "." (mapeo WS Sòstrat); **H7** — Swagger de
  `/trc/` (API `APB.API.LGP`) titulado como "APB.API.TRU" (documentación cruzada incorrecta).
- **Plan unificado → v1.6:** matriz/checklist actualizados, nueva **§16 Resultados de ejecución — Sesión
  QA navegador (2026-07-03, II)** con datos de ejecución, hallazgos H5-H7, tabla de casos no
  ejecutados/bloqueados por ID y motivo, y pendientes. HTML regenerado.
- Informes de ejecución (MD+HTML) en OneDrive
  `Proyectos/SDD - Framework desarrollo asistido por IA/QA_TruckCenter_evidencias/030726/`:
  `INFORME_EJECUCION_030726.md/.html` (sesión I) e `INFORME_EJECUCION_030726_II.md/.html` (sesión II),
  con GIF `QA_TruckCenter_030726_II_bloque1.gif` como evidencia (no segmentado por bloque — desviación del
  §7.2 del estándar, declarada en el informe).

**Corrección de proceso (feedback directo de Débora, 3 preguntas encadenadas):**
1. *"¿Has usado mi agente de QA? teóricamente el agente genera el informe, las evidencias, me pregunta si
   quiero abrir Jira"* — no se siguió el proceso "razonar → plan → aceptación → ejecutar" ni se ofreció
   Jira (§12/§6.3 de la skill).
2. *"¿Por qué has creado GIF si dijimos vídeo?"* — el punto #88 ya especificaba Playwright MCP para vídeo
   real; no se comprobó su disponibilidad antes de sustituirlo en silencio por GIF sin segmentar.
3. *"¿Por qué no puedes ejecutar el agente? ¿El runtime debería estar en el plan de fases futuras? ¿Es el
   informe incompleto o no se han ejecutado todas las pruebas? ¿Cómo evito que estos errores vuelvan a
   pasar?"* — confirmado: no existe motor de orquestación real (punto #77), el informe SÍ refleja con
   precisión lo ejecutado pero el alcance ejecutado fue un muestreo, no el plan completo pedido.

**Codificado en el framework para que no se repita:**
- **Punto #77** (`PLAN_FASES_FUTURAS.md`): nueva nota "Segunda recurrencia" — es la **segunda vez**
  documentada que ejecutar un agente/skill sin runtime real provoca un fallo de proceso (la primera fue la
  sesión DDD, 2026-06-30, SOJA mal clasificado).
- **Nueva memoria permanente** (fuera de este repo, en el sistema de memoria de Claude Code):
  `feedback_agente_runtime_vs_manual` — obliga a declarar explícitamente "runtime real" vs. "seguimiento
  manual del `.md`" al empezar cualquier invocación de agente/skill, más checklist de 5 puntos (comprobar
  PLAN_FASES antes, comprobar herramientas/MCP cargadas, plan+OK explícito antes de ejecutar, recuento
  numérico primero al cerrar, ofrecer Jira sin esperar a que se pida).

**Pendiente (registrado, fuera de esta sesión):** el **punto #88 sigue abierto tal cual** — la próxima
ejecución de TruckCenter debe reabrir Claude Code con Playwright MCP cargado desde el inicio, usar un
segundo usuario/rol para B08/B09, corregir H1/H5, y cubrir los 65 casos que siguen `Pendiente` (incluyendo
los ~26 estructuralmente fuera de alcance de navegador: B01/B11/B13/B14). Jira para H5/H6/H7 (y confirmar
estado de H1-H4) queda explícitamente en espera de instrucción directa de Débora.

---

## Sesión 19 — Terceros (#27/#45/#79/#81/#14/R8) + agentes de auditoría #86 y #85(O) — ✅ EJECUTADO 2026-07-04

**Alcance decidido por Débora en sesión:** de las fases ejecutables propuestas, eligió (1) Sesión 19
ampliada de terceros y (2) los agentes #86 + #85(O); el primer ciclo de aprobación se sacó de alcance
explícitamente. Sesión ejecutada como **seguimiento manual de los `.md`, sin runtime real** (declarado al
inicio, #77 pendiente), con acceso web para verificación de repos/licencias/SHAs.

**Fase A — Terceros (regla GOVERNANCE §4: evaluación aquí, incorporación solo tras OK de Débora):**

- **#79 (2/3 resuelto):** hallazgo de identidad — "Anthropic-Cybersecurity-Skills" es de `mukul975`
  (fuente **ya incorporada** con 5 skills curadas), no de Anthropic. El oficial real es
  `anthropics/defending-code-reference-harness` (Apache 2.0, SHA `b5b61c8`, 6 skills:
  threat-model/vuln-scan/triage/patch/quickstart/customize; harness autónomo requiere gVisor →
  excluido). Recomendación: descriptor único `third-anthropic-defending-code-v1.0` — **pendiente OK de
  Débora**. MCP Builder: alcance confirmado (`custom-api` cubre Teams/SharePoint del #30), no
  re-incorporar. "Fine Skills": sigue pendiente de URL de Débora (único resto abierto).
- **#27 items abiertos evaluados:** `context7` (MIT, ~58,5k⭐, servidor MCP de documentación → candidato
  a `prov-context7-v1.0` cuando haya caso de uso); `obra/superpowers systematic-debugging` (skill
  distinta confirmada, MIT → **candidata a incorporar**, pendiente OK); `mattpocock/skills` resto
  (repo reestructurado; mayoría duplica catálogo; 2 candidatas: `resolving-merge-conflicts` y `triage`);
  `excalidraw` (MIT, herramienta de apoyo, cierre sin componente).
- **#45 resuelto con datos:** las 3 skills `_spec-driven` del zip original de `apb-ai-skills` son
  **placeholders `[RESERVADO - NO ACTIVO]` sin implementar** — nada que fusionar; lo prometido ya lo
  cubre `apb-qa-test-plan-v1.0` v1.4.0 (input `spec`, Fase I). 2 ideas registradas (trazabilidad
  AC→TC automática; tests de contrato Pact desde plan.md).
- **#81 Obsidian resuelto:** herramienta de apoyo opcional solo-lectura (repo como vault sin
  transformación); salvaguardas: no editar desde Obsidian, `.obsidian/` al `.gitignore`. Sin componente.
- **#14 resuelto (omisión de Sesión 9):** licencia de `Lum1104/Understand-Anything` verificada = **MIT**
  (repo activo, commit `0e8ad84a`). `third-lum1104-knowledge-graph-v1.0`: `watchlist` → `draft`, con
  `license: MIT` + SHA. Bloqueo de producción levantado; su uso sigue siendo decisión de Débora.
- **R8 mitigado en su mayoría:** **48 descriptores** de terceros/wrappers fijados a SHA real
  (`git ls-remote` por repo, script una sola pasada); quedan **11** `unverified` con causa documentada
  (repos movidos/privados/no-GitHub). Warnings exentos del validador: 60 → **11**.

**Fase B — #86:** creado `agents/apb-agent-quality-compliance-v1.0.md` (`draft`, `qa`): multi-fuente
(Sonar + agentes + usuario), dedup obligatorio contra Jira antes de proponer, PR opcional con el patrón
fix-loop vía `apb-dev-pr-doc` (nunca merge). Wiring bidireccional (`consumed_by` añadido a sonar-clean,
pr-doc, telemetry-emit — incluyendo consumidores preexistentes no declarados: tech-debt, implementer).

**Fase C — #85(O):** creado `agents/apb-agent-design-compliance-v1.0.md` (`draft`, `design`): auditor a
posteriori contra APB-DESIGN-SYSTEM + WCAG 2.1 AA, informe MD+HTML (patrón `generate_test_plan_html.py`),
PR opcional, encadenable a #86. **Corrección sobre el diseño original del punto:** se cablea
`apb-qa-accessibility-v1.0`, no `apb-design-wcag-v1.0` (deprecada 2026-06-30).

**Check #25 (anti-repetición, regla de cierre):** el intento de cablear una skill deprecada en el agente
nuevo no lo detectaba nada, y el mismo defecto ya existía en `apb-agent-accessibility-auditor-v1.0`
(consumía `apb-design-wcag-patterns-v1.0`, deprecada — **corregido**). Nueva función
`validate_no_deprecated_wiring()` en `validate_repo.py`: ERROR si un componente activo cablea
(`skills`/`subagents`/`agents`/`depends_on`) un componente `deprecated`/`retired`; wiring histórico de
componentes ellos mismos deprecados queda exento. +3 tests (`TestNoDeprecatedWiring`).

`generate_catalog.py` → **349 componentes** (347 + `apb-agent-quality-compliance-v1.0` +
`apb-agent-design-compliance-v1.0`) · `validate_repo.py --strict` **exit 0** (0 errores, 11 warnings
exentos, antes 60) · **55/55 tests**.

**Incorporación aprobada por Débora (mismo día, GOVERNANCE §4) — 5 descriptores creados en `draft`:**
- `skills/third_party/anthropic/third-anthropic-defending-code-v1.0.md` (Apache 2.0, SHA `b5b61c8`,
  dominio `security`): 5 skills de análisis defensivo (threat-model/vuln-scan/triage/patch/customize);
  harness autónomo gVisor **excluido** por decisión de Arquitectura. Requiere validación de Ciberseguridad
  antes de `candidate`.
- `skills/third_party/obra/third-obra-systematic-debugging-v1.0.md` (MIT, SHA `84620bd`, `development`):
  skill standalone de depuración de 4 fases; cross-link al method wrapper para no duplicar.
- `skills/third_party/mattpocock/third-mattpocock-resolving-merge-conflicts-v1.0.md` (MIT, `development`).
- `skills/third_party/mattpocock/third-mattpocock-triage-v1.0.md` (MIT, `pm`).
- `providers/prov-context7-v1.0.md` (MIT, SHA `84620bd`, `provider_type: context`, `read-only`): servidor
  MCP de documentación actualizada; **`draft` sin activar** — activación real requiere `.mcp.json` de
  proyecto (norma `feedback_mcp_framework_activacion`).

`generate_catalog.py` → **354 componentes** (349 + 4 skills terceros + 1 provider) · `--strict` **exit 0**
(0 errores, 11 warnings exentos) · **55/55 tests**.

**Pendiente (registrado, fuera de esta sesión):** URL de "Fine Skills"; repo objetivo del primer caso real
de #85; re-identificación de los 11 repos sin SHA; decisión sobre reevaluar Understand-Anything ahora que
la licencia es MIT; validación de Ciberseguridad de `third-anthropic-defending-code` antes de `candidate`.

---

## Histórico completo de PLAN_FASES_FUTURAS.md — archivado 2026-07-06

> **Por qué está aquí:** `PLAN_FASES_FUTURAS.md` había crecido a 2311 líneas
> mezclando historial cerrado con lo genuinamente pendiente — al preguntar
> "¿qué queda pendiente?" el documento devolvía muy poco útil, señal de que
> estaba mal estructurado. Se hizo una auditoría de **7 rondas de solo
> lectura contra el repo real** (no solo contra lo que este documento decía):
> `validate_repo.py --strict` (0 errores, 60/60 tests), lectura íntegra de
> `PLAN_FASES_FUTURAS.md`, `HANDOFF_TECNICOS.md`, `HANDOFF_ORQUESTACION_MOTOR.md`,
> `WORKSTREAMS_SUMMARY_2026-07-06.md`, `AUTONOMY_ANALYSIS_2026-07-06.md` y
> ambas auditorías de proyecto, más **verificación de completitud** (no solo
> existencia) de 6 entregables muestreados — 3 de ellos del histórico más
> antiguo de este mismo fichero, nunca re-auditado hasta ahora.
>
> **Resultado de la verificación de completitud:**
>
> | Verificado | Resultado |
> |---|---|
> | `apb-gov-org-risk-report-v1.0` (7 marcos normativos) | ⚠️ **PARCIAL** — 5/7 desarrollados (ENS, ISO 27001, NIST, RGPD, OWASP); **LCSP y WCAG son mención superficial sin checklist operativo propio** — movido a backlog ejecutable en `PLAN_FASES_FUTURAS.md` Sección B en vez de darse por cerrado sin matices |
> | `apb-sub-ddd-interview-v1.0` (4 capacidades) | ✅ COMPLETO |
> | `PROMPTING_STANDARD.md` (10 ejes + 6 plantillas) | ✅ COMPLETO — recuento exacto confirmado |
> | 3 componentes antiguos al azar (`apb-agent-ux-mockup-v1.0`, `apb-dev-simplicity-first-v1.0`, `apb-plat-doc-to-markdown-v1.0`) | ✅ COMPLETO |
> | 21 dominios en `APB-DOMAIN-CATALOG` | ✅ Cifra exacta confirmada por conteo real |
> | 182/182 skills con marcado IA | ✅ Correcto (nota menor: 183 menciones de grep vs 182 ficheros, probable doble match, no bloqueante) |
>
> **Un gap real de handoff detectado:** Sesión 15 (línea 807 más abajo) cita
> `docs/HANDOFF_SESION15_INTEGRACIONES.md` como entregable — ese fichero
> **no existe**; su contenido ya vive de facto en `HANDOFF_TECNICOS.md §4`.
> Corregidas las 4 referencias colgantes del repo (`CONTINUIDAD_PROYECTO.md`,
> `docs/guia-funcional.md`, `docs/manual-arquitectura.md`, y esta misma nota).
>
> **Documentos sueltos disueltos en esta reorganización** (ya no existen como
> ficheros independientes — su contenido se distribuyó entre este archivo,
> `PLAN_FASES_FUTURAS.md` y `HANDOFF_TECNICOS.md`):
> - `HANDOFF_ORQUESTACION_MOTOR.md` — PoC del punto #77 ya entregada
>   (`scripts/orchestrate_checkpoint_gate.py`, `.github/workflows/human-checkpoint-poc.yml`,
>   `scripts/setup_github_environment.py`, funcionando); matriz de opciones de
>   motor (Azure Durable Functions/LangGraph/Temporal.io) → `PLAN_FASES_FUTURAS.md`
>   Sección A; pasos condicionados a la decisión → `HANDOFF_TECNICOS.md`.
> - `WORKSTREAMS_SUMMARY_2026-07-06.md` — entregado: skill
>   `apb-plat-dashboards-generator-v1.0`, subagente `apb-sub-dashboard-discovery-v1.0`,
>   dashboard Grafana JSON + spec Power BI + DAX (`discovery/qa-compliance-grafana-dashboard.json`,
>   `discovery/qa-compliance-powerbi-spec.json`), runbook operativo
>   (`discovery/QA_COMPLIANCE_DASHBOARD_RUNBOOK.md`, que se conserva tal cual)
>   y análisis de autonomía (350 componentes escaneados: L0=1, L1=318, L2=31,
>   L3/4=0; 3 candidatos a promoción L2 identificados). Pasos de despliegue
>   real → `HANDOFF_TECNICOS.md`; 3 de los 4 gaps de enforcement (timeout,
>   loop detection, hardcoded limits) → `PLAN_FASES_FUTURAS.md` Sección B; el
>   4º (async messaging) → `HANDOFF_TECNICOS.md` (requiere infraestructura).
> - `AUTONOMY_ANALYSIS_2026-07-06.md` — duplicado casi literal de la
>   Workstream 2 del fichero anterior; eliminado sin pérdida de información.
> - `AUDIT_DESIGN_COMPLIANCE_TRU_2026-07-06.md` y
>   `AUDIT_QUALITY_COMPLIANCE_SMS_2026-07-06.md` — auditorías reales y
>   cerradas de aplicaciones concretas (TruckCenter, SMS) con hallazgos para
>   los equipos de desarrollo de esas apps, no estado del framework. Movidas
>   a `discovery/archive/` (misma convención que el resto de este archivo).
>   Follow-ups pendientes de un humano (TruckCenter: refactor CSS ~4-5h; SMS:
>   revisar ticket ARQ-3716) → `HANDOFF_TECNICOS.md`.
>
> **A partir de aquí, el texto es el histórico íntegro y verbatim** (sin
> resumir) que vivía en `PLAN_FASES_FUTURAS.md` hasta esta fecha — se
> conserva completo como bitácora de auditoría, aunque la mayoría de su
> contenido ya estaba correctamente marcado como cerrado en las tablas
> anteriores de este mismo fichero. Los pocos puntos que seguían realmente
> abiertos dentro de este texto (identificables porque no llevan ✅) ya están
> extraídos y clasificados en `PLAN_FASES_FUTURAS.md` (Secciones A/B/C) — no
> hace falta volver a leerlos aquí para saber qué queda pendiente.

<details><summary>Texto íntegro archivado (2311 líneas, click para expandir)</summary>

## Mapeo a sesiones planificadas (actualizado durante Sesión 8)

| Punto (#) | Sesión asignada |
|---|---|
| 1 (OpenSpec/SDD) | 8 (parcial — cobertura cap. 5 proyecto.md) |
| 2 (Guía de uso de agentes) | **13** |
| 3 (flujo legacy→SDD) | 8 (parcial — checklist de cobertura) |
| 4 (Sonar + PR automático) | ✅ **Resuelto, Sesión 11** — discovery confirmó que ya existía: `apb-dev-sonar-clean-v1.0`, `apb-dev-pr-doc-v1.0`, `prov-sonar-v1.0`, conectados a `apb-agent-implementer-v1.0`. No se reimplementó. |
| 5 (agente meta-gobernanza) | ✅ **Resuelto, Sesión 10** — `apb-agent-meta-builder-v1.0` creado (dominio `governance`). |
| 6 (plantillas + ofimáticas) | **13** — requiere ejemplos de Debora |
| 7 (mapa agentes↔Jira) | **13** |
| 8 (COSMIC con histórico real) | **13** — requiere datos de Debora |
| 9 (documentar terceros) | **9** |
| 10 (catálogo automático) | ✅ Resuelto, Sesión 3 |
| 11 (DDD + inventario dominios negocio) | ✅ **Unificado con #38 Fase 0** (decisión Debora post-Sesión 9) — mismo artefacto, se resuelve en la sesión de #38, no en 13 |
| 12 (loops de iteración) | **13** |
| 13 (guía UI/UX) | ✅ **Documentos recibidos** (ver bloque nuevo abajo) — tratamiento en **Sesión Frontend** |
| 14 (licencia Understand-Anything) | ✅ **RESUELTO (Sesión 19, 2026-07-04)** — licencia de `Lum1104/Understand-Anything` verificada: **MIT**. El bloqueo de producción por licencia desconocida (motivo de la decisión inicial de Débora de no usarlo) queda levantado; `third-lum1104-knowledge-graph-v1.0.md` **existe** en el repo, en `status: draft`, sin `consumed_by` (sin wiring). Uso futuro pendiente de reevaluación de Débora ahora que la licencia está clara — ver detalle más abajo. *(Corregido 2026-07-04: esta fila decía antes "descartado, eliminado del repo", desactualizada frente al detalle del punto #14 más abajo tras la Sesión 19 — quedaban dos afirmaciones contradictorias en el mismo fichero.)* |
| 15 (soporte incidencias técnicas) | **Sesión 21** |
| 16 (análisis de riesgos validación Ciber/Arq/QA) | **Sesión 12** (parcial) + **Sesión 16** (pendiente). Sesión 12 construyó `apb-gov-ai-risk-gate-v1.0` — evalúa los 6 riesgos *específicos de uso de IA* de `proyecto.md` §3.5. **El alcance completo del punto #16 queda pendiente para Sesión 16:** informe de análisis de riesgos organizativo (incumplimientos de políticas APB, deuda técnica, ENS nivel alto) con procedimiento de excepciones corporativo, para validación por Ciberseguridad y Arquitectura — informe listo para que un humano decida si acepta el incumplimiento y qué plan de mitigación exige. Requiere: esbozo de contenido del informe que facilitará Debora + procedimiento corporativo de excepciones. |
| 17 (auditoría Playwright/apb-ai-skills) | ✅ **Sesión QA — CERRADA** (4 fusiones realizadas, apb-ai-skills deprecado) |
| 18 (comparar funcionalidad GitHub vs. zips previos) | **8** |
| 19 (checklist exhaustivo proyecto.md) | **8** |
| 20 (agente mockups UI para funcionales, añadido hoy) | ✅ **Resuelto, Sesión Frontend** — `apb-agent-ux-mockup-v1.0` creado |
| 21 (agente generación frontend para devs, añadido hoy) | ✅ **Resuelto, Sesión Frontend** — `apb-dev-devexpress-front-v1.0` actualizado + `apb-dev-devexpress-selector-v1.0` nuevo |
| 22 (análisis catálogo de componentes/sistema de diseño, añadido hoy) | **Sesión Design System** — confirmado por Debora (2026-06-24): múltiples equipos usan DevExtreme, componentes corporativos ya se copian entre proyectos. Repo GitHub propio `apb-design-system`; skills/agentes quedan en `APB-IA-FRAMEWORK`. |
| 23 (documentación por audiencias en Word, añadido hoy) | **14** — última sesión del plan |
| 24 (incorporar enfoque andrej-karpathy-skills, añadido hoy) | ✅ **Confirmado: Sesión 10** (decisión Debora post-Sesión 9) — resolver antes/dentro del briefing, no después en 13 |
| 25 (agente de deuda técnica/vulnerabilidades/remediación con Jira, añadido hoy) | ✅ **Confirmado: ampliación de Sesión 11** (decisión Debora post-Sesión 9) — alcance completo: deuda técnica, vulnerabilidades, dependencias obsoletas, rendimiento, incumplimientos de políticas APB |
| 26 (telemetría para KPIs proyecto.md §6, añadido hoy — checklist Sesión 8) | A determinar — relacionado con Sesión 14 |
| 31 (skill conversión universal a Markdown) | ✅ **Confirmado: Sesión 10** (decisión Debora post-Sesión 9), junto con #24 |
| 38 Fase 0 (catálogo de dominios) | ✅ **EJECUTADO (Sesión DDD, 2026-06-30)** — inventario `API_INVENTORY_APIM.md` recibido; 21 dominios de negocio `proposed` en `APB-DOMAIN-CATALOG/domains/`. Incluye #11. Pendiente: aprobación Arquitectura + fronteras de negocio. BCs diferidos a "DDD Fase BC" (requiere código) |
| 33 (skills/agentes de SQL) | **Sesión 21** |
| 34 (validación QA en flujos de despliegue) | **Sesión 21** — aplica a framework y aplicaciones APB; durante construcción del framework no se activa sobre el propio repo, pero se diseña para poder hacerlo. |
| 43 (aplicación retroactiva de política "Generado por IA" + "Validado por humano" a TODO el catálogo) | ✅ **CERRADA (Sesión 23, 2026-06-26)** — ver detalle en punto #43 abajo |

| 77 (orquestación y coreografía de agentes) | **Sesión de Análisis de Orquestación** (nueva, bloqueante: decisión runtime Debora + Plataforma) |

**Nota Sesión 8 (3ª corrección, mismo día):** Debora pidió separar la
Sesión QA (testing: Playwright, `apb-ai-skills`, solape con el framework)
de una **Sesión Frontend** propia e independiente (mockups, generación de
frontend para devs, catálogo de componentes/sistema de diseño). No son la
misma sesión aunque ambas usen la guía de estilo y DevExpress como insumo
común — QA es sobre pruebas, Frontend es sobre construcción de interfaz.

**Nota Sesión 8 (2ª corrección de proceso, mismo día):** Debora señaló un
segundo punto ausente del plan — documentación del framework en Word,
segmentada por audiencia (arquitectos, desarrolladores/analistas, dirección)
— que había sido hablado en sesiones/chats previos pero **nunca llegó a
registrarse en ningún documento del repo** (verificado: no aparece en
`proyecto.md` §7 "Entregables clave", que solo menciona "Guía de uso de
herramientas (Rovo, Copilot, etc.)" como único entregable documental, sin
segmentación por audiencia ni formato). A diferencia de los puntos 11-13,
este no es un caso de "anotado sin fecha" — es un caso de "nunca anotado".
Corregido ahora.

**Nota Sesión 8 — corrección de proceso:** los puntos 2, 6, 7, 8, 11 y 12
estaban marcados como "sin sesión asignada" al cierre de la Sesión 7.
Debora señaló que esto generaba la duda razonable de si de verdad estaban
en el plan. Se corrige asignándoles **Sesión 13** (sesión de cierre de
pendientes históricos), en vez de dejarlos en un cajón sin fecha.

## Sesión QA — ✅ CERRADA · Sesión Frontend — ✅ CERRADA

> ✅ **Ejecutadas** (QA post-Sesión 12; Frontend 2026-06-24). Registro completo
> movido a [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).
> Pendiente derivado que sigue vivo: **#22** (catálogo de componentes /
> design system más allá de la guía en PDF) — ver más abajo.

---

## Bloque añadido (continuación de Sesión 2)

1. **Estandarización Spec Driven Development / OpenSpec Kit**
   Verificar que el framework tiene todo lo necesario para trabajar con SDD
   basado en OpenSpec Kit (`https://github.com/Fission-AI/OpenSpec`).
   Valorar si GitHub Spec Kit aporta algo de valor adicional que incorporar
   o complementar.

2. **Guía de uso de agentes**
   Crear documento guía (`docs/AGENT_USAGE_GUIDE.md` o similar) explicando
   cómo usar los agentes del framework: cuándo invocar cada uno, qué
   esperar como input/output, flujo de aprobación humana asociado.

3. **Flujo/agente de ciclo completo legacy → SDD**
   Identificar si existe ya un flujo o agente que cubra el ciclo completo de
   una aplicación existente (legacy) a través de SDD de principio a fin, o
   si hay que construirlo. Candidatos a revisar: `apb-wf-legacy-onboarding-v1.0`,
   `apb-wf-spec-from-legacy-v1.0`, `apb-agent-modernization-v1.0`.

4. **Corrección de incumplimientos Sonar + PR automático**
   Verificar si el framework tiene lo necesario para: (a) corregir
   incumplimientos detectados por SonarQube/SonarCloud, y (b) preparar un
   Pull Request con esas correcciones. Candidatos a revisar:
   `apb-dev-sonar-clean-v1.0`, `apb-dev-pr-doc-v1.0`, provider `prov-sonar-v1.0`.

5. **(Ya en plan previo, se mantiene)** Agente/subagentes/skills para crear
   agentes/subagentes/skills siguiendo el estándar del framework,
   actualizando catálogo e índice automáticamente.
6. **(Ya en plan previo)** Verificar cobertura de plantillas de todos los
   tipos de componente + plantillas ofimáticas (Debora aportará ejemplos).
7. **(Ya en plan previo)** Mapa de interacción agentes/subagentes ↔ Jira:
   qué agente crea qué ticket y en qué momento (ej. tras OK de backlog,
   tras valoración COSMIC).
8. **(Ya en plan previo)** Entrenar valoración COSMIC con histórico real de
   horas de la organización, para informar conversión puntos↔horas de cara
   a facturación de proveedores por precio/hora.
9. **(Ya en plan previo)** Documentar cómo quedaron estructuradas las
   skills de terceros y el enriquecimiento que aplica APB sobre ellas.
10. **(Ya en plan previo)** Mecanismo de actualización automática del
    catálogo e índice del framework (relacionado con Sesión 3).

## Bloque añadido (2ª ronda, continuación de Sesión 2)

11. **Análisis basados en DDD + inventario global de dominios**
    Asegurar que los análisis del framework (discovery, arquitectura,
    modernización) se basan consistentemente en DDD. Construir un
    inventario global de dominios de negocio APB (distinto de
    `DOMAIN_REGISTRY.md`, que es de dominios *funcionales del framework*,
    no de dominios *de negocio APB*) con gobernanza definida y mecanismo de
    actualización automática — relacionado con el "mecanismo anti-duplicación
    de dominios" ya señalado como gap en `Plan_trabajo_correcciones_GitHub.md`
    punto 4.
12. **Necesidad de definir loops**
    Evaluar si el framework necesita bucles de iteración/retroalimentación
    explícitos (p. ej. reflexión iterativa ya cubierta parcialmente por
    `apb-dev-autocorrect-v1.0`, o loops de validación humana repetida) y
    dónde se formalizarían (¿a nivel de skill, de workflow, de agente?).
13. **Guía de estilo UI/UX como política/contexto corporativo** ✅
    **Documentos recibidos en Sesión 8** (ver "Sesión Frontend" arriba):
    `Guía_Estilos__Port_de_Barcelona__2022__v1.pdf`,
    `GISPEM__Guía_de_estilos.pdf`, `ManualUsuario_WidgetsLayout_v1.pdf`.
    Debe tratarse como política o contexto corporativo (ubicación candidata:
    `context/apb/policies/` o `context/apb/standards/`), y las skills de
    frontend (DevExpress, React/Stitch, frontend-integration) deben
    referenciarla y tenerla en cuenta. Tratamiento completo en Sesión
    Frontend.

## Bloque añadido (cierre de Sesión 7 / apertura Sesión 8)

14. **Verificar licencia de Understand-Anything** ✅ **RESUELTO (Sesión 19,
    2026-07-04).** Licencia verificada vía API de GitHub sobre
    `Lum1104/Understand-Anything`: **MIT** (SPDX confirmado), repo activo
    (~70,7k ⭐, último push 2026-07-03), commit fijado `0e8ad84a`. El stub
    `third-lum1104-knowledge-graph-v1.0` pasa de `watchlist` a `draft` con
    `license: MIT` y `source_commit` real; bloqueo de producción por
    licencia levantado (`CONTINUIDAD_PROYECTO.md §5.14` actualizado).
    Nota: la decisión previa de Débora de descartar el componente (fila 14
    de la tabla de mapeo) se tomó con licencia desconocida — puede
    reevaluarse ahora o mantenerse el descarte; hasta que lo decida, el
    componente queda en `draft` sin consumidores.
    **Corrección de consistencia (2026-07-04):** la fila 14 de la tabla de
    mapeo (arriba, línea ~30) seguía diciendo "descartado, eliminado del
    repo" pese a esta resolución — corregida para que ambas coincidan.
    **Recomendación (no decisión) para cuando Débora reevalúe el uso:**
    candidato natural es `apb-agent-ddd-v1.0` / `apb-sub-ddd-interview-v1.0`
    (construcción de grafos de conocimiento de dominio a partir de
    documentación no estructurada) — no se cablea aquí, es una decisión de
    negocio pendiente.

15. **Soporte a incidencias técnicas generalista**
    Agente/skill que ayude a diagnosticar y resolver incidencias técnicas de
    cualquier tipo (no solo desarrollo) a partir de descripción en lenguaje
    natural, capturas de pantalla/imágenes, o logs. Distinto de
    `apb-agent-sre-v1.0` (RCA formal post-incidente): este es soporte de
    primera línea, más amplio en alcance (no exclusivamente SRE/operación).

16. **Análisis de riesgos para validación de Ciberseguridad/Arquitectura/QA**
    Skill/agente que aplique las políticas corporativas APB y el
    procedimiento de gestión de excepciones/incumplimientos (`proyecto.md`
    §3.5 Gestión de Riesgos, §3.3 Gestión de Excepciones) y genere un informe
    de análisis de riesgos **listo para validación humana** — nunca
    auto-aprobado, el agente no puede aprobar sus propias excepciones
    (principio ya establecido en `proyecto.md` §3.6).

    **Decisión de Debora (Sesión 12, post-Sesión 11):** se construye como
    **skill transversal** (no agente propio, no subagente) — cualquier
    agente del framework la invoca antes de presentar su output a
    validación humana, en cualquiera de las 11 fases de la tabla de Puntos
    de Validación Obligatorios de `proyecto.md` §3.6. Cubre los 6 riesgos
    específicos del uso de IA listados en §3.5 (alucinaciones, información
    desactualizada, incumplimiento de estándares, dependencia excesiva,
    pérdida de conocimiento humano, código inseguro) — **distinto** de
    `apb-sec-risk-analysis-v1.0` (riesgos de seguridad de la información,
    ISO 27005/NIST/MAGERIT, sobre activos técnicos), que no se duplica.

    **Decisión de Debora (Sesión 12, post-Sesión 11):** la fila "Release" se
    resuelve como **"Release Manager / Arquitectura"** en ambos documentos.
    Aplicado en `SYSTEM.md` §6 (era "PMO / Operaciones / Arquitectura",
    corregido). **`proyecto.md` §3.6 no se pudo actualizar** — es un
    documento de proyecto en `/mnt/project/`, de solo lectura para Claude;
    Debora debe actualizar manualmente esa celda de "¿?" a "Release Manager
    / Arquitectura" en su copia del documento, o pedir a Claude que genere
    el texto exacto a copiar si lo prefiere.

17. **Auditoría de skills/agentes de testing Playwright** — ✅ EJECUTADO
    (Sesión QA). Detalle en [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).

18. **Comparación de funcionalidad: GitHub real vs. zip vs. zips de sesiones previas**
    Confirmar que no se ha perdido funcionalidad respecto al repo de GitHub
    (rama paralela, ver nota Sesión 7) ni respecto a zips de sesiones de
    trabajo previas que Debora guardó localmente — Sesión 8.

19. **Checklist exhaustivo de cobertura de `proyecto.md`**
    No limitarse a la tabla de skills de `Plan_trabajo_correcciones_GitHub.md`
    §5.1 (ya parcialmente desactualizada tras Sesión 1.5c) — verificar
    sistemáticamente cobertura de TODO `proyecto.md`: agentes (§4), KPIs
    (§6), entregables clave (§7), no solo skills (§5) — Sesión 8.

## Bloque añadido durante Sesión 8 (Sesión Frontend)

20. **Agente de mockups para perfiles funcionales** — ✅ EJECUTADO (Sesión
    Frontend: `apb-agent-ux-mockup-v1.0`). Detalle en [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).

21. **Agente/skill de generación de frontend para desarrolladores** — ✅
    EJECUTADO (Sesión Frontend: `apb-dev-devexpress-front-v1.0` +
    `apb-dev-devexpress-selector-v1.0`). Detalle en [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).

22. **Catálogo de componentes / sistema de diseño** — ✅ EJECUTADO (Sesión
    Design System, repo `APB-DESIGN-SYSTEM`). Detalle en [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).
    Pendiente derivado vivo: **#53** (prueba e2e Design System).

23. **Documentación del framework por audiencias, en formato Word**
    Generar documentación de `APB-IA-FRAMEWORK` (no de `apb-ai-skills`,
    confirmado por Debora en Sesión 8) segmentada en tres documentos
    distintos, cada uno como entregable Word (.docx):
    - **Arquitectos** que mantienen el framework de IA: cómo está
      estructurado, cómo se extiende, cómo funciona la gobernanza
      (`SCHEMA.md`, `GOVERNANCE.md`, validador, CI), cómo se crean nuevos
      componentes.
    - **Desarrolladores / analistas / perfiles de uso**: cómo invocar
      agentes y skills en el día a día, qué esperar de cada uno, flujo de
      aprobación humana — construye sobre `docs/sdd-getting-started.md`
      (Sesión 7) pero en formato Word y con más profundidad por rol.
    - **Dirección**: documento ejecutivo de alto nivel — qué es el
      framework, qué resuelve, estado de adopción, métricas (conectar con
      `proyecto.md` §3.7 Métricas y Seguimiento), sin detalle técnico.

    Última sesión del plan (Sesión 14) — se beneficia de que todas las
    sesiones anteriores (8-13) ya hayan cerrado gaps de cobertura, para no
    documentar un estado todavía incompleto del framework.

    **Estado 2026-06-27:** borradores Markdown ya disponibles en el repo:
    - `docs/guia-funcional.md` — guía para analistas, desarrolladores y
      jefes de proyecto (cubre: qué hace el framework, cómo empezar, reglas
      de uso, catálogo completo de agentes/workflows/skills, integración con
      las herramientas existentes, limitaciones actuales, ejemplos de uso
      real). Equivale al documento de audiencia "Desarrolladores / analistas".
    - `docs/manual-arquitectura.md` — manual para arquitectos y Tech Leads
      (cubre: mapa técnico de componentes, jerarquía, inventario por capa,
      infraestructura de gobierno/validación, gaps técnicos detectados,
      recomendaciones de infraestructura, componentes futuros recomendados,
      guía de extensibilidad, modelo de gobernanza, deuda técnica del propio
      framework). Equivale al documento de audiencia "Arquitectos".
    Ambos documentos están en estado draft (generados 2026-06-27) y
    **pendientes de validación humana por Arquitectura APB**. La Sesión 14
    los convierte a .docx y añade el documento de Dirección (que aún no
    existe en ningún formato).

24. **Incorporar el enfoque de `multica-ai/andrej-karpathy-skills`** — ✅
    EJECUTADO (Sesión 10/11): `apb-dev-simplicity-first-v1.0` +
    `apb-dev-surgical-changes-v1.0` creadas; principios 1 y 4 tratados como
    transversales. Detalle en [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).

25. **Agente/subagente de análisis de deuda técnica y remediación** — ✅
    EJECUTADO: `apb-agent-tech-debt-v1.0` creado (deuda, vulnerabilidades,
    dependencias, rendimiento, incumplimientos APB → plan priorizado +
    tickets Jira). Detalle en [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).

26. **Mecanismo de telemetría para los KPIs de `proyecto.md` §6**
    (añadido en Sesión 8, durante el checklist exhaustivo). El framework no
    tiene ningún mecanismo documentado para producir los datos que
    alimentarían las 7 dimensiones de KPIs de `proyecto.md` §6
    (Productividad, Calidad, Arquitectura, Uso de IA, Adopción, SDD,
    Automatización, Gestión de Riesgos) — son métricas de uso en
    producción, no componentes que se "construyen" como skill/agente, pero
    sin instrumentación no hay forma de medirlas. Evaluar: ¿campo de
    telemetría en `SCHEMA.md` (ej. `invocation_count`, `human_override_rate`
    por componente), skill de reporting dedicada, o ambos? Relacionado con
    `proyecto.md` §3.7 (Métricas y Seguimiento) y con la Sesión 14
    (documentación ejecutiva para Dirección, que necesitará estos datos
    para tener contenido real, no solo cualitativo). Sesión a determinar.

## Bloque añadido durante Sesión 9 (Debora, mismo día — volumen alto, pendiente de asignación fina de sesión)

> **Nota de proceso:** este bloque agrupa una petición muy densa recibida en
> un único mensaje. Se ha separado en sub-bloques temáticos para mantener
> trazabilidad. Ninguno de estos puntos se ejecuta en Sesión 9 — Sesión 9
> está acotada a §8 de `proyecto.md` (ya en curso). Se proponen sesiones
> candidatas, a confirmar con Debora.

### 27. Repos de terceros adicionales a evaluar (ampliación de §8)

Repos/skills mencionados por Debora para evaluar valor de incorporación,
**no confirmados todavía como §8 oficial** — pendiente de que Debora
confirme si se añaden formalmente a `proyecto.md` §8 o se tratan como lista
paralela. Aparcados para una futura sesión de terceros (¿Sesión 9-bis o
ampliación de Sesión 9?):

- `obra/superpowers` — ya incorporado parcialmente (`third-obra-superpowers-method-v1.0`,
  `third-obra-test-driven-development-v1.0` en Sesión 8); Debora pide
  revisar si falta algo, en concreto **"systematic debugging" de superpowers**
  (mencionado aparte) — verificar si es una skill distinta dentro del mismo
  repo no incorporada aún
- `context7` — gestor de contexto/documentación para LLMs, sin evaluar
- `excalidraw` — herramienta de diagramas; evaluar como posible integración
  para skills de arquitectura/diseño (no como skill en sí, sino posible
  MCP/herramienta)
- `ui ux pro max` — ya evaluado en Sesión 9 actual
  (`nextlevelbuilder/ui-ux-pro-max-skill`, ya incorporado como
  `third-nextlevel-ux-v1.0` en Sesión 8) — confirmar con Debora si se
  refiere a este mismo o a otro recurso
- ✅ **`impecable` — RESUELTO (post-Sesión 9):** `pbakaus/impeccable`
  ("The design language that makes your AI harness better at design").
  Sistema de detección de antipatrones de diseño/UI para harnesses de IA
  (Claude, Cursor, Copilot, Gemini, Codex), con CLI npm, reglas
  deterministas (44 detectores) + crítica vía LLM, hooks de post-edición.
  Verificado por búsqueda directa, repo activo. **DESCARTADO por decisión
  de Debora** — no se incorpora al catálogo.
- ✅ **`caveman` — RESUELTO (post-Sesión 9):** `JuliusBrussee/caveman`
  (~76.3k★ a fecha de verificación, no ~60k como estimó Debora). Skill que
  hace que el agente responda en estilo telegráfico para ahorrar tokens de
  salida — no es una capacidad técnica de desarrollo/arquitectura.
  **DESCARTADO por decisión de Debora** — no se incorpora al catálogo.
- ✅ **`kim barret` — RESUELTO (post-Sesión 9):** `realkimbarrett/*`
  (`avatar-extraction`, `offer-extraction`, `schwartz-awareness-mapper`,
  `mechanism-builder`, `headline-matrix`, `objection-crusher`, etc.) —
  skills de copywriting publicitario de respuesta directa, sin relación
  con el stack técnico de APB. **DESCARTADO por decisión de Debora** — no
  se incorpora al catálogo.
- ✅ **`color expert` — RESUELTO (post-Sesión 9):** `meodai/skill.color-expert`
  — ciencia del color (OKLCH/OKLAB, accesibilidad APCA/WCAG, paletas,
  teoría histórica). Único candidato consistente, conectaba con WCAG 2.1
  AA. **DESCARTADO por decisión de Debora** — no se incorpora al catálogo.
- ✅ **`web scrapper` / `unslot` — RESUELTOS (post-Sesión 9):**
  `D4Vinci/Scrapling` (framework de scraping) y `unslothai/unsloth`
  (~67.2k★, fine-tuning de LLMs locales — confirma que "unslot" era error
  de transcripción de "unsloth"). La skill de scraping del agregador
  `sickn33/antigravity-awesome-skills` (~32k★ del repo contenedor, ya en el
  catálogo APB) también se evaluó y queda descartada como incorporación
  puntual. **DESCARTADOS por decisión de Debora** — ninguno se incorpora
  al catálogo.
- **Cerrados sin identificación (decisión Debora, post-Sesión 9):**
  `pintarlos` y `brand guidelines` se descartan. A diferencia de los 6
  términos anteriores, estos dos **nunca llegaron a identificarse** como
  un repositorio concreto — no se evaluaron y se rechazaron, se cierran
  directamente sin resolución. Si en el futuro Debora recuerda a qué
  repo se refería, no es una reapertura de este punto sino una entrada
  nueva con su propia URL.
- `heygen-com/hyperframes` — sin evaluar, naturaleza a determinar (parece
  herramienta de vídeo/presentación, no típica de desarrollo — verificar
  relevancia real para APB)
- `mcpbuilder` de Anthropic — ya incorporado
  (`third-anthropic-mcp-builder-v1.0`, Sesión 8) — confirmar alcance pedido
- `frontend design` de Anthropic — ya incorporado parcialmente
  (`third-skills-sh-frontend-v1.0` vía skills.sh, Sesión 7/8); verificar si
  Debora se refiere a la misma fuente o a otra variante
- `graphify` — ya incorporado (`third-graphify-visual-v1.0`, Sesión 8)
- `unslot` — sin evaluar, nombre a confirmar (posible error de transcripción
  de "unsloth"? requiere aclaración de Debora)
- `pintarlos`, `impecable`, `caveman` — sin evaluar, nombres no
  identificados como repos conocidos — **requiere que Debora aporte
  URL/organización exacta**, no se puede buscar con garantías solo con el
  nombre
- `kim barret` — sin evaluar, posible referencia a una persona/autora de
  skills — **requiere URL o nombre de repositorio exacto**
- `brand guidelines`, `color expert` — sin evaluar, posible relación con
  Sesión Frontend (guía de estilo APB) más que con Sesión 9 de terceros —
  **requiere URL/fuente exacta**
- `pm skills` — posible solape con el dominio `pm` ya existente en el
  framework (creado en Sesión 1.5) — verificar si Debora se refiere a un
  repo de terceros concreto o al dominio propio
- `matt pocock` — ya incorporado parcialmente
  (`third-mattpocock-grill-prd-issues-v1.0`,
  `third-mattpocock-codebase-architecture-analysis-v1.0`, Sesión 7/8) —
  verificar si Debora pide revisar el resto del monorepo (~21 skills, solo
  2 cubiertas hasta ahora)
- `web scrapper` — sin evaluar, fuente/repo concreto no especificado —
  **requiere URL exacta**

> **Acción inmediata sin esperar a sesión propia:** para los puntos sin URL
> exacta (`pintarlos`, `impecable`, `caveman`, `kim barret`, `brand
> guidelines`, `color expert`, `web scrapper`, `unslot`), Claude no puede
> buscarlos con garantías de precisión por nombre solo — riesgo real de
> identificar el repo equivocado. **Debora debe aportar URL o organización
> de GitHub exacta** en la sesión donde se aborden, igual que se hizo con
> el resto de §8.

### 28. Arquitectura de comunicación entre agentes (pregunta conceptual, no construcción)

Debora pide explicación de cómo se enlazan los agentes entre sí y cómo
comparten información. **Esto es una pregunta a responder con el estado
real del framework, no una construcción nueva** — candidata a responder
en la misma Sesión 9 (o inmediatamente después) revisando `SYSTEM.md`,
`GOVERNANCE.md` y el campo `depends_on`/`consumed_by` de `SCHEMA.md`, en
vez de aparcarla a una sesión futura. Ver respuesta directa al final de
este mensaje.

### 29. Loop engineering — análisis de aplicabilidad

Relacionado con el punto #12 ya existente en este documento (mecanismos de
iteración) y con el punto #24 (Goal-Driven Execution de
andrej-karpathy-skills). Debora pide evaluar explícitamente si el
framework debe incorporar mecanismos de "loop engineering" (iteración
automática hasta criterio de éxito verificable). **No crear contenido
nuevo sin análisis previo** — candidata natural: Sesión 13, donde ya están
los puntos #12 y #24 relacionados. Se recomienda resolver los tres puntos
(#12, #24, #29) en la misma sesión por ser la misma decisión de fondo.

### 30. Integraciones de plataforma Microsoft

Integrar agentes del framework con:
- Microsoft Teams
- Envío de correo (mail)
- SharePoint
- Microsoft Copilot (también preguntado como pregunta de compatibilidad,
  ver punto #34)

Requiere decisión arquitectónica previa: ¿se construye como `provider`
nuevo por servicio (`prov-teams-v1.0`, `prov-sharepoint-v1.0`,
`prov-mail-v1.0`), siguiendo el patrón ya usado para otros providers
(`provider_type: action`, `access_mode`), o como capa de adaptador
(`adapters/`)? Candidata: sesión propia de integraciones, o ampliación de
Sesión 10 (meta-gobernanza) si se decide tratarlo como extensión de
plataforma transversal. **Pendiente de alcance con Debora**: ¿qué casos de
uso concretos? (¿notificación de aprobaciones humanas vía Teams/mail?
¿lectura de documentos desde SharePoint como input de skills?).

### 31. Skill de conversión universal a Markdown — ✅ EJECUTADO

> `apb-plat-doc-to-markdown-v1.0` creada (dominio `platform`): normaliza
> cualquier adjunto ofimático/PDF a Markdown antes de ser consumido por los
> componentes. Detalle en [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).

### 32. Mecanismo automático de actualización de inventario/documentación

Debora pide un mecanismo **automático** que garantice que inventario,
`INDEX.md`, `about`/`README`, y cualquier archivo del repo con referencias
cruzadas, además de la documentación funcional, se mantienen actualizados
sin intervención manual. **Esto ya existe parcialmente**:
`scripts/generate_catalog.py` regenera `CATALOG.md`/`INDEX.md`/
`DOMAIN_REGISTRY.md`, y el CI (`validate.yml`) bloquea PRs si hay drift
(Sesión 6, decisión explícita de Debora: sin auto-commit). **Lo que falta**
y debe analizarse: ¿"documentación funcional" se refiere a algo más amplio
que el catálogo técnico (ej. los documentos Word de Sesión 14, o
descripciones funcionales de negocio)? Si es así, requiere mecanismo nuevo
distinto del validador actual. Sesión candidata: ampliación de Sesión 10 o
de Sesión 14, según se aclare el alcance exacto de "documentación
funcional" con Debora.

### 33. Skills/agentes de SQL

Petición de skill/agente/subagente para: generar queries SQL, revisarlas,
optimizarlas, detectar errores, revisar PRs de SQL, documentar PRs de SQL.
Sin componente equivalente detectado hasta ahora en el framework (dominio
`development` tiene skills genéricas de revisión de código, no
específicas de SQL/Azure SQL). Candidata: dominio `development`, sesión a
determinar — posible ampliación de Sesión 11 (que ya cubre Sonar/calidad de
código) o sesión propia si el volumen de sub-tareas SQL lo justifica.

### 34. Validación QA en flujos de despliegue (incluyendo Markdown)

Los flujos de despliegue (CI/CD vía Jenkins + GitHub Actions, estándar
APB) deben validar cumplimiento de QA antes de desplegar, **incluyendo
despliegues de contenido Markdown** (no solo código). Relacionado con el
CI ya existente (`validate.yml`, Sesión 6) pero ese CI valida el propio
repositorio del framework, no los despliegues de las aplicaciones que el
framework ayuda a construir — **aclarar con Debora** si se refiere a (a)
extender la validación QA del framework a más artefactos, o (b) un
principio para los pipelines de las aplicaciones APB en general (fuera del
propio framework). Sesión candidata: Sesión 11 o Sesión QA, según se
aclare el alcance.

### 35. Documento de uso del framework: Claude web/cliente Windows + compatibilidad Copilot/Rovo

Debora pide:
(a) explicación + documento de cómo usar este framework desde Claude (web
o cliente Windows)
(b) si el framework puede usarse desde Microsoft Copilot o Rovo de
Atlassian, y en caso afirmativo, cómo

**Esto solapa directamente con el punto #2 ya existente** ("Guía de uso de
agentes", asignado a Sesión 13) y con `proyecto.md` §7 ("Guía de uso de
herramientas (Rovo, Copilot, etc.)" ya listada como entregable clave). No
es contenido nuevo de alcance, sino una **priorización**: Debora lo pide
ahora, no en Sesión 13. Requiere decisión: ¿adelantamos este documento a
sesión propia antes de la 13, o se mantiene en el plan original? Nota
técnica importante a verificar antes de prometer nada: el framework está
diseñado primariamente para **Claude y GitHub Copilot** (`runtime: list de
["copilot", "claude"]` en `SCHEMA.md` §3.2); su uso desde Microsoft Copilot
o Rovo dependería de si esas plataformas soportan consumo de
agentes/skills en formato Markdown+YAML estándar de Anthropic Skills o
equivalente — **no confirmado, requiere investigación dedicada antes de
responder con certeza**.

### 36. Agentes de licitación (pendiente de detalle)

Debora anuncia que necesitará 1-2 agentes para crear y revisar
documentación relacionada con una licitación (procedimiento de
contratación pública LCSP), **pero aún no ha dado los detalles**. No se
puede definir alcance, dominio, ni sesión hasta recibir esa información.
Marcado como **pendiente de briefing**, sin sesión asignada todavía.

### 37. Agente de documentación funcional/spec desde histórico (app existente)

Agente que, a partir de documentación existente + histórico de tickets
Jira de una aplicación ya en producción, genere documentación funcional y
especificaciones (spec) de esa aplicación. **Solape parcial detectado**
con `apb-agent-documentation-v1.0` (genera ADRs, Swagger/OpenAPI, manuales)
y `apb-agent-spec-engineer-v1.0` (genera specs, pero parte del output de un
Business Analyst humano, no de reconstrucción desde histórico). Ninguno de
los dos parte de "Jira histórico + docs existentes" como fuente primaria
de reconstrucción retroactiva — éste sería un caso de uso distinto
(reconstrucción/discovery inverso, no especificación hacia delante).
Candidata: nuevo agente o subagente de `apb-agent-spec-engineer-v1.0`,
dominio `discovery` o `pm`. Sesión a determinar.

### 38bis. Unificación confirmada con punto #11 (decisión Debora, post-Sesión 9)

**Decisión de Debora:** el punto #11 ("inventario global de dominios de
negocio APB") y el punto #38 Fase 0 ("catálogo corporativo de dominios" a
partir del listado de APIs que aportará Debora) **son el mismo artefacto**.
No se construyen por separado. Cuando se aborde la sesión de #38 (Fase 0),
se considera resuelto también el punto #11 — no requiere sesión propia
adicional en el bloque de Sesión 13. Actualizar la tabla de mapeo: #11 deja
de estar asignado a Sesión 13 en solitario y pasa a resolverse junto con
#38 Fase 0.

### 38. Agente de descomposición de monolitos a microservicios (DDD + eventos)

Agente que analice un monolito existente y proponga:
- Descomposición en microservicios orientados a dominios (DDD)
- Diseño orientado a eventos, alineado con el **catálogo corporativo de
  dominios**
- Estrategia de migración hacia la arquitectura objetivo
- Creación de tickets Jira
- Documentación funcional y specs asociadas

**Decisión de Debora (Sesión 9, confirmada):** no existe hoy un catálogo
corporativo de dominios en APB. **Debe resolverlo el propio framework de
IA, no asumirse como insumo externo ya disponible.** Mecanismo previsto:
Debora aportará una lista de APIs existentes (sin garantía de que sus
agrupaciones actuales sean dominios correctos) como **borrador de
entrada**; un agente analizará esa lista y propondrá si los dominios
detectados son correctos tal cual, o si conviene unificar o dividir
algunos. Esto reordena el propio agente del punto #38 en dos fases
diferenciadas, no una sola:

1. **Fase 0 — Construcción del catálogo de dominios** (nueva, no estaba
   contemplada originalmente): a partir del listado de APIs que aportará
   Debora, el agente identifica agrupaciones candidatas a dominio/bounded
   context, señala posibles solapamientos, fragmentaciones excesivas, o
   APIs sin dominio claro, y propone una versión depurada del catálogo
   para validación humana (`SYSTEM.md` §6, validación de "Dominios,
   bounded contexts, eventos de negocio" ya exige revisión de
   Arquitecto/Tech Lead — coherente con el framework existente, no
   requiere excepción).
2. **Fase 1 — Descomposición de monolitos** (alcance original del punto
   #38): una vez exista el catálogo de dominios (fruto de la Fase 0, no
   antes), el agente de descomposición lo usa como referencia para
   alinear la propuesta de microservicios/eventos a dominios ya validados,
   en vez de inventar agrupaciones ad-hoc por monolito analizado.

**Implicación de secuenciación:** la Fase 0 debe completarse, al menos en
una primera iteración validada por Arquitectura, antes de que la Fase 1
pueda producir resultados alineados de forma consistente entre distintos
monolitos. Si se analizan varios monolitos sin un catálogo de dominios
común ya estable, cada análisis corre el riesgo de proponer una
taxonomía de dominios distinta e incompatible entre sí.

**Primer input real disponible (2026-06-30):** Azure API Manager en
`https://apipre.portdebarcelona.cat` es la fuente de verdad de las APIs DOCKS
publicadas. Primeras 3 APIs confirmadas: `APB.API.RESPONSIBLE`, `APB.API.ROSS`,
`APB.API.SIG` — función y dominio TBD, pendiente de análisis DDD.
La knowledge base (`APB_KNOWLEDGE_BASE.md §4.4`) ya documenta 42+ APIs ARQ
adicionales — este listado combinado es el punto de partida para Fase 0.
**Restricción explícita de Debora (2026-06-30):** los dominios actuales NO están
bien definidos — el agente de análisis debe proponer la taxonomía correcta, no
asumir que la agrupación actual de la knowledge base es válida. Su misión es
detectar solapamientos, repeticiones, novedades y proponer bounded contexts.

Sigue siendo, en conjunto (Fase 0 + Fase 1), un agente de alcance
considerable que combina: análisis arquitectónico
(`apb-disc-ddd-legacy-v1.0` ya existente como insumo), diseño event-driven
(`apb-arch-event-driven-v1.0`, y las skills de terceros incorporadas en
Sesión 9: `third-sickn33-saga-orchestration-v1.0`,
`third-sickn33-event-store-design-v1.0`,
`third-sickn33-ddd-context-mapping-v1.0` — esta última especialmente
relevante para la Fase 0, dado que cubre exactamente el mapeo de
relaciones entre contextos/dominios), gestión de Jira, y generación de
documentación. Candidato natural a **agente orquestador nuevo** que
consuma varias skills/subagentes existentes en vez de construirse desde
cero. Sesión candidata: sesión propia (volumen alto, ahora mayor por la
Fase 0 añadida) o ampliación de Sesión 13.

### 39. Agente de dashboards/métricas (Power BI, Grafana, Prometheus)

Agente que, a partir de petición en lenguaje natural o de una spec, genere
dashboards y métricas en Power BI, Grafana y Prometheus. Sin componente
equivalente detectado en el framework actual (existe `apb-agent-finops-v1.0`
para costes, pero no para dashboards/observabilidad general). Dominio
candidato: `platform` u `operation`. Sesión a determinar.

### 40. Agente de propuesta y generación de logs para dashboards

Agente complementario al #39: a partir de los dashboards/métricas
definidos, propone qué logs deben incorporarse a las aplicaciones para
alimentarlos, y ayuda a generarlos (instrumentación de logging). Trabajaría
en tándem con el #39. Dominio candidato: `platform` u `operation`, mismo
agente extendido o subagente dedicado — a decidir según volumen real al
construir el #39.

### 41. Análisis: ¿algún agente no debería requerir revisión humana? + orquestación real entre agentes

(Añadido por Debora tras la explicación del punto #28 sobre cómo se
enlazan los agentes hoy.) Dos preguntas relacionadas pero distintas, ambas
pendientes de análisis, no de implementación directa:

1. **¿Hay algún agente candidato a operar sin revisión humana
   obligatoria?** Hoy `SYSTEM.md` §5.1 fija Nivel 1 (revisión humana
   previa obligatoria) como mínimo para análisis, arquitectura, seguridad,
   despliegue y gobierno, y el Nivel por defecto es 1 para todo lo demás.
   Solo "tests automatizados de regresión" puede operar en Nivel 3
   (auditoría periódica, no aprobación previa) si están previamente
   autorizados — y el Nivel 4 nunca se activa sin aprobación explícita de
   Arquitectura y Ciberseguridad. Analizar: ¿qué agentes/skills concretos
   del catálogo actual (217 componentes) son candidatos reales a Nivel 2/3
   sin romper el principio `SYSTEM.md` §2.1 regla 2 ("ningún agente puede
   aprobar sus propios resultados")? Candidatos a evaluar primero: skills
   de solo lectura/diagnóstico (auditoría, detección de drift, generación
   de informes) frente a skills que escriben código o tocan producción.

2. **Mecanismo real de orquestación entre agentes** (más allá del enlace
   declarativo por referencia de ID explicado en el punto #28). Hoy el
   "enlace" es textual (`agents:`, `skills:`, `subagents:` en frontmatter)
   y la información se comparte vía artefactos en Git/Jira entre sesiones
   — no hay paso de mensajes en tiempo real ni un orquestador que encadene
   llamadas automáticamente. Analizar si conviene introducir una capa de
   orquestación real (ej. un `provider` o `adapter` que ejecute la cadena
   `workflow → agent → skill` sin intervención manual entre cada paso,
   dentro de los límites de autonomía ya definidos) y cómo encajaría con
   los `human_checkpoints` obligatorios de cada workflow sin romperlos.

**Relación directa con puntos ya existentes:** este punto es la otra cara
de la moneda del #29 (loop engineering) y del #24 (Goal-Driven Execution) —
los tres tratan, desde ángulos distintos, hasta qué punto el framework
puede/debe reducir la intervención humana sin comprometer
`SYSTEM.md` §2.1. **Recomendación: resolver #24, #28 (ya respondido),
#29 y #41 en la misma sesión** (candidata: Sesión 13), porque son la misma
decisión de fondo vista desde ángulos distintos, y decidirlos por separado
arriesga conclusiones contradictorias entre sí.

---

### 42. Comillas mal cerradas en sección "Dependencias" ✅ **RESUELTO**

> ✅ Corregido (19 archivos, preparación de Sesión 11). Registro completo en
> [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).

---

### 43. Aplicación retroactiva de "Generado por IA" + "Validado por humano" a todo el catálogo

**Decisión de Debora (post-Sesión 11):** la política de identificación explícita —
`SYSTEM.md` §7.2, todo artefacto debe declarar visiblemente que fue generado por IA y qué
humano lo validó — se aplicará a la **totalidad** del catálogo existente (~225 componentes a
fecha de Sesión 11, número crecerá con cada sesión futura), pero como **última fase del
plan**, después de que todas las sesiones de construcción/remediación (8 a 14) hayan
cerrado.

**Razón de la secuenciación:** aplicar esto antes sería trabajo desechable — cada sesión
futura (12, 13, 14, Sesión QA, Sesión Frontend, #38, etc.) sigue creando o modificando
componentes. Aplicar la identificación al final, una sola vez sobre el catálogo ya estable,
evita repetir el trabajo sobre los mismos archivos varias veces.

**Pendiente de definir cuando se aborde esta fase:**
- ¿Quién es "el humano validador" para componentes creados en sesiones donde Debora ya dio
  el OK conversacional (¿se usa su nombre retroactivamente, o queda "pendiente" hasta una
  revisión formal explícita por componente?) — Debora decide el criterio antes de ejecutar.
- Si el propio `apb-agent-meta-builder-v1.0` (Sesión 10) se usa para aplicar esto de forma
  sistemática (candidato natural, ya que su función es generar/mantener componentes
  conforme al esquema), o se hace como tarea de script dedicado.
- Si esta fase también cubre los componentes de terceros (`skills/third_party/`,
  `wrappers/`) o se limita a los `apb-owned`, dado que los de terceros ya tienen su propio
  campo `source_repo`/`source_license` que en cierto modo ya identifica el origen no-APB.

**No bloquea ninguna sesión intermedia** — los componentes que se han creado en Sesiones 10
y 11 (`apb-dev-simplicity-first-v1.0`, `apb-dev-surgical-changes-v1.0`,
`apb-plat-doc-to-markdown-v1.0`, `apb-agent-meta-builder-v1.0`,
`apb-ops-dependency-audit-v1.0`, `apb-ops-perf-bottleneck-v1.0`,
`apb-ops-debt-remediation-plan-v1.0`, `apb-agent-tech-debt-v1.0`) ya tienen el bloque
aplicado individualmente como precedente — la fase #43 es para el resto del catálogo
retroactivamente, de una sola vez.

### 44. Plantilla `context/apb/templates/AGENT.md` desactualizada respecto a `SCHEMA.md`

**Hallazgo detectado durante Sesión 10, nunca registrado formalmente como tarea hasta esta
revisión post-Sesión QA** (Debora detectó que la bitácora y el plan tenían huecos y pidió
verificación exhaustiva). `context/apb/templates/AGENT.md` usa un formato antiguo (metadatos
en blockquote `> **ID:**`) que **ya no es válido** según `SCHEMA.md` §1 — solo YAML
frontmatter es válido para cualquier componente. Los agentes reales del repo (`agents/*.md`)
usan correctamente YAML frontmatter; solo la plantilla de referencia quedó desactualizada,
probablemente de una etapa anterior a la Sesión 0/2 (normalización de frontmatter).

**Riesgo si no se corrige:** cualquier persona o agente que use esa plantilla como base para
crear un agente nuevo (en vez de copiar el formato real observado en `agents/*.md`)
generaría un componente inválido que fallaría el validador. No bloquea nada hoy porque
`apb-agent-meta-builder-v1.0` (Sesión 10) ya fue instruido para seguir el formato real, no la
plantilla — pero la plantilla en sí sigue siendo una trampa para cualquier humano que la use
directamente. **Sesión a determinar** — corrección sencilla (reescribir
`templates/AGENT.md` con YAML frontmatter, replicando la estructura de `templates/SKILL_APB.md`
que sí está correcta), candidata a tarea trivial dentro de cualquier sesión de mantenimiento,
o a resolverse junto con la Sesión 13.

### 45. Carpeta `skills/_spec-driven/` de `apb-ai-skills` — ✅ RESUELTO (Sesión 19, 2026-07-04)

**Cruce ejecutado con datos (fuente: `apb-ai-skills.zip` original, OneDrive
`Proyectos/.../Repo GitHub versiones/`):** las 3 skills (`spec-to-api-contract`,
`spec-to-e2e-flows`, `spec-to-test-plan`) resultaron ser **placeholders
`[RESERVADO - NO ACTIVO]` sin implementación** — solo describen una intención
futura ("se activará cuando el proyecto adopte Open Spec Kit"). **No hay
contenido que fusionar.** Además, lo que prometían ya está cubierto o
superado por el framework actual:
- `spec-to-test-plan` → cubierto por `apb-qa-test-plan-v1.0` v1.4.0, que
  desde Fase I acepta `spec` como fuente funcional autoritativa.
- `spec-to-e2e-flows` → parcialmente cubierto (`apb-qa-test-auto-v1.0`,
  `apb-sub-qa-e2e-v1.0`); **idea aprovechable registrada:** trazabilidad
  automática criterio de aceptación → caso (AC-XXX → TC-XXX) en el nombre
  del test generado.
- `spec-to-api-contract` → `apb-arch-api-contract-v1.0` diseña contratos;
  **idea aprovechable registrada:** generación de tests de contrato (estilo
  Pact) desde la spec, para que la implementación no se desvíe del diseño.
**Recomendación aplicada: cerrar sin fusiones** (coherente con la
deprecación general de `apb-ai-skills`); las 2 ideas quedan anotadas aquí
como mejoras opcionales de futuras versiones de esas skills APB.

<details><summary>Planteamiento original (histórico)</summary>

**Hallazgo de la Sesión QA, documentado como dato pero nunca convertido en tarea con
decisión pendiente** (mismo patrón de hueco que el #44). Al auditar `apb-ai-skills.zip` se
encontró una carpeta `skills/_spec-driven/` con 3 skills (`spec-to-api-contract`,
`spec-to-e2e-flows`, `spec-to-test-plan`) no contabilizadas en la descripción original del
repo ("10 skills APB + 10 externas + agente + 5 subagentes"). Se documentó su existencia en
`CONTINUIDAD_PROYECTO.md` §13.1, pero **nunca se decidió qué hacer con ellas** — a diferencia
de las 10 skills APB, que sí se cruzaron una por una contra el catálogo de
`APB-IA-FRAMEWORK` (resultando en las 4 fusiones de la Sesión QA), estas 3 nunca se evaluaron
individualmente.

**Pregunta pendiente para Debora:** ¿se evalúan estas 3 skills para posible fusión (mismo
tratamiento que las 10 ya cruzadas), o se consideran cubiertas por la decisión general de
deprecar `apb-ai-skills` y no requieren evaluación individual? Sesión a determinar — no
bloquea nada del plan actual, pero queda abierta hasta que Debora decida el criterio.

</details>

---

**Resumen de acción inmediata para Debora:** Punto #27 **cerrado en su
totalidad** (post-Sesión 9). De los 8 términos originales: 6 se
identificaron y se descartaron tras evaluación (`impecable`, `caveman`,
`kim barret`, `color expert`, `web scrapper`, `unslot`); 2 se cierran sin
haber llegado a identificarse (`pintarlos`, `brand guidelines`). Ninguno
se incorpora al catálogo. No queda ninguna acción pendiente sobre este
punto.
- Punto #36 (licitación): **pendiente de briefing** de Debora.
- Punto #38 (Fase 0, catálogo de dominios): **pendiente de que Debora
  aporte el listado de APIs** cuando se vaya a abordar esta sesión —
  confirmado que no existe catálogo corporativo previo; lo construirá el
  propio framework a partir de ese listado.
- Punto #35: decidir si se prioriza sobre el orden original del plan
  (estaba en Sesión 13).

> **Nota de proceso (Sesión 9):** Debora confirmó que las dependencias
> abiertas de cada punto (URLs, briefings, listados) se resolverán en el
> momento de abordar la sesión específica correspondiente, no antes. Este
> resumen se mantiene como recordatorio de qué falta por punto, sin
> bloquear el resto del plan.

---

## Plan de sesiones completo — confirmado por Debora (2026-06-24)

> Decisión: a partir de ahora todo componente nuevo que se cree en cualquier sesión
> sigue el protocolo de `apb-agent-meta-builder-v1.0`: discovery previo en
> `CATALOG.md`/`INDEX.md`, YAML frontmatter conforme a `SCHEMA.md`, ejecución de
> `validate_repo.py --strict` y regeneración de catálogo. Claude Code actúa como
> ejecutor del protocolo.

### Sesiones pendientes en orden de ejecución

| Sesión | Tema principal | Puntos del plan | Bloqueante |
|---|---|---|---|
| ~~**Frontend**~~ | ~~Mockups para perfiles funcionales + generación de frontend para devs~~ | ~~#20, #21~~ | ✅ CERRADA |
| ~~**Design System**~~ | ~~Análisis y construcción del sistema de diseño APB sobre DevExtreme: tokens CSS, componentes compuestos corporativos (cabecera, menú, tarjetas de dominio), guía de estilos integrada. Repo GitHub propio `apb-design-system`.~~ | ~~#22~~ | ✅ CERRADA (2026-06-26, v1.3.0) — repo APB-DESIGN-SYSTEM creado. Skills y agentes de diseño en APB-IA-FRAMEWORK; artefactos CSS/JS en repo propio. |
| ~~**15**~~ | ~~Integraciones Microsoft (Teams, mail, SharePoint) + cierre de gaps de otras plataformas IA: Rovo (Forge App skeleton + guía activación) y M365 Copilot (OpenAPI spec + manifest plugin). Claude web y GitHub Copilot VS Code ya funcionan hoy sin desarrollo adicional.~~ | ~~#30, #35, #47~~ | ✅ CERRADA (2026-06-26) — artefactos generados: `openapi/apb-framework-api.yaml`, `openapi/ai-plugin.json`, `forge/manifest.yml` + `forge/src/`, `docs/rovo-getting-started.md`. Pendiente de equipo APB (Plataforma + Desarrollo + Admins): ver `discovery/HANDOFF_TECNICOS.md §4` *(corregido 2026-07-06: el fichero `docs/HANDOFF_SESION15_INTEGRACIONES.md` citado aquí originalmente nunca llegó a crearse — su contenido real vive en `HANDOFF_TECNICOS.md §4`)*. |
| ~~**16**~~ | ~~Informe de análisis de riesgos organizativo (ENS alto, políticas APB, deuda técnica, excepciones) para validación Ciberseguridad/Arquitectura~~ | ~~#16 (alcance completo, no el parcial de Sesión 12)~~ | ✅ CERRADA (2026-06-24) — `apb-gov-org-risk-report-v1.0` (v1.2.0) alineado con `PROCEDURE_NONCOMPLIANCE_MANAGEMENT_v1.0` + `PROCEDURE_RISK_EVALUATION`. Análisis multidimensional (ENS, ISO 27001, NIST, OWASP, RGPD, LCSP, WCAG), recomendación explícita APROBAR/DENEGAR/ESCALAR, plan de mitigación, plantilla de informe con firmas. |
| ~~**17**~~ | ~~Observabilidad: dashboards Power BI/Grafana/Prometheus + logging + telemetría de KPIs del framework~~ | ~~#26, #39, #40~~ | ✅ CERRADA — ver punto #46 para pendiente de telemetría en chat |
| **13** | Cierre de pendientes históricos: guía de uso de agentes, plantillas, mapa Jira, COSMIC, loops, autonomía de agentes, plantilla AGENT.md | #2, #6, #7, #8, #12, #29, #41, #44, #48 | ✅ PARCIAL (2026-06-26, 7/10 puntos): #2 ✅ #7 ✅ #12 ✅ #29 ✅ #41 ✅ #44 ✅ #48 ✅. Bloqueados: #6 (ejemplos Word/Excel de Debora), #8 (horas históricas COSMIC), #52 (email Arquitectura). |
| ~~**18**~~ | ~~DDD: catálogo corporativo de dominios (Fase 0) + descomposición de monolitos (Fase 1) + spec desde histórico Jira~~ | ~~#11/#38 Fase 0, #38 Fase 1, #37~~ | ✅ CERRADA (Sesión 18, 2026-06-25) — repo apb-domain-catalog creado (github.com/apb-dmartin/APB-DOMAIN-CATALOG), apb-agent-ddd-v1.0 + 5 subagentes (code/db/doc/spec/interview), submodule integrado en APB-IA-FRAMEWORK. Fase 1 (descomposición monolitos) → pendiente sesión futura. |
| **19** | Terceros pendientes de §8 + evaluación `_spec-driven` de `apb-ai-skills` | #27 (items abiertos), #45 | ✅ **CERRADA (2026-07-04, Sesión 19)** — #45: las 3 skills `_spec-driven` resultaron ser placeholders `[RESERVADO - NO ACTIVO]` sin implementar (verificado en el zip original); nada que fusionar, lo prometido ya lo cubre `apb-qa-test-plan-v1.0` v1.4.0 (input `spec`, Fase I). 2 ideas registradas como mejora futura: trazabilidad AC-XXX→TC-XXX automática y tests de contrato tipo Pact desde plan.md. #27 items: evaluados (ver tabla F). Detalle en [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md). |
| **20** | Agentes de licitación (LCSP) | #36 | **Pendiente de briefing de Debora** |
| **14** | Documentación Word por audiencias (arquitectos, devs/analistas, dirección) + mecanismo de actualización de documentación funcional | #23, #32 | ⚠️ PARCIAL (2026-06-27): borradores Markdown disponibles (`docs/guia-funcional.md` y `docs/manual-arquitectura.md`). Pendiente: conversión a .docx + documento de Dirección |
| ~~**#43**~~ | ~~Aplicación retroactiva "Generado por IA + Validado por humano" a todo el catálogo~~ | ~~#43~~ | ✅ CERRADA (Sesión 23, 2026-06-26) — 129/129 skills apb-owned marcadas con `## Marcado IA obligatorio (POLICY_AI_USAGE §6)`. Estándar canónico: `context/apb/standards/AI_MARKING_STANDARD.md`. Mecanismos preventivos: check #13 en `validate_repo.py` (ERROR si falta la sección), sección en templates `SKILL_APB.md` y `AGENT.md`, `CLAUDE.md` en raíz del repo. |

| ~~**21**~~ | ~~SQL + soporte de primera línea de incidencias técnicas + QA del propio framework~~ | ~~#15, #33, #34, #50~~ | ✅ CERRADA (2026-06-29, Enriquecimiento D) — `apb-agent-db-v1.0` creado (skills sql-gen/review/fix + subagente sql), `apb-dev-sql-review-v1.0` añadido a implementer. M1-M6 del backlog resueltos: 2 skills orchestration + skill WCAG + agente PM + diferenciación STRIDE/ISO27005 + verificación UTF-8. Total: 5 nuevos componentes + 14 modificaciones. |
| ~~**22 (#47bis)**~~ | ~~Refactorización de taxonomía de carpetas skills/ — consolidar 13 carpetas de un solo archivo en dominios correctos~~ | ~~#47bis~~ | ✅ CERRADA (2026-06-26) — 13 carpetas consolidadas, archivos movidos a dominios correctos, nomenclatura auditada (259 componentes verificados), 1 violación corregida (`apb-skill-` → `apb-design-`), 12 terceros reorganizados en subcarpetas por autor. |
| **22 (#49)** | Propagación automática Design System (decisión distribución: npm / Git submodule / CDN) | #49 | **Requiere decisión de Debora sobre mecanismo de distribución** |
| ~~**Sesión 18 cont. (#54)**~~ | ~~Entrevista portuaria + verificación de dominio + actualización repo dominios~~ | ~~#54~~ | ✅ CERRADA (2026-06-26) — `apb-sub-ddd-interview-v1.0` v1.3.0: (A) Banco A portuario (buques, escalas, consignatario, GISPEM, PORTIC…); (B) Banco B corporativo (RRHH, viajes, contratación LCSP, adm. electrónica, finanzas, jurídico); (C) Fase 1-INT integración entre sistemas (flujo de datos, trigger, frecuencia, fallo, patrón ACL/Published Language/Shared Kernel/event-driven); (D) Fase 1-EVO evolutivos (revisión de lo existente, clasifica en extensión/nuevo BC/deuda técnica/breaking change); Fase 5 verificación APB-DOMAIN-CATALOG; Fase 6 generación artefacto `domain.md`. |
| ~~**Harness**~~ | ~~Harness Engineering agnóstico de LLM: 5 subsistemas, System of Record + ACID, Feature Lists + Pass-State Gating, validación 3 capas, Clean State Handoff. Gobernanza + scaffolding + checks nuevos en `validate_repo.py`~~ | ~~#83~~ | ✅ CERRADA (2026-07-02, sesión combinada con #78) — SYSTEM.md §10 + GOVERNANCE.md §8 + `repo-scaffold/harness-ready/` + check #19 |
| ~~**Estándar Prompting**~~ | ~~Estándar de estructura de prompt para todos los componentes (razonar→plan→ejecutar, objetivo, autocrítica, qué-NO-hacer, ejemplo E/S, separación SISTEMA/USUARIO) + retrofit + check en validador~~ | ~~#78~~ | ✅ CERRADA (2026-07-02, sesión combinada con #83) — `PROMPTING_STANDARD.md` + 6 plantillas + retrofit 244 componentes + check #18 en ERROR |
| ~~**QA-2**~~ | ~~Metodología y plantilla de planes de pruebas + navegación agéntica para pruebas funcionales~~ | ~~#82, #84~~ | ✅ CERRADA (2026-07-02) — `TEST_PLAN_STANDARD` + plantilla `TEST_PLAN.md`, skill `apb-qa-test-plan` v1.2.0 (interactiva, procedencia múltiple, degradación de fuentes, ingesta de planes aportados), ejemplo unificado TruckCenter (112 casos sin duplicar), `prov-browser-agent-v1.0` + `apb-qa-exploratory-nav-v1.0` (#84), ejecución real sobre TruckCenter PRE con evidencias, check #20. Detalle en [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md). |
| **QA-3** | Ejecución funcional COMPLETA de TruckCenter (y patrón para otras apps): **datos de prueba sembrados y anonimizados** (RGPD) + acceso de escritura para flujos de alta/baja/modificación + 2ª pasada **USER_READ** + **rendimiento (k6)** + **seguridad (SonarQube/OWASP ZAP)** + **evidencia visual PNG/traza/vídeo con Playwright** (escribe ficheros reales) + **unitarias** (repo `APB.TRU` + xUnit) + **despliegue real del entorno Azure QA** (`prov-azure-qa-runtime-v1.0`, diseñado en `draft` en Fase I: nombrar suscripción/entorno + autorizar aprovisionamiento del job efímero con Playwright+k6 + Managed Identity → AKV) + **bucle fallo→PR→Jira real** (`apb-sub-qa-fix-loop-v1.0`, cableado en Fase I). | #82/#84 (ejecución) | **Bloqueantes detectados en QA-2 E-bis (2026-07-02):** F3 PRE sin datos; F2 formulario de Alta no carga (>45s); requiere dataset + autorización de carga/escaneo. **Fase I (2026-07-03) dejó diseñados en `draft`** el provider Azure QA y el subagente fix-loop; QA-3 los **despliega/ejecuta**. ⚠️ **PARCIAL (2026-07-03, dos sesiones):** sesión I ejecutó 44/120 casos con escritura real (B02-B07 + E2E T112), 2 hallazgos críticos (H1/H2). **Sesión II (misma fecha, sin reabrir Claude Code → Playwright MCP no disponible, se usó GIF de `claude-in-chrome` en su lugar)** ejecutó 11 casos netos adicionales + reconfirmó H1/H2/H4 en vivo, con 3 hallazgos nuevos (H5 empresa rechaza NIF manual, H6 Nombre Conductor="." por mapeo WS Sòstrat, H7 Swagger `/trc/` titulado "APB.API.TRU"). **Total acumulado: 55/120 casos con algún estado registrado, 65 siguen `Pendiente` sin tocar** (ver checklist §9 y §16 de `QA_TRU_TruckCenter_UNIFICADO.md` v1.6). → **punto #88** sigue abierto para el resto: reabrir sesión con Playwright MCP cargado desde el inicio, segundo usuario/rol, corrección de H1/H5, y los ~26 casos estructuralmente fuera de alcance de navegador (B01/B11/B13/B14). Ver `PLAN_FASES_COMPLETADAS.md` (QA-2 + Fase I + Sesión QA TruckCenter) y punto #77 (segunda recurrencia del riesgo de runtime, misma fecha). |
| **19 (ampliada)** | Terceros #79 (MCP Builder alcance, cybersecurity skills, "Fine Skills") + Obsidian como capa de navegación | #79, #81 | ✅ **CERRADA (2026-07-04, Sesión 19)** salvo un único pendiente: **"Fine Skills" sigue requiriendo URL de Débora**. #79: "Anthropic cybersecurity skills" resultó ser `mukul975/Anthropic-Cybersecurity-Skills` (NO es de Anthropic; fuente ya incorporada con 5 skills curadas); el oficial real es `anthropics/defending-code-reference-harness` (Apache 2.0, 6 skills) — **✅ incorporado el mismo día con OK de Débora** como `third-anthropic-defending-code-v1.0` (`draft`, 5 skills de análisis, harness gVisor excluido). MCP Builder: alcance confirmado, cubre Teams/SharePoint vía `custom-api`, sin re-incorporar. #81 Obsidian: evaluado y documentado en M.6 como herramienta de apoyo. Detalle en [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md). |
| **Memoria/Runtime** | Memoria corporativa del framework (contexto/histórico/aprendizaje/persistencia): arquitectura Git+`PROGRESS.md` base + LightRAG/mem0 semántica | #80 | Ligada a decisión de runtime (misma que #77) |

> **Sesión Auditoría + Cobertura de Huecos ✅ EJECUTADA (2026-07-04)** → registro movido a
> [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md). Resumen: auditoría de desfase plan↔repo
> (`AUDITORIA_DESFASE_PLAN_REPO.md`; el desfase es de **madurez**, no de existencia — 313/359 draft,
> 0 apb-owned approved, 0 DRIFT-repo) + 5 componentes nuevos que cubren huecos #15/#33/#34/#39-40 +
> check #26 anti-desfase. Pendiente derivado: **avanzar draft→approved** (ciclo de gobernanza) y
> activación MCP Graph #30 (creds/tenant M365, Plataforma).
>
> **Sesión de seguimiento ✅ EJECUTADA (2026-07-04, misma fecha)** — 3 tareas accionables elegidas
> por Débora → registro movido a [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).
> Resumen: #85(K)(a)/(d) ejecutado en `APB-DOMAIN-CATALOG` (HTML de consulta + 1er CI de
> gobernanza del repo + catálogo de referencia); 2/10 SHAs `unverified` de terceros
> re-identificados con evidencia real (8 documentados como no resolubles hoy); corregida
> contradicción interna sobre Understand-Anything (L30 vs. detalle #14); **push confirmado y
> ejecutado en ambos repos**. Además, **#30 MCP Graph completado en la parte no bloqueada**:
> `@softeria/ms-365-mcp-server` cableado en `.mcp.json` (device-code, sin credenciales, aprobado
> explícitamente por Débora tras bloqueo de seguridad del clasificador de auto-mode por ser un
> paquete de terceros no vetado previamente). Solo queda pendiente de Plataforma la app
> registration Entra ID para el flujo headless/producción.

### Decisiones tomadas sobre puntos pendientes (2026-06-24)

- **#34 (validación QA en despliegues):** aplica a todo — framework y aplicaciones APB. De momento, durante la fase de construcción del framework, no se aplica al propio repo; se diseña de forma que pueda activarse también sobre él en el futuro. Se incluye en Sesión 21 junto con #15 y #33.
- **#15 y #33:** sesión propia (Sesión 21), no absorbidos en Sesión 13.
- **#47 (gaps plataformas IA) y #47bis (taxonomía carpetas):** añadidos post-Sesión 17 (2026-06-25) — ver detalle abajo. Asignados a Sesiones 15 y 22 respectivamente.
- **#48 (plantillas de arq + DevExpress):** asignado a Sesión 13 junto con #44.
- **#50 (QA del propio framework):** asignado a Sesión 21 junto con #15, #33, #34.
- **#52 (cambio contacto Arq → mail Jira):** tarea de mantenimiento en Sesión 13, pendiente de que Debora facilite la dirección.

---

### 46. Telemetría automática para usuarios de chat sin commit (pendiente Sesión 17)

**Detectado durante Sesión 17 como gap no resoluble en el alcance de la sesión.**

Los usuarios funcionales que solo interactúan por chat (Claude.ai, GitHub Copilot chat) y nunca hacen commit no están cubiertos por ninguno de los tres mecanismos de telemetría construidos en Sesión 17:
- Mecanismo 1 (Claude Code automático): solo aplica si el runtime es Claude Code.
- Mecanismo 2 (script manual): requiere terminal, inaplicable para usuarios funcionales.
- Mecanismo 3 (GitHub Actions / JSONL): requiere que alguien commitee al repo.

**La cobertura automática para este perfil requiere instrumentar la plataforma de chat**, lo cual está fuera del alcance del framework de Markdown.

**Opciones a evaluar en sesión futura:**
- Proxy de invocación (Azure API Management delante del endpoint de Claude/Copilot) que capture la llamada y emita telemetría antes de pasarla al LLM.
- Wrapper de interfaz que envuelva la sesión de chat y registre eventos de uso.
- Aceptar cobertura parcial y documentarlo en el informe ejecutivo de KPIs.

**Sesión a determinar.** No bloquea ninguna sesión del plan actual — la telemetría de desarrolladores con Claude Code ya es funcional y cubre el caso de uso principal.

---

### 47. Cierre de gaps de uso desde otras plataformas IA (Sesión 15)

**Detectado durante Sesión 17 al anticipar respuesta para pruebas de Debora (2026-06-25).**

El framework tiene adapters para cuatro runtimes, pero con distinto grado de completitud:

| Plataforma | Estado hoy | Gap |
|---|---|---|
| Claude (web / Claude Code) | ✅ Usable hoy | Ninguno — adjuntar .md al chat o usar Claude Code directamente |
| GitHub Copilot (VS Code) | ✅ Usable hoy | `#file:agents/xxx.md` en el chat de Copilot |
| Rovo (Atlassian) | ⚠️ Adapter definido, no desplegable | Falta: Forge App skeleton (manifest + estructura) + `docs/rovo-getting-started.md` |
| M365 Copilot (Teams/Word/Outlook) | ⚠️ Adapter definido, no desplegable | Falta: OpenAPI 3.0 spec de los endpoints APB + manifest `ai-plugin.json` |

**Trabajo concreto para Sesión 15:**

**Rovo:**
- Generar el esqueleto de la Forge App (`forge/manifest.yml` + estructura de carpetas) lista para que el equipo de desarrollo la complete y publique en el tenant Atlassian APB.
- Crear `docs/rovo-getting-started.md` con guía de activación paso a paso.
- Prerrequisito operativo (no de framework): tenant Atlassian con Rovo activado (previsto julio 2026).

**M365 Copilot:**
- Generar la especificación OpenAPI 3.0 (`openapi/apb-framework-api.yaml`) de los endpoints que M365 Copilot consumiría como API Plugin.
- Generar el manifest del plugin (`openapi/ai-plugin.json`).
- Nota explícita: el backend que sirve esos endpoints (Azure APIM o Azure Function) es infraestructura de plataforma, no competencia del framework — el framework entrega la spec, no el backend desplegado.

**Lo que NO se construye en Sesión 15:** backends reales (Forge App desplegada, Azure APIM aprovisionado) — eso es trabajo de plataforma APB.

---

### 47bis. Refactorización de taxonomía de carpetas de skills (Sesión 22)

**Detectado durante Sesión 17 al revisar escalabilidad hacia IT-general y negocio (2026-06-25).**

**Problema actual:** `skills/apb-owned/` mezcla dominios funcionales (`development`, `qa`, `security`) con categorías de capacidad (`api-design`, `code-review`, `event-driven`) y tiene duplicidades aparentes (`architecture` + `architecture-design`, `docs` + `documentation`, `design` + `design-approval`). Con 114 skills APB y crecimiento previsto hacia IT-general y negocio, la inconsistencia escala mal.

**Opción elegida (Debora, 2026-06-25): Opción C — limpiar taxonomía primero, escalar después.**

**Trabajo concreto para Sesión 22:**

1. **Auditoría completa** de las ~114 skills APB: mapear cada carpeta actual a un dominio canónico propuesto.
2. **Propuesta de taxonomía** (8-10 dominios canónicos con criterio claro) — presentar a Debora antes de mover nada. Checkpoint humano obligatorio en este punto.
3. **Ejecución tras aprobación:** mover archivos, actualizar referencias cruzadas en frontmatter (`depends_on`, `consumed_by`, `skills`, `subagents`), actualizar el validador si detecta rutas hardcodeadas.
4. **Validación final:** `validate_repo.py --strict` en verde, 0 drift, 19/19 tests OK.

**Criterio de diseño para la taxonomía:** los dominios deben ser lo suficientemente amplios para absorber skills de IT-general y negocio futuras sin necesidad de restructurar de nuevo. Si el volumen de skills no-dev supera ~30 en algún momento, se evalúa añadir un nivel de área (`software/`, `it-operations/`, `business/`) encima — no antes.

**Bloqueante:** ninguno. Puede ejecutarse en cualquier momento sin depender de insumos externos.

---

## Bloque añadido post-Sesión 18 (2026-06-25)

### 48. Usar plantillas de arquitectura APB como base de nuevos componentes

Las plantillas oficiales de Arquitectura APB (actualmente en `context/apb/templates/`) deben ser el punto de partida de cualquier componente nuevo que se cree en el framework. Relacionado con el punto #44 (plantilla `AGENT.md` desactualizada): la corrección de #44 debe alinear **todas** las plantillas con el formato real de `SCHEMA.md`, incluyendo la referencia a DevExpress como stack frontend estándar APB, que ya figura en las plantillas actuales.

**Acción concreta:** verificar en Sesión 13 (junto con #44) que todas las plantillas (`SKILL_APB.md`, `AGENT.md`, `SUBAGENT.md`, `WORKFLOW.md`, `PROVIDER.md`) incluyen la referencia a DevExtreme/DevExpress como herramienta corporativa estándar en los campos relevantes (p. ej. `tools`, `context`), de forma que cualquier nuevo componente creado desde plantilla ya la tenga referenciada por defecto.

**Sesión asignada:** Sesión 13 (junto con #44).

---

### 49. Sistema de diseño como repo central instanciable por apps APB

El repo `APB-DESIGN-SYSTEM` (creado en Sesión Design System) debe configurarse como **dependencia centralizada** que las aplicaciones APB instancian directamente (npm package, git submodule, o similar), en lugar de que cada proyecto copie los artefactos CSS/JS manualmente. El objetivo es que un cambio en el Design System se propague automáticamente a todas las apps que lo consumen sin intervención manual por proyecto.

**Decisiones pendientes para la sesión que aborde esto:**
- Mecanismo de distribución: npm package privado (Azure Artifacts), git submodule versionado, o CDN corporativo APB.
- Política de versiones semánticas: cuándo un cambio es breaking (major) vs. compatible (minor/patch).
- CI del Design System: añadir job que publique la nueva versión al mecanismo elegido al hacer merge a main.
- Qué apps APB existen ya y cuál es la primera candidata a pilotar la integración.

**Sesión asignada:** pendiente — candidata natural: ampliación de la sesión de Design System o Sesión 22 (refactorización de taxonomía), dado que implica decisiones de infraestructura de distribución. Requiere confirmación de Debora sobre el mecanismo preferido.

---

### 50. Pruebas y QA del propio framework

El framework construye skills y agentes para probar aplicaciones APB, pero no tiene una suite de pruebas propia que valide su propio comportamiento. Gap identificado: las GitHub Actions actuales (`validate.yml`, `telemetry.yml`) validan estructura/sintaxis y drift, pero no comportamiento funcional — no verifican que un agente dado produzca el output esperado para un input conocido.

**Trabajo a definir:**
- Batería de pruebas de integración para los scripts del framework (`validate_repo.py`, `generate_catalog.py`, `emit_telemetry.py`).
- Tests de comportamiento de agentes: given a prompt + skill.md, assert that the agent's response meets defined criteria (formato, campos obligatorios, restricciones de autonomía).
- Considerar si usar el propio `apb-qa-unit-test-gen-v1.0` (fusionado en Sesión QA) para generar estos tests — aplicar el framework a sí mismo.

**Sesión asignada:** pendiente — candidata natural: Sesión 21 (SQL + incidencias técnicas ya incluye #34 de validación QA en despliegues; añadir aquí el QA del propio repo sería coherente). Confirmar con Debora si se prefiere sesión propia.

---

### 51. Prueba real de todos los agentes del catálogo

Más allá de la validación estructural (`validate_repo.py --strict`), verificar que **todos los agentes activos del catálogo funcionan correctamente** cuando se invocan desde Claude con un caso de uso real. Hoy se crean componentes y se valida su sintaxis, pero no hay evidencia registrada de que cada agente haya sido ejercitado con un prompt real y producido output útil.

**Alcance:**
- Para cada agente en `agents/` y `subagents/`: documentar al menos un caso de prueba real (input → output observado → ¿cumple criterios del `purpose` declarado en el frontmatter?).
- Marcar explícitamente los agentes que no se han podido probar por falta de datos/entorno (ej. agentes que requieren Jira real, Rovo activo, o tenant Azure específico).
- Este trabajo alimenta directamente el punto #43 (política "Generado por IA + Validado por humano"): la validación real es la que convierte el campo `human_validated_by` de vacío a un nombre real.

**Sesión asignada:** pendiente — candidata: post-Sesión 13 o como sub-fase de #43 (última fase del plan), ya que tiene sentido probar antes de marcar como validado.

---

### 52. Cambiar contacto de Arquitectura por mail de Jira en toda la documentación

Las referencias a un contacto de arquitectura personal deben sustituirse por la dirección de correo/cola de Jira oficial del equipo de Arquitectura APB, para que las notificaciones y aprobaciones lleguen al canal correcto independientemente de quién esté disponible.

**Acción concreta:** buscar en todo el repo (skills, agentes, documentos, configuración) cualquier mención a un correo personal o nombre directo de contacto de Arquitectura y reemplazarlo por el mail de Jira / cola de equipo que Debora indique.

**Pendiente:** Debora debe facilitar la dirección de Jira / mail del equipo de Arquitectura APB antes de ejecutar este cambio.

**Sesión asignada:** tarea de mantenimiento, sin sesión propia — ejecutar en la primera sesión disponible una vez Debora aporte la dirección. Candidata: Sesión 13 (cierre de pendientes históricos).

---

### 53. Mockup de validación: agente de diseño + verificación de uso del Design System

Una vez el agente `apb-agent-ux-mockup-v1.0` (creado en Sesión Frontend) y el repo `APB-DESIGN-SYSTEM` estén ambos operativos, realizar una prueba de extremo a extremo:

1. Invocar `apb-agent-ux-mockup-v1.0` con un caso de uso real portuario (p. ej. pantalla de gestión de atraques o ficha de buque).
2. Verificar que el mockup generado usa **exclusivamente** componentes del Design System APB (tokens CSS, componentes compuestos de `APB-DESIGN-SYSTEM`), no componentes DevExtreme "en crudo" sin wrapper corporativo.
3. Si el agente usa componentes fuera del Design System, actualizar su `context`/`tools` para restringirlo explícitamente al catálogo de `APB-DESIGN-SYSTEM`.

**Objetivo:** cerrar el ciclo Frontend → Design System: no basta con que el Design System exista, los agentes que generan UI deben referenciarlo activamente.

**Sesión asignada:** pendiente — se puede ejecutar en cuanto `APB-DESIGN-SYSTEM` tenga al menos un componente compuesto publicado. Candidata: ampliación de la sesión que cierre el punto #49, o tarea inline en la sesión de Design System si el tiempo lo permite.

---

### 54. Agente de análisis funcional: entrevista portuaria + verificación de dominio + actualización de repo de dominios

Ampliación del agente `apb-agent-ddd-v1.0` (creado en Sesión 18) o posible agente/subagente complementario que cubra el flujo de análisis funcional desde el inicio:

**Comportamiento deseado:**

1. **Entrevista al funcional:** en lugar de esperar que el funcional describa el problema de forma estructurada, el agente hace preguntas activas específicas del negocio portuario y del dominio que toque (p. ej. si el dominio es "atraques": ¿escala de tiempo?, ¿integración con GISPEM?, ¿tipos de buque involucrados?, ¿permisos de Autoridad Portuaria?). Las preguntas deben estar contextualizadas al vocabulario APB, no ser genéricas.

2. **Verifica si el dominio ya existe:** antes de proponer un dominio nuevo, consulta el repo `APB-DOMAIN-CATALOG` (submodule ya integrado en `APB-IA-FRAMEWORK`) y avisa al funcional si el dominio solicitado ya existe, ya sea exacto o parcialmente — evita proliferación de dominios duplicados o fragmentados.

3. **Actualiza el repo de dominios:** si el dominio es nuevo y se valida, el agente genera el artefacto correspondiente en `APB-DOMAIN-CATALOG` (conforme al schema de ese repo) y propone el commit — con aprobación humana previa obligatoria (nivel de autonomía 1, coherente con `SYSTEM.md` §5.1).

**Relación con componentes existentes:**
- `apb-agent-ddd-v1.0` (Sesión 18): análisis DDD una vez el dominio está identificado — este punto es el paso anterior, el de identificación y validación.
- `apb-sub-ddd-interview-v1.0` (creado en Sesión 18 como subagente de entrevista): verificar si ya cubre parte de este alcance o si el punto #54 lo amplía significativamente.
- `APB-DOMAIN-CATALOG` (repo submodule): es el repositorio de destino para las actualizaciones.

**Pendiente de verificar:** leer el contenido de `apb-sub-ddd-interview-v1.0` para determinar si ya implementa la entrevista portuaria contextualizada (#54.1) o si ese subagente es más genérico. En función de eso, puede ser ampliación del subagente existente o componente nuevo.

**Sesión asignada:** pendiente — candidata natural: sesión de continuación de Sesión 18 (la Fase 1 de descomposición de monolitos ya está marcada como pendiente en esa sesión; este punto podría incluirse en la misma sesión o en la de Sesión 13 si el volumen lo permite). Confirmar con Debora.

---

## Bloque añadido post-Sesión 23 (2026-06-27) — Análisis de enriquecimiento del framework

> Fuente: `discovery/analisis-enriquecimiento-framework.md` (análisis completo: 26 agentes · 23 subagentes · 129 skills · 8 workflows, generado 2026-06-27). El documento fuente completo está en el repo — esta sección extrae las tareas accionables en formato de plan.
> Sesiones candidatas: **Sesión Enriquecimiento A** (rewirings + agentes alta prioridad), **Sesión Enriquecimiento B** (skills nuevas por dominio), **Sesión Enriquecimiento C** (workflows + providers).

> **Estado de ejecución — TODO el bloque #55–#76: ✅ COMPLETADO** (Enriq. A/B/C/D;
> reconciliado 2026-07-02). Enriq. A (rewirings #55 + primeros componentes),
> B/C/D (resto de skills/agentes/subagentes/providers/workflows). El detalle de
> #55 y el registro consolidado de #56–#76 (7 agentes + 8 subagentes + 43 skills +
> 5 providers + 9 workflows verificados en repo) están en
> [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md). Único pendiente real:
> #64 (capacity/portfolio, diferidos por datos) y la decisión sobre #59 incident-l2.

---

### 56–#76 — Enriquecimiento del framework — ✅ EJECUTADO (Enriq. B/C/D, reconciliado 2026-07-02)

> **Reconciliación 2026-07-02:** discovery del repo confirma que **todo el bloque
> de construcción #56–#76 ya está creado y cableado** (se ejecutó en las Sesiones
> Enriquecimiento B/C/D, cerradas en conversación, pero el plan no se había
> reconciliado). Detalle movido a [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).
>
> **Verificado en repo (2026-07-02):**
>
> | Bloque | Propuesto | En repo |
> |---|---|---|
> | Agentes #56–#63 | 8 | ✅ 7 creados (`change-manager`, `problem-manager`, `data-governance`, `accessibility-auditor`, `vendor-manager`, `knowledge-manager`, `api-product-manager`) |
> | Subagentes #65 | 8 | ✅ 8 (`ops-k8s`, `ops-servicebus`, `finops-azure`, `doc-confluence`, `sec-sast`, `qa-performance`, `gov-data`, `ops-entra`) |
> | Skills #66–#72 | 43 | ✅ 43 (operation, security, governance, platform+FinOps, qa, documentation, arch/disc/pm/design) |
> | Providers #73 | 5 | ✅ 5 (`azure-cost`, `confluence`, `entra-id`, `sentinel`, `jira-software`) |
> | Workflows #74 | 9 | ✅ 9 (`change-management`, `problem-management`, `accessibility-audit`, `api-lifecycle`, `data-governance`, `finops-review`, `incident-l2`, `security-patch`, `vendor-procurement`) |
>
> **Pendiente real (no construido, por decisión):**
> - **#59 `apb-agent-incident-l2`** — NO se creó agente dedicado; la capacidad L2
>   se cubre con `apb-agent-incident-support-v1.0` + `apb-agent-sre-v1.0` a través
>   del workflow `apb-wf-incident-l2-v1.0` (+ subagentes k8s/servicebus/oracle).
>   Decisión: mantener así salvo que se quiera separar formalmente.
> - **#64 `apb-agent-capacity-planner`** — diferido: requiere ≥12 meses de datos Azure.
> - **#64 `apb-agent-portfolio-it`** — diferido: requiere datos reales de uso del framework.
> - **#75** (mejoras de calidad por agente) y **#76** (priorización) — aplicados durante Enriq.;
>   los gaps de calidad residuales se rastrean vía el check #18 del validador y §H.


## Revisión integral del framework — 2026-06-29 → ✅ ARCHIVADA

> Auditoría fechada (4 dimensiones + sesiones propuestas + backlog M1–M6, todos
> resueltos) movida a [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).
> Es una fotografía de estado ya superada por la ejecución posterior; los
> pendientes derivados se siguen en las secciones §H/§I de más abajo.

---

## Análisis 360° y reconciliación de estado — 2026-06-29 (post-Enriquecimiento B, revisión exhaustiva)

> ⚠️ Borrador generado por IA (Claude, Anthropic) — pendiente de validación por Arquitectura APB.
> **Commit base:** `bf1c72a` (local). **Método:** lectura completa del repositorio con 3 agentes
> paralelos: plan de fases (1881 líneas íntegras), los 35 agentes, los 33 subagentes, muestra de
> las 175 skills APB, las 51 skills de terceros, los 17 workflows, los 19 providers, scripts y
> docs clave (SYSTEM.md, GOVERNANCE.md, manual-arquitectura.md, SCHEMA.md, templates). Auditoría
> exhaustiva, no parcial.

> **⚠️ Nota de sesión:** Durante la sesión de análisis se aplicó un fix de wiring en
> `apb-agent-incident-support-v1.0.md` (añadidos 7 subagentes que estaban declarando este padre
> pero no estaban listados en él). El resto del wiring y los cambios al validador se realizarán
> en la próxima sesión.

---

### Conformidad estructural real por tipo de componente

| Tipo | Total | Conformes | % | Observación |
|------|-------|-----------|---|-------------|
| Skills APB | 175 | 175 | 100% | ✅ Todas con frontmatter, "Comportamiento", "Marcado IA" |
| Providers | 19 | 19 | 100% | ✅ |
| Wrappers | 7 | 7 | 100% | ✅ |
| Adapters | 4 | 4 | 100% | ✅ |
| Skills terceros | 51 | 51* | 100%* | *`source_commit: "unverified"` en todas — política GOVERNANCE §4.2, exento en CI, pero deuda real de supply-chain |
| Agentes | 35 | Por verificar | — | Requiere ejecutar `validate_repo.py --strict 2>&1 \| grep -i "Marcado IA"` para confirmar si el check produce ERROR o WARNING |
| Subagentes | 33 | Por verificar | — | Ídem para "Prompt de Sistema" |
| Workflows | 17 | Por verificar | — | Ídem para "Manejo de Fallos" |

---

### A. Estado real reconciliado (el plan documentado va por detrás del repo)
> (`validate_repo.py --strict` + grep/conteo sobre frontmatter de huérfanos, estados, autonomía,
> marcado IA, system prompts, duplicados) + lectura íntegra de los documentos meta (`SYSTEM.md`,
> `GOVERNANCE.md`, `docs/manual-arquitectura.md`, este plan completo y
> `analisis-enriquecimiento-framework.md`). No es lectura línea a línea de los 341 archivos: es
> verificación estructural del 100% + muestreo de componentes representativos.

### A. Estado real reconciliado (el plan documentado va por detrás del repo)

| Bloque | Estado documentado | Estado **real verificado** |
|---|---|---|
| Enriquecimiento A (rewirings #55 + sec/gov/ops + 3 agentes + 5 subagentes) | ✅ Completado | ✅ Confirmado |
| Enriquecimiento B (32 skills + 4 agentes + 5 subagentes) | ✅ Componentes creados | ⚠️ **Creados pero NO cableados a sus "Agentes destino"** (los puntos #60–72 sí los especificaban) |
| Enriquecimiento C (5 providers + 9 workflows) | Sin marca | ✅ **Componentes creados** (19 providers, 17 workflows) — ⚠️ faltan mejoras de workflows existentes del #74 |
| Revisión 2026-06-29: 26 agentes sin Marcado IA / 19 subagentes sin prompt / bug validador | 🔴 Pendiente | ✅ **Ya resueltos** (35/35 marcado, 33/33 prompt, validador corregido) |
| Backlog M1–M6 | Mezcla | ✅ Resuelto |
| `README.md` → enlace `CATALOG.md` (raíz) | — | ❌ **Roto**: el catálogo está en `catalog/CATALOG.md`, no en raíz |
| `domain-catalog/domains/` | — | ✅ **POBLADO (2026-06-30)**: 21 dominios de negocio `proposed` (Sesión DDD sobre `API_INVENTORY_APIM.md`) — pendiente aprobación Arquitectura |

> **Conclusión de gobernanza:** falta un mecanismo que reconcilie "plan ↔ repo". Varias cosas marcadas
> como pendientes ya están hechas, y al revés (el wiring de B figura implícito en el plan pero no se ejecutó).

---

### B. Wiring incompleto — 12 inconsistencias confirmadas (revisión agente por agente)

Subagentes que declaran `parent_agent` pero el agente padre NO los lista en `subagents:`. Verificado
leyendo el frontmatter de los 35 agentes y los 33 subagentes:

| Subagente | Padre declarado | Estado en padre |
|-----------|----------------|-----------------|
| `apb-sub-ops-aca-v1.0` | `apb-agent-incident-support-v1.0` | ✅ **FIJADO** (sesión 2026-06-29) |
| `apb-sub-ops-iis-apache-v1.0` | `apb-agent-incident-support-v1.0` | ✅ **FIJADO** (sesión 2026-06-29) |
| `apb-sub-ops-k8s-v1.0` | `apb-agent-incident-support-v1.0` | ✅ **FIJADO** (sesión 2026-06-29) |
| `apb-sub-ops-network-v1.0` | `apb-agent-incident-support-v1.0` | ✅ **FIJADO** (sesión 2026-06-29) |
| `apb-sub-ops-oracle-v1.0` | `apb-agent-incident-support-v1.0` | ✅ **FIJADO** (sesión 2026-06-29) |
| `apb-sub-ops-rancher-v1.0` | `apb-agent-incident-support-v1.0` | ✅ **FIJADO** (sesión 2026-06-29) |
| `apb-sub-ops-servicebus-v1.0` | `apb-agent-incident-support-v1.0` | ✅ **FIJADO** (sesión 2026-06-29) |
| `apb-sub-ops-entra-v1.0` | `apb-agent-security-architect-v1.0` | ⏳ Pendiente próxima sesión |
| `apb-sub-sec-sast-v1.0` | `apb-agent-security-architect-v1.0` | ⏳ Pendiente próxima sesión |
| `apb-sub-qa-performance-v1.0` | `apb-agent-qa-auto-v1.0` | ⏳ Pendiente próxima sesión |
| `apb-sub-finops-azure-v1.0` | `apb-agent-finops-v1.0` | ⏳ Pendiente próxima sesión |
| `apb-sub-gov-data-v1.0` | `apb-agent-data-governance-v1.0` | ⏳ Pendiente próxima sesión |

**Causa raíz:** `validate_agent_subagent_consistency` en el validador verifica solo que el `parent_agent`
referenciado **exista**, no que el agente lo **liste** en `subagents:`. Es validación unidireccional.
**Fix planificado:** función `validate_bidirectional_wiring()` en próxima sesión + test nº 24.

---

### C. Mapeo de skills de Enriq. B pendientes de cablear (por agente destino)

Extraído de los puntos #68–#72 del plan. Las skills existen en el repo pero aún no están en la lista
`skills:` de los agentes que deben usarlas. Pendiente de wiring en próxima sesión:

| Agente destino | Skills a añadir |
|----------------|-----------------|
| `apb-agent-data-governance-v1.0` | `apb-gov-data-classification-v1.0`, `apb-gov-dpia-v1.0` |
| `apb-agent-governance-v1.0` | `apb-gov-data-classification-v1.0`, `apb-gov-ai-model-lifecycle-v1.0`, `apb-gov-tech-radar-v1.0`, `apb-gov-framework-metrics-v1.0`, `apb-gov-framework-audit-v1.0` |
| `apb-agent-compliance-audit-v1.0` | `apb-gov-lcsp-check-v1.0`, `apb-gov-dpia-v1.0` |
| `apb-agent-vendor-manager-v1.0` | `apb-gov-lcsp-check-v1.0`, `apb-gov-vendor-eval-v1.0` |
| `apb-agent-catalog-manager-v1.0` | `apb-gov-framework-metrics-v1.0`, `apb-gov-framework-audit-v1.0` |
| `apb-agent-tech-discovery-v1.0` | `apb-gov-tech-radar-v1.0`, `apb-disc-tech-eval-v1.0`, `apb-disc-poc-guide-v1.0` |
| `apb-agent-finops-v1.0` | `apb-plat-finops-alerting-v1.0`, `apb-plat-finops-chargeback-v1.0`, `apb-plat-finops-reservations-v1.0` |
| `apb-agent-platform-engineer-v1.0` | `apb-plat-k8s-v1.0`, `apb-plat-azure-servicebus-v1.0`, `apb-plat-secret-rotation-v1.0`, `apb-plat-environment-promotion-v1.0` |
| `apb-agent-cloud-architect-v1.0` | `apb-plat-k8s-v1.0`, `apb-plat-azure-servicebus-v1.0` |
| `apb-agent-release-manager-v1.0` | `apb-plat-environment-promotion-v1.0`, `apb-doc-changelog-v1.0`, `apb-doc-release-notes-v1.0` |
| `apb-agent-qa-auto-v1.0` | `apb-qa-performance-v1.0`, `apb-qa-contract-testing-v1.0`, `apb-qa-accessibility-v1.0` |
| `apb-agent-accessibility-auditor-v1.0` | `apb-qa-accessibility-v1.0` |
| `apb-agent-ux-mockup-v1.0` | `apb-qa-accessibility-v1.0`, `apb-design-wcag-patterns-v1.0` |
| `apb-agent-documentation-v1.0` | `apb-doc-changelog-v1.0`, `apb-doc-release-notes-v1.0`, `apb-doc-onboarding-v1.0` |
| `apb-agent-knowledge-manager-v1.0` | `apb-doc-onboarding-v1.0` |
| `apb-agent-sre-v1.0` | `apb-doc-post-mortem-v1.0` |
| `apb-agent-technical-architect-v1.0` | `apb-arch-c4-model-v1.0`, `apb-arch-context-mapping-v1.0` |
| `apb-agent-domain-architect-v1.0` | `apb-arch-context-mapping-v1.0` |
| `apb-agent-api-product-manager-v1.0` | `apb-arch-api-lifecycle-v1.0` |
| `apb-agent-business-analyst-v1.0` | `apb-disc-user-journey-v1.0`, `apb-disc-value-stream-v1.0`, `apb-pm-risk-register-v1.0`, `apb-pm-stakeholder-map-v1.0` |
| `apb-agent-pm-v1.0` | `apb-pm-risk-register-v1.0`, `apb-pm-status-report-v1.0`, `apb-pm-stakeholder-map-v1.0` |

---

### D. Evolución del framework por ámbito (análisis 360°)

#### D.1 Técnico
- **Trayectoria:** prompts sueltos → jerarquía 7 niveles + validador 19 checks + catálogo autogenerado
  + CI bloqueante + 23 tests de dogfooding. Madurez alta en *forma estructural*.
- **Brechas críticas:**
  - Sin **runtime de orquestación real**: workflows son instrucciones manuales. `invoke_agent.py`
    es un esqueleto. Manual-arquitectura §3.1 recomienda **Azure AI Foundry + Semantic Kernel**.
  - Sin **memoria compartida** inter-sesiones: Redis (short-term) + Cosmos DB (state) + Git (long-term).
  - **Wiring unidireccional** en validador: no detecta subagentes/skills huérfanos.
  - **Encoding Windows**: fix ya aplicado en `bf1c72a` (`sys.stdout.reconfigure(encoding="utf-8")`).
  - `README.md` → enlace roto a `CATALOG.md` (raíz no existe; está en `catalog/CATALOG.md`).
- **Mejoras a implementar (próxima sesión):**
  1. `validate_bidirectional_wiring()` en validador con test
  2. Fix enlace README
  3. Verificar si checks de agentes/subagentes/workflows producen ERROR o WARNING en validador actual

#### D.2 Funcional (cobertura de dominios IT)

| Área | Nivel | Gap |
|------|-------|-----|
| SDD / Especificación | ✅ Sólida | — |
| Desarrollo .NET/Django | ✅ Sólida | — |
| Code Review | ✅ Buena | — |
| QA Automatizado | ✅ Buena (caveat) | `qa-performance` no declarado en padre (fix pendiente) |
| Arquitectura / DDD | ✅ Sólida | ✅ Domain Catalog poblado: 21 dominios `proposed` (Sesión DDD 2026-06-30) — pendiente aprobación Arquitectura |
| Seguridad | ✅ Buena | `entra`/`sast` no declarados; sin DAST wrapper propio |
| Gobernanza | ✅ Muy buena | 0 aprobaciones; ningún validador humano nombrado |
| DevOps / Plataforma | 🟡 Media | Wiring de 4 platform skills pendiente |
| Operaciones L1 | ✅ Buena | 7 subagentes ya fijados en incident-support |
| SRE / Observabilidad | ✅ Buena | — |
| FinOps | 🟡 Media | 3 skills + 1 subagente pendientes de cablear |
| Change / Problem Mgmt | 🟡 Media | Agentes existen; skills de wiring pendiente |
| PM / Discovery | 🟡 Limitada | Skills Enriq. B no cableadas a BA/PM/TechDiscovery |
| WCAG / Accesibilidad | 🟡 Nueva | accessibility-auditor nuevo; wiring pendiente |
| LCSP / Licitación | ❌ Pendiente | Bloqueado: briefing de Débora |
| Descomposición monolitos | ❌ Pendiente | Domain Catalog ya poblado (21 dominios `proposed`); falta aprobación + acceso a código SOSTRAT |
| M365 / Teams / SharePoint | 🟡 CONSTRUIDO (draft) | `prov-ms365-v1.0` + `prov-entra-id-v1.0` + adapters m365/rovo + OpenAPI/Forge existen. **MCP Graph cableado en `.mcp.json` (2026-07-04, `@softeria/ms-365-mcp-server`, device-code, aprobado por Débora)** — solo falta activación de app registration Entra ID (credenciales/tenant — Plataforma) para el flujo headless. Ver `AUDITORIA_DESFASE_PLAN_REPO.md` |

#### D.3 QA del framework
- **Validación solo estructural** (forma del componente), NO funcional (comportamiento).
- `tests/test_agent_behavior.md` existe como piloto pero no está automatizado.
- Sin tests de regresión de contenido: si una skill cambia instrucción, el validador no lo detecta.
- **Madurez QA propuesta:**
  - Tier 1 (inmediato): check anti-huérfanos automático (test nº 24)
  - Tier 2 (próximas sesiones): Golden Output Tests para 5 skills críticas
  - Tier 3 (mediano plazo): integration tests con LLM mock para agentes

#### D.4 Seguridad
- `apb-sub-sec-sast-v1.0` y `apb-sub-ops-entra-v1.0`: pendientes de **visto bueno de Ciberseguridad** antes de uso.
- 51 skills terceros sin SHA fijado: **deuda de supply-chain** (política temporal deliberada).
- `prov-sentinel-v1.0` y `prov-entra-id-v1.0`: providers presentes sin integración confirmada.
- Gap: sin **DAST wrapper** propio (OWASP ZAP / Trivy) para seguridad ofensiva.

#### D.5 Gobernanza
- GOVERNANCE.md, SYSTEM.md §7.2, estados de componentes: marco bien definido.
- **Brecha crítica: 341/341 en `draft`** (KPI objetivo: <30%). 0 ciclos de aprobación iniciados.
- Ningún componente tiene `validador humano nombrado` → ninguno puede pasar a `approved`.
- Telemetría: scripts `emit_telemetry.py` e `invoke_agent.py` presentes como esqueletos. Los 5 KPIs
  de GOVERNANCE §6 son **imposibles de medir** sin datos reales.
- Plan ↔ repo desincronizado: necesita proceso de reconciliación tras cada sesión.

#### D.6 Mantenimiento futuro
- Sin check anti-huérfanos → cada sesión de enriquecimiento puede añadir deuda silenciosa.
- Sin telemetría real → componentes en desuso no detectables.
- Ciclo revisión semestral (`review_date:` vencido) → sin automatización de avisos.
- Templates actualizadas (29-Jun). Todos los tipos de componentes con plantilla válida.

---

### E. Riesgos de cara a producción

| # | Riesgo | Sev. | Mitigación |
|---|--------|------|-----------|
| R1 | Sin runtime de orquestación: workflows manuales no escalables | 🔴 | Decisión runtime + `prov-orchestration-engine-v1.0` |
| R2 | 5 subagentes no declarados → capacidades invisibles a sus agentes | 🔴 | Wiring en próxima sesión (4 pendientes) |
| R3 | 100% draft: sin ningún componente aprobado formalmente | 🔴 | Primer ciclo aprobación |
| R4 | ~~Domain Catalog vacío → DDD/monolitos bloqueados~~ ✅ MITIGADO: inventario recibido + 21 dominios `proposed` (Sesión DDD 2026-06-30) | 🟢 | Pendiente aprobación Arquitectura + experto de negocio para fronteras |
| R5 | Wiring skills Enriq. B: capacidades funcionales no invocables desde agentes | 🟡 | Mapeo §C, próxima sesión |
| R6 | Sin memoria compartida → contexto perdido inter-sesiones | 🟡 | Redis + Cosmos DB (cuando runtime listo) |
| R7 | Telemetría no instrumentada → KPIs imposibles de medir | 🟡 | Instrumentar `invoke_agent.py` |
| R8 | ~~51 skills terceros sin SHA fijado~~ ✅ MITIGADO EN SU MAYORÍA (Sesión 19, 2026-07-04): 48 descriptores fijados a SHA real vía `git ls-remote`; quedan **11** `unverified` con causa documentada (repos de origen movidos/privados/no-GitHub: `hashicorp/terraform-search-import`, `neondatabase/neon-postgres`, `openai/security-threat-model`, `mukul975/cybersecurity-arsenal`, `ccusage`/`ComposioHQ` sin repo concreto, `graphify.net` y `skills.sh` no-GitHub) | 🟢 | Los 11 restantes requieren re-identificar el repo de origen (posibles sucesores detectados: `neondatabase/agent-skills`, `openai/skills`) — confirmar equivalencia de contenido antes de re-apuntar |
| R9 | SAST/Entra sin validación Ciberseguridad | 🟡 | Revisión Ciber antes de uso |
| R10 | Sin DAST wrapper → gap de seguridad ofensiva | 🟡 | OWASP ZAP o Trivy wrapper |
| R11 | Plan ↔ repo desincronizado | 🟡 | Actualizar plan tras cada sesión |
| R12 | README → enlace roto a CATALOG.md | 🟢 | Fix trivial en próxima sesión |

---

### F. Skills / componentes de TERCEROS a evaluar

Para varios gaps conviene **incorporar** en lugar de construir desde cero. Proceso estándar:
licencia + análisis de seguridad + `source_commit` SHA real.

| Gap / necesidad | Tercero candidato | Prioridad | Nota |
|---|---|---|---|
| Runtime de orquestación | **Microsoft Semantic Kernel** / Azure AI Foundry | 🔴 | Ya recomendado en `manual-arquitectura.md §3.1` |
| Telemetría automática | **OpenTelemetry Python** | 🔴 | Para instrumentar `invoke_agent.py` |
| Developer Portal / discoverability | **Backstage** (Spotify) | 🟡 | Catálogo de servicios + componentes APB |
| DAST / seguridad ofensiva | **OWASP ZAP** / Trivy | 🟡 | Gap de cobertura en seguridad |
| Contexto enriquecido para LLM | **`context7`** | 🟡 | ✅ **Evaluado (Sesión 19):** `upstash/context7`, MIT, muy activo (~58,5k ⭐). Es un servidor MCP de documentación actualizada de librerías para LLMs — encaja como **provider/MCP** (patrón `.mcp.json` de proyecto, como Playwright), no como skill. **✅ incorporado el mismo día con OK de Débora** como `prov-context7-v1.0` (`draft`, `provider_type: context`, sin activar — activación real requiere `.mcp.json` de proyecto) |
| Debugging sistemático | **`obra/superpowers` → systematic debugging** | 🟡 | ✅ **Evaluado (Sesión 19):** confirmada como skill distinta (`skills/systematic-debugging/`, MIT, repo activo) — metodología de 4 fases de causa raíz antes de cualquier fix. No duplica las 2 obra ya incorporadas. **✅ incorporado el mismo día con OK de Débora** como `third-obra-systematic-debugging-v1.0` (`draft`, `development`) |
| Dev / arquitectura TypeScript | **`mattpocock/*` resto del monorepo** | 🟡 | ✅ **Evaluado (Sesión 19):** el repo se reestructuró (categorías `engineering/`, 16 skills + `productivity/`, `misc/`, `personal/`). Cruce: la mayoría duplica el catálogo (code-review, tdd, domain-modeling, implement, diagnosing-bugs≈systematic-debugging). **2 candidatas con valor no duplicado — ✅ ambas incorporadas el mismo día con OK de Débora:** `third-mattpocock-resolving-merge-conflicts-v1.0` (`development`) y `third-mattpocock-triage-v1.0` (`pm`), ambas `draft`. Nota: las 2 ya incorporadas apuntan a skills renombradas en origen (`grill-prd-issues`→`to-prd`/`to-issues`; `codebase-architecture-analysis`→`improve-codebase-architecture`) — SHA fijado, contenido revisar en próxima actualización |
| Diagramación arquitectura | `excalidraw` (MCP) | 🟢 | ✅ **Evaluado (Sesión 19):** `excalidraw/excalidraw`, MIT, muy activo (~126,7k ⭐). Herramienta de pizarra/diagramas. **Decisión de Débora (2026-07-04): incorporar como MCP en una fase futura** (no en esta sesión) — candidato a `prov-excalidraw-v1.0` cuando se aborde, ligado a caso de uso de `apb-arch-c4-model` / skills de arquitectura. Registrado como pendiente en M.8. |
| Terraform governance | Ampliar `hashicorp` existente | 🟢 | Ya 2 skills; ampliar a modules y workspaces |
| `_spec-driven` skills + terceros abiertos §8 | 3 skills `spec-to-*` de `apb-ai-skills` | 🟢 | Sesión 19 + #45 |

> Acción: **Sesión 19** (terceros), aportando Débora las URLs exactas que falten.

---

### G. Temas futuros planificados — consolidado

| Tema | Punto | Estado / bloqueante |
|---|---|---|
| **Valoración COSMIC con histórico real** | #8 | `apb-disc-cosmic-v1.0` existe; **bloqueado: horas históricas de Débora** |
| Agentes de licitación LCSP | #36/Sesión 20 | **Bloqueado: briefing de Débora** |
| Descomposición de monolitos (Fase 1) | #38 F1 | Catálogo ya poblado (21 dominios `proposed`); bloqueado por aprobación + acceso a código SOSTRAT |
| Spec desde histórico Jira | #37 | Sin sesión asignada |
| Runtime de orquestación real | #41 | **Bloqueado: decisión arquitectónica Débora/Plataforma** |
| Dashboards Power BI/Grafana + logs | #39/#40 | ✅ CONSTRUIDO (draft): `apb-agent-observability-v1.0` + subagentes PowerBI/Grafana + telemetría. Instrumentación real OTel añadida (`prov-otel-v1.0`, 2026-07-04). Falta activación real (Plataforma). Ver `AUDITORIA_DESFASE_PLAN_REPO.md` |
| Telemetría para usuarios de chat sin commit | #46 | Requiere proxy/wrapper de plataforma |
| Distribución Design System (npm/submodule/CDN) | #49/Sesión 22 | **Bloqueado: decisión de Débora** |
| QA del propio framework + prueba real agentes | #50/#51 | Alimenta paso a `approved` |
| Documentación Word por audiencias + doc Dirección | #23/Sesión 14 | Parcial: borradores MD; falta .docx |
| Plantillas Word/Excel ofimáticas | #6 | Bloqueado: ejemplos de Débora |
| Email Arquitectura → cola Jira | #52 | Bloqueado: dirección de Débora |
| Mockup validación Design System | #53 | Tras #49 |
| Capacity Planner / Portfolio IT | #64 | Diferidos: ≥12 meses de datos reales en Azure |
| Memoria compartida agentes | (nuevo) | Tras decisión runtime |
| Primer ciclo aprobación formal | GOVERNANCE §2 | Requires: aprobadores nombrados por ámbito |

---

### H. Siguientes fases — orden de ejecución recomendado

#### ✅ FASE 0 — Higiene de wiring + validador (COMPLETADA 2026-06-30)

Commit: `d62c6b1`. 24 ficheros, 284 inserciones. Resultado: `--strict` exit 0, 59 warnings exentos.

1. ✅ **Fix README.md**: enlace `CATALOG.md` → `catalog/CATALOG.md` corregido.
2. ✅ **Wiring 5 subagentes huérfanos**: `entra`+`sast` → `security-architect`; `performance` →
   `qa-auto`; `finops-azure` → `finops`; `gov-data` → `data-governance`.
3. ✅ **Wiring skills Enriq. B**: 40 wirings corregidos en 22 agentes (tabla §C + 19 adicionales
   detectados por el nuevo validador).
4. ✅ **`validate_bidirectional_wiring()`** añadida a `scripts/validate_repo.py` + test
   `TestValidateBidirectionalWiring` (2 casos) en `tests/test_validate_repo.py`.
5. ✅ Catálogo regenerado, `--strict` verde, 21/21 tests OK.

> **Regla de cierre de sesión (Débora, 2026-06-30):** al cierre de CADA sesión ejecutar siempre:
> `generate_catalog.py` + `validate_repo.py --strict` + tests + actualizar PLAN_FASES_FUTURAS +
> CONTINUIDAD + HANDOFF + README. Guardado en memoria del agente.

#### ✅ FASE 1 — Mejoras de workflows existentes (COMPLETADA 2026-06-30)

8. ✅ Añadir Change Manager a `sdd-full` y `cloud-migration`.
9. ✅ Añadir Security Architect a `code-review` (PRs con cambios en auth/datos sensibles).
10. ✅ Conectar `incident-l1` → `incident-l2` workflow + campo `escalation:` en frontmatter.
11. ✅ Añadir Problem Manager a `incident-l1` para incidencias recurrentes.
12. ✅ Añadir Tech Debt a `legacy-onboarding`.
13. ✅ Añadir performance y accessibility a `qa-evidence`.

#### ✅ FASE 1B — Corrección de bugs BUG-01 a BUG-08 (COMPLETADA 2026-06-30)

14. ✅ BUG-01: `context/apb/templates/WORKFLOW.md` — blockquote → YAML frontmatter canónico.
15. ✅ BUG-02: `scripts/generate_catalog.py` — regex `\s*+` → `\s*` (8 patrones, Python 3.10).
16. ⏸ BUG-03: `design-system/components/component-reference.md §9` — color sidebar pendiente confirmación equipo diseño.
17. ✅ BUG-04: `adapters/claude/adapter-claude-v1.0.md` — model string `claude-sonnet-4-6`.
18. ✅ BUG-05: `SYSTEM.md §4.2` — añadidos adapters `m365` y `rovo` (los 4 reales del repo).
19. ✅ BUG-06: `.github/workflows/telemetry.yml` — anti-pattern git push → PR automático.
20. ✅ BUG-07: `CONTINUIDAD_PROYECTO.md §8` — 208 → 341 componentes.
21. ✅ BUG-08: `third-lum1104-knowledge-graph-v1.0.md` — stub creado con `status: watchlist` y aviso licencia no verificada.

#### FASE 2 — Sesiones abiertas del plan

14. **Sesión 13** resto: puntos #6 (plantillas Word), #8 (COSMIC—bloqueado), #52 (email Jira).
15. **Sesión 14**: ✅ **documento Dirección creado** (`docs/informe-direccion.md`, 2026-06-30). Pendiente: conversión .docx (requiere decisión runtime + plantilla).
16. **Sesión 19**: terceros adicionales + decisión `_spec-driven` (bloqueado: URLs de Débora).
17. **Sesión 20**: agentes LCSP (bloqueado: briefing de Débora).
18. **Sesión 21**: SQL skills + soporte incidencias generalista (✅ completada 2026-06-29).
19. **Sesión 22**: Design System distribución (bloqueado: decisión de Débora).
20. ✅ **#50/#51**: QA del framework — 20 casos de comportamiento (6 agentes), 5 Golden Output Tests, test Python de cobertura (2026-06-30).

#### FASE 3 — Evolución estratégica (a 1–12 meses)

21. ✅ **Domain Catalog** poblado: 21 dominios de negocio `proposed` en
    `APB-DOMAIN-CATALOG/domains/` (Sesión DDD 2026-06-30, sobre `API_INVENTORY_APIM.md`).
    Pendiente: PR + aprobación de Arquitectura + experto de negocio para fronteras
    (Escalas/Cruceros/Líneas, INS/PIF, MDE/OPS, FER). **Bounded contexts diferidos**
    a sesión "DDD Fase BC" con acceso a código/BBDD.
22. **Runtime de orquestación** (decisión + `prov-orchestration-engine-v1.0` + Semantic Kernel).
23. **Memoria compartida** (`prov-agent-memory-v1.0`: Redis + Cosmos DB + Git).
24. **Telemetría automática**: instrumentar `invoke_agent.py` con OpenTelemetry → dashboard Power BI.
25. **Primer ciclo de aprobación formal**: seleccionar 10 componentes core, asignar aprobadores
    (2 por componente, ámbitos distintos), llevar a `approved`. KPI: <30% en draft.
26. **Fase 1 descomposición monolitos** — Domain Catalog ya poblado (21 dominios
    `proposed`); ahora bloqueado por: aprobación de dominios + acceso al código del
    monolito SOSTRAT (Java/Oracle → DOCKS).

---

### I. Decisiones pendientes por persona/equipo

#### Bloqueos de Débora / Dirección

| Decisión | Desbloquea | Urgencia |
|----------|-----------|---------|
| ~~Listado de APIs/sistemas APB~~ ✅ **RECIBIDO (2026-06-30)** — `API_INVENTORY_APIM.md`; Sesión DDD ejecutada, 21 dominios `proposed` | ~~Domain Catalog, DDD, descomposición monolitos~~ → ahora desbloqueado | 🟢 |
| Decisión runtime orquestación (Azure AI Foundry vs. Anthropic SDK) | Fase 3 §H-22 | 🟡 Mes 1 |
| Mecanismo distribución Design System | Sesión 22 | 🟡 Mes 1 |
| Ejemplos Word/Excel + mapa agentes↔Jira | Sesión 14, punto #6 | 🟡 Mes 1 |
| Horas históricas reales para COSMIC | Calibración `apb-disc-cosmic-v1.0` (#8) | 🟡 Mes 2 |
| Briefing LCSP | Sesión 20 (agentes licitación) | 🟡 Mes 2 |
| Qué componentes aprobar primero + aprobadores por ámbito | Primer ciclo gobernanza | 🟡 Mes 1 |
| Esbozo informe riesgos IA organizativo | Sesión 16 | 🟢 Mes 2-3 |
| URLs de repos de terceros adicionales | Sesión 19 | 🟢 Mes 2-3 |
| Email/cola Jira de Arquitectura | Toda la documentación (#52) | 🟢 |
| Confirmación disponibilidad Rovo en tenant APB | Activación `adapter-rovo-v1.0` | 🟢 Julio 2026 |
| Pasos concretos del proceso APB de evaluación/migración a Cloud | Punto #87 — reescritura de `apb-wf-cloud-migration-v1.0` | 🟡 Cuando Débora lo aporte |

#### Equipos (tareas técnicas)

| Equipo | Qué validar / hacer | Entregable |
|--------|---------------------|-----------|
| **Arquitectura APB** | Revisar y aprobar (draft→candidate) los 4 agentes y skills arch/disc/governance nuevos; validar wiring §C; decidir destino skills PM; resolver 3 grupos de duplicados; liderar primer ciclo aprobación; decidir runtime con Plataforma | Componentes con `approved_by:` nombrado |
| **Plataforma / Cloud** | Validar skills K8s/AKS, ServiceBus, secret-rotation, environment-promotion y FinOps contra stack Azure real (naming, tiers, subscriptions); activar M365 integrations (HANDOFF_SESION15); co-decidir runtime; implementar Redis+Cosmos cuando runtime decidido | Validación técnica + pipeline parametrizable |
| **Operaciones / SRE** | Validar subagente Entra ID; confirmar umbrales/SLOs reales en skills observabilidad/post-mortem/capacity; preparar runbooks puente mientras no hay orquestación; integrar `emit_telemetry.py` con Azure Monitor | SLOs reales + runbooks operativos |
| **Ciberseguridad** | Revisar y aprobar `apb-sub-sec-sast-v1.0` y `apb-sub-ops-entra-v1.0` antes de uso; validar 51 exenciones `source_commit`; proponer proceso para fijar SHAs; evaluar necesidad de DAST wrapper | Aprobación seguridad documentada |
| **DPO / Protección de datos** | Validar `apb-gov-dpia-v1.0`, `apb-gov-data-classification-v1.0`, `apb-sub-gov-data-v1.0` contra criterio AEPD (RGPD art. 30/35, ENS) | Confirmación encaje normativo |
| **QA** | Definir Golden Output Tests para 5 skills críticas; extender `test_agent_behavior.md` a automatizados; definir umbrales k6 reales para tests de performance | Estrategia test comportamiento |
| **Negocio / PM** | Validar 5 skills PM nuevas (user-journey, value-stream, risk-register, status-report, stakeholder-map); confirmar agente destino (PM vs. BA); confirmar qué perfiles las usarán | Validación utilidad funcional |
| **Gobernanza del catálogo** | Registrar validador humano por componente cuando inicie ciclo aprobación; diseñar proceso draft→candidate→approved; planificar telemetría KPIs; mantener reconciliación plan↔repo | Owner por componente + plan métricas |

---

### J. Verificación end-to-end (al final de CADA sesión — obligatorio)

```bash
# 1. Catálogo actualizado
python scripts/generate_catalog.py

# 2. Validación estricta — criterio canónico: exit 0 (NO el conteo de errores)
PYTHONIOENCODING=utf-8 python scripts/validate_repo.py --strict

# 3. Tests completos
python -m unittest tests.test_validate_repo tests.test_behavior_coverage -v
# → 33/33 (test_validate_repo) + 5/5 (test_behavior_coverage) = 38 total (2026-06-30)

# 4. Verificación de wirings aplicados (ejemplo)
grep -A30 "^subagents:" agents/apb-agent-incident-support-v1.0.md
grep -A5 "^subagents:" agents/apb-agent-security-architect-v1.0.md

# 5. Fix README verificado
grep "CATALOG.md" README.md
# debe mostrar solo "catalog/CATALOG.md", nunca "CATALOG.md" sin prefijo
```

> **Referencia:** `discovery/HANDOFF_TECNICOS.md` contiene las tareas manuales de despliegue/producción
> (crear suscripción Azure, registrar apps AD, poblar Key Vault, etc.). Las decisiones/insumos
> bloqueantes de Débora o Dirección viven **solo aquí**, en la tabla de arriba (§I).


---

## K. Evoluciones propuestas — Análisis 360° (2026-06-29)

> Fuente: `analisis_exhaustivo_framework.md` — análisis multi-perspectiva de los tres repositorios.
> Todo lo que sigue es propuesta IA. Ningún punto es ejecutable sin revisión y aprobación humana.

### K.1 Evoluciones técnicas

| ID | Título | Descripción | Prioridad | Esfuerzo est. |
|----|--------|-------------|-----------|--------------|
| E-T1 | **Motor de orquestación real** | Los workflows están en Markdown pero no se ejecutan automáticamente. Opciones: (A) GitHub Action parametrizable que lee el frontmatter YAML y pausa en `human_checkpoints` vía GitHub Environments — 1-2 días; (B) `orchestrator.py` con log de ejecución — 1 semana; (C) integración con `microsoft/semantic-kernel` — 1 mes+. Recomendada Opción A como primer paso. | Alta | 1-2 días (opción A) |
| E-T2 | **Golden tests para skills críticas** | ~~Para las 5 skills candidadas a aprobación, crear tests estáticos.~~ **✅ COMPLETADO (2026-06-30):** clase `TestGoldenOutputStructure` (5 tests) en `tests/test_validate_repo.py`. Verifica `## Marcado IA obligatorio`, `## ⚠️ Comportamiento ante inputs incompletos` e `id:` en frontmatter para: `apb-arch-api-contract-v1.0`, `apb-qa-accessibility-v1.0`, `apb-dev-code-review-v1.0`, `apb-sec-threat-model-v1.0`, `apb-gov-evidence-v1.0`. | ~~Media~~ | ✅ Cerrado |
| E-T3 | **Notificación de breaking changes en contratos de skills** | ~~Cuando una skill actualiza su versión mayor, `validate_repo.py` debería generar WARNING.~~ **✅ COMPLETADO (2026-06-30):** función `validate_version_drift()` añadida a `scripts/validate_repo.py` + clase `TestVersionDrift` (2 tests) en `tests/test_validate_repo.py`. 33/33 tests OK. | ~~Media~~ | ✅ Cerrado |
| E-T4 | **Capa formal de Capabilities** | Crear la carpeta `capabilities/` declarada en SYSTEM.md §3 con descriptores de capacidades de negocio (Generar Especificaciones, Revisar Código, Diseñar Arquitectura, Gestionar Incidentes...). Completa la jerarquía y facilita la alineación con el negocio. | Baja | 1 semana |
| E-T5 | **Caching de outputs de agentes dentro de un workflow** | Para workflows que procesan el mismo artefacto base, implementar caching por hash de input. Reduce coste de tokens en re-ejecuciones parciales. | Baja | 1-2 semanas |

### K.2 Evoluciones funcionales

| ID | Título | Descripción | Prioridad | Notas |
|----|--------|-------------|-----------|-------|
| E-F1 | **Agente de Change Management / ITIL** | APB opera con ITIL (P1–P4, L1/L2/L3, CAB, RFC, Problem Management). `apb-agent-change-manager-v1.0` cubriría: evaluación de impacto de RFC, informe para CAB, tracking de cambios de emergencia, tickets Jira. **✅ YA CONSTRUIDO (draft):** `apb-agent-change-manager-v1.0` + `apb-agent-problem-manager-v1.0` creados (Enriq. #56–#76). E-F1 pendiente = solo llevarlo a operativo/approved. | Construido | ✅ Existe (2026-07-04) |
| E-F2 | **Agente de Data Governance / RGPD** | Obligación regulatoria: RAT, bases jurídicas, plazos de conservación, DPIA. **✅ YA CONSTRUIDO (draft):** `apb-agent-data-governance-v1.0` (+ `apb-gov-dpia-v1.0`, `apb-gov-data-classification-v1.0`, `apb-sub-gov-data-v1.0`) creados (Enriq. #56–#76). Pendiente = operativo/approved + validación DPO. | Construido | ✅ Existe — requisito legal, priorizar aprobación |
| E-F3 | **Enriquecimiento FinOps Azure** | Visibilidad de costes de IA. **✅ YA CONSTRUIDO (draft):** `apb-agent-finops-v1.0` + skills `apb-plat-finops-*` (alerting/chargeback/reservations) + `apb-sub-finops-azure-v1.0` existen. Pendiente = activar sobre Azure Cost real (datos). | Construido | ✅ Existe (2026-07-04) |
| E-F4 | **Workflows de licitación / LCSP** | APB sujeto a LCSP. Preparación de pliegos, evaluación de ofertas, gestión de contratos de mantenimiento. Pendiente briefing de Débora. | Media | Bloqueado: briefing de Débora |
| E-F5 | **Agente de Onboarding de Proyectos Legacy** | `apb-agent-legacy-onboarding-v1.0` que automatice el análisis inicial de un proyecto existente (estructura de código, deuda técnica, APIs no documentadas) y genere el primer borrador del `system-spec.md`. | Media | — |

### K.3 Evoluciones de seguridad

| ID | Título | Descripción | Prioridad | Implementación |
|----|--------|-------------|-----------|---------------|
| E-S1 | **SBOM automatizado para terceros** | Los 51 skills de terceros + 7 wrappers deberían generar automáticamente un Software Bill of Materials. Ampliar `generate_catalog.py` para añadir sección SBOM en `CATALOG.md` con `source_repo`, `source_license`, `source_commit`, `verified_date`. | Alta | Extensión de script existente |
| E-S2 | **Supply chain verification en CI** | Step que intente verificar el SHA actual del repo de origen (`git ls-remote`). Si accesible y SHA cambió: WARNING "contenido modificado en origen desde la última revisión". | Media | GitHub Action adicional |
| E-S3 | **Auditoría periódica de dependencias** | GitHub Action semanal con `pip-audit` o `safety check` para wrappers con dependencias Python. Integrar hallazgos como input a `apb-agent-tech-debt-v1.0`. | Media | GitHub Action semanal |

### K.4 Evoluciones de gobernanza

| ID | Título | Descripción | Prioridad | Implementación |
|----|--------|-------------|-----------|---------------|
| E-G1 | **Dashboard de métricas de gobernanza** | Dashboard en Log Analytics o Power BI: % de componentes por estado, tiempo medio de aprobación, skills más invocadas, evolución del reuso (objetivo >50%). Dependiente de telemetría activa. | Alta | Dependiente de telemetría |
| E-G2 | **Ciclo de revisión semestral automatizado** | ~~GitHub Action mensual.~~ **✅ COMPLETADO (2026-06-30):** `scripts/check_review_dates.py` + `.github/workflows/review-reminder.yml` (cron día 1 de cada mes). Abre issue automático con componentes con `review_date` > 180 días. | ~~Media~~ | ✅ Cerrado |
| E-G3 | **Proceso formal de deprecación** | ~~Documentar en GOVERNANCE.md.~~ **✅ COMPLETADO (2026-06-30):** `GOVERNANCE.md §7` — quién propone, quién aprueba, plazos (30 días si consumed_by activo), pasos técnicos, paso a `retired` (90 días). | ~~Media~~ | ✅ Cerrado |

### K.5 Evoluciones de Developer Experience

| ID | Título | Descripción | Prioridad | Esfuerzo est. |
|----|--------|-------------|-----------|--------------|
| E-DX1 | **Guía "Primera skill / Primer agente"** | ~~`docs/getting-started-contributing.md`.~~ **✅ COMPLETADO (2026-06-30):** `docs/getting-started-contributing.md` con 8 secciones: prerrequisitos, discovery, skill paso a paso, agente paso a paso, validador, catálogo, PR checklist, cierre de sesión. | ~~Media~~ | ✅ Cerrado |
| E-DX2 | **Storybook para APB-DESIGN-SYSTEM** | Reemplazar o complementar `visual-reference.html` con Storybook. Cada componente JSX con ejemplos interactivos, documentación de props y tests de accesibilidad automáticos (addon a11y — WCAG 2.1 AA, requisito regulatorio vía RD 1112/2018). | Baja | 2-3 días configuración |

---

## Bloque añadido 2026-06-30 — Orquestación y Coreografía de Agentes

### 77. Orquestación y coreografía de agentes — análisis e implementación

> **Propuesta recibida de Debora (2026-06-30).** Este punto requiere análisis previo antes de
> implementar. Ningún componente se construye hasta que la decisión arquitectónica esté aprobada.

> **Nueva evidencia (Sesión DDD, 2026-06-30):** al ejecutar `apb-agent-ddd-v1.0` para poblar
> APB-DOMAIN-CATALOG no existía motor que invocara el agente programáticamente — se ejecutó su
> protocolo manualmente (lectura del `.md` + aplicación de los pasos). Esto provocó que se
> omitiera el paso explícito del agente "cargar `prov-apb-knowledge-v1.0` antes de ejecutar",
> causando un error de dominio (SOJA mal clasificado, modelo incompleto: 15 dominios en vez de
> 21) que solo se detectó porque Débora lo corrigió manualmente. **Conclusión: la falta de
> runtime de orquestación no es solo un problema de eficiencia — ya ha causado un error de
> calidad real por incumplimiento silencioso de las instrucciones declaradas en el frontmatter
> de un agente.** Refuerza la prioridad de este punto #77.

> **Segunda recurrencia (Sesión QA TruckCenter, continuación 2026-07-03).** Al pedir Débora "ejecutar el
> plan de pruebas completo" con `apb-agent-qa-auto-v1.0`/`apb-qa-exploratory-nav-v1.0`, se repitió el
> mismo patrón que en la sesión DDD: sin motor que invoque el agente, se siguió su `.md` manualmente y se
> omitieron en silencio varios pasos que el propio documento declara obligatorios — (1) el proceso
> "razonar → plan → aceptación → ejecutar" (no se presentó el plan de qué IDs concretos se iban a
> intentar antes de empezar); (2) la oferta explícita de abrir Jira ante hallazgos (§12/§6.3 de la
> skill); (3) el uso de vídeo real vía Playwright MCP que el propio plan ya había dejado especificado en
> el **punto #88** para esta sesión (no se consultó `PLAN_FASES_FUTURAS.md` antes de empezar, y se usó
> GIF de `claude-in-chrome` sin advertirlo). Además, al pedir "el plan completo" solo se ejecutó una
> muestra (55/120 casos con algún estado, 65 sin tocar) sin decirlo explícitamente hasta que Débora
> preguntó. **Corrección aplicada:** memoria de feedback permanente
> `feedback_agente_runtime_vs_manual` (memoria personal de Débora, fuera de este repo) — declarar siempre
> si se ejecuta con runtime real o solo siguiendo el `.md`, y checklist obligatorio (comprobar
> `PLAN_FASES_FUTURAS`/`COMPLETADAS` antes, plan explícito con OK, recuento numérico al cierre, oferta de
> Jira). Refuerza aún más la prioridad de #77: van ya dos incidentes de calidad reales y documentados por
> la misma causa raíz.

#### Contexto y propuesta recibida

Debora propone una arquitectura híbrida de dos capas para coordinar los agentes del framework:

1. **Capa de Orquestación (macro)** — workflows de alto nivel con estado, reintentos y ramificaciones.
   Herramientas candidatas: LangGraph, Temporal, Prefect/Dagster.
2. **Capa de Coreografía (micro)** — comunicación inter-agente por eventos (pub/sub).
   Herramientas candidatas: Azure Service Bus (ya en stack APB), CloudEvents + JSON.

Flujo propuesto para "Implementar feature X":

```
PM → Arch → Dev (commit+push) → CI/CD (GitHub Actions vía repository_dispatch)
   ← evento ci.completed ← Service Bus ←─────────────────────────────────────
└─ Si éxito → PR → Review → merge
└─ Si fallo → Dev corrige → nuevo commit (máx 3 reintentos)
```

Patrones adicionales mencionados en la propuesta: Saga Pattern, Event Sourcing, LangGraph con
checkpoint + webhook para reanudar workflows pausados tras eventos CI.

#### Análisis de adecuación al stack APB

**Lo que encaja bien:**

- Azure Service Bus ya está en el stack APB → la coreografía por eventos es coherente. El framework
  ya lo cubre a nivel de **skill** (`apb-plat-azure-servicebus-v1.0`) y **subagente**
  (`apb-sub-ops-servicebus-v1.0`); **NO existe aún un provider `prov-servicebus-v1.0`** (corrección
  2026-07-04: el plan lo daba por existente y no lo estaba) — crearlo sería el paso de extensión a
  orquestación por eventos.
- CloudEvents + JSON ya están en el stack APB → formato de eventos sin coste adicional.
- GitHub Actions ya gestiona CI/CD del framework → `repository_dispatch` para disparar CI desde
  agentes es viable y sin dependencias nuevas.
- El patrón de **autonomy_level 1 con gates humanos** del framework es compatible con Saga Pattern:
  cada compensación puede ser un gate de aprobación humana en vez de un rollback automático.

**Lo que requiere ajuste antes de adoptar:**

- **LangGraph** es Python y de Anthropic/LangChain; el stack APB es .NET + Azure. Viable para el
  framework de IA (ya es Python), pero introduce dependencia nueva. Alternativa nativa Azure:
  **Azure Durable Functions** o **Azure AI Foundry Agents** (ya recomendado en `manual-arquitectura.md §3.1`).
  Hay que decidir cuál antes de implementar. **No adoptar LangGraph sin evaluar las alternativas Azure.**
- **Temporal** es excelente para workflows duraderos pero añade infraestructura separada (servidor
  Temporal) que APB debería operar. **Azure Durable Functions** cubre el mismo caso de uso sin
  infraestructura adicional y ya es parte de Azure. Recomendación: Temporal solo si Azure Durable
  Functions no cubre el caso concreto de APB.
- **Event Sourcing completo** (toda acción es evento inmutable, reconstrucción de estado) es
  potente pero añade complejidad significativa de implementación. Antes de adoptarlo, verificar si
  los logs de GitHub Actions + telemetría JSONL ya existente (`emit_telemetry.py`) cubren el 80%
  del valor con el 20% del coste. El Event Sourcing puro se reserva para decisiones críticas de
  agentes que impacten producción.
- **Power BI (ejecutivo) + Grafana (operativo)** ya están en el plan (#39/#40, Sesión 17 parcial).
  El dashboard de orquestación se construye sobre la misma base, no es una herramienta nueva.

**Restricción no negociable:** todo lo que se construya **debe respetar el guardrail de autonomy_level 1**.
El orquestador no puede auto-aprobar, auto-mergear ni desplegar a producción sin gate humano, aunque
LangGraph o Temporal técnicamente lo permitan. Los `human_checkpoints` declarados en los workflows
son obligatorios también en el motor de ejecución real.

#### Decisiones arquitectónicas previas a implementar (bloqueantes)

| Decisión | Opciones | Quién decide | Urgencia |
|----------|----------|--------------|---------|
| Motor de orquestación macro | (A) Azure Durable Functions + Azure AI Foundry; (B) LangGraph; (C) Temporal | Debora + Plataforma APB | 🔴 Mes 1 |
| Broker de eventos inter-agente | Azure Service Bus (ya en stack, **recomendado**) vs. otra solución | Debora + Plataforma APB | 🟡 Mes 1 |
| Formato de eventos | CloudEvents + JSON (ya en stack, **recomendado**) vs. otro | Arquitectura APB | 🟡 Mes 1 |
| Alcance de Event Sourcing | Solo eventos de agente críticos vs. todo el pipeline vs. ninguno | Debora | 🟡 Mes 2 |
| Almacenamiento de estado de workflow | Redis (short-term) + Cosmos DB (state) — ya en plan §D.1 | Plataforma APB | 🟡 Mes 2 |
| Estrategia de reintentos | Máximo de reintentos + escalado humano (cuántos, quién recibe) | Debora | 🟡 Mes 2 |

#### Trabajo de análisis previo a implementar (Sesión de Análisis de Orquestación)

Antes de construir nada, realizar:

1. **PoC comparativo** de las opciones de orquestación macro sobre un caso de uso real APB
   (candidato: `apb-wf-sdd-full-v1.0` como primer workflow a orquestar):
   - Opción A — GitHub Action parametrizable que lee frontmatter YAML y pausa en `human_checkpoints`
     vía GitHub Environments. Esfuerzo estimado: 1-2 días. Recomendado como primer paso (`E-T1`).
   - Opción B — `orchestrator.py` con log de ejecución local. Esfuerzo: 1 semana.
   - Opción C — Azure Durable Functions (nativo Azure). Esfuerzo: 2-3 semanas.
   - Opción D — LangGraph con checkpoints (solo si C no es viable). Esfuerzo: 2-3 semanas + infra.

2. **Verificar capacidades existentes** antes de construir:
   - `apb-orch-multi-agent-v1.0`, `apb-orch-context-handoff-v1.0`, `apb-orch-human-checkpoint-v1.0`
     (ya creadas en Sesión 21). ¿Qué parte del problema ya resuelven?
   - `invoke_agent.py` (esqueleto existente). ¿Hasta dónde llega?
   - `apb-plat-azure-servicebus-v1.0` (skill existente) + `apb-sub-ops-servicebus-v1.0` (subagente existente). **No hay provider `prov-servicebus-v1.0`** (corrección 2026-07-04) — evaluar si crearlo. ¿Cubren el caso de eventos inter-agente?

3. **Definir los contratos de eventos** antes de implementar la capa de coreografía:
   - Esquema CloudEvent por tipo de evento: `code.generated`, `ci.trigger`, `ci.completed`,
     `pr.review.requested`, `pr.review.completed`, `bug.classified`, etc.
   - Qué campos son obligatorios en `data:` por tipo de evento.
   - Quién es productor y quién es consumidor de cada evento.

#### Componentes a construir (tras decisión arquitectónica)

**Fase de Coreografía (bajo riesgo — Azure Service Bus ya en stack):**

| Componente | Tipo | Descripción |
|------------|------|-------------|
| `apb-orch-event-schema-v1.0` | skill | Esquemas CloudEvents para los eventos del pipeline de desarrollo: `code.*`, `ci.*`, `pr.*`, `bug.*`, `deployment.*` |
| `apb-orch-event-router-v1.0` | skill | Reglas de enrutamiento: qué agente reacciona a qué evento, condiciones de activación, timeout por evento |
| `prov-orchestration-engine-v1.0` | provider | Adaptador al motor de orquestación elegido (Azure Durable Functions / LangGraph). Abstrae el runtime para que skills/agentes no dependan del motor concreto | 
| `apb-sub-orch-ci-bridge-v1.0` | subagente | Puente CI/CD: convierte eventos del framework en `repository_dispatch` de GitHub Actions y procesa `ci.completed` de vuelta al workflow pausado |

**Fase de Orquestación macro (tras PoC):**

| Componente | Tipo | Descripción |
|------------|------|-------------|
| `apb-wf-agent-pipeline-v1.0` | workflow | Workflow de referencia orquestado: PM → Arch → Dev → CI → Review → Deploy, con gates humanos en cada transición de fase |
| `apb-wf-bug-to-fix-v1.0` | workflow | Bug report → Triage → Dev fix → CI → Review → Deploy, con escalado a humano si reintentos fallidos |

**Agente coordinador (fase avanzada — tras orquestación funcionando):**

| Componente | Tipo | Descripción |
|------------|------|-------------|
| `apb-agent-orchestrator-v1.0` | agente | Agente que gestiona el estado global de un workflow activo: pausa en gates humanos, reanuda tras eventos CI, detecta timeouts, escala a humano si se excede el máximo de reintentos. Delega en agentes especializados, no ejecuta lógica de dominio directamente |

**Dashboard de orquestación** (construir sobre base Sesión 17 #39/#40):

- Pipeline de estado de workflows activos en Power BI / DevExpress.
- Stream de eventos CloudEvent con filtros.
- Panel de aprobaciones humanas pendientes (gates activos).

#### Stack recomendado para APB (decisión pendiente de Debora)

| Componente | Tecnología recomendada | Justificación |
|------------|----------------------|---------------|
| Motor orquestación macro | **Azure Durable Functions** (primera opción) / LangGraph (fallback) | Native Azure, sin infraestructura separada, compatible .NET + Python |
| Broker de eventos | **Azure Service Bus** | Ya en stack APB — sin nueva dependencia |
| Formato eventos | **CloudEvents + JSON** | Ya en stack APB |
| Estado de workflow | **Redis** (short-term) + **Cosmos DB** (long-term state) | Ya en plan D.1 |
| Observabilidad | **OpenTelemetry** → Azure Monitor → Power BI / Grafana | Conecta con Sesión 17 (#39/#40) |
| UI de monitoreo | **DevExpress** (JS puro) | Stack frontend APB estándar |

#### Relación con puntos existentes del plan

- **E-T1** (motor de orquestación real, §K.1): este punto #77 es la implementación completa de E-T1.
  E-T1 propone GitHub Action como primer paso; #77 amplía el análisis al ecosistema completo.
- **#41** (orquestación real entre agentes, Sesión 13): #77 es la concreción de ese punto.
- **#29** (loop engineering): los reintentos y loops de iteración forman parte del motor de orquestación.
- **#12** (definición de loops): ídem.
- **#24** (Goal-Driven Execution): el motor de orquestación es el mecanismo que ejecuta los objetivos.
- **Recomendación consolidada de #41**: resolver #12, #24, #29 y #41 en la misma sesión — este punto
  #77 es la sesión donde todo eso converge en decisión + implementación.

#### Sesión asignada

**Sesión de Análisis de Orquestación** (nueva sesión propia, tras Sesión 13).

**Bloqueante:** decisión arquitectónica de Debora + Plataforma APB sobre el motor de orquestación
(Azure Durable Functions vs. LangGraph vs. otro). Sin esa decisión el PoC no puede completarse.

**Secuencia recomendada:**

1. Debora + Plataforma: decidir motor de orquestación (Mes 1).
2. Sesión de Análisis de Orquestación: PoC, contratos de eventos, verificación de capacidades existentes.
3. Construir capa de coreografía (Service Bus + CloudEvents) — bajo riesgo, puede ir en paralelo.
4. Construir `prov-orchestration-engine-v1.0` sobre el motor elegido.
5. Implementar `apb-wf-agent-pipeline-v1.0` como primer workflow orquestado real.
6. `apb-agent-orchestrator-v1.0` — solo tras validar el motor en producción.

#### **Sesión de Análisis de Orquestación completada: 2026-07-06**

> **PoC entregada:** GitHub Action con pausas sincrónicas de aprobación humana (escalón 1 del análisis).
> 
> Ficheros generados:
> - `scripts/orchestrate_checkpoint_gate.py` — lee frontmatter YAML, extrae `human_checkpoints`, genera bloque de pausa
> - `.github/workflows/human-checkpoint-poc.yml` — workflow_dispatch + environment con required reviewers
> - `scripts/setup_github_environment.py` — crea/actualiza environment + revisores vía API (portabilidad repo)
> - [`discovery/HANDOFF_ORQUESTACION_MOTOR.md`](HANDOFF_ORQUESTACION_MOTOR.md) — tabla comparativa (Durable Functions / LangGraph / Temporal), checklist pre-decisión, contrato de eventos (v1 draft)
>
> **Próximo bloqueante:** Débora + Plataforma deciden motor de orquestación (A/B/C en handoff). Una vez confirmado, pasar a fase de especificación + prototipo + integración.
> 
> Ver [`HANDOFF_ORQUESTACION_MOTOR.md`](HANDOFF_ORQUESTACION_MOTOR.md) para detalles técnicos y checklist.

---

## Bloque añadido 2026-07-02 (Debora — estándar de prompting, memoria, planes de pruebas, harness)

> Estado: **#78 y #83 ejecutados** (Sesión #78+#83, 2026-07-02 — ver
> [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md)). El resto (#79–#82, #84)
> sigue anotado, no ejecutado, hasta su sesión propia. Se cruzan explícitamente
> con contenido existente para evitar duplicación.

### 78. Estándar de prompting para TODOS los componentes — ✅ EJECUTADO
(Sesión #78+#83, 2026-07-02). Estándar canónico: `context/apb/standards/PROMPTING_STANDARD.md`
(10 ejes + 11 prohibiciones). 6 plantillas actualizadas, retrofit completo de 244 componentes,
check #18 del validador en ERROR. Detalle en [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).

### 79. Terceros a verificar/incorporar: MCP Builder, Fine Skills, Anthropic cybersecurity skills — ✅ RESUELTO 2/3 (Sesión 19, 2026-07-04)

- **MCP Builder** — ✅ **alcance confirmado (Sesión 19):** el wrapper
  `third-anthropic-mcp-builder-v1.0` ya soporta `target_system: custom-api`,
  con lo que los MCPs de Teams/SharePoint/mail del #30 quedan cubiertos vía
  Microsoft Graph API sin re-incorporación. Única mejora futura (cuando se
  aborde #30): añadir filas explícitas `teams`/`sharepoint`/`mail` a la
  tabla de sistemas soportados del wrapper. Además su `source_commit` quedó
  fijado a SHA real (R8).
- **"Fine Skills"** — ❌ **sigue pendiente: única parte abierta del #79.**
  Requiere que Debora aporte URL/organización exacta antes de evaluar
  (mismo criterio que el bloque #27).
- **Anthropic cybersecurity skills** — ✅ **evaluado (Sesión 19), hallazgo
  de identidad importante:** el repo llamado "Anthropic-Cybersecurity-Skills"
  (817 skills, Apache 2.0, mapeo MITRE ATT&CK/NIST CSF/D3FEND) **no es de
  Anthropic** — es de `mukul975`, la misma fuente ya incorporada al catálogo
  con 5 skills curadas (`third-mukul-*`); no procede re-incorporar el
  agregado completo. El candidato **oficial de Anthropic** real es
  `anthropics/defending-code-reference-harness` (Apache 2.0, SHA `b5b61c8`,
  6 skills: quickstart/threat-model/vuln-scan/triage/patch/customize +
  harness autónomo de 7 etapas que requiere sandbox gVisor). Solape:
  threat-model solapa parcialmente con `apb-sec-threat-model-v1.0` y
  `third-openai-threat-model-v1.0`; vuln-scan/triage/patch complementan
  (SAST + triaje + parche, conecta con #86 y con el gap R10/DAST solo
  parcialmente — es SAST, no DAST). **Recomendación: incorporar un único
  descriptor `third-anthropic-defending-code-v1.0` (dominio `security`)
  cubriendo las 6 skills, excluyendo el harness autónomo (sandbox gVisor
  fuera del stack APB). Pendiente de OK de Débora antes de crear el
  descriptor (GOVERNANCE §4).**

**Cruce:** bloque #27 (terceros pendientes) y sección M.8.

### 80. Memoria corporativa del framework (contexto + histórico + aprendizaje continuo + persistencia)

Configurar una **memoria propia del framework** que proporcione a los
agentes: (a) **contexto** de proyecto/dominio, (b) **histórico** de
decisiones y sesiones, (c) **aprendizaje continuo** (lecciones, correcciones
recurrentes), con **opción de memoria persistente** entre sesiones.

**Cruces (no duplicar — esto es una DECISIÓN de arquitectura, no un
componente suelto):**
- M.6 ya propone `HKUDS/LightRAG` (`wrap-hkuds-lightrag-v1.0`, definido, sin
  desplegar) y `mem0ai/mem0` (`wrap-mem0-v1.0`, pendiente) como candidatos a
  "memoria corporativa".
- Punto #23 / R6 / la línea 2071 ya prevén **memoria compartida
  inter-sesiones** (`prov-agent-memory-v1.0`: Redis short-term + Cosmos DB
  state + Git long-term), condicionada a la decisión de runtime.
- El modelo de **Harness Engineering (#83)** aporta el mecanismo concreto de
  persistencia versionada: `PROGRESS.md`, principios ACID de estado y
  Bootstrap Contract (ver §2 y §4 de #83). La "memoria persistente en Git"
  del harness y la "memoria episódica" de LightRAG/mem0 son **capas
  complementarias**, no alternativas: Git = durabilidad/auditoría;
  LightRAG/mem0 = recuperación semántica.

**Trabajo del punto:** decidir la arquitectura de memoria (¿Git+PROGRESS.md
como capa base obligatoria + LightRAG/mem0 como capa semántica opcional?),
no reabrir la elección de herramienta desde cero. **Sesión candidata:**
ligada a la decisión de runtime (misma que #77 Orquestación) porque la
memoria compartida depende del motor.

### 81. Obsidian como capa de conocimiento/memoria navegable — ✅ RESUELTO (Sesión 19, 2026-07-04)

**Conclusión de la evaluación:** viable y recomendado como **herramienta de
apoyo opcional, solo lectura** — abrir el propio repo como vault no requiere
ninguna transformación (los `.md` ya están enlazados), el graph view y los
backlinks dan la navegación visual de `depends_on`/`consumed_by` que pedía
el punto. **No** se registra como componente del catálogo. Salvaguardas:
(1) no editar desde Obsidian — cualquier edición saltaría el validador/CI,
la fuente de verdad sigue siendo Git + PR (Principios #4/#6); (2) excluir
la carpeta `.obsidian/` del repo vía `.gitignore` si algún usuario lo abre
como vault (configuración personal, no versionable). Documentado en la fila
M.6. No introduce fuente de verdad paralela. Cierre sin componente nuevo.

<details><summary>Planteamiento original (histórico)</summary>

Evaluar **Obsidian** (vault Markdown local + grafo de enlaces) como:
- Interfaz humana de navegación sobre la memoria del framework (#80): el
  repo ya es Markdown enlazado, Obsidian lo convierte en grafo navegable sin
  transformación.
- Herramienta de visualización de dependencias entre componentes
  (`depends_on`/`consumed_by` de `SCHEMA.md`) vía backlinks/graph view.

**Cruce:** #80 (memoria) y bloque #27 (Excalidraw/context7 como
herramientas, no como skills). No es un componente del catálogo sino una
**herramienta de apoyo** — documentar como tal en M. Verificar que no
introduce una fuente de verdad paralela (Principio #4: la fuente de verdad
técnica es Git; Obsidian es solo proyección de lectura, como Confluence en
Principio #6). **Sesión candidata: Sesión 19** (junto con #79).

</details>

### 82. Metodología y plantilla corporativa de planes de pruebas — ✅ EJECUTADO
(Sesión QA-2, 2026-07-02). `context/apb/standards/TEST_PLAN_STANDARD.md` + plantilla
`context/apb/templates/TEST_PLAN.md` + skill `apb-qa-test-plan-v1.0` v1.2.0 (interactiva; orden de
fuentes con degradación; **ingesta de planes aportados por el usuario en cualquier formato** vía
`apb-plat-doc-to-markdown`; unificación sin duplicados con **procedencia múltiple**; detección de plan
previo + actualización incremental; secciones de gobernanza; no-regresión de rendimiento). Ejemplo
canónico: `docs/qa/examples/QA_TRU_TruckCenter_UNIFICADO.md` (112 casos sin duplicar) + fuentes en
`docs/qa/examples/sources/`. Check #20 en el validador. Detalle en
[`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).

> **Pendiente derivado (nuevo, Débora 2026-07-02):** el agente de pruebas funcionales debe poder
> **consultar credenciales desde un repositorio central** (encaja con Azure Key Vault, `GOVERNANCE.md §5`)
> para ejecutar de forma autónoma sin que el usuario introduzca credenciales cada vez. En la demo de QA-2
> las introdujo el usuario (login EntraID asistido). Diseñar el mecanismo (provider de secretos + captura y
> reutilización de `storage_state`). Ver HANDOFF.

<details><summary>Requisitos originales (histórico)</summary>

Elevar el plan de pruebas de "artefacto que genera una skill" a **proceso
gobernado con plantilla, histórico y trazabilidad**. Requisitos:

**a) Orden de fuentes obligatorio del agente de plan de pruebas:**
   1. **Rovo primero** — analiza los tickets de Jira y sus adjuntos, el
      análisis funcional y la documentación aportada por el usuario.
   2. **GitHub Copilot después** — ingeniería inversa del código para
      completar/contrastar lo funcional.
   (Es decir: lo funcional manda; el código se usa para verificar y
   completar, no como fuente primaria.)

**b) Detección de plan previo:** antes de generar uno nuevo, comprobar si ya
   existía un plan de pruebas. Si existe, **revisar cambios y actualizar
   desde la fecha del plan anterior** (no regenerar desde cero).

**c) Columna de trazabilidad por prueba:** cada caso lleva una columna que
   indica **qué funcional dio el OK** y **desde cuándo** se definió esa
   prueba en el plan.

**d) Secciones nuevas obligatorias del documento de plan:**
   - **Histórico de cambios del plan.**
   - **Aprobados del plan según cambios** (quién aprobó qué versión/cambio).
   - **Enlace bidireccional plan ↔ evidencias** (desde el plan a las
     evidencias de resultados y desde las evidencias al plan).
   - **Evidencias vinculadas a Jira.**

**e) Almacenamiento de resultados:** definir dónde se guardan — propuesta a
   confirmar con Debora: **en el repo de cada aplicación** (no en el repo del
   framework), con las evidencias enlazadas a Jira.

**f) Gobernanza y gestión del cambio** del plan de pruebas: proceso de
   aprobación de cambios, versionado, responsables.

**g) Plantilla de resultados esperados:** partir de **un ejemplo real que
   Debora facilitará** y convertirlo en plantilla. Todos los ejemplos
   incluyen: introducción funcional, integraciones, resumen de arquitectura
   topológica, relación de tablas y Spec — la plantilla debe contemplar
   estas secciones fijas.

**h) Verificación de no-regresión de rendimiento:** comprobar que el
   rendimiento **no empeora** respecto a la ejecución anterior del plan.
   Definir **dónde se consulta el resultado anterior**; y cuando **nunca se
   ejecutó antes**, ejecutar el plan **sobre la versión anterior del código
   y luego sobre la nueva** para obtener la comparativa. (Cruce con
   `prov-k6-v1.0` — carga/rendimiento.)

**i) Planes preliminares existentes:** Debora aportará un conjunto de
   **planes de pruebas preliminares** de ciertas aplicaciones; hay que
   dejarlos disponibles en el repo para el futuro y **actualizarlos con la
   nueva versión del agente**.

**Cruces (no duplicar):** skills `apb-qa-test-plan-v1.0` (marco
LCSP/ENS/RGPD/WCAG, ya tiene tabla de criterios de éxito),
`apb-qa-test-auto-v1.0`, wrapper `third-anthropic-playwright-v1.0`, workflow
`apb-wf-qa-evidence-v1.0`, adapter `adapter-rovo-v1.0`, provider `prov-k6-v1.0`.
Este punto **no crea otra skill de plan de pruebas**: amplía
`apb-qa-test-plan-v1.0` (columnas de trazabilidad, histórico, detección de
plan previo) + define la plantilla de resultados esperados + gobernanza.

**Bloqueantes (aportados por Debora):** el **ejemplo real** para la
plantilla (g) y los **planes preliminares** (i). **Sesión candidata:**
Sesión QA-2 propia (el volumen lo justifica).

</details>

### 83. Harness Engineering agnóstico de LLM — ✅ EJECUTADO
(Sesión #78+#83, 2026-07-02). Normativa permanente: `SYSTEM.md §10` (5 subsistemas, ACID,
routing files, WIP=1, Feature Lists) + `GOVERNANCE.md §8` (Pass-State Gating, 3 capas,
Clean State Handoff). Scaffolding en `repo-scaffold/harness-ready/` (AGENTS/PROGRESS/FEATURES/init_check).
Check #19 del validador (Cold-Start Test). Fuera de alcance aquí: OTel §83.7 (→ Sesión 17) y
arquitectura de 3 agentes ejecutable (→ #77). Detalle en [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).

### 84. Navegación agéntica para pruebas funcionales — ✅ EJECUTADO
(Sesión QA-2, 2026-07-02). `providers/prov-browser-agent-v1.0.md` (provider de acción agnóstico:
abrir URL, observar pantalla/DOM, decidir siguiente paso, rellenar, aseverar, capturar evidencia;
implementaciones de referencia Playwright MCP / claude-in-chrome / computer-use) + skill
`apb-qa-exploratory-nav-v1.0` (frontera exploratorio vs scriptado; cableada a `apb-agent-qa-auto` y
`apb-wf-qa-evidence`). **Ejecución real demostrada** sobre TruckCenter PRE (login EntraID asistido, rol
MANAGE): 4 casos PASS (TRU-T77/T26/T15/T16), 1 no evaluable, 2 hallazgos; evidencias empaquetadas (ZIP)
y camino Jira definido. Detalle en [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).

**Continuación (2026-07-03) — ejecución a mayor escala + corrección de metodología:** nueva sesión con
Débora ejecutando **44 de los 120 casos** del plan unificado v1.4 (lectura y escritura real en PRE,
bloques B02-B07 + E2E T112), con **2 hallazgos críticos** en la app (H1 sin integridad referencial al
eliminar Tipo de Vehículo; H2 maestro de tipos desactualizado en el AF/plan) documentados en el propio
plan (§15, → v1.5). Corrección de metodología derivada: `TEST_PLAN_STANDARD` → v1.4.0 (§5.15 casos no
ejecutados obligatorios por ID, §7.2 vídeo real no GIF), skill `apb-qa-exploratory-nav` → v1.1.0, check
#24 del validador, y activación real de Playwright MCP (`.mcp.json` de proyecto +
`prov-playwright-v1.0` v1.1.0) para vídeo nativo en la próxima ejecución. Detalle completo → **punto #88**
y [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).

**Segunda continuación (2026-07-03, misma fecha) — el punto #88 NO se siguió y quedó abierto:** nueva
sesión ejecutó 11 casos netos adicionales (B02/B03/B05/B06/B07/B08/B12) sin reabrir Claude Code, por lo
que Playwright MCP no estaba cargado — se usó de nuevo GIF de `claude-in-chrome` sin segmentar por bloque
(mismo defecto que motivó `TEST_PLAN_STANDARD §7.2`), y no se presentó plan explícito ni se ofreció Jira
al cerrar. 3 hallazgos nuevos (H5/H6/H7, ver §16 de `QA_TRU_TruckCenter_UNIFICADO.md` v1.6) + H1/H2/H4
reconfirmados. **Total acumulado: 55/120.** Corrección de proceso: nota añadida en punto #77 (segunda
recurrencia del riesgo de runtime) + memoria de feedback permanente de Débora
(`feedback_agente_runtime_vs_manual`, fuera de este repo). El punto #88 **sigue pendiente tal cual** —
la próxima sesión debe reabrir Claude Code con Playwright MCP cargado antes de empezar.

<details><summary>Análisis original del gap (histórico)</summary>

**Origen:** pregunta de Debora (2026-07-02) — "¿el framework puede abrir un
navegador para pruebas funcionales?". Respuesta: **parcial**. Existe
navegación *scripted* (Playwright) a nivel de diseño; **no existe**
navegación *agéntica/exploratoria* en vivo.

Estado actual:
- **Cubierto (diseño, `draft`, sin desplegar):** `prov-playwright-v1.0`
  (abre chromium/firefox/webkit, screenshots, trazas, simula interacciones),
  `third-anthropic-playwright-v1.0`, `apb-sub-qa-e2e-v1.0`,
  `apb-qa-test-auto-v1.0`, `apb-wf-qa-evidence-v1.0` → generan y ejecutan
  **tests Playwright escritos** (guion fijo).
- **Gap:** ningún componente permite que un agente **navegue la UI en vivo y
  de forma exploratoria** (abrir la app, "ver" la pantalla, rellenar
  formularios y decidir el siguiente paso sin guion) — la "agent browser
  skill" que menciona Debora.

**Propuesta:** cubrir el gap combinando **Playwright (pruebas scriptadas
reproducibles)** + una **skill de browser agéntico** para exploración en
vivo (candidatos a evaluar: Playwright MCP conducido por el agente,
computer-use / Claude-in-Chrome como referencia de patrón, siempre bajo el
principio agnóstico de LLM del #83). Definir la frontera: exploratorio para
descubrimiento/QA manual asistido; scriptado para regresión reproducible en
CI. **Sesión candidata:** Sesión QA-2 (junto con #82, comparten insumo de
plan de pruebas y evidencias).

</details>

### 85. Enriquecimiento del catálogo corporativo de dominios (consulta funcional + guía de clasificación) — (a)/(d) ✅ EJECUTADO (2026-07-04)

> **(a) y (d) ejecutados en `GitHub-Repos/APB-DOMAIN-CATALOG`** (el clon real con los 21
> `domain.md`, no el submódulo de `main` — ver aclaración de ruta en
> `AUDITORIA_DESFASE_PLAN_REPO.md §9`): `scaffolding/scripts/generate_domain_catalog_html.py`
> genera `catalog/DOMAINS.html` (listado + búsqueda/filtro + ficha por dominio) leyendo
> `domains/*/domain.md` directamente — nunca desde `ddd-discovery/` ni a mano. Añadido además el
> **primer workflow de CI de este repo** (`.github/workflows/validate.yml`), que ejecuta
> `validate_catalog.py` (ya existía, sin conectar) + un chequeo `--check` de drift del HTML en
> cada push/PR a `main` — gobernanza automática, no generación puntual por un agente. Catálogo de
> referencia en `scaffolding/reference/dominios-tipicos-referencia.md`. Commit local
> `617ae1f` en la rama `feat/carga-inicial-dominios-apim` — **sin push**, pendiente de que Débora
> confirme subirlo (igual que el resto de esa rama, aún sin PR a `main`). (b) y (c) siguen
> pendientes de la aprobación de Arquitectura de los 21 dominios, como estaba previsto.

Ampliar el **catálogo corporativo de dominios de negocio** (repo
`APB-DOMAIN-CATALOG`, 21 dominios `proposed`, ver #38 Fase 0 y #54) con:

**a) Vista HTML de consulta para perfiles funcionales.** Generar un HTML
navegable (autocontenido) para que **personas funcionales, no técnicas**,
puedan consultar el catálogo sin abrir el repo ni leer Markdown/YAML:
listado de dominios, búsqueda/filtro, ficha por dominio. Debe generarse
**automáticamente** desde los `domain.md`/artefactos del catálogo (no
mantenerse a mano) — candidato a extender
`scaffolding/scripts/validate_catalog.py` o un `generate_catalog_html.py`
nuevo en el repo del catálogo. Cruce con #81 (Obsidian) como alternativa de
navegación, pero el HTML es para **usuarios sin herramientas**, no para
arquitectos.

**b) Descripción detallada por dominio.** Cada dominio debe documentar de
forma estructurada y homogénea:
- **Descripción detallada** (qué es, propósito de negocio).
- **Tipo de elementos** que lo componen.
- **Datos** que gestiona.
- **Actividades** que abarca.
Formalizar estos campos como **obligatorios** en la plantilla del catálogo
(`bounded-context-template.md` / `domain.md`).

**c) Guía de clasificación para nuevos análisis.** Orientación explícita —
usable tanto por un humano como por `apb-agent-ddd-v1.0` /
`apb-sub-ddd-interview-v1.0` — sobre **cómo decidir, ante un dominio nuevo
detectado en un análisis, si es independiente o debe incorporarse a uno
existente** (criterios de frontera: acoplamiento de datos, lenguaje ubicuo
compartido, propiedad/gobernanza, actividades solapadas). Cruce directo con
el "mecanismo anti-duplicación de dominios" (#11) y con la Fase 1-EVO de
`apb-sub-ddd-interview-v1.0` (extensión / nuevo BC / deuda técnica).

**d) Análisis de referencia de dominios típicos.** Elaborar dos catálogos de
referencia que sirvan de base y contraste al inventario APB:
- **Dominios típicos de una empresa** (genéricos: RRHH, finanzas, compras,
  jurídico, IT, CRM, adm. electrónica…).
- **Dominios típicos de un entorno portuario** (buques/escalas,
  consignatarios, atraques, mercancías, aduana/PIF/EQV, GIS portuario,
  concesiones, seguridad marítima, PORTIC/comunidad portuaria…).
Útil para validar que el inventario APB no tiene huecos y para acelerar el
onboarding de dominios en nuevos análisis.

**Cruces (no duplicar):** #38 Fase 0 (catálogo poblado), #54 (banco de
entrevista portuario A + corporativo B — ya contiene mucho material de (d)),
#11 (anti-duplicación de dominios), M.2 (`ddd-crew/context-mapping`).
**Sesión candidata:** ampliación de la línea DDD (Sesión 18 cont. / DDD Fase
BC), tras la aprobación de Arquitectura de los 21 dominios `proposed`. Los
apartados (a) y (d) no dependen de esa aprobación y pueden adelantarse.

---

## L. Fases de evolución del framework a medio/largo plazo

### Fase 1 — Consolidación (0–6 meses)

**Objetivo:** pasar de "framework diseñado" a "framework operativo".

**Indicadores de éxito:**
- ≥30 componentes en estado `approved`, incluyendo los 5 workflows principales
- APB-DOMAIN-CATALOG con ≥5 dominios core `approved`
- Telemetría activa — al menos un evento por sesión de agente en `APBFrameworkTelemetry_CL`
- Runbooks para `wf-sdd-full`, `wf-code-review`, `wf-qa-evidence`
- Primer agente ejecutado desde Teams vía M365 Copilot adapter por usuario no-Arquitectura
- Métrica "% en draft" < 90%

**Riesgos:**
- Ciclo de aprobación como cuello de botella por falta de tiempo. Mitigación: slots recurrentes de 1h semanal de revisión.
- ✅ APB-DOMAIN-CATALOG **desbloqueado (2026-06-30)**: inventario recibido + entrevista estructurada (`apb-sub-ddd-interview-v1.0`) ejecutada → 21 dominios de negocio `proposed`. Pendiente: aprobación de Arquitectura.

### Fase 2 — Adopción corporativa (6–18 meses)

**Objetivo:** el framework pasa a ser la plataforma de referencia usada por múltiples equipos.

**Indicadores de éxito:**
- Rovo Agents activos y usados por equipos de proyecto (no solo Arquitectura APB)
- Todos los proyectos nuevos arrancan con `wf-sdd-full`
- ≥3 proyectos legacy con análisis DDD documentado y aprobado en APB-DOMAIN-CATALOG
- Motor de orquestación real (E-T1) ejecutando ≥1 workflow por semana
- Agente de Change Management / ITIL operativo (E-F1) integrado con el proceso CAB real
- Agente de Data Governance / RGPD produciendo el RAT trimestralmente (E-F2)
- Dashboard de gobernanza en producción (E-G1)
- Métrica "% en draft" < 50%

**Riesgos:**
- Vibe coding sistémico: equipos generan código sin seguir proceso SDD. Mitigación: formación + validación en PR que exija spec previa (`apb-dev-grill-before-code-v1.0`).
- Proliferación sin gobernanza. Mitigación: `apb-agent-meta-builder-v1.0` requiere discovery previo; todo componente nuevo pasa por el proceso de contribución.

### Fase 3 — Madurez y expansión (18–36 meses)

**Objetivo:** el framework es infraestructura corporativa madura, no un proyecto.

**Indicadores de éxito:**
- 80% de componentes en `approved` o `deprecated` — `draft` es la excepción
- Contribuciones de equipos de proyecto al catálogo sin necesitar a Arquitectura como intermediario
- Agente de FinOps con ahorro medible y documentado (E-F3)
- Integración con sistemas core (GISPEM, Portal Docks, etc.) vía providers específicos
- Ciclo de revisión semestral automatizado sin intervención manual (E-G2)
- Metodología o templates publicados como referencia para otras autoridades portuarias
- Métrica "% de skills con reuso >1 agente" > 50%

**Riesgos transversales:**

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| LLM vendor lock-in | Media | Alto | Mantener los 4 adapters actualizados; no hardcodear behavior de un modelo en los prompts |
| Proliferación descontrolada (>500 en draft) | Alta | Medio | Activar proceso de aprobación cuanto antes; ratio máximo draft/approved |
| ~~APB-DOMAIN-CATALOG vacío en 12 meses~~ ✅ MITIGADO (2026-06-30): 21 dominios `proposed` | Baja | Crítico | Aprobación de Arquitectura + experto de negocio para fronteras |
| Obsolescencia de skills de terceros | Alta | Medio | E-S2 (supply chain verification en CI) + revisión anual |
| Resistencia cultural | Media | Alto | ROI con métricas reales desde telemetría; involucrar equipos en los primeros dominios |
| Cambio de modelo de IA | Alta | Bajo | Los adapters abstraen el modelo; actualizar el model string es tarea de horas |

---

## M. Repositorios de terceros de interés

> Evaluación y decisión de Arquitectura APB obligatoria antes de incorporar cualquier componente.
> No evaluar M.8 hasta que los bloqueos críticos (APB-DOMAIN-CATALOG, ciclo de aprobación) estén resueltos.

### M.1 Orquestación (gap E-T1)

| Repositorio | Licencia | Uso propuesto | Esfuerzo |
|-------------|---------|--------------|---------|
| `microsoft/semantic-kernel` | Apache 2.0 | Motor de orquestación multi-agente con soporte nativo Claude + .NET. Wrapper propuesto: `wrap-semantic-kernel-v1.0`. | 2-4 semanas |
| `langchain-ai/langgraph` | MIT | Orquestación con estado persistente y backtracking. Alternativa ligera si el stack .NET no es requisito. | 1-2 semanas |

### M.2 DDD y gestión de dominios (gap Domain Catalog vacío)

| Repositorio | Licencia | Uso propuesto |
|-------------|---------|--------------|
| `ddd-crew/context-mapping` | Verificar antes de usar | Plantillas para Context Mapping DDD. Compatible con `bounded-context-template.md` del Domain Catalog. |
| Metodología Event Storming | Referencia | Complemento para talleres presenciales. Documentar cómo conecta la salida del taller con `new-domain.sh`. |

### M.3 Seguridad y compliance (gaps E-S1, E-S2, E-S3)

| Repositorio | Licencia | Uso propuesto |
|-------------|---------|--------------|
| `aquasecurity/trivy` | Apache 2.0 | Escáner de vulnerabilidades en código, dependencias y manifiestos IaC. Step de CI: `trivy fs .`. También detecta secretos en código. |
| OWASP DevSecOps Guideline | CC BY-SA 4.0 | Controles aplicables a cada fase del SDLC. Material para enriquecer `apb-sec-threat-model-v1.0` y agentes de seguridad. |

### M.4 Observabilidad (gap telemetría no activa)

| Repositorio | Licencia | Uso propuesto |
|-------------|---------|--------------|
| `open-telemetry/opentelemetry-python` | Apache 2.0 | Estándar de industria para trazas distribuidas. Compatible con `DefaultAzureCredential`. Permite envío simultáneo a Azure Monitor y otros backends (Grafana, Jaeger). **✅ Descriptor creado (2026-07-04):** `prov-otel-v1.0` (`draft`, agnóstico OTLP → Azure Monitor). Falta activación real (Plataforma). |

### M.5 Design System (gaps BUG-03, tipografía, mantenibilidad)

| Repositorio | Licencia | Uso propuesto |
|-------------|---------|--------------|
| `storybookjs/storybook` | MIT | Catálogo de componentes UI con ejemplos interactivos, documentación de props generada automáticamente y tests de accesibilidad (addon a11y — WCAG 2.1 AA, RD 1112/2018). Elimina mantenimiento manual de `visual-reference.html`. |

### M.6 Memoria y conocimiento de agentes

| Repositorio | Licencia | Uso propuesto | Estado en catálogo |
|-------------|---------|--------------|-------------------|
| `HKUDS/LightRAG` | Apache 2.0 | RAG + grafos de conocimiento. Memoria episódica entre sesiones (decisiones de arquitectura, lenguaje ubicuo de dominio). Candidato para "memoria corporativa" del framework. | Wrapper existente: `wrap-hkuds-lightrag-v1.0`. Falta desplegar y conectar. |
| `mem0ai/mem0` | Apache 2.0 | Alternativa más simple a LightRAG. SDK Python con backends PostgreSQL/Redis/Qdrant. Más fácil de operar en Azure. | Wrapper pendiente: `wrap-mem0-v1.0` |
| Obsidian (`obsidianmd`) | Freemium (app propietaria; vault = Markdown abierto) | Capa **humana** de navegación sobre la memoria del framework (#80/#81): grafo de backlinks sobre el repo Markdown ya enlazado; visualización de `depends_on`/`consumed_by`. **Solo proyección de lectura** — no fuente de verdad (Principio #4/#6). ✅ **Evaluado (Sesión 19, 2026-07-04): recomendado como herramienta opcional solo-lectura; no editar desde Obsidian (saltaría validador/CI); excluir `.obsidian/` vía `.gitignore` si se abre el repo como vault. Ver #81.** | Herramienta de apoyo, no componente de catálogo |

### M.7 Contratación pública LCSP (gap E-F4)

| Recurso | Uso propuesto |
|---------|--------------|
| Plataforma de Contratación del Sector Público (API REST, Ministerio de Hacienda) | Datos públicos de contratos: precios de referencia, pliegos adjudicados, proveedores habituales APB. Integrable como `prov-lcsp-v1.0` una vez recibido el briefing de Débora. |

### M.8 Repositorios pendientes de evaluación profunda

| Repositorio | Posible uso | Prioridad |
|-------------|------------|---------|
| `ComposioHQ/agent-orchestrator` | Alternativa de orquestación de agentes | Media |
| `ruvnet/ruflo` | Framework de agentes ligero | Baja |
| `affaan-m/ecc` | Pendiente de evaluación | Baja |
| `nexu-io/open-design` | Complemento para Design System | Baja |
| `ComposioHQ/awesome-claude-plugins` | Fuente de discovery de MCPs — no incorporar como componente | Referencia |
| `walkinglabs/learn-harness-engineering` | Modelo de Harness Engineering (12 lecciones) — base del punto #83. Insumo de gobernanza + scaffolding + checks de validación, no componente del catálogo | Alta (#83) |
| Anthropic **cybersecurity skills** | ✅ **Evaluado (Sesión 19):** el repo "Anthropic-Cybersecurity-Skills" es de `mukul975` (fuente ya incorporada, no re-incorporar). El oficial real es `anthropics/defending-code-reference-harness` (Apache 2.0, 6 skills) — **✅ incorporado (OK de Débora, 2026-07-04)** como `third-anthropic-defending-code-v1.0` (`draft`). Ver #79 | Media (#79) |
| "Fine Skills" (fuente a identificar) | Pendiente de URL/organización exacta de Debora (#79) — **único resto abierto del #79 tras Sesión 19** | A determinar |
| `excalidraw/excalidraw` (MIT) | ✅ **Evaluado (Sesión 19).** **Decisión de Débora (2026-07-04): incorporar como MCP en fase futura** → `prov-excalidraw-v1.0` (pizarra/diagramas para skills de arquitectura, complemento de `apb-arch-c4-model`). No incorporado en esta sesión; ligado a caso de uso concreto. | Media — fase futura |

## N. Bloque añadido 2026-07-03 — routing agnóstico (pendiente derivado de Fase H)

Ver `PLAN_FASES_COMPLETADAS.md` → "Fase H" para lo ya ejecutado (creación de `AGENTS.md`,
`.github/copilot-instructions.md`, check #22). Un único pendiente se deriva de esa sesión:

- **Provider de VCS alternativo a GitHub:** hoy `providers/` solo tiene `prov-github-v1.0.md`
  para control de versiones/repo hosting. Esto es un punto distinto del agnosticismo de
  LLM/herramienta (ya resuelto vía `AGENTS.md`) — es agnosticismo de **plataforma de código**.
  Si Débora decide evaluar o migrar a otra plataforma (GitLab, Azure Repos...), haría falta
  un `prov-<plataforma>-v1.0.md` equivalente antes de depender de esa migración. No construir
  hasta que Débora indique una plataforma concreta a evaluar — no hay evidencia de que vaya
  a cambiar de GitHub, solo se deja registrado el gap por si acaso.

---

## O. Bloque añadido 2026-07-03 (Débora) — auditorías de cumplimiento (Design System, calidad) + migración Cloud

### 85. Agente de cumplimiento del Design System (auditoría de app existente + informe + PR opcional) — ✅ EJECUTADO (Sesión 19, 2026-07-04)

**Creado `agents/apb-agent-design-compliance-v1.0.md`** (`draft`, dominio `design`):
escanea el frontend objetivo, compara contra `APB-DESIGN-SYSTEM`
(`apb-design-frontend-design-system-v1.0`) y WCAG 2.1 AA (vía
`apb-qa-accessibility-v1.0` — **no** la deprecada `apb-design-wcag-v1.0`,
detección que originó el check #25 del validador), genera informe MD+HTML con
el patrón de `generate_test_plan_html.py`, y PR opcional vía
`apb-dev-pr-doc-v1.0` (nunca merge). Encadenable al #86 como fuente de
hallazgos. Wiring bidireccional aplicado. **Pendiente de Débora (sin cambios):
repo(s)/carpeta(s) concretas a auditar como primer caso de prueba.**
Detalle en [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).

<details><summary>Planteamiento original (histórico)</summary>

**Petición de Débora:** "agente que revisa si una aplicación cumple con sistema de diseño, hace
informe y sugiere correcciones, da opción de preparar PR."

**Distinto del punto #53:** #53 verifica que el agente **generador** de mockups (`apb-agent-ux-mockup-v1.0`)
use el Design System en tiempo de creación. Este punto #85 es un **auditor a posteriori**: revisa una
aplicación **ya construida** (código frontend existente, propio o legacy) contra `APB-DESIGN-SYSTEM`
(tokens, componentes, tipografía, `component-reference.md`, `style-guide.md`), sin importar cómo se generó.

**Comportamiento deseado:**
1. Escanea el código frontend de la app objetivo (rutas de entrada: repo o carpeta a indicar por Débora/funcional).
2. Compara contra `APB-DESIGN-SYSTEM` (tokens de color/tipografía/espaciado, componentes React/DevExtreme
   con wrapper corporativo) — reutiliza como referencia `skills/apb-owned/design/apb-design-frontend-design-system-v1.0.md`
   y `apb-design-wcag-v1.0` (accesibilidad, incumplimientos WCAG también entran en el informe).
3. Genera **informe** de incumplimientos (formato corporativo, coherente con el patrón ya construido en
   `scripts/generate_test_plan_html.py`: cabecera azul, menú, acordeón — reutilizable en vez de reinventar).
4. Sugiere correcciones concretas por incumplimiento.
5. **Opción de preparar PR** con las correcciones — reutilizar `apb-dev-pr-doc-v1.0` para la propuesta;
   nunca merge automático (POLICY_AI_USAGE §6-7, mismo patrón que `apb-sub-qa-fix-loop-v1.0` de Fase I).

**Componentes a crear (draft):** posible `agents/apb-agent-design-compliance-v1.0.md` (o skill si el
alcance es más acotado — decidir en la sesión) + wiring con `apb-dev-pr-doc-v1.0`.

**Pendiente de Débora:** repo(s)/carpeta(s) concretas a auditar como primer caso de prueba.

</details>

---

### 86. Agente de cumplimiento de calidad — Sonar + hallazgos de otros agentes + Jira + PR opcional — ✅ EJECUTADO (Sesión 19, 2026-07-04)

**Creado `agents/apb-agent-quality-compliance-v1.0.md`** (`draft`, dominio `qa`):
multi-fuente (Sonar vía `apb-dev-sonar-clean-v1.0` + informes de otros agentes
+ lista del usuario, con procedencia declarada), **dedup obligatorio contra
Jira** (`prov-jira-software-v1.0`: si el hallazgo ya tiene ticket, se
referencia, no se duplica), correcciones concretas por hallazgo y **PR
opcional** tras OK humano reutilizando el patrón de `apb-sub-qa-fix-loop-v1.0`
vía `apb-dev-pr-doc-v1.0` — sin re-parentar ni duplicar el subagente (decisión
de la nota de diseño: mismo flujo de salida, distinto trigger). Wiring
bidireccional aplicado (`consumed_by` en sonar-clean, pr-doc,
telemetry-emit). Detalle en [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).

<details><summary>Planteamiento original (histórico)</summary>

**Petición de Débora:** "agente que analiza los incumplimientos de sonar o los detectados por otros
agentes y sugiere las correcciones. Los incumplimientos pueden estar ya registrados en Jira. Prepara
pull request con las correcciones de forma opcional."

**Punto de partida ya existente:** `skills/apb-owned/development/apb-dev-sonar-clean-v1.0.md` ya
analiza hallazgos de SonarQube y sugiere/aplica fixes — **pero solo cubre Sonar como fuente**, no
comprueba si el hallazgo ya está en Jira (riesgo de duplicar tickets), y no prepara PR.

**Huecos a cubrir (extender la skill a v2.0, o envolverla en un agente si necesita orquestar varias
fuentes):**
1. **Multi-fuente:** aceptar hallazgos no solo de Sonar sino de otros agentes/skills del framework
   (p. ej. `apb-agent-security-architect`, ZAP, el propio #85 de Design System, code review).
2. **Dedup contra Jira:** antes de proponer una corrección, consultar `prov-jira-software-v1.0` para
   comprobar si el incumplimiento ya tiene ticket abierto — si existe, referenciarlo en vez de duplicar.
3. **PR opcional:** reutilizar el mismo patrón `apb-sub-qa-fix-loop-v1.0` (Fase I, 2026-07-03): propone
   PR vía `apb-dev-pr-doc-v1.0`, anota Jira, nunca mergea sin revisión humana.

**Nota de diseño:** el sub-workflow `apb-sub-qa-fix-loop-v1.0` ya resuelve el patrón genérico
"hallazgo → PR propuesta → anotación Jira" para el caso de fallos de pruebas; valorar en la sesión si
este punto #86 puede **reutilizar ese mismo subagente** en vez de construir uno nuevo desde cero
(cambiaría el trigger de "test falla" a "hallazgo de calidad/Sonar/otro agente", pero el flujo de
salida — PR + Jira — es el mismo).

**Pendiente de Débora:** ninguna dependencia bloqueante conocida; puede diseñarse en modo `draft` como
el resto de componentes de esta sesión.

</details>

---

### 87. Flujo completo de migración a Cloud con pasos definidos por APB

**Petición de Débora:** "flujo completo para evaluar y ejecutar migración a Cloud con los pasos
definidos por APB. Yo te indicaré los pasos y tú enriqueces si es necesario."

**Ya existe un workflow genérico:** `workflows/apb-wf-cloud-migration-v1.0.md` — fases y agentes
(cloud architect, technical architect, security architect, platform engineer, QA, SRE, FinOps,
governance, release/change manager) con checkpoints humanos, pero con **pasos genéricos de industria**,
no el proceso concreto que usa APB.

**Acción pendiente:** cuando Débora aporte los pasos concretos definidos por APB (evaluación +
ejecución de migración a cloud), revisar/reescribir las fases de `apb-wf-cloud-migration-v1.0` para
que reflejen ese proceso real, enriqueciendo solo donde falte un paso evidente (p. ej. checkpoint de
aprobación, validación de coste, rollback) sin inventar un proceso paralelo al de APB.

**Pendiente de Débora (bloqueante):** los pasos concretos del proceso de evaluación/migración a Cloud
de APB. Sin este insumo no se puede iniciar la sesión — es un insumo de tipo "briefing" equivalente a
los ya listados en `discovery/HANDOFF_TECNICOS.md §10`.

### 88. Reejecución completa del plan TruckCenter con vídeo real (Playwright MCP) + corrección de H1

**Origen:** continuación del punto #84 (sesión QA TruckCenter, 2026-07-03). Tras ejecutar 44/120 casos con
2 hallazgos críticos (H1/H2 en Tabla Maestra de Vehículos) y corregir la metodología de informes
(`TEST_PLAN_STANDARD` v1.4.0, ver #84), quedan pendientes:

1. **Reiniciar/reabrir Claude Code sobre el repo** para que el servidor Playwright MCP (recién registrado
   en `.mcp.json` de proyecto) quede disponible como herramienta — no se carga en caliente dentro de una
   sesión ya iniciada.
2. **Confirmar el commit** de `.mcp.json` + `providers/prov-playwright-v1.0.md` v1.1.0 (pendiente de OK de
   Débora, hecho en la sesión anterior sin commitear aún).
3. **Corregir H1 en TruckCenter** (repo de la app, fuera de este framework): añadir validación de
   integridad referencial antes de permitir eliminar un Tipo de Vehículo en uso. Prioridad alta — el
   defecto ya está materializado en PRE (tipo "Cisterna" eliminado con 4 expedientes huérfanos).
4. **Reejecutar el plan completo de TruckCenter** (120 casos) con vídeo real por bloque vía Playwright MCP:
   los 76 casos restantes de la sesión anterior (B01 vía API, B08/B09/B10 completos con un segundo
   usuario/rol — incluido uno con permiso de "Auditoría de procesos", B02-B07 exhaustivo) + B11 (SonarQube/
   ZAP)/B13 (k6, en `azure-qa`/`ci-runner`, nunca portátil)/B14 (xUnit, repo `APB.TRU`) según corresponda a
   cada herramienta (plan §6).

**Bloqueantes:** (1) y (2) son de esta misma máquina/sesión (no requieren a Débora salvo el OK de commit);
(3) requiere acceso al repo `APB.TRU` (fuera del framework); (4) requiere login EntraID asistido de Débora
de nuevo, igual que en la sesión anterior. **Sesión candidata:** continuación directa de QA-2/#84, no
sesión nueva — mismo hilo de trabajo.

</details>

---

### 89. Auditoría de cableado agente/subagente↔skill/provider + 2 checks nuevos en `validate_repo.py` — ✅ EJECUTADO (Sesión 26, 2026-07-06)

**Origen:** Débora detectó que el informe de riesgos `INFORME_RIESGOS_ARQ-3684_APB.API.FIL.md`
citaba `PROCEDURE_NONCOMPLIANCE_MANAGEMENT_v1.0` en la cabecera pero no aplicaba su contenido real
(ticket maestro JSM §8.7, justificación de negocio §9.1, flujo de 3 aprobaciones §9.3, tabla de
plazos §10) — mientras que `PROCEDURE_RISK_EVALUATION`, citado en el mismo prompt con un paso
"Aplica" explícito, sí se aplicó a fondo. Pidió revisar si el mismo patrón de fallo se repetía en
otros agentes/skills y que se implementara un mecanismo permanente para que no se repitiera.

**Ejecutado:**
1. **Causa raíz corregida en `apb-gov-org-risk-report-v1.0`** (v1.3.0 → v1.4.0): rutas literales a
   ambos procedimientos + paso 7 nuevo (checklist de 4 puntos) en el Prompt de Sistema + 2 preguntas
   nuevas en la entrevista de contexto.
2. **`validate_repo.py` check #27:** ningún `PROCEDURE_*` puede nombrarse en un componente sin su
   ruta literal en el mismo fichero. Corregidos `apb-plat-ci-qa-gate-v1.0` (v1.0.1) y una instancia
   nueva detectada en caliente al escribir la corrección de `apb-agent-risk-exception-v1.0` (v1.1.0,
   que además ganó una sección "Relación con otros componentes" aclarando que no tiene asignada
   `apb-gov-org-risk-report-v1.0` — el informe ARQ-3684 se había atribuido al agente equivocado).
3. **Auditoría manual de los 38 agentes + 35 subagentes** (script ad-hoc comparando IDs mencionados
   en el bloque "Prompt de Sistema" contra `skills:`/`depends_on:` declarados, excluyendo referencias
   cruzadas legítimas entre agentes/subagentes — confirmado empíricamente que esas SÍ son mayoría
   falsos positivos). **6 gaps reales** corregidos: `apb-agent-business-analyst-v1.0` (v1.0.1,
   `apb-qa-anonymize-v1.0`), `apb-agent-compliance-audit-v1.0` (v1.2.0, `apb-plat-doc-to-markdown-v1.0`
   + `prov-atlassian-v1.0` + `prov-ms365-v1.0`), `apb-agent-finops-v1.0` (v1.0.1, `prov-azure-cost-v1.0`
   — y nota "Gap conocido" corregida, el provider ya existe desde el 29/6), `apb-agent-observability-v1.0`
   (v1.0.1, `prov-azure-monitor-v1.0`), y los subagentes `apb-sub-ops-azure-v1.0`/`apb-sub-obs-powerbi-v1.0`
   (v1.0.1 ambos).
4. **`validate_repo.py` check #28:** generaliza el #27 a cualquier skill/provider (no solo
   `PROCEDURE_*`) usado en el Prompt de Sistema de un agente o subagente sin declarar. Excluye
   deliberadamente menciones de tipo `agent`/`subagent`.
5. **`SCHEMA.md` v1.0.0 → v1.1.0:** formaliza `skills`/`depends_on` como campos condicionales de
   `Subagent` (§3.3) — antes eran convención informal sin respaldo en el schema; el check #28 ahora
   escanea también `subagents/`.

**Verificación:** `validate_repo.py --strict` → 0 errores en cada paso · 60/60 tests · catálogo
regenerado sin huecos.

**Informe ARQ-3684 corregido a v3** (ver `discovery/examples/INFORME_RIESGOS_ARQ-3684_APB.API.FIL.md`):
atribución de agente corregida, ticket maestro JSM y justificación de negocio marcados
explícitamente como pendientes de confirmar (sin inventarlos), flujo de 3+1 aprobaciones y tabla de
plazos aplicados.

**Pendiente de Débora:** ninguna — cerrado en la misma sesión.

---

### 90. Agente de soporte técnico para analistas funcionales — ✅ EJECUTADO (Sesión 26, 2026-07-06)

Petición original y decisiones de diseño documentadas en
[`PLAN_FASES_FUTURAS.md`](PLAN_FASES_FUTURAS.md) (fila marcada `✅ CREADO`). Resumen:

**Creado `agents/apb-agent-functional-technical-support-v1.0.md`** (reescritura del borrador previo,
que no seguía las convenciones del repo: `review_date: pending` inválido, campos de frontmatter
inexistentes en el schema `agents:`/`created_by`, Prompt de Sistema como prosa suelta) + skill nueva
`skills/apb-owned/pm/apb-pm-jira-estimation-review-v1.0.md` (dominio `pm`) que sustituye la
dependencia inadecuada de `apb-dev-code-review-v1.0` (revisión de código C#/.NET ya escrito, no
estimación a partir de la descripción de un ticket).

**Decisiones de Débora incorporadas:** búsqueda de precedentes híbrida (Jira en vivo siempre +
catálogo del repo `discovery/ESTIMATION_REFERENCES.md` como referencia rápida a partir de ≥20
entradas por categoría); unidad de estimación en **horas** (no story points); acceso a Jira vía
`prov-jira-software-v1.0` (REST API específica de Jira Software, no MCP ni Rovo —
`search_issues`/JQL más preciso que `prov-atlassian-v1.0` para este caso, ver punto #91); regla de
contrapropuesta al superar el **+25%** de la media de precedentes comparables, con argumentos
citados (no dispara por infra-estimación, solo se reporta como observación).

**Verificación:** `validate_repo.py --strict` → 0 errores · 60/60 tests · catálogo regenerado
(183 skills `apb-owned`, +1).

**Pendiente:** acceso real a histórico Jira (`HANDOFF_TECNICOS.md` ACC1) — el componente ya es
operativo, falta el aprovisionamiento de credenciales para probarlo en runtime real. La
reconciliación de `prov-atlassian-v1.0`/`prov-jira-software-v1.0` marcada aquí se resolvió en la
misma sesión — ver punto #91.

---

### 91. Reconciliación de providers Atlassian (`prov-atlassian-v1.0` / `prov-jira-software-v1.0`) — ✅ EJECUTADO (Sesión 26, 2026-07-06)

**Origen:** al crear #90, se detectó que `prov-atlassian-v1.0` se llamaba *"Provider: Atlassian
Rovo MCP"* pero su contenido documentado siempre fue una integración REST CRUD genérica — sin
relación real con el protocolo MCP ni con Rovo. Esto generaba una duplicidad confusa con
`prov-jira-software-v1.0` (también REST, específico de Jira Software con JQL/`search_issues` mejor
documentado). Débora pidió la reconciliación explícitamente.

**Hallazgo adicional durante la investigación:** existe `adapters/rovo/adapter-rovo-v1.0.md`
(Sesión 15, 2026-06-24) que documenta la integración *real* de Rovo — búsqueda semántica, Rovo
Agents expuestos en Jira/Confluence vía Forge App — como componente **aparte**, pendiente de
activación en el tenant Atlassian de APB (previsto julio 2026, ver `HANDOFF_TECNICOS.md §4`). Ni
`prov-atlassian-v1.0` ni `prov-jira-software-v1.0` usan MCP ni Rovo como transporte — ambos son
REST puro. La afirmación "acceso vía conector MCP de Atlassian (Rovo)" que se había escrito en el
punto #90 (skill, agente y entradas de `PLAN_FASES_FUTURAS.md`/`CONTINUIDAD_PROYECTO.md`) era
incorrecta y se corrigió en todos esos ficheros en esta misma sesión.

**Ejecutado:**
1. **Renombrado `prov-atlassian-v1.0`** de "Atlassian Rovo MCP" a "Atlassian REST API (JSM +
   Confluence + Compass)" (v1.1.0) — su alcance se acota explícitamente a Jira Service Management,
   Confluence y Compass (no Jira Software/backlog, competencia de `prov-jira-software-v1.0`).
2. **Tabla de diferenciación** añadida a ambos providers (`prov-atlassian-v1.0` §"Diferencia con
   otros componentes Atlassian"; nota espejo en `prov-jira-software-v1.0`, v1.1.0) distinguiendo los
   3 componentes relacionados: `prov-atlassian-v1.0` (JSM/Confluence/Compass), `prov-jira-software-v1.0`
   (Jira Software/JQL) y `adapter-rovo-v1.0` (capa de IA, pendiente de activación).
3. **Corregidas las 3 afirmaciones erróneas sobre MCP/Rovo** introducidas en el punto #90:
   `apb-pm-jira-estimation-review-v1.0` (v1.0.1), `apb-agent-functional-technical-support-v1.0`
   (changelog), `PLAN_FASES_FUTURAS.md:74` y `CONTINUIDAD_PROYECTO.md` (Sesión 26).

**Alcance deliberadamente NO cubierto en este punto:** no se fusionó ni deprecó ninguno de los dos
providers en este momento de la sesión — ambos tenían consumidores reales activos y fusionarlos
habría significado tocar ~15 ficheros más sin que hubiera (todavía) un defecto funcional real.
**Superado más adelante en la misma sesión:** Débora pidió explícitamente la fusión — ver punto #92.

**Verificación:** `validate_repo.py --strict` → 0 errores · 60/60 tests.

**Pendiente de Débora:** ninguna en este punto — la fusión real se ejecutó a continuación, #92.

---

### 92. Fusión real de `prov-jira-software-v1.0` en `prov-atlassian-v1.0` + revisión de `adapter-rovo-v1.0` — ✅ EJECUTADO (Sesión 26, 2026-07-06)

**Petición de Débora:** "fusiona los providers. también asegúrate que el adapter para rovo es
correcto. necesitamos el mcp de atlassian + rovo?" — tras el punto #91, que solo había
diferenciado sin fusionar.

**Ejecutado:**
1. **`prov-atlassian-v1.0` → v2.0.0:** absorbe todas las acciones de `prov-jira-software-v1.0`
   (`get_issue`, `search_issues`/JQL, `add_to_sprint`, `link_issues`, `get_backlog`, `get_sprint`,
   etc.). `prov-jira-software-v1.0` marcado `status: deprecated` con `deprecated_reason` (patrón
   ya usado en el repo, p. ej. `apb-design-wcag-patterns-v1.0`) — el check #25 de
   `validate_repo.py` bloquea automáticamente cualquier wiring nuevo hacia él.
2. **Hallazgo durante la fusión, no detectado en #91:** `prov-atlassian-v1.0` v2.0.0 incluía
   también una tabla de acciones de Confluence — duplicando sin necesidad `prov-confluence-v1.0`,
   un tercer provider ya existente (2026-06-29) con acciones mucho más completas (`move_page`,
   `delete_page`, `get_space`, `attach_file`, etc.). Corregido en v2.1.0: `prov-atlassian-v1.0`
   queda acotado a Jira (Software + JSM) + Compass ligero; Confluence se delega enteramente en
   `prov-confluence-v1.0`, con tabla de relación explícita entre los 3 componentes.
3. **10 ficheros consumidores actualizados** (`depends_on` frontmatter + prosa): 3 con wiring
   formal detectado automáticamente por el check #25 al deprecar
   (`apb-pm-jira-estimation-review-v1.0`, `apb-agent-quality-compliance-v1.0`,
   `apb-sub-qa-fix-loop-v1.0`) + 7 con mención solo en prosa
   (`TEST_PLAN_STANDARD.md`, `TEST_PLAN.md`, `apb-qa-test-plan-v1.0.md`,
   `third-mattpocock-triage-v1.0.md`, y los workflows `apb-wf-problem-management-v1.0`,
   `apb-wf-qa-evidence-v1.0`, `apb-wf-security-patch-v1.0`).
4. **`adapter-rovo-v1.0` revisado y corregido (v1.1.0):** su tabla de diferenciación citaba a
   `prov-atlassian-v1.0` cubriendo Confluence (ya no cierto tras la corrección del punto 2);
   añadido `prov-confluence-v1.0` a `adapted_components` y como credencial correcta para las
   llamadas Rovo sobre Confluence (antes decía, incorrectamente, que todo usaba el token de
   `prov-atlassian-v1.0`). El resto del adapter (Forge App, Rovo Agents expuestos, límites,
   activación pendiente julio 2026) ya era correcto.
5. **`adapter-claude-v1.0` corregido (v1.2.0):** tenía un hueco real — Azure/GitHub/Sonar
   aparecían mapeados a MCP explícitamente, Atlassian no aparecía en absoluto. Añadido como
   "⚠️ Parcial" (REST directo, sin conector MCP de Atlassian confirmado en este runtime a fecha
   2026-07-06) en vez de darlo por hecho.

**Respuesta a "¿necesitamos el MCP de Atlassian + Rovo?":** son dos cosas distintas que no
compiten entre sí. (a) **MCP de Atlassian** — mecanismo de transporte (framework → Atlassian)
que sustituiría el REST directo actual de `prov-atlassian-v1.0`/`prov-confluence-v1.0` si el
tenant APB expone un servidor MCP; no se ha podido confirmar su disponibilidad concreta en este
entorno de sesión (sin conector instalado, búsqueda en el registro MCP sin resultados) — queda
anotado como "⚠️ Parcial" en `adapter-claude-v1.0` hasta confirmarlo. (b) **Rovo** —
`adapter-rovo-v1.0`, capa de IA de Atlassian con dos direcciones: framework invocando búsqueda
semántica/análisis de Rovo, y agentes del framework expuestos dentro de Jira/Confluence como
Rovo Agents (Forge App) — un propósito totalmente distinto al de mover datos CRUD, pendiente de
activación en APB (julio 2026). Ambos son necesarios si se activan: no son alternativas entre
sí, cubren direcciones de integración diferentes.

**Verificación:** `validate_repo.py --strict` → 0 errores (incluye 1 gap documentado
`prov-compass-v1.0`, mención a futuro, no bloqueante) · 60/60 tests · catálogo regenerado.

**Pendiente de Débora:** confirmar si existe/se activará un servidor MCP de Atlassian real en el
tenant APB, para pasar `prov-atlassian-v1.0`/`prov-confluence-v1.0` de "⚠️ Parcial" a "✅ MCP" en
`adapter-claude-v1.0`.

---

## Wiring de 5 subagentes — ✅ VERIFICADO (2026-07-07)

`PLAN_FASES_FUTURAS.md` marcaba como pendiente el wiring de 5 subagentes (origen R2,
revisión 360° 2026-06-29): `apb-sub-ops-entra-v1.0`, `apb-sub-sec-sast-v1.0` →
`apb-agent-security-architect-v1.0`; `apb-sub-qa-performance-v1.0` →
`apb-agent-qa-auto-v1.0`; `apb-sub-finops-azure-v1.0` → `apb-agent-finops-v1.0`;
`apb-sub-gov-data-v1.0` → `apb-agent-data-governance-v1.0`.

Verificación directa de frontmatter (inspección de cada fichero en `subagents/` y de sus
agentes padre en `agents/`) confirmó que el wiring **ya existía** en ambos sentidos:
cada subagente declara el `parent_agent` correcto, y cada agente padre ya lo lista en su
propio array `subagents:`. La entrada original del backlog quedó desactualizada respecto
al estado real del repo — no requirió ninguna edición de código, solo la corrección del
propio plan (movida aquí y tachada en `PLAN_FASES_FUTURAS.md`).
