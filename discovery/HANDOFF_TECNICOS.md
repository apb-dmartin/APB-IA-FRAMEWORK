# Handoff Técnico APB — Pendientes por equipo

> ⚠️ Borrador generado por IA (Claude, Anthropic) — pendiente de validación por Arquitectura APB.  
> **Para:** Equipo técnico APB (Plataforma, Desarrollo, Operaciones, Ciberseguridad, QA, DPO, Negocio)  
> **De:** Arquitectura APB — Débora Martín  
> **Última actualización:** 2026-06-30 (post KB+SP — knowledge base corporativa + system prompts LLM-agnósticos)  
> **Repositorios cubiertos:** APB-IA-FRAMEWORK · APB-DESIGN-SYSTEM · APB-DOMAIN-CATALOG  
> **Estado global:** 343 componentes (176 skills APB, 52 third-party, 35 agentes, 33 subagentes,
> 17 workflows, 19 providers, 7 wrappers, 4 adapters). 0 componentes aprobados. Pendiente despliegue e inicio
> del ciclo de gobernanza. 211/211 skills+agents con system prompt LLM-agnóstico. 7 de 8 bugs resueltos (BUG-03 pendiente confirmación color).

---

## ÍNDICE

1. [Bugs críticos — acción inmediata](#1-bugs-críticos--acción-inmediata)
2. [Ciclo de aprobación — la prioridad de gobernanza](#2-ciclo-de-aprobación--la-prioridad-de-gobernanza)
3. [Wiring y deuda interna del catálogo](#3-wiring-y-deuda-interna-del-catálogo)
4. [Integraciones Microsoft y Atlassian](#4-integraciones-microsoft-y-atlassian)
5. [APB Design System](#5-apb-design-system)
6. [APB Domain Catalog](#6-apb-domain-catalog)
7. [Seguridad y compliance](#7-seguridad-y-compliance)
8. [Telemetría](#8-telemetría)
9. [Documentación pendiente](#9-documentación-pendiente)
10. [Insumos bloqueantes de Débora](#10-insumos-bloqueantes-de-débora)
11. [Orden de ejecución recomendado](#11-orden-de-ejecución-recomendado)

---

## 1. Bugs críticos — acción inmediata

Estos bugs afectan al CI y a la integridad del catálogo. Esfuerzo total < 2h.

| Bug | Archivo | Impacto | Fix | Esfuerzo |
|-----|---------|---------|-----|---------|
| **BUG-01** | `context/apb/templates/WORKFLOW.md` | Cualquier workflow nuevo creado desde el template falla en CI — usa blockquotes en lugar de frontmatter YAML | Reemplazar encabezado blockquote por bloque YAML con campos de SCHEMA.md §3.4 | 20 min |
| **BUG-02** | `scripts/generate_catalog.py` función `update_index_md` | El step de CI "Verificar sincronización de catálogo" lleva tiempo crasheando — cuantificador posesivo `\s*+` no válido en Python 3.10 | Cambiar `\s*+` → `\s*` en los 8 patrones afectados | 30 min |
| **BUG-03** | `APB-DESIGN-SYSTEM/components/component-reference.md §9` | Sidebar color documentado como `#2c3e50` pero el CSS real es `--apb-sidebar-bg: #ffffff` (corregido en v1.3.0) | Actualizar §9 para referenciar `var(--apb-sidebar-bg)` | 5 min |
| **BUG-04** | `adapters/claude/adapter-claude-v1.0.md` | Model string `claude-sonnet-4-20250514` obsoleto | Actualizar al model string actual | 5 min |
| **BUG-05** | `SYSTEM.md §4.2` | Solo documenta 2 adapters; existen 4 (`claude`, `copilot`, `m365`, `rovo`) | Añadir filas de `adapters/m365/` y `adapters/rovo/` con estado `draft` | 10 min |
| **BUG-06** | `.github/workflows/telemetry.yml` | El workflow hace `git push` directo a `main` para actualizar `telemetry/events.jsonl` — anti-patrón CI y vector de seguridad | Usar Azure Blob Storage como buffer (Opción A) o rama `telemetry-log` sin protección (Opción B) | 1 día |
| **BUG-07** | `discovery/CONTINUIDAD_PROYECTO.md §8` | Inventario documenta 226 componentes; la realidad es 341 (+115 de sesiones 15-23 no registradas) | Ejecutar `generate_catalog.py` (tras BUG-02) y actualizar §8 | 1h |
| **BUG-08** | `skills/third_party/third-lum1104-knowledge-graph-v1.0.md` | `source_license: "unverified"` — riesgo legal si se usa en producción | Verificar LICENSE en `https://github.com/Lum1104/Understand-Anything`; si no existe, marcar como `rejected` | 30 min |

**Criterio de éxito de BUG-01 + BUG-02:** `python scripts/validate_repo.py --strict` (exit 0) y `python scripts/generate_catalog.py --check` (sin drift) pasan en verde en CI.

---

## 2. Ciclo de aprobación — la prioridad de gobernanza

**Situación actual:** 341 componentes, 100% en estado `draft`. Los controles de seguridad y autonomía declarados en frontmatter son promesas no auditadas. Sin aprobaciones, el framework no tiene base formal para uso en producción.

**Responsables:** Arquitectura APB + Ciberseguridad (two-eyes obligatorio por GOVERNANCE.md)

**Añadido 2026-07-02:** aprobar también `context/apb/standards/PROMPTING_STANDARD.md`
(estándar de estructura de prompt, ya aplicado a 244 componentes y exigido por el check #18
de `validate_repo.py`) y las secciones de harness `SYSTEM.md §10` / `GOVERNANCE.md §8`
(Pass-State Gating, Clean State Handoff). Responsable: Arquitectura APB.

### Preparación previa (Arquitectura APB, 2h)

Antes de iniciar aprobaciones, añadir a `SCHEMA.md` los campos:
- `human_validator`: string. Formato `"Nombre Apellido (Rol)"`. Obligatorio en estado `approved`.
- `retry_strategy`: objeto con `max_retries`, `backoff_seconds`, `on_failure` (enum: `halt` / `skip` / `escalate`).

### Los 5 primeros candidatos (por impacto y uso actual)

| # | Componente | Tipo | Razón |
|---|-----------|------|-------|
| 1 | `apb-gov-ai-risk-gate-v1.0` | Skill | Transversal — otros workflows la necesitan aprobada |
| 2 | `apb-dev-code-review-v1.0` | Skill | Más usada en revisiones de código diarias |
| 3 | `apb-agent-spec-engineer-v1.0` | Agente | Central del flujo SDD, el más invocado |
| 4 | `apb-agent-technical-architect-v1.0` | Agente | Necesaria para diseños con respaldo formal |
| 5 | `apb-wf-sdd-full-v1.0` | Workflow | Aprobarlo valida el proceso extremo a extremo |

### Proceso por componente (~90 min cada uno)

| Paso | Tiempo | Responsable |
|------|--------|-------------|
| 1. Verificar frontmatter completo (todos los campos de SCHEMA.md presentes) | 10 min | Dev |
| 2. Verificar secciones obligatorias: Marcado IA, Comportamiento ante inputs incompletos | 20 min | Dev |
| 3. Revisión funcional: ¿el prompt hace lo que declara `description`? | 30 min | Arquitectura APB |
| 4. Revisión two-eyes (segundo aprobador del ámbito correspondiente) | 30 min | Ciberseguridad / QA |
| 5. Actualizar: `status: approved`, `human_validator`, `review_date` + PR | 5 min | Dev |

**Criterio de éxito:** ≥5 componentes en `approved`. La métrica "% en draft" baja del 100%.

---

## 3. Wiring y deuda interna del catálogo

> **Actualizado 2026-06-30 — FASE 0 completada (commit `d62c6b1`).**

| # | Acción | Detalle | Estado |
|---|--------|---------|--------|
| T1 | **Wiring Enriquecimiento B** | 40 wirings aplicados en 22 agentes (skills + subagentes). `validate_bidirectional_wiring()` en validador garantiza consistencia futura. | ✅ RESUELTO |
| T2 | **Huérfanos previos** | Todos los huérfanos identificados (orch×2, design-wcag, ops-capacity/continuity, finops-azure, ops-k8s/aca/rancher/servicebus) cableados en sesiones anteriores o en FASE 0. | ✅ RESUELTO |
| T3 | **Duplicados — decidir** | 3 grupos: `apb-design-wcag` vs `apb-design-wcag-patterns`; `apb-arch-api-contract`/`api-lifecycle`/`apb-dev-api-design`; `apb-qa-validation-e2e` vs `apb-sub-qa-e2e`. | ⬜ Pendiente decisión Arquitectura |
| T4 | **Validador bidireccional** | `validate_bidirectional_wiring()` añadida; `TestValidateBidirectionalWiring` (2 tests). `--strict` → exit 0, 0 errores, 59 warnings exentos. | ✅ RESUELTO |
| T5 | **Template `AGENT.md`** | Sigue en formato blockquote antiguo (punto #44). Quien lo use genera un componente que falla el validador. Fix: YAML frontmatter igual que SCHEMA.md. | ⬜ Pendiente |

**Estado actual:** `validate_repo.py --strict` → exit 0. 341 componentes, 0 huérfanos de wiring.

---

## 4. Integraciones Microsoft y Atlassian

> Artefactos generados: `openapi/apb-framework-api.yaml`, `openapi/ai-plugin.json`, `forge/`, `docs/rovo-getting-started.md`  
> Detalle de implementación técnica: `docs/rovo-getting-started.md`

### PLATAFORMA APB — Bloqueante para todas las integraciones

Sin estas acciones, ni M365 Copilot ni Rovo pueden invocar el framework.

| # | Acción | Referencia | Estado |
|---|--------|-----------|--------|
| P1 | Desplegar backend del framework en Azure (Azure Function o Container Apps) | `openapi/apb-framework-api.yaml` | ⬜ Pendiente |
| P2 | Publicar en Azure API Management — importar spec OpenAPI + OAuth 2.0 | `openapi/apb-framework-api.yaml` | ⬜ Pendiente |
| P3 | Registrar app Azure AD `apb-ai-framework-api` (scopes: `framework.read`, `framework.execute`) | `docs/rovo-getting-started.md §Paso 2` | ⬜ Pendiente |
| P4 | Registrar app Azure AD `apb-forge-rovo-client` (Client Credentials) | `docs/rovo-getting-started.md §Paso 3` | ⬜ Pendiente |
| P5 | Registrar app Azure AD `apb-m365-copilot-plugin` (Authorization Code + Client Credentials) | `docs/rovo-getting-started.md` | ⬜ Pendiente |
| P6 | Publicar `ai-plugin.json` en `https://apim.portdebarcelona.cat/.well-known/ai-plugin.json` | `openapi/ai-plugin.json` | ⬜ Pendiente |
| P7 | Guardar todas las credenciales en Azure Key Vault APB | — | ⬜ Pendiente |
| P8 | Configurar acceso a repos privados `portdebarcelona/ArqBase` y `portdebarcelona/ArqApiBase` | `providers/prov-arqbase-v1.0.md` | ⬜ Pendiente |

**Hito de verificación P:** `GET https://apim.portdebarcelona.cat/ai-framework/v1/health` devuelve `200 OK`.

### DESARROLLO APB — Requiere P3 y P4 completados

| # | Acción | Referencia | Estado |
|---|--------|-----------|--------|
| D1 | Implementar `getFrameworkToken()` en Forge App (OAuth 2.0 Client Credentials) | `forge/src/functions/invokeFramework.js` + `docs/rovo-getting-started.md §Paso 5` | ⬜ Pendiente |
| D2 | Añadir caché de token (~1h) y renovación automática (<5 min para expirar) | `forge/src/functions/invokeFramework.js` | ⬜ Pendiente |
| D3 | Implementar polling robusto o webhook para jobs >60 s | `forge/src/functions/invokeFramework.js` | ⬜ Pendiente |
| D4 | Desplegar Forge App: `forge deploy --environment development` → `production` | `docs/rovo-getting-started.md §Paso 4` | ⬜ Pendiente |

**Hito de verificación D:** Desde Jira, chat Rovo → `¿Qué agentes APB tengo disponibles?` lista los agentes.

### ADMINISTRADOR MICROSOFT 365 APB — Requiere P6 completado

| # | Acción | Estado |
|---|--------|--------|
| M1 | Verificar licencias activas de **Microsoft 365 Copilot** en el tenant APB | ⬜ Pendiente |
| M2 | Microsoft 365 Admin Center > Integrated Apps > cargar manifest o URL del `ai-plugin.json` | ⬜ Pendiente |
| M3 | Activar inicialmente solo para el grupo **Arquitectura APB** (piloto) | ⬜ Pendiente |

### ADMINISTRADOR ATLASSIAN APB — Requiere D4 completado

| # | Acción | Estado |
|---|--------|--------|
| A1 | Confirmar con Atlassian que el tenant APB tiene **Rovo activado** (previsto julio 2026) | ⬜ Pendiente |
| A2 | Atlassian Admin > Marketplace > Apps privadas: aprobar `APB AI Framework — Rovo Agents` | ⬜ Pendiente |
| A3 | Activar inicialmente solo para el grupo **Arquitectura APB** | ⬜ Pendiente |

### Aclaraciones frecuentes

- **Probar antes del despliegue:** es posible hoy adjuntando el `.md` del agente directamente en Claude web o Claude Code. No requiere infraestructura.
- **Si Rovo no está disponible en julio:** la integración M365 Copilot (plugin) es independiente y puede activarse antes.
- **Arquitectura de seguridad:** M365 Copilot / Rovo → APIM APB → backend framework → Claude API. El backend es el único componente con la clave de Claude API.

---

## 5. APB Design System

> Repositorio: `APB-DESIGN-SYSTEM` — versión actual **v1.3.0**  
> Estado: completo para consumo — tokens CSS, componentes React, configs DevExtreme, UI Kit.

| # | Tarea | Responsable | Estado |
|---|-------|-------------|--------|
| DS1 | Verificar compatibilidad del tema `generic.light` de DevExtreme con los tokens CSS APB en proyecto CLI real | Desarrollo APB | ⬜ Pendiente |
| DS2 | Completar catálogo de componentes más allá de los documentados en guías PDF originales | Desarrollo APB | ⬜ Pendiente |
| DS3 | **Decisión sobre distribución** (npm privado / git submodule / CDN) — ver punto #49 | **Débora decide** | ⬜ Bloqueado |
| DS4 | Resolver discrepancia tipográfica: Cabin vs. Helvetica Neue en `style-guide.md §2.1` | Arquitectura APB (decisión), Dev (implementación) | ⬜ Pendiente |

**Consumo actual del Design System:**
```bash
# Tokens CSS
<link rel="stylesheet" href="tokens/tokens.css">

# Componente React
import { APBButton } from './components/core/APBButton';

# DevExtreme
<link rel="stylesheet" href="components-dx/apb-dx-overrides.css">
<script src="components-dx/apb-dx-config.js"></script>
```

---

## 6. APB Domain Catalog

> Repositorio: `APB-DOMAIN-CATALOG` — **21 dominios de negocio `proposed`** (Sesión DDD, 2026-06-30)  
> **Estado:** inventario `API_INVENTORY_APIM.md` recibido + entrevista ejecutada → 15 `domain.md` en `domains/`. **Pendiente:** PR + aprobación de Arquitectura APB (y experto de negocio para las fronteras pendientes). Hasta que pasen a `approved`, los subagentes DDD aún no deben consumirlos como verdad establecida. **Bounded contexts diferidos** a sesión con acceso a código/BBDD.

| # | Tarea | Prerrequisito | Estado |
|---|-------|--------------|--------|
| DC1 | ~~Ejecutar entrevista DDD para identificar el primer dominio APB~~ | Lista de sistemas/APIs de Débora | ✅ **Hecho (2026-06-30)** — 21 dominios `proposed` |
| DC2 | Aprobación de los 21 dominios `proposed` (PR a APB-DOMAIN-CATALOG) | Revisión Arquitectura + experto de negocio | ⬜ Pendiente |
| DC3 | Modelar bounded contexts (`bc-*.md`) por dominio | Acceso a código/BBDD de los repos DOCKS/SOSTRAT | ⬜ Diferido |
| DC2 | Revisar `domain.md` generado y abrir PR en `APB-DOMAIN-CATALOG/domains/<nombre>/` | DC1 | ⬜ Pendiente |
| DC3 | Aprobar dominio (estado `proposed` → `under_review` → `approved`) vía GOVERNANCE.md del catalog | DC2 | ⬜ Pendiente |

**Objetivo mínimo de Fase 1:** ≥3 dominios en estado `approved`. Candidatos probables: Gestión de Atraques, Tráfico de Mercancías, Gestión de Concesiones.

**Proceso de ingesta:**
```
1. Funcional habla con apb-sub-ddd-interview-v1.0 (entrevista guiada)
2. Subagente verifica APB-DOMAIN-CATALOG — si el dominio no existe, genera domain.md
3. Equipo revisa domain.md y abre PR en APB-DOMAIN-CATALOG/domains/<nombre>/
4. Arquitectura APB aprueba PR → estado: proposed → under_review → approved
```

---

## 7. Seguridad y compliance

| # | Tarea | Urgencia | Responsable |
|---|-------|---------|-------------|
| S1 | **Co-aprobar los 5 componentes candidatos** (rol two-eyes obligatorio por GOVERNANCE.md) | Crítica | Ciberseguridad |
| S2 | Verificar licencia `third-lum1104-knowledge-graph-v1.0` (ver BUG-08) | Alta | Ciberseguridad / Arquitectura APB |
| S3 | Auditar que el M365 plugin no expone credenciales AKV al runtime de Copilot | Alta | Ciberseguridad |
| S4 | Definir scopes OAuth mínimos para adapter-rovo Forge App (scope `write:confluence-content` es amplio) | Alta | Ciberseguridad |
| S5 | Ejecutar `apb-gov-org-risk-report-v1.0` sobre cada agente y skill antes del despliegue | Alta | Arquitectura APB |
| S6 | Validar `apb-gov-dpia`, `apb-gov-data-classification` y `apb-sub-gov-data` contra criterio AEPD (RGPD art. 30/35, ENS) | Alta | DPO |
| S7 | Definir proceso de gestión de supply chain para los 59 componentes de terceros sin SHA verificado | Media | Ciberseguridad |
| S8 | Desactivar GitHub Actions de `apb-ai-skills` deprecado (`sync-skills.yml`, `validate-skills.yml`) | Media | Plataforma |

---

## 8. Telemetría

El código de telemetría está completo (`emit_telemetry.py`, `telemetry.yml`). Solo faltan los secrets de Azure.

| # | Acción | Responsable | Estado |
|---|--------|-------------|--------|
| TEL1 | Crear Data Collection Endpoint (DCE) en Azure Monitor | Plataforma | ⬜ Pendiente |
| TEL2 | Crear Data Collection Rule (DCR) con tabla `APBFrameworkTelemetry_CL` | Plataforma | ⬜ Pendiente |
| TEL3 | Configurar GitHub Secrets: `AZURE_MONITOR_DCE_ENDPOINT`, `AZURE_MONITOR_DCR_ID`, `AZURE_TENANT_ID`, `AZURE_MONITOR_CLIENT_ID`, `AZURE_MONITOR_CLIENT_SECRET` | Plataforma | ⬜ Pendiente |
| TEL4 | Test manual: `python3 scripts/emit_telemetry.py --event '{"component_id":"test","outcome":"success"}'` → verificar en Log Analytics | Plataforma + Dev | ⬜ Pendiente |
| TEL5 | Rediseñar `telemetry.yml` para eliminar auto-commit a `main` (BUG-06) — usar Azure Blob Storage | Dev + Plataforma | ⬜ Pendiente |

**Criterio de éxito:** evento visible en `APBFrameworkTelemetry_CL` en < 5 min tras la emisión.

---

## 9. Documentación pendiente

| # | Entregable | Audiencia | Estado |
|---|-----------|-----------|--------|
| DOC1 | Runbook `wf-sdd-full` — paso a paso reproducible | Arquitectura + Dev | ⬜ Pendiente |
| DOC2 | Runbook `wf-code-review` — paso a paso reproducible | Dev + QA | ⬜ Pendiente |
| DOC3 | Documento Word: Guía ejecutiva del framework APB IA | Dirección / Comité TIC | ⬜ Pendiente |
| DOC4 | Documento Word: Guía de uso para analistas y desarrolladores | Equipos técnicos APB | ⬜ Pendiente |
| DOC5 | Documento Word: Manual de administración del framework | Plataforma / Operaciones | ⬜ Pendiente |
| DOC6 | Guía de "Primera skill / Primer agente" para onboarding rápido | Nuevos contribuidores | ⬜ Pendiente |
| DOC7 | Documentar deprecación `apb-ai-skills` en README del framework | Todos | ⬜ Pendiente |
| DOC8 | Actualizar `CONTINUIDAD_PROYECTO.md §8` con recuento real: 341 componentes (sesiones 15-23 no registradas) | IA / Arquitectura APB | ⬜ Pendiente |

**Estructura mínima de cada runbook:**
```markdown
## Prerrequisitos (permisos, herramientas, artefactos de entrada)
## Ejecución normal — tabla fase/agente/input/output/checkpoint humano
## Gestión de errores por fase
## Rollback
## Métricas de éxito
```

---

## 10. Insumos bloqueantes de Débora

Estas tareas no pueden iniciarse sin una decisión o aportación explícita de Débora.

| Prioridad | Insumo | Desbloquea | Cuándo se necesita |
|-----------|--------|-----------|-------------------|
| ~~🔴 Alta~~ ✅ | ~~**Lista de APIs/servicios APB por dominio de negocio**~~ **RECIBIDA (2026-06-30)** — `API_INVENTORY_APIM.md` | APB-DOMAIN-CATALOG poblado (21 dominios `proposed`) + agentes DDD desbloqueados | Hecho |
| 🔴 Alta | **Mail oficial de contacto de Arquitectura APB** | Punto #52 — todo el framework | Este mes |
| 🟡 Media | **Qué componentes aprobar primero + aprobadores por ámbito** | Primer ciclo de aprobación formal | Este mes |
| 🟡 Media | **Decisión distribución Design System** (npm / submodule / CDN) | DS3 + sesión 22 punto #49 | Este trimestre |
| 🟡 Media | **Ejemplos de plantillas Word/Excel ofimáticas en uso en APB** | Sesión 13 punto #6 | Este trimestre |
| 🟡 Media | **Histórico de proyectos: horas reales vs. COSMIC estimadas** | Calibración `apb-disc-cosmic-v1.0` | Este trimestre |
| 🟠 Baja | **Briefing de procesos de licitación LCSP** | Agentes de licitación (sesión 20, punto #36) | Este trimestre |
| 🟠 Baja | **URLs de repositorios externos pendientes de evaluación** | Sesión 19 punto #27 | Este trimestre |
| 🟠 Baja | **Confirmación disponibilidad Rovo en tenant APB** | Activación `adapter-rovo-v1.0` | Julio 2026 |

---

## 11. Orden de ejecución recomendado

```
ESTA SEMANA (< 4h, cualquier desarrollador):
  ├── BUG-02: Fix regex generate_catalog.py (30 min)
  ├── BUG-01: Fix WORKFLOW.md template frontmatter (20 min)
  ├── BUG-03: Fix sidebar color component-reference.md (5 min)
  ├── BUG-04: Fix modelo adapter-claude-v1.0 (5 min)
  ├── BUG-05: Fix SYSTEM.md §4.2 — 4 adapters (10 min)
  └── DOC7: Documentar deprecación apb-ai-skills en README (30 min)

ESTE MES (alta prioridad):
  ├── ✅ T1+T2: Wiring huérfanos Enriquecimiento B — COMPLETADO (FASE 0, 2026-06-30)
  ├── FASE 1: Mejoras workflows (sdd-full, cloud-migration, code-review, incident-l1, legacy-onboarding, qa-evidence)
  ├── SCHEMA.md: Añadir campos human_validator + retry_strategy (Arquitectura APB)
  ├── Ciclo de aprobación: 5 componentes candidatos (Arquitectura + Ciber)
  ├── TEL1→TEL4: Configurar telemetría Azure Monitor (Plataforma)
  └── DOC1+DOC2: Runbooks wf-sdd-full y wf-code-review

EN PARALELO CON LO ANTERIOR (no bloqueante entre sí):
  ├── Plataforma: P1→P8 (integraciones, 4-8 semanas)
  └── Débora: aportar insumos de §10

CUANDO P3+P4 listos:
  └── Desarrollo: D1→D4 (Forge App)

CUANDO insumos de Débora disponibles:
  └── DC1→DC3 (APB-DOMAIN-CATALOG primer dominio)

ESTE TRIMESTRE:
  ├── BUG-06: Rediseñar telemetry.yml (Dev + Plataforma)
  ├── BUG-07: Actualizar CONTINUIDAD con recuento real
  ├── BUG-08: Verificar licencia lum1104
  ├── S3+S4: Auditorías de seguridad integraciones
  ├── DOC3→DOC6: Documentación por audiencias (Sesión 14)
  └── T3: Resolver duplicados del catálogo
```

---

## Estado global por repositorio

| Repositorio | Versión | Componentes | Estado |
|-------------|---------|-------------|--------|
| `APB-IA-FRAMEWORK` | — | **341 componentes** (0 aprobados) | ✅ Framework construido / ⬜ Gobernanza pendiente / ⬜ Integraciones pendientes despliegue |
| `APB-DESIGN-SYSTEM` | v1.3.0 | 15 componentes React + configs DX + UI Kit | ✅ Listo para consumo / ⬜ Verificación DevExtreme CLI / ⬜ Decisión distribución |
| `APB-DOMAIN-CATALOG` | — | 21 dominios `proposed` (Sesión DDD 2026-06-30) | 🟢 Pendiente aprobación de Arquitectura |

---

> **Mantenimiento:** actualizar en cada sesión de trabajo. Marcar ✅ las acciones completadas.  
> **Generado por IA:** Claude (Anthropic/Claude Code), 2026-06-30.  
> **Validado por:** _pendiente — Débora Martín, Arquitectura APB._
