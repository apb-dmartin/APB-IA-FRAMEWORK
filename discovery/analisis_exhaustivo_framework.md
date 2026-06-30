# Análisis Exhaustivo APB AI Framework — Multi-perspectiva
> **Preparado por:** Claude (Anthropic) — Análisis de repositorios APB-IA-FRAMEWORK, APB-DOMAIN-CATALOG, APB-DESIGN-SYSTEM  
> **Fecha:** 2026-06-29  
> **Validado por humano:** _pendiente — Débora Martín / Arquitectura APB_  
> **Advertencia:** Todo lo que aquí se propone es propuesta IA. Ningún punto es ejecutable sin revisión y aprobación humana.


---

## 1. Estado Real del Framework — Cifras Verificadas

### 1.1 Recuento por generate_catalog.py (ejecutado hoy)

El inventario real difiere significativamente del recuento de CONTINUIDAD_PROYECTO.md (226 componentes, que quedó desactualizado tras las sesiones 15-23):

| Tipo | Real (2026-06-29) | CONTINUIDAD decía | Delta |
|------|-------------------|-------------------|-------|
| Skills APB | **175** | 114 | +61 |
| Skills terceros | **51** | 52 | -1 |
| Agentes | **35** | 21 | +14 |
| Subagentes | **33** | 13 | +20 |
| Workflows | **17** | 7 | +10 |
| Providers | **19** | 10 | +9 |
| Wrappers | **7** | 7 | 0 |
| Adaptadores | **4** | 2 | +2 |
| **TOTAL** | **341** | **226** | **+115** |

Las sesiones 15, 16, 21, 22, 23 y parcialmente 13 añadieron 115 componentes que CONTINUIDAD no registró. **Cualquier planificación basada en ese recuento trabajaba con datos incorrectos.**

### 1.2 Estado de gobernanza

- **0 componentes aprobados** de 341. Todos en `draft`.
- **0 dominios** en APB-DOMAIN-CATALOG (catálogo completamente vacío).
- **0 runbooks** operativos.
- **19 tests de validador** OK.
- **CI/CD activo** en cada PR a `main` (con un bug crítico — ver BUG-02).
- **APB-DESIGN-SYSTEM v1.3.0** funcional pero con inconsistencia documental (BUG-03).

### 1.3 Adapters reales vs. lo documentado en SYSTEM.md

SYSTEM.md §4.2 lista solo 2 adapters. La realidad es 4:

| Adapter | Estado | Activación |
|---------|--------|-----------|
| `adapter-claude-v1.0` | draft | Activo — en uso en esta sesión |
| `adapter-copilot-v1.0` | draft | Activo — uso diario |
| `adapter-m365-copilot-v1.0` | draft | Pendiente — 5 pasos definidos, esperando activación |
| `adapter-rovo-v1.0` | draft | Pendiente — objetivo julio 2026 |

**SYSTEM.md §4.2 está desactualizado. Es el BUG-05.**


---

## 2. Revisión 100% del plan_accion.md — Validación en Código

### Acción 1 — "Fix context/apb/templates/AGENT.md"

**Veredicto: ARCHIVO INCORRECTO IDENTIFICADO EN EL PLAN.**

He leído el archivo. `AGENT.md` ya tiene frontmatter YAML correcto y completo. No hay nada que corregir en él.

El archivo que SÍ usa el formato blockquote antiguo es **`context/apb/templates/WORKFLOW.md`**, que empieza así:

```
# {name}

> **ID:** `{id}`
> **Versión:** {version}
```

Esto no es frontmatter YAML. El validador rechazará cualquier workflow creado desde esta plantilla porque no tendrá el bloque `---`. La Acción 1 debe corregirse para apuntar a WORKFLOW.md.

**Riesgo:** cualquier desarrollador que cree un nuevo workflow desde el template actual produce un archivo que falla en CI desde el primer commit.

### Acción 2 — Documentar deprecación de apb-ai-skills

**Veredicto: NO EJECUTADA.** CONTINUIDAD §13.3 dice explícitamente "no se ha tocado el repositorio apb-ai-skills". La decisión verbal de deprecar está tomada pero no documentada formalmente en ningún README.

### Acción 3 — Verificar source_commit para skills de terceros

**Veredicto: APLAZADA POR POLÍTICA DELIBERADA — CORRECTO.** GOVERNANCE.md §4.2 exime explícitamente `source_commit: "unverified"` del modo estricto. 59 warnings, todos exentos por política. No es un defecto. El plan_accion.md debería aclarar que esta acción requiere acceso de red a cada repo externo y no es urgente.

### Acción 4 — Primer ciclo de aprobación formal

**Veredicto: NO EJECUTADA.** Ningún componente ha avanzado de `draft`. Es la acción de mayor impacto de gobernanza pendiente.

### Acción 5 — Catálogo de dominios

**Veredicto: BLOQUEADA.** APB-DOMAIN-CATALOG tiene cero dominios. El scaffolding está listo. Bloqueada esperando la lista de APIs/sistemas de Débora.

### Acción 6 — Runbooks

**Veredicto: NO EJECUTADA.** No existe ningún runbook en el repositorio.

### Acción 7 — Telemetría Azure Monitor

**Veredicto: PARCIALMENTE IMPLEMENTADA.** El código está completo y funcional (`emit_telemetry.py`, `telemetry.yml`). Lo que falta son los GitHub Secrets de Azure configurados. Sin ellos, la Action falla silenciosamente.

### Acción 8 — Campos SCHEMA.md (human_validator, retry_strategy)

**Veredicto: NO EJECUTADA.** SCHEMA.md no tiene estos campos.

### Acción 9 — Skills autorizadas para Level 2

**Veredicto: NO EJECUTADA.** No existe documento ni proceso consolidado.

### Acción 10 — Tipografía Design System

**Veredicto: NO EJECUTADA.** La discrepancia Cabin vs. Helvetica Neue sigue sin resolverse en style-guide.md §2.1.

### Resumen del plan

| Acción | Estado real |
|--------|-------------|
| 1 — Fix template | ⚠️ Archivo incorrecto — el bug está en WORKFLOW.md, no AGENT.md |
| 2 — Deprecar apb-ai-skills | ❌ Pendiente |
| 3 — source_commit | ✅ Aplazada por política (decisión correcta) |
| 4 — Primer ciclo aprobación | ❌ **Crítica — no ejecutada** |
| 5 — Catálogo dominios | 🔴 Bloqueada esperando dato de Débora |
| 6 — Runbooks | ❌ Pendiente |
| 7 — Telemetría | ⚠️ Código OK, Azure sin configurar |
| 8 — Campos SCHEMA | ❌ Pendiente |
| 9 — Nivel 2 autorizado | ❌ Pendiente |
| 10 — Tipografía | ❌ Pendiente |


---

## 3. Bugs y Errores Encontrados — Revisión 100% de Código

### BUG-01 — CRÍTICO: Template WORKFLOW.md sin frontmatter YAML

**Archivo:** `context/apb/templates/WORKFLOW.md`  
**Impacto:** cualquier workflow nuevo creado desde esta plantilla falla en CI en el primer commit.  
**Fix:** reemplazar el encabezado blockquote por un bloque YAML frontmatter completo con los campos de SCHEMA.md §3.4 (`id`, `name`, `description`, `version`, `status`, `owner`, `domain`, `autonomy_level`, `agents`, `human_checkpoints`, `created_date`, `review_date`).

### BUG-02 — MEDIO: generate_catalog.py crashea en Python 3.10 por regex inválida

**Archivo:** `scripts/generate_catalog.py`, función `update_index_md`  
**Código afectado:**
```python
(re.compile(r"(agents/\s*+# )\d+( agentes)"), ...)
```
El cuantificador posesivo `\s*+` no es válido en el módulo `re` estándar de Python (solo en el módulo `regex` de terceros). Causa crash con `error: nothing to repeat` en Python 3.10.

**Verificado empíricamente:** `python3 scripts/generate_catalog.py --check` lanza Traceback en este entorno.

**Consecuencia operativa:** el step de CI "Verificar sincronización de catálogo" lleva tiempo fallando sin detectarse. El drift de INDEX.md, CATALOG.md y DOMAIN_REGISTRY.md no se valida en ningún PR. Puede haber desincronización acumulada.

**Fix:** eliminar el `+` posesivo en los 8 patrones afectados de la función. Cambiar `\s*+` por `\s*` en cada uno.

### BUG-03 — BAJO: Design System — sidebar color inconsistente entre documentación y CSS

**Archivo:** `APB-DESIGN-SYSTEM/components/component-reference.md`, sección §9  
**Texto actual:** "Menú lateral izquierdo: Fondo `#2c3e50`"  
**CSS real (tokens/colors.css):** `--apb-sidebar-bg: #ffffff`  
**CHANGELOG v1.3.0:** "`--apb-sidebar-bg` corregido de `#2c3e50` a `#ffffff`"  
**Fix:** actualizar §9 con `var(--apb-sidebar-bg)` = `#ffffff`. Usar la variable CSS en lugar del valor hex directo para que futuras correcciones se propaguen automáticamente.

### BUG-04 — BAJO: adapter-claude-v1.0 referencia modelo desactualizado

**Archivo:** `adapters/claude/adapter-claude-v1.0.md`  
**Código:** `"model": "claude-sonnet-4-20250514"` — obsoleto.  
**Fix:** actualizar al model string actual. Considerar usar una referencia simbólica para evitar repetir este bug en cada release de modelo.

### BUG-05 — BAJO: SYSTEM.md §4.2 documenta 2 adapters en lugar de 4

**Archivo:** `SYSTEM.md`  
**Situación:** existen `adapters/m365/` y `adapters/rovo/` pero no aparecen en §4.2.  
**Fix:** añadir las dos filas a la tabla de adaptadores con estado `draft` y descripción.

### BUG-06 — MEDIO: telemetry.yml auto-commit a main es anti-patrón CI

**Archivo:** `.github/workflows/telemetry.yml`  
**Problema:** el workflow hace `git push` directamente a `main` para actualizar `telemetry/events.jsonl` con flags `sent`. Esto contradice el principio "ningún proceso automático modifica ramas protegidas sin PR" del propio workflow de validación. El `[skip ci]` mitiga el loop pero no el problema arquitectónico.  
**Riesgo de seguridad:** un bot con write access a `main` es vector de ataque si se comprometen sus credenciales.  
**Fix:** usar Azure Blob Storage como buffer de eventos pendientes, o una rama `telemetry-log` sin protección.

### BUG-07 — BAJO: CONTINUIDAD_PROYECTO.md desactualizado — 226 vs 341 componentes

**Archivo:** `discovery/CONTINUIDAD_PROYECTO.md`, sección §8  
**Problema:** el inventario documentado está 115 componentes por debajo del real. Las sesiones 15-23 no actualizaron esta bitácora.  
**Impacto:** cualquier Claude que lea CONTINUIDAD como arranque partirá con datos incorrectos del estado del framework.  
**Fix:** ejecutar `generate_catalog.py` (tras BUG-02), capturar el recuento y actualizar §8. Añadir nota de qué sesiones cerraron sin actualizar la bitácora.

### BUG-08 — INFORMATIVO: third-lum1104-knowledge-graph-v1.0 — licencia no verificada

**Situación:** documentado en CONTINUIDAD §4 como "bloqueante para uso en producción". El componente existe en catálogo con `source_license: "unverified"`.  
**Riesgo:** uso en producción sin licencia verificada puede constituir incumplimiento de derechos de autor.  
**Acción:** acceder a `https://github.com/Lum1104/Understand-Anything` directamente. Si no existe LICENSE file: marcar el componente como `rejected` en el catálogo con nota explicativa.


---

## 4. Análisis Multi-perspectiva de los Tres Repositorios

### 4.1 Perspectiva Técnica

**Fortalezas:**
- `validate_repo.py` con 18+ reglas y 19 tests de dogfooding es el componente técnico más maduro. CI bien diseñado.
- Frontmatter YAML como fuente de verdad parseable. Todos los scripts derivan del estado real de los archivos, sin catálogos hardcodeados.
- Esquema de IDs (`apb-{dominio}-{nombre}-v{major}.{minor}`) consistente y validable por regex.
- Cuatro adapters (claude, copilot, m365, rovo) cubren todos los runtimes relevantes del stack APB.
- `emit_telemetry.py` usa `DefaultAzureCredential` — patrón correcto para Managed Identity, sin credenciales en código.

**Debilidades técnicas:**
- BUG-02: `generate_catalog.py` crashea — el drift check de CI no funciona. El step de validación de catálogo lleva tiempo sin ejecutarse realmente.
- `invoke_agent.py` es un simulador declarado, no un ejecutor. No existe mecanismo de invocación real de agentes en el repositorio.
- `capabilities/` declarada en SYSTEM.md §3 no existe como carpeta. La jerarquía completa no está implementada.
- Sin gestión de versiones entre componentes: si una skill cambia su contrato de output, los agentes que la consumen no son notificados.
- Sin caching de outputs entre agentes del mismo workflow: cada re-ejecución calcula desde cero.

### 4.2 Perspectiva Funcional

**Cobertura por dominio IT:**

| Dominio | Skills APB | Agentes | Subagentes | Evaluación |
|---------|-----------|---------|-----------|-----------|
| Development | 27+ | 4 | 10+ | Bien cubierto |
| QA | 14+ | 3 | 6 | Bien cubierto |
| Architecture | 13+ | 4 | 5 | Bien cubierto |
| Operation | 13+ | 4 | 3 | Cubierto (telemetría incompleta) |
| Discovery | 12+ | 3 | 2 | Cubierto |
| Governance | 12+ | 3 | 1 | Cubierto (0 aprobaciones reales) |
| Platform | 12+ | 3 | 2 | Cubierto |
| PM | 8+ | 2 | 2 | Básico |
| Security | 8+ | 2 | 2 | Básico |
| Documentation | 7+ | 2 | 0 | Básico |
| Design | 2 | 1 | 0 | Mínimo |
| Orchestration | 1 | 1 | 0 | Incipiente |

**Gaps funcionales confirmados por revisión de código:**
- No existe agente de Change Management / ITIL (CAB, RFC, gestión de cambios formales).
- No existe agente de Data Governance / RGPD — obligación regulatoria, no nice-to-have.
- FinOps: 1 skill funcional para 19 providers Azure. Cobertura de costes insuficiente.
- No existe soporte para workflows de licitación/LCSP (pendiente de briefing de Débora según CONTINUIDAD).

### 4.3 Perspectiva QA

**Lo que funciona:**
- CI en cada PR: validate_repo.py --strict + generate_catalog.py --check (este último con el bug BUG-02).
- 19 tests unitarios del validador con fixtures sintéticos.
- Sección `## ⚠️ Comportamiento ante inputs incompletos` obligatoria en templates — buen contrato de input.

**Gaps de QA:**
- No existen tests end-to-end de ningún workflow.
- No existen tests de comportamiento de skills (golden tests que verifiquen que el output tiene la estructura esperada).
- `validate_repo.py` no verifica que los IDs en `consumed_by` correspondan a agentes que existen en `agents/` — solo verifica referencias en el cuerpo del Markdown.
- No hay regression testing cuando una skill usada por múltiples agentes cambia.
- No existe forma de ejecutar un agente en entorno de test real.

### 4.4 Perspectiva de Seguridad

**Controles correctamente implementados:**
- Azure Key Vault como único almacén de secretos. Patrón `{{secrets.apb-keyvault.nombre}}` consistente en todos los archivos revisados.
- `prov-akv-v1.0` scoped `read-only`. El framework solo consume referencias, nunca gestiona rotación.
- `DefaultAzureCredential` en telemetría — Managed Identity preferida sobre Service Principal.
- M365 adapter: proxy via APIM, las credenciales no se exponen al runtime de Copilot.

**Riesgos de seguridad identificados:**
- BUG-08: licencia Lum1104 no verificada — riesgo legal real si se usa en producción.
- 59 componentes de terceros sin SHA verificado: el framework no puede detectar cambios en repos de origen (supply chain risk).
- BUG-06: bot con write a `main` via telemetry.yml es vector de ataque potencial.
- Scope `write:confluence-content` en adapter-rovo Forge App es amplio — revisar mínimo necesario.
- **0 componentes aprobados**: los controles de autonomía y human_review declarados en frontmatter nunca han pasado auditoría formal. Son declaraciones no verificadas.

### 4.5 Perspectiva de Gobernanza

La arquitectura de gobernanza es excelente en diseño: 8 estados, matriz de aprobadores, regla two-eyes, ciclo de 6 meses. En práctica, es gobernanza no activada.

**Métricas actuales vs. objetivos de GOVERNANCE.md:**

| Métrica | Objetivo | Real hoy | Gap |
|---------|---------|----------|-----|
| Componentes en draft | < 30% | **100%** | -70 pp |
| Tiempo medio de aprobación | < 10 días | N/A (nunca iniciado) | ∞ |
| Excepciones activas | < 5% | N/A | — |
| Reuso de skills | > 50% | No medido | — |
| Incidentes atribuibles a IA | < 2% | No medido | — |

### 4.6 Perspectiva de Arquitectura

**Fortalezas:**
- Jerarquía de componentes conceptualmente sólida y runtime-agnóstica.
- Cuatro adapters permiten ejecutar el mismo agente en cualquier runtime del stack APB.
- Distinción correcta y bien documentada entre `prov-atlassian-v1.0` (CRUD) y `adapter-rovo-v1.0` (IA semántica sobre el mismo ecosistema).
- El patrón bidireccional de los adapters m365 y rovo (framework → plataforma y plataforma → framework) es arquitectónicamente maduro y diferencial.

**Debilidades:**
- `capabilities/` no existe como carpeta — la jerarquía completa declarada en SYSTEM.md no está implementada.
- No existe motor de orquestación real. Los workflows son documentación de intención, no código ejecutable.
- APB-DOMAIN-CATALOG vacío bloquea toda la arquitectura DDD: los agentes DDD existen pero no tienen catálogo del que leer ni al que escribir.
- Sin gestión de compatibilidad entre versiones: un cambio de contrato en una skill no notifica a los agentes consumidores.
- Providers de acción sin circuit breaker ni retry policy formal (pendiente SCHEMA.md Acción 8).

### 4.7 Perspectiva de Performance

- No existen SLOs definidos para ningún agente o workflow.
- Sin telemetría activa, no hay datos de rendimiento real de ningún componente.
- Workflows complejos (`wf-sdd-full` con ≥5 agentes) sin estimación de tiempo ni puntos de timeout.
- Extended Thinking habilitado por defecto en adapter-claude para arquitectura y threat modeling — correcto funcionalmente pero sin control de presupuesto de tokens por workflow.
- Sin caching de outputs — re-ejecuciones tienen el coste completo de tokens.

### 4.8 Perspectiva de Mantenibilidad

**Alta mantenibilidad:**
- Frontmatter YAML como fuente de verdad parseable — la mejor decisión de mantenibilidad del framework.
- Scripts de generación automática de catálogos eliminan la deuda de sincronización manual.
- Templates con checklist integrado reducen errores en la creación de nuevos componentes.

**Baja mantenibilidad:**
- 341 componentes en draft: sin ciclo de revisión activo, la deuda de gobernanza crece linealmente con cada componente nuevo.
- BUG-02 enmascaraba drift de INDEX.md en CI — se desconoce desde cuándo y cuánto drift hay acumulado.
- CONTINUIDAD_PROYECTO.md desactualizada en 115 componentes: fuente de confusión para futuras sesiones.
- Sin changelog automatizado por componente: los cambios entre versiones dependen de las secciones manuales "Historial de Cambios".

### 4.9 Perspectiva de Escalabilidad

- La infraestructura de validación y generación escala bien: todo basado en parseo de archivos, sin catálogos en memoria.
- **No escala en aprobaciones**: 341 componentes en draft requieren cientos de horas-persona si se abordan sin priorización estricta.
- **No escala en dominios**: APB-DOMAIN-CATALOG vacío genera outputs DDD incompatibles entre proyectos y equipos.
- El adapter M365 via APIM es una decisión excelente de escalabilidad para consumo corporativo masivo sin exponer el modelo directamente.

### 4.10 Perspectiva DX/UX (Developer Experience)

**APB-IA-FRAMEWORK:**
- `invoke_agent.py --list` es una buena primera experiencia de descubrimiento, aunque al ser simulador no ejecuta nada real.
- El proceso de contribución (discovery obligatorio, checklist de PR) es riguroso pero puede intimidar a nuevos contribuidores sin experiencia en el framework.
- No existe una guía de "primer agente" o "primera skill" para onboarding rápido.

**APB-DESIGN-SYSTEM:**
- Stack DX sólida: tokens CSS + style guide + visual reference + component reference + oxlintrc.
- BUG-03 crea confusión directa: el desarrollador que lee `component-reference.md` ve `#2c3e50`; el que inspecciona el CSS ve `#ffffff`. Contradicción no resuelta.
- La discrepancia tipográfica Cabin/Helvetica es la principal fuente de inseguridad para desarrolladores frontend — sin saber qué fuente usar, no pueden escribir CSS consistente.

**APB-DOMAIN-CATALOG:**
- `new-domain.sh` es excelente DX — interactivo, guiado, con sustituciones automáticas.
- Sin dominios aprobados, cualquier agente DDD produce outputs huérfanos. La DX de los agentes DDD es actualmente nula en la práctica.


---

## 5. Orden de Ejecución Óptimo con Dependencias

### Árbol de dependencias

```
[BUG-02] Fix generate_catalog.py regex
    ├── Habilita: CI drift check real en cada PR
    └── [BUG-07] Actualizar CONTINUIDAD con recuento correcto

[BUG-01] Fix WORKFLOW.md template
    └── Habilita: nuevos workflows válidos en CI desde el primer commit

[Acción 8] Actualizar SCHEMA.md (human_validator, retry_strategy)
    └── Prerrequisito blando de Acción 4
        (mejor definir los campos antes de aprobar los primeros componentes)

[Acción 4] Primer ciclo de aprobación (5 componentes)
    ├── No tiene prerequisito técnico — puede iniciarse ya
    ├── Habilita: métricas de gobernanza reales
    └── Habilita: confianza en producción

[Acción 7] Configurar Azure Monitor
    ├── Requiere: GitHub Secrets configurados por Platform
    └── Habilita: todas las métricas de uso y gobernanza

[Acción 5] APB-DOMAIN-CATALOG — primer contenido
    ├── BLOQUEADA: requiere lista de sistemas/APIs de Débora
    └── Habilita: todos los agentes DDD

[Acción 6] Runbooks sdd-full y code-review
    └── Independiente — puede ejecutarse en paralelo con lo anterior

[Acción 9] Catálogo skills Level 2
    └── Depende de: Acción 4 (al menos parcialmente ejecutada)

[Acción 10] Decisión tipografía Design System
    └── Requiere: decisión ejecutiva de Arquitectura APB (no técnica)

[BUG-06] Rediseñar telemetry.yml anti-patrón
    └── Independiente, prioridad media
```

### Orden recomendado

**Esta semana — quick wins, < 4h total, cualquier desarrollador:**

| # | Tarea | Esfuerzo |
|---|-------|---------|
| 1 | BUG-02: Fix regex `generate_catalog.py` | 30 min |
| 2 | BUG-01: Fix `WORKFLOW.md` template frontmatter | 20 min |
| 3 | BUG-03: Fix sidebar color `component-reference.md` | 5 min |
| 4 | BUG-04: Fix modelo en `adapter-claude-v1.0` | 5 min |
| 5 | BUG-05: Fix `SYSTEM.md §4.2` — añadir m365 y rovo | 10 min |
| 6 | Acción 2: Documentar deprecación `apb-ai-skills` en README | 30 min |

**Este mes — alta prioridad:**

| # | Tarea | Esfuerzo | Responsable |
|---|-------|---------|------------|
| 7 | Acción 8: Campos SCHEMA.md (`human_validator`, `retry_strategy`) | 2h | Arquitectura APB |
| 8 | Acción 4: Primer ciclo de aprobación (5 componentes) | 3–5 días | Arquitectura + Ciber |
| 9 | Acción 7: Configurar Azure Monitor secrets | 1 día | Platform |
| 10 | Acción 6: Runbooks `wf-sdd-full` y `wf-code-review` | 2–3 días | Arquitectura + Dev |
| 11 | Acción 5: APB-DOMAIN-CATALOG — primer contenido | 3–5 días | Arquitectura (tras input de Débora) |

**Este trimestre:**

| # | Tarea | Esfuerzo | Responsable |
|---|-------|---------|------------|
| 12 | Acción 9: Catálogo skills autorizadas para Level 2 | 3–4 días | Arquitectura + Ciber |
| 13 | Acción 10: Decisión y resolución tipografía | 1h decisión + 2h impl. | Arquitectura APB |
| 14 | BUG-07: Actualizar CONTINUIDAD recuento real | 1h | Dev |
| 15 | BUG-06: Rediseñar telemetry.yml — eliminar auto-commit | 1 día | Dev + Platform |
| 16 | BUG-08: Verificar licencia `third-lum1104-knowledge-graph-v1.0` | 30 min | Arquitectura APB |


---

## 6. Plan de Acción Detallado — Todas las Tareas Justificadas

### BLOQUE A — Correcciones urgentes (esta semana, < 4h total)

#### A-1. Fix generate_catalog.py — regex possessive quantifier (BUG-02)
**Responsable:** Dev  
**Esfuerzo:** 30 min  
**Qué hacer exactamente:** en `scripts/generate_catalog.py`, función `update_index_md` (líneas ~240-252), localizar los 8 patrones `re.compile(r"(...\s*+...)")` y eliminar el `+` posesivo. Cambiar `\s*+` por `\s*` en cada uno. Verificar con `python3 scripts/generate_catalog.py` que no lanza traceback.  
**Criterio de éxito:** el step "Verificar sincronización de catálogo" en CI pasa en verde y el script termina sin excepción.  
**Por qué es urgente:** el CI lleva tiempo sin validar el drift de INDEX.md. Cada PR que ha pasado CI podía tener documentación desincronizada sin que nadie lo detectara.

#### A-2. Fix WORKFLOW.md template — frontmatter YAML (BUG-01)
**Responsable:** Dev  
**Esfuerzo:** 20 min  
**Qué hacer:** en `context/apb/templates/WORKFLOW.md`, reemplazar el encabezado con blockquotes (las líneas `> **ID:**`, `> **Versión:**`, etc.) por un bloque YAML frontmatter completo con los campos obligatorios según SCHEMA.md §3.4:

```yaml
---
id: "apb-wf-{nombre}-v{major}.{minor}"
name: "{Nombre legible del workflow}"
description: "{1–3 frases: qué hace el workflow y cuándo usarlo.}"
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "{dominio}"
autonomy_level: 1
agents:
  - "apb-agent-{nombre}-v1.0"
human_checkpoints:
  - "{Punto de control humano 1}"
created_date: "YYYY-MM-DD"
review_date: "YYYY-MM-DD"
---
```

El cuerpo del template (secciones de Mermaid, fases, fallos, etc.) se mantiene igual.  
**Criterio de éxito:** crear un workflow de prueba copiando el template, ejecutar `validate_repo.py` sobre él, sin errores de frontmatter.

#### A-3. Fix component-reference.md §9 — sidebar color (BUG-03)
**Responsable:** Dev Design System  
**Esfuerzo:** 5 min  
**Qué hacer:** en `APB-DESIGN-SYSTEM/components/component-reference.md`, sección §9 "Estructura de pantalla APB", cambiar:  
- Antes: "Menú lateral izquierdo: Fondo `#2c3e50`"  
- Después: "Menú lateral izquierdo: Fondo `var(--apb-sidebar-bg)` = `#ffffff` (corregido en v1.3.0 — ver CHANGELOG)"  

**Por qué usar la variable CSS en lugar del hex:** si el color cambia de nuevo en el futuro, el CSS será siempre la fuente de verdad y la documentación solo necesita apuntar a la variable.

#### A-4. Fix adapter-claude-v1.0 — modelo desactualizado (BUG-04)
**Responsable:** Dev  
**Esfuerzo:** 5 min  
**Qué hacer:** en `adapters/claude/adapter-claude-v1.0.md`, actualizar el model string en la sección de configuración al modelo actual. Añadir una nota en el adapter: "Este campo debe actualizarse con cada nueva versión mayor del modelo. Verificar en la documentación de Anthropic el model string correcto antes de activar."

#### A-5. Fix SYSTEM.md §4.2 — cuatro adapters (BUG-05)
**Responsable:** Arquitectura APB  
**Esfuerzo:** 10 min  
**Qué hacer:** añadir dos filas a la tabla de §4.2:

| Adaptador | Estado | Descripción |
|-----------|--------|-------------|
| `adapters/m365/` | draft | Integración bidireccional con Microsoft 365 Copilot. Pendiente activación en tenant APB. |
| `adapters/rovo/` | draft | Integración bidireccional con Atlassian Rovo. Pendiente Forge App — objetivo julio 2026. |

#### A-6. Documentar deprecación apb-ai-skills (Acción 2)
**Responsable:** Dev + Arquitectura APB  
**Esfuerzo:** 30 min  
**Qué hacer:**  
1. En `README.md` del framework, añadir una sección "Repositorios relacionados" o un aviso en el README que documente: "El repositorio `apb-ai-skills` ha sido deprecado. Todo desarrollo futuro de skills y agentes de QA vive exclusivamente en este repositorio (APB-IA-FRAMEWORK)."  
2. Actualizar `discovery/CONTINUIDAD_PROYECTO.md` §13.3 con la formalización de esta decisión y la fecha.  
**Criterio de éxito:** un desarrollador que llegue al repo por primera vez entiende la situación sin necesidad de leer CONTINUIDAD.

---

### BLOQUE B — Gobernanza urgente (este mes)

#### B-1. Actualizar SCHEMA.md antes de iniciar aprobaciones (Acción 8)
**Responsable:** Arquitectura APB  
**Esfuerzo:** 2h  
**Por qué antes de las aprobaciones:** los primeros componentes que pasen a `approved` deben poder registrar `human_validator` de forma machine-readable. Mejor definir el campo ahora que retroalimentar 30 componentes después.

**Campos a añadir a SCHEMA.md:**

*Sección §2 — Campos comunes (añadir como opcionales):*
- `human_validator`: string. Formato: `"Nombre Apellido (Rol)"`. Obligatorio en estado `approved`, opcional en otros estados. Permite consultas en el catálogo de "quién ha validado qué".

*Sección §3.5 Provider y §3.1 Skill (añadir como opcional):*
- `retry_strategy`: objeto con tres subatributos:
  - `max_retries`: entero (0–5)
  - `backoff_seconds`: entero
  - `on_failure`: enum — `halt` (detener el workflow), `skip` (saltar este paso y continuar), `escalate` (notificar al humano y esperar)

Necesario para providers de acción sujetos a rate limits o indisponibilidad (Atlassian, Azure Monitor, SharePoint). Sin este campo, un fallo de provider detiene silenciosamente el workflow.

#### B-2. Primer ciclo de aprobación formal — 5 componentes (Acción 4)
**Responsable:** Arquitectura APB + Ciberseguridad (two-eyes obligatorio)  
**Esfuerzo:** 3–5 días distribuidos (~90 min por componente)  
**Por qué es la acción más crítica del plan:** el framework lleva en construcción múltiples sesiones y tiene 341 componentes, todos en `draft`. Sin ningún componente aprobado, no existe base formal para decir que ningún agente está listo para uso en proyectos reales. Los controles de seguridad y autonomía declarados en los frontmatter son promesas no auditadas.

**Proceso por componente:**

| Paso | Tiempo | Responsable |
|------|--------|------------|
| 1. Verificar frontmatter completo y correcto (todos los campos de SCHEMA.md presentes) | 10 min | Dev |
| 2. Verificar secciones obligatorias del cuerpo: Marcado IA, Comportamiento ante inputs incompletos, Manejo de Fallos (workflows) | 20 min | Dev |
| 3. Revisión funcional: ¿el prompt/instrucciones hacen lo que declara el `description`? | 30 min | Arquitectura APB |
| 4. Revisión two-eyes: segundo aprobador de ámbito diferente (Ciberseguridad para componentes de seguridad, QA para skills de testing, etc.) | 30 min | Ciberseguridad / QA |
| 5. Actualizar: `status: approved`, `human_validator: "Nombre (Rol)"`, `review_date` | 5 min | Dev |
| 6. PR + regenerar catálogo | 15 min | Dev |

**Orden de los 5 candidatos (por impacto real y uso actual):**

1. `apb-gov-ai-risk-gate-v1.0` — skill transversal que otros workflows necesitan aprobada antes de usarla formalmente
2. `apb-dev-code-review-v1.0` — skill más usada en el día a día de revisiones de código
3. `apb-agent-spec-engineer-v1.0` — agente central del flujo SDD, el más invocado
4. `apb-agent-technical-architect-v1.0` — necesaria para diseños de arquitectura con respaldo formal
5. `apb-wf-sdd-full-v1.0` — workflow más completo; aprobarlo demuestra que el proceso funciona extremo a extremo

**Criterio de éxito:** ≥5 componentes en estado `approved`. La métrica "% en draft" baja del 100%.

#### B-3. Configurar telemetría Azure Monitor (Acción 7)
**Responsable:** Platform/Operaciones  
**Esfuerzo:** 1 día  
**Qué hacer paso a paso:**

1. Crear o reutilizar un **Data Collection Endpoint (DCE)** en Azure Monitor del tenant APB.
2. Crear un **Data Collection Rule (DCR)** con la tabla `APBFrameworkTelemetry_CL` y el schema esperado por `emit_telemetry.py` (campos mínimos: `TimeGenerated`, `invocation_id`, `component_id`, `outcome`).
3. Configurar los **GitHub Secrets** en el repositorio APB-IA-FRAMEWORK:
   - `AZURE_MONITOR_DCE_ENDPOINT`
   - `AZURE_MONITOR_DCR_ID`
   - `AZURE_MONITOR_STREAM_NAME` (si difiere del default `Custom-APBFrameworkTelemetry_CL`)
   - `AZURE_TENANT_ID`, `AZURE_MONITOR_CLIENT_ID`, `AZURE_MONITOR_CLIENT_SECRET` (o Managed Identity si el runner lo soporta)
4. Ejecutar test manual: `python3 scripts/emit_telemetry.py --event '{"component_id":"test-connection","outcome":"success","agent":"manual-test"}'`
5. Verificar en Azure Monitor Log Analytics que el evento aparece en `APBFrameworkTelemetry_CL`.

**Criterio de éxito:** evento de prueba visible en Log Analytics en < 5 minutos tras la emisión.

#### B-4. Runbooks para wf-sdd-full y wf-code-review (Acción 6)
**Responsable:** Arquitectura APB + Dev  
**Esfuerzo:** 2–3 días  
**Dónde guardarlos:** `docs/runbook-wf-sdd-full.md` y `docs/runbook-wf-code-review.md`

**Estructura obligatoria de cada runbook:**

```markdown
## Prerrequisitos
- Permisos necesarios (Jira, GitHub, repos de destino)
- Herramientas instaladas (Claude Code / Copilot, MCP providers activos)
- Artefactos de entrada requeridos

## Ejecución normal — paso a paso
| Fase | Agente | Input | Output | Punto de control humano |
|------|--------|-------|--------|------------------------|

## Gestión de errores por fase
| Fase | Fallo posible | ¿Bloqueante? | Acción | Decisor |
|------|--------------|-------------|--------|--------|

## Rollback
- Cómo revertir si el output de alguna fase no es válido
- Qué artefactos eliminar / qué tickets cerrar

## Métricas de éxito
- Cómo saber que el workflow se ejecutó correctamente
- Qué registrar en telemetría y en Jira
```

**Criterio de éxito:** un miembro del equipo sin experiencia previa en el workflow puede ejecutarlo de principio a fin usando solo el runbook, sin preguntar.

#### B-5. APB-DOMAIN-CATALOG — primer contenido real (Acción 5)
**Responsable:** Arquitectura APB  
**Desbloqueador crítico:** Débora debe proveer la lista de sistemas/APIs corporativas de APB. Sin este input no puede iniciarse.  
**Esfuerzo (una vez desbloqueado):** 3–5 días

**Por qué es crítico:** sin dominios aprobados, los 33 subagentes DDD y los agentes de decomposición de monolitos producen outputs que no se pueden integrar entre proyectos. Cada proyecto genera su propio modelo DDD incompatible con el de los demás.

**Qué hacer una vez recibida la lista:**

1. Identificar 3–5 dominios core de negocio (ejemplos probables: Gestión de Atraques, Tráfico de Mercancías, Gestión de Concesiones, Administración Portuaria, Seguridad y Accesos).
2. Para cada dominio, ejecutar `scaffolding/scripts/new-domain.sh` interactivamente.
3. Completar el YAML de bounded contexts con entidades, eventos de dominio y lenguaje ubicuo real de APB.
4. Someter cada dominio al proceso de GOVERNANCE.md del APB-DOMAIN-CATALOG (estado `proposed` → revisión de Arquitectura → `approved`).

**Criterio de éxito:** ≥3 dominios en estado `approved` en APB-DOMAIN-CATALOG. Los agentes DDD pueden leer el catálogo y producir outputs coherentes entre proyectos.

---

### BLOQUE C — Este trimestre

#### C-1. Catálogo de skills autorizadas para Level 2 (Acción 9)
**Responsable:** Arquitectura APB + Ciberseguridad  
**Esfuerzo:** 3–4 días  
**Entregable:** documento `docs/autonomy-level2-registry.md` con la lista formal de skills autorizadas para operar sin aprobación previa.

**Criterios de elegibilidad para Level 2** (la skill solo opera sobre sus outputs sin efectos externos no revertibles):
- Documentación de código existente (solo lectura del código, escribe documentación)
- Generación de tests unitarios en rama de feature (sin merge sin revisión humana)
- Análisis de calidad / deuda técnica (solo lectura, produce informe para humano)
- Generación de specs en estado draft (no publicadas, esperan aprobación explícita)
- Análisis de riesgos sin propuesta de acción automática

**Criterios de exclusión de Level 2:**
- Cualquier skill que modifique código en rama principal
- Cualquier skill que cree tickets Jira sin punto de control humano previo
- Cualquier skill que modifique configuraciones de infraestructura
- Skills de seguridad (siempre Level 1 mínimo)

**Criterio de éxito:** documento aprobado con al menos 10 skills listadas, responsable de la autorización, y fecha.

#### C-2. Decisión y resolución tipografía Design System (Acción 10)
**Responsable:** Arquitectura APB (decisión ejecutiva, no técnica)  
**Esfuerzo:** 1h de decisión + 2h de implementación técnica  

**Opciones documentadas en style-guide.md §2.1:**

| Opción | Descripción | Cambios técnicos |
|--------|-------------|-----------------|
| **A (recomendada)** | Cabin como única fuente oficial — ya en los tokens CSS | Solo actualizar `style-guide.md` y aclarar en `_adherence.oxlintrc.json`. Sin cambios en CSS. |
| B | Helvetica Neue principal + Cabin fallback | Actualizar tokens CSS, style-guide y oxlintrc. |
| C | Cabin para componentes APB custom + Helvetica Neue en DevExtreme | Documentar cuándo usa cada fuente — riesgo de inconsistencia. No recomendada. |

La Opción A es la más pragmática: Cabin ya está implementada en CSS, no requiere cambios de código, solo cierra la ambigüedad documental. Hasta que Arquitectura APB tome esta decisión, ningún desarrollador frontend puede escribir CSS de fuentes con seguridad.

#### C-3. Rediseñar telemetry.yml — eliminar auto-commit a main (BUG-06)
**Responsable:** Dev + Platform  
**Esfuerzo:** 1 día  
**Solución recomendada:** eliminar el paso `git commit / git push` del workflow. En su lugar:
- Opción A (simple): usar **Azure Blob Storage** como buffer de eventos pendientes en lugar de `telemetry/events.jsonl` en el repo. El GitHub Action lee y envía desde el blob sin tocar el repositorio.
- Opción B (mínima): crear una rama `telemetry-log` sin protección donde el bot puede hacer push. La rama no activa el workflow de validación y no está sujeta a las reglas de ramas protegidas.

La Opción A es la arquitectónicamente correcta: desacopla el estado de telemetría del repo de código.


---

## 7. Evoluciones Propuestas por Perspectiva

### 7.1 Evoluciones Técnicas

**E-T1: Motor de orquestación real** (prioridad alta)  
Los workflows están definidos en Markdown pero no se ejecutan automáticamente. Hoy, ejecutar un workflow requiere que un humano invoque manualmente cada agente en secuencia. Opciones por complejidad ascendente:

- **Opción simple** (1–2 días): GitHub Action parametrizable que lee el frontmatter YAML de un workflow (`agents`, `human_checkpoints`), llama a cada agente en secuencia usando `inputs` de GitHub Actions, y pausa en los checkpoints usando GitHub Environments con aprobación manual. No requiere código nuevo de orquestación.
- **Opción media** (1 semana): `orchestrator.py` que procesa el YAML del workflow, invoca agentes en secuencia, registra telemetría en cada paso, y escribe el estado de ejecución en un archivo de log.
- **Opción avanzada** (1 mes+): integrar `microsoft/semantic-kernel` como motor de orquestación, aprovechando su soporte nativo para Claude y .NET (ver §10.1).

**E-T2: Golden tests para skills críticas** (prioridad media)  
Para las 5 skills candidatas a aprobación, crear tests de comportamiento esperado: dado un input estándar → verificar que el output contiene las secciones obligatorias y los campos requeridos por el template. Implementable sin ejecutar el modelo (análisis estático del template de output). Añadir al suite de tests existente en `tests/`.

**E-T3: Notificación de cambios breaking en contratos de skills** (prioridad media)  
Cuando una skill actualiza su versión mayor (e.g., de v1.0 a v2.0), `validate_repo.py` debería generar un WARNING para todos los agentes que tienen esa skill en `skills:`. Implementable añadiendo una verificación de compatibilidad de versiones en el validador: si el `id` de una skill referenciada en un agente contiene `v1.0` pero el archivo real de la skill dice `v2.0`, emitir advertencia de posible incompatibilidad.

**E-T4: Capa formal de Capabilities** (prioridad baja)  
Crear la carpeta `capabilities/` declarada en SYSTEM.md §3 con descriptores de las capacidades de negocio principales (Generar Especificaciones, Revisar Código, Diseñar Arquitectura, Gestionar Incidentes, etc.). Completa la jerarquía conceptual del framework y facilita la alineación con el negocio cuando se presentan los resultados a dirección.

**E-T5: Caching de outputs de agentes dentro de un workflow** (prioridad baja)  
Para workflows con múltiples agentes que procesan el mismo artefacto base, implementar caching por hash de input. Reduce el coste de tokens en re-ejecuciones parciales (cuando un agente intermedio falla y hay que reintentar solo desde ese punto).

---

### 7.2 Evoluciones Funcionales

**E-F1: Agente de Change Management / ITIL** (prioridad alta)  
APB opera con ITIL (P1–P4, L1/L2/L3, CAB, RFC, Problem Management). Ningún agente actual gestiona el proceso de cambio formal. Un agente `apb-agent-change-manager-v1.0` cubriría:
- Evaluación de impacto de RFC (quién se ve afectado, qué sistemas, qué riesgo)
- Preparación del informe para el CAB (formato estandarizado)
- Tracking de cambios de emergencia (ECAB, aprobación acelerada)
- Generación de tickets Jira de seguimiento post-cambio
- Integración con `prov-atlassian-v1.0` para creación automatizada de RFCs

**E-F2: Agente de Data Governance / RGPD** (prioridad alta — obligación regulatoria)  
El framework puede procesar datos potencialmente personales (expedientes, datos de empleados, datos de empresas concesionarias). RGPD obliga a APB, como organismo público, a mantener:
- Registro de actividades de tratamiento (RAT)
- Bases jurídicas documentadas para cada tratamiento
- Plazos de conservación definidos y aplicados
- Análisis de impacto relativo a protección de datos (DPIA) para tratamientos de alto riesgo

Un agente `apb-agent-data-governance-v1.0` que audite el estado de estos requisitos y genere el RAT actualizado es una necesidad regulatoria, no una mejora opcional.

**E-F3: Enriquecimiento FinOps Azure** (prioridad media)  
El framework declara 19 providers Azure. No existe visibilidad de costes de IA (tokens, llamadas a Azure Monitor, Log Analytics ingestion). Un agente o skill de FinOps que analice Azure Cost Management y proponga optimizaciones evitaría sorpresas en la factura y permitiría justificar el ROI del framework ante dirección con datos reales.

**E-F4: Soporte para workflows de licitación/LCSP** (prioridad media)  
APB es organismo público sujeto a LCSP. Los procesos de contratación (preparación de pliegos, evaluación de ofertas, gestión de contratos de mantenimiento) tienen suficiente complejidad y repetición para justificar agentes especializados. Pendiente de briefing específico de Débora sobre qué partes del proceso son más costosas en tiempo.

**E-F5: Agente de Onboarding de Proyectos Legacy** (prioridad media)  
Identificado en CONTINUIDAD como pendiente: workflow de ciclo completo legacy → SDD. Un agente `apb-agent-legacy-onboarding-v1.0` que automatice el análisis inicial de un proyecto existente (estructura de código, deuda técnica, APIs no documentadas) y genere el primer borrador del `system-spec.md` reduciría significativamente el tiempo de arranque de proyectos de modernización.

---

### 7.3 Evoluciones de Seguridad

**E-S1: SBOM automatizado para componentes de terceros** (prioridad alta)  
Los 51 skills de terceros + 7 wrappers deberían generar automáticamente un Software Bill of Materials con licencias, versiones verificadas y estado de cada componente. Implementable ampliando `generate_catalog.py` para añadir una sección de SBOM en `CATALOG.md` con los campos `source_repo`, `source_license`, `source_commit` y `verified_date` de todos los componentes de terceros.

**E-S2: Supply chain verification como step de CI** (prioridad media)  
Para skills con `source_commit: "unverified"`, añadir un step opcional en CI que intente verificar el SHA actual del repo de origen (`git ls-remote`). Comportamiento:
- Si el repo no es accesible: mantener `unverified`, no bloquear.
- Si el repo es accesible y el contenido coincide con el SHA registrado: marcar como verificado automáticamente.
- Si el contenido del repo de origen ha cambiado desde la última revisión: generar un WARNING específico de "contenido modificado en origen desde la última revisión".

**E-S3: Análisis periódico de dependencias de terceros** (prioridad media)  
Añadir al CI (o como GitHub Action semanal) un step de `pip-audit` o `safety check` para los wrappers de repos externos que usen dependencias Python. Integrar los hallazgos como input al agente `apb-agent-tech-debt-v1.0`.

---

### 7.4 Evoluciones de Gobernanza

**E-G1: Dashboard de métricas de gobernanza en tiempo real** (prioridad alta — dependiente de telemetría)  
Una vez configurado Azure Monitor, construir un dashboard en Log Analytics o Power BI que muestre:
- % de componentes en cada estado (draft / candidate / approved / deprecated)
- Tiempo medio de aprobación por tipo de componente
- Skills más invocadas por workflows
- Agentes con más incidencias o fallos registrados
- Evolución del reuso de skills (métrica de GOVERNANCE.md: objetivo >50%)

Las métricas objetivo están declaradas en GOVERNANCE.md — lo que falta es el tablero que las haga visibles.

**E-G2: Ciclo de revisión semestral automatizado** (prioridad media)  
GOVERNANCE.md §6 declara un ciclo de revisión de 6 meses para componentes aprobados, pero no existe ningún mecanismo que lo enforce. Implementar una GitHub Action mensual que:
1. Lee todos los componentes en estado `approved`.
2. Calcula los días desde `review_date`.
3. Si han pasado ≥180 días: crea un issue en GitHub asignado al `owner` del componente con el título "Revisión semestral pendiente: {id}".

**E-G3: Proceso formal de deprecación** (prioridad media)  
Actualmente la deprecación de `apb-ai-skills` es una decisión verbal en CONTINUIDAD. El framework necesita un proceso formal documentado en GOVERNANCE.md que cubra:
- Quién puede proponer la deprecación de un componente (cualquier miembro del equipo)
- Quién debe aprobarla (el `owner` + un aprobador del ámbito correspondiente)
- Período de aviso antes de mover a `deprecated` (mínimo 30 días para skills con consumidores activos)
- Qué hacer con los consumidores del componente deprecado (actualizar sus `skills:` o `depends_on:`)
- Cuándo pasa de `deprecated` a `retired` (propuesta: 90 días sin incidencias tras la deprecación)

---

### 7.5 Evoluciones de DX (Developer Experience)

**E-DX1: Guía de "Primera skill" y "Primer agente"** (prioridad media)  
No existe una guía de onboarding rápido para un desarrollador nuevo en el framework. Propuesta: `docs/getting-started-contributing.md` con un walkthrough completo de:
1. Leer SYSTEM.md y GOVERNANCE.md (30 min)
2. Ejecutar `python3 scripts/invoke_agent.py --list` para explorar lo que existe
3. Crear una skill sencilla paso a paso usando el template SKILL_APB.md
4. Ejecutar el validador y ver que pasa
5. Abrir un PR de prueba y ver el CI en acción

**E-DX2: Storybook para APB-DESIGN-SYSTEM** (prioridad baja)  
Reemplazar o complementar `visual-reference.html` con Storybook — el estándar de la industria para catálogos de componentes UI. Cada componente JSX del Design System tendría ejemplos interactivos, documentación de props y tests de accesibilidad automáticos (addon a11y). Elimina la necesidad de mantener el HTML estático manualmente.


---

## 8. Tareas Humanas Pendientes por Equipo

### Equipo de Arquitectura APB

| Tarea | Urgencia | Tiempo est. | Desbloqueador de |
|-------|---------|------------|-----------------|
| **Proveer lista de sistemas/APIs APB para DOMAIN-CATALOG** | **Crítica** | 2–3h inventario | Todos los agentes DDD, decomposición de monolitos |
| **Iniciar ciclo de aprobación de 5 componentes candidatos** | **Crítica** | 3–5 días | Gobernanza real, confianza en producción |
| Decidir tipografía Design System (Cabin vs. Helvetica Neue) | Alta | 1h decisión | Oxlint enforcement de fuentes sin excepciones |
| Revisar y aprobar campos adicionales SCHEMA.md (human_validator, retry_strategy) | Alta | 1h | SCHEMA.md v1.1 — antes de iniciar aprobaciones |
| Actualizar SYSTEM.md §4.2 con los cuatro adapters reales (BUG-05) | Media | 10 min | Documentación coherente con la realidad |
| Verificar licencia `third-lum1104-knowledge-graph-v1.0` | Alta | 30 min | Uso seguro de la skill, sin riesgo legal |
| Decidir si `capabilities/` se implementa como carpeta o se elimina de SYSTEM.md | Media | 30 min | Arquitectura documentada coherente |
| Formalizar proceso de deprecación en GOVERNANCE.md (E-G3) | Media | 2h | Ciclo de vida completo de componentes |
| Definir criterios y listado de skills autorizadas para Level 2 (Acción 9) | Media | 3–4 días | Autonomía supervisada en producción |

### Equipo de Platform/Operaciones

| Tarea | Urgencia | Tiempo est. | Desbloqueador de |
|-------|---------|------------|-----------------|
| **Configurar GitHub Secrets para telemetría Azure Monitor** | Alta | 4–8h | Métricas de uso y gobernanza en producción |
| **Crear DCR y DCE en Azure Monitor para APBFrameworkTelemetry_CL** | Alta | 2–4h | Telemetría |
| Aprobar y publicar M365 Copilot plugin en el tenant APB (5 pasos documentados en adapter-m365-v1.0) | Media | 1 día | Acceso al framework desde Teams, Word, SharePoint |
| Desarrollar y publicar Forge App de Rovo Agents (julio 2026, 6 pasos en adapter-rovo-v1.0) | Media | 3–5 días | Integración nativa con Jira/Confluence |
| Desactivar GitHub Actions de `apb-ai-skills` (`sync-skills.yml`, `validate-skills.yml`) | Media | 30 min | Limpieza de CI en repo deprecado |
| Rediseñar telemetry.yml — eliminar auto-commit a main (BUG-06) | Media | 1 día | Arquitectura CI correcta y segura |
| Implementar recordatorio semestral de revisión de componentes aprobados (E-G2) | Baja | 1 día | Gobernanza sostenible a largo plazo |

### Equipo de Desarrollo

| Tarea | Urgencia | Tiempo est. | Desbloqueador de |
|-------|---------|------------|-----------------|
| **Fix `generate_catalog.py` regex bug (BUG-02)** | **Urgente** | 30 min | CI drift check funcional |
| **Fix `WORKFLOW.md` template frontmatter (BUG-01)** | **Urgente** | 20 min | Nuevos workflows válidos desde el primer commit |
| Fix `component-reference.md §9` sidebar color (BUG-03) | Alta | 5 min | DX coherente del Design System |
| Fix `adapter-claude-v1.0` modelo desactualizado (BUG-04) | Media | 5 min | Documentación correcta del adapter |
| Documentar deprecación `apb-ai-skills` en README (Acción 2) | Alta | 30 min | Claridad para nuevos desarrolladores |
| Crear runbooks para `wf-sdd-full` y `wf-code-review` (Acción 6) | Alta | 2–3 días | Operación real reproducible |
| Actualizar CONTINUIDAD_PROYECTO.md con recuento real (BUG-07) | Media | 1h | Fuente de verdad para futuras sesiones |
| Crear guía de "Primera skill / Primer agente" (E-DX1) | Media | 1–2 días | Onboarding de nuevos contribuidores |
| Implementar motor de orquestación simple vía GitHub Action (E-T1 — opción simple) | Alta | 1–2 días | Ejecución real de workflows |

### Equipo de Seguridad / Ciberseguridad

| Tarea | Urgencia | Tiempo est. | Desbloqueador de |
|-------|---------|------------|-----------------|
| **Co-aprobar los 5 componentes candidatos (rol two-eyes obligatorio)** | **Crítica** | 2 días | Primer ciclo de aprobación |
| Definir scopes OAuth mínimos necesarios para adapter-rovo Forge App | Alta | 2h | Reducción de superficie de ataque |
| Auditar que el M365 plugin no expone credenciales AKV al runtime de Copilot | Alta | 1h | Seguridad antes de activación en tenant |
| Definir y documentar proceso de gestión de supply chain para skills de terceros (E-S1, E-S2) | Media | 1 día | Protección contra supply chain attacks |
| Verificar la licencia de `third-lum1104-knowledge-graph-v1.0` (BUG-08) | Alta | 30 min | Uso legalmente seguro |

### Decisiones exclusivas de Débora (input bloqueante)

Estas tareas no pueden iniciarse sin una decisión o input explícito:

| Decisión/Input | Bloquea | Cuándo se necesita |
|----------------|---------|-------------------|
| **Lista de sistemas/APIs corporativas de APB** | APB-DOMAIN-CATALOG completo, todos los agentes DDD | Este mes |
| **Ejemplos de documentos Word/Excel de referencia** | Templates ofimáticos del framework (punto #6 de CONTINUIDAD) | Este trimestre |
| **Histórico de horas COSMIC** | Calibración de la skill de valoración COSMIC (punto #8 de CONTINUIDAD) | Este trimestre |
| **Briefing sobre procesos de licitación APB** | Agentes de licitación LCSP (E-F4) | Este trimestre |
| **Confirmación de disponibilidad de Rovo API en el tenant APB** | Activación de adapter-rovo-v1.0 | Julio 2026 |


---

## 9. Evolución del Framework a Medio/Largo Plazo

### Fase 1 — Consolidación (0–6 meses desde hoy)

**Objetivo:** pasar de "framework diseñado" a "framework operativo". Los 341 componentes existen pero ninguno está aprobado. La telemetría no emite. El dominio catalog está vacío.

**Indicadores de éxito al final de esta fase:**
- ≥30 componentes en estado `approved`, incluyendo los 5 workflows principales.
- APB-DOMAIN-CATALOG con ≥5 dominios core `approved`.
- Telemetría activa — al menos un evento por sesión de agente en `APBFrameworkTelemetry_CL`.
- Runbooks para los 3 workflows más usados (`wf-sdd-full`, `wf-code-review`, `wf-qa-evidence`).
- Primer agente ejecutado desde Teams via M365 Copilot adapter por un usuario no-Arquitectura.
- La métrica "% de componentes en draft" baja del 100% al <90%.

**Riesgos de esta fase:**
- El ciclo de aprobación se convierte en cuello de botella porque nadie tiene tiempo. Mitigación: dedicar slots recurrentes de revisión (e.g., 1h semanal de "revisión de componentes APB").
- APB-DOMAIN-CATALOG sigue sin desbloquearse porque Débora no puede priorizar el inventario de sistemas. Mitigación: establecer un deadline formal y usar el agente `apb-sub-ddd-interview-v1.0` para guiar la extracción del inventario desde una entrevista estructurada.

---

### Fase 2 — Adopción corporativa (6–18 meses)

**Objetivo:** el framework deja de ser "un proyecto de Arquitectura" y pasa a ser la plataforma de referencia usada por múltiples equipos.

**Indicadores de éxito:**
- Rovo Agents activos y usados por equipos de proyecto (no solo Arquitectura APB).
- Todos los proyectos nuevos arrancan con el workflow `wf-sdd-full`.
- ≥3 proyectos legacy con análisis DDD documentado y aprobado en APB-DOMAIN-CATALOG.
- Motor de orquestación real (E-T1) desplegado y ejecutando al menos un workflow por semana.
- Agente de Change Management / ITIL operativo (E-F1) e integrado con el proceso CAB real de APB.
- Agente de Data Governance / RGPD produciendo el RAT actualizado trimestralmente (E-F2).
- Dashboard de gobernanza en producción con datos de uso real.
- La métrica "% de componentes en draft" < 50%.

**Riesgos de esta fase:**
- **Vibe coding sistémico**: equipos de proyecto usan los agentes para generar código sin seguir el proceso SDD, aprovechando que "la IA ya lo hace". Mitigación: formación obligatoria + validación en el proceso de PR que exija spec previa para código generado por IA (`apb-dev-grill-before-code-v1.0`).
- **Proliferación sin gobernanza**: cada equipo crea sus propios agentes y skills fuera del catálogo. Mitigación: el agente `apb-agent-meta-builder-v1.0` requiere discovery previo y exige que todo componente nuevo pase por el proceso de contribución.

---

### Fase 3 — Madurez y expansión (18–36 meses)

**Objetivo:** el framework es infraestructura corporativa madura, no un proyecto.

**Indicadores de éxito:**
- El 80% de componentes en `approved` o `deprecated` — `draft` es la excepción.
- Contribuciones de equipos de proyecto al catálogo de skills sin necesitar a Arquitectura como intermediario.
- Agente de FinOps con ahorro medible y documentado (E-F3).
- Integración con sistemas core de gestión portuaria (GISPEM, Portal Docks, etc.) vía providers específicos.
- Ciclo de revisión semestral automatizado funcionando sin intervención manual.
- El framework, o partes de él (la metodología, los templates, los estándares), publicado como referencia para otras autoridades portuarias o entidades públicas (excluyendo código sensible y políticas internas).
- La métrica "% de skills con reuso >1 agente" > 50% (objetivo de GOVERNANCE.md cumplido).

---

### Riesgos transversales a largo plazo

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| LLM vendor lock-in — dependencia de Claude/Copilot | Media | Alto | Mantener los 4 adapters actualizados; no hardcodear behavior específico de un modelo en los prompts de skills |
| Proliferación descontrolada — más de 500 componentes en draft sin revisión | Alta | Medio | Activar el proceso de aprobación formal cuanto antes; considerar un ratio máximo de componentes en draft por componente aprobado |
| APB-DOMAIN-CATALOG vacío en 12 meses | Media | Crítico | Deadline formal e input de Débora — es el desbloqueador más crítico del framework |
| Obsolescencia de skills de terceros — repos externos abandonados o comprometidos | Alta | Medio | Implementar E-S2 (supply chain verification en CI) y ciclo de revisión anual de terceros |
| Resistencia cultural — equipos que prefieren no usar el framework | Media | Alto | Demostrar ROI con métricas reales desde la telemetría; involucrar a los equipos en la definición de los primeros dominios del catálogo |
| Cambio de modelo de IA — el modelo actual queda obsoleto | Alta | Bajo | Los adapters abstraen el modelo; actualizar el model string es una tarea de horas |


---

## 10. Repositorios de Terceros de Interés

Recomendaciones basadas en los gaps identificados en los tres repositorios. Para cada uno se indica el gap que cubre, el esfuerzo de integración estimado y la licencia.

### 10.1 Orquestación de agentes (gap E-T1)

**`microsoft/semantic-kernel`** (Apache 2.0)  
Motor de orquestación multi-agente con soporte nativo para Claude, GPT y otros LLMs. Compatible con .NET (el stack principal de APB) y Python. Tiene plugins, gestión de memoria, y planners que pueden mapear directamente al concepto de workflows del framework. Es la opción más robusta para implementar E-T1 en el medio plazo. El wrapper APB correspondiente sería `wrap-semantic-kernel-v1.0`.  
Esfuerzo de integración: 2–4 semanas para un wrapper básico + 1 workflow piloto.

**`langchain-ai/langgraph`** (MIT)  
Orquestación con estado persistente, ciclos de retroalimentación y backtracking. Alternativa más ligera que Semantic Kernel si el stack .NET no es un requisito. Especialmente útil para los workflows que tienen puntos de decisión condicionales (e.g., si el análisis de seguridad falla, volver a la fase de diseño).  
Esfuerzo: 1–2 semanas para un wrapper piloto.

---

### 10.2 DDD y gestión de dominios (gap APB-DOMAIN-CATALOG vacío)

**`ddd-crew/context-mapping`** (verificar licencia antes de usar)  
Herramientas visuales y plantillas para Context Mapping DDD. Complementa los templates de APB-DOMAIN-CATALOG añadiendo visualización de relaciones entre bounded contexts (upstream/downstream, patrones ACL, shared kernel, etc.). Sus plantillas son compatibles con el schema de `bounded-context-template.md`.  
Esfuerzo: bajo — adaptar sus plantillas al formato APB, sin dependencia de código ejecutable.

**Metodología Event Storming** (referencia, no código)  
El subagente `apb-sub-ddd-interview-v1.0` (v1.3.0) ya incorpora el proceso de entrevista DDD. Event Storming es la metodología complementaria para talleres presenciales con los equipos de negocio que producen el input directo para el catálogo de dominios. Documentar cómo conecta la salida de un taller de Event Storming con el `new-domain.sh` del APB-DOMAIN-CATALOG.

---

### 10.3 Seguridad y compliance (gaps E-S1, E-S2, E-S3)

**`aquasecurity/trivy`** (Apache 2.0)  
Escáner de vulnerabilidades en código, dependencias Python/npm, y manifiestos de infraestructura (Terraform, Kubernetes). Integrable como step de CI en el framework — añadir al `validate.yml` como job adicional. Sus hallazgos pueden ser consumidos directamente por `apb-agent-tech-debt-v1.0` para el análisis de CVEs. También detecta secretos en código (complementa la validación de `validate_repo.py`).  
Esfuerzo: bajo — un step de CI con `trivy fs .` no requiere desarrollo propio.

**`OWASP/www-project-devsecops-guideline`** (Creative Commons CC BY-SA 4.0)  
Guía DevSecOps del OWASP con controles aplicables a cada fase del SDLC. Material para enriquecer `apb-sec-threat-model-v1.0` y los agentes de seguridad. Especialmente relevante para el stack .NET/Azure y los requisitos ENS (alto) ya implementados en el framework.  
Esfuerzo: bajo — incorporar como referencia en los prompts de skills de seguridad.

**`FlorianBruniaux/claude-code-ultimate-guide`** (verificar licencia)  
Identificado en CONTINUIDAD §9 como candidato a insumo de `POLICY_VULNERABILITY_MANAGEMENT_v1.1.md`. Contiene criterios de hardening y listado de CVEs conocidos de MCP servers y Claude Code. Pendiente de evaluación y decisión de Débora.

---

### 10.4 Observabilidad y telemetría (gap telemetría no activa)

**`open-telemetry/opentelemetry-python`** (Apache 2.0)  
Si la telemetría de Azure Monitor resulta insuficiente o se quiere portabilidad futura, OpenTelemetry es el estándar de la industria para trazas distribuidas. Compatible con `DefaultAzureCredential` y el stack Azure actual. Permite enviar trazas simultáneamente a Azure Monitor y a otros backends (Grafana, Jaeger). El `emit_telemetry.py` actual podría refactorizarse para emitir trazas OpenTelemetry.  
Esfuerzo: medio — refactorizar `emit_telemetry.py` y actualizar el schema de telemetría.

---

### 10.5 Design System (gaps BUG-03, tipografía, mantenibilidad)

**`storybookjs/storybook`** (MIT)  
Estándar de la industria para catálogos de componentes UI. Reemplazaría o complementaría `visual-reference.html` con un entorno real donde cada componente JSX del Design System tiene ejemplos interactivos, documentación de props generada automáticamente, y tests de accesibilidad con el addon `@storybook/addon-a11y` (WCAG 2.1 AA — requisito regulatorio de APB vía RD 1112/2018).  
Esfuerzo: medio — 2–3 días para configurar Storybook y añadir stories para los componentes existentes (Button, DataGrid, etc.). Elimina el mantenimiento manual de `visual-reference.html`.

---

### 10.6 Memoria y conocimiento de agentes

**`HKUDS/LightRAG`** (Apache 2.0)  
Ya wrapeado como `wrap-hkuds-lightrag-v1.0`. El wrapper existe en el catálogo; lo que falta es desplegarlo y conectarlo a los agentes de discovery y documentación. LightRAG combina RAG con grafos de conocimiento, lo que lo hace especialmente adecuado para la memoria episódica entre sesiones (recordar qué decisiones de arquitectura se tomaron en el proyecto X, qué términos del ubiquitous language usa el dominio Y). Candidato natural para implementar la "memoria corporativa" del framework.  
Esfuerzo: alto — requiere infraestructura (vector store, grafo, API), pero el wrapper APB ya existe.

**`mem0ai/mem0`** (Apache 2.0)  
Alternativa más simple a LightRAG para memoria de agentes. SDK Python con múltiples backends (PostgreSQL, Redis, Qdrant). Más fácil de operar en Azure que LightRAG. Evaluar si LightRAG resulta demasiado complejo para el equipo de Platform de APB.  
Esfuerzo: medio — 1 semana para integrar y crear el wrapper `wrap-mem0-v1.0`.

---

### 10.7 Contratación pública LCSP (gap E-F4)

**Plataforma de Contratación del Sector Público** (API pública, sin licencia de software)  
`https://contrataciones.gob.es/` — API REST del Ministerio de Hacienda con datos de contratos del sector público en España. Permite consultar contratos similares, precios de referencia, pliegos adjudicados y proveedores habituales de APB. Integrable como `prov-lcsp-v1.0` para un futuro agente de licitación. Los datos son públicos por ley.  
Esfuerzo: bajo — crear el descriptor del provider y la skill correspondiente una vez recibido el briefing de Débora.

---

### 10.8 Repositorios pendientes de evaluación profunda

Según `discovery/PLAN_FASES_FUTURAS.md`, los siguientes repos están anotados como pendientes de análisis (punto #27 de PLAN_FASES_FUTURAS):

| Repositorio | Posible uso | Prioridad |
|-------------|------------|---------|
| `ComposioHQ/agent-orchestrator` | Alternativa de orquestación de agentes | Media |
| `ruvnet/ruflo` | Framework de agentes ligero | Baja |
| `affaan-m/ecc` | Pendiente de evaluación | Baja |
| `nexu-io/open-design` | Complemento para Design System | Baja |
| `ComposioHQ/awesome-claude-plugins` | Fuente de discovery de MCPs — no incorporar como componente | Referencia |

Recomendación: no evaluar estos repositorios hasta que los BLOQUEOs críticos (APB-DOMAIN-CATALOG, ciclo de aprobación) estén resueltos. El beneficio marginal de añadir más componentes de terceros es menor que el coste de gobernanza de 341 componentes ya en draft.


---

## Apéndice A — Comandos de Verificación del Estado del Repositorio

```bash
# Verificación completa del estado (ejecutar en este orden):
cd APB-IA-FRAMEWORK/
pip install pyyaml --break-system-packages

# 1. Validar estructura, frontmatter y referencias
python3 scripts/validate_repo.py --strict
# Esperado: 0 errores, N warnings source_commit:unverified (exentos por política), ✅

# 2. Verificar sincronización de catálogos (REQUIERE BUG-02 RESUELTO ANTES)
python3 scripts/generate_catalog.py --check
# Esperado (tras fix BUG-02): exit 0, sin drift
# Estado actual SIN fix: CRASH por possessive quantifier en regex de Python 3.10

# 3. Tests del validador
python3 -m unittest tests.test_validate_repo -v
# Esperado: 19/19 OK

# 4. Listar componentes reales
python3 scripts/invoke_agent.py --list
python3 scripts/invoke_agent.py --list-workflows

# 5. Recuento de componentes por tipo (tras fix BUG-02)
python3 scripts/generate_catalog.py 2>&1 | head -15
# Real a 2026-06-29: 341 total (175 skills APB, 51 third-party, 35 agentes,
#                               33 subagentes, 17 workflows, 19 providers,
#                               7 wrappers, 4 adapters)
```

---

## Apéndice B — Resumen Ejecutivo de Hallazgos Críticos

Para una presentación rápida a dirección o al equipo, los hallazgos más importantes son:

**Lo que funciona bien:**
1. El framework tiene 341 componentes con arquitectura sólida y validación automática en CI.
2. Cuatro adapters cubren todos los runtimes relevantes (Claude, Copilot, M365, Rovo).
3. El código de telemetría, validación y generación de catálogos es de alta calidad.
4. El Design System v1.3.0 tiene una stack DX sólida (tokens + style guide + visual reference + oxlintrc).

**Lo que necesita acción urgente:**
1. **BUG-02**: `generate_catalog.py` crashea — el CI no valida el drift de catálogo. Fix en 30 minutos.
2. **BUG-01**: Template de workflows sin frontmatter YAML — cualquier workflow nuevo creado desde él falla en CI. Fix en 20 minutos.
3. **0 componentes aprobados de 341**: el framework es operativamente un conjunto de borradores. El primer ciclo de aprobación es la acción de mayor impacto.
4. **APB-DOMAIN-CATALOG vacío**: bloquea todos los agentes DDD. El desbloqueador es la lista de sistemas/APIs que debe proveer Débora.

**Los dos inputs humanos más críticos (bloqueantes):**
1. Débora: lista de sistemas/APIs corporativas de APB → desbloquea DOMAIN-CATALOG.
2. Arquitectura APB + Ciberseguridad: iniciar ciclo de aprobación de 5 componentes → desbloquea la gobernanza real.

---

*Generado por IA: Claude Sonnet (Anthropic/Cowork), sesión 2026-06-29*  
*Revisión y aprobación pendiente: Débora Martín / Arquitectura APB*  
*Este documento es una propuesta IA. Ningún punto es vinculante sin aprobación humana explícita.*  
*Conforme al AI_MARKING_STANDARD del APB AI Framework — documento tipo `doc`.*

