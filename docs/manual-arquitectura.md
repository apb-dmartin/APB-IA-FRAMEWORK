# Manual de Arquitectura — APB AI Framework

> **Audiencia:** Arquitectos de sistemas, Technical Leads, responsables de gobierno TI.
> **Versión analizada:** 1.0.0-draft (estado al 26 de junio de 2026, commit más reciente)
> **Repositorios analizados:**
> - `APB-IA-FRAMEWORK` (repositorio principal)
> - `APB-DOMAIN-CATALOG` (submódulo: `domain-catalog/`)
> - `APB-DESIGN-SYSTEM` (submódulo: `design-system/`)

---

## 1. Mapa técnico de componentes

### 1.1 Jerarquía de componentes

El framework define una jerarquía de 7 niveles. El nivel superior (Capability) es opcional en la fase actual de arranque; los tres niveles operativos obligatorios son Skill, Agent y Workflow.

```
CAPABILITY          (opcional en arranque — capa de negocio, no implementada aún)
      ↓
PROVIDER            (14 instancias — fuentes de conocimiento y acción)
      ↓
WRAPPER             (7 instancias — adaptación APB sobre terceros)
      ↓
SKILL               (129 APB-owned + 51 third-party — unidades atómicas reutilizables)
      ↓
SUBAGENT            (23 instancias — especializaciones por tecnología/contexto)
      ↓
AGENT               (26 instancias — roles con responsabilidades y límites)
      ↓
WORKFLOW            (8 instancias — orquestación de agentes para objetivos de negocio)
```

**Total de componentes catalogados:** 262 (incluyendo 4 adaptadores, sin contar contexto y políticas corporativas).

### 1.2 Inventario por capa

**Skills APB-owned por dominio (129):**

| Dominio | Cantidad | Prefijo |
|---------|----------|---------|
| Development | 27 | `apb-dev-*` |
| QA | 14 | `apb-qa-*` |
| Architecture | 13 | `apb-arch-*` |
| Operation | 13 | `apb-ops-*` |
| Discovery | 12 | `apb-disc-*` |
| Governance | 12 | `apb-gov-*` |
| Platform | 12 | `apb-plat-*` |
| Project Management | 8 | `apb-pm-*` |
| Security | 8 | `apb-sec-*` |
| Documentation | 7 | `apb-doc-*` |
| Design | 2 | `apb-design-*` |
| Orchestration | 1 | `apb-orch-*` |

**Providers (14):** Azure, Azure Monitor, Azure Key Vault, Atlassian, GitHub, Playwright, SonarQube, MS365, DevExpress, k6, APB Knowledge, MS Learn, Base Architecture APB, API Base Architecture APB.

**Wrappers (7):** LightRAG (knowledge graph), Composio, Mukul Cyber, OpenSpec, Skills.sh, Anthropic Skills, MemoryWrapper.

**Adaptadores (4):** Claude (Anthropic), GitHub Copilot, Atlassian Rovo, M365 Copilot.

**Submódulos Git:**
- `domain-catalog/` → `APB-DOMAIN-CATALOG` (estructura lista, sin dominios creados aún)
- `design-system/` → `APB-DESIGN-SYSTEM` (tokens CSS verificados, tipografía pendiente, catálogo de componentes parcial)

### 1.3 Infraestructura de gobierno y validación

El framework incluye tres scripts operativos en `scripts/`:

- **`validate_repo.py`**: validador de integridad del repositorio. Valida frontmatter YAML, IDs, formato, estados, dominios, nivel de autonomía, secretos hardcodeados, IPs internas, referencias cruzadas entre componentes, coherencia agente↔subagente, dependencias circulares y marcado IA obligatorio. Tiene modo `--strict` que bloquea PRs en CI para cualquier error o warning (excepto `source_commit: "unverified"`, que es un warning deliberado de gobernanza).
- **`generate_catalog.py`**: regenera automáticamente `CATALOG.md`, `INDEX.md` y `DOMAIN_REGISTRY.md` a partir del frontmatter real de cada componente. Nunca se editan estos archivos manualmente.
- **`invoke_agent.py`**: simulador de invocación de agentes para pruebas locales. **No ejecuta el agente real** — lee el frontmatter del agente y muestra sus metadatos. La ejecución real ocurre en el runtime (Claude o Copilot).
- **`emit_telemetry.py`**: emite eventos de telemetría al log local (`telemetry/events.jsonl`) y a Azure Monitor (tabla `APBFrameworkTelemetry_CL`).

**CI/CD:** dos workflows de GitHub Actions:
- `.github/workflows/validate.yml`: ejecuta `validate_repo.py --strict` en cada PR. Bloquea el merge ante cualquier error. Sin auto-commit ni push automático.
- `.github/workflows/telemetry.yml`: emite telemetría de invocación al pipeline.

### 1.4 Esquema de metadatos (SCHEMA.md)

Todos los componentes declaran metadatos en YAML frontmatter al inicio del archivo `.md`. Campos comunes obligatorios: `id`, `name`, `description`, `version`, `status`, `owner`, `domain`, `created_date`, `review_date`. Campos adicionales según tipo (por ejemplo, `autonomy_level`, `skills`, `runtime`, `human_review_points` para agentes; `agents`, `human_checkpoints` para workflows).

El ID es la única fuente de verdad de identidad. Debe coincidir exactamente con el nombre del archivo. El validador lo comprueba y rechaza cualquier discrepancia.

### 1.5 Modelo de ejecución real

**Punto crítico para cualquier arquitecto que evalúe el framework:** la ejecución de los agentes es manual. El framework define prompts de sistema y metadatos en Markdown/YAML. El agente "se invoca" cuando un humano abre Claude o Copilot, copia el prompt del agente y conduce la conversación. No existe hoy una capa de orquestación programática que encadene agentes automáticamente. La "orquestación" que declaran los workflows es una secuencia documentada de pasos humanos.

Esta arquitectura es deliberada en la fase actual — reduce el riesgo operacional y garantiza supervisión humana. Pero implica que los workflows no son ejecutables por sí solos: requieren un operador humano en cada paso.

---

## 2. Gaps técnicos detectados

Los siguientes gaps se clasifican por criticidad para la madurez del framework.

### 2.1 GAP CRÍTICO — Ausencia de runtime de orquestación real

**Descripción:** No existe un motor de ejecución que encadene agentes automáticamente. La orquestación entre agentes es declarativa (campos `agents:`, `skills:`, `subagents:` en el frontmatter) pero no programática. `invoke_agent.py` lo confirma explícitamente: "Este script es un simulador... No ejecuta el agente real."

**Impacto:** Los workflows multi-agente requieren intervención manual en cada paso. El SDD full (10 agentes en secuencia) necesita que un humano conduzca 10 conversaciones separadas, pasando manualmente el output de cada una como input de la siguiente. No es viable a escala.

**Referencia en el plan:** Punto #41 del `PLAN_FASES_FUTURAS.md` — "mecanismo real de orquestación entre agentes". Sesión candidata: 13.

**Solución recomendada:** Ver sección 4.1.

### 2.2 GAP CRÍTICO — Sin memoria compartida entre agentes ni entre sesiones

**Descripción:** No existe ninguna capa de memoria (short-term ni long-term) para los agentes. El estado se preserva mediante artefactos Git y tickets Jira, pero no hay ningún mecanismo programático de contexto compartido. Cada sesión comienza desde cero.

**Impacto:** Los agentes no pueden "recordar" decisiones tomadas en pasos anteriores del mismo workflow sin que el operador humano las proporcione explícitamente. En workflows largos (SDD full: 10 agentes) esto genera pérdida de contexto y riesgo de inconsistencias entre artefactos generados por distintos agentes.

**Referencia:** No hay un punto específico en `PLAN_FASES_FUTURAS.md` para memoria. Es un gap arquitectónico no explicitado todavía como tarea.

**Solución recomendada:** Ver sección 4.2.

### 2.3 GAP ALTO — Telemetría declarativa, no instrumentada automáticamente

**Descripción:** El sistema de telemetría existe (`apb-ops-telemetry-emit-v1.0`, `emit_telemetry.py`, tabla `APBFrameworkTelemetry_CL` en Azure Monitor) pero su activación es manual. Los agentes deben emitir un `TELEMETRY_BLOCK` al final de su output, que el operador humano ejecuta o no. Los ~226 componentes anteriores a la Sesión 17 no tienen telemetría aplicada (pendiente como "Fase #43").

**Impacto:** Las métricas de gobierno declaradas en `GOVERNANCE.md` §6.1 (% de componentes en draft, tiempo de aprobación, reutilización de skills, incidencias atribuibles a IA) no tienen datos reales que las alimenten. El dashboard ejecutivo que se quiere construir para Dirección no tendría contenido real.

**Estado actual:** `telemetry/events.jsonl` existe como log local. El pipeline CI `telemetry.yml` existe pero no está verificado que emita a Azure Monitor de forma fiable.

**Solución recomendada:** Ver sección 4.3.

### 2.4 GAP ALTO — Sin mecanismo de retry ni manejo de fallos programático

**Descripción:** El framework no define ningún mecanismo de retry automático, exponential backoff, ni circuit breaker para el caso de que un agente produzca output de baja calidad o incorrecto. La única estrategia de fallback documentada son los bucles de iteración manuales (`ITERATION_LOOPS.md`): hasta 3 iteraciones, con gate humano entre cada una.

**Impacto:** En flujos autónomos futuros (cuando exista el runtime de orquestación), los fallos de un agente propagarán errores hacia abajo en el workflow sin ninguna mitigación automática.

**Solución recomendada:** Definir una política de retry por nivel de autonomía como parte del diseño del runtime de orquestación. Incluir en el SCHEMA.md un campo opcional `max_retries` y `retry_strategy` por componente.

### 2.5 GAP ALTO — Catálogo de dominios APB vacío

**Descripción:** El submódulo `domain-catalog/` tiene la estructura correcta (schemas YAML, plantillas, scripts de scaffolding, governance) pero `domains/` solo contiene un `.gitkeep`. No existe ningún dominio de negocio APB creado y aprobado.

**Impacto:** Las capacidades de DDD y de descomposición de monolitos del framework (`apb-agent-ddd-v1.0`, `apb-agent-domain-architect-v1.0`, workflow `apb-wf-cloud-migration-v1.0`) producirán resultados no alineados con la arquitectura real de APB hasta que exista este catálogo. Cada análisis de monolito inventará su propia taxonomía de dominios.

**Referencia:** Punto #38 Fase 0 de `PLAN_FASES_FUTURAS.md`. Desbloqueado cuando Débora aporte el listado de APIs existentes.

**Solución recomendada:** Priorizar la construcción del catálogo de dominios usando `apb-agent-ddd-v1.0` con el listado de APIs como input. Es el prerequisito para que los agentes de arquitectura y modernización funcionen de forma consistente entre proyectos.

### 2.6 GAP MEDIO — Todos los componentes en estado `draft`

**Descripción:** El 100% de los 262 componentes está en estado `draft`. Ninguno ha pasado por el ciclo de aprobación formal (candidate → under_review → approved).

**Impacto:** El framework no es consumible formalmente por proyectos APB hasta que al menos los componentes más críticos (workflows principales, agentes core) estén en `approved`. El tiempo medio de aprobación objetivo es <10 días hábiles (`GOVERNANCE.md` §6.1), pero no se ha ejecutado ni un solo ciclo de aprobación.

**Observación:** Esto es coherente con el estado declarado del framework ("preparado para pilotos controlados, no para producción") pero requiere un plan de priorización de qué componentes aprobar primero y quién son los aprobadores concretos de cada ámbito.

### 2.7 GAP MEDIO — Capa Capability no implementada

**Descripción:** El nivel superior de la jerarquía (Capability — capacidades de negocio como "Generar especificaciones" o "Modernizar aplicación") está definido en `SYSTEM.md` y `README.md` pero ningún archivo de capacidad existe en `capabilities/` (la carpeta no aparece en el repositorio).

**Impacto:** No es un gap operacional hoy (la jerarquía funciona desde Skill hacia arriba), pero sí es un gap de discoverability: sin la capa de capacidades, un stakeholder de negocio no puede navegar el catálogo por capacidad de negocio; solo puede hacerlo por componente técnico. Esto dificulta la adopción por perfiles no técnicos.

### 2.8 GAP MEDIO — Integraciones M365 pendientes de activación

**Descripción:** Los artefactos de integración existen (`openapi/apb-framework-api.yaml`, `openapi/ai-plugin.json`, `forge/manifest.yml`, `forge/src/functions/invokeFramework.js`, `adapters/rovo/`, `adapters/m365/`) pero están en estado `draft` y requieren trabajo de activación por parte del equipo de Plataforma APB. Documentado en `docs/HANDOFF_SESION15_INTEGRACIONES.md`.

**Impacto:** El framework no está disponible desde M365 Copilot ni desde Rovo (Atlassian) sin este trabajo de activación. Tampoco hay integración activa con Teams, SharePoint ni correo corporativo.

### 2.9 GAP BAJO — Plantilla AGENT.md desactualizada

**Descripción:** `context/apb/templates/AGENT.md` usa el formato antiguo de metadatos en blockquote (`> **ID:** ...`) que ya no es válido según `SCHEMA.md`. Los agentes reales del repositorio usan correctamente YAML frontmatter, pero la plantilla de referencia para crear nuevos agentes está desactualizada.

**Impacto:** Cualquier persona que use la plantilla directamente (sin consultar un agente real del catálogo) generará un componente que fallará el validador.

**Referencia:** Punto #44 de `PLAN_FASES_FUTURAS.md`. Corrección trivial.

### 2.10 GAP BAJO — Skills `_spec-driven/` de `apb-ai-skills` sin decisión

**Descripción:** Al deprecar el repositorio `apb-ai-skills` (decisión Sesión QA), tres skills de la carpeta `skills/_spec-driven/` (`spec-to-api-contract`, `spec-to-e2e-flows`, `spec-to-test-plan`) no fueron evaluadas individualmente para posible fusión con el framework principal.

**Referencia:** Punto #45 de `PLAN_FASES_FUTURAS.md`. Pendiente de criterio de Débora.

---

## 3. Recomendaciones de infraestructura

### 3.1 Runtime de orquestación — Prioridad 1

El gap más crítico del framework es la ausencia de ejecución programática. La arquitectura objetivo recomendada para el entorno Azure/M365 de APB es:

**Opción A: Azure AI Foundry + Semantic Kernel (recomendada)**
Construir una capa de orquestación sobre Azure AI Foundry usando Semantic Kernel como SDK de agentes. Cada agente del framework se traduce a un `KernelAgent` con su system prompt, sus tools (providers APB como MCP servers) y su `AutoFunctionCallingBehavior`. Los workflows se implementan como `AgentGroupChat` o `ProcessFramework` con los human_checkpoints como interrupciones programáticas. Ventajas: native Azure, compatible con Azure Key Vault, integración nativa con M365, soporte multi-modelo.

**Opción B: Anthropic Agent SDK + Claude API**
Implementar los agentes como agentes Claude usando el Agent SDK de Anthropic. Más adecuado si el runtime primario sigue siendo Claude. Permite tool_use nativo, subagent delegation y multi-turn context.

**Opción C: Hybrid (Copilot + Claude para arranque)**
En el corto plazo, mientras se construye el runtime programático, formalizar los pasos manuales de los workflows en runbooks operativos detallados (qué pegar, en qué herramienta, cuándo aprobar). Esto no resuelve el gap pero hace el proceso reproducible y auditable.

**Recomendación:** Implementar la Opción A como objetivo a 6-12 meses, con la Opción C como puente operacional inmediato.

### 3.2 Capa de memoria — Prioridad 1

Para workflows multi-agente, se necesita un store de contexto compartido. Opciones en el entorno Azure:

- **Azure Cosmos DB (NoSQL):** store de estado de sesión y contexto de workflow. Cada ejecución de workflow tiene un `session_id` que los agentes usan para leer/escribir contexto. Soporta TTL automático para limpiar sesiones expiradas.
- **Azure Cache for Redis:** para contexto de corta duración dentro de una misma sesión de ejecución (short-term memory). Latencia sub-milisegundo, ideal para pasar el output de un agente al siguiente en tiempo real.
- **Azure Blob Storage / Git:** para memoria de larga duración (artefactos de sesiones pasadas). Ya está parcialmente implementado via artefactos Git.

La arquitectura recomendada combina las tres capas: Redis para contexto inmediato entre agentes en el mismo workflow, Cosmos DB para estado de sesión persistente entre sesiones del mismo proyecto, y Git para la memoria de largo plazo (specs, ADRs, código).

### 3.3 Observabilidad del framework — Prioridad 2

La tabla `APBFrameworkTelemetry_CL` en Azure Monitor ya está especificada. Lo que falta es:

1. **Instrumentación automática en el runtime de orquestación** (cuando exista): cada invocación de skill/agent/workflow emite automáticamente un evento de telemetría, sin depender de que el agente incluya un `TELEMETRY_BLOCK` en su output.
2. **Dashboard de KPIs del framework** en Power BI: usando `apb-agent-observability-v1.0` con la fuente `APBFrameworkTelemetry_CL`. Este agente ya está preparado para ello.
3. **Alertas operativas** en Azure Monitor: umbral para `% componentes en draft > 30%`, tiempo medio de aprobación, tasa de override humano.

Para la fase de transición (sin runtime automático), la estrategia es: emitir telemetría manualmente desde el CI (`telemetry.yml`) capturando al menos las invocaciones de validate_repo.py y generate_catalog.py como proxies de actividad del framework.

### 3.4 Infraestructura de secretos — Prioridad 2

El framework referencia Azure Key Vault correctamente (política documentada, secretos nunca en prompts). Lo que falta es:

- El provider `prov-akv-v1.0` existe pero su integración con el runtime futuro debe garantizar que los agentes resuelven secretos en tiempo de ejecución, no en tiempo de diseño.
- Para el runtime de orquestación, usar **Managed Identity** de Azure (no connection strings) para que los agentes accedan a Key Vault sin credenciales explícitas.

### 3.5 Pipelines CI/CD — Prioridad 3

Los pipelines existentes (`validate.yml`, `telemetry.yml`) cubren la integridad del framework. Para las aplicaciones que el framework ayuda a construir, el estándar APB soporta Jenkins y GitHub Actions (detección automática). Lo que falta es:

- Plantilla de pipeline parametrizable que incluya las validaciones APB (SonarQube gate, test coverage ≥80%, validación ENS) lista para ser usada por proyectos que adopten el framework.
- Integración del validador APB (`validate_repo.py`) como paso de pipeline en repositorios de aplicaciones (no solo en el repositorio del framework).

---

## 4. Componentes futuros recomendados

### 4.1 Orchestration Engine Provider

**Propuesta:** `prov-orchestration-engine-v1.0` — provider de tipo `action` que encapsula la capa de ejecución programática (Azure AI Foundry o Anthropic Agent SDK).

**Responsabilidades:**
- Resolver la cadena `workflow → agent → skill` sin intervención manual entre pasos.
- Gestionar los `human_checkpoints` como interrupciones programáticas (pause/resume con notificación Teams/correo).
- Mantener el `session_id` y el contexto compartido entre agentes.
- Emitir telemetría automática en cada invocación.

**Dependencias previas:** definir el runtime de orquestación (sección 3.1) antes de construir este provider.

### 4.2 Memory Provider

**Propuesta:** `prov-agent-memory-v1.0` — provider de tipo `action` con tres backends configurables (Redis, Cosmos DB, Git/Blob).

**Responsabilidades:**
- API uniforme `read_context(session_id, key)` / `write_context(session_id, key, value)` para todos los agentes.
- TTL configurable por tipo de contexto.
- Cifrado at-rest (Azure Cosmos DB con Customer Managed Keys).

### 4.3 Workflow State Manager

**Propuesta:** `apb-orch-workflow-state-v1.0` — skill de orquestación que gestiona el estado de ejecución de un workflow.

**Responsabilidades:**
- Registrar qué fase del workflow está activa y cuáles están completadas.
- Gestionar rollback si una fase falla.
- Notificar al responsable humano cuando se alcanza un `human_checkpoint`.

### 4.4 Agente de licitación (LCSP)

**Pendiente de briefing** de Débora (punto #36 del plan). Una vez recibido, debería cubrir: creación y revisión de pliegos de prescripciones técnicas, criterios de adjudicación, análisis de ofertas. Dominio candidato: `governance` o `pm`.

### 4.5 Agentes de plataforma Microsoft

**Propuesta:** tres providers/agentes nuevos para cubrir el punto #30:
- `prov-teams-v1.0` (action) — notificación de gates humanos y aprobaciones via Teams.
- `prov-sharepoint-v1.0` (knowledge) — lectura de documentos corporativos como input de skills.
- `prov-mail-v1.0` (action) — notificación de aprobaciones y resultados via correo corporativo.

La arquitectura base (`openapi/apb-framework-api.yaml`, `forge/`) ya está preparada para exponer estas capacidades.

### 4.6 Completar catálogo de dominios APB

**Prerequisito para todo lo demás de DDD.** Usar `apb-agent-ddd-v1.0` con el listado de APIs de APB como input. Resultado esperado: 15-30 dominios de negocio con sus bounded contexts, aprobados por Arquitectura. Esto desbloquea el agente de descomposición de monolitos (punto #38 Fase 1).

### 4.7 Aprobación formal de componentes core

El primer ciclo de aprobación debería cubrir, en este orden de prioridad:
1. `apb-wf-sdd-full-v1.0` (workflow de mayor impacto)
2. `apb-agent-spec-engineer-v1.0`, `apb-agent-technical-architect-v1.0`, `apb-agent-code-reviewer-v1.0`
3. Skills del dominio `development` de mayor uso (code-review, implement, api-design)
4. Políticas de seguridad relevantes del framework

---

## 5. Guía de extensibilidad técnica

### 5.1 Crear un nuevo componente

El proceso obligatorio para cualquier componente nuevo es:

1. **Discovery previo** en `catalog/CATALOG.md` e `INDEX.md`. Si ya existe cobertura parcial, ampliar el componente existente en lugar de crear uno nuevo.
2. **Si no hay alternativa**, documentar el hallazgo en `discovery/` antes de proceder.
3. **Crear el archivo `.md`** con frontmatter YAML completo conforme a `context/apb/SCHEMA.md`. El `id` debe coincidir exactamente con el nombre de archivo.
4. **Ejecutar el validador**: `python scripts/validate_repo.py --strict` — debe terminar con 0 errores.
5. **Regenerar el catálogo**: `python scripts/generate_catalog.py` — nunca editar `CATALOG.md`, `INDEX.md` ni `DOMAIN_REGISTRY.md` manualmente.
6. **Abrir PR** con el checklist de `CONTRIBUTING.md`. El CI bloqueará el merge si hay errores.
7. El componente nace en `draft`. Pasar a `candidate` requiere revisión de Arquitectura APB.

El agente `apb-agent-meta-builder-v1.0` automatiza este proceso cuando se le proporciona el tipo de componente, dominio y descripción funcional.

### 5.2 Añadir un nuevo dominio funcional

Los dominios funcionales válidos están definidos en `DOMAIN_REGISTRY.md`. Para añadir un dominio nuevo:

1. Actualizar `DOMAIN_REGISTRY.md` con el nuevo dominio y su prefijo de ID.
2. Actualizar `VALID_DOMAINS` en `scripts/validate_repo.py` (línea ~68).
3. Crear la carpeta `skills/apb-owned/<nuevo-dominio>/`.
4. Crear al menos una skill en ese dominio.
5. Ejecutar `scripts/generate_catalog.py` para que el nuevo dominio aparezca en el índice.

### 5.3 Integrar un componente de terceros

El proceso para skills/providers/wrappers de terceros es:

1. Verificar licencia compatible con uso interno APB.
2. Realizar análisis de seguridad del componente.
3. Crear el descriptor en `skills/third_party/<ecosistema>/` con frontmatter YAML que incluya `source_repo`, `source_license` y `source_commit` (SHA real, o `"unverified"` + `verified_date` si no hay acceso de red al repositorio).
4. Si el componente requiere adaptación APB, crear un wrapper en `wrappers/`.
5. Documentar el discovery en `discovery/`.
6. El wrapper APB puede ser usado por agentes como si fuera un componente propio.

**Nota sobre source_commit "unverified":** esta política es explícita (`GOVERNANCE.md` §4.2). El modo `--strict` no bloquea PRs por este warning, pero debe refinarse a un SHA real en cuanto haya acceso de red.

### 5.4 Añadir un nuevo runtime/adaptador

Para soportar un nuevo LLM o plataforma (Gemini, Azure OpenAI nativo, etc.):

1. Crear `adapters/<nuevo-runtime>/adapter-<runtime>-v1.0.md` con frontmatter YAML y `runtime_target: "<nuevo-runtime>"`.
2. Añadir `"<nuevo-runtime>"` como valor válido en el campo `runtime` de `SCHEMA.md` §3.2.
3. Actualizar `validate_repo.py` para reconocer el nuevo runtime como válido.
4. Para cada agente que quiera soportar el nuevo runtime, añadirlo a su lista `runtime:`.
5. El adaptador traduce el system prompt y el formato de inputs/outputs al formato específico de la plataforma.

### 5.5 Añadir un provider de acción

Los providers de tipo `action` permiten a los agentes interactuar con sistemas externos (Jira, GitHub, Azure Monitor, etc.):

1. Crear `providers/prov-<nombre>-v1.0.md` con `provider_type: action` y `access_mode` apropiado.
2. Si el provider requiere credenciales, referenciarlo via Azure Key Vault — nunca hardcoded.
3. Crear skills que consuman el provider (listado en `depends_on` del frontmatter de la skill).
4. Para providers que requieren integración programática con el runtime de orquestación futuro, añadir las especificaciones de tool-use (parámetros, schema JSON, ejemplos de invocación) en el cuerpo del documento del provider.

### 5.6 Extender el validador

`scripts/validate_repo.py` está diseñado para ser extensible. Para añadir una nueva regla de validación:

1. Añadir la función de validación con la firma `validate_<nombre>(repo_path: Path, result: ValidationResult, ...)`.
2. Invocarla desde `main()` en el orden apropiado.
3. Usar `ValidationIssue("ERROR", ...)` para bloquear el merge en CI.
4. Usar `ValidationIssue("WARNING", ...)` para advertencias (bloqueantes en `--strict` salvo si se añaden a `is_policy_exempt_warning()`).
5. Documentar la nueva regla en `GOVERNANCE.md` con la referencia a la política que la justifica.

---

## 6. Modelo de gobernanza — puntos de control para arquitectos

### 6.1 Aprobadores por ámbito

| Ámbito | Aprobador primario | Escalado |
|--------|-------------------|----------|
| Arquitectura de solución | Arquitecto de Solución / Referencia | Arquitecto Enterprise |
| Cloud / Infraestructura | Arquitecto Cloud | Arquitectura Enterprise |
| APIs / Eventos | Arquitecto de Integración | Arquitectura |
| DDD / Dominios | Arquitecto de Solución | Arquitectura Enterprise |
| Ciberseguridad | Security Architect / CISO | CISO |
| QA / Calidad | QA Lead / Gobierno QA | Dirección QA |
| Operaciones / SRE | SRE Lead / Responsable de Operaciones | Dirección de Operaciones |

**Regla de doble firma:** para pasar a `approved`, un componente requiere al menos dos aprobadores de ámbitos distintos. Esto está codificado en `GOVERNANCE.md` §2.2 pero no en el validador — sería una mejora futura añadir la verificación de firmas en el frontmatter.

### 6.2 Indicadores de gobierno objetivo

| Indicador | Objetivo | Frecuencia |
|-----------|----------|------------|
| Componentes en `draft` | < 30% del total | Mensual |
| Tiempo medio de aprobación | < 10 días hábiles | Mensual |
| Excepciones activas | < 5% de proyectos | Trimestral |
| Reutilización de skills corporativas | > 50% de skills corporativas | Trimestral |
| Incidencias atribuibles a IA | < 2% del total | Mensual |

**Estado actual (junio 2026):** 100% de componentes en `draft`, 0 aprobados, 0 métricas de gobierno con datos reales.

### 6.3 Niveles de autonomía — decisiones de diseño

Al diseñar un nuevo componente, la asignación del `autonomy_level` debe seguir estas reglas:

- **Nivel 0:** solo análisis/consulta, sin propuestas de acción. Apropiado para skills de solo lectura (búsqueda en catálogo, análisis de texto).
- **Nivel 1:** genera propuesta, espera confirmación explícita por acción. **Nivel por defecto.** Obligatorio para: análisis de arquitectura, seguridad, despliegue, gobierno.
- **Nivel 2:** ejecuta acciones de bajo riesgo autónomamente, gate en acciones de riesgo medio/alto. Apropiado para agentes de desarrollo, QA y operación en entornos no-producción.
- **Nivel 3:** reservado para casos muy específicos con runbooks completamente reversibles en entornos controlados. Requiere aprobación explícita previa.
- **Nivel 4:** no se usa en APB. Nunca.

El principio "ningún agente puede aprobar sus propios resultados" (`SYSTEM.md` §2.1 regla 2) es inviolable independientemente del nivel de autonomía.

### 6.4 Política de identificación obligatoria de artefactos IA

Todo artefacto producido por un agente o skill del framework debe incluir en su propio cuerpo (no solo en metadatos internos):

1. Que fue generado por IA (agente y skill concretos, no solo "IA genérica").
2. El nombre o rol del humano que lo validó (una vez completada la revisión).

Sin estos dos elementos, el artefacto no puede pasar a `approved`. Esta política (denominada "Política de Débora", `SYSTEM.md` §7.2) se está aplicando retroactivamente a los ~226 componentes del catálogo como Fase #43 del plan — la última fase antes del cierre.

---

## 7. Deuda técnica conocida del propio framework

| ID | Descripción | Criticidad | Sesión/Fase |
|----|-------------|-----------|-------------|
| #41 | Sin orquestación real entre agentes | Crítica | Sesión 13 |
| #43 | Aplicación retroactiva de marcado IA a ~226 componentes | Alta | Fase final |
| #38 F0 | Catálogo corporativo de dominios APB vacío | Alta | Pendiente de listado de APIs |
| #44 | Plantilla AGENT.md desactualizada respecto a SCHEMA.md | Media | Sesión 13 |
| #45 | Skills `_spec-driven/` de `apb-ai-skills` sin evaluar | Baja | A decidir |
| #30 | Providers Teams/SharePoint/mail sin activar | Media | Pendiente activación equipo |
| #36 | Agentes de licitación (LCSP) | A definir | Pendiente briefing |
| — | Telemetría retroactiva en ~226 componentes anteriores a Sesión 17 | Media | Fase #43 |
| — | Tipografía del design system pendiente de verificación | Baja | Design System |
| — | Catálogo de componentes DevExtreme parcial | Baja | Design System |

---

*Este documento fue generado por análisis automatizado del repositorio APB-IA-FRAMEWORK (v1.0.0-draft, commit 2026-06-26) y sus submódulos APB-DOMAIN-CATALOG y APB-DESIGN-SYSTEM.*
*Pendiente de validación humana por Arquitectura APB antes de distribución oficial.*
