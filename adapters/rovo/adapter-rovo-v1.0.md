---
id: "adapter-rovo-v1.0"
name: "Atlassian Rovo Adapter"
description: "Adaptador de doble sentido entre el APB AI Framework y Atlassian Rovo: (1) expone agentes y skills del framework como Rovo Agents personalizados, accesibles desde Jira y Confluence; (2) permite que el framework invoque capacidades de Rovo (búsqueda semántica en Confluence/Jira, análisis de tickets, resumen de espacios) como herramientas dentro de un workflow. Complementa prov-atlassian-v1.0 añadiendo la capa de IA de Rovo sobre el ecosistema Atlassian ya conectado."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "orchestration"
runtime_target: "rovo"
adapted_components:
  - "apb-agent-spec-engineer-v1.0"
  - "apb-agent-business-analyst-v1.0"
  - "apb-agent-tech-discovery-v1.0"
  - "apb-agent-documentation-v1.0"
  - "apb-agent-tech-debt-v1.0"
  - "apb-gov-jira-evidence-v1.0"
  - "apb-disc-reverse-doc-v1.0"
  - "prov-atlassian-v1.0"
created_date: "2026-06-24"
review_date: "2026-06-24"
---

# Atlassian Rovo Adapter

---

## Propósito

Atlassian Rovo es la capa de IA de Atlassian sobre el ecosistema Jira + Confluence. A partir de julio 2026 APB comenzará a utilizarlo. Este adaptador define cómo el APB AI Framework se integra con Rovo en las dos direcciones posibles:

- **Dirección A (framework → Rovo):** el framework invoca capacidades de Rovo —búsqueda semántica en Confluence, análisis de tickets Jira, resumen de espacios— como herramientas dentro de sus workflows. Esto complementa `prov-atlassian-v1.0`, que ya gestiona operaciones CRUD sobre Jira/Confluence.

- **Dirección B (Rovo → framework):** los usuarios de APB que ya trabajan en Jira o Confluence pueden invocar agentes del framework a través de **Rovo Agents** personalizados, sin salir de su entorno Atlassian habitual.

---

## Diferencia entre `prov-atlassian-v1.0` y `adapter-rovo-v1.0`

| Componente | Qué hace | Cuándo usarlo |
|-----------|----------|---------------|
| `prov-atlassian-v1.0` | CRUD sobre Jira/Confluence vía REST API: crear tickets, actualizar issues, escribir páginas | El framework necesita crear/modificar objetos Atlassian |
| `adapter-rovo-v1.0` | Capa de IA de Rovo: búsqueda semántica, resúmenes, análisis, agentes conversacionales | El framework necesita razonar sobre el contenido de Jira/Confluence, o el usuario quiere invocar el framework desde Rovo |

Los dos componentes se complementan: `prov-atlassian-v1.0` escribe los resultados, `adapter-rovo-v1.0` los descubre y razona sobre ellos.

---

## Arquitectura de integración

### Dirección A — Framework invoca Rovo

El framework llama a la **Rovo API** (o equivalente Graph semántico de Atlassian) para obtener conocimiento sintetizado del ecosistema Jira/Confluence APB:

| Capacidad Rovo | Endpoint | Uso en el framework |
|---------------|----------|---------------------|
| Búsqueda semántica Confluence | `POST /rovo/v1/search` | Encontrar políticas, guías, decisiones técnicas relevantes como input de agentes |
| Resumen de espacio Confluence | `GET /rovo/v1/spaces/{key}/summary` | Obtener estado de documentación de un proyecto para `apb-agent-documentation-v1.0` |
| Análisis de tickets Jira | `POST /rovo/v1/issues/analyze` | Extraer patrones de un conjunto de tickets para `apb-agent-spec-engineer-v1.0` |
| Chat con contexto de proyecto | `POST /rovo/v1/chat` con `context.project_key` | Preguntas sobre el estado de un proyecto para `apb-agent-tech-discovery-v1.0` |
| Resumen de historial Jira | `POST /rovo/v1/issues/summarize` con filtros | Reconstrucción de specs desde histórico para agente de spec desde histórico (#37) |

Todas las llamadas usan el token de `prov-atlassian-v1.0` (mismas credenciales, distinto endpoint de Rovo).

### Dirección B — Rovo invoca el framework

Los agentes APB se implementan como **Rovo Agents personalizados** (Atlassian Forge App). El usuario los invoca desde el chat de Rovo en Jira o Confluence con lenguaje natural.

```
Arquitectura:
[Usuario en Jira/Confluence]
    → [Rovo — interpreta la intención]
    → [Rovo Agent APB (Forge App)]
    → [Framework skill/agent correspondiente via API REST APB]
    → [Respuesta devuelta a Rovo]
    → [Rovo muestra resultado al usuario en Jira/Confluence]
```

---

## Rovo Agents APB expuestos

### Agente Rovo: APB Spec desde Jira

Analiza el historial de tickets de un proyecto Jira y genera o actualiza la especificación funcional en Confluence.

```yaml
rovo_agent_id: "apb-spec-from-jira"
display_name: "APB — Spec desde historial Jira"
description: "Analiza los tickets de este proyecto y genera la especificación funcional actualizada en Confluence."
framework_agent: "apb-agent-spec-engineer-v1.0"
trigger_examples:
  - "Genera la spec de la pantalla de gestión de buques a partir de los tickets de GISPEM"
  - "¿Cuál es el comportamiento esperado del módulo de atraques según los tickets de los últimos 6 meses?"
  - "Actualiza la spec de Portal Docks con los cambios del último sprint"
input_context:
  - "Project key Jira activo en el contexto del usuario"
  - "Filtros de sprint, etiquetas, o épicas (opcionales)"
output:
  - "Página Confluence creada o actualizada con la spec generada"
  - "Ticket Jira de revisión creado y asignado al Product Owner"
```

### Agente Rovo: APB Tech Discovery

Analiza el código y la arquitectura de un proyecto y genera un informe de discovery técnico.

```yaml
rovo_agent_id: "apb-tech-discovery"
display_name: "APB — Discovery Técnico"
description: "Analiza la arquitectura y el estado técnico de un proyecto y genera un informe de discovery."
framework_agent: "apb-agent-tech-discovery-v1.0"
trigger_examples:
  - "Analiza el estado técnico del proyecto GISPEM y genera el informe de discovery"
  - "¿Qué deuda técnica tiene detectada el proyecto Portal Docks?"
```

### Agente Rovo: APB Documentación

Genera o actualiza documentación técnica y funcional en Confluence a partir del estado del proyecto.

```yaml
rovo_agent_id: "apb-documentation"
display_name: "APB — Generador de Documentación"
description: "Genera o actualiza documentación técnica y funcional en Confluence."
framework_agent: "apb-agent-documentation-v1.0"
trigger_examples:
  - "Genera el manual de usuario del módulo de gestión de atraques"
  - "Actualiza la documentación de arquitectura del proyecto Portal Docks con los últimos cambios"
  - "Crea el ADR de la decisión de usar DevExtreme para la nueva pantalla de buques"
```

---

## Configuración del Rovo Agent (Forge App)

```yaml
forge_app:
  id: "apb-rovo-agents"
  name: "APB AI Framework — Rovo Agents"
  version: "1.0.0"
  permissions:
    scopes:
      - "read:jira-work"
      - "write:jira-work"
      - "read:confluence-content.all"
      - "write:confluence-content"
      - "read:rovo:user"
  modules:
    rovo:agents:
      - key: "apb-spec-from-jira"
        name: "APB Spec desde Jira"
        description: "Genera specs funcionales desde el historial de tickets Jira"
        prompt: "Invoca el framework APB para generar especificaciones funcionales..."
        externalAuth:
          - key: "apb-framework-api"
            displayName: "APB AI Framework API"
            apiDefinition: "https://apim.portdebarcelona.cat/ai-framework/openapi.yaml"
      - key: "apb-tech-discovery"
        name: "APB Tech Discovery"
        description: "Análisis técnico y de deuda de proyectos"
        prompt: "Invoca el framework APB para análisis de estado técnico..."
      - key: "apb-documentation"
        name: "APB Documentación"
        description: "Generación y actualización de documentación en Confluence"
        prompt: "Invoca el framework APB para generar documentación técnica y funcional..."
```

La Forge App se publica en el marketplace privado del tenant Atlassian APB — no visible externamente.

---

## Capacidades de Rovo aprovechadas por el framework

| Capacidad Rovo | Cómo la usa el framework |
|---------------|--------------------------|
| **Búsqueda semántica** en Confluence/Jira | `apb-disc-reverse-doc-v1.0` la usa para encontrar documentación existente antes de generar nueva |
| **Resumen automático** de espacios Confluence | `apb-agent-documentation-v1.0` la usa para detectar qué secciones están desactualizadas |
| **Análisis de patrones** en tickets Jira | `apb-agent-spec-engineer-v1.0` la usa para extraer requisitos implícitos del historial |
| **Chat con contexto de proyecto** | `apb-agent-tech-discovery-v1.0` la usa para preguntas sobre el estado actual |
| **Detección de duplicados** en issues | `apb-agent-tech-debt-v1.0` la usa para identificar incidencias repetidas sin resolver |

---

## Limitaciones del runtime Rovo

| Limitación | Implicación |
|-----------|-------------|
| Los Rovo Agents solo ven el contexto del tenant Atlassian APB | No pueden acceder directamente a repos GitHub ni a SharePoint — el framework es el puente |
| Las respuestas en Rovo son texto + tablas básicas | Artefactos complejos (HTML, mockups) se entregan via Confluence/SharePoint, no inline |
| La Forge App requiere revisión y aprobación por el administrador Atlassian APB | Arquitectura APB debe publicar la app antes de que los usuarios la vean |
| Rovo no puede ejecutar código Python/JS | Las skills de ejecución usan el runtime de Claude; Rovo solo recibe el resultado |
| Cuota de llamadas Rovo API sujeta a plan de licencia Atlassian | Verificar límites de rate con el proveedor antes de activar en producción |

---

## Pasos de activación (pendiente — julio 2026)

1. **Confirmar disponibilidad de Rovo API** en el tenant Atlassian APB (previsto julio 2026)
2. **Desarrollar la Forge App** con los tres Rovo Agents descritos arriba
3. **Publicar en marketplace privado** del tenant Atlassian APB
4. **Aprobar la app** como administrador Atlassian
5. **Piloto con equipo de Arquitectura** antes de roll-out general
6. **Documentar en `docs/rovo-getting-started.md`** para usuarios finales

---

## Restricciones

- Los Rovo Agents no pueden aprobar sus propios artefactos — la aprobación siempre requiere acción humana explícita, coherente con `SYSTEM.md §2.1`
- Todo artefacto generado a través de Rovo lleva el aviso visible `Generado por APB AI Framework` en la página Confluence o ticket Jira de destino
- Los datos personales procesados en Rovo se rigen por las mismas políticas RGPD que el resto del framework (`context/apb/policies/compliance/`)
- Este adapter sustituye el mecanismo manual de copiar prompts del framework en Rovo — no crea un segundo framework paralelo

---

> **Generado por IA:** Claude (Anthropic/Claude Code), Sesión 15 del plan APB-IA-FRAMEWORK.
> **Validado por humano:** _pendiente — completar nombre/rol del validador antes de pasar a `candidate`._
