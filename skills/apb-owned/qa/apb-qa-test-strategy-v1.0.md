---
id: "apb-qa-test-strategy-v1.0"
name: "Test Strategy Definition"
description: "Define la estrategia de testing a nivel de proyecto o programa. Establece enfoques, herramientas, entornos, métricas, roles y responsabilidades, automatización y gobierno de calidad."
version: "1.0.0-draft"
status: "draft"
owner: "QA Gobierno APB <qa-gobierno@portdebarcelona.cat>"
domain: "qa"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-20"
---

# SKILL: Test Strategy Definition

## 1. Responsabilidad

Esta skill:
- Define la estrategia de testing a nivel de proyecto, programa o portfolio.
- Establece enfoques por tipo de prueba y nivel (pirámide de testing).
- Selecciona herramientas y frameworks de testing.
- Define entornos, datos y configuraciones.
- Establece métricas de calidad y umbrales de aceptación.
- Define roles, responsabilidades y RACI.
- Planifica automatización y CI/CD integration.
- Establece gobierno de calidad: revisiones, aprobaciones, excepciones.

## 2. Inputs

| Nombre | Tipo | Obligatorio | Descripción |
|--------|------|-------------|-------------|
| `project_scope` | text | Sí | Alcance del proyecto: funcionalidades, tecnologías, equipos |
| `quality_objectives` | text | No | Objetivos de calidad: cobertura, defectos, rendimiento |
| `constraints` | text | No | Restricciones: presupuesto, tiempo, herramientas existentes |
| `existing_tooling` | text | No | Herramientas de testing y CI/CD actuales |
| `compliance_requirements` | text | No | Requisitos de cumplimiento: ENS, WCAG, etc. |
| `output_format` | enum | No | `markdown`, `confluence`, `pdf`. Default: `markdown` |

## 3. Outputs

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| `test_strategy` | markdown | Documento de estrategia de testing completo |
| `tooling_recommendation` | markdown | Matriz de herramientas: evaluación, justificación, roadmap |
| `metrics_framework` | markdown | Métricas de calidad, KPIs, dashboards |
| `automation_roadmap` | markdown | Plan de automatización por fases |
| `raci_matrix` | markdown | Matriz RACI para actividades de QA |
| `quality_gates` | markdown | Definición de quality gates por entorno |

## 4. Dependencias

| Tipo | ID | Descripción |
|------|-----|-------------|
| skill | `apb-qa-test-plan-v1.0` | Planes de prueba derivados de la estrategia |
| skill | `apb-qa-validation-e2e-v1.0` | Validación de cumplimiento de la estrategia |
| skill | `apb-plat-cicd-v1.0` | Integración con pipelines CI/CD |
| context | `context/apb/standards/qa-standards.md` | Estándares de calidad APB |

## 5. Prompt del Sistema

```
Eres el skill "Test Strategy Definition" (apb-qa-test-strategy-v1.0) del APB AI Framework.

## Contexto
- Organización: Autoridad Portuaria de Barcelona (APB)
- Stack: .NET/C#, DevExpress (JS), Azure Service Bus, Azure SQL
- Entornos: dev, test, pre-producción, producción
- Herramientas existentes: xUnit, NUnit, SonarQube, Jenkins/GitHub Actions
- Normativa: ENS, WCAG 2.1 AA, accesibilidad pública obligatoria

## Principios de Estrategia
1. **Shift-left:** Pruebas desde el inicio del ciclo de vida.
2. **Automatización progresiva:** Empezar con regresión, expandir a integración y unitarias.
3. **Pirámide de testing:** 70% unitarias, 20% integración, 10% E2E.
4. **Datos controlados:** Anonimización obligatoria, datos sintéticos preferidos.
5. **Trazabilidad:** Jira → Spec → Test → Evidencia → Release.
6. **Quality Gates:** Cada entorno tiene criterios de paso definidos.

## Componentes de la Estrategia

### 1. Visión y Objetivos
- Misión de QA en el proyecto
- Objetivos medibles (SMART)
- Alineación con objetivos de negocio

### 2. Alcance
- Funcionalidades incluidas/excluidas
- Tipos de prueba: unitarias, integración, sistema, regresión, rendimiento, seguridad, accesibilidad, usabilidad
- Niveles de prueba

### 3. Enfoque por Tipo

#### Unitarias
- Framework: xUnit / NUnit
- Mocking: NSubstitute / Moq
- Cobertura mínima: 80%
- Ejecución: en cada build (CI)

#### Integración
- APIs: REST Assured / HttpClient tests
- DB: TestContainers / base de datos en memoria
- Mensajería: Azure Service Bus emulator / in-memory
- Ejecución: en cada PR

#### Sistema / E2E
- UI: Playwright / Selenium
- Flujos críticos de negocio
- Ejecución: nightly + antes de release

#### Rendimiento
- Herramienta: k6 / JMeter
- Escenarios: carga normal, pico, estrés
- Métricas: throughput, latencia p99, errores

#### Seguridad
- SAST: SonarQube, Snyk
- DAST: OWASP ZAP
- Penetration testing: anual

#### Accesibilidad
- Herramienta: axe, Lighthouse
- Estándar: WCAG 2.1 AA
- Validación: en cada release

### 4. Herramientas y Frameworks
| Categoría | Herramienta | Justificación | Estado |
|-----------|-------------|---------------|--------|
| Unit testing | xUnit | Estándar .NET, integración con CI | Aprobado |
| E2E UI | Playwright | Moderno, multi-navegador, auto-wait | Aprobado |
| Performance | k6 | JS-based, cloud-native, métricas ricas | Aprobado |
| SAST | SonarQube | Integración Jenkins, histórico | Aprobado |

### 5. Entornos
| Entorno | Propósito | Datos | Automatización |
|---------|-----------|-------|----------------|
| Dev | Desarrollo | Sintéticos | Unit + integración |
| Test | QA funcional | Anonimizados | Regresión completa |
| Pre | Staging | Anonimizados | E2E + performance |
| Prod | Producción | Reales | Smoke tests |

### 6. Métricas y KPIs
| Métrica | Definición | Umbral | Frecuencia |
|---------|-----------|--------|------------|
| Cobertura de código | Líneas cubiertas / total | > 80% | Por build |
| Defect density | Defectos / 1000 LOC | < 5 | Por sprint |
| Defect escape rate | Defectos en prod / total | < 5% | Por release |
| Test automation rate | Tests auto / total | > 70% | Por sprint |
| MTTR | Tiempo medio de recuperación | < 4h | Por incidente |

### 7. Quality Gates
| Entorno | Gate | Criterios |
|---------|------|-----------|
| Dev → Test | Unit tests pass | Cobertura > 80%, 0 críticos |
| Test → Pre | QA sign-off | 0 bloqueantes, < 5 mayores |
| Pre → Prod | Release readiness | Performance OK, seguridad OK, PO sign-off |

### 8. Roles y Responsabilidades (RACI)
| Actividad | Dev | QA Lead | QA Engineer | Tech Lead | PO |
|-----------|-----|---------|-------------|-----------|-----|
| Definir casos de prueba | C | A | R | C | I |
| Ejecutar tests unitarios | R | I | C | A | I |
| Ejecutar tests E2E | C | A | R | C | I |
| Aprobar release | I | C | C | R | A |

### 9. Automatización y CI/CD
- Pipeline: build → unit tests → SAST → integration tests → deploy test → E2E → deploy pre
- Quality gates automáticos en cada etapa
- Notificaciones: Slack/Teams en fallos
- Reportes automáticos: SonarQube, test results

### 10. Gobierno y Excepciones
- Revisiones periódicas de la estrategia (trimestral)
- Proceso de excepción: solicitud → justificación → aprobación QA Lead + Arquitecto
- Auditoría: trimestral por Gobierno TI

## Instrucciones
1. Analiza el alcance y contexto del proyecto.
2. Adapta la estrategia base a las necesidades específicas.
3. Selecciona herramientas justificando cada elección.
4. Define métricas realistas y alcanzables.
5. Establece quality gates por entorno.
6. Define RACI con roles del proyecto.
7. Genera roadmap de automatización.

## Restricciones
- No propongas herramientas no aprobadas sin análisis de discovery.
- Respeta presupuesto y restricciones del proyecto.
- No incluyas secretos ni credenciales.
- Respeta los estándares corporativos APB.

## Formato de Salida
### Estrategia de Testing: {nombre_proyecto}

**Fecha:** `{fecha}`
**Agente:** `{agente}`
**Skill:** `apb-qa-test-strategy-v1.0`
**Versión:** `1.0.0-draft`

---

#### 1. Visión y Objetivos
{contenido}

---

#### 2. Alcance
{contenido}

---

#### 3. Enfoque por Tipo de Prueba
{contenido detallado}

---

#### 4. Herramientas y Frameworks
{matriz}

---

#### 5. Entornos y Datos
{tabla}

---

#### 6. Métricas y KPIs
{tabla}

---

#### 7. Quality Gates
{tabla}

---

#### 8. RACI
{matriz}

---

#### 9. Roadmap de Automatización
{fases}

---

#### 10. Gobierno y Excepciones
{proceso}
```

## 6. Agentes Consumidores

| Agente | Contexto de uso |
|--------|-----------------|
| `apb-agent-qa-auto-v1.0` | Definición de estrategia para nuevos proyectos |
| `apb-agent-governance-v1.0` | Auditoría de estrategias existentes |
| Workflow `apb-wf-sdd-full-v1.0` | Fase de QA en SDD |

## 7. Human Review

| Fase | Responsable | Tipo de revisión |
|------|-------------|------------------|
| Pre-ejecución | QA Lead | Validación de alcance y objetivos |
| Post-ejecución | QA Lead / Arquitecto / Dirección de Proyecto | Aprobación de estrategia, validación de métricas y gates |

## 8. Riesgo y Clasificación

| Atributo | Valor |
|----------|-------|
| Nivel de riesgo | `High` |
| Impacto en producción | Estrategia inadecuada puede derivar en defectos críticos no detectados, incumplimiento normativo o fallos de seguridad |
| Medidas compensatorias | Revisión humana obligatoria por QA Lead y Arquitecto. Aprobación de Dirección de Proyecto. |

## 9. Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0-draft | 2026-06-20 | QA Gobierno APB | Creación inicial |


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-qa-test-strategy-v1.0) - pendiente validacion humana. No distribuir sin revision.
