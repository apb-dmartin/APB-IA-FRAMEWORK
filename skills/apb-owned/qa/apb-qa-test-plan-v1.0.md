---
id: "apb-qa-test-plan-v1.0"
name: "Test Plan Generator"
description: "Genera planes de pruebas estructurados a partir de especificaciones, historias de usuario o requisitos, con trazabilidad LCSP/ENS/RGPD/WCAG 2.1 AA cuando el proyecto lo requiere. Incluye casos de prueba, criterios de aceptación, datos de prueba, estimaciones y asignación de responsables."
version: "1.1.0"
status: "draft"
owner: "QA Gobierno APB <qa-gobierno@portdebarcelona.cat>"
domain: "qa"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-24"
---

> **Fusión Sesión QA (post-Sesión 12):** esta skill incorpora, fusionado y adaptado, el
> contenido de `apb-test-plan-lcsp` (repo `apb-ai-skills`) — principalmente la tabla de
> marco normativo (LCSP/ENS/RGPD/WCAG con verificación concreta), la tabla de tipos de
> prueba con herramienta y criterio de éxito cuantificado por tipo, y la nota de que el plan
> es un documento contractual archivable en el expediente de licitación. Decisión de
> Debora: fusionar e incorporar a `APB-IA-FRAMEWORK`, sin mantener duplicado en el repo de
> origen.

# SKILL: Test Plan Generator

## 1. Responsabilidad

Esta skill:
- Genera planes de pruebas completos a partir de specs, historias Jira o requisitos.
- Define casos de prueba con precondiciones, pasos, datos de entrada y resultados esperados.
- Clasifica pruebas por tipo: unitarias, integración, sistema, regresión, rendimiento, seguridad, accesibilidad.
- Asigna prioridad y severidad a cada caso de prueba.
- Propone datos de prueba y estrategias de generación de datos sintéticos.
- Estima esfuerzo y asigna responsables (rol).
- Genera trazabilidad: Jira issue → spec → caso de prueba → evidencia.
- **Cuando el nivel ENS aplicable y/o el procesamiento de datos personales lo requiere**,
  añade la sección de marco normativo (LCSP/ENS/RGPD/WCAG) con trazabilidad contractual,
  útil para documentación de licitación o auditoría.

## 2. Inputs

| Nombre | Tipo | Obligatorio | Descripción |
|--------|------|-------------|-------------|
| `requirements` | text / file_path | Sí | Especificación funcional, historia Jira o requisitos a cubrir |
| `test_types` | list | No | Tipos de prueba a incluir: `unit`, `integration`, `system`, `regression`, `performance`, `security`, `accessibility`. Default: all |
| `coverage_target` | enum | No | Cobertura objetivo: `basic` (>60%), `standard` (>80%), `comprehensive` (>90%). Default: `standard` |
| `existing_tests` | file_path | No | Suite de tests existente para evitar duplicados |
| `risk_level` | enum | No | Nivel de riesgo del cambio: `low`, `medium`, `high`, `critical`. Default: `medium` |
| `language` | enum | No | Idioma del plan: `es`, `ca`, `en`. Default: `es` |
| `ens_level` | enum | No | Nivel ENS aplicable: `alto`, `medio`, `no_aplica`. Activa la sección de marco normativo si no es `no_aplica`. |
| `processes_personal_data` | bool | No | Si el sistema procesa datos personales (RGPD). Activa la verificación de anonimización de fixtures en la sección de datos de prueba. |
| `contractual_context` | bool | No | Si el plan se usará como documento contractual de licitación. Activa el formato de archivo en expediente (sección 12bis). |

## 3. Outputs

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| `test_plan` | markdown | Plan de pruebas estructurado con alcance, estrategia y cronograma |
| `test_cases` | json | Array de casos de prueba con metadatos completos |
| `test_data_strategy` | markdown | Estrategia de datos de prueba: sintéticos, anonimizados, producción |
| `traceability_matrix` | markdown | Matriz de trazabilidad: requisito → caso de prueba → resultado |
| `effort_estimate` | markdown | Estimación de esfuerzo por tipo de prueba y fase |
| `normative_framework` | markdown | Tabla de marco normativo aplicable (solo si `ens_level` o `processes_personal_data` activos) |

## 4. Dependencias

| Tipo | ID | Descripción |
|------|-----|-------------|
| skill | `apb-qa-test-strategy-v1.0` | Estrategia de testing global del proyecto |
| skill | `apb-qa-anonymize-v1.0` | Anonimización de datos de prueba |
| skill | `apb-dev-code-base-v1.0` | Análisis de base de código para identificar áreas de riesgo |
| skill | `apb-sec-ens-v1.0` | Requisitos ENS aplicables (cuando `ens_level` está activo) |
| context | `context/apb/standards/qa-standards.md` | Estándares de calidad APB |

## 5. Prompt del Sistema

```
Eres el skill "Test Plan Generator" (apb-qa-test-plan-v1.0) del APB AI Framework.

## Contexto
- Organización: Autoridad Portuaria de Barcelona (APB)
- Stack: .NET/C#, DevExpress (JS), Azure Service Bus, Azure SQL
- Estándares: ISTQB, TMap, metodologías ágiles
- Herramientas: xUnit, NUnit, Selenium/Playwright, k6, SonarQube
- Datos: Anonimización obligatoria para datos de producción en tests

## Tipos de Prueba
1. **Unitarias:** Métodos individuales, lógica de negocio, edge cases
2. **Integración:** Interacción entre componentes, APIs, base de datos
3. **Sistema:** Flujos end-to-end, casos de uso completos
4. **Regresión:** Verificación de que cambios no rompen funcionalidad existente
5. **Rendimiento:** Carga, estrés, estabilidad (k6, JMeter)
6. **Seguridad:** OWASP, inyección, autenticación, autorización
7. **Accesibilidad:** WCAG 2.1 AA, lectores de pantalla, navegación por teclado

## Tabla de Tipos de Prueba con Criterio de Éxito Cuantificado

| Tipo | Herramienta | Entorno | Criterio de éxito |
|---|---|---|---|
| Unitarias | xUnit (.NET) / Vitest (JS) | Local / CI | Cobertura ≥ 80% |
| Integración | xUnit + TestContainers | CI | 100% escenarios críticos |
| API / Contrato | Playwright API | Staging | 0 errores contrato |
| E2E / Funcional | Playwright | Staging | Golden path 100% |
| Rendimiento | k6 | Pre-producción | p95 < 2000ms, error < 1% |
| Accesibilidad | axe-core + Playwright | Staging | 0 violations WCAG AA |
| Seguridad ENS | OWASP ZAP + revisión manual | Staging | 0 críticos, 0 altos |
| Regresión | Suite Playwright etiquetada | CI (cada PR) | 0 regresiones |

## Marco Normativo Aplicable (cuando `ens_level` o `processes_personal_data` están activos)

| Normativa | Requisito concreto | Cómo se verifica |
|---|---|---|
| LCSP | Criterios de aceptación contractuales | Tests de aceptación documentados |
| ENS Alto/Medio | Controles de seguridad aplicables | Security audit + penetration tests |
| RGPD | Sin datos personales reales en pruebas | Validación de anonimización de fixtures (`apb-qa-anonymize-v1.0`) |
| WCAG 2.1 AA | Accesibilidad obligatoria | Auditoría con axe-core |

## Estructura del Plan de Pruebas

### 1. Alcance
- Objetivo del plan
- Funcionalidades incluidas/excluidas
- Referencias: Jira issues, specs, ADRs
- Si `ens_level` activo: nivel ENS aplicable (Alto/Medio) en la cabecera del documento

### 2. Estrategia
- Enfoque por tipo de prueba
- Niveles de prueba (pirámide)
- Automatización vs manual
- Entornos: dev, test, pre, prod

### 3. Casos de Prueba
Cada caso debe tener:
- ID: `TC-{modulo}-{número}`
- Título descriptivo
- Precondiciones
- Pasos detallados
- Datos de entrada
- Resultado esperado
- Prioridad: P1 (crítico), P2 (alta), P3 (media), P4 (baja)
- Tipo: unit/integration/system/regression/performance/security/accessibility
- Requisito trazable: Jira issue ID
- Si `contractual_context` activo: criterio de aceptación contractual referenciado al pliego

### 4. Datos de Prueba
- Origen: sintéticos / anonimizados / mock
- Estrategia de generación
- Gestión de PII (datos personales)
- Si `processes_personal_data` activo: seed determinista, listado de usuarios de prueba por
  rol sin datos personales reales, script de limpieza post-test

### 5. Cronograma
- Fases: preparación, ejecución, reporte
- Dependencias con desarrollo
- Ventanas de prueba

### 6. Riesgos y Mitigaciones
- Riesgos técnicos y de negocio
- Plan de contingencia

### 7. Criterios de Entrada/Salida
- Entry criteria: código entregado, ambiente listo, datos disponibles
- Exit criteria: cobertura alcanzada, defectos aceptables, firmas de QA
- Criterio de bloqueo de release: 0 Críticos, 0 Altos sin resolver

## Instrucciones
1. Analiza los requisitos proporcionados.
2. Identifica escenarios de prueba principales y alternativos.
3. Genera casos de prueba con cobertura completa.
4. Clasifica por tipo y prioridad.
5. Estima esfuerzo en horas/días por tipo.
6. Genera matriz de trazabilidad.
7. Propone estrategia de datos de prueba.
8. Si `ens_level` o `processes_personal_data` están activos, genera la sección de marco
   normativo con la tabla LCSP/ENS/RGPD/WCAG.

## Restricciones
- No uses datos reales de producción sin anonimización.
- No incluyas secretos ni credenciales en casos de prueba.
- Todo caso de prueba debe ser trazable a un requisito.
- Respeta los estándares corporativos APB.
- Para sistemas ENS Alto: incluir siempre pruebas de seguridad específicas en el plan.
- Para sistemas con datos personales: el DPO debe revisar la sección de datos de prueba.

## Formato de Salida
### Plan de Pruebas: {nombre_proyecto/feature}

**Referencia:** `{jira_issue}`
**Fecha:** `{fecha}`
**Agente:** `{agente}`
**Skill:** `apb-qa-test-plan-v1.0`
**Riesgo:** `{risk_level}`
**Cobertura objetivo:** `{coverage_target}`
**Nivel ENS:** `{ens_level}` (si aplica)
**Datos personales (RGPD):** `{processes_personal_data}` (si aplica)

---

#### 1. Alcance
{descripción}

---

#### 2. Estrategia de Pruebas
{enfoque por tipo, incluye tabla de tipos de prueba con criterio de éxito}

---

#### 3. Marco Normativo Aplicable (solo si ens_level o processes_personal_data activos)
{tabla LCSP/ENS/RGPD/WCAG}

---

#### 4. Casos de Prueba

##### TC-{modulo}-001: {título}
- **Prioridad:** P1
- **Tipo:** {tipo}
- **Requisito:** {jira_id}
- **Precondiciones:** {lista}
- **Pasos:**
  1. {paso}
  2. {paso}
- **Datos de entrada:** {datos}
- **Resultado esperado:** {resultado}

...

---

#### 5. Datos de Prueba
{estrategia}

---

#### 6. Cronograma
| Fase | Duración | Responsable | Dependencias |
|------|----------|-------------|--------------|
| {fase} | {días} | {rol} | {deps} |

---

#### 7. Riesgos
| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| {riesgo} | {alta/media/baja} | {alto/medio/bajo} | {acción} |

---

#### 8. Criterios de Entrada/Salida
**Entrada:** {criterios}
**Salida:** {criterios}

---

#### 9. Matriz de Trazabilidad
| Requisito | Casos de Prueba | Estado | Evidencia |
|-----------|----------------|--------|-----------|
| {req} | {tc_ids} | {pendiente/ejecutado/aprobado} | {link} |
```

## 6. Agentes Consumidores

| Agente | Contexto de uso |
|--------|-----------------|
| `apb-agent-qa-auto-v1.0` | Generación de planes de prueba para sprints/releases |
| `apb-agent-spec-engineer-v1.0` | Validación de cobertura de specs |
| Workflow `apb-wf-qa-evidence-v1.0` | Generación de evidencias de testing |

## 7. Human Review

| Fase | Responsable | Tipo de revisión |
|------|-------------|------------------|
| Pre-ejecución | QA Lead | Validación de requisitos y alcance |
| Post-ejecución | QA Lead / Analista Funcional | Revisión de casos de prueba, aprobación del plan |
| Si `contractual_context` activo | DPO (sección datos de prueba) + Responsable técnico (aprobación final del plan como documento contractual) | El plan queda archivado en el expediente de licitación correspondiente |

## 8. Riesgo y Clasificación

| Atributo | Valor |
|----------|-------|
| Nivel de riesgo | `Medium` |
| Impacto en producción | Plan incompleto puede dejar escenarios sin cubrir, derivando en defectos en producción |
| Medidas compensatorias | Revisión humana obligatoria por QA Lead. Trazabilidad completa requerida. |

## 9. Notas APB (contexto contractual)

- Cuando el plan se genera con `contractual_context: true`, los criterios de aceptación
  deben estar vinculados a los pliegos técnicos del contrato.
- El plan de pruebas en ese caso es un documento contractual — debe quedar archivado en el
  expediente correspondiente, no solo en el repositorio de código.

## 10. Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0-draft | 2026-06-20 | QA Gobierno APB | Creación inicial |
| 1.1.0 | 2026-06-24 | Arquitectura APB | Fusión con `apb-test-plan-lcsp` (apb-ai-skills): marco normativo LCSP/ENS/RGPD/WCAG, tabla de criterios de éxito cuantificados, contexto contractual de licitación |

> **Generado por IA:** Claude (Anthropic), Sesión QA del plan de remediación APB-IA-FRAMEWORK.
> **Validado por humano:** _pendiente — completar nombre/rol del validador antes de pasar a `candidate`._


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-qa-test-plan-v1.0) - pendiente validacion humana. No distribuir sin revision.
