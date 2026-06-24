---
id: "third-neolabhq-sdd-implement-v1.0"
name: "Spec-Driven Implementation (SDD)"
description: "Implementa código production-ready mediante Spec-Driven Development: transforma especificaciones en implementaciones con quality gates."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "development"
created_date: "2026-06-22"
review_date: "2026-06-22"
autonomy_level: 1
source_repo: "https://github.com/NeoLabHQ/context-engineering-kit"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
---

# SKILL_DEV_IMPLEMENT — Spec-Driven Development Implementation

## 1. Propósito y Alcance

Esta skill adapta el plugin SDD de NeoLabHQ al framework APB, extendiendo su alcance
a un workflow universal de implementación para cualquier tecnología y dominio.

**Filosofía core**: "Development as compilation" — Las especificaciones son el código fuente;
la implementación es el compilado. El agente actúa como compilador que transforma
especificaciones de alta calidad en código funcional.

**Características clave:**
- Basado en estándar arc42 (documentación de arquitectura) adaptado para LLMs
- Multi-agent orchestration con context isolation (previene context rot)
- Quality gates con LLM-as-Judge (evaluación basada en rúbricas)
- Continuous learning: skills generadas automáticamente para tareas específicas
- Funciona mejor en codebases complejas y legacy (análisis de impacto integrado)

## 2. Workflow SDD (3 Comandos Core)

### 2.1 /add-task — Crear Especificación Inicial

```bash
# Crear archivo de especificación inicial
/add-task "Implementar sistema de autenticación con JWT y refresh tokens"

# Output: .specs/tasks/draft/auth-system.feature.md
```

**Estructura del archivo generado:**
```yaml
---
id: AUTH-001
title: Sistema de Autenticación JWT
status: draft
priority: high
assigned_to: developer-agent
depends_on: []  # IDs de tareas previas
---

# Contexto y Motivación
## Business Context
El sistema requiere autenticación segura para usuarios web y mobile.

## Current State
Autenticación actual basada en sessions (stateful), no escalable.

## Target State
Autenticación stateless con JWT access tokens (15min) y refresh tokens (7días).

# Requisitos Funcionales
## Must Have
- [ ] Login con email/password
- [ ] Generación de JWT access token
- [ ] Generación de refresh token
- [ ] Validación de tokens en middleware
- [ ] Logout con invalidación de refresh tokens

## Should Have
- [ ] 2FA con TOTP
- [ ] Rate limiting en login (5 intentos/15min)

## Nice to Have
- [ ] OAuth2 integration (Google, GitHub)

# Requisitos No-Funcionales
- Latencia login: < 200ms p99
- Availability: 99.9%
- Security: OWASP ASVS Level 2
- Compliance: GDPR data retention

# Impacto en Codebase
## Files Affected
- src/auth/controller.py (nuevo)
- src/auth/service.py (nuevo)
- src/auth/repository.py (nuevo)
- src/middleware/auth.py (modificar)
- src/models/user.py (modificar)

## Patterns to Follow
- Repository pattern (existente en src/*/repository.py)
- Dependency injection (existente en src/container.py)
- Domain events (existente en src/events/)

# Definition of Done
- [ ] Tests unitarios: coverage > 90%
- [ ] Tests de integración: login/logout flow
- [ ] Tests E2E: API endpoints
- [ ] Documentación API (OpenAPI/Swagger)
- [ ] Code review aprobado
- [ ] Performance test: < 200ms p99
```

### 2.2 /plan-task — Refinar Especificación

```bash
# Analizar y refinar la especificación
/plan-task .specs/tasks/draft/auth-system.feature.md

# Output: .specs/tasks/todo/auth-system.feature.md (movido a todo)
```

**Fases del planning (ejecutadas por sub-agents especializados):**

```
Phase 1: Research & Analysis
  └── researcher-agent: Tecnologías disponibles, dependencias, best practices
  └── code-explorer-agent: Análisis de codebase, patrones existentes, impacto
  └── business-analyst-agent: Requisitos, stakeholders, edge cases

Phase 2: Architecture Design
  └── software-architect-agent: Diseño de componentes, interfaces, data flow
  └── tech-lead-agent: Decomposición de tareas, dependencias, riesgos

Phase 3: Execution Planning
  └── team-lead-agent: Asignación de agents, paralelización, timeline
  └── qa-engineer-agent: Rúbricas de verificación, quality gates, tests

Phase 4: Quality Gate
  └── judge-agent: Evaluación de especificación vs. criterios de calidad
  └── Si falla: iteración con feedback; Si pasa: mover a /todo
```

**Rúbricas de evaluación (LLM-as-Judge):**
| Criterio | Peso | Descripción |
|----------|------|-------------|
| Completeness | 25% | Todos los requisitos cubiertos |
| Clarity | 20% | Instrucciones unambiguous |
| Feasibility | 20% | Implementable con recursos disponibles |
| Testability | 15% | Criterios de aceptación verificables |
| Maintainability | 20% | Diseño extensible y documentado |

### 2.3 /implement-task — Implementar desde Especificación

```bash
# Implementar la tarea especificada
/implement-task .specs/tasks/todo/auth-system.feature.md

# Output: Código implementado + .specs/tasks/done/auth-system.feature.md
```

**Fases de implementación:**

```
Phase 1: Setup
  └── developer-agent: Leer especificación, preparar entorno
  └── code-explorer-agent: Re-analizar codebase para contexto actualizado

Phase 2: Implementation
  └── developer-agent: Implementar siguiendo especificación y patrones existentes
  └── TDD: Tests primero, luego implementación (si aplica)
  └── Continuous integration: Commit frecuentes con mensajes descriptivos

Phase 3: Self-Review
  └── code-reviewer-agent: Revisar contra especificación y quality rubrics
  └── Verificar: SOLID, DDD, Clean Architecture, security, performance
  └── Identificar: bugs, edge cases, missing tests, documentation gaps

Phase 4: Fix & Verify
  └── developer-agent: Corregir issues encontrados
  └── qa-engineer-agent: Ejecutar tests, verificar coverage, performance
  └── Si falla: iteración; Si pasa: mover a /done

Phase 5: Documentation
  └── tech-writer-agent: Actualizar docs, ADRs, API specs, runbooks
  └── Generar: CHANGELOG, migration guides, deployment notes
```

## 3. Estructura de Directorios SDD

```
.specs/
├── tasks/
│   ├── draft/          # Especificaciones en desarrollo
│   ├── todo/           # Especificaciones listas para implementar
│   ├── in-progress/    # Especificaciones en implementación
│   ├── review/         # Especificaciones en code review
│   └── done/           # Especificaciones implementadas y verificadas
├── issues/             # Issues de GitHub analizados y convertidos a specs
│   └── 007-make-code-review-trigger-on-sql-sh-changes.specs.md
├── skills/             # Skills generadas automáticamente por tarea
│   └── auth-system/
│       ├── jwt-validation.md
│       ├── refresh-token-rotation.md
│       └── rate-limiting.md
├── rubrics/            # Rúbricas de calidad por dominio
│   ├── security.md
│   ├── performance.md
│   └── maintainability.md
└── memory/               # Insights memorizados de reflexiones previas
    └── lessons-learned.md
```

## 4. Patrones de Razonamiento Estructurado

### 4.1 Chain of Thought (CoT)
- Zero-shot: "Piensa paso a paso"
- Few-shot: Ejemplos de razonamiento previo en contexto
- Aplicado en: planning, debugging, análisis de impacto

### 4.2 Tree of Thoughts (ToT)
- Explorar múltiples soluciones en paralelo
- Evaluar cada rama con scoring
- Pruning de ramas prometedoras
- Aplicado en: diseño arquitectónico, selección de tecnología

### 4.3 Problem Decomposition
- Dividir problema complejo en sub-problemas independientes
- Resolver cada sub-problema con sub-agent dedicado
- Componer solución final
- Aplicado en: implementación de features complejas, refactoring

### 4.4 Self-Critique
- Evaluar propia solución antes de presentar
- Identificar debilidades, edge cases, optimizaciones
- Iterar hasta alcanzar umbral de calidad
- Aplicado en: code review, optimización de performance

## 5. Quality Gates (LLM-as-Judge)

### 5.1 Rúbricas por Fase

**Planning Gate:**
```yaml
criteria:
  - id: completeness
    weight: 25
    description: "Todos los requisitos funcionales y no-funcionales están definidos"
    threshold: 80
  - id: clarity
    weight: 20
    description: "Las instrucciones son unambiguous y verificables"
    threshold: 85
  - id: feasibility
    weight: 20
    description: "La implementación es viable con recursos y tecnologías actuales"
    threshold: 75
  - id: testability
    weight: 15
    description: "Criterios de aceptación son medibles y automatizables"
    threshold: 80
  - id: maintainability
    weight: 20
    description: "El diseño permite extensión y modificación futura"
    threshold: 75

min_total_score: 80
required_criteria: [completeness, clarity]
```

**Implementation Gate:**
```yaml
criteria:
  - id: correctness
    weight: 30
    description: "Código funciona según especificación, tests pasan"
    threshold: 95
  - id: code_quality
    weight: 25
    description: "SOLID, DDD, Clean Architecture, no code smells"
    threshold: 80
  - id: test_coverage
    weight: 20
    description: "Coverage > 80% lógica de negocio, tests meaningful"
    threshold: 80
  - id: security
    weight: 15
    description: "No vulnerabilities, secrets management, input validation"
    threshold: 90
  - id: performance
    weight: 10
    description: "Cumple requisitos de latencia y throughput"
    threshold: 75

min_total_score: 85
required_criteria: [correctness, code_quality, security]
```

### 5.2 Scoring
- Cada criterio: 0-100
- Peso aplicado: score * weight / 100
- Total: suma de scores ponderados
- Pass: total >= min_total_score AND todos los required_criteria >= threshold

## 6. Multi-Agent Orchestration

### 6.1 Context Isolation
- Cada sub-agent recibe solo el contexto necesario para su tarea
- Previene context rot (degradación por contexto excesivo)
- Comunicación via filesystem (archivos .md, .json) entre agents
- Memoria compartida: `.specs/memory/` para insights cross-task

### 6.2 Agent Roles

| Agent | Role | Tasks | Model |
|-------|------|-------|-------|
| researcher | Technology research | Dependencies, best practices, alternatives | Standard |
| code-explorer | Codebase analysis | Pattern identification, impact analysis | Standard |
| business-analyst | Requirements analysis | Stakeholders, edge cases, acceptance criteria | Standard |
| software-architect | Architecture design | Components, interfaces, data flow | Advanced |
| tech-lead | Task decomposition | Sub-tasks, dependencies, risk analysis | Advanced |
| team-lead | Execution planning | Agent assignment, parallelization | Standard |
| qa-engineer | Quality definition | Rubrics, test plans, verification | Standard |
| developer | Implementation | Code, tests, documentation | Advanced |
| code-reviewer | Code review | Quality check, bug hunting, optimization | Advanced |
| tech-writer | Documentation | Docs, ADRs, API specs, runbooks | Standard |

### 6.3 MAKER Pattern (Million-Step Reliability)
- Clean-state agent launches: Cada sub-agent inicia con contexto limpio
- Filesystem-based memory: Persistencia entre sesiones
- Multi-agent voting: Decisiones críticas con consenso de múltiples agents
- Checkpointing: Guardar estado cada N pasos para recovery

## 7. Continuous Learning

### 7.1 /memorize — Curar Insights
```bash
# Después de reflexión o corrección, memorizar insights
/memorize

# Output: Actualización de .specs/memory/lessons-learned.md
```

**Formato de memoria:**
```yaml
---
date: 2026-06-19
task: AUTH-001
category: security
---

## Lesson Learned
JWT refresh tokens deben rotarse en cada uso (refresh token rotation)
para prevenir replay attacks.

## Context
Durante implementación de auth system, se identificó que reutilizar
refresh tokens compromete seguridad si el token es robado.

## Solution
Implementar refresh token rotation: cada uso genera nuevo refresh token,
invalida el anterior. Mantener familia de tokens para detectar reuse.

## Prevention
Añadir regla a security rubric: "Refresh tokens MUST implement rotation"
```

### 7.2 Skills Auto-Generadas
- Después de cada tarea compleja, extraer skills reutilizables
- Guardar en `.specs/skills/{task-name}/`
- Incluir: contexto, problema, solución, código de ejemplo, tests
- Reutilizar en tareas futuras similares

## 8. Anti-patrones SDD (Qué NO hacer)

- **Vague specifications**: Requisitos ambiguos o incompletos
- **Over-specification**: Especificar detalles de implementación (cómo) en lugar de comportamiento (qué)
- **Skipping planning**: Ir directo a implementación sin especificación
- **Ignoring codebase context**: No analizar patrones existentes antes de implementar
- **No verification**: No ejecutar quality gates después de implementación
- **No documentation**: Omitir documentación de decisiones y APIs
- **Big bang tasks**: Tareas demasiado grandes (> 20 archivos cambiados); descomponer
- **Ignoring feedback**: No iterar cuando quality gate falla

## 9. Integración con otras Skills APB

- **SKILL_DEV_CODE_BASE**: Reglas de calidad de código (SOLID, DDD) aplicadas en implementación
- **SKILL_DEV_MICRO_BASE**: Especificación de servicios en arquitecturas de microservicios
- **SKILL_DEV_AUTOCORRECT**: Reflexión y auto-corrección durante implementación
- **SKILL_DEV_REVIEW_TL**: Code review por tech lead como quality gate adicional
- **SKILL_DEV_REVIEW_ADVANCED**: Análisis estático y security review
- **SKILL_ARCH_DESIGN**: Diseño arquitectónico previo a especificación
- **SKILL_OPS_OBSERVABILITY**: Métricas y observabilidad en definition of done

## 10. Referencias

- [NeoLabHQ/context-engineering-kit - SDD Plugin](https://github.com/NeoLabHQ/context-engineering-kit)
- [arc42 Specification Standard](https://arc42.org/)
- [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651)
- [Reflexion: Self-Reflective Agents](https://arxiv.org/abs/2303.11366)
- [Agentic Context Engineering](https://arxiv.org/abs/2502.14757)
- [Solving a Million-Step LLM Task with Zero Errors (MAKER)](https://arxiv.org/abs/2506.05706)
- [Chain of Thought Prompting](https://arxiv.org/abs/2201.11903)
- [Tree of Thoughts](https://arxiv.org/abs/2305.10601)
