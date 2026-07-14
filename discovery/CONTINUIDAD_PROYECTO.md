# CONTINUIDAD DEL PROYECTO — APB-IA-FRAMEWORK

> Generado al cierre de la Sesión 6 (CI/CD), actualizado al cierre de la
> Sesión 7 (huecos estructurales y cierre final), de la Sesión 8
> (auditoría de cobertura), de la Sesión 9 (terceros §8), de la Sesión 10
> (meta-gobernanza), de la Sesión 11 (deuda técnica ampliada), de la
> Sesión 12 (AI Risk Gate) y de la Sesión QA (fusión con `apb-ai-skills`,
> ahora deprecado). Léeme primero si retomas este trabajo en una
> conversación nueva: resume el estado exacto, lo ejecutado, lo pendiente,
> y las decisiones de Debora que deben respetarse.
>
> **Nota de corrección (post-Sesión QA):** este documento estuvo
> desactualizado durante un tiempo — las Sesiones 10, 11, 12 y QA se
> ejecutaron y cerraron en conversación, pero esta bitácora no se
> actualizó hasta después de generar el primer zip de migración a Claude
> Code. Si una instancia de Claude Code leyó este documento antes de esta
> corrección, habrá visto esas sesiones marcadas como "❌ Pendiente"
> incorrectamente. Esta es la versión corregida.

## 0. Qué es este zip

Es la **foto completa del repositorio** `apb-dmartin/APB-IA-FRAMEWORK`,
reconstruida sesión a sesión a partir de:
1. El repo real descargado de GitHub (`APB-IA-FRAMEWORK-main.zip`).
2. Un zip de trabajo paralelo (`apb-ai-framework_v1.zip`) con contenido que
   nunca llegó a fusionarse al repo de GitHub (dominios `qa`, `platform`,
   `security`, `operation` completos, y 13 skills sueltas).

**Nota Sesión 7 (importante):** el repositorio real en GitHub
(`apb-dmartin/APB-IA-FRAMEWORK`) avanzó en paralelo con commits propios de
Debora ("session-6b", "session-6c", y un commit del 22-jun con skills nuevas
como `atomic-plan`, `mitre-mapping`) que **no corresponden a este plan de
sesiones**. Debora confirmó explícitamente que la fuente de verdad para la
continuidad de este trabajo es **este zip local**, no el estado de GitHub.
Cualquier instancia de Claude que retome este trabajo debe partir de este
zip, no clonar y confiar en el repo remoto sin antes confirmarlo con Debora.

**Acción al recibir este zip:** sustituir el contenido actual del repo de
GitHub por el contenido de este zip (es la versión consolidada y corregida).

## 1. Estado de las sesiones del plan

| # | Sesión | Estado |
|---|---|---|
| 0 | Fundamentos de automatización (validador + esquema YAML) | ✅ Completa |
| 1 | Auditoría y fusión de duplicados (repo principal) | ✅ Completa |
| 1.5a | Triage del zip paralelo | ✅ Completa |
| 1.5b | Fusión de 3 agentes en conflicto | ✅ Completa (resultado: sin acción, ya estaban fusionados) |
| 1.5c | Incorporación de dominios qa/platform/security/operation/pm | ✅ Completa |
| 2 | Normalización de nomenclatura y frontmatter YAML | ✅ Completa |
| 3 | Reconciliación de catálogos (generación automática) | ✅ Completa |
| 4 | Validador completo y robusto | ✅ Completa |
| 5 | Gobernanza de terceros (source_commit, descriptores) | ✅ Completa |
| 6 | CI/CD (GitHub Action) | ✅ Completa — `.github/workflows/validate.yml` ya creado y verificado |
| 7 | Huecos estructurales (`tests/`, `docs/`) y cierre final | ✅ **Completa** — ver sección 4 |
| 8 | Auditoría de cobertura (checklist `proyecto.md`, comparación GitHub/zips, limpieza skills "BMAD") | ✅ **Completa** — ver sección 9 |
| 9 | Terceros (patrón + revisión repos `proyecto.md` §8) | ✅ **Completa** — ver sección 9 |
| 10 | Agente meta-gobernanza | ✅ **Completa** — ver sección 10 |
| 11 | Sonar + incidencias técnicas (+ posible deuda técnica/Jira, punto #25) | ✅ **Completa** — ver sección 11 |
| 12 | Análisis de riesgos para validación Ciber/Arq/QA | ✅ **Completa** — ver sección 12 |
| QA | Testing — auditoría `apb-ai-skills`, resolver solape | ✅ **Completa** — ver sección 13 |
| Frontend | Mockups, generación frontend, catálogo de componentes | ✅ **Completa** |
| Design System | Sistema de diseño APB sobre DevExtreme — repo propio `APB-DESIGN-SYSTEM` | ✅ **Completa** (v1.3.0, 2026-06-26) |
| 15 | Integraciones Microsoft + gaps Rovo / M365 Copilot | ✅ **Completa** (2026-06-26) — artefactos en `openapi/`, `forge/`, `docs/`. Pendiente de equipo APB: ver `discovery/HANDOFF_TECNICOS.md §4` |
| 16 | Skill de análisis de riesgos con procedimientos APB | ✅ **Completa** (2026-06-24) — `apb-gov-org-risk-report-v1.0` v1.2.0. Multi-framework (ENS, ISO 27001, NIST CSF 2.0, OWASP, RGPD, LCSP, WCAG 2.1 AA), recomendación APROBAR/DENEGAR/ESCALAR, plan de mitigación, alineado con `PROCEDURE_RISK_EVALUATION` + `PROCEDURE_NONCOMPLIANCE_MANAGEMENT_v1.0` |
| 13 | Cierre de pendientes históricos (plantillas, Jira, COSMIC, DDD, loops, guía agentes) | ⚠️ **Parcial** (2026-06-26, 7/10) — bloqueados: #6 (ejemplos Word/Excel de Débora), #8 (horas COSMIC históricas de Débora), #52 (mail Jira de Arquitectura) |
| 22/#47bis | Taxonomía de capacidades en agentes y skills | ✅ **Completa** (2026-06-26) — taxonomía APB normalizada en frontmatter |
| 18/#54 | Subagente entrevista DDD → análisis funcional completo | ✅ **Completa** (2026-06-26) — `apb-sub-ddd-interview-v1.0` v1.3.0: vocabulario portuario (Banco A) + corporativo (Banco B: RRHH, viajes, contratación, adm. electrónica, finanzas, jurídico), Fase 1-INT (integración entre sistemas), Fase 1-EVO (evolutivo de app existente), Fase 5 verificación APB-DOMAIN-CATALOG, Fase 6 generación artefacto |
| 23/#43 | Marcado IA obligatorio — retroactivo + mecanismos preventivos | ✅ **Completa** (2026-06-26) — 129/129 skills `apb-owned` marcadas con sección `## Marcado IA obligatorio (POLICY_AI_USAGE §6)`. Estándar: `context/apb/standards/AI_MARKING_STANDARD.md` (9 tipos de artefacto: código, SQL, OpenAPI, PR, Jira, Markdown, Word/PPT, email/Teams, IaC). Mecanismos preventivos duraderos: check #13 en `validate_repo.py` (ERROR si falta), sección en templates `SKILL_APB.md` y `AGENT.md`. Mecanismo IA: `CLAUDE.md` en raíz del repo. |
| 21 | SQL + incidencias técnicas + Backlog M1-M6 (Enriquecimiento D) | ✅ **Completa** (2026-06-29) — `apb-agent-db-v1.0`, `apb-agent-pm-v1.0`, `apb-orch-context-handoff-v1.0`, `apb-orch-human-checkpoint-v1.0`, `apb-design-wcag-v1.0`. 5 nuevos componentes + 14 modificaciones. M1-M6 resueltos. |
| DDD/#38 F0 | Análisis de dominios sobre inventario APIM → poblar APB-DOMAIN-CATALOG | ✅ **Completa (2026-06-30)** — `API_INVENTORY_APIM.md` (~118 APIs) → 21 dominios de negocio `proposed` en `APB-DOMAIN-CATALOG/domains/`. Artefactos en `ddd-discovery/`. **Pendiente:** PR + aprobación de Arquitectura; fronteras de negocio (Escalas/Cruceros/Líneas, INS/PIF, MDE/OPS, FER). **Diferido:** bounded contexts (requiere acceso a código/BBDD). |
| 14 | Documentación por audiencias (Word) | ❌ Pendiente |
| KB+SP | Knowledge Base corporativa + system prompts LLM-agnósticos | ✅ **Completa** (2026-06-30) — ver §21 |

## 2. Decisiones de Debora que deben respetarse (no reabrir sin pedirlo)

- **Refactorización de fondo**, no limpieza mínima: unificar nomenclatura,
  fusionar duplicados, reescribir frontmatter de todo. (Confirmado al inicio.)
- **Gobernanza de terceros: prioridad media**, no bloqueante sobre el resto.
- **Debora prepara/aplica los cambios finales manualmente** (yo preparo
  archivos, no hago push directo a GitHub).
- **`source_commit` sin acceso de red verificado** → usar
  `"unverified"` + `verified_date: "YYYY-MM-DD"`, nunca inventar un SHA.
  Refinar a SHA real cuando el equipo tenga `git ls-remote` disponible.
- **CI/CD: bloquear el PR si hay drift de catálogo**, NUNCA auto-commit.
  El autor del PR regenera localmente con `scripts/generate_catalog.py` y
  sube el resultado.
- **Esquema YAML único obligatorio** para los 7 tipos de componente,
  documentado en `context/apb/SCHEMA.md` — es la fuente de verdad.
- **`validate_repo.py --strict` exento de warnings `source_commit:
  unverified`** (decisión Sesión 7, formalizada en `GOVERNANCE.md` §4.2):
  cualquier otro warning sigue bloqueando en modo estricto; solo este tipo
  específico está exento, porque exigir su resolución bloquearía el repo
  indefinidamente por falta de acceso de red, no por un defecto real.
- **`fix-apb-brand.sh` / `.ps1` eliminados** (decisión Sesión 7, no
  archivados) — ya cumplieron su función de corrección puntual de marca.
- **Convención de entrega de zips (decisión Sesión 8, vigente para todas
  las sesiones futuras):** cada zip que se entregue a Debora debe contener
  el **repositorio completo**, no solo los archivos modificados en la
  sesión. Debora sustituye su repo de GitHub eliminando todo y subiendo el
  contenido del zip tal cual — por tanto, omitir cualquier archivo
  (modificado o no) provoca pérdida real de contenido en su repo. Antes de
  empaquetar, verificar que el zip contiene el árbol completo de
  `APB-IA-FRAMEWORK/`, no un subconjunto.

## 3. Cómo verificar el estado del repo (primer comando a ejecutar)

```bash
pip install pyyaml --break-system-packages
python3 scripts/validate_repo.py --strict   # esperado: 0 errores, ✅ VALIDACIÓN EXITOSA
python3 scripts/generate_catalog.py --check # esperado: exit 0, sin drift
python3 -m unittest tests.test_validate_repo -v  # esperado: 19/19 OK
```

Si estos tres comandos no dan ese resultado, algo se perdió en el traspaso
del zip — revisar antes de continuar con cualquier sesión futura.

## 4. Sesión 7 — qué se hizo (cerrada)

- Creado `tests/test_validate_repo.py`: 19 tests de dogfooding sobre
  fixtures sintéticos aislados (no toca el repo real). Cubre
  `parse_frontmatter`, patrones de secretos/marca antigua/IPs,
  `iter_component_files`, `validate_references` (frontmatter = ERROR, cuerpo
  = WARNING), `validate_no_circular_dependencies`, y la nueva
  `is_policy_exempt_warning`.
- Creado `docs/sdd-getting-started.md`: cierra la referencia rota desde
  `README.md`. Documenta el ciclo SDD completo, cómo invocar agentes
  (`scripts/invoke_agent.py`), y cómo mantener el catálogo sincronizado.
- Eliminados `fix-apb-brand.sh` y `fix-apb-brand.ps1` de la raíz (decisión
  explícita de Debora: eliminar, no archivar).
- Resueltas las 5 referencias rotas reales detectadas como warning
  (Grupo C, ver histórico de validación):
  - Creado `agents/apb-agent-code-reviewer-v1.0.md` (gap real: dos skills lo
    citaban como agente consumidor sin que existiera).
  - Creado `providers/prov-akv-v1.0.md` (Azure Key Vault, provider tipo
    `secret` — citado en Principio Fundamental #9 y por
    `apb-agent-business-analyst-v1.0`, nunca formalizado).
  - Creado `skills/third_party/third-mattpocock-grill-prd-issues-v1.0.md`
    (verificado por búsqueda web: repo real es `mattpocock/skills`, MIT,
    flujo `grill-me → to-prd → to-issues`).
  - Creado
    `skills/third_party/third-mattpocock-codebase-architecture-analysis-v1.0.md`
    (mismo repo origen, skill `improve-codebase-architecture`).
  - Creado `skills/third_party/third-lum1104-knowledge-graph-v1.0.md`
    (repo `Lum1104/Understand-Anything` / fork `Egonex-AI/Understand-Anything`)
    — ⚠️ **licencia NO verificada** (al menos una fuente externa reporta
    ausencia de archivo LICENSE); marcado explícitamente como bloqueante
    para uso en producción hasta confirmación manual directa del repo.
- Modificado `scripts/validate_repo.py`: añadida función
  `is_policy_exempt_warning()` y ajustado el cálculo de exit code en
  `--strict` para excluir warnings `source_commit: unverified`. Probado que
  sigue bloqueando ante cualquier otro tipo de warning (carpeta ausente,
  referencia rota, drift).
- Actualizado `.github/workflows/validate.yml` (comentario) y
  `GOVERNANCE.md` §4.2 (regla formal) para reflejar la nueva semántica de
  `--strict`.
- Regenerados `catalog/CATALOG.md`, `INDEX.md` tras los componentes nuevos
  (208 componentes totales, antes 203).

**Resultado final de validación: 0 errores, 50 warnings (todos
`source_commit: unverified`, política deliberada), `--strict` en verde,
0 drift de catálogo, 19/19 tests OK.**

## 4bis. Sesión 8 — qué se hizo (cerrada)

- **Corrección de proceso (x2):** varios puntos del plan estaban "anotados
  sin sesión asignada" o, en un caso (documentación por audiencias en Word),
  nunca llegaron a registrarse en absoluto pese a haberse hablado en
  sesiones previas. Debora lo señaló dos veces en la misma sesión; ambas
  veces se verificó con búsqueda exhaustiva en el repo antes de corregir
  (no se asumió que faltaba sin comprobar primero). Resultado: todos los
  puntos históricos (1-13) tienen ahora sesión asignada explícita.
- **Separación de sesiones:** la sesión inicialmente llamada "Sesión QA"
  (testing + frontend) se separó en dos, a petición de Debora: **Sesión
  QA** (solo testing: Playwright, `apb-ai-skills`, solape con el
  framework) y **Sesión Frontend** (mockups, generación de frontend,
  catálogo de componentes/sistema de diseño).
- **Recibidos e integrados como insumo:** `apb-ai-skills.zip` (repo
  Copilot-oriented de testing, 10 skills APB + 10 externas + agente
  `qa-orchestrator` + 5 subagentes — confirmado sin pérdida respecto a lo
  esperado); 3 documentos de guía de estilo/widgets
  (`Guía_Estilos__Port_de_Barcelona__2022__v1.pdf`,
  `GISPEM__Guía_de_estilos.pdf`, `ManualUsuario_WidgetsLayout_v1.pdf`).
- **Checklist exhaustivo de `proyecto.md` completado:**
  - §4 Agentes (15 esperados): 100% cubiertos, +4 agentes adicionales.
  - §5 Skills (49 capacidades): cubierto — ver hallazgo de las 22 skills
    "BMAD" más abajo.
  - §6 KPIs (7 dimensiones): **gap nuevo identificado** — el framework no
    tiene mecanismo de telemetría para producir estos datos. Anotado como
    punto #26 del plan.
  - §7 Entregables (7 items): 5/7 cubiertos; 2/7 (plantillas funcionales,
    guía de herramientas) ya capturados en puntos #6 y #2, Sesión 13.
- **Comparación de funcionalidad GitHub vs. zip:** confirmado que el repo
  remoto de GitHub (rama paralela no actualizada por Debora) no aporta
  funcionalidad ausente en nuestro zip — las diferencias eran nomenclatura
  antigua ya renombrada, o contenido ya evaluado y descartado en la
  Sesión 1.5a (ver hallazgo siguiente).
- **Hallazgo mayor: 22 skills con contenido heredado de fuente BMAD/wshobson
  sin adaptar.** La Sesión 1.5a había decidido explícitamente "NO
  incorporar" 6 de estas skills (Grupo B del triage), pero llegaron al
  repositorio de todas formas con el `id` renombrado al esquema correcto
  sin que el contenido se adaptara. Ampliando la búsqueda se encontraron
  16 más con el mismo patrón (22 en total). Tras revisión técnica caso por
  caso (decisión de Debora: revisar antes de decidir, no eliminar a
  ciegas):
  - **21 skills**: contenido técnico legítimo y aprovechable (patrones
    Azure Service Bus/CloudEvents, componentes DevExpress, MCP servers,
    generación de documentos). Limpieza aplicada: eliminada la sección
    final "Integración con BMAD" de cada una, y conectadas a su agente
    real correspondiente vía `consumed_by` (antes huérfanas, sin ningún
    agente real que las consumiera).
  - **1 skill** (`apb-orch-multi-agent-v1.0`, antes "Multi-Agent
    Orchestration"): el modelo de roles inventado ("PM Agent", "Architect
    Agent", "Conductor Directory") permeaba el cuerpo entero, no solo la
    coletilla final — no era aprovechable con poda simple. Reescrita por
    completo (v2.0.0) usando los 19 agentes reales del framework, con
    sistema de "tracks" para coordinación en paralelo y resolución de
    conflictos vía `apb-agent-governance-v1.0`. No requirió migración:
    ningún agente real consumía la versión anterior.
- **Nueva convención de entrega (decisión Debora, vigente desde ahora):**
  todo zip entregado debe contener el **repositorio completo**, no solo
  los archivos tocados en la sesión — Debora sustituye su repo de GitHub
  por completo con el contenido del zip. Verificado en esta sesión: 278
  archivos, diff vacío entre árbol de trabajo y contenido del zip.
- Regenerado `catalog/CATALOG.md`, `INDEX.md` — 208 componentes (sin
  cambio en el total: la limpieza fue sobre contenido existente, no
  creó/eliminó componentes).

**Resultado final de validación: 0 errores, 50 warnings (mismos de
siempre), `--strict` en verde, 0 drift de catálogo, 19/19 tests OK.**

## 5. Bloque de tareas anotadas por Debora — NINGUNA ejecutada todavía

Ver el detalle completo en `discovery/PLAN_FASES_FUTURAS.md`. Resumen:

1. Agente/subagentes/skills para crear agentes/subagentes/skills siguiendo
   el estándar (actualizando catálogo/índice automáticamente).
2. Verificar cobertura de plantillas de todos los tipos + plantillas
   ofimáticas (Debora aportará ejemplos cuando se aborde).
3. Mapa de interacción agentes/subagentes ↔ Jira (qué agente crea qué
   ticket y cuándo: ej. tras OK de backlog, tras valoración COSMIC).
4. Entrenar valoración COSMIC con histórico real de horas de la
   organización (conversión puntos↔horas para facturación de proveedores).
5. Documentar cómo quedaron estructuradas las skills de terceros y el
   enriquecimiento que aplica APB sobre ellas (parcialmente respondible ya
   con `discovery/SESSION_1_DUPLICATES_MAP.md` y `SESSION_1_5A_*`, pero
   falta consolidar en un documento único de cara a esta pregunta).
6. Mecanismo de actualización automática del catálogo e índice — **ya
   resuelto en Sesión 3** (`scripts/generate_catalog.py`), marcar como
   completado en el plan de fases futuras.
7. Verificar cobertura para SDD basado en OpenSpec Kit; valorar aporte de
   GitHub Spec Kit.
8. Guía de uso de agentes (`docs/AGENT_USAGE_GUIDE.md` o similar). Nota:
   `docs/sdd-getting-started.md` (Sesión 7) cubre parcialmente esta
   necesidad a nivel de flujo general; sigue pendiente una guía dedicada
   por agente.
9. Identificar/construir flujo de ciclo completo legacy → SDD (candidatos:
   `apb-wf-legacy-onboarding-v1.0`, `apb-wf-spec-from-legacy-v1.0`).
10. Verificar capacidad de corregir incumplimientos Sonar + preparar PR
    automático (candidatos: `apb-dev-sonar-clean-v1.0`, `apb-dev-pr-doc-v1.0`,
    `prov-sonar-v1.0`).
11. Análisis basados en DDD + inventario global de **dominios de negocio
    APB** (distinto de `DOMAIN_REGISTRY.md`, que es de dominios funcionales
    del framework) con gobernanza y actualización automática.
12. Evaluar necesidad de definir "loops" (bucles de iteración/
    retroalimentación) y dónde formalizarlos.
13. Guía de estilo UI/UX de Debora como política/contexto corporativo —
    **Debora debe adjuntar el documento** cuando se aborde esta tarea. Las
    skills de frontend (`apb-dev-devexpress-front-v1.0`,
    `third-google-labs-code-react-patterns-v1.0`,
    `apb-dev-frontend-devexpress-events-v1.0`) deben referenciarla.
14. ✅ **RESUELTO (Sesión 19, 2026-07-04):** licencia de
    `Lum1104/Understand-Anything` verificada vía API de GitHub: **MIT**
    (commit `0e8ad84a`, repo activo). Bloqueo de producción levantado;
    `third-lum1104-knowledge-graph-v1.0` pasa de `watchlist` a `draft` con
    `license: MIT` y `source_commit` fijado. Su eventual uso sigue
    pendiente de decisión de Débora (que en #14 lo había descartado cuando
    la licencia era desconocida).

## 6. Gaps de catálogo — resueltos en Sesión 7

Los 5 gaps documentados al cierre de la Sesión 6 se resolvieron en la
Sesión 7 (ver sección 4). No quedan referencias rotas conocidas en el
repositorio a fecha de cierre de esta sesión.

## 7. Documentos de evidencia de cada sesión (no editar retroactivamente)

Todos en `discovery/`:
- `SESSION_0_BASELINE.md`
- `SESSION_1_DUPLICATES_MAP.md`
- `SESSION_1_5A_PARALLEL_ZIP_TRIAGE.md`
- `SESSION_4_VALIDATOR_HARDENING.md`
- `SESSION_9_THIRD_PARTY_REVIEW.md`
- `PLAN_FASES_FUTURAS.md`

## 8. Inventario final verificado (al cierre de Sesión 8)

- **341 componentes** con frontmatter YAML válido al cierre de FASE 0 (2026-06-30) — ver §15 para detalle. El desglose de Sesión 8 (208 componentes) quedó superado por las Sesiones 9-22 y los bloques de Enriquecimiento A y B. (Nota histórica original: 107 skills APB, 44 skills
  terceros, 19 agentes, 13 subagentes, 7 workflows, 10 providers, 7
  wrappers, 2 adapters. Sin cambio en el total respecto a Sesión 7: la
  limpieza de las 22 skills "BMAD" en Sesión 8 fue sobre contenido
  existente, no creó ni eliminó componentes. Nota Sesión 9: el conteo de
  "43" reportado originalmente en este documento era un error de cómputo
  manual — el valor real verificado por `generate_catalog.py` siempre fue
  44; corregido en Sesión 9 sin que esto implique ningún cambio de
  contenido real de Sesión 8.)
- `scripts/validate_repo.py`, `scripts/generate_catalog.py`,
  `scripts/invoke_agent.py` — los 3 dinámicos, sin catálogos hardcodeados.
- `.github/workflows/validate.yml` — CI activo en cada PR a `main`.
- `tests/test_validate_repo.py` — 19 tests, dogfooding del validador.
- `docs/sdd-getting-started.md` — guía de arranque SDD.
- **Insumos recibidos, no integrados todavía** (pendientes de su propia
  sesión): `apb-ai-skills.zip` (repo separado, Sesión QA),
  `Guía_Estilos__Port_de_Barcelona__2022__v1.pdf`,
  `GISPEM__Guía_de_estilos.pdf`, `ManualUsuario_WidgetsLayout_v1.pdf`
  (Sesión Frontend).

## 9. Sesión 9 — qué se hizo (cerrada)

**Alcance:** revisión de terceros conforme a `proyecto.md` §8 (34 URLs de
referencia), patrón de tratamiento para listas curadas, e incorporación de
skills concretas con valor real para el stack APB.

### 9.1 Patrón confirmado para listas curadas (meta-repos)

Decisión de Debora: las listas curadas que solo enlazan a otros repos sin
contenido ejecutable propio (`ComposioHQ/awesome-claude-plugins`,
`ComposioHQ/awesome-claude-skills`, `hesreallyhim/awesome-claude-code`,
`skills.sh/.../find-skills`) se documentan como fuente de descubrimiento,
sin crear ningún componente de catálogo (`skills/`, `wrappers/`).

**Hallazgo durante la verificación:** dos repos de §8 inicialmente
clasificados como "lista curada" resultaron ser, tras inspección directa,
**mega-agregadores instalables con contenido real** (no listas de
enlaces): `sickn33/antigravity-awesome-skills` (1.682+ skills empaquetadas,
instalable vía `npx`) y `davila7/claude-code-templates` (cientos de
skills, no solo plantillas de proyecto como sugería su nombre). Ambos se
trataron con un patrón intermedio: no se instala el agregador como
dependencia, pero se evalúa y adapta el contenido textual de skills
puntuales con valor real para APB.

### 9.2 Cobertura de §8 (34 URLs) tras Sesión 9

- **Ya incorporadas antes de Sesión 9:** 10 de 34.
- **Listas curadas puras (sin contenido propio):** documentadas como
  fuente de descubrimiento, sin componente de catálogo.
- **Mega-agregadores con contenido evaluado:** `sickn33/antigravity-awesome-skills`
  y `davila7/claude-code-templates` — 8 skills puntuales incorporadas (ver
  9.3).
- **Repos tipo guía/producto sin skill instalable** (`anthropics/claude-code`,
  `Piebald-AI/claude-code-system-prompts`): sin incorporación, son
  referencia/inspiración, no contenido aplicable al catálogo.
- **`FlorianBruniaux/claude-code-ultimate-guide`:** identificado como
  candidato a insumo de gobernanza (criterios de hardening/CVEs de
  MCP/Claude Code) para `POLICY_VULNERABILITY_MANAGEMENT_v1.1.md` —
  **no incorporado todavía como componente**, queda anotado en
  `PLAN_FASES_FUTURAS.md` punto #27 para decisión de Debora.
- **Pendientes de evaluación a fondo** (`ComposioHQ/agent-orchestrator`,
  `ruvnet/ruflo`, `affaan-m/ecc`, `nexu-io/open-design`): no evaluados en
  detalle en esta sesión, anotados en `PLAN_FASES_FUTURAS.md` punto #27.

### 9.3 Las 8 skills incorporadas (decisión de Debora: "incorpora todas las de C")

**De `davila7/claude-code-templates`** (`skills/third_party/davila7/`):
- `third-davila7-dotnet-backend-v1.0.md` — patrones ASP.NET Core 8+/EF
  Core, adaptado a Azure SQL y Azure Service Bus.
- `third-davila7-csharp-pro-v1.0.md` — checklist de C# moderno/SOLID,
  complemento de revisión técnica (contenido genérico, menor densidad que
  el anterior).

**De `sickn33/antigravity-awesome-skills`** (`skills/third_party/sickn33/`):
- `third-sickn33-saga-orchestration-v1.0.md` — sagas orquestadas/
  coreografiadas, adaptado a Azure Service Bus.
- `third-sickn33-event-store-design-v1.0.md` — diseño de event store, con
  nota sobre Marten para .NET.
- `third-sickn33-ddd-context-mapping-v1.0.md` — Context Mapping de DDD,
  reenrutado a componentes APB reales (el original referenciaba skills
  hermanas inexistentes en APB).
- `third-sickn33-domain-driven-design-v1.0.md` — router de viabilidad DDD,
  mismo tratamiento de reenrutado.
- `third-sickn33-auth-implementation-patterns-v1.0.md` — JWT/OAuth2/RBAC,
  adaptado a ASP.NET Core Identity/Azure AD.
- `third-sickn33-django-access-review-v1.0.md` — revisión IDOR para
  Django/DRF. **Doble atribución:** MIT (repo contenedor) + OWASP Cheat
  Sheet Series CC BY-SA 4.0 (material de referencia base, citado en el
  propio fichero de origen). Skill de mayor relevancia directa por el
  stack GIS Django/DRF de APB.
- `third-sickn33-screen-reader-testing-v1.0.md` — testing WCAG 2.1 AA con
  lectores de pantalla. **Cubre un gap real**: no existía ninguna skill,
  propia ni de terceros, dedicada a este requisito explícito de APB.

**Nota de seguridad verificada:** `sickn33/antigravity-awesome-skills`
documenta en su propio repo (`docs/maintainers/security-findings-triage-*`)
hallazgos de seguridad históricos ya resueltos, pero **sobre su tooling de
instalación** (scripts npm, app web), no sobre el contenido de las
`SKILL.md` adaptadas. Por eso la decisión de no instalar el paquete como
dependencia, solo adaptar el texto de skills puntuales.

**Correcciones aplicadas durante la validación:** 4 referencias a nombres
de subagentes/workflows obsoletos en los descriptores recién creados
(`apb-sub-django-v1.0` → `apb-sub-dev-django-v1.0`, `apb-sub-security-v1.0`
→ `apb-sub-qa-security-v1.0`, `apb-sub-e2e-v1.0` → `apb-sub-qa-e2e-v1.0`,
`apb-wf-qa-v1.0` → `apb-wf-qa-evidence-v1.0`) — error de redacción propio,
no un gap real del repo; corregido antes del cierre de sesión.

### 9.4 Resultado de validación final

**0 errores, 59 warnings (todos `source_commit: unverified`, exentos por
política `GOVERNANCE.md` §4.2), `--strict` en verde, 0 drift de catálogo,
19/19 tests OK.**

Inventario actualizado: **217 componentes** (antes 208): 107 skills APB,
**52 skills terceros** (antes 44, +8 de esta sesión), 19 agentes, 13
subagentes, 7 workflows, 10 providers, 7 wrappers, 2 adapters.

### 9.5 Bloque extenso de nuevas peticiones de Debora (mismo día, fuera del alcance de §8)

Durante el cierre de Sesión 9, Debora aportó un bloque muy amplio de
peticiones nuevas (puntos #27 a #41 de `PLAN_FASES_FUTURAS.md`): repos de
terceros adicionales a evaluar (varios sin URL exacta, pendientes de que
Debora la aporte), pregunta conceptual sobre arquitectura de comunicación
entre agentes (respondida directamente en la conversación, no requiere
sesión propia), loop engineering, integraciones Microsoft (Teams/mail/
SharePoint/Copilot), skill de normalización a Markdown, mecanismo de
actualización automática de documentación funcional, skills de SQL,
validación QA en despliegues, documento de uso del framework +
compatibilidad con Microsoft Copilot/Rovo (sin confirmar todavía),
agentes de licitación (pendiente de briefing de Debora), agente de
spec/documentación funcional desde histórico Jira, agente de
descomposición de monolitos a microservicios DDD, y agentes de dashboards/
métricas (Power BI/Grafana/Prometheus) + logging asociado. **Ninguno de
estos puntos se ejecutó en Sesión 9** — todos quedan anotados con detalle
completo en `PLAN_FASES_FUTURAS.md` para asignación de sesión futura.
Varios requieren información adicional de Debora antes de poder
acometerse (URLs exactas de repos ambiguos, detalle de la licitación,
confirmación de si existe un catálogo corporativo de dominios).

## 10. Sesión 10 — qué se hizo (cerrada)

**Alcance:** agente de meta-gobernanza (#5 del plan), resolviendo además
los puntos #24 (disciplina karpathy) y #31 (normalización a Markdown)
dentro de esta misma sesión — decisión de Debora para evitar que el
meta-builder naciera sin esos principios y hubiera que retocarlo después.

### 10.1 Discovery previo (evitó duplicar trabajo)

Antes de construir, se verificó que el framework ya cubría 2 de los 4
principios karpathy: `apb-dev-grill-before-code-v1.0` (Think Before
Coding) y `apb-dev-verify-before-done-v1.0` (Goal-Driven Execution), con
ejemplos reales y flujo `grill → atomic-plan → verify`. Solo se
construyeron los 2 que faltaban genuinamente.

### 10.2 Componentes construidos

- `agents/apb-agent-meta-builder-v1.0.md` — agente nuevo, dominio
  `governance`. Crea agentes/skills/subagentes siguiendo `SCHEMA.md`,
  exige discovery previo, aplica las 5 skills de disciplina karpathy y
  normaliza adjuntos ofimáticos. Nunca se auto-aprueba ni hace
  commit/push directo.
- `skills/apb-owned/development/apb-dev-simplicity-first-v1.0.md` —
  principio karpathy "Simplicity First".
- `skills/apb-owned/development/apb-dev-surgical-changes-v1.0.md` —
  principio karpathy "Surgical Changes".
- `skills/apb-owned/platform/apb-plat-doc-to-markdown-v1.0.md` —
  normalización de adjuntos ofimáticos a Markdown (#31).

### 10.3 Reforzado transversalmente (no son componentes, son gobernanza)

- `README.md` — Principios Fundamentales #11 (disciplina de codificación
  agéntica) y #12 (normalización a Markdown), añadidos sin romper la
  numeración 1-10 existente.
- `GOVERNANCE.md` §3.1 (Alta de componentes) — referencia explícita y
  obligatoria a los Principios #11/#12 para cualquier alta, generada por
  el meta-builder o por un humano.

### 10.4 Resultado de validación final

**0 errores, 59 warnings exentos, `--strict` en verde, 0 drift de
catálogo, 19/19 tests OK.** Inventario: **221 componentes** (antes 217):
110 skills APB (+3), 52 terceros (sin cambio), 20 agentes (+1).

## 11. Sesión 11 — qué se hizo (cerrada)

**Alcance:** corrección de un defecto de formato detectado al preparar la
sesión, más la ampliación completa del punto #25 (deuda técnica,
vulnerabilidades, dependencias, rendimiento — más allá de solo Sonar).

### 11.1 Hallazgo y corrección de formato (a petición de Debora)

Se detectaron 19 archivos de skills con comillas mal cerradas en la
sección "Dependencias" del cuerpo (`` `apb-dev-code-review-v1.0" `` en
vez de `` `apb-dev-code-review-v1.0` ``) — defecto cosmético, no afectaba
al frontmatter YAML. Debora pidió explícitamente corregirlo ("Arregla el
tema de las comillas"), tratado como excepción válida a la regla de
cambios quirúrgicos (Debora, como Arquitectura, priorizó la corrección).
47 líneas corregidas en 19 archivos, cambio puramente sintáctico,
verificado diff por diff antes y después.

### 11.2 Discovery previo (evitó duplicar trabajo)

Se verificó que el flujo Sonar+PR del punto #4 original (alcance inicial
de Sesión 11) ya estaba construido desde antes (`apb-dev-sonar-clean-v1.0`,
`apb-dev-pr-doc-v1.0`, `prov-sonar-v1.0`, conectados a
`apb-agent-implementer-v1.0`). También se verificó que
`apb-gov-jira-evidence-v1.0` + `prov-atlassian-v1.0` ya existían para la
creación real de tickets Jira — no se reimplementó, se reutilizó.

### 11.3 Componentes construidos — ampliación de #25, dominio `operation`

- `agents/apb-agent-tech-debt-v1.0.md` — agente nuevo, autonomy_level 2.
  Diferenciado explícitamente de `apb-agent-risk-exception-v1.0` (gestiona
  riesgo aceptado, no genera plan) y `apb-agent-sre-v1.0` (reactivo a
  incidentes, no auditoría proactiva).
- `skills/apb-owned/operation/apb-ops-dependency-audit-v1.0.md` —
  dependencias obsoletas + vulnerabilidades CVE.
- `skills/apb-owned/operation/apb-ops-perf-bottleneck-v1.0.md` — cuellos
  de botella de rendimiento con propuesta concreta.
- `skills/apb-owned/operation/apb-ops-debt-remediation-plan-v1.0.md` —
  consolida hallazgos, **presenta el plan al humano, espera "OK" explícito,
  solo entonces crea tickets Jira** (autonomy_level 2). Regla no
  negociable, decisión expresa de Debora: nunca se crea ningún ticket sin
  ese punto de control cumplido.

### 11.4 Resultado de validación final

**0 errores, 59 warnings exentos, `--strict` en verde, 0 drift de
catálogo, 19/19 tests OK.** Inventario: **225 componentes** (antes 221):
113 skills APB (+3), 21 agentes (+1).

## 12. Sesión 12 — qué se hizo (cerrada)

**Alcance:** punto #16 del plan — análisis de riesgos para validación de
Ciberseguridad/Arquitectura/QA, con dos decisiones de diseño de Debora
tomadas antes de construir.

### 12.1 Decisiones de diseño de Debora

- Se construye como **skill transversal** (no agente propio, no
  subagente) — cualquier agente del framework la invoca antes de
  presentar su output a validación humana, no es una sesión de trabajo en
  sí misma.
- La fila "Release" de la tabla de Puntos de Validación Obligatorios
  (`SYSTEM.md` §6, equivalente a `proyecto.md` §3.6) se resuelve como
  **"Release Manager / Arquitectura"** — corregido en `SYSTEM.md` (antes
  decía "PMO / Operaciones / Arquitectura"). **`proyecto.md` no se pudo
  actualizar** — es un documento externo de solo lectura para Claude;
  Debora debe corregirlo manualmente en su copia.

### 12.2 Componente construido

- `skills/apb-owned/governance/apb-gov-ai-risk-gate-v1.0.md` — skill
  transversal, dominio `governance`. Evalúa los 6 riesgos de uso de IA de
  `proyecto.md` §3.5 (alucinaciones, información desactualizada,
  incumplimiento de estándares, dependencia excesiva, pérdida de
  conocimiento humano, código inseguro) y adjunta un aviso al artefacto
  antes de la validación humana. Nunca aprueba ni bloquea — solo informa.
  Diferenciada explícitamente de `apb-sec-risk-analysis-v1.0` (esa es
  sobre seguridad de la información, ISO 27005; esta es sobre el proceso
  de generación por IA).

### 12.3 Resultado de validación final

**0 errores, 59 warnings exentos, `--strict` en verde, 0 drift de
catálogo, 19/19 tests OK.** Inventario: **226 componentes** (antes 225):
114 skills APB (+1).

## 13. Sesión QA — qué se hizo (cerrada)

**Alcance:** punto #17 del plan — auditoría completa de
`apb-ai-skills.zip` (subido de nuevo en esta sesión, el zip original no
había persistido entre sesiones), y resolución del solapamiento detectado
con `APB-IA-FRAMEWORK`.

### 13.1 Auditoría — hallazgo no anticipado

Confirmados 10 skills APB + 10 externas + 1 agente (`qa-orchestrator`) +
5 subagentes, tal como esperaba el plan. **Hallazgo adicional no
contabilizado en la descripción original:** una carpeta
`skills/_spec-driven/` con 3 skills más (`spec-to-api-contract`,
`spec-to-e2e-flows`, `spec-to-test-plan`).

### 13.2 Solapamiento — 4 fusiones, no 1 como anticipaba el plan

Decisión de Debora en los 4 casos: "fusionar e incorporar al repo de
APB-IA-FRAMEWORK". Ninguna fusión se mantuvo duplicada en el repo de
origen:

- `apb-qa-unit-test-gen-v1.0` ← `apb-unit-test-generator` → v1.1.0
  (cobertura JS/TS, ejemplos de código, tests de eventos).
- `apb-qa-test-plan-v1.0` ← `apb-test-plan-lcsp` → v1.1.0 (marco
  normativo LCSP/ENS/RGPD/WCAG con criterios cuantificados, contexto
  contractual de licitación).
- `apb-sec-ens-v1.0` ← `apb-ens-security-audit` → v1.1.0 (tablas
  operativas de controles por nivel Alto/Medio, cruce OWASP, formato de
  informe de hallazgos).
- `apb-qa-anonymize-v1.0` ← `apb-test-data-rgpd` → v1.2.0 (tabla de
  dominios ficticios APB con vocabulario portuario — IMO, código de
  atraque —, fixtures concretos Oracle/Cosmos/PostGIS/.NET/TypeScript).

### 13.3 Decisión arquitectónica de fondo: `apb-ai-skills` queda DEPRECADO

Decisión de Debora. Todo desarrollo futuro de skills/agentes/subagentes
de QA vive exclusivamente en `APB-IA-FRAMEWORK`. **No se ha tocado el
repositorio `apb-ai-skills` físicamente** (decisión explícita de Debora:
"no toques nada de apb-ai-skills, quédate solo con la decisión verbal").
Sus referencias internas al `qa-orchestrator` y 3 subagentes
(`dotnet-backend-agent`, `data-persistence-agent`, `django-gis-agent`)
apuntan a nombres antiguos de las 4 skills ahora fusionadas, y sus 2
GitHub Actions (`sync-skills.yml`, `validate-skills.yml`) seguirán
ejecutándose salvo que alguien los desactive manualmente en ese repo.

### 13.4 Resultado de validación final

**0 errores, 59 warnings exentos, `--strict` en verde, 0 drift de
catálogo, 19/19 tests OK.** Inventario: **226 componentes** (sin cambio
respecto a Sesión 12 — las 4 fusiones fueron de contenido dentro de
componentes ya existentes, no crearon componentes nuevos).

## 14. Migración a Claude Code (post-Sesión QA)

Tras el cierre de las Sesiones 10-12 y QA, Debora solicitó migrar todo el
trabajo a un entorno local con Claude Code. Se generó
`CONTEXTO_PARA_CLAUDE_CODE.md` (en la raíz del repo, dirigido a que
Claude Code lo lea al iniciar) e `INSTRUCCIONES_MIGRACION_DEBORA.md`
(fuera del repo, guía personal de Debora). Durante la migración se
detectó y corrigió un bug real de compatibilidad Windows en
`tests/test_validate_repo.py` (8 llamadas a `write_text()` sin
`encoding="utf-8"` explícito, que fallaban en Windows por usar la
codificación local del sistema en vez de UTF-8 — corregido, verificado
19/19 tests OK tanto en el entorno de validación como en Windows real de
Debora tras el fix).

**Importante para cualquier instancia de Claude/Claude Code que retome
este trabajo:** este mismo documento de continuidad estuvo
desactualizado durante la migración — la tabla de la sección 1 marcaba
las Sesiones 10, 11, 12 y QA como "❌ Pendiente" cuando ya estaban
completas. Si encuentras inconsistencias similares en otros documentos
(`PLAN_FASES_FUTURAS.md`, `CATALOG.md`, etc.), verifica siempre contra el
estado real de los archivos (`scripts/validate_repo.py --strict` +
inspección directa de `agents/`, `skills/`) antes de asumir que la
bitácora es exacta — esta sección queda como recordatorio de que la
bitácora puede desincronizarse si no se actualiza al cierre de cada
sesión, no solo al generar el zip de entrega.

---

## 15. FASE 0 — Higiene de wiring + validador bidireccional (2026-06-30, cerrada)

**Contexto:** Sesión post-Enriquecimiento B. El análisis 360° (§H de `PLAN_FASES_FUTURAS.md`)
identificó que ~32 skills creadas en Enriquecimiento B no estaban cableadas en el frontmatter
`skills:` de sus agentes destino, y que 5 subagentes tampoco estaban listados en sus padres.
Además, el validador no comprobaba estos wirings en ambas direcciones.

**Qué se ejecutó:**

1. **Fix README.md** — enlace roto `CATALOG.md` → `catalog/CATALOG.md` corregido.

2. **Wiring de 5 subagentes huérfanos** (frontmatter `subagents:` de sus padres):
   - `apb-sub-ops-entra-v1.0` + `apb-sub-sec-sast-v1.0` → `apb-agent-security-architect-v1.0`
   - `apb-sub-qa-performance-v1.0` → `apb-agent-qa-auto-v1.0`
   - `apb-sub-finops-azure-v1.0` → `apb-agent-finops-v1.0`
   - `apb-sub-gov-data-v1.0` → `apb-agent-data-governance-v1.0`

3. **Wiring skills Enriquecimiento B** en 21 agentes destino (tabla §C del plan) + 19 wirings
   adicionales detectados por el nuevo validador. Total: 40 wirings corregidos en 22 agentes.

4. **`validate_bidirectional_wiring()`** — nueva función en `scripts/validate_repo.py`. Test
   `TestValidateBidirectionalWiring` con 2 casos añadido a `tests/test_validate_repo.py`.

5. **Regla de cierre de sesión** — Débora pidió que al cierre de cada sesión se actualicen
   siempre: catálogo, validador, PLAN_FASES_FUTURAS, CONTINUIDAD, HANDOFF, README.

**Resultado:** `validate_repo.py --strict` → exit 0, 0 errores, 59 warnings exentos
(`source_commit: unverified`), 21/21 tests OK. Commit `d62c6b1`, 24 ficheros, 284 inserciones.

**Estado del inventario al cierre:** 341 componentes (sin cambio — wirings son metadatos).
0 aprobados, todos en `draft`.

**Próxima fase desbloqueada:** FASE 1 — Mejoras de workflows existentes:
añadir Change Manager a `sdd-full` y `cloud-migration`, Security Architect a `code-review`,
conectar `incident-l1` → `incident-l2`, Problem Manager en `incident-l1`,
Tech Debt en `legacy-onboarding`, performance + accessibility en `qa-evidence`.

---

## 16. FASE 1 + FASE 1B — Mejoras de workflows y corrección de bugs (2026-06-30, cerrada)

**Contexto:** Sesión inmediatamente posterior a FASE 0. Dos bloques ejecutados en la misma sesión.

### FASE 1 — Mejoras de 6 workflows existentes

- `apb-wf-sdd-full-v1.0`: añadido `apb-agent-change-manager-v1.0`.
- `apb-wf-cloud-migration-v1.0`: añadido `apb-agent-change-manager-v1.0`.
- `apb-wf-code-review-v1.0`: añadido `apb-agent-security-architect-v1.0`.
- `apb-wf-incident-l1-v1.0`: añadido `apb-agent-problem-manager-v1.0` + campo `escalation: apb-wf-incident-l2-v1.0`.
- `apb-wf-legacy-onboarding-v1.0`: añadido `apb-agent-tech-debt-v1.0`.
- `apb-wf-qa-evidence-v1.0`: añadidas skills `apb-qa-performance-v1.0` y `apb-qa-accessibility-v1.0`.

### FASE 1B — Corrección de bugs BUG-01 a BUG-08

- ✅ BUG-01: `context/apb/templates/WORKFLOW.md` — blockquote → YAML frontmatter canónico con delimitadores `---`.
- ✅ BUG-02: `scripts/generate_catalog.py` — eliminado cuantificador posesivo `\s*+` inválido en Python 3.10 (8 patrones, líneas 251-258).
- ⏸ BUG-03: `design-system/components/component-reference.md §9` — color sidebar omitido; pendiente confirmación del equipo de diseño APB.
- ✅ BUG-04: `adapters/claude/adapter-claude-v1.0.md` — model string actualizado a `claude-sonnet-4-6`.
- ✅ BUG-05: `SYSTEM.md §4.2` — tabla de adapters completada con `m365/` y `rovo/` (los 4 adapters reales del repo).
- ✅ BUG-06: `.github/workflows/telemetry.yml` — reemplazado `git push` directo a main por `git push` a rama + `gh pr create`.
- ✅ BUG-07: `CONTINUIDAD_PROYECTO.md §8` — número de componentes corregido de 208 a 341 (cierre FASE 0).
- ✅ BUG-08: creado stub `skills/third_party/third-lum1104-knowledge-graph-v1.0.md` con `status: watchlist` y aviso de licencia no verificada.

**Resultado:** exit 0, 0 errores, 60 warnings exentos, 21 tests OK. **342 componentes** (341 + 1 stub nuevo).

**Inventario al cierre:** 342 componentes, 0 aprobados, todos `draft` o `watchlist`.

**Próxima fase desbloqueada:** FASE 2 — Sesiones abiertas del plan (puntos #6, #8, #52, #14, #19, #20, #21).

---

## 17. FASE 2 — Documento de Dirección + actualización docs audiencias (2026-06-30, cerrada)

**Contexto:** Sesión 14 (punto #23 del plan) — documentación segmentada por audiencia. Los borradores de arquitectos y devs existían; faltaba el informe ejecutivo para Dirección.

**Ejecutado:**
- Creado `docs/informe-direccion.md` — informe ejecutivo para Dirección APB / CIO / CISO. Cubre: qué resuelve el framework, estado actual (342 componentes, 0 aprobados), capacidades por dominio, política de gobierno IA, inversión realizada, decisiones pendientes de Dirección, índice de documentación por audiencia.
- Actualizada cabecera `docs/guia-funcional.md` — fecha 2026-06-30, 342 componentes.
- Actualizada cabecera `docs/manual-arquitectura.md` — fecha 2026-06-30, 342 componentes, commit 4f02f38.

**Resultado:** exit 0, 0 errores, 60 warnings exentos, 21 tests OK. Catálogo sin cambios (documentos no son componentes del catálogo).

**Inventario al cierre:** 342 componentes, 0 aprobados.

**Pendiente de Sesión 14:** conversión .docx de los 3 documentos Markdown (requiere decisión runtime orquestación + plantilla corporativa Word APB).

**Próxima fase disponible:** FASE 3 estratégica o sesiones bloqueadas pendientes de decisiones de Dirección (ver §I de PLAN_FASES_FUTURAS.md).

---

## 18. FASE #50/#51 — QA del framework: tests de comportamiento (2026-06-30, cerrada)

**Contexto:** Puntos #50 (QA del framework) y #51 (prueba real de agentes). Solo 1 de 35 agentes tenía casos de comportamiento documentados.

**Ejecutado:**
- `tests/test_agent_behavior.md` v1.1.0: añadidos 5 agentes críticos × 3 casos cada uno (total 20 casos, 6 agentes cubiertos): `apb-agent-qa-auto-v1.0`, `apb-agent-technical-architect-v1.0`, `apb-agent-governance-v1.0`, `apb-agent-implementer-v1.0`, `apb-agent-release-manager-v1.0`.
- `tests/golden_output_tests.md`: NUEVO — 5 Golden Output Tests para las skills más críticas: `apb-dev-code-review-v1.0`, `apb-arch-event-driven-master-v1.0`, `apb-gov-policy-check-v1.0`, `apb-ops-incident-triage-v1.0`, `apb-plat-deliver-artifact-v1.0`.
- `tests/test_behavior_coverage.py`: NUEVO — test Python (5 casos) que valida que los 6 agentes críticos tienen cobertura y que el archivo GOT existe.

**Resultado:** 26/26 tests OK (21 existentes + 5 nuevos de cobertura), exit 0, 0 errores.

**Inventario al cierre:** 342 componentes, 0 aprobados. 6/35 agentes con tests de comportamiento documentados.

**Próxima fase:** T5 (template AGENT.md), T3 (análisis duplicados), o sesiones bloqueadas cuando lleguen inputs externos.

---

## 19. T3 — Resolución de skills duplicadas WCAG/API/E2E (2026-06-30, cerrada)

**Contexto:** Análisis T3 identificó 3 grupos de skills duplicadas o solapadas. Decisiones de Arquitectura APB:
- Grupo 1 (WCAG): Opción B — deprecar `apb-design-wcag-v1.0` y `apb-design-wcag-patterns-v1.0`, consolidar en `apb-qa-accessibility-v1.0`.
- Grupo 2 (API): Opción A — deprecar `apb-dev-api-design-v1.0`, mantener `apb-arch-api-contract-v1.0` + `apb-arch-api-lifecycle-v1.0`.
- Grupo 3 (E2E): Opción A — renombrar `apb-qa-validation-e2e-v1.0` → nuevo `apb-qa-e2e-patterns-v1.0`.

**Ejecutado (commit `eb4a348`):**
- 4 skills deprecadas: `apb-design-wcag-v1.0`, `apb-design-wcag-patterns-v1.0`, `apb-dev-api-design-v1.0`, `apb-qa-validation-e2e-v1.0`.
- 1 skill nueva: `apb-qa-e2e-patterns-v1.0` (con 4 plantillas E2E: Happy Path, Idempotencia, Saga, DLQ).
- 3 wirings actualizados: `apb-agent-ux-mockup-v1.0`, `apb-agent-technical-architect-v1.0`, `apb-agent-qa-auto-v1.0`.
- Patrón canonizado: deprecar = `status: deprecated` + `deprecated_reason` + `consumed_by: []` + rewiring antes del commit.

**Resultado:** 0 errores, 60 warnings exentos, 343 componentes, 26/26 tests OK.

---

## 20. Sesión Post-T3 — Evoluciones técnicas + gobernanza + DX (2026-06-30, cerrada)

**Ejecutado:**
- **E-T3** (`scripts/validate_repo.py`): nueva función `validate_version_drift()` — WARNING cuando un agente referencia una skill con major version inferior a la última disponible en el repo.
- **E-T2** (`tests/test_validate_repo.py`): nueva clase `TestVersionDrift` (2 tests) + clase `TestGoldenOutputStructure` (5 tests sobre skills críticas reales).
- **E-G2** (`scripts/check_review_dates.py` + `.github/workflows/review-reminder.yml`): GitHub Action mensual que abre issue con componentes con `review_date` > 180 días.
- **E-G3** (`GOVERNANCE.md §7`): proceso formal de deprecación documentado — quién propone, quién aprueba, plazos, pasos técnicos, paso a `retired`.
- **E-DX1** (`docs/getting-started-contributing.md`): guía paso a paso para crear skills y agentes nuevos desde plantilla, ejecutar el validador, y abrir PR.

**Resultado:** 33/33 tests OK (26 existentes + 7 nuevos), 0 errores, 343 componentes.

**Inventario al cierre:** 343 componentes (175 skills APB, 51 skills terceros, 35 agentes, 33 subagentes, 17 workflows, 19 providers, 7 wrappers, 4 adapters).

**Próximas fases sin bloqueantes:** ver `PLAN_FASES_FUTURAS.md §H FASE 2` (sesiones 13 resto, 14 .docx). Bloqueadas externamente: sesiones 19, 20, 22, FASE 3.

---

## 21. Sesión KB+SP — Knowledge Base corporativa + system prompts LLM-agnósticos (2026-06-30, cerrada)

**Contexto:** Tres ficheros de conocimiento corporativo APB (v1, v2, v3) entregados por Debora. Se consolidan en una única fuente de verdad y se cablea en todo el framework de forma LLM-agnóstica.

**Ejecutado:**

- **`context/apb/knowledge/APB_KNOWLEDGE_BASE.md`** (nuevo): Knowledge base consolidada (~1100 líneas) con 14 secciones: negocio portuario (escalas/atraques/tasas/EDI), catálogo de aplicaciones (ARGOS, SÒSTRAT legacy, APIs ARQ, AE, GIS), integraciones (PORTIC, AGE, AIS, VTS Kongsberg, Alfresco SOA), GoToCloud, seguridad, contratación, herramientas, mapa Jira/equipos/GitHub, estrategia IA, diccionario trilingüe CA/ES/EN. Guardrail explícito: el legacy es contexto, no prescripción tecnológica. Stack aprobado = STANDARD_ARCHITECTURE.md (sin cambios).

- **`context/apb/knowledge/GOVERNANCE_KNOWLEDGE_BASE.md`** (nuevo): Proceso de gobernanza — owner (Debora Martin), revisores por dominio (Alberto Ponseti, Xavier Estebanell, Enrique Salinas...), triggers obligatorios/recomendados, flujo PR + hotfix, proceso para equipos funcionales sin acceso al repo, restricciones de contenido, versionado semántico, SLAs (24h errores críticos, 1 sprint nuevos sistemas), checks en validate_repo.py.

- **`providers/prov-apb-knowledge-v1.0.md`** (actualizado): v1.0.0→v1.1.0, status draft→approved. Dos capas: framework standards + business context (APB_KNOWLEDGE_BASE.md).

- **`scripts/inject_knowledge_context.py`** (nuevo): Script idempotente que añade `prov-apb-knowledge-v1.0` en frontmatter + sección `## Contexto Corporativo APB` en 211 skills/agents existentes. Funciona para cualquier LLM runtime (no solo Claude). Segundo run: 0 ficheros modificados.

- **Templates actualizados** (`SKILL_APB.md`, `AGENT.md`): `## Prompt de Sistema` / `## 🤖 Prompt de Sistema` marcados como **OBLIGATORIOS** con estructura fija de 7 subsecciones: Identidad → Contexto APB → Misión → Inputs → Instrucciones/Capacidades → Restricciones → Formato.

- **`scripts/generate_system_prompts.py`** (nuevo): Script idempotente que genera system prompts contextualizados para todos los ficheros sin prompt. Extrae contenido real de cada fichero (frontmatter + secciones funcionales), diferencia skills (Proceso) de agents (Capacidades), inserta antes del anchor correcto (Comportamiento/Historial/Marcado IA). 199 ficheros generados, 12 ya tenían prompt (skip), 0 errores.

**Resultado:** 211/211 skills y agents tienen `## Prompt de Sistema` con contenido real y funcional. Cualquier LLM que cargue un fichero obtiene el prompt correcto independientemente del runtime. validate_repo.py: 0 errores, 60 warnings exentos.

**Inventario al cierre:** 343 componentes (sin cambios en número — mejora de calidad interna, no nuevos componentes).


## 22. Sesión #78+#83 — Estándar de Prompting + Harness Engineering (2026-07-02, cerrada)

**Contexto:** Sesión combinada decidida por Debora ANTES del Enriquecimiento #56–#76,
para que los futuros componentes nazcan conformes al estándar (anti-retrabajo). Registro
completo en `PLAN_FASES_COMPLETADAS.md`.

**Ejecutado:**

- **`context/apb/standards/PROMPTING_STANDARD.md`** (nuevo): estándar canónico de estructura
  de prompt — 10 ejes, "Qué NO hacer" con 4 mínimos + 7 prohibiciones adicionales, bloque
  canónico machine-checkable (6 headings literales), ejemplo E/S completo, ámbito por tipo.
- **6 plantillas actualizadas** (AGENT, SUBAGENT, SKILL_APB, SKILL_THIRD_PARTY, ADAPTER,
  WORKFLOW) con el bloque canónico + checklist.
- **`scripts/retrofit_prompting.py`** (nuevo, idempotente): retrofit de **244 componentes**
  (35 agentes + 33 subagentes + 176 skills APB); deriva el contenido de lo que cada
  componente ya declara (referencia sus secciones, no duplica ni inventa).
- **Harness (punto #83), agnóstico de LLM/herramienta:** `SYSTEM.md §10` (5 subsistemas,
  System of Record + ACID, routing files 50–200 líneas, WIP=1 + Bootstrap Contract, Feature
  Lists; Referencias → §11) + `GOVERNANCE.md §8` (Pass-State Gating, validación 3 capas,
  Clean State Handoff, Planner/Generator/Evaluator como insumo de #77; Referencias → §9).
- **`repo-scaffold/harness-ready/`** (nuevo): `AGENTS.md`, `PROGRESS.md`, `FEATURES.md`,
  `init_check.py` (Python portable).
- **`scripts/validate_repo.py`**: check **#18** Estándar de Prompting (nivel ERROR tras el
  retrofit — anti-repetición) + check **#19** `validate_harness_cold_start` (Cold-Start Test,
  gobernanza harness, scaffold completo). +5 tests (33 en test_validate_repo).

**Resultado:** 244/244 componentes conformes (contador 244→0). `validate_repo.py --strict`
exit 0 (0 errores, 60 warnings exentos). Tests 38/38.

**Inventario al cierre:** 343 componentes (sin cambios en número — estándar + harness, no
nuevos componentes).

## 23. Sesión QA-2 — Planes de pruebas (#82) + Navegación agéntica (#84) (2026-07-02, cerrada)

**Contexto:** Débora eligió el bloque QA. Aportó 3 visiones del plan de pruebas de TruckCenter
(Rovo/Jira, Rovo/Jira+AF, Copilot/código) y pidió unificarlas sin duplicar con trazabilidad de
procedencia; además exigió **ejecución funcional real** con evidencias descargables o a Jira, skill
interactiva, degradación de fuentes, procedencia múltiple e ingesta de planes aportados en cualquier formato.

**Ejecutado:**
- **`context/apb/standards/TEST_PLAN_STANDARD.md`** + plantilla **`context/apb/templates/TEST_PLAN.md`**.
- **`apb-qa-test-plan-v1.0` → v1.2.0** (interactiva; ingesta de planes aportados vía
  `apb-plat-doc-to-markdown`; procedencia múltiple; degradación de fuentes; plan previo incremental;
  no-regresión rendimiento).
- **`docs/qa/examples/QA_TRU_TruckCenter_UNIFICADO.md`** (112 casos sin duplicar, procedencia por prueba,
  mapeo A→unificado) + fuentes en `docs/qa/examples/sources/`.
- **#84:** `providers/prov-browser-agent-v1.0.md` + `skills/apb-owned/qa/apb-qa-exploratory-nav-v1.0.md`,
  cableados a `apb-agent-qa-auto-v1.0` y `apb-wf-qa-evidence-v1.0`.
- **Ejecución real** sobre TruckCenter PRE (EntraID asistido, rol MANAGE): 4 PASS, 1 no evaluable, 2 hallazgos;
  evidencias en ZIP (informe MD+HTML+log); 0 datos modificados.
- **Validador:** check **#20** `validate_test_plan_methodology` + 2 tests → 40/40 suite.

**Resultado:** `validate_repo.py --strict` exit 0 (0 errores, 60 warnings exentos). Tests 40/40.

**Inventario al cierre:** **345 componentes** (+2: `prov-browser-agent-v1.0`, `apb-qa-exploratory-nav-v1.0`).

**Pendiente derivado (Débora):** el agente de pruebas funcionales debe **consultar credenciales desde un
repositorio central** (Azure Key Vault, `GOVERNANCE.md §5`) + captura/reutilización de `storage_state` para
ejecutar sin login manual. Ver HANDOFF.

**Continuación E-bis (2026-07-02):** ejecución ampliada para cubrir los 112 casos en **solo lectura** (informe
en OneDrive `QA_TruckCenter_evidencias/INFORME_EJECUCION_112.md`). 8 PASS + 8 parciales (MANAGE). Hallazgos:
**F2** (form Alta no carga >45s), **F3** (PRE sin datos → ~45 casos no evaluables), **F4** (API LGP ~9,3s),
**F5** (maestro multiidioma CA/ES/EN ≠ AF). Rendimiento, seguridad, USER_READ y evidencia visual PNG/vídeo →
**Sesión QA-3** (registrada en FUTURAS). Limitación de entorno: las capturas del navegador MCP no persisten
como fichero → visual con Playwright en QA-3. **0 datos modificados en PRE.**

**Fase E-ter (2026-07-02):** Débora detectó que la unificación de TruckCenter había **perdido información**
narrativa (incidencias históricas y más) — error grave, norma nueva "unificar nunca elimina información".
Restaurado íntegramente + `TEST_PLAN_STANDARD §3.1` (principio de conservación) + check #21 anti-repetición.

**Fase G (2026-07-03):** Débora pidió 4 mejoras más sobre metodología de planes de pruebas: plantilla
restaurada, **ID canónico append-only** `{APP}-B{NN}-T{NN}` (§3.2, con columna "Legado" para no romper
trazabilidad con informes ya emitidos), **gobernanza por aplicación** (§6.1, reutiliza `GOVERNANCE.md`),
**entrega dual Markdown+HTML** (§7.1, script `scripts/generate_test_plan_html.py`, sin CDN/DevExpress, azul
corporativo + logo APB). Check #21 ampliado (parte c). Commit `29b9799`. Detalle: `PLAN_FASES_COMPLETADAS.md`.

**Fase H (2026-07-03):** Débora corrigió: "el framework debe ser agnóstico al LLM y la herramienta". El
principio ya estaba declarado (`SYSTEM.md §4.3`) pero el propio `SYSTEM.md §10.1` exigía un routing file raíz
`AGENTS.md` que **no existía** — el único fichero raíz era `CLAUDE.md`, específico de Claude Code, invirtiendo
la regla. Creado `AGENTS.md` (fuente única de reglas) + `CLAUDE.md` y `.github/copilot-instructions.md`
reescritos como ficheros delgados que derivan de él. Débora señaló **GitHub Copilot** como la alternativa
concreta de "día después" — su punto de entrada ya está cableado de verdad, no solo en el adapter `draft`.
Check **#22** `validate_agnostic_root_routing` (anti-deriva) + 3 tests. Detalle: `PLAN_FASES_COMPLETADAS.md`.

**Estado al cierre de Fase H:** `validate_repo.py --strict` exit 0 (0 errores, 60 warnings exentos) ·
**41/41 tests** · 345 componentes (sin cambio — ficheros de routing no son catalogables). Pendiente:
decidir si pushear la rama `feat/qa2-test-plan-methodology`; provider de VCS alternativo si Débora
diversifica de GitHub (distinto del punto agnóstico de LLM/herramienta, ya resuelto en Fase H).

**Fase I (2026-07-03):** Débora aportó 7 huecos de la metodología de planes de pruebas frente a un uso
real. Cubiertos en `TEST_PLAN_STANDARD` v1.3.0 y skill `apb-qa-test-plan` v1.4.0: **(1)** matriz de roles +
columna «Rol requerido» por caso, usuario de ejecución por **AKV** o runtime (nunca en fichero, §9.2);
**(2)** informe corporativo (HTML con badges de estado); **(3)** **Acta de aprobación del informe**
(Funcional + Desarrollador, persistida en `.md` **y** Jira, §6.2 — decisión: se aprueba el *informe*, no el
PR); **(4)** destino de ejecución `local`/`ci-runner`/`azure-qa` (§9.1, k6 nunca desde el portátil);
**(5)** guía `docs/qa/EJECUCION_LOCAL.md` + instalación asistida; **(6)** `spec` SDD como fuente
autoritativa (§1) + nuevo subagente **`apb-sub-qa-fix-loop-v1.0`** (fallo→PR→Jira, propone sin mergear),
cableado en `apb-wf-qa-evidence` y `apb-wf-sdd-full`; **(7)** nuevo provider **`prov-azure-qa-runtime-v1.0`**
(`draft`) para ejecución en la suscripción QA de Azure sin instalar nada. Check **#23**
`validate_execution_and_approval_methodology` + 3 tests. Detalle: `PLAN_FASES_COMPLETADAS.md`.

**Estado al cierre de Fase I:** `validate_repo.py --strict` exit 0 (0 errores, 60 warnings exentos) ·
**49/49 tests** · **347 componentes** (345 + subagente fix-loop + provider Azure QA, ambos `draft`).
Pendiente: decidir si pushear la rama `feat/qa2-test-plan-methodology`; **QA-3** (despliegue real del
entorno Azure QA + ejecución funcional completa con dataset, k6 y SonarQube/OWASP ZAP).

## 24. Sesión Orquestación PoC (#77) + Auditorías de Cumplimiento (#85, #86) (2026-07-06)

**Contexto:** Débora continuó con "las siguientes fases" del framework. Tras mapear
`PLAN_FASES_FUTURAS.md` y `CONTINUIDAD_PROYECTO.md`, pidió avanzar en paralelo en:
(A) PoC de orquestación (#77) — demostrar viabilidad de pausas humanas sincrónicas;
(B) Auditoría Design System (#85) — APB.TRU contra tokens/componentes/tipografía/WCAG;
(C) Auditoría de calidad (#86) — verificar cierre de hallazgos Sonar en APB.API.SMS.

**Bloqueante resuelto previamente:** #77 quedó pendiente de "decisión arquitectónica del motor"
(Azure Durable / LangGraph / Temporal). Esta sesión **no elige el motor definitivo** (eso sigue siendo
responsabilidad de Débora + Plataforma APB), pero **demuestra viabilidad** de la capa de checkpoint
humano como primer escalón hacia la orquestación real.

**Ejecutado:**

- **PoC #77 (3 artefactos):**
  - `scripts/orchestrate_checkpoint_gate.py` — lee frontmatter YAML (`human_checkpoints`), genera bloque de
    pausa exacto según `apb-orch-human-checkpoint-v1.0.md` (formato: ⏸️ header, ¿Qué completado?, ¿Qué revisar?,
    artifacts table, 3 opciones ✅/🔄/❌, YAML decision log).
  - `.github/workflows/human-checkpoint-poc.yml` — workflow_dispatch (input `workflow_id`, default
    `apb-wf-sdd-full-v1.0`), job de generación + job pausa en `environment: human-checkpoint` + job de
    registro de decisión (GitHub Artifacts, 90 días, `.yaml` con timestamp + reviewer + decision).
  - `scripts/setup_github_environment.py` — configura Environment + required reviewers vía API
    (`gh api` / REST, parametrizable `--repo owner/repo --environment human-checkpoint --reviewers user1,user2`),
    permite portabilidad automática repo personal → repo oficial APB sin depender de UI manual.
  - Memo ejecutivo con tabla comparativa (Durable Functions ⭐⭐⭐⭐⭐ recomendado / LangGraph ⭐⭐⭐ /
    Temporal ⭐⭐), checklist pre-decisión, **primer borrador de contratos de eventos** (CloudEvents
    `code.*`, `ci.*`, `pr.*`, `bug.*`, `deployment.*`), checklist de migración repo personal → oficial.
    *(Nota 2026-07-06: este memo vivía en `discovery/HANDOFF_ORQUESTACION_MOTOR.md`, disuelto en la
    reorganización — la decisión de motor está ahora en `PLAN_FASES_FUTURAS.md` Sección A y los pasos
    condicionados a la decisión en `HANDOFF_TECNICOS.md §10.1`.)*

- **Actualización del roadmap:**
  - `discovery/PLAN_FASES_FUTURAS.md` (#77): añadida sección "Sesión de Análisis de Orquestación completada"
    con puntero a handoff.
  - Este fichero (`CONTINUIDAD_PROYECTO.md`): esta sesión 24.

- **#85, #86:** (pendiente de ejecución) — preparados: repos ya clonados (`APB.TRU`, `APB.API.SMS`),
  agentes `apb-agent-design-compliance-v1.0` + `apb-agent-quality-compliance-v1.0` ya en `agents/`
  (draft 2026-07-04), insumo de 4 hallazgos Sonar en `incumplimientos_sms_arq.md` (aportado por Débora).

**Resultado:** PoC validada por ejecución local (`orchestrate_checkpoint_gate.py --workflow
apb-wf-sdd-full-v1.0 --checkpoint 1` genera bloque correcto). Cambios aún no commiteados hasta
confirmación de Débora (scripts pueden disparar CI/CD, requieren aprobación explícita).

`validate_repo.py --strict` (aún no ejecutado post-cambios, en validación final §8 del plan).

**Próximos pasos bloqueantes:**
1. Débora + Plataforma APB: **decidir motor de orquestación** (A/B/C en `PLAN_FASES_FUTURAS.md` Sección A).
2. Débora: OK explícito para commitar nuevos scripts/workflow `.github/workflows/human-checkpoint-poc.yml`.
3. GitHub: Configurar Environment `human-checkpoint` + required reviewers (`setup_github_environment.py` o UI).
4. Ejecutar #85 + #86 (auditorías de cumplimiento sobre APB.TRU + APB.API.SMS).
5. Validación final: `validate_repo.py --strict` + tests `python -m unittest discover tests`.

**Inventario:** 347 componentes (sin cambios — 3 scripts + 1 workflow + 1 handoff memo, cambios, no nuevos
componentes en `agents/`/`workflows/`/`skills/` que requieran ID). Los agentes #85/#86 ya existen desde
sesión anterior (estado `draft`).

**Nota sobre #88:** explícitamente pospuesto a sesión posterior (TruckCenter reejecución completa con vídeo + corrección H1).

---

## Sesión 25 — #39/#40 Dashboards + #41 Autonomía (2026-07-06)

**Participantes:** Débora Martín, Claude Haiku 4.5 (sesión parallel workstreams)

**Tipo:** Implementación + Análisis

### Workstream 1: #39/#40 — Dashboards Genéricos (COMPLETADO)

**Objetivo:** Generar skill + subagent para crear dashboards agnósticos (Power BI, Grafana) desde especificación natural.

**Entregables:**
- ✅ Skill `apb-plat-dashboards-generator-v1.0` (generador agnóstico)
- ✅ Subagent `apb-sub-dashboard-discovery-v1.0` (entrevista + reuso)
- ✅ Dashboard **Grafana JSON** (importable en 5 min)
- ✅ Dashboard **Power BI spec** (guía + DAX measures)
- ✅ **Runbook operativo** (SLAs, alertas, troubleshooting)

**Caso de uso (MVP):** QA Compliance Dashboard
- Origen: Sonar (coverage, bugs), Dependabot (vulnerabilities), Jira (resolution time)
- Metrics: test coverage%, High/Critical bugs, open vulnerabilities, MTTR
- Dimensions: app, environment (DEV/PRE/PROD), team
- Frecuencia: Real-time (Grafana) + Daily (Power BI)

**Hallazgos de reutilización:**
- Subagentes existentes encontrados (`apb-sub-obs-powerbi-v1.0`, `apb-sub-obs-grafana-v1.0`)
- Plantillas Grafana comunitarias identificadas
- Estrategia: CUSTOMIZE_TEMPLATE (Grafana) + BUILD_FROM_SCRATCH (Power BI)

**Próximos pasos:**
1. Probar dashboard Grafana JSON en vivo (requiere Prometheus/Azure Monitor)
2. Construir Power BI dataset desde spec (1-2 horas)
3. Validar alertas y SLAs en operación

---

### Workstream 2: #41 — Autonomía de Agentes (COMPLETADO)

**Objetivo:** Analizar qué 217 componentes pueden operar sin revisión humana previa (Nivel 2/3).

**Descubrimiento:**
- **350 componentes** mapeados (no 217)
- **Distribución:** Level 0 (1), Level 1 (318), Level 2 (31), Level 3/4 (0)
- **Candidatos identificados:** 3 (auditoría read-only, bajo riesgo)
  - `apb-agent-accessibility-auditor-v1.0`
  - `apb-ops-dependency-audit-v1.0`
  - `apb-wf-accessibility-audit-v1.0`

**Gaps críticos identificados:**
1. ❌ Sin timeout policy (agente puede colgarse indefinidamente)
2. ❌ Sin loop detection (ciclos no detectados)
3. ❌ Sin enforcement real (validación es solo metadata)
4. ❌ Sin async messaging (comunicación síncrona via Git/Jira)

**Recomendación:**
- NO promover a Nivel 2 hasta cerrar gaps
- Implementar enforcement en futuro
- Usar candidatos actuales como test case para validation

---

### Calidad & Validación

- ✅ `validate_repo.py --strict`: EXITOSO (0 errores, 10 warnings conocidos)
- ✅ 14 files changed, 2679 insertions
- ✅ Commit: 0788c9c

### Commits Relevantes

- `0788c9c`: feat: #39/#40 dashboards genéricos + #41 análisis autonomía

---

### Próxima Sesión

**Tema:** Prueba de implementación dashboard Power BI (construcción real dataset + import)

**Bloqueantes resueltos:**
- Especificación Power BI lista
- DAX measures documentadas
- Data model definido

**Bloqueantes pendientes:**
- Azure Monitor / Sonar credenciales para Grafana
- Acceso Power BI Service para deploy

---

*Cierre de sesión 2026-07-06*

---

## Sesión 26 — Estrategia de Optimización de Tokens (2026-07-06, continuación)

**Participantes:** Débora Martín, Claude Haiku 4.5

**Tipo:** Análisis estratégico + Documentación

**Solicitud:** "apunta para fases futuras, estrategias para optimizar consumo tokens por el framework"

### Entregable Principal

- ✅ **`discovery/ESTRATEGIA_OPTIMIZACION_TOKENS_2026-07-06.md`** (5 KB, completo)
  - 10 estrategias viables (priorizadas por impacto/esfuerzo)
  - Roadmap de 3 fases de implementación
  - Estimación de ahorro anual (30-50% en tokens/turno)
  - Checklist detallado para cada fase
  - Métricas de validación de impacto

### Resumen Ejecutivo de Estrategias

| # | Estrategia | Impacto | Esfuerzo | Prioridad |
|---|-----------|---------|----------|-----------|
| 1 | Caching YAML frontmatter | 15-20t | Bajo | 🔴 CRÍTICA |
| 2 | Workflows paralelos | 10-15% | Medio | 🔴 CRÍTICA |
| 3 | Lazy loading de archivos | 5-10t | Bajo | 🟡 ALTA |
| 4 | Dedup búsquedas Grep/Glob | 2-5t | Bajo | 🟡 ALTA |
| 5 | Batch processing análisis | 20-30% | Medio | 🟡 ALTA |
| 6 | Model selection inteligente | 15-25% | Bajo | 🟢 MEDIA |
| 7 | Context compression | 5-10% | Bajo | 🟢 MEDIA |
| 8 | Subagent registry | 10-20% | Medio | 🟢 MEDIA |
| 9 | Streaming resultados | 5-15% | Alto | 🔵 FUTURA |
| 10 | MCP caching | 2-5t | Bajo | 🔵 FUTURA |

**Ahorro teórico acumulado (Fases 1+2+3):** 30-50% tokens/sesión

### Roadmap de Implementación

**Fase 1 (1-2 semanas) — QUICK WINS**
- Caching frontmatter YAML
- Lazy loading con índices
- Dedup búsquedas
- Esfuerzo: ~4-6 horas
- Ahorro esperado: 20-35 tokens/turno

**Fase 2 (Semanas 3-4) — ARQUITECTURA**
- Workflow patterns para paralelismo
- Batch processing framework
- Model selection heuristics
- Esfuerzo: ~8-12 horas
- Ahorro esperado: +15-30% adicional

**Fase 3 (Mes 2) — AVANZADO**
- Subagent registry
- Context compression tuning
- Streaming + MCP caching (si disponible)
- Esfuerzo: ~12-16 horas
- Ahorro esperado: +10-20% adicional

### Insights Clave

1. **Context matters más que model size** — Haiku con buen contexto > Opus con mal contexto
2. **Paralelismo es gratis** — Workflows no cuestan más, ahorran tiempo y tokens
3. **Lazy > Eager** — Solo cargar lo necesario es ~10% más barato que full context
4. **Caching pequeño ahorra grande** — 180KB cache frontmatter → 20 tokens/turno ahorrados
5. **Batch > Sequential** — 50 items en 1 agente (5K tokens) vs 50 agentes (50K tokens)

### Artefactos Anexos

- Estimación de ahorro anual (416K tokens → 150K tokens con todas las fases)
- Baseline Sesión 25: ~45K tokens gastados, 2h ejecución
- Target post-optimización: ~25K tokens (-44%)

### Recomendaciones para Debate (Arquitectura APB)

1. **¿Adoptar todas las estrategias, o piloto Fase 1 primero?**
   - Recomendación: Piloto Fase 1 (4-6h, bajo riesgo)

2. **¿Reutilizar optimizer para workflows existentes (#77 PoC)?**
   - Recomendación: Sí, medir Sesión 25 vs post-optimización

3. **¿Formalizar "token budgets" por sesión?**
   - Recomendación: Sí, directiva +500k ya existe

### Próximas Acciones (Debate Débora)

- [ ] Revisar documento de estrategia
- [ ] Elegir modelo de implementación (piloto Fase 1 vs. full rollout)
- [ ] Decidir si priorizar caching YAML o workflows primero
- [ ] Asignar recursos para Fase 1

---

*Cierre de sesión 2026-07-06 (continuación)*

---

## Sesión 26 — Auditoría de cableado (#27/#28) + Agente de soporte funcional-técnico (2026-07-06)

**Participantes:** Débora Martín, Claude Sonnet 5

**Tipo:** Corrección de defecto + refuerzo de gobernanza + creación de componente

### Workstream 1: Auditoría de cableado agente/subagente↔skill/provider (COMPLETADO)

**Origen:** Débora detectó que `INFORME_RIESGOS_ARQ-3684_APB.API.FIL.md` citaba
`PROCEDURE_NONCOMPLIANCE_MANAGEMENT_v1.0` en la cabecera sin aplicar su contenido real —
la skill lo nombraba en prosa, sin ruta literal ni verbo de carga, a diferencia de
`PROCEDURE_RISK_EVALUATION` (que sí tenía un paso "Aplica" explícito y se aplicó a fondo).
Pidió revisar si el mismo patrón se repetía en otros agentes/skills y un mecanismo
permanente para que no volviera a ocurrir.

**Ejecutado:**
- Corregida la causa raíz en `apb-gov-org-risk-report-v1.0` (v1.4.0) y en la atribución de
  agente equivocada de `apb-agent-risk-exception-v1.0` (v1.1.0 — no tiene asignada esa skill;
  es competencia de `apb-agent-compliance-audit-v1.0`).
- `validate_repo.py` checks **#27** (procedimientos sin ruta literal) y **#28** (skill/provider
  usado sin declarar, generaliza el #27) — el #28 escanea `agents/` y `subagents/`.
- Auditoría manual de los 38 agentes + 35 subagentes: **6 gaps reales** corregidos
  (`apb-agent-business-analyst-v1.0`, `apb-agent-compliance-audit-v1.0`, `apb-agent-finops-v1.0`,
  `apb-agent-observability-v1.0`, `apb-sub-ops-azure-v1.0`, `apb-sub-obs-powerbi-v1.0`).
- `SCHEMA.md` v1.1.0: formaliza `skills`/`depends_on` como campos condicionales de `Subagent` §3.3.
- Informe `INFORME_RIESGOS_ARQ-3684_APB.API.FIL.md` corregido a v3 (ticket maestro JSM y
  justificación de negocio marcados como pendientes de confirmar, no inventados).

**Detalle completo:** [`PLAN_FASES_COMPLETADAS.md` #89](PLAN_FASES_COMPLETADAS.md).

**Verificación:** `validate_repo.py --strict` → 0 errores en cada paso · 60/60 tests.

---

### Workstream 2: Agente de soporte técnico para analistas funcionales (COMPLETADO)

**Objetivo:** Convertir en componente conforme al schema el borrador
`apb-agent-functional-technical-support-v1.0.md` que Débora ya había esbozado, más la skill que
le faltaba.

**Entregables:**
- Skill `apb-pm-jira-estimation-review-v1.0` (dominio `pm`): explica tickets Jira en lenguaje
  accesible, analiza complejidad, busca precedentes híbridos (Jira en vivo + catálogo del repo),
  y contrapropone valoración si supera el +25% de la media de precedentes.
- Catálogo `discovery/ESTIMATION_REFERENCES.md` (fichero seed).
- Agente `apb-agent-functional-technical-support-v1.0` reescrito conforme a convenciones.

**Decisiones de Débora:** catálogo en el repo (no Confluence/custom field); estimación en horas
(no story points); acceso a Jira vía `prov-jira-software-v1.0` (REST API, no MCP ni Rovo — ver
Workstream 3); umbral de contrapropuesta en +25% sobre la media de precedentes.

**Pendiente:** acceso real a histórico Jira (`HANDOFF_TECNICOS.md` ACC1).

**Detalle completo:** [`PLAN_FASES_COMPLETADAS.md` #90](PLAN_FASES_COMPLETADAS.md).

---

### Workstream 3: Reconciliación de providers Atlassian (COMPLETADO)

**Origen:** al escribir el Workstream 2 se afirmó (incorrectamente) que el acceso a Jira se hacía
"vía el conector MCP de Atlassian (Rovo)". Débora pidió reconciliar `prov-atlassian-v1.0` y
`prov-jira-software-v1.0`, que se solapaban.

**Hallazgo:** `prov-atlassian-v1.0` se llamaba *"Atlassian Rovo MCP"* pero su contenido siempre fue
REST CRUD genérico, sin relación con MCP ni Rovo. La integración real de Rovo (búsqueda semántica,
Rovo Agents vía Forge App) ya existía documentada aparte en `adapters/rovo/adapter-rovo-v1.0.md`
(Sesión 15) — pendiente de activación en APB (julio 2026). Ninguno de los dos providers Jira usa
MCP ni Rovo como transporte.

**Ejecutado:** renombrado `prov-atlassian-v1.0` → "Atlassian REST API (JSM + Confluence + Compass)"
(v1.1.0), tabla de diferenciación añadida a ambos providers (+ referencia a `adapter-rovo-v1.0`),
corregidas las 3 afirmaciones erróneas sobre MCP/Rovo introducidas en el Workstream 2. **No** se
fusionaron los providers (ambos tienen consumidores reales activos; el problema era de
nomenclatura, no de wiring roto).

**Detalle completo:** [`PLAN_FASES_COMPLETADAS.md` #91](PLAN_FASES_COMPLETADAS.md).

**Verificación:** `validate_repo.py --strict` → 0 errores · 60/60 tests.

---

### Workstream 4: Fusión real de providers Atlassian + revisión de Rovo (COMPLETADO)

**Petición de Débora:** "fusiona los providers. también asegúrate que el adapter para rovo es
correcto. necesitamos el mcp de atlassian + rovo?"

**Ejecutado:**
- `prov-atlassian-v1.0` → v2.0.0 (fusión con `prov-jira-software-v1.0`, ahora deprecado) → v2.1.0
  (corrección: se detectó que la fusión duplicaba Confluence, ya cubierto por un tercer provider
  ya existente, `prov-confluence-v1.0` — acotado a Jira Software+JSM+Compass).
- 10 ficheros consumidores actualizados (3 con wiring formal detectados por el check #25 al
  deprecar, 7 con mención en prosa).
- `adapter-rovo-v1.0` (v1.1.0) y `adapter-claude-v1.0` (v1.2.0) corregidos: el primero no
  reflejaba que Confluence ya no vive en `prov-atlassian-v1.0`; el segundo no mapeaba Atlassian a
  ningún mecanismo MCP pese a hacerlo con Azure/GitHub/Sonar — añadido como "⚠️ Parcial" en vez de
  darlo por hecho, sin conector MCP de Atlassian confirmado en este entorno de sesión.

**Respuesta a "¿necesitamos MCP de Atlassian + Rovo?":** no compiten — son direcciones distintas.
MCP de Atlassian sería el transporte (framework → Atlassian) si el tenant lo expone; Rovo
(`adapter-rovo-v1.0`) es la capa de IA + exposición del framework como Rovo Agents dentro de
Jira/Confluence, pendiente de activación en APB (julio 2026). Ambos son necesarios si se activan.

**Detalle completo:** [`PLAN_FASES_COMPLETADAS.md` #92](PLAN_FASES_COMPLETADAS.md).

**Pendiente de Débora:** confirmar si existe/se activará un servidor MCP de Atlassian real en el
tenant APB.

**Verificación:** `validate_repo.py --strict` → 0 errores · 60/60 tests · catálogo regenerado.

---

*Cierre de Sesión 26 (2026-07-06).*

---

## Sesión 27 — Plan MCP Server APB Agents consolidado + skill third-party supervision (2026-07-07)

**Participantes:** Débora Martín, Claude Sonnet 5

**Tipo:** Consolidación de documentación + creación de componente

**Solicitud:** "añade al plan por fases lo indicado en el proyecto [los dos ficheros
adjuntos `PLAN_MCP_SERVER_APB_v1.md` y `PLAN_MCP_SERVER_APB_FASES_1-7.md`] y las
funcionalidades de terceros de `roboflow/supervision`". Aclarado antes de ejecutar
(dos preguntas): (1) "el proyecto" = los propios ficheros adjuntos, no otra
decisión ya registrada; (2) `supervision` es una skill de terceros normal en el
catálogo, sin relación con el servidor MCP.

### Workstream 1: Consolidación del plan MCP Server APB Agents (COMPLETADO)

**Ejecutado:**
- Releídos y reverificados contra el repo real los 5 ficheros de contexto que el
  propio plan exige (`agents/apb-agent-ddd-v1.0.md`, `providers/prov-apb-knowledge-v1.0.md`,
  `scripts/invoke_agent.py`, `context/apb/SCHEMA.md`) — frontmatter y los "dos bloques
  Prompt de Sistema" confirmados como describía el plan original.
- Creado `discovery/PLAN_MCP_SERVER_APB.md`: consolida íntegramente (sin resumir)
  los dos documentos adjuntos (Fase 0 MVP local + Fases 1-7 con leyenda de
  confianza Seguro/Probable/Suposición), más una sección nueva "Vínculos con el
  resto del framework APB" que conecta el plan con **N8** (runtime de agentes en
  producción — este MCP server es el mecanismo que falta), **#78** (tagging
  `runtime: rovo`), `adapter-rovo-v1.0`, y aclara que no se solapa con los
  providers P1-P6 de `PLAN_FASES_FUTURAS.md` §B.2.
- `PLAN_FASES_FUTURAS.md`: añadidas 4 filas a Sección A (**MCP-1** a **MCP-4**,
  los 5 bloqueantes reales de las Fases 1-7 condensados en 4 decisiones), 1 fila
  a Sección B (Fase 0, ejecutable ya, ligada a N8), y notas de puntero en N8 y en
  el cierre de §B.2.

**No implementado en esta sesión:** el servidor MCP en sí (código, Dockerfile,
tests) — esta sesión fue de consolidación de planificación, no de construcción.
La Fase 0 queda en el backlog ejecutable (Sección B) para una sesión futura.

### Workstream 2: Skill de terceros — visión artificial (roboflow/supervision) (COMPLETADO)

**Verificación previa (no se asumió nada del enunciado del usuario):** grep
exhaustivo del repo confirmó que no existía ninguna mención previa a visión
artificial, cámaras, detección de objetos o tracking — no hay caso de uso APB
que justifique esta skill. Verificado vía API de GitHub: licencia **MIT**,
commit real `fd3de344dc9ba2dacd1e996ee6416b60d5e4d0d2` (rama `main`), repo activo
(~47k ⭐, no archivado).

**Ejecutado:**
- Creado `skills/third_party/roboflow/third-roboflow-supervision-v1.0.md`
  (dominio `development`, `status: draft`, `consumed_by` vacío). Cuerpo con
  Capacidades (anotación de detecciones/segmentación, tracking multi-objeto,
  análisis por zonas, conversión de datasets YOLO/COCO/Pascal VOC, métricas de
  evaluación), y una **Nota de gobernanza explícita**: sin caso de uso ni
  agente consumidor confirmado, no debe wirearse a ningún componente real sin
  que Arquitectura APB documente antes el caso de uso concreto (mismo
  tratamiento que `third-lum1104-knowledge-graph-v1.0`).

**Pendiente:** identificar (si Débora lo decide) un caso de uso real antes de
conectar esta skill a cualquier agente/workflow.

### Calidad & Validación

`scripts/generate_catalog.py` regenerado (364 componentes, +1 sobre los 363
previos: la skill `third-roboflow-supervision-v1.0`) ·
`scripts/validate_repo.py --strict` → **0 errores**, 10 warnings exentos
(`source_commit: unverified`, política `GOVERNANCE.md §4.2`) · **60/60 tests**
(`python -m unittest discover tests`).

**Inventario al cierre:** 364 componentes (57 skills terceros [+1 sobre las 56
previas], resto sin cambio — el plan MCP Server es documentación en
`discovery/`, no un componente catalogable).

---

*Cierre de Sesión 27 (2026-07-07).*

## Sesión 28 — Corrección de handoff + Agente de Valoración Técnica COSMIC/Horas-Perfil (2026-07-08)

**Participantes:** Débora Martín, Claude Sonnet 5

**Tipo:** Corrección documental + construcción de agente nuevo con metodología corporativa real

**Solicitud:** (1) "siguientes tareas pendientes que podríamos realizar" → ejecución
de 3 tareas de bajo riesgo detectadas como ya resueltas pero mal reflejadas en
`HANDOFF_TECNICOS.md`; (2) "vamos a mejorar el agente que permita valorar tareas
técnicas..." — construir un agente de valoración (COSMIC / Horas-Perfil) apoyado en
histórico real de Jira, aportando 3 documentos de metodología corporativa
(`Guía para valoración de desarrollos con Cosmic`, `ANEXO - Criterios de valoración`,
`OBSOLETO - Guía genérica`), datos reales de 12 meses de Jira, y un Excel
(`Catálogo de coste de tareas técnicas APB`) con la hoja de servicios USM/UEC/UTA.

### Workstream 1: Corrección de handoff desactualizado (COMPLETADO)

**Ejecutado:**
- `HANDOFF_TECNICOS.md`: verificado contra código real que **7 de 8 bugs** de la
  tabla §1 ya estaban resueltos (BUG-01, 02, 04, 05, 06, 07, 08) — el documento
  los listaba como pendientes. Hallazgos nuevos en la verificación: BUG-06
  (`telemetry.yml` ya usa rama + PR, no push directo a `main`) y BUG-08 (licencia
  `third-lum1104-knowledge-graph-v1.0` = MIT, ya verificada 2026-07-04, repo
  transferido de `Lum1104` a `Egonex-AI`). Solo BUG-03 (Design System, repo
  separado) sigue pendiente real.
- README.md: nueva sección "Relación con Otros Repositorios APB" documentando la
  deprecación de `apb-ai-skills` (DOC7).
- Commit `22c5af9`.

### Workstream 2: Agente de Valoración Técnica — COSMIC + Horas/Perfil + Catálogo USM/UEC/UTA (COMPLETADO)

**Hallazgo clave de planificación:** ya existía
`apb-pm-jira-estimation-review-v1.0` (Sesión 26) cubriendo búsqueda híbrida de
precedentes (Jira en vivo + catálogo) y regla de desviación >25% para tickets
técnicos — no se duplicó esa maquinaria, se extendió.

**Ejecutado:**
- `apb-disc-cosmic-v1.0` reescrita v1.0.0→v2.0.0: de ISO/IEC 19761 genérico a las
  reglas reales de la `Guía para valoración de desarrollos con Cosmic` vigente
  (checklist de validación, tablas E/X/R/W con inclusiones/exclusiones, catálogo
  de acciones, 6 ejemplos reales, sección de calibración interna no contractual
  con los factores del informe Rovo aportado por Débora, marcados explícitamente
  "no verificados").
- `apb-pm-jira-estimation-review-v1.0` ampliada v1.0.2→v1.1.0: de "solo tickets
  técnicos" a todo el sistema Horas/Perfil (incluye desarrollo funcional cuando
  el contrato de proveedor no usa COSMIC — caso real: proyectos Java/Sòstrat).
  Sustituida la guía obsoleta 2020-2022 por Tablas A/B de datos reales de 12
  meses de Jira aportados por Débora (7 categorías de desarrollo + 4 de tareas
  técnicas, con confianza ✅/⚠️/❌ por nº de tickets).
- `apb-pm-catalogo-servicios-v1.0` (nueva): catálogo real USM/UEC/UTA de 12
  servicios desatendidos + 11 servicios "bajo evento" del ciclo de construcción,
  extraído del Excel real de Débora.
- `apb-agent-valoracion-tecnica-v1.0` (nuevo): orquestador que aplica la
  clasificación ANEXO (Naturaleza × Modo) **solo como sugerencia, nunca forzada**
  — el enfoque (COSMIC/Horas-Perfil) lo elige el usuario, porque depende del
  contrato del proveedor, no solo de la naturaleza del trabajo.
- `discovery/ESTIMATION_REFERENCES.md`: sembrado con las tablas reales (antes 0
  entradas).
- Gap #8 de `PLAN_FASES_FUTURAS.md` (horas históricas para calibrar COSMIC↔horas)
  marcado **aportado, no 100% resuelto** — categorías con <50 tickets siguen
  indicativas; detalle en `PLAN_FASES_COMPLETADAS.md`.
- Commit `ae2b7a7`.

**Corrección de rumbo post-commit (Débora):** el catálogo USM/UEC/UTA no debía
estimar €/unidad vía referencias de mercado externas (día/hora de consultoría,
pricing SaaS) — el framework APB solo valora en horas o CFP. Se investigaron
referencias de mercado (España 2026: DevOps/SRE 40-90€/h freelance; benchmarks de
monitorización/SOC/backup-DR/FinOps/helpdesk) pero se descartaron por completo tras
la corrección. `apb-pm-catalogo-servicios-v1.0` v1.1.0 ahora estima **volumen de
horas de referencia** citando datos reales del Excel donde hay concepto equivalente
(Platform Engineering, Observabilidad, SRE, QA equipos desarrollo) y declarando
"sin dato real — pendiente" en el resto; la conversión horas→€ se deja a
`tarifa_hora_proveedor` (dato real del contrato, nunca estimado). `apb-agent-
valoracion-tecnica-v1.0` v1.0.0→v1.0.1 actualizado en consecuencia. Commit
`001c94c`.

### Calidad & Validación

`scripts/validate_repo.py --strict` → **0 errores**, 10 warnings exentos
(`source_commit: unverified`) tras cada commit · **68/68 tests** · catálogo
regenerado sin drift tras cada cambio.

**Inventario al cierre:** 367 componentes (184 skills APB [+1: `apb-pm-catalogo-
servicios-v1.0`], 57 skills terceros, 40 agentes [+1: `apb-agent-valoracion-
tecnica-v1.0`], 35 subagentes, 17 workflows, 23 providers, 7 wrappers, 4 adapters).

---

*Cierre de Sesión 28 (2026-07-08).*

## Sesión 29 — Cierre del lote de 32 planes de pruebas + auditoría y definición de infraestructura de ejecución (2026-07-10)

**Participantes:** Débora Martín, Claude Sonnet 5

**Tipo:** Continuación de sesión QA (uso del framework, no construcción) + corrección
de gobernanza documental tras un hallazgo real de la propia sesión

**Solicitud:** continuar el lote de 32 planes de pruebas (`quiero-que-ejecuten-el-
valiant-castle.md`, sesión anterior) desde donde quedó (INS); tras cerrarlo, Débora
preguntó "si quiero ejecutar un plan de pruebas completo, ¿tengo todo lo necesario?
k6, sonar, unitarias…" — la respuesta a esa pregunta reveló un gap de gobernanza real
que Débora pidió corregir con dos enfoques (inmediato/futuro), y después señaló
correctamente que ese contenido también debía reflejarse en `PLAN_FASES_FUTURAS.md`
y `HANDOFF_TECNICOS.md`, no solo en el estándar.

### Workstream 1: Cierre del lote de 32 planes de pruebas (fuera del repo del framework)

**Ejecutado (deliverable externo, no versionado en este repo):** los 32 planes de
pruebas del lote QA-continuación viven en `Proyectos\SDD - Framework desarrollo
asistido por IA\planes de pruebas\` (fuera de este repo, sin control de versiones).
Cerrados en esta sesión:
- **INS:** el `.md` (120 KB, con hallazgos de código reales sobre `APB.INS`) ya
  estaba completo de la sesión anterior; solo faltaba generar el `.html`
  (`scripts/generate_test_plan_html.py`).
- **MPT (AEATService):** única app del lote de 32 sin ninguna carpeta de salida.
  Generada desde cero cruzando la fuente Jira (42 casos) con el código real de
  `APB.API.MPT` (commit `d9ee4ea`): hallazgos relevantes incluyen que el "sello
  electrónico" documentado es en realidad autenticación mTLS de transporte (el
  método de firma WS-Security existe pero es código muerto), un contrato de
  respuesta real con 6 campos no documentados, un `AutoMapper`/DTO nunca invocado,
  y una contradicción confirmada por el propio test suite del repo entre el caso
  `MPT-R04` de la fuente Jira y el comportamiento real ante XML malformado.
- **Verificación de integridad de las 32 apps:** existencia de `.md`+`.html`,
  tamaño no-stub, footer estándar, cierre HTML correcto, `assets/` generado,
  matriz de pruebas con bloques reales — 32/32 conformes (33 carpetas de salida,
  la 33ª es `AOM_ARGOS-MDE`, el piloto original conservado sin tocar).
- `python scripts/validate_repo.py --strict` ejecutado como cierre del lote:
  0 errores, mismos 10 warnings exentos de siempre — repo del framework intacto
  (esta parte del trabajo no toca ningún fichero del framework).

### Workstream 2: Auditoría de infraestructura de ejecución + corrección de gobernanza (COMPLETADO)

**Hallazgo de la auditoría** (2 subagentes de investigación, verificación
componente a componente contra el repo real, no asumida):
- **k6:** `prov-k6-v1.0` en `draft`, `endpoint: "local://k6"` (CLI local, no cuenta
  k6 Cloud). `infra/azure-qa-runtime/k6/` es un runner Docker **genérico** —
  ningún script `.js` de ninguna aplicación existe todavía.
- **SonarQube:** conexión REST real y verificada (`http://gisplanolpre.port.apb.es:9001`,
  100 proyectos reales listados vía User Token) — pero es el **token personal de
  Débora** como variable de entorno local, solo consumido hoy por
  `scripts/generate_powerbi_dashboard.py`, sin gate de calidad ni confirmación de
  qué apps del lote de 32 tienen project key registrado.
- **Tests unitarios:** el CI del framework (`validate.yml`) solo valida el propio
  repo (`validate_repo.py`, `tests/`) — no orquesta ejecución de tests de ninguna
  app. Verificado por inspección directa: la mayoría de los ~68 repos clonados en
  `GitHub-Repos\otros\` sí tienen carpeta de tests propia; `APB.INS` es una
  excepción confirmada sin ningún test automatizado.
- **AKV:** `prov-akv-v1.0` con `endpoint` placeholder literal (`https://<vault-name>...`),
  cero vault provisionado, cero código resolutor — la referencia `AKV://<secret>`
  que todo plan de pruebas cita como "usuario de ejecución por defecto" **no es
  operativa hoy**.

**Ejecutado (corrección de gobernanza, en el repo del framework):**
- `context/apb/standards/TEST_PLAN_STANDARD.md` v1.6.1→**1.7.0**: nueva **§9.5
  "Estado real de la infraestructura de ejecución — inmediato vs. futuro"**, con
  dos tablas explícitas (qué es operativo hoy con destino `local` vs. qué falta
  aprovisionar para `ci-runner`/`azure-qa`). §9.2 enlazado (aviso de que la vía
  AKV no es operativa). Ítem nuevo en el checklist §10. Entrada en `Historial`.
- `context/apb/templates/TEST_PLAN.md`: §1.6 actualizado para no describir
  `AKV://<secret>` como resoluble por defecto sin remitir a §9.5.
- `discovery/HANDOFF_TECNICOS.md`: **QA2-1** y **QA3-2** ampliados para dejar
  explícito que ya no bloquean solo a TruckCenter, sino a los 32 planes del lote.
  **QA3-3** (nuevo): pasar Sonar de token personal a cuenta de servicio real —
  tarea de Plataforma/Ciberseguridad, no ejecutable por Claude.
- `discovery/PLAN_FASES_FUTURAS.md` Sección B (lo que Claude puede ejecutar sin
  más insumos): 2 filas nuevas — escribir los 32 scripts k6 reales, y confirmar
  qué apps del lote tienen project key en Sonar (ambas con la REST API ya
  verificada, sin depender de que Plataforma aprovisione nada). Ninguna se
  duplicó en `HANDOFF_TECNICOS.md` (regla explícita del propio documento: trabajo
  ejecutable por Claude va a Sección B, trabajo manual de Plataforma/Ciberseguridad
  va a `HANDOFF_TECNICOS.md`).
- Catálogo regenerado (`generate_catalog.py`): drift detectado en `INDEX.md`/
  `catalog/CATALOG.md` — no de esta sesión, venía de un cambio previo sin
  commitear en `providers/prov-sonar-v1.0.md` (fecha del MCP oficial SonarSource);
  sincronizado.

### Calidad & Validación

`scripts/validate_repo.py --strict` → **0 errores**, 10 warnings exentos
(`source_commit: unverified`) · **68/68 tests** · catálogo regenerado sin drift
tras la sincronización.

**Inventario al cierre:** sin cambio de componentes (367) — esta sesión modificó
gobernanza (estándar, plantilla, handoff, plan de fases) y generó contenido de
negocio fuera del repo (32 planes de pruebas), no creó/eliminó componentes del
catálogo.

**Pendiente real, no de esta sesión:** ver `HANDOFF_TECNICOS.md` QA2-1/QA3-2/QA3-3
(Plataforma/Ciberseguridad) y `PLAN_FASES_FUTURAS.md` Sección B (Claude, a demanda)
para el detalle de qué falta antes de poder ejecutar los 32 planes con
infraestructura centralizada en vez de local/manual.

---

*Cierre de Sesión 29 (2026-07-10).*

---

## Sesión 30 — Descomposición DDD completa de SÒSTRAT: 24 dossiers de aplicación final (2026-07-11 a 2026-07-14)

**Participantes:** Débora Martín, Claude Sonnet 5

**Tipo:** Uso del framework (discovery/DDD sobre un monolito real) — no construcción de componentes del catálogo

**Contexto:** tres commits consecutivos (`c631fc2` 2026-07-11, `c6dd4fe` 2026-07-13,
`5513c72` 2026-07-14) que ejecutan la descomposición DDD completa del monolito
`SOSTRAT-Sostrat-MJ8` con los agentes propios del framework
(`apb-agent-ddd-v1.0`, `apb-arch-decompose-v1.0`). **Esta bitácora no se
actualizó al cierre de ninguna de las tres** — corregido ahora (verificación
2026-07-14: los 24 dossiers existen, `validate_repo.py --strict` limpio,
68/68 tests OK, sin trabajo real pendiente de ejecución en los dossiers
mismos).

### 30.1 — Fase 0-4: primera pasada de descomposición (commit `c631fc2`, 2026-07-11)

14 apps, reparentadas contra el catálogo real de `apb-domain-catalog` (21
dominios, 21 bounded contexts), roadmap de 6 fases, 14 OpenAPI + 4 AsyncAPI
grounded en código real, testing strategy + threat model STRIDE, backlog Jira
de 16 épicas y ~45 pantallas UI. Fase 5 (Escalas) documentada como migración
hacia ARGOS, no extracción, con evidencia de código real (`MSG0004`,
`PortCallCreatedDto.cs`).

**Incidente de proceso detectado y corregido en la misma sesión** (documentado
en `discovery/ddd-sostrat-mj8/session-retro-2026-07-11.md`): se generaron 28
propuestas de dominio/BC asumiendo que `apb-domain-catalog` estaba vacío y que
la estructura de ficheros destino era la de los templates locales. Ambas
asunciones eran incorrectas — el submodule local estaba 4 commits por detrás
del remoto (21 dominios `proposed` ya existentes de una sesión previa,
solapando con 6 de los inventados), y la estructura real de ficheros
(`domains/<nombre>/domain.md` + `contexts/<contexto>.md`) estaba documentada
en el README del propio `apb-domain-catalog`, no leído hasta la tercera
pasada. Causa raíz: generar sobre supuestos plausibles de un sistema externo
en vez de leer su estado real. **Mitigación aplicada:** parche a
`agents/apb-agent-ddd-v1.0.md` (Fase 1 exige ahora `git fetch` + comparación
local vs. `origin/<rama>` antes de leer cualquier submodule como fuente de
verdad) + memoria de sesión guardada
(`feedback_verificar_repos_externos_antes_generar.md`).

**Deliberadamente no corregido en esa sesión** (requiere confirmación
explícita, no es un fix de contenido): el puntero del submodule
`domain-catalog` en `APB-IA-FRAMEWORK` sigue apuntando a `c90668d`
(desactualizado) — pendiente `git submodule update --remote domain-catalog` +
revisión de diff + commit explícito de Débora. Ver §30.4 Sección A del plan
de fases.

### 30.2 — Auditoría de cobertura + 6 BCs de Fase 6 + primeros 14 dossiers (commit `c6dd4fe`, 2026-07-13)

- `coverage-audit.md`: auditoría de cobertura funcional verificada contra
  inventario real de Struts/SOAP/Batch.
- `dead-code-register.md`: registro de código muerto con evidencia citada
  (líneas y ficheros concretos).
- **6 bounded contexts nuevos descubiertos en la auditoría** (no anticipados
  en la Fase 0-4): Buques, Operadores Portuarios, Efficiency Network,
  Servicios Auxiliares de Cruceros, Inspección SCPP, Trámites de Cliente —
  con sus specs OpenAPI/AsyncAPI.
- 14 de 24 dossiers de aplicación final generados (funcional + técnico +
  datos + arquitectura + pantallas + APIs + eventos + convivencia), marcados
  `[IA-GEN]` pendiente de validación humana.

### 30.3 — Cierre de los 24 dossiers + índice consolidado (commit `5513c72`, 2026-07-14)

Generados los 10 dossiers restantes (Manifiestos, Aduanas/Contenedores,
Facturación y Liquidaciones, Clavegueram, Buques, Servicios Auxiliares de
Cruceros, Inspección SCPP, Trámites de Cliente, Suministro Eléctrico a
Buques, Operadores Portuarios), cada uno **re-verificado campo a campo contra
el código real** de `SOSTRAT-Sostrat-MJ8`, no copiado de sesiones anteriores.
Renumerado `dossier-17-operadores-portuarios` → `dossier-23` (colisión de
numeración con `dossier-17-buques`).

Creado `discovery/ddd-sostrat-mj8/app-dossiers/INDEX.md` (v1.0.0): consolida
los 24 dossiers (23 apps finales + 1 documento de migración/retirada de
Escalas), con tabla de 4 bloqueantes de decisión y tabla de 9 correcciones
pendientes de propagar a specs/eventos/código muerto ya publicados.

**Hallazgos destacados de esta pasada final** (re-verificación campo a
campo, no solo generación):
- Motor de reglas de liquidación (`liquidadormm/`) con **153 referencias a
  Manifiestos** + 56 a Escalas — el acoplamiento más profundo de toda la
  serie.
- Fusión PIF/SCPP confirmada con evidencia de código (cero uso de
  `LlocDInspeccio` fuera de PIF/SCPP/Posicionament, comentarios que citan el
  ticket compartido PIF-1429).
- Fan-out real muy superior al documentado: Operadores Portuarios (369
  ficheros) y Buques (145 ficheros consumidores / 4x lo documentado).
- Entidad no documentada `CompteBancari` (IBAN/BIC, datos SEPA) ausente de la
  spec OpenAPI de Operadores Portuarios y del catálogo de eventos.
- Varias specs OpenAPI ya publicadas construidas sobre entidades equivocadas
  o nombres de campo incorrectos (detalle completo: tabla §4 del `INDEX.md`).
- 2 de 4 hallazgos de `dead-code-register.md` en Facturación son **falsos
  positivos** (overrides polimórficos activos en producción) — corregido en
  la propia auditoría antes de publicarse como definitivo.

### 30.4 — Pendientes reales derivados de esta serie (verificados 2026-07-14, no ejecutados hasta ahora)

Trasladados a `PLAN_FASES_FUTURAS.md` (secciones A y B) y a
`HANDOFF_TECNICOS.md` (§6, §7, §10.3) en esta misma sesión de cierre:

1. **4 bloqueantes de decisión de Arquitectura APB** (INDEX.md §3): fusión
   PIF+SCPP (con recomendación de extender a Posicionament), `parent_domain`
   compartido de Operadores Portuarios (#23) y Efficiency Network (#22),
   conflicto de planificación Clavegueram (EPIC-15 vs. EPIC-13B en
   `jira-backlog.md`), gap de evidencia de Aguada (modelo transaccional de
   escritura no existe en el checkout auditado).
2. **Corrección de specs ya publicadas** (INDEX.md §4): 9 correcciones
   acotadas (entidad equivocada, nombres de campo, campos faltantes) sobre
   specs OpenAPI/AsyncAPI/catálogo de eventos ya generados en sesiones
   anteriores — ejecutable por Claude sin insumos externos.
3. **Decisión de publicación**: el trabajo de esta serie contiene información
   de negocio real de SÒSTRAT (estructura de datos, integraciones externas,
   volúmenes) y sigue solo en commits locales — `apb-dmartin/APB-IA-FRAMEWORK`
   es un repositorio **público** en GitHub. Débora debe decidir destino de
   publicación antes de cualquier `git push` de estos commits (no se ha
   pusheado nada de esta serie).
4. **Bump del submodule `domain-catalog`** (ver §30.1) — pendiente de
   confirmación explícita de Débora, no ejecutado automáticamente.
5. **Formalización opcional**: no existe todavía una skill dedicada "dossier
   de aplicación" — el formato se sintetizó combinando 4 skills/agentes
   existentes. Si el formato resulta útil de forma recurrente en futuras
   descomposiciones de monolitos, considerar formalizarlo.

### Calidad y validación (verificación de cierre, 2026-07-14)

`scripts/validate_repo.py --strict` → 0 errores, 10 warnings exentos ·
`scripts/generate_catalog.py --check` → drift detectado y corregido (2 líneas
triviales: fecha de `INDEX.md` y `status` de `prov-sonar-v1.0` desincronizados
desde antes de esta serie, sin relación con SÒSTRAT) · `python -m unittest
discover tests` → **68/68 OK**.

**Inventario al cierre:** 367 componentes (sin cambio — los 24 dossiers y
demás artefactos DDD viven en `discovery/`, no son componentes catalogables
del framework).

---

*Cierre de Sesión 30 (2026-07-14).*
