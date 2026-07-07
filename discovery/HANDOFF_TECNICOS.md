# Handoff Técnico APB — Pendientes por equipo

> ⚠️ Borrador generado por IA (Claude, Anthropic) — pendiente de validación por Arquitectura APB.  
> **Para:** Equipo técnico APB (Plataforma, Desarrollo, Operaciones, Ciberseguridad, QA, DPO, Negocio)  
> **De:** Arquitectura APB — Débora Martín  
> **Última actualización:** 2026-07-06 (reorganización verificada de
> `PLAN_FASES_FUTURAS.md` + sincronización de cifras — ver nota de proceso
> más abajo)  
> **Repositorios cubiertos:** APB-IA-FRAMEWORK · APB-DESIGN-SYSTEM · APB-DOMAIN-CATALOG  
> **Estado global:** 365 componentes (`generate_catalog.py`, 2026-07-07): 183 skills APB,
> 57 third-party, 39 agentes, 35 subagentes, 17 workflows, 23 providers, 7 wrappers,
> 4 adapters. 37 `approved` (todos terceros/wrapper de contexto, 0 apb-owned), 4
> `deprecated`, resto `draft`. Pendiente despliegue e inicio del ciclo de gobernanza
> sobre componentes propios. 7 de 8 bugs resueltos (BUG-03 pendiente confirmación color).
>
> **Nota de proceso (2026-07-06):** este documento es el único lugar donde debe
> vivir trabajo de puesta en producción real. No crear documentos de handoff
> sueltos adicionales (p. ej. `HANDOFF_SESION_N.md`) — cualquier hallazgo nuevo
> de esta categoría se añade aquí, en la sección que corresponda. Al cerrar
> cada sesión: regenerar catálogo (`generate_catalog.py`) y corregir aquí
> cualquier cifra de componentes desfasada.
> **Alcance de este documento:** solo tareas manuales de despliegue/producción que debe ejecutar
> una persona (crear una suscripción Azure, registrar una app AD, poblar un secreto en Key Vault,
> activar una licencia...). Las **decisiones o insumos que Débora/Dirección deben aportar** para
> poder planificar o construir algo viven en `discovery/PLAN_FASES_FUTURAS.md §I` (Bloqueos de
> Débora / Dirección), no aquí.

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
10. [Motor de orquestación, dashboards y seguimiento de auditorías](#10-motor-de-orquestación-dashboards-y-seguimiento-de-auditorías)
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
| **BUG-07** | `discovery/CONTINUIDAD_PROYECTO.md §8` | ✅ **RESUELTO (2026-07-07):** `generate_catalog.py` ejecutado, cifra real 365 componentes — corregido en este documento (cabecera + §2 + §3 + Estado global). `CONTINUIDAD_PROYECTO.md §8` **no requiere cambio**: su entrada histórica (208→341) es un BUG-07 distinto ya cerrado en su momento; la entrada de Sesión 27 ya refleja la cifra correcta. Nota de proceso: esta fila queda obsoleta cada vez que el catálogo se regenera tras añadir/quitar componentes — revisar contra `catalog/CATALOG.md` antes de asumir que sigue vigente. | — (sin acción pendiente) | — |
| **BUG-08** | `skills/third_party/third-lum1104-knowledge-graph-v1.0.md` | `source_license: "unverified"` — riesgo legal si se usa en producción | Verificar LICENSE en `https://github.com/Lum1104/Understand-Anything`; si no existe, marcar como `rejected` | 30 min |

**Criterio de éxito de BUG-01 + BUG-02:** `python scripts/validate_repo.py --strict` (exit 0) y `python scripts/generate_catalog.py --check` (sin drift) pasan en verde en CI.

---

## 2. Ciclo de aprobación — la prioridad de gobernanza

**Situación actual (2026-07-07):** 365 componentes; 37 `approved` (todos terceros/wrapper de contexto — ninguno `apb-owned` funcional), 4 `deprecated`, el resto en `draft`. Los controles de seguridad y autonomía declarados en frontmatter de los componentes `apb-owned` son promesas no auditadas. Sin aprobaciones propias, el framework no tiene base formal para uso en producción.

**Responsables:** Arquitectura APB + Ciberseguridad (two-eyes obligatorio por GOVERNANCE.md)

**Añadido 2026-07-02:** aprobar también `context/apb/standards/PROMPTING_STANDARD.md`
(estándar de estructura de prompt, ya aplicado a 244 componentes y exigido por el check #18
de `validate_repo.py`) y las secciones de harness `SYSTEM.md §10` / `GOVERNANCE.md §8`
(Pass-State Gating, Clean State Handoff). Responsable: Arquitectura APB.

**Reconciliación 2026-07-02 (Enriquecimiento #56–#76):** el discovery confirma que los
~55 componentes del enriquecimiento (7 agentes, 8 subagentes, 43 skills, 5 providers,
9 workflows) **ya están construidos** (Enriq. B/C/D) y **en `draft`** — son parte
prioritaria de este ciclo de aprobación. Diferidos por falta de datos: `apb-agent-capacity-planner`
y `apb-agent-portfolio-it` (#64). El agente `apb-agent-incident-l2` (#59) no se creó: su
función la cubren `apb-agent-incident-support` + `apb-wf-incident-l2`. Detalle en
`PLAN_FASES_COMPLETADAS.md`.

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

**Estado actual (2026-07-07):** `validate_repo.py --strict` → exit 0. 365 componentes, 0 huérfanos de wiring (los 5 subagentes que aparecían como pendientes de cablear ya estaban correctamente wireados en el repo real — verificado 2026-07-07, ver `PLAN_FASES_COMPLETADAS.md`). Estándar de prompting (check #18 en ERROR) + Cold-Start (check #19) + metodología de planes de pruebas (check #20) + conservación íntegra/ID canónico (check #21) + routing raíz agnóstico (check #22) + metodología de ejecución y aprobación (check #23, Fase I) + **evidencia de informes de ejecución: entrega dual + casos no ejecutados + vídeo real (check #24, nuevo)**. 47/47 tests. Sesión QA-2 cerrada: `TEST_PLAN_STANDARD`, `apb-qa-test-plan` v1.2.0, `prov-browser-agent`, `apb-qa-exploratory-nav`, ejemplo unificado TruckCenter, ejecución real en PRE.

**Sesión QA TruckCenter (2026-07-03) — ejecución real + corrección de metodología:**
- **Ejecución:** 44/120 casos del plan unificado (v1.4 → v1.5) con escritura real en PRE (B02-B07 + E2E
  T112), login EntraID asistido por Débora. **2 hallazgos críticos en la app** (H1 sin integridad
  referencial al eliminar Tipo de Vehículo; H2 maestro de tipos desactualizado) — documentados en el plan
  §15 y en `PLAN_FASES_COMPLETADAS.md`. **Acción manual pendiente de un desarrollador de TruckCenter (no
  IA, fuera de este framework): corregir H1 en el repo `APB.TRU`** (validación de integridad referencial
  antes de eliminar un tipo de vehículo en uso) — el defecto ya está materializado en PRE.
- **Corrección de metodología:** `TEST_PLAN_STANDARD` v1.3.0 → v1.4.0 (§5.15 casos no ejecutados
  obligatorios por ID, §7.2 vídeo real no GIF), skill `apb-qa-exploratory-nav` v1.0.0 → v1.1.0, check #24
  nuevo (+3 tests).
- **Playwright MCP activado:** `.mcp.json` de **proyecto** (raíz del repo, pendiente de confirmar commit)
  con el servidor oficial `@playwright/mcp`; `providers/prov-playwright-v1.0.md` v1.0.0 → v1.1.0 con la
  configuración real (sustituye el placeholder `local://playwright`). **Acción manual pendiente de
  cualquiera que retome esta sesión: reiniciar/reabrir Claude Code sobre el repo** para que las
  herramientas Playwright queden disponibles (no se cargan en caliente).
- Detalle completo → `discovery/PLAN_FASES_FUTURAS.md` puntos #84 (continuación) y #88 (nuevo,
  reejecución pendiente) + `PLAN_FASES_COMPLETADAS.md`.

**Continuación — Sesión II (misma fecha, 2026-07-03) — punto #88 NO seguido, queda abierto:**
- **+11 casos netos** (plan v1.5 → v1.6). **Total acumulado: 55/120 con estado registrado, 65 `Pendiente`
  sin tocar.** Reconfirmación en vivo de H1/H2/H4. **3 hallazgos nuevos:** H5 (rechaza NIF de empresa
  manual no existente en Sòstrat — no permite el alta libre descrita en el AF), H6 (Nombre Conductor
  mapeado como "." — mapeo WS Sòstrat), H7 (Swagger de `/trc/`, API `APB.API.LGP`, titulado por error como
  "APB.API.TRU"). **Acción manual pendiente de un desarrollador de TruckCenter/Sòstrat: revisar H5/H6/H7.**
- **Se saltó el punto #88**: no se reabrió Claude Code (Playwright MCP seguía sin cargar), se reusó GIF de
  `claude-in-chrome` sin segmentar por bloque (desviación de §7.2, declarada en el informe). **Acción
  manual pendiente de quien retome la sesión: reabrir Claude Code sobre este repo antes de empezar**, para
  que Playwright MCP quede disponible desde el inicio.
- Informes MD+HTML en OneDrive `QA_TruckCenter_evidencias/030726/` (sesión I y II). Detalle completo →
  `PLAN_FASES_COMPLETADAS.md` (subsección "Continuación — Sesión II") y punto #77 (segunda recurrencia del
  riesgo de runtime sin motor real, misma causa raíz que la sesión DDD del 2026-06-30).

**Fase I (2026-07-03) — 7 huecos de uso real cubiertos, `TEST_PLAN_STANDARD` v1.2.0 → v1.3.0:**
- Matriz de roles + usuario de ejecución (AKV ref o runtime, nunca persistido) — §9.2, columna «Rol requerido» en el ejemplo TruckCenter.
- Acta de aprobación del informe de resultados (Analista Funcional + Desarrollador; persistida en `.md` y en Jira, no firma criptográfica) — §6.2.
- Destino de ejecución `local` / `ci-runner` / `azure-qa` con matriz de decisión — §9.1; guía `docs/qa/EJECUCION_LOCAL.md` (nueva).
- Spec SDD como fuente autoritativa de primer nivel en el plan de pruebas — §1.
- Nuevo subagente `subagents/apb-sub-qa-fix-loop-v1.0.md` (`draft`): fallo → propone PR → anota Jira; nunca mergea.
- Nuevo provider `providers/prov-azure-qa-runtime-v1.0.md` (`draft`): entorno de ejecución efímero en Azure QA (Playwright + k6 preinstalados, Managed Identity → AKV) para no requerir instalación local.
- Ejemplo TruckCenter ampliado a 120 casos (**B13 Rendimiento k6** + **B14 Unitarias xUnit**, nuevos, append-only); secciones en prosa reformateadas a tabla (ARQ Docks, Integraciones, flujos ENTRADA/SALIDA, columnas GRID).
- Nota de desviación menor: el provider Azure QA **no** se registró en `SYSTEM.md §4.2` — esa tabla es solo de `adapters/`, no de `providers/`. Sin acción pendiente al respecto.

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
| DOC8 | ~~Actualizar `CONTINUIDAD_PROYECTO.md §8` con recuento real~~ | IA / Arquitectura APB | ✅ No aplica (verificado 2026-07-07): esa sección es un BUG-07 histórico distinto, ya correcto; la entrada de Sesión 27 tiene la cifra real (365, ver BUG-07) |
| QA2-1 | **Credenciales centrales para pruebas funcionales:** el agente de pruebas (`apb-qa-exploratory-nav` / `prov-browser-agent`) debe consultar credenciales desde un **repositorio central de secretos** (Azure Key Vault, `GOVERNANCE.md §5`) y capturar/reutilizar `storage_state` (EntraID), para ejecutar sin login manual. En la demo QA-2 (2026-07-02) las introdujo el usuario. **Diseño cubierto en Fase I** (2026-07-03): `TEST_PLAN_STANDARD §9.2` (usuario de ejecución por `AKV://<secret>` o runtime) + `docs/qa/EJECUCION_LOCAL.md` (captura/reutilización de `storageState`). **Pendiente:** poblar el secreto real en AKV y verificar el flujo end-to-end (Plataforma/Ciberseguridad). | Plataforma / Ciberseguridad / IA | 🟡 Diseñado, ejecución pendiente |
| QA3-1 | **Sesión QA-3 — ejecución funcional COMPLETA de TruckCenter.** Bloqueantes detectados en QA-2 E-bis: **F3** (PRE sin datos → sembrar dataset anonimizado RGPD), **F2** (formulario de Alta no carga >45s → investigar/priorizar), acceso de escritura para altas/bajas, 2ª pasada **USER_READ**, **k6** (rendimiento; API LGP ~9,3s F4), **SonarQube/OWASP ZAP** (seguridad), **unitarias** (repo `APB.TRU` + xUnit). Actualizar el AF por **F5** (maestro multiidioma CA/ES/EN). **Fase I añadió el andamiaje** (aún sin ejecución real): Bloque B13 (4 casos k6, `Pendiente`) y B14 (4 casos xUnit, `Pendiente`) en el ejemplo unificado, destino de ejecución `azure-qa` en `TEST_PLAN_STANDARD §9.1`. Evidencia visual: ver **QA3-2**, ítem separado por tener responsable y urgencia propios. | QA / Plataforma / Ciberseguridad / Dev | ⬜ Pendiente (Débora 2026-07-02; andamiaje Fase I 2026-07-03) |
| QA3-2 | **Desplegar `prov-azure-qa-runtime-v1.0` en Azure Container Apps — entorno efímero con Playwright/k6 preinstalados.** Resuelve de raíz un problema ya materializado dos veces (sesión QA TruckCenter, 2026-07-03, punto #88): la evidencia en vídeo real (`TEST_PLAN_STANDARD §7.2`) depende hoy de que Playwright MCP esté cargado en la sesión de Claude Code de quien ejecuta, y la carga k6 real (`TEST_PLAN_STANDARD §8.1`) no puede lanzarse desde un portátil — ambas dependen del puesto de trabajo de cada persona. **Actualización 2026-07-07: las imágenes Docker ya están generadas** en [`infra/azure-qa-runtime/`](../infra/azure-qa-runtime/README.md) (Dockerfiles Playwright + k6, listas para build/run en local ya mismo — ver README de esa carpeta). Débora ya tiene el entorno Container Apps creado; **avisará cuando quiera desplegar** (sin fecha fija, no es bloqueante urgente mientras el uso local cubra la necesidad). Pendiente real cuando lo confirme: build/push a ACR, crear el Container Apps Job referenciando la imagen, Managed Identity, red aislada a PRE/QA, población del secreto en AKV (comparte bloqueante con QA2-1). | Plataforma (a demanda de Débora) | 🟡 Contenedores listos para uso local; despliegue Azure pendiente de que Débora confirme el momento |

**Estructura mínima de cada runbook:**
```markdown
## Prerrequisitos (permisos, herramientas, artefactos de entrada)
## Ejecución normal — tabla fase/agente/input/output/checkpoint humano
## Gestión de errores por fase
## Rollback
## Métricas de éxito
```

---

## 10. Motor de orquestación, dashboards y seguimiento de auditorías

> Añadido 2026-07-06 al disolver `HANDOFF_ORQUESTACION_MOTOR.md` y
> `WORKSTREAMS_SUMMARY_2026-07-06.md` en este documento — ver
> `PLAN_FASES_COMPLETADAS.md` para el detalle de lo ya entregado.

### 10.1 Motor de orquestación (#77) — pasos condicionados a la decisión

La PoC de pausas humanas ya está entregada y funcionando
(`scripts/orchestrate_checkpoint_gate.py`, `.github/workflows/human-checkpoint-poc.yml`,
`scripts/setup_github_environment.py`). La elección del motor definitivo
(Azure Durable Functions / LangGraph / Temporal.io) vive en
`PLAN_FASES_FUTURAS.md` Sección A — es una decisión de Débora + Plataforma,
no una acción de ejecución. Una vez decidida, Plataforma ejecuta:

| Si se elige... | Plataforma ejecuta |
|---|---|
| **Azure Durable Functions** (recomendado) | 1) Arquitectura de Durable Functions + contratos de eventos. 2) Implementar motor macro + registrador de eventos. 3) Integrar agentes del framework (binding). 4) Validar workflow SDD completo. |
| **LangGraph** | 1) Wrapper de LangGraph sobre agentes existentes. 2) Refactor PoC → grafo con estado. 3) Persistencia opcional en Redis. 4) Integrar con GitHub Actions o ejecutor local. |
| **Temporal.io** | 1) Evaluación coste-beneficio previa (Arquitectura). 2) Desplegar `temporal-server` (auto-hosted o Cloud). 3) Refactor agentes → activities/workflows. 4) Workers dedicados + escalado. |

### 10.2 Despliegue real de dashboards de observabilidad (#39/#40)

Entregado y listo para importar (`discovery/qa-compliance-grafana-dashboard.json`,
`discovery/qa-compliance-powerbi-spec.json`, runbook operativo en
`discovery/QA_COMPLIANCE_DASHBOARD_RUNBOOK.md`):

| # | Acción | Responsable | Estado |
|---|--------|-------------|--------|
| OBS1 | Importar `qa-compliance-grafana-dashboard.json` en Grafana real, configurar datasource (Prometheus/Azure Monitor) | Plataforma | ⬜ Pendiente (~5 min) |
| OBS2 | Construir el modelo de datos de `qa-compliance-powerbi-spec.json` en Power BI, conectar Sonar/Jira/Dependabot, publicar | Plataforma / QA | ⬜ Pendiente (~1-2h) |
| OBS3 | Desplegar infraestructura de mensajería asíncrona (Azure Service Bus o Kafka) para cerrar el 4º gap de enforcement de autonomía (async messaging — los otros 3 gaps son ejecutables por Claude, ver `PLAN_FASES_FUTURAS.md` Sección B) | Plataforma | ⬜ Pendiente |

### 10.3 Accesos pendientes para sesiones ya diseñadas

| # | Qué se necesita | Desbloquea | Responsable |
|---|---|---|---|
| ACC1 | Acceso a histórico Jira (la skill de ingesta ya es ejecutable, falta el acceso real para probarla) | #37 — spec desde histórico | Plataforma / Jira Admin |
| ACC2 | Acceso a código del monolito SÒSTRAT (Java/Oracle → DOCKS) | #38 Fase 1 — descomposición de monolitos (además de la aprobación de dominios, ver §6) | Arquitectura / equipo SÒSTRAT |
| ACC3 | ≥12 meses de datos reales de uso en Azure | `apb-agent-capacity-planner`, `apb-agent-portfolio-it` (#64) | Plataforma |
| ACC4 | Validación de Ciberseguridad de `apb-sub-sec-sast-v1.0` + `apb-sub-ops-entra-v1.0` (SAST/Entra) y evaluación de necesidad de wrapper DAST (OWASP ZAP/Trivy) | R9/R10 — gap de seguridad ofensiva | Ciberseguridad |

### 10.4 Seguimiento de auditorías de aplicaciones (evidencia archivada)

Dos auditorías de aplicaciones concretas, ejecutadas y cerradas por el
framework, con follow-ups que debe resolver el equipo de desarrollo de cada
aplicación (no el framework). Informes completos archivados en
`discovery/archive/`:

| Auditoría | Hallazgo pendiente | Responsable | Esfuerzo |
|---|---|---|---|
| `archive/AUDIT_DESIGN_COMPLIANCE_TRU_2026-07-06.md` (TruckCenter) | No consume `apb-dx-overrides.css`/`tokens/*.css` del Design System, tipografía Cabin no aplicada, estilos inline sin variables CSS | Equipo TruckCenter | ~4-5h |
| `archive/AUDIT_QUALITY_COMPLIANCE_SMS_2026-07-06.md` (APB.API.SMS) | Ticket ARQ-3716 marcado "Resuelta" en Jira pero el código aún diverge de la corrección esperada (`NormalizeSender` debería ser `static`) | Equipo APB.API.SMS | Revisar y reabrir si aplica |

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
  └── Débora: aportar insumos — ver `PLAN_FASES_FUTURAS.md §I` (Bloqueos de Débora / Dirección)

CUANDO P3+P4 listos:
  └── Desarrollo: D1→D4 (Forge App)

CUANDO insumos de Débora disponibles (ver `PLAN_FASES_FUTURAS.md §I`):
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
| `APB-IA-FRAMEWORK` | — | **365 componentes** (37 aprobados, todos terceros — 0 apb-owned) | ✅ Framework construido / ⬜ Gobernanza pendiente / ⬜ Integraciones pendientes despliegue |
| `APB-DESIGN-SYSTEM` | v1.3.0 | 15 componentes React + configs DX + UI Kit | ✅ Listo para consumo / ⬜ Verificación DevExtreme CLI / ⬜ Decisión distribución |
| `APB-DOMAIN-CATALOG` | — | 21 dominios `proposed` (Sesión DDD 2026-06-30) | 🟢 Pendiente aprobación de Arquitectura |

---

> **Mantenimiento:** actualizar en cada sesión de trabajo. Marcar ✅ las acciones completadas.  
> **Generado por IA:** Claude (Anthropic/Claude Code), 2026-06-30.  
> **Validado por:** _pendiente — Débora Martín, Arquitectura APB._
