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
