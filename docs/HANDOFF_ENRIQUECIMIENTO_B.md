# Handoff — Post-Enriquecimiento B y análisis 360° (2026-06-29)

> ⚠️ Borrador generado por IA (Claude, Anthropic) — pendiente de validación por Arquitectura APB.
> **Audiencia:** Arquitectura, Plataforma/Cloud, Operaciones/SRE, Ciberseguridad, DPO, QA, Negocio/PM,
> Gobernanza del catálogo. **Fuente:** análisis 360° en `discovery/PLAN_FASES_FUTURAS.md`
> (sección "Análisis 360° y reconciliación de estado — 2026-06-29"). **Commit base:** `384f9d1`.

## 1. Qué entrega esta sesión

- Enriquecimiento B: 32 skills + 4 agentes + 5 subagentes creados y validados (CI verde, 19/19 tests).
- Fix de plantilla `SUBAGENT.md` (faltaba frontmatter) y de referencia rota que tumbaba el CI.
- Mejora del validador: en `--strict` ahora **destaca los warnings bloqueantes** por separado de los
  59 exentos de `source_commit` (evita leer "0 errores" como éxito).
- Este análisis 360° + handoff.

## 2. Lo que NO está cerrado (acción técnica, costo casi cero)

| # | Acción | Detalle |
|---|--------|---------|
| T1 | **Wiring de Enriquecimiento B** | Las 16 skills nuevas no están en la lista `skills:` de sus "Agentes destino" (especificados en el plan #60–72), y 4 de 5 subagentes no están declarados en su agente padre. Hoy son **invocables solo desde los 4 agentes nuevos**, no desde QA Auto, Technical Architect, Platform Engineer, FinOps, Governance, etc. |
| T2 | **Huérfanos previos** | 9 skills + 5 subagentes de sesiones anteriores también sin cablear (orch×2, design-wcag, ops-capacity/continuity, finops-azure, ops-k8s/aca/rancher/servicebus). |
| T3 | **Duplicados** | Decidir sobre 3 grupos: `apb-design-wcag` vs `apb-design-wcag-patterns`; `apb-arch-api-contract`/`api-lifecycle`/`apb-dev-api-design`; `apb-qa-validation-e2e` vs `apb-sub-qa-e2e`. |
| T4 | **Endurecer validador** | Check anti-huérfanos (warning) + fix encoding Windows (`cp1252`) + test (20/20). Evita que la deuda se repita. |
| T5 | **Plantilla `AGENT.md`** (#44) | Sigue en formato blockquote antiguo: quien la use genera un componente que falla el validador. |

## 3. Decisiones que SOLO puede tomar Débora / Dirección (desbloquean trabajo)

| Decisión | Desbloquea | Punto |
|---|---|---|
| **Listado de APIs de APB** | Poblar el catálogo de dominios → toda la cadena DDD/modernización (Fase 1 monolitos) | #38 |
| **Mecanismo de distribución del Design System** (npm Azure Artifacts / git submodule / CDN) | Sesión 22, skills de plataforma, mockup validación | #49/#53 |
| **Briefing de licitación (LCSP)** | Agentes de licitación | #36 |
| **Horas históricas para COSMIC** | Calibrar `apb-disc-cosmic-v1.0` (puntos↔horas para facturación) | #8 |
| **URLs de terceros + decisión `_spec-driven`** | Sesión 19 (incorporación de terceros) | #27/#45 |
| **Email/cola Jira de Arquitectura** | Sustituir contacto en toda la documentación | #52 |
| **Ejemplos Word/Excel ofimáticos** | Plantillas de documentación | #6 |
| **Qué componentes aprobar primero + aprobadores por ámbito** | Primer ciclo de aprobación (salir de 89% draft) | §2.6 |

## 4. Tareas por equipo

| Equipo | Qué validar / hacer |
|---|---|
| **Arquitectura APB** | Revisar y aprobar (draft→candidate) los 4 agentes y skills arch/disc nuevos; validar el wiring (T1–T2); decidir duplicados (T3); priorizar el primer ciclo de aprobación; liderar la decisión de runtime de orquestación (Semantic Kernel / Azure AI Foundry). |
| **Plataforma / Cloud** | Validar K8s/AKS, Service Bus, secret-rotation, environment-promotion y las 3 skills FinOps contra el stack y las cuentas Azure reales (naming, tiers, tags). Activar integraciones M365 (ver `HANDOFF_SESION15_INTEGRACIONES.md`). Preparar pipeline parametrizable con validaciones APB. |
| **Operaciones / SRE** | Validar subagente Entra ID y skills post-mortem/capacity/continuity; aportar umbrales y SLOs reales; preparar runbooks-puente mientras no haya orquestación programática. |
| **Ciberseguridad** | Aprobar `apb-sub-sec-sast` y `apb-sub-ops-entra` (operaciones sensibles: SAST, MFA, Conditional Access) antes de uso real; validar exenciones `source_commit`; cerrar `prov-sentinel`/`prov-entra-id`. |
| **DPO / Protección de datos** | Validar `apb-gov-dpia`, `apb-gov-data-classification` y `apb-sub-gov-data` contra criterio AEPD (RGPD art. 30/35, ENS). |
| **QA** | Definir y arrancar tests de **comportamiento** (extender el piloto `tests/test_agent_behavior.md`, #50/#51); validar performance/contract/accessibility. |
| **Negocio / PM** | Validar utilidad de las skills funcionales (user-journey, value-stream, risk-register, status-report, stakeholder-map) y confirmar perfiles que las usarán. |
| **Gobernanza del catálogo** | Registrar el validador humano por componente (requisito `SYSTEM.md §7.2` para `approved`); planificar la telemetría que alimente los KPIs; mantener reconciliado `plan ↔ repo`. |

## 5. Criterio de cierre (verificación)

- `PYTHONIOENCODING=utf-8 python scripts/validate_repo.py --strict` → **EXITOSA** (exit 0 es el
  criterio canónico, **no** el conteo de "errores").
- `python scripts/generate_catalog.py --check` → sin drift · `unittest` → 19/19 (20/20 con T4).
- Tras T1–T2: 0 skills huérfanas de B; cada subagente declarado en su padre.
- Un componente solo pasa a `approved` cuando tiene, en su propio cuerpo, origen IA **y** validador
  humano nombrado (`SYSTEM.md §7.2`).
