# Guía Funcional del APB AI Framework

> **Audiencia:** Analistas funcionales, desarrolladores, jefes de proyecto, perfiles de uso del framework.
> **Versión analizada:** 1.0.0-draft (estado al 26 de junio de 2026)
> **Estado del framework:** Todos los componentes en `draft`. Preparado para pilotos controlados. No usar en producción sin aprobación formal de Arquitectura, QA y Ciberseguridad APB.

---

## ¿Qué es el APB AI Framework?

El APB AI Framework es la plataforma corporativa de inteligencia artificial del Port de Barcelona. Su propósito es que cualquier equipo técnico de APB pueda resolver problemas reales — analizar código, generar especificaciones, diseñar arquitecturas, preparar releases — usando agentes de IA que ya conocen los estándares, políticas y tecnologías propias de la organización.

No es una herramienta genérica de IA. Es un sistema diseñado específicamente para el contexto de APB: sus políticas de seguridad, su stack tecnológico (.NET, DevExpress, Azure SQL, Azure Service Bus), sus estándares de desarrollo, y sus obligaciones de cumplimiento (ENS, OWASP, RGPD, LCSP).

La premisa central es que **la IA propone, el humano aprueba**. Ningún agente del framework puede tomar decisiones de producción por sí solo.

---

## ¿Qué puede hacer el framework por ti hoy?

### Desarrollo de nuevas aplicaciones (Spec Driven Development)

El framework cubre el ciclo completo de desarrollo desde cero: desde la conversación inicial con el negocio hasta el primer release. El flujo es:

1. El **Business Analyst Agent** convierte entrevistas y documentación existente en un documento de descubrimiento de negocio.
2. El **Spec Engineer** genera la especificación técnica del sistema (`system-spec.md`), el backlog ágil en Jira y la estimación COSMIC de puntos de función.
3. El **Domain Architect** modela los dominios de negocio con DDD y Event Storming.
4. El **Technical Architect** diseña la arquitectura de solución, los contratos API (OpenAPI) y el plan técnico.
5. El **Security Architect** aplica threat modeling STRIDE, valida ENS y OWASP antes de escribir una línea de código.
6. El **Implementer Agent** genera el código conforme a los estándares APB, con su code review y la documentación del PR.
7. El **QA Automation Agent** produce el plan de pruebas, tests unitarios, de integración y E2E.
8. El **Governance Agent** valida cumplimiento de estándares antes del release.
9. El **Release Manager** decide el go/no-go con información completa.
10. El **Documentation Agent** cierra el ciclo con ADRs, Swagger/OpenAPI y el manual del sistema.

Cada agente produce artefactos que van directamente al repositorio Git del proyecto. El resultado no es solo código — es código trazable hasta el ticket Jira de origen.

### Modernización de aplicaciones legacy

Para los ~550 repositorios existentes que no tienen especificaciones formales, el framework ofrece un flujo de onboarding:

- El **Tech Discovery Agent** analiza el código fuente, las bases de datos y los logs para reconstruir qué hace la aplicación hoy.
- El **Modernization Agent** propone la estrategia de modernización: qué migrar a microservicios, qué refactorizar in-place, qué retirar.
- El workflow `apb-wf-spec-from-legacy-v1.0` genera la especificación retrospectiva (lo que la aplicación hace) como punto de partida para su evolución.

### Revisión de código y calidad

El **Code Reviewer Agent** analiza pull requests conforme a los estándares APB: convenciones .NET, seguridad, deuda técnica, cumplimiento de SonarQube. Produce un informe de defectos clasificados por severidad (Crítico/Alto/Medio/Bajo) con criterio de salida claro: 0 defectos Críticos y 0 defectos Altos antes del merge.

### Seguridad y cumplimiento

Hay agentes específicos para cada fase de la seguridad:

- **Security Architect Agent**: diseño seguro, threat modeling, análisis de riesgos.
- **Compliance Audit Agent**: verifica cumplimiento de políticas APB, ENS, OWASP, RGPD, LCSP.
- **Risk Exception Agent**: gestiona las solicitudes de excepción formales cuando un proyecto necesita desviarse de un estándar.

Todas las políticas corporativas APB (seguridad, infraestructura, calidad, capacidad, contratación) están integradas en el framework y son consultadas automáticamente por los agentes relevantes.

### Operación y observabilidad

El **SRE Agent** y el **Incident Support Agent** asisten en incidencias técnicas: triaje, diagnóstico y escalado. El **Observability Agent** diseña dashboards de monitorización en Power BI o Grafana a partir de una descripción en lenguaje natural, identificando qué métricas ya están disponibles y qué instrumentación hay que añadir.

El **Tech Debt Agent** analiza repositorios existentes y produce un plan priorizado de remediación: vulnerabilidades, dependencias obsoletas, incumplimientos de políticas, cuellos de botella de rendimiento. El plan incluye la apertura automática de tickets en Jira para cada acción.

### Arquitectura de plataforma y cloud

El **Cloud Architect Agent** asiste en migraciones a Azure y en el diseño de infraestructura cloud conforme a las políticas corporativas (POLICY_AZURE_v2.0, POLICY_INFRASTRUCTURE_CLOUD). El **Platform Engineer Agent** cubre pipelines CI/CD (Jenkins / GitHub Actions), contenedores y Terraform.

### Diseño de interfaz

El **UX Mockup Agent** permite a perfiles funcionales (sin escribir código) generar mockups estructurados de interfaz usando los componentes DevExtreme y la guía de estilo corporativa del Port de Barcelona. La salida puede ser directamente el input del agente de implementación frontend.

---

## Cómo empezar a usar el framework

### Prerrequisito: tener acceso al repositorio

El framework vive en GitHub. Para proyectos nuevos, se referencia como submódulo Git:

```bash
git submodule add https://github.com/apb-dmartin/APB-IA-FRAMEWORK.git .apb-ai
```

Para repositorios legacy, el primer paso es ejecutar el validador sobre el repositorio existente:

```bash
python .apb-ai/scripts/validate_repo.py --path /ruta/al/repo
```

El validador dirá exactamente qué falta: estructura de carpetas, specs, estándares.

### Para un proyecto nuevo con SDD

1. Copiar el scaffold SDD-ready en el nuevo repositorio:
   ```bash
   cp -r .apb-ai/repo-scaffold/sdd-ready/* /ruta/al/nuevo-repo/
   ```
2. Seguir la guía `docs/sdd-getting-started.md`.
3. Invocar el Business Analyst Agent como primer paso con el contexto del negocio.

### Para invocar un agente individual

Cada agente tiene su propio archivo en `agents/` con su prompt de sistema, sus capacidades, los inputs que espera y los outputs que produce. Para usarlo:

1. Abre Claude (web o cliente Windows) o GitHub Copilot en VS Code.
2. Carga el prompt de sistema del agente en la conversación.
3. Proporciona el input que el agente solicita (código, descripción, documento).
4. Revisa y aprueba el output antes de incorporarlo al proyecto.

También puedes listar todos los agentes disponibles:

```bash
python .apb-ai/scripts/invoke_agent.py --list
python .apb-ai/scripts/invoke_agent.py --list-workflows
```

### Para ejecutar un workflow completo

Un workflow coordina múltiples agentes en secuencia. El workflow `apb-wf-sdd-full-v1.0` cubre el ciclo completo de desarrollo. Para usarlo, prepara el input inicial (contexto de negocio, stakeholders, stack tecnológico, requisitos de compliance) y sigue las fases del workflow con las aprobaciones humanas requeridas en cada gate.

---

## Reglas fundamentales de uso

**La IA propone, el humano decide.** Todo output de un agente es una propuesta. Antes de incorporarlo a un repositorio, subirlo a Jira, desplegarlo o usarlo en producción, debe pasar por revisión humana explícita. El nivel por defecto del framework es Nivel 1: generación asistida con aprobación humana obligatoria antes de cada acción.

**No al vibe coding.** El framework no genera código a partir de una petición vaga en lenguaje natural. Toda generación de código parte de una especificación técnica, un issue en Jira o un hallazgo documentado. Esto no es una restricción arbitraria — es la diferencia entre código trazable y mantenible, y código que nadie entiende tres meses después.

**Los estándares APB prevalecen.** Si un agente recomienda algo que contradice los estándares corporativos, los estándares ganan. Los agentes conocen las políticas de APB y las aplican por defecto, pero el equipo técnico siempre tiene la última palabra.

**Todo resultado debe identificar su origen.** Cualquier artefacto generado por IA (un informe, un plan, un componente, un documento) debe declarar explícitamente que fue generado por IA y qué humano lo validó. Esto es obligatorio antes de que un artefacto se considere aprobado. No basta con saberlo internamente — debe estar visible en el propio documento.

**Los secretos no van en prompts.** Nunca introduzcas credenciales, contraseñas, connection strings ni API keys en los inputs de los agentes. El framework usa referencias a Azure Key Vault. Si necesitas que un agente trabaje con un sistema que requiere credenciales, usa el provider `prov-akv-v1.0`.

---

## Capacidades disponibles: catálogo completo

### Agentes disponibles (26)

| Agente | Qué hace |
|--------|----------|
| Business Analyst | Descubrimiento de negocio, entrevistas con stakeholders, documento de capacidades |
| Spec Engineer | Especificaciones técnicas, backlog ágil, estimación COSMIC |
| Domain Architect | Modelado DDD, Event Storming, bounded contexts |
| Technical Architect | Arquitectura de solución, contratos API, plan técnico |
| Security Architect | Threat modeling, análisis de riesgos, ENS/OWASP |
| Implementer | Generación de código .NET/Django, code review, PR |
| QA Automation | Plan de pruebas, tests automáticos, criterios de calidad |
| Code Reviewer | Revisión de código, estándares APB, detección de defectos |
| Cloud Architect | Diseño cloud Azure, migraciones, infraestructura |
| Platform Engineer | CI/CD, pipelines, contenedores, Terraform |
| SRE | RCA post-incidente, SLOs, runbooks operativos |
| Incident Support | Triaje, diagnóstico y escalado de incidencias técnicas L1 |
| Observability | Diseño de dashboards Power BI / Grafana, instrumentación de logging |
| Tech Debt | Análisis de deuda técnica, vulnerabilidades, plan de remediación con Jira |
| Modernization | Estrategia de modernización de legacy, roadmap de migración |
| Tech Discovery | Ingeniería inversa de sistemas existentes |
| DDD Agent | Análisis DDD sobre repositorios y bases de datos existentes |
| Domain Architect | Dominios de negocio, catálogo corporativo de dominios APB |
| UX Mockup | Mockups de interfaz para perfiles funcionales (DevExtreme + guía APB) |
| Documentation | ADRs, Swagger/OpenAPI, manuales del sistema |
| Governance | Validación de cumplimiento, estándares, auditorías |
| Compliance Audit | Auditoría de políticas corporativas y normativas |
| Risk Exception | Gestión de excepciones formales a estándares |
| FinOps | Análisis de costes cloud, optimización Azure |
| Catalog Manager | Mantenimiento del catálogo del framework, estados de componentes |
| Meta Builder | Creación de nuevos componentes del framework conforme al esquema |
| Release Manager | Coordinación y validación de releases |

### Workflows disponibles (8)

| Workflow | Cuándo usarlo |
|----------|---------------|
| SDD Full | Desarrollo completo de una nueva aplicación desde cero |
| Legacy Onboarding | Incorporar un repositorio existente al framework |
| Spec from Legacy | Generar especificación retrospectiva de una app en producción |
| Code Review | Revisión exhaustiva de código de un repositorio o PR |
| QA Evidence | Generación de evidencias de calidad para releases |
| Cloud Migration | Planificación y ejecución de migraciones a Azure |
| Incident L1 | Soporte de primera línea para incidencias técnicas |
| Risk Exception | Proceso formal de solicitud y aprobación de excepciones |

### Skills (129 propias + 51 de terceros)

Las skills son las capacidades atómicas del framework: tareas concretas con inputs y outputs bien definidos. Los agentes las invocan internamente; como usuario normalmente no las invocas directamente, pero sí las verás referenciadas en los outputs de los agentes.

Ejemplos por dominio:
- **Desarrollo**: generación de código .NET, revisión SonarQube, diseño de API, queries SQL, frontend DevExtreme
- **QA**: generación de tests unitarios, plan de pruebas, anonimización de datos RGPD, criterios de release
- **Arquitectura**: diseño DDD, Event Storming, contratos API, diseño cloud
- **Seguridad**: OWASP, ENS, threat modeling, análisis forense, hardening cloud
- **Gobernanza**: cumplimiento de estándares, gestión de catálogo, análisis de riesgos de IA
- **Operación**: observabilidad, SLOs, telemetría, gestión de dependencias, análisis de rendimiento

---

## Integración con las herramientas que ya usas

### Con GitHub Copilot (VS Code / Visual Studio)

El framework tiene un adaptador nativo para Copilot. El archivo `adapters/copilot/adapter-copilot-v1.0.md` explica cómo configurar `copilot-instructions.md` en tu repositorio para que Copilot use los agentes y estándares del framework.

### Con Claude (web o cliente Windows)

Copia el prompt de sistema del agente que quieres usar y ábrelo como una nueva conversación en Claude. El framework tiene un adaptador Claude en `adapters/claude/adapter-claude-v1.0.md`. Para flujos complejos, Claude Code (CLI) permite automatizar la invocación de agentes.

### Con Jira

Los agentes que generan backlog, tickets o planes de remediación producen la estructura en formato compatible con Jira. El mapa completo de qué agente crea qué tipo de ticket y en qué momento del ciclo de vida está documentado en `docs/JIRA_AGENT_MAP.md`.

### Con Microsoft 365 (Teams, SharePoint, correo)

El framework dispone de una API OpenAPI (`openapi/apb-framework-api.yaml`) y una aplicación Forge para Atlassian (`forge/`). La integración con Teams, SharePoint y correo está disponible como provider (`prov-ms365-v1.0`) y documentada en `docs/HANDOFF_SESION15_INTEGRACIONES.md`. Su activación requiere trabajo por parte del equipo de Plataforma APB.

### Con M365 Copilot / Rovo (Atlassian)

El framework puede exponerse como plugin de M365 Copilot mediante el manifest en `openapi/ai-plugin.json`. Para Rovo (Atlassian), la Forge App actúa como puente. Ambas integraciones están parcialmente implementadas y requieren configuración por parte del equipo de administración de APB.

---

## Qué esperar del proceso de aprobación

El framework tiene un ciclo de vida de gobierno para todos sus componentes. Cuando un agente genera un artefacto:

1. El artefacto nace en estado `draft` — es una propuesta, no un resultado aprobado.
2. El responsable técnico lo revisa y, si es correcto, lo mueve a `candidate`.
3. Para componentes que van a producción, se requiere revisión formal por los aprobadores correspondientes (Arquitectura, QA, Ciberseguridad según el tipo).
4. Solo cuando está en `approved` es consumible por otros proyectos.

Este proceso existe para que la organización pueda confiar en los artefactos que produce el framework. No es burocracia — es la garantía de que el código que llega a producción tiene los ojos humanos adecuados encima.

---

## Ejemplos de uso real

### "Necesito especificar una nueva aplicación de gestión de amarres"

1. Abre Claude o Copilot con el prompt de `apb-agent-business-analyst-v1.0`.
2. Describe el sistema en lenguaje natural (qué problema resuelve, quién lo usa, qué datos maneja).
3. El agente produce `business-discovery.md`.
4. Apruébalo y pásalo como input a `apb-agent-spec-engineer-v1.0`.
5. En 2-3 iteraciones tienes `system-spec.md` + backlog Jira + estimación.

### "Tengo un PR de 400 líneas de código .NET, ¿cómo lo reviso?"

1. Abre `apb-agent-code-reviewer-v1.0`.
2. Pega el diff del PR como input.
3. El agente produce un informe de defectos clasificado por severidad con referencias a los estándares APB.
4. Los defectos Críticos y Altos bloquean el merge hasta ser resueltos.

### "Quiero un dashboard Grafana del uso de los agentes de IA"

1. Abre `apb-agent-observability-v1.0`.
2. Describe qué quieres monitorizar: audiencia (técnica), fuente (Azure Monitor, tabla APBFrameworkTelemetry_CL), plataforma (Grafana).
3. El agente produce el diseño de KPIs, el JSON del dashboard y las alertas.
4. Apruébalo en el checkpoint humano antes de importarlo a Grafana.

### "Tenemos un monolito Java de 10 años. ¿Cómo lo modernizamos?"

1. Ejecuta el workflow `apb-wf-legacy-onboarding-v1.0` sobre el repositorio.
2. El Tech Discovery Agent reconstruye la arquitectura actual.
3. El Domain Architect propone la descomposición en dominios DDD.
4. El Modernization Agent define la estrategia (strangler fig, lift-and-shift parcial, etc.).
5. El resultado es un roadmap priorizado, no un big bang de reescritura.

---

## Limitaciones actuales que debes conocer

**Estado draft de todos los componentes.** El framework está en fase de pilotos controlados. Ningún componente ha pasado por el proceso de aprobación formal completo. Antes de usarlo en proyectos de producción, verifica con Arquitectura APB el estado de aprobación de los componentes que vas a usar.

**Sin ejecución automática.** El framework define lo que los agentes deben hacer, pero no los ejecuta automáticamente. Un humano debe abrir Claude o Copilot, cargar el prompt del agente y conducir la conversación. No hay integración programática end-to-end hoy — está planificada para fases futuras.

**Sin memoria entre sesiones.** Si usas un agente hoy y vuelves mañana, el agente no recuerda la sesión anterior. El estado se preserva mediante los artefactos Git (especificaciones, ADRs, código) y los tickets Jira. Es responsabilidad del usuario proporcionar el contexto relevante en cada sesión.

**Catálogo de dominios APB pendiente.** El catálogo corporativo de dominios de negocio del Port de Barcelona (necesario para las capacidades DDD y de descomposición de monolitos) está en construcción. Los agentes de arquitectura pueden trabajar sin él, pero los resultados serán más precisos cuando exista.

**Integraciones M365/Copilot requieren activación.** Las integraciones con Teams, SharePoint, M365 Copilot y Rovo requieren configuración por parte del equipo de Plataforma y Administración de APB. El código está preparado, pero no está activado en producción.

---

*Este documento fue generado por análisis automatizado del repositorio APB-IA-FRAMEWORK (v1.0.0-draft, commit 2026-06-26).*
*Pendiente de validación humana por Arquitectura APB antes de distribución oficial.*
