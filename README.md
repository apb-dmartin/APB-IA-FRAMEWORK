# APB AI Framework

Repositorio corporativo de la **Autoridad Portuaria de Barcelona (APB)** para desarrollo asistido por Inteligencia Artificial.

## Visión

Construir una plataforma corporativa de conocimiento, capacidades y automatización asistida por IA, reutilizable por distintos LLM y herramientas, orientada a:

- **Spec Driven Development (SDD)** para nuevos desarrollos.
- **Modernización de legacy** para los ~550 repositorios existentes.
- **QA, arquitectura, cloud, operación, evidencias y gobierno** transversales.

## Principios Fundamentales

| # | Principio | Descripción |
|---|-----------|-------------|
| 1 | **Agnóstico al LLM** | El framework no depende de Claude, GPT, Gemini ni Kimi. Los modelos son reemplazables mediante adaptadores. |
| 2 | **Runtime inicial: GitHub Copilot** | Preparado para Claude, OpenAI y Gemini mediante adaptadores en `adapters/`. |
| 3 | **Responsabilidad humana** | La IA propone, estructura y automatiza; la responsabilidad final siempre es humana. |
| 4 | **Fuente de verdad técnica: Git** | Specs, ADRs, código, tests y evidencias viven en Git. |
| 5 | **Fuente de verdad funcional: Jira** | Épicas, historias, bugs, priorización y Acceptance Criteria iniciales. |
| 6 | **Confluence como proyección** | No es fuente maestra. |
| 7 | **Estado como metadato** | Nunca forma parte de la estructura de carpetas. |
| 8 | **No vibe coding** | Toda generación de código parte de spec, plan técnico, issue Jira o hallazgo documentado. |
| 9 | **Secretos en Azure Key Vault** | Nunca en prompts, skills ni catálogos. |
| 10 | **Reutilización antes que creación** | No se crea una skill APB sin discovery previo de alternativas oficiales y de comunidad. |
| 11 | **Disciplina de codificación agéntica** *(Sesión 10)* | Todo componente que genere código sigue 4 reglas: pensar antes de codificar (señalar ambigüedad, no asumir en silencio); simplicidad ante todo (código mínimo, sin abstracciones no solicitadas); cambios quirúrgicos (tocar solo lo que el cambio requiere, no "mejorar" código adyacente); ejecución dirigida a objetivos (criterio de éxito verificable, no instrucción imperativa vaga). Extiende el Principio #8 (No vibe coding) con disciplina operativa concreta. Origen: `multica-ai/andrej-karpathy-skills` (MIT), adaptado por APB. |
| 12 | **Normalización a Markdown** *(Sesión 10)* | Todo adjunto ofimático (Word, Excel, PowerPoint, PDF) que se pase como input a un agente, skill o subagente se normaliza a Markdown antes de ser consumido. El componente trabaja internamente en Markdown por eficiencia, aunque el usuario aporte el archivo en su formato original. |

## Jerarquía de Componentes

```
Capability
 ↓
Provider (Knowledge | Action | Secret)
 ↓
Wrapper (APB sobre componente de terceros)
 ↓
Skill (reutilizable, con inputs/outputs definidos)
 ↓
Subagent (especialización de un agente)
 ↓
Agent (rol con responsabilidades, skills y límites)
 ↓
Workflow (orquestación de agentes para un objetivo de negocio)
```

> **Nota de arranque:** Para el inicio del framework, los niveles de Capability, Provider y Wrapper son opcionales. Se comienza con Skill → Agent → Workflow, evolucionando hacia la jerarquía completa.

## Niveles de Autonomía

| Nivel | Descripción | Ejemplos de uso |
|-------|-------------|-----------------|
| **Nivel 0** | Asistencia y recomendaciones. | Sugerencias de mejora de código, análisis de arquitectura. |
| **Nivel 1** | Generación de artefactos con revisión humana obligatoria. | Generación de specs, código, planes de pruebas. **(Nivel por defecto)** |
| **Nivel 2** | Cambios en documentación/spec/código mediante PR. | Actualización automática de specs tras merge, refactorización guiada. |
| **Nivel 3** | Actualización de Jira/GitHub con aprobación explícita. | Registro de evidencias, sincronización de estado de issues. |
| **Nivel 4** | Automatización controlada de bajo riesgo previamente autorizada. | Ejecución de tests de regresión, generación de datos sintéticos. |

> **Regla de oro:** Las actividades de análisis, arquitectura, seguridad, despliegue en producción y gobierno operan como mínimo en **Nivel 1**.

## Estados de Componentes

| Estado | Significado |
|--------|-------------|
| `draft` | Definido, no aprobado. Estado por defecto. |
| `candidate` | Apto para piloto controlado. |
| `under_review` | En revisión formal. |
| `approved` | Aprobado por responsables humanos. |
| `deprecated` | Sustituido, no recomendado para nuevos usos. |
| `retired` | Retirado. |
| `watchlist` | Observado, no consumible hasta nueva evaluación. |
| `rejected` | Descartado. |

## Tecnología Soportada

| Ámbito | Tecnología / Estándar |
|--------|----------------------|
| Backend principal | .NET y C# |
| Frontend corporativo | DevExpress / DevExtreme (JavaScript predominante, Blazor en casos específicos) |
| APIs y servicios web | .NET (REST); Django / Django REST Framework / GeoDjango (GIS) |
| Bases de datos | Azure SQL Database (principal); Cosmos DB (justificado); PostgreSQL/PostGIS (geoespacial) |
| Mensajería e integración | Azure Service Bus (Avro/JSON) |
| CI/CD | Jenkins o GitHub Actions (detección automática) |
| Secretos | Azure Key Vault |

## Cómo Empezar

### Para repos existentes sin specs (Legacy Onboarding)

```bash
# 1. Clonar este repo o referenciarlo como submodule
git submodule add https://github.com/apb-dmartin/APB-IA-FRAMEWORK.git .apb-ai

# 2. Ejecutar el workflow de legacy onboarding
cd .apb-ai/workflows/legacy-onboarding
# Seguir WORKFLOW.md

# 3. Validar la estructura generada
python scripts/validate_repo.py --path /ruta/al/repo/legacy
```

### Para nuevos proyectos (SDD-Ready)

```bash
# 1. Copiar el scaffold SDD-ready
cp -r repo-scaffold/sdd-ready/* /ruta/al/nuevo-repo/

# 2. Inicializar el spec
cd /ruta/al/nuevo-repo
# Seguir docs/sdd-getting-started.md
```

### Para usar agentes de forma independiente

```bash
# Invocar un agente individual sin workflow completo
# Ejemplo: revisión de código .NET
python scripts/invoke_agent.py --agent code-reviewer --path ./src --output ./review.md
```

## Estructura del Repositorio

```
apb-ai-framework/
├── README.md                    # Este archivo
├── SYSTEM.md                    # Fuente raíz del comportamiento del framework
├── GOVERNANCE.md                # Reglas de gobierno, estados y aprobadores
├── CONTRIBUTING.md              # Guía de contribución
├── LICENSE.md                   # Licencia interna APB
│
├── capabilities/                # Capacidades de negocio (opcional en arranque)
│
├── providers/                   # Proveedores de conocimiento, acción y secretos
│   ├── knowledge/             # Microsoft Learn, DevExpress, Knowledge APB
│   ├── action/                # GitHub, Playwright, Azure, Sonar, Atlassian
│   └── secret/                # Azure Key Vault
│
├── wrappers/                  # Wrappers APB sobre componentes de terceros
│
├── skills/                    # Skills reutilizables
│   ├── apb-owned/             # Skills propias de APB
│   │   ├── discovery/         # Ingeniería inversa, business discovery
│   │   ├── architecture/      # DDD, diseño de APIs, cloud
│   │   ├── development/       # Generación de código, refactorización
│   │   ├── qa/                # Testing, datos de prueba, evidencias
│   │   ├── platform/          # CI/CD, Docker, Terraform
│   │   ├── operation/         # Observabilidad, SLO, runbooks
│   │   ├── governance/        # Cumplimiento, estándares, catálogo
│   │   ├── security/          # Threat modeling, análisis forense, riesgos
│   │   └── documentation/     # Generación de docs, ADRs, evidencias
│   └── third-party/           # Skills de terceros (descriptores, no copias)
│       ├── anthropic/
│       ├── skills-sh/
│       ├── composio/
│       └── openspec/
│
├── subagents/                 # Especializaciones de agentes
│
├── agents/                    # Agentes principales del framework
│
├── workflows/                 # Orquestaciones de agentes
│   ├── legacy-onboarding/
│   ├── spec-driven-development/
│   ├── qa-evidence/
│   ├── cloud-migration/
│   └── risk-exception/
│
├── context/apb/               # Contexto corporativo APB
│   ├── standards/             # Estándares de arquitectura, desarrollo, QA
│   ├── templates/             # Plantillas de código, specs, ADRs
│   └── policies/              # Políticas de seguridad, IA, calidad
│
├── discovery/                 # Evidencias de discovery de alternativas
│
├── catalog/                   # Catálogo centralizado de skills, agentes y prompts
│
├── scripts/                   # Scripts de utilidad y validación
│
├── repo-scaffold/             # Plantillas para nuevos repos
│   ├── sdd-ready/
│   └── legacy-ready/
│
├── docs/                      # Documentación del framework
│
├── examples/                  # Ejemplos funcionales
│   ├── dotnet-review/
│   └── spec-generation/
│
├── adapters/                  # Adaptadores para distintos runtimes de IA
│   ├── copilot/
│   └── claude/
│
└── tests/                     # Tests del framework mismo
```

## Catálogo de Componentes

Consultar `catalog/CATALOG.md` para el listado completo de skills, agentes, subagentes y workflows con sus metadatos, estados y dependencias.

## Contribución

Ver `CONTRIBUTING.md`. Antes de crear una skill APB, debe existir evidencia en `discovery/` de revisión de alternativas.

## Estado Actual

> **⚠️ Todos los componentes están en estado `draft`.**
>
> Este repositorio está preparado para iniciar pilotos controlados. No debe usarse en producción sin revisión y aprobación explícita de Arquitectura, QA, Ciberseguridad y Gobierno de APB.

## Contacto

- **Arquitectura APB:** arquitectura@portdebarcelona.cat
- **QA:** arquitectura@portdebarcelona.cat
- **Ciberseguridad:** albert.prats@portdebarcelona.cat
