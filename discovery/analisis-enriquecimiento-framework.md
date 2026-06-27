# Análisis de Enriquecimiento del APB AI Framework
## Análisis completo: 26 agentes · 23 subagentes · 129 skills · 8 workflows

> **Generado por:** Claude (Anthropic), Sesión post-plan de acción  
> **Validado por:** _pendiente — completar nombre/rol antes de usar como referencia oficial_  
> **Fecha:** 2026-06-27  
> **Metodología:** Lectura completa de todos los componentes del framework (CATALOG.md + cada archivo individual). No se ha usado muestra representativa.

---

## Índice

1. [Diagnóstico de cobertura actual por dominio IT](#1-diagnóstico-de-cobertura-actual)
2. [Análisis por agente: gaps y mejoras (26/26)](#2-análisis-por-agente)
3. [Análisis por subagente: gaps y mejoras (23/23)](#3-análisis-por-subagente)
4. [Análisis por dominio de skills: gaps (129 skills)](#4-análisis-de-skills-por-dominio)
5. [Análisis por workflow: gaps (8/8)](#5-análisis-por-workflow)
6. [Nuevos agentes propuestos (9)](#6-nuevos-agentes-propuestos)
7. [Nuevos subagentes propuestos (8)](#7-nuevos-subagentes-propuestos)
8. [Nuevas skills propuestas por dominio (+38)](#8-nuevas-skills-propuestas)
9. [Nuevos workflows propuestos (9)](#9-nuevos-workflows-propuestos)
10. [Nuevos providers propuestos (5)](#10-nuevos-providers-propuestos)
11. [Resumen ejecutivo y priorización](#11-resumen-ejecutivo-y-priorización)

---

## 1. Diagnóstico de cobertura actual

### Distribución de calidad por tipo de componente

| Tipo | Total | Con prompt de sistema | Shallow (solo lista) | Observación |
|---|---|---|---|---|
| Agents | 26 | 26/26 | ~8/26 | Los más recientes (compliance-audit, tech-debt, incident-support) son notablemente más ricos que los primeros |
| Subagents | 23 | 19/23 | 4/23 | ops-iis-apache, ops-network, ops-oracle no tienen prompt explícito |
| Skills APB | 129 | ~75% | ~25% | Governance (100% deep), Discovery (100% shallow), resto mixto |
| Workflows | 8 | 8/8 | — | Todos tienen fases documentadas; SDD es el más completo (8 fases, 10 agentes) |

### Cobertura de dominios IT — visión general

| Área IT | Cobertura actual | Nivel |
|---|---|---|
| Ciclo de vida de software (SDD) | ✅ Completa | Alta |
| Arquitectura y diseño | ✅ Sólida | Alta |
| Code review y QA | ✅ Buena | Alta |
| Governance de artefactos y seguridad de diseño | ✅ Buena | Media-alta |
| Operaciones L1 (incidencias) | ⚠️ Solo L1 | Media |
| SRE y fiabilidad | ⚠️ Sin cambios ni capacidad | Media |
| FinOps y costes cloud | ❌ Muy superficial (1 skill) | Baja |
| Modernización de legacy | ⚠️ Análisis sí, DB migration no conectada | Media |
| Gestión de cambios ITIL | ❌ Ausente | Nula |
| Problem Management ITIL | ❌ Ausente | Nula |
| Gobierno de datos (RGPD/ENS) | ❌ Ausente | Nula |
| Accesibilidad (WCAG / RD 1112/2018) | ❌ Ausente (solo referenciada) | Nula |
| Kubernetes / AKS | ❌ Ausente (Docker sí) | Nula |
| Contratación pública (LCSP) | ❌ Ausente | Nula |
| API product management (lifecycle) | ❌ Diseño sí, gestión no | Nula |
| Gestión de proveedores técnicos | ❌ Ausente | Nula |
| Knowledge management operativo | ⚠️ Skill existe, no orquestada | Baja |
| Performance testing (k6) | ⚠️ Provider existe, sin skill ni agente | Baja |

---

## 2. Análisis por agente

### 2.1 `apb-agent-business-analyst-v1.0` — Business Analyst

**Skills actuales:** apb-disc-business-v1.0, apb-disc-reverse-doc-v1.0, apb-disc-enrich-req-v1.0, apb-plat-deliver-artifact-v1.0  
**Subagentes:** ninguno  
**Autonomía:** 1

**Gaps identificados:**

- `apb-disc-brainstorming-v1.0` existe en el catálogo pero **no está conectada a este agente**, siendo la skill de exploración creativa obligatoria antes de cualquier trabajo. Gap inconsistente con el principio "grill before code".
- `apb-disc-adversarial-v1.0` tampoco está conectada: el BA debería hacer devil's advocate sobre los requisitos que recoge, no solo documentarlos.
- No tiene ninguna capacidad de **user journey mapping** ni **value stream mapping**: las técnicas de análisis funcional son básicas (stories, requisitos) pero falta la capa de experiencia de usuario y flujo de valor.
- No tiene skill de **estimación funcional** (COSMIC está en el Spec Engineer, no en el BA que es quien tiene el contexto de negocio).
- No usa `apb-pm-product-analysis-v1.0` que existe para análisis de producto.

**Añadir:**

| Skill | Tipo | Justificación |
|---|---|---|
| `apb-disc-brainstorming-v1.0` | Existente (conectar) | Obligatoria antes de cualquier trabajo creativo |
| `apb-disc-adversarial-v1.0` | Existente (conectar) | Validación crítica de requisitos recogidos |
| `apb-pm-product-analysis-v1.0` | Existente (conectar) | Análisis de producto está separado pero complementa |
| `apb-disc-user-journey-v1.0` | Nueva | User journey maps para portales ciudadanos APB |
| `apb-disc-value-stream-v1.0` | Nueva | Mapeo de flujos de valor para procesos portuarios |

---

### 2.2 `apb-agent-catalog-manager-v1.0` — AI Catalog Manager

**Skills actuales:** apb-gov-catalog-v1.0, apb-gov-knowledge-v1.0  
**Subagentes:** ninguno  
**Autonomía:** 1

**Gaps identificados:**

- Solo 2 skills. Es el agente más delgado junto a FinOps. Gestiona el catálogo de IA pero no tiene capacidad de **validación** (`validate_repo.py` existe como script pero no hay skill que instrumente su lógica).
- No tiene conexión con `generate_catalog.py` para regenerar índices.
- No tiene skill de **métricas de gobierno**: el GOVERNANCE.md define targets (<30% en draft, <10 días aprobación) pero no hay skill que genere el cuadro de mando de esas métricas.
- No tiene skill de **auditoría de uso**: ¿qué agentes/skills se usan más? ¿Cuáles llevan >6 meses sin usarse? Datos de telemetría existen pero no se explotan.

**Añadir:**

| Skill | Tipo | Justificación |
|---|---|---|
| `apb-gov-framework-metrics-v1.0` | Nueva | Cuadro de mando: % en draft, tiempo aprobación, uso por componente |
| `apb-gov-framework-audit-v1.0` | Nueva | Detección de componentes obsoletos, sin uso, con inconsistencias entre versiones |
| `apb-gov-standards-v1.0` | Existente (conectar) | Validación de que los componentes cumplen los estándares del propio framework |

---

### 2.3 `apb-agent-cloud-architect-v1.0` — Cloud Architect

**Skills actuales:** apb-arch-cloud-infra-v1.0, apb-plat-cloud-ready-v1.0, apb-plat-terraform-v1.0, apb-plat-docker-v1.0, apb-plat-finops-v1.0, apb-plat-cicd-v1.0, apb-plat-deliver-artifact-v1.0  
**Subagentes:** ninguno  
**Autonomía:** 1

**Gaps identificados:**

- No tiene skill de **Kubernetes/AKS**. Para arquitecturas cloud-native modernas, Docker sin K8s cubre solo la containerización, no la orquestación.
- No tiene skill de **Azure Service Bus** en su dimensión de arquitectura (patrones de mensajería, topologías). La skill `apb-arch-event-driven-master-v1.0` existe pero no está conectada aquí.
- No tiene skill de **Azure Entra ID / Zero Trust** para arquitecturas de identidad federada. La seguridad cloud está en Security Architect, pero el Cloud Architect diseña la infraestructura sin herramientas de identidad.
- No tiene subagentes. Para un agente que genera diseños de infraestructura complejos, la especialización por servicio Azure (networking, compute, storage, identity) sería valiosa.
- La FinOps skill conectada (`apb-plat-finops-v1.0`) está en la capa de plataforma, no en la de arquitectura: las decisiones de diseño que impactan el coste (reserved instances vs. pay-as-you-go, tier de servicio) deberían estar disponibles en fase de diseño.

**Añadir:**

| Skill | Tipo | Justificación |
|---|---|---|
| `apb-plat-k8s-v1.0` | Nueva | AKS architecture: node pools, ingress, HPA, PDB, network policies |
| `apb-arch-event-driven-master-v1.0` | Existente (conectar) | Skill maestro de eventos que no está conectada al Cloud Architect |
| `apb-plat-azure-servicebus-v1.0` | Nueva | Configuración Service Bus desde perspectiva de diseño |
| `apb-plat-secret-rotation-v1.0` | Nueva | Especificación de rotación de secretos en Key Vault |

---

### 2.4 `apb-agent-code-reviewer-v1.0` — Code Reviewer

**Skills actuales:** apb-dev-code-review-v1.0, apb-dev-code-review-gate-v1.0, apb-dev-review-advanced-v1.0, apb-dev-openspec-review-v1.0, apb-dev-api-standard-v1.0  
**Subagentes:** ninguno  
**Autonomía:** 1

**Gaps identificados:**

- `apb-dev-code-review-v1.0` cubre C#/.NET bien pero **no hay skill de code review para Python/Django** (existe apb-dev-gis-django-v1.0 en el Implementer pero no en el Code Reviewer).
- No tiene skill de **revisión de seguridad de código** (SAST): `apb-sub-qa-security-v1.0` está en el QA Automation agent, no aquí. El code reviewer debería poder verificar reglas de seguridad SonarQube.
- No tiene skill de **revisión de tests**: revisa el código pero no la calidad del test coverage ni la cobertura de los casos de prueba.
- No usa `apb-dev-surgical-changes-v1.0` para asegurar que el PR toca solo lo necesario.
- No tiene skill de `apb-dev-impact-analysis-v1.0` para analizar qué rompe el PR revisado.

**Añadir:**

| Skill | Tipo | Justificación |
|---|---|---|
| `apb-dev-review-tl-v1.0` | Existente (conectar) | Perspectiva de Tech Lead, complementa al review básico |
| `apb-dev-impact-analysis-v1.0` | Existente (conectar) | ¿Qué rompe este PR? Esencial en un reviewer |
| `apb-dev-surgical-changes-v1.0` | Existente (conectar) | Detectar scope creep en un PR es función del reviewer |
| `apb-dev-gis-django-v1.0` | Existente (conectar) | Review de código Python/Django |
| `apb-sec-sast-v1.0` | Nueva | Interpretación de hallazgos de seguridad en SonarQube |

---

### 2.5 `apb-agent-compliance-audit-v1.0` — Compliance Audit

**Skills actuales:** apb-gov-org-risk-report-v1.0, apb-gov-policy-check-v1.0, apb-sec-ens-v1.0, apb-gov-ai-risk-gate-v1.0, apb-sec-owasp-v1.0, apb-sec-threat-model-v1.0, apb-dev-grill-before-code-v1.0, apb-gov-jira-evidence-v1.0, apb-plat-ms-notify-v1.0, apb-plat-sharepoint-io-v1.0, apb-plat-deliver-artifact-v1.0  
**Subagentes:** ninguno  
**Autonomía:** 2

**Evaluación:** El agente más completo y mejor diseñado del framework. Flujo, grill, fases paralelas, puntos de control humano explícitos, entrega múltiple. Es el agente de referencia en calidad de diseño.

**Gaps menores:**

- No incluye `apb-qa-accessibility-v1.0` (nueva): WCAG 2.1 está citado como marco normativo en el agente pero no hay skill que lo instrumente. APB como organismo público tiene obligación legal (RD 1112/2018).
- No incluye `apb-gov-lcsp-check-v1.0` (nueva): para sistemas adquiridos o contratados, la verificación de cumplimiento LCSP debería ser parte del compliance.
- No incluye `apb-gov-dpia-v1.0` (nueva): la EIPD/DPIA del RGPD art. 35 está implícita en la auditoría pero no instrumentada como skill específica.

---

### 2.6 `apb-agent-ddd-v1.0` — DDD Domain Discovery

**Skills actuales:** apb-ops-telemetry-emit-v1.0, apb-gov-ai-risk-gate-v1.0  
**Subagentes:** apb-sub-ddd-code-v1.0, apb-sub-ddd-db-v1.0, apb-sub-ddd-doc-v1.0, apb-sub-ddd-spec-v1.0, apb-sub-ddd-interview-v1.0  
**Autonomía:** 1

**Evaluación:** Diseño inteligente — delega el trabajo real a 5 subagentes especializados. El agente coordina, los subagentes analizan. Las skills directas son las transversales (telemetría, riesgo IA).

**Gaps:**

- Cuando el domain catalog tenga dominios aprobados, este agente necesitará una skill de **consulta y cruce contra el catálogo** para evitar duplicados. Hoy solo tiene `apb-gov-ai-risk-gate-v1.0` como control.
- No tiene skill de **síntesis cross-subagente**: los 5 subagentes producen 5 salidas, ¿hay instrucción de cómo consolidarlas? Un `apb-disc-domain-synthesis-v1.0` nuevo sería útil.
- El subagente de entrevista (`apb-sub-ddd-interview-v1.0`) hace domain storytelling pero no tiene skill de **event storming** para sesiones más estructuradas — esa skill está en el Domain Architect agent.

---

### 2.7 `apb-agent-documentation-v1.0` — Documentation

**Skills actuales:** apb-doc-adr-v1.0, apb-doc-swagger-v1.0, apb-doc-aipimanager-v1.0, apb-doc-manual-v1.0, apb-gov-evidence-v1.0, apb-gov-jira-evidence-v1.0, apb-plat-deliver-artifact-v1.0  
**Subagentes:** ninguno  
**Autonomía:** 1

**Gaps:**

- No tiene `apb-doc-adr-v1.0` para eventos (tiene la de arquitectura pero no la de eventos CloudEvents/AsyncAPI, que sería `apb-doc-event-specs-v1.0` — esta sí existe pero no está conectada al agente).
- No tiene skill de **changelog automático**: cuando se modifica un componente, el agente debería poder generar el registro de cambios.
- No tiene skill de **release notes**: distinto al PR documentation, las release notes van a usuarios finales.
- No tiene subagente Confluence: toda la documentación se entrega como archivo, pero no hay integración directa para publicar en Confluence.
- No tiene skill de **onboarding de desarrolladores**: guías de setup, arquitectura, convenciones para alguien nuevo en un proyecto.

**Añadir:**

| Skill | Tipo | Justificación |
|---|---|---|
| `apb-doc-event-specs-v1.0` | Existente (conectar) | Specs CloudEvents/AsyncAPI, no está conectada |
| `apb-doc-changelog-v1.0` | Nueva | Generación de changelog semántico desde commits/PRs |
| `apb-doc-release-notes-v1.0` | Nueva | Release notes orientadas a usuario final |
| `apb-doc-onboarding-v1.0` | Nueva | Guía de onboarding de desarrollador en un proyecto |
| `apb-sub-doc-confluence-v1.0` | Subagente nuevo | Publicar documentación directamente en Confluence |

---

### 2.8 `apb-agent-domain-architect-v1.0` — Domain Architect

**Skills actuales:** apb-arch-ddd-v1.0, apb-arch-event-storming-v1.0, apb-disc-ddd-legacy-v1.0, apb-disc-reverse-code-v1.0, apb-plat-deliver-artifact-v1.0  
**Subagentes:** ninguno  
**Autonomía:** 1

**Gaps:**

- No tiene skill de **context mapping**: las relaciones entre bounded contexts (upstream/downstream, ACL, Open Host Service, etc.) son el siguiente paso tras identificar los contextos. DDD estratégico sin context map está incompleto.
- No tiene skill de **team topology**: en proyectos APB grandes, la organización de equipos debería seguir al modelo de dominio (ley de Conway). Esto es DDD estratégico aplicado a la organización.
- No tiene `apb-disc-brainstorming-v1.0` para la fase exploratoria.

**Añadir:**

| Skill | Tipo | Justificación |
|---|---|---|
| `apb-arch-context-mapping-v1.0` | Nueva | Relaciones entre bounded contexts: patrones ACL, OHS, CF, Published Language |
| `apb-disc-brainstorming-v1.0` | Existente (conectar) | Fase exploratoria antes de modelar |

---

### 2.9 `apb-agent-finops-v1.0` — FinOps

**Skills actuales:** apb-plat-finops-v1.0, apb-plat-deliver-artifact-v1.0  
**Subagentes:** ninguno  
**Autonomía:** 1

**Evaluación:** El agente más delgado del catálogo, junto a Catalog Manager. Con 1 sola skill funcional no puede hacer chargeback, alerting, análisis de reservas ni multi-cloud comparison.

**Gaps críticos:**

- No tiene skill de **alertas de budget**: la `apb-plat-finops-v1.0` solo analiza, no configura alertas.
- No tiene skill de **chargeback/showback**: imprescindible para que TI pueda rendir cuentas del gasto cloud por proyecto, equipo o dominio.
- No usa `third-google-finobs-multicloud-v1.0` (ya en el catálogo, aprobada) que cubre comparativa multi-cloud.
- No tiene subagente para Azure Cost Management API.
- No tiene skill de **análisis de reservas y Hybrid Benefit**: Azure ofrece descuentos significativos por reservas a 1/3 años y por licencias Windows existentes, que no están instrumentados.

**Añadir:**

| Componente | Tipo | Justificación |
|---|---|---|
| `apb-plat-finops-alerting-v1.0` | Nueva | Configuración de alertas de budget y anomalías en Azure Cost Management |
| `apb-plat-finops-chargeback-v1.0` | Nueva | Allocación de costes por proyecto/equipo, estrategia de tagging |
| `apb-plat-finops-reservations-v1.0` | Nueva | Análisis de reservas, Hybrid Benefit, Savings Plans |
| `third-google-finobs-multicloud-v1.0` | Existente (conectar) | Ya aprobada, no está conectada |
| `apb-ops-dependency-audit-v1.0` | Existente (conectar) | Detectar recursos huérfanos (sin proyecto asignado) |
| `apb-sub-finops-azure-v1.0` | Subagente nuevo | Especialista Azure Cost Management API |
| `prov-azure-cost-v1.0` | Provider nuevo | Azure Cost Management API separada del Azure MCP genérico |

---

### 2.10 `apb-agent-governance-v1.0` — Governance

**Skills actuales:** apb-gov-standards-v1.0, apb-gov-compliance-v1.0, apb-gov-policy-check-v1.0, apb-gov-arch-ref-v1.0, apb-gov-catalog-v1.0, apb-gov-knowledge-v1.0, apb-gov-evidence-v1.0  
**Subagentes:** apb-sub-gov-standards-v1.0  
**Autonomía:** 1

**Gaps:**

- No tiene skill de **gobierno de datos**: datos como activo (clasificación, linaje, retención) no están instrumentados.
- No tiene skill de **gobierno de modelos IA**: qué modelos usa APB, en qué versión, qué cambios en el modelo afectan a qué agentes.
- No tiene skill de **gobierno de proveedores técnicos**: evaluación técnica de terceros en el contexto LCSP.
- No tiene `apb-gov-spec-sync-v1.0` conectada, que mantiene specs en sinc con código.

**Añadir:**

| Skill | Tipo | Justificación |
|---|---|---|
| `apb-gov-data-classification-v1.0` | Nueva | Clasificación de datos según RGPD y ENS |
| `apb-gov-ai-model-lifecycle-v1.0` | Nueva | Versión, cambios, impacto de modelos IA usados en APB |
| `apb-gov-lcsp-check-v1.0` | Nueva | Verificación LCSP en contratación tecnológica |
| `apb-gov-spec-sync-v1.0` | Existente (conectar) | Gobernanza implica que las specs estén sincronizadas |

---

### 2.11 `apb-agent-implementer-v1.0` — Implementer

**Skills actuales:** apb-dev-code-base-v1.0, apb-dev-micro-base-v1.0, apb-dev-implement-v1.0, apb-dev-autocorrect-v1.0, apb-dev-review-tl-v1.0, apb-dev-openspec-review-v1.0, apb-dev-sql-fix-v1.0, apb-dev-pr-doc-v1.0, apb-dev-legacy-mapper-v1.0, apb-dev-template-update-v1.0, apb-dev-sonar-clean-v1.0, apb-dev-api-standard-v1.0, apb-dev-devexpress-front-v1.0, apb-dev-gis-django-v1.0, apb-plat-deliver-artifact-v1.0  
**Subagentes:** apb-sub-dev-net-v1.0, apb-sub-dev-devexpress-v1.0, apb-sub-dev-django-v1.0, apb-sub-dev-sql-v1.0  
**Autonomía:** 1

**Evaluación:** El agente más rico del catálogo en skills (15) y subagentes (4). Bien instrumentado. Gaps menores.

**Gaps:**

- `apb-sub-dev-parallel-v1.0` existe como subagente de despacho paralelo pero **no está en la lista de subagentes del Implementer**. Este es el subagente que permite implementar tareas independientes en paralelo, clave para acelerar el desarrollo.
- No tiene skill de **accesibilidad en implementación**: cuando implementa interfaces DevExtreme, no verifica WCAG. La responsabilidad recae en QA, pero el implementer podría prevenirlo.
- No tiene skill de **test coverage check**: implementa y auto-corrige, pero no verifica si el test coverage supera el umbral corporativo.

**Añadir:**

| Componente | Tipo | Justificación |
|---|---|---|
| `apb-sub-dev-parallel-v1.0` | Existente (conectar) | El subagente de despacho paralelo existe pero no está en la lista del agente |
| `apb-dev-frontend-devexpress-events-v1.0` | Existente (conectar) | Skill de DevExtreme para eventos, no conectada al implementer |
| `apb-dev-implementation-patterns-v1.0` | Existente (conectar) | Catálogo de patrones, no conectado al implementer principal |

---

### 2.12 `apb-agent-incident-support-v1.0` — Incident Support

**Skills actuales:** apb-ops-incident-triage-v1.0, apb-ops-incident-diagnose-v1.0, apb-ops-incident-escalate-v1.0, apb-plat-ms-notify-v1.0  
**Subagentes:** apb-sub-ops-oracle-v1.0, apb-sub-ops-iis-apache-v1.0, apb-sub-ops-network-v1.0, apb-sub-ops-azure-v1.0  
**Autonomía:** 2

**Evaluación:** Muy bien diseñado para L1. Cobertura tecnológica correcta (Oracle, IIS/Apache, Network, Azure). El gap está en lo que pasa después del escalado.

**Gaps:**

- No tiene skill de **problem management**: detecta incidencias recurrentes pero no puede abrir un problema ITIL ni documentar un known error.
- No tiene subagente para **Azure Service Bus**: el stack APB usa Service Bus (Azure Service Bus está en la tech stack), y los problemas de mensajería (dead-letter, backlog, consumers muertos) son frecuentes.
- El ciberincidente queda explícitamente excluido: "derivar al equipo de seguridad APB" sin más instrumentación. Debería haber al menos un triage de ciberincidente básico.

**Añadir:**

| Componente | Tipo | Justificación |
|---|---|---|
| `apb-ops-problem-management-v1.0` | Nueva | Detectar patrón, abrir problema ITIL, documentar known error |
| `apb-sub-ops-servicebus-v1.0` | Subagente nuevo | Azure Service Bus: dead-letter, backlog, consumers |

---

### 2.13 `apb-agent-meta-builder-v1.0` — Meta Builder

**Skills actuales:** apb-gov-standards-v1.0, apb-gov-catalog-v1.0, apb-dev-grill-before-code-v1.0, apb-dev-atomic-plan-v1.0, apb-dev-simplicity-first-v1.0, apb-dev-surgical-changes-v1.0, apb-dev-verify-before-done-v1.0, apb-plat-doc-to-markdown-v1.0  
**Autonomía:** 1

**Evaluación:** El agente que construye el propio framework. Bien diseñado con principios de construcción. El gap más importante está en la validación.

**Gaps:**

- No usa `validate_repo.py` ni tiene una skill que instrumente la validación de los componentes que genera.
- No tiene skill de **testing de componentes**: el `apb-qa-framework-v1.0` existe para validar la corrección de componentes del framework, pero no está conectada al meta-builder.

**Añadir:**

| Skill | Tipo | Justificación |
|---|---|---|
| `apb-qa-framework-v1.0` | Existente (conectar) | El meta-builder debería auto-validar los componentes que genera |

---

### 2.14 `apb-agent-modernization-v1.0` — Modernization Architect

**Skills actuales:** apb-disc-reverse-code-v1.0, apb-disc-ddd-legacy-v1.0, apb-arch-decompose-v1.0, apb-dev-legacy-mapper-v1.0, apb-disc-epic-mono-v1.0, apb-qa-post-migration-v1.0, apb-plat-deliver-artifact-v1.0  
**Autonomía:** 1

**Gaps:**

- No tiene `apb-plat-db-migration-v1.0` conectada: la modernización de un legacy implica casi siempre migración de base de datos, pero la skill está en Platform Engineer, no aquí.
- No tiene skill de **strangler fig pattern**: hay `apb-arch-decompose-v1.0` que descompone el monolito, pero la ejecución del strangler fig (migración gradual mientras el legacy sigue activo) requiere una skill más específica de coexistencia.
- No tiene skill de **evaluación de riesgo de migración**: cuánto cuesta técnicamente modernizar vs. reescribir vs. mantener. `apb-sec-risk-analysis-v1.0` existe para seguridad pero no para riesgo técnico de migración.

**Añadir:**

| Skill | Tipo | Justificación |
|---|---|---|
| `apb-plat-db-migration-v1.0` | Existente (conectar) | La modernización sin migración de BD es incompleta |
| `apb-disc-reverse-doc-v1.0` | Existente (conectar) | Análisis de documentación del legacy, complementa reverse-code |

---

### 2.15 `apb-agent-observability-v1.0` — Observability

**Skills actuales:** apb-ops-observability-v1.0, apb-ops-telemetry-emit-v1.0, apb-gov-ai-risk-gate-v1.0, apb-plat-doc-to-markdown-v1.0  
**Subagentes:** apb-sub-obs-powerbi-v1.0, apb-sub-obs-grafana-v1.0  
**Autonomía:** 1

**Evaluación:** Bien orientado a primer setup de observabilidad. La descripción menciona "agnóstico de fuente de datos: Sonar, VMware, Azure Monitor, bases de datos APB, IA framework, etc." que es una ambición amplia bien planteada.

**Gaps:**

- No tiene skill de **SLO monitoring**: `apb-ops-slo-design-v1.0` está en el SRE Agent, no aquí. El agente de observabilidad debería poder configurar alertas sobre SLOs definidos.
- No tiene subagente de **Azure Monitor** (apb-sub-ops-azure-v1.0 está en el SRE Agent, no aquí, a pesar de que la fuente de datos principal del observability agent es APBFrameworkTelemetry_CL en Azure Monitor).
- No tiene skill de **diseño de alertas**: diferente de diseñar dashboards, el alerting requiere definir umbrales, severidades, escalados, y runbooks asociados.

**Añadir:**

| Componente | Tipo | Justificación |
|---|---|---|
| `apb-sub-ops-azure-v1.0` | Existente (conectar) | Es la fuente de datos principal, pero el subagente está solo en SRE |
| `apb-ops-slo-design-v1.0` | Existente (conectar) | Monitoring sin SLOs no tiene objetivo |
| `apb-ops-alerting-design-v1.0` | Nueva | Diseño de alertas: umbrales, severidades, escalado, runbook asociado |

---

### 2.16 `apb-agent-platform-engineer-v1.0` — Platform Engineer

**Skills actuales:** apb-plat-cicd-v1.0, apb-plat-docker-v1.0, apb-plat-db-migration-v1.0, apb-plat-terraform-v1.0, apb-plat-cloud-ready-v1.0, apb-ops-observability-v1.0, apb-plat-deliver-artifact-v1.0  
**Subagentes:** apb-sub-plat-jenkins-v1.0, apb-sub-plat-ghactions-v1.0  
**Autonomía:** 1

**Gaps:**

- No tiene skill ni subagente de **Kubernetes/AKS**: la roadmap cloud implica AKS, y el Platform Engineer es quien genera los manifiestos de despliegue.
- No tiene skill de **Azure Service Bus**: configuración de namespaces, topics, subscriptions, políticas de retry, alertas. El stack lo usa pero no hay skill.
- No tiene skill de **rotación de secretos**: el framework referencia Key Vault pero no hay instrumentación del proceso de rotación (90 días según GOVERNANCE.md).
- No tiene skill de **environment promotion**: el proceso de promoción de artefactos entre entornos (dev→staging→prod) con sus checks, aprobaciones y rollback.

**Añadir:**

| Skill | Tipo | Justificación |
|---|---|---|
| `apb-plat-k8s-v1.0` | Nueva | Manifiestos K8s, Helm charts, Network Policies para AKS |
| `apb-plat-azure-servicebus-v1.0` | Nueva | Configuración Service Bus: topics, subscriptions, retry, DLQ |
| `apb-plat-secret-rotation-v1.0` | Nueva | Especificación automatización rotación Key Vault (cumple GOVERNANCE.md §secretos) |
| `apb-plat-environment-promotion-v1.0` | Nueva | Proceso de promoción dev→staging→prod con gates |
| `apb-sub-ops-k8s-v1.0` | Subagente nuevo | Diagnóstico AKS: pods, deployments, HPA, logs, eventos |

---

### 2.17 `apb-agent-qa-auto-v1.0` — QA Automation

**Skills actuales:** apb-qa-test-plan-v1.0, apb-qa-test-strategy-v1.0, apb-qa-test-auto-v1.0, apb-qa-unit-test-gen-v1.0, apb-qa-anonymize-v1.0, apb-qa-post-migration-v1.0, apb-qa-release-ready-v1.0, apb-plat-deliver-artifact-v1.0  
**Subagentes:** apb-sub-qa-unit-v1.0, apb-sub-qa-e2e-v1.0, apb-sub-qa-security-v1.0  
**Autonomía:** 2

**Gaps:**

- No tiene skill de **performance testing con k6**: el provider `prov-k6-v1.0` existe en el catálogo pero no hay ninguna skill que lo instrumente. El QA Agent no puede diseñar ni ejecutar tests de carga.
- No tiene skill de **contract testing**: para verificar contratos entre servicios en arquitecturas de microservicios (Pact o similar).
- No tiene skill de **accesibilidad**: WCAG 2.1 testing debería ser parte del QA Automation.
- No tiene skill de **mutation testing**: verificar la calidad de los tests unitarios mutando el código.
- `apb-qa-tdd-v1.0`, `apb-qa-readiness-check-v1.0`, `apb-qa-validation-e2e-v1.0`, `apb-qa-testing-strategy-v1.0`, `apb-qa-pipeline-v1.0`, `apb-qa-framework-v1.0`, `apb-qa-tdd-v1.0`, `apb-qa-verification-before-completion-v1.0` existen en el catálogo pero **no están conectadas al agente**.

**Añadir:**

| Componente | Tipo | Justificación |
|---|---|---|
| `apb-qa-tdd-v1.0` | Existente (conectar) | TDD existe pero no está en el QA Agent |
| `apb-qa-readiness-check-v1.0` | Existente (conectar) | Gate de readiness antes de implementar |
| `apb-qa-testing-strategy-v1.0` | Existente (conectar) | Estrategia de testing para eventos, no conectada |
| `apb-qa-pipeline-v1.0` | Existente (conectar) | Evaluación de calidad del pipeline CI/CD |
| `apb-qa-performance-v1.0` | Nueva | Tests de carga con k6: escenarios, thresholds, análisis |
| `apb-qa-contract-testing-v1.0` | Nueva | Consumer-driven contract testing (Pact) |
| `apb-qa-accessibility-v1.0` | Nueva | WCAG 2.1/2.2 audit automatizado |

---

### 2.18 `apb-agent-release-manager-v1.0` — Release Manager

**Skills actuales:** apb-qa-release-ready-v1.0, apb-gov-evidence-v1.0, apb-gov-jira-evidence-v1.0, apb-plat-deliver-artifact-v1.0  
**Subagentes:** ninguno  
**Autonomía:** 1

**Evaluación:** El agente más delgado para su responsabilidad crítica. El Release Manager es el gate final antes de producción, pero solo tiene 4 skills.

**Gaps críticos:**

- No tiene skill de **checklist de despliegue**: pasos detallados antes, durante y después del despliegue.
- No tiene skill de **rollback plan**: cómo revertir si el despliegue falla.
- No tiene skill de **comunicación de release**: notificar a stakeholders, generar release notes, actualizar changelog.
- No tiene conexión con el proceso de cambios (Change Management): el release debería abrir un RFC o verificar que hay uno aprobado.
- No tiene `apb-plat-deployment-finish-v1.0` conectada — esa skill existe exactamente para verificar y cerrar el proceso de despliegue pero no está en el Release Manager.

**Añadir:**

| Skill | Tipo | Justificación |
|---|---|---|
| `apb-plat-deployment-finish-v1.0` | Existente (conectar) | La skill de cierre de deployment existe pero no está aquí |
| `apb-plat-ms-notify-v1.0` | Existente (conectar) | Notificación post-release a stakeholders |
| `apb-doc-release-notes-v1.0` | Nueva | Release notes para usuarios finales |
| `apb-ops-change-management-v1.0` | Nueva | Verificación de RFC aprobado antes de despliegue |

---

### 2.19 `apb-agent-risk-exception-v1.0` — Risk & Exception

**Skills actuales:** apb-sec-risk-analysis-v1.0, apb-sec-risk-policies-v1.0, apb-gov-policy-check-v1.0, apb-plat-deliver-artifact-v1.0  
**Subagentes:** ninguno  
**Autonomía:** 1

**Gaps:**

- No tiene `apb-gov-jira-evidence-v1.0`: gestiona excepciones pero no puede crear el ticket Jira de excepción. Esta skill está en Compliance Audit pero debería estar aquí también.
- No tiene `apb-gov-evidence-v1.0`: generación de evidencias para el expediente de excepción.
- No tiene `apb-plat-ms-notify-v1.0`: debería notificar al CISO/CTO igual que hace el Compliance Audit.

**Añadir:**

| Skill | Tipo | Justificación |
|---|---|---|
| `apb-gov-jira-evidence-v1.0` | Existente (conectar) | Crear tickets de excepción en Jira |
| `apb-gov-evidence-v1.0` | Existente (conectar) | Evidencias para el expediente de excepción |
| `apb-plat-ms-notify-v1.0` | Existente (conectar) | Notificación a validadores de excepción |

---

### 2.20 `apb-agent-security-architect-v1.0` — Security Architect

**Skills actuales:** apb-sec-threat-model-v1.0, apb-sec-ens-v1.0, apb-sec-owasp-v1.0, apb-sec-forensic-v1.0, apb-sec-risk-analysis-v1.0, apb-sec-risk-policies-v1.0, apb-plat-deliver-artifact-v1.0  
**Subagentes:** apb-sub-sec-ens-v1.0  
**Autonomía:** 1

**Gaps:**

- No tiene skill de **SAST**: `apb-sub-qa-security-v1.0` hace testing de seguridad en QA pero la interpretación de hallazgos SAST desde una perspectiva arquitectónica es diferente.
- No tiene skill de **supply chain security**: SBOM, análisis de dependencias transitivas desde perspectiva de integridad (diferente de auditoría de obsolescencia que es del Tech Debt Agent).
- `apb-sec-mitre-mapping-v1.0` existe en el catálogo pero **no está conectada al Security Architect**.
- `apb-sec-cloud-hardening-v1.0` existe pero **no está conectada** — el Security Architect debería poder generar hardening guides para Azure.

**Añadir:**

| Skill | Tipo | Justificación |
|---|---|---|
| `apb-sec-mitre-mapping-v1.0` | Existente (conectar) | Mapeo de amenazas a MITRE ATT&CK, existe pero no conectada |
| `apb-sec-cloud-hardening-v1.0` | Existente (conectar) | CIS Benchmark hardening, existe pero no conectada |
| `apb-sec-sast-v1.0` | Nueva | Interpretación de resultados SAST con contexto APB |
| `apb-sec-supply-chain-v1.0` | Nueva | SBOM, licencias open source, integridad de dependencias |
| `apb-sec-patch-management-v1.0` | Nueva | Priorización patches: CVE severity × impacto APB × ventana de cambio |

---

### 2.21 `apb-agent-spec-engineer-v1.0` — Spec Engineer

**Skills actuales:** apb-disc-spec-gen-v1.0, apb-disc-backlog-v1.0, apb-disc-enrich-req-v1.0, apb-disc-cosmic-v1.0, apb-disc-adversarial-v1.0, apb-disc-epic-mono-v1.0, apb-gov-spec-sync-v1.0, apb-plat-deliver-artifact-v1.0  
**Subagentes:** ninguno  
**Autonomía:** 1

**Evaluación:** Bien equipado para ingeniería de especificaciones. Los gaps son menores.

**Gaps:**

- No tiene `apb-disc-brainstorming-v1.0` como primera fase exploratoria.
- No tiene `apb-disc-design-approval-v1.0` como gate de aprobación del diseño antes de generar el spec completo.
- No tiene skill de **user story quality**: verificar que las historias de usuario cumplen criterios INVEST (Independent, Negotiable, Valuable, Estimable, Small, Testable).

**Añadir:**

| Skill | Tipo | Justificación |
|---|---|---|
| `apb-disc-brainstorming-v1.0` | Existente (conectar) | Fase exploratoria previa |
| `apb-disc-design-approval-v1.0` | Existente (conectar) | Gate de aprobación de diseño, existe pero no conectada |

---

### 2.22 `apb-agent-sre-v1.0` — SRE

**Skills actuales:** apb-ops-operability-v1.0, apb-ops-slo-design-v1.0, apb-ops-observability-v1.0, apb-ops-prr-v1.0, apb-ops-rca-v1.0, apb-ops-runbook-v1.0, apb-plat-deliver-artifact-v1.0  
**Subagentes:** apb-sub-ops-azure-v1.0  
**Autonomía:** 1

**Gaps:**

- No tiene skill de **capacity planning**: forecasting de recursos basado en histórico y proyecciones de negocio. APB tiene tráfico estacional (puerto).
- No tiene skill de **post-incident review**: el RCA genera el análisis, pero el PIR/post-mortem estructurado (timeline, impacto, blameless, action items) es distinto y no existe.
- No tiene skill de **change management**: el SRE debería validar que los cambios en producción tienen RFC aprobado antes de ejecutarse.
- Solo tiene 1 subagente (Azure Monitor). Cuando APB migre a AKS no tendrá visibilidad Kubernetes.

**Añadir:**

| Componente | Tipo | Justificación |
|---|---|---|
| `apb-ops-capacity-planning-v1.0` | Nueva | Forecasting de recursos, seasonality portuaria |
| `apb-ops-post-incident-review-v1.0` | Nueva | PIR blameless: timeline, 5 whys, action items con owner |
| `apb-ops-service-continuity-v1.0` | Nueva | BCP/DRP: RTOs, RPOs, estrategia de backup por servicio |
| `apb-sub-ops-k8s-v1.0` | Subagente nuevo | Diagnóstico AKS: pods, HPA, eventos, logs kubectl |

---

### 2.23 `apb-agent-tech-debt-v1.0` — Tech Debt

**Skills actuales:** apb-ops-dependency-audit-v1.0, apb-ops-perf-bottleneck-v1.0, apb-ops-debt-remediation-plan-v1.0, apb-dev-sonar-clean-v1.0, apb-gov-policy-check-v1.0  
**Subagentes:** ninguno  
**Autonomía:** 2

**Evaluación:** Bien diseñado. Principios claros, flujo definido, respeta el "no crear tickets sin aprobación humana".

**Gaps menores:**

- No tiene `apb-sec-patch-management-v1.0` (nueva): la priorización de patches de seguridad es una forma específica de gestión de deuda con urgencia adicional (CVE activo).
- No tiene subagente por stack: .NET, Django, JavaScript tienen deuda técnica con características propias, pero el agente argumenta explícitamente que "las skills de diagnóstico ya cubren .NET, Django y JavaScript". Esta decisión es correcta pero limita la profundidad del análisis de deuda por stack.

---

### 2.24 `apb-agent-tech-discovery-v1.0` — Technology Discovery

**Skills actuales:** apb-disc-business-v1.0, apb-gov-catalog-v1.0, apb-plat-deliver-artifact-v1.0  
**Subagentes:** ninguno  
**Autonomía:** 1

**Evaluación:** El segundo agente más delgado (3 skills). Es el agente que evalúa nuevas tecnologías para APB pero tiene menos herramientas que un Business Analyst. Esto es un gap real.

**Gaps críticos:**

- No tiene skill de **evaluación técnica de alternativas**: framework de comparación (criterios técnicos, madurez, comunidad, licencias, integración con stack APB, coste).
- No tiene skill de **proof-of-concept guide**: cómo hacer un PoC estructurado con criterios de éxito y decisión go/no-go.
- No tiene skill de **technology radar**: registro de tecnologías en evaluación, adoptadas, en hold, deprecated (formato ThoughtWorks Tech Radar adaptado a APB).
- No usa `apb-disc-brainstorming-v1.0` para exploración inicial.
- No usa `apb-gov-standards-v1.0` para verificar que la tecnología evaluada cumple los estándares de arquitectura APB.

**Añadir:**

| Skill | Tipo | Justificación |
|---|---|---|
| `apb-disc-brainstorming-v1.0` | Existente (conectar) | Fase exploratoria |
| `apb-gov-standards-v1.0` | Existente (conectar) | Verificar que la tecnología encaja con los estándares APB |
| `apb-disc-tech-eval-v1.0` | Nueva | Framework de evaluación técnica de alternativas tecnológicas |
| `apb-disc-poc-guide-v1.0` | Nueva | Guía para PoC estructurado: criterios éxito, go/no-go, alcance |
| `apb-gov-tech-radar-v1.0` | Nueva | Technology radar APB: ADOPT / TRIAL / ASSESS / HOLD |

---

### 2.25 `apb-agent-technical-architect-v1.0` — Technical Architect

**Skills actuales:** apb-arch-design-v1.0, apb-arch-event-driven-v1.0, apb-arch-decompose-v1.0, apb-arch-api-contract-v1.0, apb-arch-tech-plan-v1.0, apb-arch-validate-v1.0, apb-arch-security-design-v1.0, apb-arch-cloud-infra-v1.0, apb-plat-deliver-artifact-v1.0  
**Subagentes:** ninguno  
**Autonomía:** 1

**Gaps:**

- Tiene `apb-arch-event-driven-v1.0` (shallow, 35 items) pero no `apb-arch-event-driven-master-v1.0` (deep, 31 items, skill maestro para events). La skill básica y la avanzada deberían estar las dos.
- `apb-arch-dotnet-base-v1.0` (reglas para proyectos .NET, cuándo usar APB.ARQ.BASE vs APB.ARQ.APIBASE) existe pero **no está conectada al Technical Architect**.
- No tiene skill de **C4 model**: los diagramas de arquitectura en niveles C4 (Context, Container, Component, Code) son el estándar para documentar arquitecturas y no hay skill específica.
- No tiene subagentes: para arquitecturas complejas, delegar en subagentes especializados por capa (API, datos, eventos, identidad) sería valioso.

**Añadir:**

| Skill | Tipo | Justificación |
|---|---|---|
| `apb-arch-event-driven-master-v1.0` | Existente (conectar) | La skill maestro de eventos, más profunda que la básica |
| `apb-arch-dotnet-base-v1.0` | Existente (conectar) | Reglas obligatorias para proyectos .NET, no conectada |
| `apb-arch-design-events-v1.0` | Existente (conectar) | Diseño de microservicios orientados a eventos, no conectada |
| `apb-arch-c4-model-v1.0` | Nueva | Generación de diagramas de arquitectura en C4 (Context, Container, Component) |
| `apb-arch-context-mapping-v1.0` | Nueva | Context maps DDD: relaciones entre bounded contexts |

---

### 2.26 `apb-agent-ux-mockup-v1.0` — UX Mockup

**Skills actuales:** apb-dev-devexpress-selector-v1.0, apb-dev-devexpress-front-v1.0, apb-dev-grill-before-code-v1.0, apb-gov-ai-risk-gate-v1.0, apb-plat-deliver-artifact-v1.0  
**Subagentes:** ninguno  
**Autonomía:** 1

**Evaluación:** Bien orientado a crear mockups y prototipos HTML interactivos con DevExtreme. El gap fundamental es la accesibilidad.

**Gaps:**

- No tiene skill de **accesibilidad WCAG**: APB como ente público tiene obligación legal (RD 1112/2018) de que sus portales sean WCAG 2.1 AA. El mockup es el momento ideal para verificarlo.
- `third-sickn33-screen-reader-testing-v1.0` existe en el catálogo en estado draft. Desbloquearlo y conectarlo aquí añadiría valor inmediato.
- No tiene skill de **user research synthesis**: el UX Mockup recibe una "descripción de necesidad" pero no tiene herramientas para sintetizar investigación de usuarios (entrevistas, analítica).

**Añadir:**

| Skill | Tipo | Justificación |
|---|---|---|
| `apb-qa-accessibility-v1.0` | Nueva | WCAG 2.1 AA audit de mockups y HTML generado |
| `third-sickn33-screen-reader-testing-v1.0` | Existente draft (activar) | Screen reader testing, existe pero en draft |
| `third-nextlevel-ux-v1.0` | Existente aprobada (conectar) | Skill de UX, existe pero no conectada a este agente |

---

## 3. Análisis por subagente

### 3.1 Grupo DDD (5 subagentes)

`apb-sub-ddd-code-v1.0`, `apb-sub-ddd-db-v1.0`, `apb-sub-ddd-doc-v1.0`, `apb-sub-ddd-interview-v1.0`, `apb-sub-ddd-spec-v1.0`

**Evaluación:** Los mejor diseñados del catálogo. Todos tienen prompts de sistema específicos para su tipo de análisis. La cobertura de fuentes es completa: código fuente, esquemas de BD, documentación, conversación estructurada, specs API.

**Gap único:**
- No hay subagente de **análisis de integraciones**: cuando el legacy tiene integraciones con sistemas externos (EDI, APIs de terceros, ficheros) que no están en el código fuente ni en la BD.

---

### 3.2 Grupo Dev (5 subagentes)

`apb-sub-dev-devexpress-v1.0`, `apb-sub-dev-django-v1.0`, `apb-sub-dev-net-v1.0`, `apb-sub-dev-parallel-v1.0`, `apb-sub-dev-sql-v1.0`

**Evaluación:** Bien cubiertos para el stack principal. El subagente paralelo (`apb-sub-dev-parallel-v1.0`) es un patrón inteligente pero no está conectado al Implementer Agent.

**Gaps:**

- No hay subagente de **JavaScript/TypeScript standalone**: el DevExpress subagente cubre el frontend, pero no el TypeScript/Node.js puro para utilidades, CLIs o lambdas.
- No hay subagente de **PostGIS/GeoDjango** separado del Django genérico: las queries geoespaciales tienen características muy específicas que justifican especialización.

---

### 3.3 Grupo Ops (4 subagentes)

`apb-sub-ops-azure-v1.0`, `apb-sub-ops-iis-apache-v1.0`, `apb-sub-ops-network-v1.0`, `apb-sub-ops-oracle-v1.0`

**Evaluación:** Los tres de diagnóstico (iis-apache, network, oracle) tienen `autonomy_level: 2` y **no tienen prompt de sistema** según el análisis (no hay ## 🧠 en el body). Son los subagentes de menor calidad del catálogo.

**Gaps críticos:**

- Los 3 subagentes de diagnóstico necesitan **prompts de sistema** que codifiquen el conocimiento específico de diagnóstico (comandos exactos, patrones de error conocidos para el stack APB).
- No hay subagente para **Azure Service Bus** (dead-letter, backlog, consumers muertos) — parte del stack APB.
- No hay subagente para **Cosmos DB** — parte del stack APB.
- No hay subagente para **AKS/Kubernetes** — necesario para la roadmap cloud.
- No hay subagente para **Azure Entra ID** (usuarios bloqueados, MFA, conditional access).

---

### 3.4 Grupo Obs (2 subagentes)

`apb-sub-obs-grafana-v1.0`, `apb-sub-obs-powerbi-v1.0`

**Evaluación:** Bien diseñados, orientados a primer setup de dashboards. El de Grafana también cubre alerting Prometheus.

**Gap:**
- No hay subagente para **Azure Application Insights** específicamente (diferente de Azure Monitor genérico): Application Insights tiene capacidades específicas (dependency tracking, exception tracking, custom events) que merecen especialización.

---

### 3.5 Grupo QA (3 subagentes)

`apb-sub-qa-e2e-v1.0`, `apb-sub-qa-security-v1.0`, `apb-sub-qa-unit-v1.0`

**Evaluación:** Buena cobertura de los 3 tipos principales de testing. El de seguridad (`apb-sub-qa-security-v1.0`) hace análisis estático con SonarQube, pruebas dinámicas con OWASP ZAP.

**Gaps:**

- No hay subagente de **performance testing**: `prov-k6-v1.0` existe pero no hay subagente que lo explote para diseño y análisis de tests de carga.
- No hay subagente de **accesibilidad**: para auditorías WCAG más profundas que las que puede hacer una skill genérica.

---

### 3.6 Grupo Platform (2 subagentes)

`apb-sub-plat-ghactions-v1.0`, `apb-sub-plat-jenkins-v1.0`

**Evaluación:** Bien cubiertos para los dos CI/CD soportados.

**Gap:**
- No hay subagente de **Terraform avanzado**: el Platform Engineer tiene la skill de Terraform, pero un subagente especializado en state management, módulos APB, y troubleshooting de plans añadiría valor.

---

### 3.7 Grupo Gov y Sec (2 subagentes)

`apb-sub-gov-standards-v1.0`, `apb-sub-sec-ens-v1.0`

**Evaluación:** Correctos para su función. El de ENS hace validación específica del Esquema Nacional de Seguridad.

**Gaps:**

- No hay subagente de **RGPD/Protección de datos**: la normativa RGPD tiene especificidades (base legal, derechos de interesados, DPIA) que justifican un subagente propio.
- No hay subagente de **clasificación de datos**: diferente al compliance general, un subagente especializado en clasificar activos de datos (personal/sensible/operativo/público) sería útil para el agente de gobierno de datos propuesto.

---

## 4. Análisis de skills por dominio

### 4.1 Architecture (13 skills) — Calidad: media-alta

**Gaps detectados:**

| ID propuesto | Descripción | Agente destino |
|---|---|---|
| `apb-arch-c4-model-v1.0` | Generación de diagramas C4 (Context, Container, Component): estándar de documentación de arquitectura | Technical Architect |
| `apb-arch-context-mapping-v1.0` | Context maps DDD: relaciones entre bounded contexts (ACL, OHS, CF, Published Language) | Domain Architect, Technical Architect |

**Skills existentes sin conectar:**
- `apb-arch-event-driven-master-v1.0` no está en Technical Architect
- `apb-arch-dotnet-base-v1.0` no está en Technical Architect
- `apb-arch-design-events-v1.0` no está en Technical Architect

---

### 4.2 Design (2 skills) — Calidad: baja (solo 2)

**Nota:** El dominio design tiene el menor número de skills. La `apb-design-frontend-design-system-v1.0` es shallow (5 bullet items). La `apb-dev-devexpress-selector-v1.0` está bien.

**Gaps:**

| ID propuesto | Descripción | Agente destino |
|---|---|---|
| `apb-design-wcag-patterns-v1.0` | Patrones de componentes DevExtreme accesibles: configuraciones ARIA, navegación por teclado, contraste | UX Mockup |

---

### 4.3 Development (27 skills) — Calidad: alta

**Análisis de profundidad:** Las skills con prompts detallados (DEEP) son las de más uso diario: code-review-v1.0, api-standard-v1.0, code-base-v1.0, sql-gen-v1.0, sql-review-v1.0, implementation-patterns-v1.0. Las SHALLOW son las de control (simplicity-first, surgical-changes, verify-before-done) que tienen lógica corta por diseño.

**Skills existentes no conectadas a agentes (gap de wiring):**
- `apb-dev-implementation-patterns-v1.0` no está en el Implementer
- `apb-dev-frontend-devexpress-events-v1.0` no está en el Implementer
- `apb-dev-sql-gen-v1.0` no está en el Implementer (sí está apb-dev-sql-fix-v1.0)

**Gaps de skills nuevas:**

| ID propuesto | Descripción | Agente destino |
|---|---|---|
| `apb-dev-accessibility-impl-v1.0` | Implementación de accesibilidad WCAG en DevExtreme: atributos ARIA, roles, focus management | Implementer, UX Mockup |

---

### 4.4 Discovery (12 skills) — Calidad: media (todas SHALLOW por diseño)

**Análisis:** Las skills de discovery son intencionalmente SHALLOW: son interrogatorios y estructuras, no prompts profundos. Esto es correcto.

**Skills existentes no conectadas:**
- `apb-disc-brainstorming-v1.0` no está en Business Analyst, Spec Engineer, Tech Discovery, Domain Architect
- `apb-disc-design-approval-v1.0` no está en Spec Engineer

**Gaps de skills nuevas:**

| ID propuesto | Descripción | Agente destino |
|---|---|---|
| `apb-disc-user-journey-v1.0` | User journey maps para portales y servicios APB: actores, pasos, touchpoints, pain points | Business Analyst |
| `apb-disc-value-stream-v1.0` | Value stream mapping para procesos portuarios: flujo de valor, desperdicios, oportunidades | Business Analyst |
| `apb-disc-tech-eval-v1.0` | Framework de evaluación técnica de alternativas: criterios, scoring, comparativa | Tech Discovery |
| `apb-disc-poc-guide-v1.0` | Guía para Proof of Concept estructurado: alcance, criterios de éxito, go/no-go, timeboxing | Tech Discovery |

---

### 4.5 Documentation (7 skills) — Calidad: alta

**Evaluación:** Todas las skills de documentación son DEEP. La `apb-doc-generate-ppt-v1.0` y `apb-doc-generate-word-v1.0` son interesantes (48 y 40 bullets respectivamente) pero no están conectadas al Documentation Agent.

**Skills existentes no conectadas:**
- `apb-doc-event-specs-v1.0` no está en Documentation Agent
- `apb-doc-generate-ppt-v1.0` no está conectada a ningún agente
- `apb-doc-generate-word-v1.0` no está conectada a ningún agente

**Gaps de skills nuevas:**

| ID propuesto | Descripción | Agente destino |
|---|---|---|
| `apb-doc-changelog-v1.0` | Generación de changelog semántico (SemVer) desde commits, PRs y tags de Git | Documentation, Release Manager |
| `apb-doc-release-notes-v1.0` | Release notes para usuarios finales: qué hay nuevo, qué se ha corregido, cómo afecta | Release Manager, Documentation |
| `apb-doc-onboarding-v1.0` | Guía de onboarding de desarrollador en un proyecto: setup, arquitectura, convenciones, contactos | Documentation, Knowledge Manager |
| `apb-doc-post-mortem-v1.0` | Documento post-mortem blameless: timeline, impacto, causa raíz, 5 whys, action items | SRE, Incident L2 |

---

### 4.6 Governance (12 skills) — Calidad: muy alta (100% DEEP)

**Evaluación:** El dominio de mayor calidad. `apb-gov-org-risk-report-v1.0` con 117 bullet items es la skill más elaborada del framework.

**Skills existentes no conectadas:**
- `apb-gov-spec-sync-v1.0` no está en Governance Agent
- `apb-dev-verify-before-done-v1.0` (está clasificada en governance pero no conectada al Governance Agent)

**Gaps de skills nuevas:**

| ID propuesto | Descripción | Agente destino |
|---|---|---|
| `apb-gov-data-classification-v1.0` | Clasificación de datos: personal/sensible/operativo/público según RGPD y ENS | Data Governance, Governance |
| `apb-gov-lcsp-check-v1.0` | Verificación LCSP: procedimiento correcto según cuantía, criterios de adjudicación, documentación | Compliance Audit, Vendor Manager |
| `apb-gov-vendor-eval-v1.0` | Evaluación técnica de proveedores: capacidad, solvencia, seguridad, SLA, continuidad | Vendor Manager |
| `apb-gov-ai-model-lifecycle-v1.0` | Gobierno de modelos IA: versión en uso, cambios, impacto en agentes, retiro | Governance |
| `apb-gov-dpia-v1.0` | EIPD/DPIA según RGPD art. 35: necesidad, alcance, riesgos, medidas | Data Governance, Compliance Audit |
| `apb-gov-tech-radar-v1.0` | Technology radar APB: ADOPT / TRIAL / ASSESS / HOLD con justificación | Tech Discovery, Governance |
| `apb-gov-framework-metrics-v1.0` | Métricas del framework: % en draft, tiempo aprobación, cobertura de dominios, uso de componentes | Catalog Manager |
| `apb-gov-framework-audit-v1.0` | Auditoría del framework: componentes obsoletos, inconsistencias, sin uso en >6 meses | Catalog Manager |

---

### 4.7 Operation (13 skills) — Calidad: mixta

**Análisis de profundidad:** Las skills de incidencias (triage, diagnose, escalate) son SHALLOW (24-56 bullets) — son interrogatorios estructurados. Las de SRE (observability, prr, rca, runbook, slo-design) son DEEP. Las de deuda (debt-remediation, dependency-audit, perf-bottleneck) son SHALLOW.

**Gaps críticos — dominio con más carencias:**

| ID propuesto | Descripción | Agente destino |
|---|---|---|
| `apb-ops-change-management-v1.0` | RFC: descripción, impacto, ventana, rollback, verificación post-cambio. Gate antes de producción | Change Manager, Release Manager, SRE |
| `apb-ops-problem-management-v1.0` | Detección de patrones en incidencias, apertura de problema ITIL, known error database, workaround | Problem Manager, Incident Support |
| `apb-ops-post-incident-review-v1.0` | PIR blameless: timeline, impacto real, 5 whys, action items con owner y fecha límite | SRE, Incident L2 |
| `apb-ops-capacity-planning-v1.0` | Forecasting de demanda: trend analysis, seasonal modeling (tráfico portuario), right-sizing | SRE, Capacity Planner |
| `apb-ops-service-continuity-v1.0` | BCP/DRP: RTOs y RPOs por servicio, estrategia de backup, plan de recuperación | SRE, Platform Engineer |
| `apb-ops-alerting-design-v1.0` | Diseño de alertas: umbrales, severidades, páginas de guardia, silencias, runbooks asociados | SRE, Observability |

---

### 4.8 Platform (12 skills) — Calidad: muy alta (100% DEEP)

**Evaluación:** Segundo dominio de mayor calidad. `apb-plat-terraform-v1.0` con 50 bullets es la skill de plataforma más rica.

**Gaps:**

| ID propuesto | Descripción | Agente destino |
|---|---|---|
| `apb-plat-k8s-v1.0` | Manifiestos Kubernetes, Helm charts, Network Policies, PodDisruptionBudgets, HPA para AKS | Platform Engineer, Cloud Architect |
| `apb-plat-azure-servicebus-v1.0` | Config Service Bus: topics, subscriptions, retry policies, DLQ, alertas, particionado | Platform Engineer, Cloud Architect |
| `apb-plat-secret-rotation-v1.0` | Especificación automatización rotación Key Vault: cadencia 90d, actualización de referencias | Platform Engineer |
| `apb-plat-environment-promotion-v1.0` | Promoción dev→staging→prod: smoke tests, gates, aprobación, rollback triggers | Platform Engineer, Release Manager |

---

### 4.9 PM (8 skills) — Calidad: alta (100% DEEP)

**Evaluación:** Bien enfocadas en arquitecturas orientadas a eventos. `apb-pm-retrospective-v1.0` con 39 bullets es particularmente rica.

**Gaps:**

| ID propuesto | Descripción | Agente destino |
|---|---|---|
| `apb-pm-risk-register-v1.0` | Registro de riesgos de proyecto: probabilidad × impacto, owner, mitigaciones, seguimiento | Business Analyst, PM |
| `apb-pm-status-report-v1.0` | Informe de estado semanal: avance, riesgos activos, hitos, impedimentos, RAG status | PM |
| `apb-pm-stakeholder-map-v1.0` | Mapa de stakeholders: interés, influencia, comunicación, frecuencia de reporte | Business Analyst |

---

### 4.10 QA (14 skills) — Calidad: alta (mayoría DEEP)

**Evaluación:** Buena cobertura para testing funcional. Los gaps están en performance, accesibilidad y testing de seguridad a nivel de código.

**Skills existentes no conectadas:**
- `apb-qa-tdd-v1.0` no está en QA Auto Agent
- `apb-qa-readiness-check-v1.0` no está en QA Auto Agent
- `apb-qa-testing-strategy-v1.0` no está en QA Auto Agent
- `apb-qa-pipeline-v1.0` no está en QA Auto Agent
- `apb-qa-framework-v1.0` no está en Meta Builder

**Gaps:**

| ID propuesto | Descripción | Agente destino |
|---|---|---|
| `apb-qa-performance-v1.0` | Tests de carga k6: escenarios de tráfico portuario, thresholds, análisis de resultados | QA Automation |
| `apb-qa-contract-testing-v1.0` | Consumer-Driven Contract Testing (Pact): definición de contratos entre servicios | QA Automation |
| `apb-qa-accessibility-v1.0` | WCAG 2.1 AA: criterios de éxito, análisis de HTML/mockups, declaración de accesibilidad | QA Automation, Accessibility Auditor, UX Mockup |

---

### 4.11 Security (8 skills) — Calidad: alta (mayoría DEEP)

**Skills existentes no conectadas:**
- `apb-sec-mitre-mapping-v1.0` no está en Security Architect
- `apb-sec-cloud-hardening-v1.0` no está en Security Architect

**Gaps:**

| ID propuesto | Descripción | Agente destino |
|---|---|---|
| `apb-sec-sast-v1.0` | Interpretación de resultados SAST (SonarQube security rules, Semgrep, Bandit) con contexto APB | Security Architect, Code Reviewer |
| `apb-sec-supply-chain-v1.0` | SBOM, licencias open source, integridad de dependencias, typosquatting | Security Architect |
| `apb-sec-patch-management-v1.0` | Priorización patches: CVE severity × impacto APB × ventana de cambio disponible | Security Architect, Tech Debt |
| `apb-sec-dast-v1.0` | Interpretación resultados DAST (OWASP ZAP, Burp) en entornos de test | Security Architect |

---

### 4.12 Orchestration (1 skill) — Calidad: media

`apb-orch-multi-agent-v1.0`: Coordinación entre agentes, deep, 10 bullets. Es la única skill del dominio.

**Gap:** No hay skill de **gestión de estado de workflow**: cuando un workflow multi-agente falla a mitad, ¿cómo se reanuda? Esto conecta con el gap de orchestration engine del manual de arquitectura.

---

## 5. Análisis por workflow

### 5.1 `apb-wf-sdd-full-v1.0` — Spec Driven Development

**Evaluación:** El workflow más completo (10 agentes, 8 fases, 6 puntos de decisión). Referencia de calidad.

**Gap:** No incluye la fase de **change management** post-release: cuando el SDD genera un artefacto listo para producción, no hay fase de RFC/CAB antes del despliegue real. El Release Manager valida la calidad pero no el proceso de cambio.

---

### 5.2 `apb-wf-code-review-v1.0` — Code Review Asistido

**Evaluación:** Bien estructurado (3 agentes, 5 fases). Cubre implementador, governance y QA.

**Gap:** No incluye al Security Architect para PRs con cambios en autenticación, autorización o manejo de datos sensibles. El `apb-sub-qa-security-v1.0` hace testing de seguridad pero el Security Architect debería estar en el loop para cambios de alto impacto.

---

### 5.3 `apb-wf-cloud-migration-v1.0` — Cloud Migration

**Evaluación:** Muy bien diseñado (9 agentes, 8 fases). Incluye todos los especialistas: cloud, técnico, seguridad, plataforma, QA, SRE, FinOps, governance, release.

**Gaps:**
- No incluye al **Change Manager** para las ventanas de migración (cada fase de migración es un cambio de producción que debería tener RFC).
- No incluye al **Problem Manager** para documentar incidencias durante la migración.

---

### 5.4 `apb-wf-incident-l1-v1.0` — Gestión Incidencia L1

**Evaluación:** Correcto para L1. Un solo agente con 8 fases bien definidas. El escalado a L2 está instrumentado en el agente pero no hay un workflow L2 al que conectar.

**Gap crítico:** No hay `apb-wf-incident-l2-v1.0`. El escalado produce un resumen técnico que desaparece — no hay workflow que recoja el handoff.

---

### 5.5 `apb-wf-legacy-onboarding-v1.0` — Legacy Onboarding

**Evaluación:** Buena cobertura (5 agentes, 5 fases). Modernización → Domain Architect → Spec → QA → Documentation.

**Gaps:**
- No incluye **Security Architect** para el inventario de vulnerabilidades del legacy durante el onboarding.
- No incluye **Tech Debt Agent** para el inventario inicial de deuda técnica (que es el primer output útil de onboardar un legacy).

---

### 5.6 `apb-wf-qa-evidence-v1.0` — QA & Evidence

**Evaluación:** Bien diseñado (4 agentes, 7 fases). Cubre plan, ejecución, evidencias, release.

**Gap:** No incluye tests de performance ni accesibilidad — la evidencia de release debería incluir también estos aspectos para sistemas de cara al ciudadano.

---

### 5.7 `apb-wf-risk-exception-v1.0` — Risk & Exception

**Evaluación:** 4 agentes, 6 fases. Bien diseñado como complemento al Compliance Audit Agent.

**Gap:** No tiene fase de **seguimiento post-aprobación**: cuando se aprueba una excepción con condiciones, no hay fase que verifique que las condiciones se cumplieron antes del deadline.

---

### 5.8 `apb-wf-spec-from-legacy-v1.0` — Spec Generation from Legacy

**Evaluación:** 6 agentes, 6 fases. Bien orientado a generar spec desde código existente.

**Gap:** No incluye al **DDD Agent** con sus 5 subagentes, que es exactamente la herramienta para analizar un legacy y producir propuestas de dominio. El Domain Architect hace event storming pero el DDD Agent hace el análisis bottom-up.

---

## 6. Nuevos agentes propuestos

---

### 🔴 ALTA PRIORIDAD

#### `apb-agent-change-manager-v1.0` — Change Management Agent

**Dominio:** operation | **Autonomía:** 1 | **Owner:** SRE / Operaciones

**Por qué es crítico:** El framework genera releases pero no instrumenta el proceso ITIL de gestión de cambios que precede cualquier despliegue en producción APB. Sin este agente, existe el riesgo de que el equipo salte el CAB.

**Skills:**
- `apb-ops-change-management-v1.0` (nueva)
- `apb-ops-runbook-v1.0` (existente)
- `apb-gov-jira-evidence-v1.0` (existente)
- `apb-plat-ms-notify-v1.0` (existente)
- `apb-gov-evidence-v1.0` (existente)

**Subagentes:** ninguno

**Capacidades:**
- Generación de RFC con: descripción del cambio, impacto, ventana propuesta, rollback plan, responsables
- Evaluación de impacto: qué sistemas afecta, usuarios impactados, servicios en riesgo
- Preparación del expediente para CAB (Change Advisory Board)
- Verificación post-cambio (smoke tests, rollback trigger conditions)
- Calendario de cambios: qué hay en la ventana, conflictos, congelaciones

---

#### `apb-agent-problem-manager-v1.0` — Problem Management Agent

**Dominio:** operation | **Autonomía:** 1 | **Owner:** Operaciones / SRE

**Por qué es crítico:** Actualmente el conocimiento de incidencias recurrentes se fragmenta en tickets individuales. Ningún agente hace el análisis de patrones para identificar problemas sistémicos (ITIL Problem Management).

**Skills:**
- `apb-ops-problem-management-v1.0` (nueva)
- `apb-ops-rca-v1.0` (existente)
- `apb-gov-jira-evidence-v1.0` (existente)
- `apb-gov-knowledge-v1.0` (existente)
- `apb-plat-ms-notify-v1.0` (existente)

**Capacidades:**
- Análisis de patrones en histórico JSM para detectar problemas sistémicos
- Creación de tickets de Problema y gestión del estado (Investigación → Known Error → Cerrado)
- Known Error Database: workaround documentado y publicado para el equipo de soporte
- Propuesta de corrección definitiva (input para Tech Debt o Platform Engineer)
- Métricas de efectividad: ¿bajaron las incidencias recurrentes?

---

#### `apb-agent-data-governance-v1.0` — Data Governance Agent

**Dominio:** governance | **Autonomía:** 1 | **Owner:** DPO / Arquitectura

**Por qué es crítico:** APB procesa datos de operaciones portuarias, ciudadanos y proveedores. La combinación RGPD + ENS crea obligaciones legales de clasificación, inventario y EIPD que no tienen soporte en el framework.

**Skills:**
- `apb-gov-data-classification-v1.0` (nueva)
- `apb-gov-dpia-v1.0` (nueva)
- `apb-sec-risk-analysis-v1.0` (existente)
- `apb-gov-evidence-v1.0` (existente)
- `apb-gov-jira-evidence-v1.0` (existente)
- `apb-doc-manual-v1.0` (existente — para catálogo de datos)

**Subagentes:** `apb-sub-gov-data-v1.0` (nuevo)

**Capacidades:**
- Inventario de tratamientos RGPD art. 30 (registro por sistema)
- Clasificación de activos de datos: personal / sensible / operativo / público
- EIPD/DPIA cuando aplica (sistemas nuevos con datos personales)
- Catálogo de datos: qué datos tiene APB, dónde están, quién es el responsable de cada dataset
- Política de retención: plazos de conservación y procedimiento de destrucción

---

### 🟡 PRIORIDAD MEDIA

#### `apb-agent-incident-l2-v1.0` — Incident Support L2

**Dominio:** operation | **Autonomía:** 1 | **Owner:** Operaciones

**Por qué importa:** El L1 escala pero no hay nadie que recoja el handoff. El L2 hace diagnóstico más profundo: correlación con cambios recientes, análisis de traces de aplicación, coordinación con desarrollo.

**Skills:**
- `apb-ops-rca-v1.0` (existente)
- `apb-ops-perf-bottleneck-v1.0` (existente)
- `apb-dev-impact-analysis-v1.0` (existente — correlacionar incidente con cambios de código)
- `apb-ops-post-incident-review-v1.0` (nueva)
- `apb-gov-jira-evidence-v1.0` (existente)

**Subagentes:** apb-sub-ops-oracle-v1.0, apb-sub-ops-azure-v1.0, apb-sub-ops-k8s-v1.0 (nuevo), apb-sub-ops-servicebus-v1.0 (nuevo)

---

#### `apb-agent-accessibility-auditor-v1.0` — Accessibility Auditor

**Dominio:** qa | **Autonomía:** 1 | **Owner:** QA / Desarrollo

**Por qué importa:** Obligación legal (RD 1112/2018) para portales públicos de organismos del sector público. APB tiene portales de cara al ciudadano.

**Skills:**
- `apb-qa-accessibility-v1.0` (nueva)
- `third-sickn33-screen-reader-testing-v1.0` (existente draft — activar)
- `apb-doc-manual-v1.0` (existente — para declaración de accesibilidad obligatoria)

---

#### `apb-agent-vendor-manager-v1.0` — Vendor Management Agent

**Dominio:** governance | **Autonomía:** 1 | **Owner:** Dirección TI / Contratación

**Por qué importa:** APB como ente público contrata tecnología bajo LCSP. Ningún componente del framework cubre la evaluación técnica de proveedores ni la verificación de cumplimiento LCSP.

**Skills:**
- `apb-gov-lcsp-check-v1.0` (nueva)
- `apb-gov-vendor-eval-v1.0` (nueva)
- `apb-sec-risk-analysis-v1.0` (existente — riesgo de concentración en proveedores)
- `apb-gov-evidence-v1.0` (existente)

---

#### `apb-agent-knowledge-manager-v1.0` — Knowledge Management Agent

**Dominio:** documentation | **Autonomía:** 2 | **Owner:** Operaciones / TI

**Por qué importa:** El conocimiento operativo APB vive en personas y correos, no en un sistema estructurado. El Knowledge Manager genera artículos de KB desde incidencias resueltas y organiza Confluence.

**Skills:**
- `apb-gov-knowledge-v1.0` (existente)
- `apb-doc-manual-v1.0` (existente)
- `apb-doc-onboarding-v1.0` (nueva)
- `apb-plat-sharepoint-io-v1.0` (existente)

**Subagentes:** `apb-sub-doc-confluence-v1.0` (nuevo)

---

#### `apb-agent-api-product-manager-v1.0` — API Product Manager

**Dominio:** architecture | **Autonomía:** 1 | **Owner:** Arquitectura

**Por qué importa:** Cuando el domain catalog tenga APIs registradas, alguien debe gestionar su ciclo de vida: versiones, deprecaciones, breaking changes, consumers. El framework sabe diseñar APIs pero no gestionar el portfolio.

**Skills:**
- `apb-arch-api-contract-v1.0` (existente)
- `apb-dev-api-standard-v1.0` (existente)
- `apb-doc-swagger-v1.0` (existente)
- `apb-dev-openspec-review-v1.0` (existente)
- `apb-gov-spec-sync-v1.0` (existente)
- `apb-arch-api-lifecycle-v1.0` (nueva)

---

### 🟢 PRIORIDAD BAJA (estratégica)

#### `apb-agent-capacity-planner-v1.0` — Capacity Planning Agent

**Dominio:** operation | **Autonomía:** 1

**Propósito:** Forecasting de demanda de infraestructura basado en histórico y proyecciones del negocio portuario. APB tiene estacionalidad significativa (tráfico de cruceros en verano, campañas logísticas). Implementar cuando haya ≥12 meses de datos históricos Azure.

---

#### `apb-agent-portfolio-it-v1.0` — IT Portfolio Agent

**Dominio:** governance | **Autonomía:** 1

**Propósito:** Vista consolidada del portfolio de proyectos IT: alineamiento estratégico, duplicidades, deuda técnica agregada, inversión vs. valor. Input para dirección TI. Implementar cuando otros agentes lleven meses en uso produciendo datos.

---

## 7. Nuevos subagentes propuestos

| ID | Agente(s) padre | Descripción | Prioridad |
|---|---|---|---|
| `apb-sub-ops-k8s-v1.0` | SRE, Platform Engineer, Incident L2 | Diagnóstico AKS: pods crashlooping, OOMKilled, pending, HPA, PDB, eventos de cluster, logs kubectl | Alta |
| `apb-sub-ops-servicebus-v1.0` | Incident Support, Platform Engineer | Azure Service Bus: dead-letter queues, backlog, consumers muertos, poison messages, namespaces | Alta |
| `apb-sub-finops-azure-v1.0` | FinOps | Azure Cost Management API: exportaciones, budgets, alertas, reservas, Hybrid Benefit, savings plans | Alta |
| `apb-sub-doc-confluence-v1.0` | Documentation, Knowledge Manager | Creación y actualización de páginas Confluence: espacios, plantillas, metadatos, jerarquía | Media |
| `apb-sub-sec-sast-v1.0` | Security Architect, Code Reviewer | SonarQube security rules, Semgrep, Bandit: interpretación con contexto .NET, Django, JS de APB | Media |
| `apb-sub-qa-performance-v1.0` | QA Automation | Diseño y análisis de tests de carga k6: escenarios, virtual users, thresholds, resultados | Media |
| `apb-sub-gov-data-v1.0` | Data Governance | Clasificación de activos de datos por sensibilidad (RGPD + ENS): análisis de sistemas y datasets | Media |
| `apb-sub-ops-entra-v1.0` | Security Architect, Incident Support | Microsoft Entra ID: usuarios bloqueados, MFA, conditional access, SSPR, auditlog | Baja |

---

## 8. Nuevas skills propuestas

### Por dominio — resumen completo

#### Operation (+6 nuevas)

| ID | Descripción |
|---|---|
| `apb-ops-change-management-v1.0` | RFC, evaluación de impacto, plan de rollback, gate de CAB, verificación post-cambio |
| `apb-ops-problem-management-v1.0` | Análisis de patrones en incidencias, problema ITIL, known error, workaround |
| `apb-ops-post-incident-review-v1.0` | PIR blameless: timeline, impacto real, 5 whys, action items con owner y fecha |
| `apb-ops-capacity-planning-v1.0` | Forecasting de recursos: trend, seasonality portuaria, right-sizing |
| `apb-ops-service-continuity-v1.0` | BCP/DRP: RTOs, RPOs, estrategia de backup, plan de recuperación |
| `apb-ops-alerting-design-v1.0` | Diseño de alertas: umbrales, severidades, páginas de guardia, runbooks asociados |

#### Security (+4 nuevas)

| ID | Descripción |
|---|---|
| `apb-sec-sast-v1.0` | Interpretación SAST (SonarQube security, Semgrep, Bandit) con contexto APB |
| `apb-sec-supply-chain-v1.0` | SBOM, licencias open source, integridad de dependencias transitivas |
| `apb-sec-patch-management-v1.0` | Priorización patches: CVE severity × impacto APB × ventana de cambio |
| `apb-sec-dast-v1.0` | Interpretación DAST (OWASP ZAP, Burp Suite) en entornos de test |

#### Governance (+8 nuevas)

| ID | Descripción |
|---|---|
| `apb-gov-data-classification-v1.0` | Clasificación datos: personal/sensible/operativo/público según RGPD y ENS |
| `apb-gov-lcsp-check-v1.0` | LCSP: procedimiento correcto, criterios de adjudicación, documentación requerida |
| `apb-gov-vendor-eval-v1.0` | Evaluación técnica de proveedores: capacidad, solvencia, seguridad, continuidad |
| `apb-gov-ai-model-lifecycle-v1.0` | Gobierno de modelos IA en APB: versión, cambios, impacto en agentes |
| `apb-gov-dpia-v1.0` | EIPD/DPIA RGPD art. 35: necesidad, alcance, riesgos, medidas |
| `apb-gov-tech-radar-v1.0` | Technology radar APB: ADOPT / TRIAL / ASSESS / HOLD |
| `apb-gov-framework-metrics-v1.0` | Métricas del framework: % draft, tiempo aprobación, uso de componentes |
| `apb-gov-framework-audit-v1.0` | Auditoría framework: obsoletos, sin uso, inconsistencias entre versiones |

#### Platform (+4 nuevas)

| ID | Descripción |
|---|---|
| `apb-plat-k8s-v1.0` | Manifiestos K8s, Helm charts, Network Policies, PodDisruptionBudgets para AKS |
| `apb-plat-azure-servicebus-v1.0` | Config Service Bus: topics, subscriptions, retry, DLQ, particionado, alertas |
| `apb-plat-secret-rotation-v1.0` | Automatización rotación Key Vault: cadencia 90d, actualización de referencias en apps |
| `apb-plat-environment-promotion-v1.0` | Promoción dev→staging→prod: smoke tests, gates de aprobación, rollback triggers |

#### FinOps (+3 nuevas, bajo dominio platform)

| ID | Descripción |
|---|---|
| `apb-plat-finops-alerting-v1.0` | Alertas de budget, anomalías de coste, proyecciones en Azure Cost Management |
| `apb-plat-finops-chargeback-v1.0` | Allocación de costes por proyecto/equipo, estrategia de tagging, reportes |
| `apb-plat-finops-reservations-v1.0` | Análisis de reservas Azure, Hybrid Benefit, Savings Plans |

#### QA (+3 nuevas)

| ID | Descripción |
|---|---|
| `apb-qa-performance-v1.0` | Tests de carga k6: escenarios de tráfico portuario, thresholds, análisis |
| `apb-qa-contract-testing-v1.0` | Consumer-driven contract testing (Pact) entre servicios |
| `apb-qa-accessibility-v1.0` | WCAG 2.1 AA: criterios, análisis HTML/mockups, declaración de accesibilidad |

#### Documentation (+4 nuevas)

| ID | Descripción |
|---|---|
| `apb-doc-changelog-v1.0` | Changelog semántico desde commits, PRs y tags Git |
| `apb-doc-release-notes-v1.0` | Release notes orientadas a usuario final |
| `apb-doc-onboarding-v1.0` | Guía de onboarding de desarrollador: setup, arquitectura, convenciones, contactos |
| `apb-doc-post-mortem-v1.0` | Post-mortem blameless: timeline, impacto, causa raíz, 5 whys, action items |

#### Architecture (+3 nuevas)

| ID | Descripción |
|---|---|
| `apb-arch-c4-model-v1.0` | Diagramas C4: Context, Container, Component — estándar de documentación de arquitectura |
| `apb-arch-context-mapping-v1.0` | Context maps DDD: relaciones entre bounded contexts (ACL, OHS, CF, Published Language) |
| `apb-arch-api-lifecycle-v1.0` | Ciclo de vida de APIs: versionado, deprecation timeline, impact analysis sobre consumers |

#### Discovery (+4 nuevas)

| ID | Descripción |
|---|---|
| `apb-disc-user-journey-v1.0` | User journey maps para portales APB: actores, pasos, touchpoints, pain points |
| `apb-disc-value-stream-v1.0` | Value stream mapping para procesos portuarios: flujo de valor, desperdicios |
| `apb-disc-tech-eval-v1.0` | Framework evaluación técnica de alternativas: criterios, scoring, comparativa |
| `apb-disc-poc-guide-v1.0` | PoC estructurado: alcance, criterios de éxito, go/no-go, timeboxing |

#### PM (+3 nuevas)

| ID | Descripción |
|---|---|
| `apb-pm-risk-register-v1.0` | Registro de riesgos: probabilidad × impacto, owner, mitigaciones, seguimiento |
| `apb-pm-status-report-v1.0` | Informe de estado semanal: avance, riesgos activos, hitos, impedimentos, RAG |
| `apb-pm-stakeholder-map-v1.0` | Mapa de stakeholders: interés, influencia, comunicación, frecuencia de reporte |

#### Design (+1 nueva)

| ID | Descripción |
|---|---|
| `apb-design-wcag-patterns-v1.0` | Patrones DevExtreme accesibles: configuraciones ARIA, navegación teclado, contraste |

---

## 9. Nuevos workflows propuestos

| ID | Agentes | Prioridad | Justificación |
|---|---|---|---|
| `apb-wf-change-management-v1.0` | Change Manager → Governance → Release Manager → SRE | Alta | Gap de ITIL crítico: ningún workflow cubre el proceso de aprobación de cambios en producción |
| `apb-wf-problem-management-v1.0` | Problem Manager → SRE → Tech Debt → Knowledge Manager | Alta | El Incident L1 escala pero no hay workflow de problema para incidencias recurrentes |
| `apb-wf-data-governance-v1.0` | Data Governance → Compliance Audit → Security Architect → Documentation | Alta | Obligación RGPD art. 30 (inventario de tratamientos) no tiene soporte |
| `apb-wf-incident-l2-v1.0` | Incident L2 → SRE → Problem Manager → Knowledge Manager | Media | El escalado de L1 no tiene receptor estructurado |
| `apb-wf-security-patch-v1.0` | Security Architect → Tech Debt → Change Manager → Platform Engineer → QA Auto | Media | Vulnerabilidades detectadas siguen proceso ad hoc; falta workflow estructurado |
| `apb-wf-api-lifecycle-v1.0` | API Product Manager → Technical Architect → Security Architect → Documentation → Release Manager | Media | Gestión del ciclo de vida de APIs del domain catalog cuando esté poblado |
| `apb-wf-accessibility-audit-v1.0` | Accessibility Auditor → UX Mockup → Implementer → QA Automation | Media | Obligación legal RD 1112/2018 para portales ciudadanos APB |
| `apb-wf-vendor-procurement-v1.0` | Business Analyst → Vendor Manager → Compliance Audit → Governance | Baja | Contratación LCSP es relevante pero el uso del agente aún no está probado |
| `apb-wf-finops-review-v1.0` | FinOps → Cloud Architect → Platform Engineer | Baja | Revisión periódica de costes; útil cuando FinOps Agent esté enriquecido |

---

## 10. Nuevos providers propuestos

| ID | Sistema | Descripción | Prioridad |
|---|---|---|---|
| `prov-azure-cost-v1.0` | Azure Cost Management API | API dedicada de costes: exportaciones, budgets, alertas, reservas. Diferente al Azure MCP genérico | Alta |
| `prov-confluence-v1.0` | Atlassian Confluence (REST API) | Operaciones directas Confluence: crear/actualizar páginas, espacios, adjuntos. Diferente de Rovo que es AI-driven | Media |
| `prov-entra-id-v1.0` | Microsoft Entra ID | Consultas Azure AD: usuarios, grupos, conditional access, registros de auditoría de identidad | Media |
| `prov-sentinel-v1.0` | Microsoft Sentinel | SIEM APB: consultas KQL, alertas activas, incidentes de seguridad, playbooks | Media |
| `prov-jira-software-v1.0` | Jira Software | Proyectos Jira Software: epics, sprints, backlog. Diferente de JSM para incidencias (prov-atlassian-v1.0) | Baja |

---

## 11. Resumen ejecutivo y priorización

### Gaps críticos por skills no conectadas (acción inmediata, costo cero)

El análisis revela que **varias skills existentes no están conectadas a los agentes correctos**. Estas conexiones son gratuitas (no requieren crear nada nuevo) y tienen impacto inmediato:

| Acción | Impacto |
|---|---|
| `apb-sub-dev-parallel-v1.0` → Implementer Agent | Habilita implementación paralela en el agente principal |
| `apb-disc-brainstorming-v1.0` → BA, Spec Engineer, Tech Discovery, Domain Architect | La skill obligatoria de exploración no está en los agentes que más la necesitan |
| `apb-sec-mitre-mapping-v1.0` + `apb-sec-cloud-hardening-v1.0` → Security Architect | Dos skills de seguridad robustas desconectadas |
| `apb-doc-generate-ppt-v1.0` + `apb-doc-generate-word-v1.0` → Documentation Agent | Skills de generación de documentos sin agente asignado |
| `apb-gov-jira-evidence-v1.0` + `apb-gov-evidence-v1.0` + `apb-plat-ms-notify-v1.0` → Risk Exception Agent | El agente de excepciones no puede registrar ni notificar |
| `apb-plat-deployment-finish-v1.0` → Release Manager | La skill de cierre de deployment existe pero no está en el Release Manager |
| `apb-qa-tdd-v1.0`, `apb-qa-readiness-check-v1.0`, `apb-qa-testing-strategy-v1.0`, `apb-qa-pipeline-v1.0` → QA Auto Agent | 4 skills de QA existentes no conectadas al agente principal de QA |
| `apb-arch-event-driven-master-v1.0`, `apb-arch-dotnet-base-v1.0`, `apb-arch-design-events-v1.0` → Technical Architect | 3 skills de arquitectura avanzadas sin conectar al Technical Architect |
| `apb-qa-framework-v1.0` → Meta Builder | El meta-builder no auto-valida los componentes que genera |

### Nuevos componentes por impacto y esfuerzo

| Prioridad | Componente | Esfuerzo estimado | Impacto |
|---|---|---|---|
| 🔴 1 | Change Management Agent + skill + workflow | 2-3 días-persona | Cierra el gap de ITIL en producción. Sin esto, el framework no está listo para producción real |
| 🔴 2 | Data Governance Agent + skills + workflow | 3-4 días-persona | Obligación legal RGPD art. 30. Riesgo de incumplimiento regulatorio |
| 🔴 3 | FinOps Agent: 3 skills + subagente + provider | 2-3 días-persona | El agente más delgado del catálogo para una función con impacto presupuestario directo |
| 🟡 4 | Problem Management Agent + skill | 2 días-persona | Completa el ciclo Incident → Problem → Known Error |
| 🟡 5 | Security: SAST + supply chain + patch skills → Security Architect | 2 días-persona | Moderniza la seguridad del framework con técnicas actuales |
| 🟡 6 | Platform: K8s + Service Bus + secret rotation skills | 2-3 días-persona | Necesario antes de cualquier migración a AKS |
| 🟡 7 | QA: performance + accesibilidad + contract testing | 2 días-persona | Testing moderno y cumplimiento legal WCAG |
| 🟡 8 | Incident L2 Agent + workflow | 1-2 días-persona | Completa el ciclo de soporte |
| 🟡 9 | Accessibility Auditor Agent + skill | 1-2 días-persona | Obligación legal RD 1112/2018 para portales ciudadanos |
| 🟢 10 | Tech Discovery: 3 skills nuevas | 1-2 días-persona | El agente más desaprovechado del catálogo; skills baratas que multiplican su valor |

### Cuadro resumen de componentes

| Tipo | Actuales | Conectar existentes | Nuevos | Total propuesto |
|---|---|---|---|---|
| Agentes | 26 | — | +9 | 35 |
| Subagentes | 23 | — | +8 | 31 |
| Skills APB | 129 | ~20 rewirings | +38 | 167 |
| Workflows | 8 | — | +9 | 17 |
| Providers | 14 | — | +5 | 19 |
| **Total** | **262** | **~20 rewirings (costo 0)** | **+69** | **~351** |

---

### Lo que NO implementar todavía

- **Portfolio IT Agent**: necesita datos reales de proyectos procesados por el framework.
- **Capacity Planner Agent**: necesita ≥12 meses de datos Azure históricos.
- **Chaos Engineering skill**: después de que SLOs estén definidos y testing normal esté maduro.
- **Vendor Procurement workflow**: después de que Vendor Manager Agent esté probado.

---

*Documento generado por IA (Claude, Anthropic). Requiere revisión y validación humana antes de usar como referencia oficial para el backlog del framework.*
