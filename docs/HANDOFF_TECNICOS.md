# Handoff Técnico APB — Pendientes por equipo

> **Para:** Equipo técnico APB (Plataforma, Desarrollo, Operaciones, Administración)  
> **De:** Arquitectura APB — Débora Martín  
> **Última actualización:** 2026-06-26  
> **Repositorios cubiertos:** APB-IA-FRAMEWORK · APB-DESIGN-SYSTEM · APB-DOMAIN-CATALOG  
> **Estado global:** Framework construido (262 componentes), integraciones especificadas, pendiente despliegue. Ver estado detallado de construcción en `discovery/CONTINUIDAD_PROYECTO.md`.

---

## ÍNDICE

1. [Integraciones Microsoft y Atlassian](#1-integraciones-microsoft-y-atlassian) — **BLOQUEANTE**
2. [Sesiones pendientes del framework](#2-sesiones-pendientes-del-framework)
3. [APB Design System](#3-apb-design-system)
4. [APB Domain Catalog](#4-apb-domain-catalog)
5. [Insumos que necesito de Débora](#5-insumos-que-necesito-de-débora)
6. [Orden de ejecución recomendado](#6-orden-de-ejecución-recomendado)

---

## 1. Integraciones Microsoft y Atlassian

> Detalle completo: [`docs/HANDOFF_SESION15_INTEGRACIONES.md`](./HANDOFF_SESION15_INTEGRACIONES.md)  
> Artefactos generados: `openapi/apb-framework-api.yaml`, `openapi/ai-plugin.json`, `forge/`, `docs/rovo-getting-started.md`

### PLATAFORMA APB — Requisito bloqueante para todas las integraciones

Sin estas acciones, ni M365 Copilot ni Rovo pueden invocar el framework.

| # | Acción | Artefacto de referencia | Estado |
|---|--------|------------------------|--------|
| P1 | Desplegar el backend del APB AI Framework en Azure (Azure Function o Container Apps) | `openapi/apb-framework-api.yaml` | ⬜ Pendiente |
| P2 | Publicar en Azure API Management — importar la spec OpenAPI y configurar OAuth 2.0 | `openapi/apb-framework-api.yaml` | ⬜ Pendiente |
| P3 | Registrar app Azure AD `apb-ai-framework-api` (scopes: `framework.read`, `framework.execute`) | `docs/rovo-getting-started.md §Paso 2` | ⬜ Pendiente |
| P4 | Registrar app Azure AD `apb-forge-rovo-client` (Client Credentials, permiso sobre P3) | `docs/rovo-getting-started.md §Paso 3` | ⬜ Pendiente |
| P5 | Registrar app Azure AD `apb-m365-copilot-plugin` (Authorization Code + Client Credentials) | `docs/HANDOFF_SESION15_INTEGRACIONES.md §Acción 4` | ⬜ Pendiente |
| P6 | Publicar `ai-plugin.json` en `https://apim.portdebarcelona.cat/.well-known/ai-plugin.json` | `openapi/ai-plugin.json` | ⬜ Pendiente |
| P7 | Guardar todas las credenciales en Azure Key Vault APB (nunca en texto plano ni en el repo) | — | ⬜ Pendiente |

| P8 | Configurar acceso del APB AI Framework a repos privados `portdebarcelona/ArqBase` y `portdebarcelona/ArqApiBase` en la organización GitHub | `providers/prov-arqbase-v1.0.md`, `providers/prov-arqapibase-v1.0.md` | ⬜ Pendiente |

**Verificación de hito P:** `GET https://apim.portdebarcelona.cat/ai-framework/v1/health` devuelve `200 OK`.

### DESARROLLO APB — Requiere P3 y P4 completados

| # | Acción | Fichero | Estado |
|---|--------|---------|--------|
| D1 | Implementar `getFrameworkToken()` en la Forge App (OAuth 2.0 Client Credentials) | `forge/src/functions/invokeFramework.js` — implementación de referencia en `docs/rovo-getting-started.md §Paso 5` | ⬜ Pendiente |
| D2 | Añadir caché de token (válido ~1h) y renovación automática (<5 min para expirar) | `forge/src/functions/invokeFramework.js` | ⬜ Pendiente |
| D3 | Implementar polling robusto o webhook para jobs >60 s (agentes complejos) | `forge/src/functions/invokeFramework.js` | ⬜ Pendiente |
| D4 | Desplegar Forge App: `forge deploy --environment development`, después `production` | `docs/rovo-getting-started.md §Paso 4` | ⬜ Pendiente |

**Verificación de hito D:** Desde Jira, chat Rovo → `¿Qué agentes APB tengo disponibles?` lista los 4 agentes.

### ADMINISTRADOR MICROSOFT 365 APB — Requiere P6 completado

| # | Acción | Estado |
|---|--------|--------|
| M1 | Verificar que el tenant APB tiene licencias activas de **Microsoft 365 Copilot** (no solo M365) | ⬜ Pendiente |
| M2 | Ir a **Microsoft 365 Admin Center > Integrated Apps > Upload custom app**, cargar el manifest o apuntar a la URL del `ai-plugin.json` | ⬜ Pendiente |
| M3 | Activar el plugin inicialmente solo para el grupo **Arquitectura APB** (piloto) | ⬜ Pendiente |

### ADMINISTRADOR ATLASSIAN APB — Requiere D4 completado

| # | Acción | Estado |
|---|--------|--------|
| A1 | Confirmar con Atlassian que el tenant APB tiene **Rovo activado y licenciado** (previsto julio 2026) | ⬜ Pendiente |
| A2 | Ir a **Atlassian Admin > Marketplace > Apps privadas**, aprobar `APB AI Framework — Rovo Agents` | ⬜ Pendiente |
| A3 | Activar inicialmente solo para el grupo **Arquitectura APB** | ⬜ Pendiente |

---

## 2. Sesiones pendientes del framework

> Repositorio: `APB-IA-FRAMEWORK`  
> Referencia: `discovery/PLAN_FASES_FUTURAS.md` y `discovery/CONTINUIDAD_PROYECTO.md`

### Sesión 13 — Cierre de pendientes históricos ✅ PARCIAL (2026-06-26)

Ejecutable mayoritariamente por Arquitectura APB. Algunos puntos requieren insumos de Débora (ver §5).

| Punto | Descripción | Insumo requerido | Estado |
|-------|-------------|-----------------|--------|
| #2 | Guía de uso de agentes (`docs/AGENT_USAGE_GUIDE.md`) | Ninguno — ejecutable | ✅ `docs/AGENT_USAGE_GUIDE.md` |
| #6 | Validación de cobertura de plantillas (comparación contra plantillas ofimáticas reales APB) | **Débora aporta ejemplos de plantillas Word/Excel en uso** | ⬜ Bloqueado |
| #7 | Mapa agente ↔ tipo de ticket Jira (qué genera qué, campos mínimos) | Ninguno — ejecutable | ✅ `docs/JIRA_AGENT_MAP.md` |
| #8 | COSMIC con histórico real de horas APB (calibrar estimaciones) | **Débora aporta histórico de proyectos (horas reales vs. estimadas)** | ⬜ Bloqueado |
| #12 | Formalizar bucles de iteración (loops de revisión/refinamiento entre agentes) | Ninguno — ejecutable | ✅ `docs/ITERATION_LOOPS.md` |
| #29 | Análisis de aplicabilidad de loop engineering en el framework | Ninguno — ejecutable | ✅ `docs/LOOP_ENGINEERING.md` |
| #41 | Análisis de niveles de autonomía + orquestación real de agentes (más allá de links declarativos) | Ninguno — ejecutable | ✅ `docs/AUTONOMY_LEVELS.md` |
| #44 | Actualizar `context/apb/templates/AGENT.md` (usa blockquotes obsoletos, debe usar YAML frontmatter igual que `SCHEMA.md`) | Ninguno — ejecutable | ✅ Template actualizado a YAML frontmatter |
| #48 | Estándares base .NET APB (APB.ARQ.BASE + APB.ARQ.APIBASE) — skill para agentes de implementación | Repos ArqBase + ArqApiBase revisados por Arquitectura APB | ✅ `skills/apb-owned/architecture/apb-arch-dotnet-base-v1.0.md` |
| #52 | Actualizar contacto de Arquitectura en todo el framework | **Débora confirma el mail oficial a usar** | ⬜ Bloqueado |

### Sesión 14 — Documentación por audiencias (Word)

| Entregable | Audiencia | Estado |
|-----------|-----------|--------|
| Documento Word: Guía ejecutiva del framework APB IA | Dirección / Comité TIC | ⬜ Pendiente |
| Documento Word: Guía de uso para analistas y desarrolladores | Equipos técnicos APB | ⬜ Pendiente |
| Documento Word: Manual de administración del framework | Plataforma / Operaciones | ⬜ Pendiente |

### Sesión 16 — Análisis de riesgo completo ✅ CONSTRUIDO

El skill está listo. Requiere que el equipo lo use en el proceso de validación antes de producción:

| Acción para el equipo | Responsable | Estado |
|----------------------|------------|--------|
| Ejecutar `apb-gov-org-risk-report-v1.0` sobre cada agente y skill antes del despliegue en producción | Arquitectura APB | ⬜ Pendiente |
| Obtener firma de aprobación de Ciber / Arq / QA en los informes generados | Dirección / Comité TIC | ⬜ Pendiente |

### Sesión 19 — Evaluaciones de terceros pendientes

| Punto | Descripción | Insumo requerido | Estado |
|-------|-------------|-----------------|--------|
| #27 | Repositorios externos sin URL confirmada (evaluación de herramientas) | **Débora aporta URLs o confirma descarte** | ⬜ Bloqueado |
| #45 | 3 skills en `skills/apb-ai-skills/_spec-driven/` — evaluar para fusión o archivo | Ninguno — ejecutable | ⬜ Pendiente |

### Sesión 20 — Agentes de contratación (LCSP)

| Punto | Descripción | Insumo requerido | Estado |
|-------|-------------|-----------------|--------|
| #36 | Agentes especializados en procedimientos LCSP (Ley de Contratos del Sector Público) | **Débora aporta briefing de contratación (tipos de procedimiento, plantillas, umbrales)** | ⬜ Bloqueado |

### Sesión 21 — SQL, soporte a incidencias y QA ✅ CERRADA (2026-06-26)

| Punto | Descripción | Estado |
|-------|-------------|--------|
| #15 | Agente de soporte técnico de primera línea (incidencias) | ✅ `agents/apb-agent-incident-support-v1.0.md` |
| #33 | Skills SQL (generación, revisión, optimización) | ✅ `skills/.../apb-dev-sql-gen-v1.0.md` + `apb-dev-sql-review-v1.0.md` |
| #34 | Validación QA en pipelines de despliegue | ✅ `skills/.../apb-qa-pipeline-v1.0.md` |
| #50 | QA del propio framework | ✅ `skills/.../apb-qa-framework-v1.0.md` |

**Componentes adicionales generados en Sesión 21:**
- `skills/apb-owned/operation/apb-ops-incident-triage-v1.0.md`
- `skills/apb-owned/operation/apb-ops-incident-diagnose-v1.0.md`
- `skills/apb-owned/operation/apb-ops-incident-escalate-v1.0.md`
- `subagents/apb-sub-ops-oracle-v1.0.md`
- `subagents/apb-sub-ops-iis-apache-v1.0.md`
- `subagents/apb-sub-ops-network-v1.0.md`
- `subagents/apb-sub-ops-azure-v1.0.md`
- `workflows/apb-wf-incident-l1-v1.0.md`

### Sesión 22 — Refactor de taxonomía de carpetas ✅ PARCIAL (2026-06-26)

| Punto | Descripción | Insumo requerido | Estado |
|-------|-------------|-----------------|--------|
| #47bis | Revisar taxonomía de carpetas `skills/` y `agents/` tras el crecimiento del framework | Ninguno — ejecutable | ✅ Completado — 13 carpetas consolidadas, 12 third_party a `_uncategorized/`, nueva carpeta `orchestration/` |
| #49 | Decisión sobre el mecanismo de distribución del Design System | **Débora decide: npm privado, Git submodule, o CDN** | ⬜ Bloqueado |

### Fase #43 — Marcado IA obligatorio ✅ COMPLETADO (2026-06-26)

Las 129 skills `apb-owned` ya tienen la sección `## Marcado IA obligatorio (POLICY_AI_USAGE §6)`.
El estándar completo está en `context/apb/standards/AI_MARKING_STANDARD.md`.

**Acción pendiente del equipo humano (Arquitectura APB):**

| Tarea | Descripción | Responsable | Estado |
|-------|-------------|-------------|--------|
| Validar marcado | Revisar que el tipo de artefacto asignado a cada skill es correcto (código, SQL, Jira, doc, IaC, email…). Corregir si alguna skill tiene el tipo equivocado. | Arquitectura APB | ⬜ Pendiente revisión |
| Aprobar `AI_MARKING_STANDARD.md` | El estándar está en `draft`. Arquitectura APB debe formalizarlo (`status: active`). | Arquitectura APB | ⬜ Pendiente aprobación |
| Campo `human_validated_by` | Cuando se valide formalmente cada skill, rellenar el campo de validador humano según el criterio que decida Débora (nombre retroactivo / revisión formal por componente). | Arquitectura APB | ⬜ Criterio pendiente de Débora |

---

## 3. APB Design System

> Repositorio: `APB-DESIGN-SYSTEM` — versión actual **v1.3.0**  
> Estado general: **Completo para consumo** — tokens, componentes React, configs DevExtreme, UI Kit listos.

### Verificaciones técnicas pendientes

| # | Tarea | Responsable | Estado |
|---|-------|-------------|--------|
| DS1 | Verificar compatibilidad del tema base `generic.light` de DevExtreme con los tokens CSS APB en un proyecto CLI real (no solo en mockup) | Desarrollo APB | ⬜ Pendiente |
| DS2 | Completar el catálogo de componentes más allá de los documentados en las guías PDF originales (identificar gaps) | Desarrollo APB | ⬜ Pendiente |
| DS3 | Decisión sobre distribución formal del Design System (ver punto #49 del framework: npm privado, submodule o CDN) | **Débora decide** | ⬜ Bloqueado |

### Consumo del Design System — recordatorio para Desarrollo APB

```bash
# Tokens CSS
<link rel="stylesheet" href="tokens/tokens.css">

# Componente React (import directo del repo)
import { APBButton } from './components/core/APBButton';

# DevExtreme — incluir en el proyecto
<link rel="stylesheet" href="components-dx/apb-dx-overrides.css">
<script src="components-dx/apb-dx-config.js"></script>
```

---

## 4. APB Domain Catalog

> Repositorio: `APB-DOMAIN-CATALOG`  
> Estado general: **Repositorio inicializado y scaffolding listo** — pendiente primera propuesta de dominio.

### Acciones pendientes

| # | Tarea | Insumo requerido | Estado |
|---|-------|-----------------|--------|
| DC1 | Ejecutar una sesión de análisis funcional con el subagente `apb-sub-ddd-interview-v1.0` para identificar el primer dominio APB a catalogar | Ninguno — ejecutable con cualquier área funcional APB | ⬜ Pendiente |
| DC2 | Revisar el artefacto `domain.md` generado por el subagente y abrirlo como PR en `APB-DOMAIN-CATALOG/domains/<nombre>/` | Requiere DC1 | ⬜ Pendiente |
| DC3 | Aprobar el dominio siguiendo el proceso de `GOVERNANCE.md` (estado `proposed` → `under_review` → `approved`) | Arquitectura APB | ⬜ Bloqueado hasta DC2 |

**Nota:** El subagente ya verifica automáticamente si el dominio existe en el catálogo antes de proponer uno nuevo. El equipo solo necesita revisar el `domain.md` generado y abrir el PR — no hay que rellenar el template a mano.

### Proceso de ingesta de dominios

```
1. El funcional habla con apb-sub-ddd-interview-v1.0 (entrevista guiada)
2. El subagente verifica APB-DOMAIN-CATALOG — si el dominio no existe, genera domain.md
3. El equipo revisa el domain.md y abre PR en APB-DOMAIN-CATALOG/domains/<nombre>/
4. Arquitectura APB revisa y aprueba el PR → estado pasa a "proposed" → "under_review" → "approved"
5. El catálogo DOMAINS.md se actualiza
```

---

## 5. Insumos que necesito de Débora

> Estas tareas están **bloqueadas** hasta que Débora aporte los siguientes materiales.  
> Para cada una: enviar por mail a `arquitectura@portdebarcelona.cat` o subir a la carpeta acordada en SharePoint APB.

| Prioridad | Insumo | Para desbloquear | Formato sugerido |
|-----------|--------|-----------------|-----------------|
| 🔴 Alta | Mail oficial de contacto de Arquitectura APB | Punto #52 (todo el framework) | Una dirección de correo |
| 🔴 Alta | Lista de APIs/servicios APB por dominio de negocio | APB-DOMAIN-CATALOG (DC1) | Excel, Word o correo |
| 🟡 Media | Ejemplos de plantillas Word/Excel ofimáticas en uso actualmente en APB | Sesión 13 punto #6 | Ficheros Word/Excel reales |
| 🟡 Media | Histórico de proyectos: horas reales vs. horas COSMIC estimadas | Sesión 13 punto #8 | Excel o tabla |
| 🟡 Media | Decisión sobre distribución del Design System (npm / submodule / CDN) | DS3 + Sesión 22 punto #49 | Decisión verbal o escrita |
| 🟠 Baja | URLs de repositorios externos pendientes de evaluación | Sesión 19 punto #27 | Lista de URLs |
| 🟠 Baja | Briefing de contratación LCSP (procedimientos, plantillas, umbrales) | Sesión 20 punto #36 | Word o PDF |

---

## 6. Orden de ejecución recomendado

```
AHORA — en paralelo:
  ├── Plataforma APB: P1 → P2 → P3+P4+P5 → P6+P7  (4-8 semanas, bloqueante)
  ├── Débora aporta insumos de §5 (sin bloqueo técnico)
  └── Arquitectura APB: Sesión 13 (puntos sin insumos: #2, #7, #12, #29, #41, #44, #48)

CUANDO P3+P4 listos:
  └── Desarrollo APB: D1 → D2 → D3 → D4

CUANDO P8 listo (acceso GitHub repos privados):
  └── Agentes de implementación pueden leer ArqBase/ArqApiBase en tiempo real

CUANDO D4 listo:
  ├── Admin Atlassian: A1 → A2 → A3
  └── Admin M365: M1 → M2 → M3

CUANDO insumos de Débora disponibles:
  ├── Sesión 13 (puntos bloqueados: #6, #8, #52)
  ├── Sesión 14 (documentación Word)
  ├── Sesión 16 (riesgo)
  ├── Sesión 19 (#27, #45)
  ├── Sesión 20 (LCSP)
  └── APB Domain Catalog (DC1 → DC2 → DC3)

CUANDO sesiones 13-22 completas:
  └── Fase #43 — etiquetado retroactivo (última fase del plan)

CUANDO integraciones P1-P7 desplegadas (fase posterior):
  └── Migrar actualización prov-arqbase/prov-arqapibase a CI automático
      (GitHub Action en ArqBase/ArqApiBase → PR automático en APB-IA-FRAMEWORK)
      Referencia: context/apb/policies/POLICY_ARCHITECTURE_BASE.md §5
```

---

## Estado global por repositorio

| Repositorio | Versión | Componentes | Estado |
|-------------|---------|-------------|--------|
| `APB-IA-FRAMEWORK` | — | 226 componentes | ✅ Framework construido / ⬜ Sesiones 13–22 pendientes / ⬜ Integraciones pendientes despliegue |
| `APB-DESIGN-SYSTEM` | v1.3.0 | 15 componentes React + configs DX + UI Kit | ✅ Listo para consumo / ⬜ Verificación DevExtreme CLI pendiente |
| `APB-DOMAIN-CATALOG` | — | 0 dominios (scaffolding listo) | ⬜ Primera propuesta de dominio pendiente de insumos |

---

> **Mantenimiento de este documento:** actualizar en cada sesión de trabajo. Marcar ✅ las acciones completadas.  
> **Generado por IA:** Claude (Anthropic/Claude Code), 2026-06-26.  
> **Validado por:** _pendiente — Débora Martín, Arquitectura APB._
