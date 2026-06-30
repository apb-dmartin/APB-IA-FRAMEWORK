# APB AI Framework — Informe Ejecutivo

> ⚠️ Borrador generado por IA (APB AI Framework) — pendiente validación humana. No distribuir sin revisión.

> **Audiencia:** Dirección APB, CIO, CISO, Gerencia TI  
> **Fecha:** 2026-06-30  
> **Versión del framework:** 1.0.0-draft · 342 componentes construidos  
> **Estado:** Preparado para pilotos controlados. Pendiente aprobación formal para uso en producción.

---

## 1. ¿Qué es y qué problema resuelve?

### El problema

Los equipos de APB llevan meses usando herramientas de IA (GitHub Copilot, Claude, Rovo) de forma **no coordinada**: cada equipo configura la IA a su manera, sin que ésta conozca los estándares de codificación APB, la arquitectura Azure corporativa, las obligaciones ENS o los procedimientos internos. El resultado es que la IA genera código o documentos que hay que corregir manualmente porque no tiene el contexto de la organización.

### La solución

El **APB AI Framework** es la plataforma corporativa de IA del Port de Barcelona: un repositorio de conocimiento estructurado que enseña a las herramientas de IA a trabajar como lo hace APB.

En lugar de usar IA genérica, los equipos invocan **agentes especializados** que ya conocen:
- El stack tecnológico APB (.NET, DevExpress, Azure SQL, Service Bus, AKS)
- Los estándares de desarrollo y las políticas de seguridad (ENS nivel alto, OWASP, RGPD, LCSP)
- Los procesos internos (SDD, gestión de incidencias, releases, auditorías)

### La premisa irrenunciable

> **La IA propone. El humano aprueba.**

Ningún componente del framework puede auto-aprobarse, auto-mergearse ni tomar decisiones de producción. Todos los puntos críticos requieren validación humana explícita.

---

## 2. Estado actual (a 2026-06-30)

| Indicador | Valor |
|-----------|-------|
| Componentes construidos | **342** (175 skills, 52 third-party, 35 agentes, 33 subagentes, 17 workflows, 19 providers, 7 wrappers, 4 adapters) |
| Componentes aprobados para producción | **0** — todos en `draft` |
| Validación técnica | ✅ exit 0, 0 errores, 21 tests OK |
| Runtimes soportados | GitHub Copilot · Claude · M365 Copilot · Atlassian Rovo |
| Repositorios del framework | APB-IA-FRAMEWORK · APB-DESIGN-SYSTEM · APB-DOMAIN-CATALOG |
| Esfuerzo de construcción | 22 sesiones de trabajo (mayo–junio 2026) |

**Todos los componentes están en `draft`**, lo que significa que están construidos y validados técnicamente pero aún no han pasado el ciclo de revisión y aprobación formal por parte de los equipos responsables (Arquitectura, Ciberseguridad, QA, DPO según el dominio).

---

## 3. Capacidades disponibles hoy

El framework cubre **6 dominios** del ciclo de vida del software en APB:

| Dominio | Qué hace la IA | Agente principal |
|---------|---------------|-----------------|
| **Desarrollo** | Genera código .NET siguiendo estándares APB, revisa PRs, escribe tests unitarios (cobertura ≥80%) | `apb-agent-implementer-v1.0` |
| **Arquitectura** | Diseña arquitecturas C4, diagramas DDD, bounded contexts, mapas de contexto | `apb-agent-technical-architect-v1.0` |
| **QA** | Genera planes de pruebas, automatiza tests E2E (Playwright), valida accesibilidad (WCAG), evalúa release readiness | `apb-agent-qa-auto-v1.0` |
| **Operaciones** | Gestiona incidencias L1→L2, diagnóstico, escalado, post-mortem, observabilidad | `apb-agent-incident-support-v1.0` |
| **Gobierno** | Verifica cumplimiento ENS/OWASP/RGPD, genera evidencias Jira, evalúa riesgos IA, audita el propio framework | `apb-agent-governance-v1.0` |
| **Plataforma / Cloud** | Gestiona infraestructura AKS, Service Bus, FinOps Azure, rotación de secretos, promoción de entornos | `apb-agent-platform-engineer-v1.0` |

### Flujos de trabajo completos ya disponibles

| Workflow | Qué automatiza |
|----------|---------------|
| `apb-wf-sdd-full-v1.0` | Ciclo completo Spec Driven Development: desde discovery hasta release |
| `apb-wf-code-review-v1.0` | Revisión de código asistida: calidad, seguridad, estándares, evidencias |
| `apb-wf-incident-l1-v1.0` | Gestión de incidencia L1 con escalación automática a L2 |
| `apb-wf-cloud-migration-v1.0` | Migración a cloud con validación de infraestructura, seguridad y costes |
| `apb-wf-legacy-onboarding-v1.0` | Onboarding de repos legacy: documentación, specs, backlog de modernización |
| `apb-wf-qa-evidence-v1.0` | QA completo con evidencias auditables para gobierno y releases |

---

## 4. Política de uso y gobierno IA

El framework implementa la política corporativa **POLICY_AI_USAGE §6** en cada componente:

- **Marcado obligatorio** de todos los artefactos generados por IA (documentos, código, commits, tickets Jira)
- **Sin credenciales en el repositorio** — todas las referencias usan Azure Key Vault o variables de entorno
- **Sin despliegue directo a producción** desde workflows automatizados — siempre requiere revisión humana
- **Trazabilidad total** de qué generó la IA y cuándo, para auditorías ENS y RGPD

La autonomía máxima de cualquier agente es **Nivel 1** (genera con revisión), con excepción de escenarios de telemetría interna (Nivel 2, supervisada). Los niveles 3 y 4 (automatización) no están habilitados.

---

## 5. Inversión realizada y próximo hito

### Lo construido (mayo–junio 2026)

| Etapa | Resultado |
|-------|-----------|
| Sesiones 1–8 | Estructura base: skills APB, agentes, workflows, providers, catálogo automático |
| Sesiones 9–16 | Enriquecimiento: gobierno, plataforma, FinOps, terceros, arquitectura |
| Sesiones 17–22 | Marcado IA completo, system prompts, wiring bidireccional, design system |
| FASE 0 (2026-06-30) | Higiene de wiring + validador bidireccional — exit 0 |
| FASE 1 (2026-06-30) | 6 workflows mejorados (Change Manager, Security Architect, escalación L1→L2…) |
| FASE 1B (2026-06-30) | 7 bugs corregidos (regex Python, model string, CI anti-pattern, templates, docs) |

### Próximo hito: primer ciclo de aprobación formal

El objetivo es pasar del **0% aprobado actual** a un estado en que los componentes críticos (los que más se usarán primero) estén en `approved`. KPI objetivo: **<30% en draft** en los próximos 3 meses.

Para ello, Arquitectura APB necesita:
1. Seleccionar los 10 componentes core a aprobar primero
2. Asignar 2 aprobadores por componente (ámbitos distintos: técnico + seguridad o funcional)
3. Ejecutar el ciclo de revisión con los equipos correspondientes

---

## 6. Decisiones que requieren intervención de Dirección

| Decisión | Impacto si no se toma | Urgencia |
|----------|-----------------------|---------|
| **Qué componentes aprobar primero y quién aprueba** | El framework no puede usarse en producción; los equipos siguen improvisando | 🔴 Mes 1 |
| **Runtime de orquestación** (Azure AI Foundry vs. Anthropic Claude SDK) | Sin esta decisión no hay ejecución real de workflows multi-agente | 🟡 Mes 1 |
| **Mecanismo de distribución del Design System** | Los componentes UI corporativos siguen copiándose entre proyectos a mano | 🟡 Mes 1 |
| **Listado de APIs/sistemas APB** | El Domain Catalog queda vacío; no se puede hacer DDD ni descomposición de monolitos | 🔴 Bloqueante FASE 3 |
| **Primer piloto real** (equipo + proyecto) | Sin un piloto, el framework sigue siendo teoría; los KPIs de uso siguen a 0 | 🔴 Mes 1 |

---

## 7. Documentación disponible por audiencia

| Documento | Audiencia | Ubicación |
|-----------|-----------|-----------|
| Este informe | Dirección / CIO / CISO | `docs/informe-direccion.md` |
| Guía funcional | Analistas, desarrolladores, PMs | `docs/guia-funcional.md` |
| Manual de arquitectura | Arquitectos, Technical Leads | `docs/manual-arquitectura.md` |
| Guía de uso de agentes | Equipos técnicos | `docs/AGENT_USAGE_GUIDE.md` |
| Handoff técnico por equipo | Plataforma, QA, Ciberseguridad, DPO, Negocio | `discovery/HANDOFF_TECNICOS.md` |

---

*Documento generado por el APB AI Framework. Requiere revisión y validación humana antes de distribución.*
