# APB AI Framework — Adaptación de Skills

## Resumen Ejecutivo

| Métrica | Valor |
|---------|-------|
| **Skills adaptados/generados** | 8 |
| **Skills existentes corregidos** | 6 (revisados en análisis previo) |
| **Skills restantes por adaptar** | 38 |
| **Fuentes principales** | Superpowers (obra), BMAD Method, wshobson/agents, Anthropic Skills |
| **Licencias** | MIT (todas las fuentes) |

## Skills Generados en Esta Sesión

### 1. `apb-brainstorming`
- **Fuente:** Superpowers (brainstorming) + BMAD (analysis-phase)
- **Adaptación:** Enriquecido con preguntas obligatorias de event-driven (eventos, schemas, idempotencia, compensación, DLQ)
- **Solapamiento resuelto:** ✅ Mantiene estructura de Superpowers, añade contexto específico APB

### 2. `apb-planning`
- **Fuente:** Superpowers (writing-plans) + BMAD (planning workflows)
- **Adaptación:** Plantilla de tarea específica para event-driven (evento, topic, subscription, schema, idempotencia, compensación, DLQ)
- **Solapamiento resuelto:** ✅ Refactorizado con estructura de Spec Kit + BMAD, adaptado a Azure Service Bus

### 3. `apb-tdd`
- **Fuente:** Superpowers (test-driven-development) + wshobson/agents (tdd-workflows)
- **Adaptación:** Añadido testing específico de eventos (productor, consumidor, idempotencia, saga, DLQ)
- **Solapamiento resuelto:** ✅ Mantiene ciclo red-green-refactor, añade anti-patrón "mock-itis" en event-driven

### 4. `apb-code-review`
- **Fuente:** Superpowers (requesting-code-review + receiving-code-review)
- **Adaptación:** Proceso de dos etapas con verificaciones específicas de event-driven (schemas CloudEvents, contratos, idempotencia, compensación, DLQ, ordenamiento)
- **Solapamiento resuelto:** ✅ Adoptado two-stage review de Superpowers, añadida validación de contratos CloudEvents

### 5. `apb-subagent-dev`
- **Fuente:** Superpowers (subagent-driven-development) + wshobson/agents (task-coordination + parallel-feature-development)
- **Adaptación:** Prompt de implementador con restricciones de event-driven, soporte para despacho paralelo
- **Solapamiento resuelto:** ✅ Nuevo skill que combina orquestación de Superpowers con coordinación de wshobson

### 6. `apb-event-driven` ⭐ NUEVO
- **Fuente:** Creado desde cero + adaptado de wshobson/agents (microservices-patterns, saga-orchestration, cqrs-implementation, event-store-design)
- **Adaptación:** Skill maestro con 9 patrones fundamentales de event-driven architecture
- **Solapamiento resuelto:** ✅ N/A — skill nuevo, no existía equivalente

### 7. `apb-verification`
- **Fuente:** Superpowers (verification-before-completion)
- **Adaptación:** Añadidas verificaciones de infraestructura de eventos (Service Bus, DLQ, schemas, idempotencia, saga)
- **Solapamiento resuelto:** ✅ Mantiene "evidence before claims", añade comandos específicos de Azure

### 8. `apb-deployment`
- **Fuente:** Superpowers (finishing-a-development-branch) + wshobson/agents (deployment-strategies)
- **Adaptación:** Health checks, rolling updates, verificación post-deploy, rollback strategy para microservicios
- **Solapamiento resuelto:** ✅ Añadido despliegue independiente de microservicios con verificación de eventos

## Mapeo de Skills del APB AI Framework

```
APB AI Framework (103 componentes, 18 agentes, 7 workflows)
│
├── Skills Adaptados (8/46 restantes)
│   ├── apb-brainstorming ← Superpowers + BMAD
│   ├── apb-planning ← Superpowers + BMAD
│   ├── apb-tdd ← Superpowers + wshobson
│   ├── apb-code-review ← Superpowers (2 skills mergeados)
│   ├── apb-subagent-dev ← Superpowers + wshobson
│   ├── apb-event-driven ← wshobson (4 skills mergeados) + creado
│   ├── apb-verification ← Superpowers
│   └── apb-deployment ← Superpowers + wshobson
│
├── Skills Existentes Corregidos (6/6)
│   ├── apb-brainstorming ✅ (enriquecido)
│   ├── apb-planning 🔧 (refactorizado)
│   ├── apb-tdd ✅ (enriquecido)
│   ├── apb-code-review 🔧 (refactorizado)
│   ├── apb-deployment ✅ (enriquecido)
│   └── apb-documentation 🔧 (refactorizado)
│
└── Skills Restantes (38/46)
    ├── Grupo A: Adaptar desde Superpowers (5 skills)
    │   ├── apb-design-approval
│   ├── apb-task-breakdown
│   ├── apb-implementation-patterns
│   ├── apb-refactoring
│   └── apb-testing-strategy
│   ├── Grupo B: Adaptar desde BMAD (6 skills)
│   │   ├── apb-pm-analysis
│   │   ├── apb-architecture-design
│   │   ├── apb-readiness-check
│   │   ├── apb-qa-validation
│   │   ├── apb-sprint-planning
│   │   └── apb-retrospective
│   ├── Grupo C: Adaptar desde Anthropic Skills (4 skills)
│   │   ├── apb-mcp-building
│   │   ├── apb-frontend-integration
│   │   ├── apb-document-processing
│   │   └── apb-api-design
│   ├── Grupo D: Adaptar desde wshobson/agents (3 skills)
│   │   ├── apb-multi-agent-orchestration
│   │   ├── apb-parallel-execution
│   │   └── apb-slash-commands
│   └── Grupo E: Crear desde cero (20 skills)
│       ├── apb-event-schema-design
│       ├── apb-service-bus-topology
│       ├── apb-event-publishing
│       ├── apb-event-consumption
│       ├── apb-saga-orchestration
│       ├── apb-dead-letter-handling
│       ├── apb-message-duplication
│       ├── apb-session-management
│       ├── apb-event-versioning
│       ├── apb-asyncapi-generation
│       ├── apb-devops-pipeline
│       ├── apb-observability
│       ├── apb-service-discovery
│       ├── apb-circuit-breaker
│       ├── apb-event-sourcing
│       ├── apb-cqrs-implementation
│       ├── apb-api-gateway-events
│       ├── apb-security-events
│       ├── apb-performance-tuning
│       ├── apb-disaster-recovery
│       └── apb-cost-optimization
```

## Stack Tecnológico Confirmado

| Capa | Tecnología | Justificación |
|------|-----------|---------------|
| **Broker** | Azure Service Bus | Elección del usuario, enterprise-grade |
| **Schemas** | JSON + CloudEvents 1.0 | Elección del usuario, interoperable |
| **UI** | DevExpress + JavaScript puro | Elección del usuario, no React/TypeScript |
| **Patrón** | Event-driven microservices | Arquitectura del framework |

## Consideraciones de Seguridad

- ✅ Todos los skills auditados: sin shell access arbitrario
- ✅ Sin prompt injection detectado en código adaptado
- ✅ Sin dependencias maliciosas (solo repositorios oficiales)
- ✅ Licencias verificadas: MIT (todas las fuentes)

## Próximos Pasos

1. **Semana 1:** Completar Grupo A (Superpowers) — 5 skills
2. **Semana 2:** Completar Grupo B (BMAD) — 6 skills
3. **Semana 3:** Completar Grupo C (Anthropic) — 4 skills
4. **Semana 4:** Completar Grupo D (wshobson) — 3 skills
5. **Semanas 5-6:** Crear Grupo E desde cero — 20 skills
6. **Semana 7:** Validación completa con los 18 agentes del framework



## Grupo A Completado (5 skills)

| # | Skill | Fuente | Estado | Tamaño |
|---|-------|--------|--------|--------|
| A1 | `apb-design-approval` | Superpowers (brainstorming gate) | ✅ Adaptado | 4,786 bytes |
| A2 | `apb-task-breakdown` | Superpowers (task decomposition) + wshobson | ✅ Adaptado | 5,710 bytes |
| A3 | `apb-implementation-patterns` | Superpowers + wshobson (microservices-patterns) | ✅ Adaptado | 16,732 bytes |
| A4 | `apb-refactoring` | Superpowers + wshobson (code-refactoring) | ✅ Adaptado | 9,750 bytes |
| A5 | `apb-testing-strategy` | Superpowers + wshobson (testing) | ✅ Adaptado | 12,807 bytes |

### Skills del Grupo A: Resumen de Adaptaciones

**A1 - Design Approval:**
- Gate estructurado entre brainstorming y planning
- Checklist de 18 ítems (10 específicos de event-driven + 8 generales)
- Revisión por subagente con verificaciones de arquitectura de eventos

**A2 - Task Breakdown:**
- 3 estrategias de descomposición: por evento, por capa, por patrón
- Reglas de dependencia entre tareas (schemas primero, infraestructura primero)
- Plantilla de sub-tarea con campos de event-driven

**A3 - Implementation Patterns:**
- 6 patrones con código JavaScript real:
  1. Event Producer (outbox pattern)
  2. Event Consumer (idempotencia + DLQ)
  3. Saga Orchestrator (compensaciones)
  4. Circuit Breaker (resiliencia)
  5. Read Model Projection (CQRS)
  6. DevExpress Event Grid (UI)
- Anti-patrones específicos de event-driven

**A4 - Refactoring:**
- 5 tipos de refactorización:
  1. Handlers (pipeline de procesamiento)
  2. Schemas (expand-contract)
  3. Sagas (pasos declarativos)
  4. Topología Service Bus (topics por dominio)
  5. DevExpress UI (separación de concerns)
- Checklist de refactorización segura

**A5 - Testing Strategy:**
- Pirámide de tests APB (60% unit, 20% contract, 15% integration, 5% E2E)
- Código real para cada nivel de test
- Tests específicos: idempotencia, ordenamiento, performance
- Configuración CI/CD con Service Bus Emulator
- Métricas de calidad de tests

---
*Actualizado: 2026-06-20 — Grupo A completado*



## Grupo B Completado (6 skills)

| # | Skill | Fuente | Estado | Tamaño |
|---|-------|--------|--------|--------|
| B1 | `apb-pm-analysis` | BMAD (agent-analyst + product-brief + prfaq) | ✅ Adaptado | 6,335 bytes |
| B2 | `apb-architecture-design` | BMAD (agent-architect + create-architecture) | ✅ Adaptado | 10,245 bytes |
| B3 | `apb-readiness-check` | BMAD (check-implementation-readiness) | ✅ Adaptado | 6,908 bytes |
| B4 | `apb-qa-validation` | BMAD (qa-generate-e2e-tests) | ✅ Adaptado | 8,856 bytes |
| B5 | `apb-sprint-planning` | BMAD (sprint-planning) | ✅ Adaptado | 6,966 bytes |
| B6 | `apb-retrospective` | BMAD (retrospective) | ✅ Adaptado | 6,386 bytes |

### Skills del Grupo B: Resumen de Adaptaciones

**B1 - PM Analysis:**
- Fase de descubrimiento con mapeo de eventos de negocio
- Bounded contexts identificados desde el análisis
- PRFAQ adaptado con FAQ específicos de event-driven
- Requisitos funcionales con perspectiva de eventos (productor/consumidor)

**B2 - Architecture Design:**
- Topología de Azure Service Bus documentada con decisiones
- 3 patrones arquitectónicos: comunicación, saga, consistencia
- Decisiones de stack con justificación (Service Bus, CloudEvents, DevExpress)
- Documento de arquitectura con diagramas Mermaid, ADRs, DR

**B3 - Readiness Check:**
- Inventario de 8 artefactos obligatorios
- Verificación de trazabilidad entre artefactos
- Checklist de 10 ítems específicos de event-driven
- Grafo de dependencias entre artefactos

**B4 - QA Validation:**
- Tests E2E con código JavaScript real para Azure Service Bus
- 6 tipos de tests: happy path, idempotencia, compensación, DLQ, performance, ordenamiento
- Plantilla completa con EventMonitor helper
- Reporte de QA con cobertura de eventos

**B5 - Sprint Planning:**
- Stories organizadas por eventos y servicios
- Grafo de dependencias entre productores y consumidores
- Sprint board visualizado como flujo de eventos
- Definition of Done específica de event-driven

**B6 - Retrospective:**
- Métricas de eventos (volumen, latencia, sagas, throughput)
- Lecciones arquitectónicas sobre topología, patrones, observabilidad
- Acciones de mejora con ajustes arquitectónicos propuestos
- Documento de retrospectiva con baseline para próximo epic

---
*Actualizado: 2026-06-20 — Grupos A y B completados*



## Grupo C Completado (4 skills)

| # | Skill | Fuente | Estado | Tamaño |
|---|-------|--------|--------|--------|
| C1 | `apb-mcp-building` | Anthropic (mcp-builder) | ✅ Adaptado | 9,513 bytes |
| C2 | `apb-frontend-integration` | Anthropic (frontend-design + web-artifacts-builder) | ✅ Adaptado | 12,216 bytes |
| C3 | `apb-document-processing` | Anthropic (docx + pdf) | ✅ Adaptado | 12,504 bytes |
| C4 | `apb-api-design` | Anthropic (claude-api + frontend-design) | ✅ Adaptado | 13,494 bytes |

### Skills del Grupo C: Resumen de Adaptaciones

**C1 - MCP Building:**
- 3 MCP servers especializados: Event Monitor, Saga Controller, Schema Validator
- Herramientas con código TypeScript real para Azure Service Bus
- Naming convention: `apb_[dominio]_[accion]_[objeto]`
- Error messages con contexto y sugerencias

**C2 - Frontend Integration:**
- DevExpress + JavaScript puro (no React, no TypeScript)
- 3 componentes: EventMonitorDashboard, SagaVisualizer, DLQManager
- Código real con dxDataGrid, dxChart, dxDiagram, dxTileView
- Anti-patrón "AI slop" específico para dashboards de eventos

**C3 - Document Processing:**
- 4 generadores: AsyncAPI DOCX, Event Catalog DOCX, Architecture Report PDF, Operations Manual DOCX
- Código JavaScript real con docx-js y puppeteer
- Plantilla de spec de evento con metadata, schema, example, business rules

**C4 - API Design:**
- OpenAPI 3.0.3 para APIs REST (comandos + queries CQRS)
- AsyncAPI 2.6.0 para contratos de eventos
- Naming convention de eventos: `[empresa].[dominio].[accion].v[version]`
- Versionado de APIs con estrategia de deprecación

---
*Actualizado: 2026-06-20 — Grupos A, B y C completados*



## Grupo D Completado (3 skills)

| # | Skill | Fuente | Estado | Tamaño |
|---|-------|--------|--------|--------|
| D1 | `apb-multi-agent-orchestration` | wshobson/agents (task-coordination + context-driven-dev + track-management) | ✅ Adaptado | 8,467 bytes |
| D2 | `apb-parallel-execution` | wshobson/agents (parallel-feature-development + task-coordination) | ✅ Adaptado | 8,316 bytes |
| D3 | `apb-slash-commands` | wshobson/agents (workflow-patterns + track-management) | ✅ Adaptado | 6,192 bytes |

### Skills del Grupo D: Resumen de Adaptaciones

**D1 - Multi-Agent Orchestration:**
- 18 agentes del APB con roles especializados (PM, Architect, Dev, QA, Ops, Event, Schema, Saga, DLQ, Monitor)
- Artefactos de contexto compartidos (Conductor directory)
- Handoffs estructurados entre fases con checklists
- Track lifecycle completo (CREATED → SPECIFIED → PLANNED → IN_PROGRESS → VERIFYING → COMPLETED)
- Resolución de conflictos entre agentes

**D2 - Parallel Execution:**
- 3 estrategias de file ownership: por servicio, por evento, por capa (vertical slice)
- Contratos de interfaz: schema de evento (frozen) + API REST
- Proceso de ejecución paralela con timeline visual
- Reglas de independencia basadas en topología de Service Bus
- Métricas de paralelismo (speedup, conflictos, re-trabajo)

**D3 - Slash Commands:**
- 9 comandos: /apb:brainstorm, /apb:plan, /apb:implement, /apb:review, /apb:verify, /apb:deploy, /apb:retro, /apb:status, /apb:help
- Mapeo de comandos a skills principales y secundarios
- Alias cortos para productividad
- Workflows completos por comando

---
*Actualizado: 2026-06-20 — Grupos A, B, C y D completados*

---
*Documento generado: 2026-06-20*
*APB AI Framework — Adaptación de Skills v1.0*
