---
id: "third-obra-test-driven-development-v1.0"
name: "Test-Driven Development Strategy"
description: "Estrategia de testing y TDD, adaptada de obra/superpowers."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "qa"
created_date: "2026-06-22"
review_date: "2026-06-22"
autonomy_level: 1
source_repo: "https://github.com/obra/superpowers"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
---

# Estrategia de Testing para APB

## Overview
Definición de estrategia de testing integral para proyectos de la APB, cubriendo niveles de prueba (unitario, integración, sistema, aceptación), tipos de prueba (funcional, no funcional, seguridad, accesibilidad), cobertura objetivo y plan de automatización. Basada en principios de Test-Driven Development (TDD) adaptados al stack tecnológico APB.

## When to Use
- Inicio de nuevo proyecto o fase de desarrollo
- Cambio arquitectónico significativo
- Definición de Definition of Done (DoD)
- Planificación de sprint o release
- Auditoría de calidad

**When NOT to use:**
- Bugfix puntual (usar prueba de regresión específica)
- Cambio menor sin impacto arquitectónico (usar pruebas existentes)
- Mantenimiento correctivo rutinario

## Core Pattern

### Fase 1: Análisis de Contexto
1. **Stack tecnológico:** .NET, Django, DevExpress, Azure SQL, PostgreSQL
2. **Tipo de aplicación:** Web, API, Desktop, Móvil
3. **Críticidad:** Baja, Media, Alta, Crítica (según ENS)
4. **Restricciones:** Tiempo, recursos, entornos disponibles
5. **Regulatorio:** Requisitos ENS, LOPDGDD, accesibilidad

### Fase 2: Definición de Niveles de Prueba

| Nivel | Tipo | Objetivo | Cobertura APB | Automatización |
|-------|------|----------|---------------|----------------|
| **Unitario** | Caja blanca | Validar unidades de código individuales | ≥ 80% líneas | Obligatoria |
| **Integración** | Caja gris | Validar interacción entre componentes | ≥ 60% flujos críticos | Obligatoria |
| **Sistema** | Caja negra | Validar sistema completo | 100% casos de uso críticos | Recomendada |
| **Aceptación** | Caja negra | Validar criterios de aceptación | 100% AC definidos | Manual + automatizada |

### Fase 3: Definición de Tipos de Prueba

#### Funcionales
- **Pruebas de regresión:** Validar que cambios no rompen funcionalidad existente
- **Pruebas de humo (smoke):** Validar funcionalidad básica tras despliegue
- **Pruebas de sanidad:** Validar corrección específica tras bugfix

#### No Funcionales
- **Rendimiento:** Tiempo de respuesta, throughput, escalabilidad (k6, JMeter)
- **Carga:** Comportamiento bajo carga esperada y pico
- **Estrés:** Comportamiento bajo carga extrema
- **Accesibilidad:** WCAG 2.1 AA mínimo (axe, Lighthouse)
- **Seguridad:** SAST/DAST en pipeline (SonarQube, OWASP ZAP)
- **Usabilidad:** Validación con usuarios finales (proyectos críticos)

#### Específicas APB
- **Compatibilidad navegadores:** Edge (corporativo), Chrome, Firefox
- **Compatibilidad dispositivos:** Desktop principal, tablet según necesidad
- **Localización:** Español, catalán (cuando aplique)
- **Backup/recovery:** Validación de procedimientos de recuperación

### Fase 4: Definición de Entornos

| Entorno | Propósito | Datos | Automatización |
|---------|-----------|-------|----------------|
| **Local** | Desarrollo | Datos sintéticos (anonymize) | Unit + integración parcial |
| **CI** | Validación automática | Datos de prueba | Unit + integración + smoke |
| **Pre-producción** | Validación funcional | Datos anonimizados producción | Regresión completa |
| **Producción** | Sanidad post-despliegue | Datos reales | Smoke + monitorización |

### Fase 5: Definición de Métricas

| Métrica | Objetivo APB | Herramienta |
|---------|-------------|-------------|
| Cobertura de código | ≥ 80% (unitario) | SonarQube, Coverlet |
| Cobertura de mutación | ≥ 60% (proyectos críticos) | Stryker |
| Defectos por sprint | Tendencia decreciente | Jira |
| Defectos escapados | < 5% | Jira + monitorización |
| Tiempo medio de resolución | < 3 días (críticos) | Jira |
| Pruebas automatizadas | ≥ 70% del total | Pipeline CI/CD |
| Tiempo de ejecución suite | < 15 min (unit + integración) | Pipeline |

### Fase 6: Plan de Automatización

#### Prioridad 1 (Obligatorio)
- Pruebas unitarias (xUnit, NUnit, pytest)
- Pruebas de integración de APIs (REST Assured, pytest)
- Pruebas de regresión críticas (Playwright, Selenium)

#### Prioridad 2 (Recomendado)
- Pruebas E2E de flujos críticos (Playwright)
- Pruebas de contrato API (Pact, Spring Cloud Contract)
- Pruebas de rendimiento base (k6)

#### Prioridad 3 (Deseable)
- Pruebas de accesibilidad automatizadas (axe-core)
- Pruebas de seguridad automatizadas (OWASP ZAP en CI)
- Pruebas de carga periódicas

### Fase 7: Generación de Estrategia

```markdown
# Estrategia de Testing — [Nombre Proyecto]

## Contexto
- Proyecto: [nombre]
- Stack: [tecnologías]
- Críticidad: [nivel]

## Niveles de Prueba
| Nivel | Cobertura | Automatización | Herramienta |
|-------|-----------|----------------|-------------|
| Unitario | ≥ 80% | Sí | xUnit + Moq |
| Integración | ≥ 60% | Sí | TestServer + EF InMemory |
| E2E | 100% críticos | Sí | Playwright |

## Tipos de Prueba
- Funcionales: [lista]
- No funcionales: [lista]
- Específicas: [lista]

## Entornos
[Definición de entornos y datos]

## Métricas
[Objetivos y herramientas]

## Plan de Automatización
[Fases y prioridades]

## Riesgos
| Riesgo | Mitigación |
|--------|-----------|
| [desc] | [mitigación] |

## Aprobación
- QA Lead: [nombre] — [fecha]
- Tech Lead: [nombre] — [fecha]
```

## Quick Reference

| Tipo Proyecto | Cobertura Mínima | Pruebas Obligatorias |
|--------------|-----------------|---------------------|
| Crítico (ENS Alto) | 85% unit, 70% integración, 100% AC | Unit + Integración + E2E + Rendimiento + Seguridad |
| Importante (ENS Medio) | 80% unit, 60% integración, 100% AC | Unit + Integración + E2E críticos |
| Estándar (ENS Básico) | 70% unit, 50% integración | Unit + Integración + Smoke |

## Implementation

### Checklist de Estrategia
```
□ Niveles de prueba definidos y justificados
□ Cobertura objetivo establecida por nivel
□ Tipos de prueba identificados por criticidad
□ Entornos definidos con datos especificados
□ Métricas objetivo con herramientas asignadas
□ Plan de automatización con prioridades
□ Riesgos identificados con mitigaciones
□ Aprobadores definidos
```

## Common Mistakes
- **Testing como fase final:** El testing debe integrarse desde el diseño (shift-left)
- **Cobertura como única métrica:** 100% cobertura ≠ 0 bugs; calidad de pruebas importa más
- **Ignorar pruebas no funcionales:** Rendimiento y seguridad son tan críticos como funcionalidad
- **Automatizar todo indiscriminadadamente:** Algunas pruebas son más eficientes manuales
- **No mantener pruebas:** Las pruebas obsoletas generan falsos positivos y desconfianza
- **Olvidar accesibilidad:** Es obligatorio legal (RD 1112/2018) y ético

## Real-World Impact
- Reducción de 50% en defectos escapados a producción
- Reducción de 30% en tiempo de validación de releases
- Cumplimiento de requisitos de contratación pública

---

## Adapted From
- **Source:** obra/superpowers — skill `test-driven-development`
- **License:** MIT
- **Attribution:** Patrón RED-GREEN-REFACTOR y filosofía de testing sistemático inspirados en obra/superpowers. Reescrito completamente para estrategia integral de testing, stack tecnológico APB y requisitos regulatorios españoles.

## References
- ISTQB — Syllabus Foundation Level
- OWASP Testing Guide 4.2
- RD 1112/2018 — Accesibilidad web
- context/apb/standards/qa-standards.md
- context/apb/policies/qa-policy.md
