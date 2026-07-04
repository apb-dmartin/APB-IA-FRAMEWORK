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

**Bloqueado (no construido):** activación MCP Graph real de #30 (requiere tenant/credenciales M365 — Plataforma).

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
11, bajó por las 2 re-identificaciones), tests verdes, plan y memoria actualizados. **Sin push**
en ninguno de los dos repos (`APB-IA-FRAMEWORK` ni `APB-DOMAIN-CATALOG`) — pendiente de
confirmación explícita de Débora.

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
