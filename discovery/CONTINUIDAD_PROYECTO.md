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
| 15 | Integraciones Microsoft + gaps Rovo / M365 Copilot | ✅ **Completa** (2026-06-26) — artefactos en `openapi/`, `forge/`, `docs/`. Pendiente de equipo APB: ver `docs/HANDOFF_SESION15_INTEGRACIONES.md` |
| 16 | Skill de análisis de riesgos con procedimientos APB | ✅ **Completa** (2026-06-24) — `apb-gov-org-risk-report-v1.0` v1.2.0. Multi-framework (ENS, ISO 27001, NIST CSF 2.0, OWASP, RGPD, LCSP, WCAG 2.1 AA), recomendación APROBAR/DENEGAR/ESCALAR, plan de mitigación, alineado con `PROCEDURE_RISK_EVALUATION` + `PROCEDURE_NONCOMPLIANCE_MANAGEMENT_v1.0` |
| 13 | Cierre de pendientes históricos (plantillas, Jira, COSMIC, DDD, loops, guía agentes) | ⚠️ **Parcial** (2026-06-26, 7/10) — bloqueados: #6 (ejemplos Word/Excel de Débora), #8 (horas COSMIC históricas de Débora), #52 (mail Jira de Arquitectura) |
| 22/#47bis | Taxonomía de capacidades en agentes y skills | ✅ **Completa** (2026-06-26) — taxonomía APB normalizada en frontmatter |
| 18/#54 | Subagente entrevista DDD → análisis funcional completo | ✅ **Completa** (2026-06-26) — `apb-sub-ddd-interview-v1.0` v1.3.0: vocabulario portuario (Banco A) + corporativo (Banco B: RRHH, viajes, contratación, adm. electrónica, finanzas, jurídico), Fase 1-INT (integración entre sistemas), Fase 1-EVO (evolutivo de app existente), Fase 5 verificación APB-DOMAIN-CATALOG, Fase 6 generación artefacto |
| 23/#43 | Marcado IA obligatorio — retroactivo + mecanismos preventivos | ✅ **Completa** (2026-06-26) — 129/129 skills `apb-owned` marcadas con sección `## Marcado IA obligatorio (POLICY_AI_USAGE §6)`. Estándar: `context/apb/standards/AI_MARKING_STANDARD.md` (9 tipos de artefacto: código, SQL, OpenAPI, PR, Jira, Markdown, Word/PPT, email/Teams, IaC). Mecanismos preventivos duraderos: check #13 en `validate_repo.py` (ERROR si falta), sección en templates `SKILL_APB.md` y `AGENT.md`. Mecanismo IA: `CLAUDE.md` en raíz del repo. |
| 14 | Documentación por audiencias (Word) | ❌ Pendiente |

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
14. **Nuevo (Sesión 7):** verificar formalmente la licencia de
    `Lum1104/Understand-Anything` antes de cualquier uso productivo de
    `third-lum1104-knowledge-graph-v1.0` — requiere acceso directo al repo
    de origen, no solo búsqueda web.

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

- 208 componentes con frontmatter YAML válido: 107 skills APB, 44 skills
  terceros, 19 agentes, 13 subagentes, 7 workflows, 10 providers, 7
  wrappers, 2 adapters. (Sin cambio en el total respecto a Sesión 7: la
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



