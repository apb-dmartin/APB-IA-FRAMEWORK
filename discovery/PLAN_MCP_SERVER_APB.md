# Plan — APB Agents MCP Server (Fases 0-7)

> **Procedencia:** consolidado de dos documentos entregados por Débora (sesión de
> arquitectura, 2026-07-07): `PLAN_MCP_SERVER_APB_v1.md` (Fase 0 / MVP) y
> `PLAN_MCP_SERVER_APB_FASES_1-7.md` (Fases 1-7). Integrado aquí como documento
> canónico único, siguiendo la regla de mantenimiento de
> [`PLAN_FASES_FUTURAS.md`](PLAN_FASES_FUTURAS.md) ("no crear documentos de
> handoff/resumen/estado sueltos... si algo necesita vida propia por volumen, se
> archiva con puntero desde los 3 documentos canónicos"). Contenido íntegro, sin
> resumir (regla de conservación de `TEST_PLAN_STANDARD §3.1`, aplicada aquí por
> analogía: unificar nunca elimina información).
>
> **Punteros desde los documentos canónicos:** ver `PLAN_FASES_FUTURAS.md`
> Sección A (bloqueantes MCP-1 a MCP-4) y Sección B (Fase 0, ligada a **N8**), y
> `CONTINUIDAD_PROYECTO.md` Sesión 27.

---

## Fase 0 — MVP local (contenido íntegro de `PLAN_MCP_SERVER_APB_v1.md`)

> **Audiencia:** Claude Code, ejecutando en local sobre el repo `APB-IA-FRAMEWORK`.
> **Objetivo de esta fase:** contenedor local funcional, sin desplegar a Azure todavía.
> **Autor del plan:** sesión de arquitectura con Débora (Arquitectura APB), 2026-07-07.

### 0. Contexto obligatorio para Claude Code

Antes de escribir código, lee estos archivos del repo para entender el formato real de los agentes:

- `agents/apb-agent-ddd-v1.0.md` — ejemplo de agente con frontmatter YAML completo
- `agents/apb-agent-meta-builder-v1.0.md` — otro ejemplo de agente
- `providers/prov-apb-knowledge-v1.0.md` — define dónde vive el conocimiento corporativo
- `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` — el documento que hay que poder consultar
- `scripts/invoke_agent.py` — muestra cómo se parsea el frontmatter hoy (referencia, no reutilizar tal cual — es un simulador)
- `context/apb/SCHEMA.md` — esquema formal de metadatos de cada componente

**No inventes campos de frontmatter que no existan en los archivos reales.** Verifica contra los `.md` reales, no contra lo que este plan describa de memoria.

> **Verificación 2026-07-07 (al consolidar este documento):** los 5 ficheros de
> contexto de arriba se releyeron contra el repo real antes de escribir este
> documento. El frontmatter de `agents/apb-agent-ddd-v1.0.md` coincide con lo
> descrito aquí (`id/name/description/version/status/owner/domain/autonomy_level/
> skills/subagents/runtime/depends_on/human_review_points/created_date/
> review_date`), y el fichero contiene efectivamente **dos** bloques "Prompt de
> Sistema" — el segundo (bajo el heading `## Prompt de Sistema`, tras "🔄
> Historial de Cambios") es el consolidado que generó
> `scripts/generate_system_prompts.py` (Sesión KB+SP) y es el que debe devolver
> `get_agent_instructions` (§4.2). `context/apb/SCHEMA.md` está en `context/apb/`,
> no en la raíz — confirmar la ruta exacta al implementar `repo_paths.py`.

### 1. Objetivo del MVP

Construir un servidor MCP (Model Context Protocol) que permita a un usuario en **Claude Code** o **GitHub Copilot** (con el MCP configurado) invocar agentes del APB AI Framework **sin clonar el repositorio**, leyendo la definición de los agentes desde un backend controlado por APB.

Este MVP corre en **local, en Docker**, sin desplegar a Azure todavía. El destino final de infraestructura es **Azure Container Apps** (decisión ya tomada, fuera del alcance de esta fase).

### 2. Alcance de esta fase — explícito

#### Dentro de alcance (v1)
- Servidor MCP con **exactamente 3 tools** (ver sección 4)
- Transporte: `streamable-http` (no `stdio`, no SSE legacy)
- Servidor **stateless** — cada request se resuelve leyendo del filesystem, sin memoria entre llamadas
- Lenguaje: **Python**, usando el SDK oficial de MCP (`mcp` en PyPI)
- Contenedor Docker que corre el servidor localmente
- Prueba manual con **MCP Inspector** (`npx @modelcontextprotocol/inspector`)
- Prueba de conexión real desde Claude Code local

#### Fuera de alcance (v1) — NO implementar, aunque parezca fácil añadirlo
- ❌ Autenticación (Entra ID llega en la fase de despliegue a Azure, no antes)
- ❌ Telemetría/auditoría a Azure Monitor (requiere credenciales que no existen en esta fase)
- ❌ Gestión de estado o sesión entre llamadas (decisión explícita — ver nota de gobernanza abajo)
- ❌ Tools adicionales más allá de las 3 listadas
- ❌ Despliegue a Azure Container Apps (fase posterior, no confundir)
- ❌ Integración con GitHub Copilot o Rovo en esta fase (se prueba solo con MCP Inspector y Claude Code)

> **Nota de gobernanza:** si en algún punto de la implementación parece "conveniente" añadir estado, caché persistente entre requests, o cualquier otra cosa fuera de esta lista, **detente y pregúntale a Débora antes de añadirlo**. No asumas necesidad no confirmada — consistente con el principio `apb-dev-simplicity-first-v1.0` ya vigente en este framework.

### 3. Estructura de proyecto propuesta

```
apb-mcp-server/
├── Dockerfile
├── requirements.txt
├── src/
│   ├── server.py              # Entry point, inicialización del servidor MCP
│   ├── tools/
│   │   ├── list_agents.py
│   │   ├── get_agent_instructions.py
│   │   └── get_apb_knowledge.py
│   └── lib/
│       ├── frontmatter.py     # Parser de YAML frontmatter (reutilizar lógica de invoke_agent.py)
│       └── repo_paths.py      # Resolución de rutas al repo APB-IA-FRAMEWORK
├── tests/
│   └── test_tools.py
└── README.md
```

El repo `APB-IA-FRAMEWORK` se monta como **volumen de solo lectura** dentro del contenedor (no se copia, no se clona dentro de la imagen — se monta desde el host). Esto es intencional: en local, el contenedor lee del checkout real de Débora; en producción (fase futura), leerá de donde Arquitectura decida servir el contenido versionado.

### 4. Especificación de los 3 tools

#### 4.1 `list_agents`

**Descripción:** Lista todos los agentes disponibles en el catálogo, con sus metadatos básicos.

**Input:** ninguno (o `domain` opcional para filtrar)

```python
class ListAgentsInput(BaseModel):
    domain: str | None = Field(default=None, description="Filtrar por dominio funcional, ej. 'architecture', 'governance'")
```

**Output:**
```json
{
  "agents": [
    {
      "id": "apb-agent-ddd-v1.0",
      "name": "DDD Domain Discovery Agent",
      "description": "...",
      "domain": "architecture",
      "status": "draft",
      "autonomy_level": 1,
      "human_review_points": ["..."]
    }
  ],
  "total": 37
}
```

**Implementación:** leer todos los `.md` de `agents/`, parsear frontmatter YAML (reutilizar la lógica de `scripts/invoke_agent.py::load_frontmatter`), devolver metadatos. **Nunca devolver el prompt de sistema completo en este tool** — eso es responsabilidad de `get_agent_instructions`.

**Anotaciones MCP:** `readOnlyHint: true`, `idempotentHint: true`

#### 4.2 `get_agent_instructions`

**Descripción:** Devuelve el prompt de sistema completo de un agente específico, para que el cliente (Claude Code, Copilot) lo cargue como contexto activo.

**Input:**
```python
class GetAgentInstructionsInput(BaseModel):
    agent_id: str = Field(description="ID exacto del agente, ej. 'apb-agent-ddd-v1.0'. Usa list_agents para obtener IDs válidos.")
```

**Output:**
```json
{
  "agent_id": "apb-agent-ddd-v1.0",
  "name": "DDD Domain Discovery Agent",
  "system_prompt": "Eres el agente \"DDD Domain Discovery Agent\"...",
  "autonomy_level": 1,
  "human_review_points": ["..."],
  "human_review_required": true
}
```

**Implementación:** localizar el archivo `agents/{agent_id}.md`, extraer la sección "Prompt de Sistema" (la segunda ocurrencia en el archivo — verificado contra `apb-agent-ddd-v1.0.md`, tiene dos bloques de prompt, el segundo es el consolidado). Si el `agent_id` no existe, devolver error accionable: *"Agente '{agent_id}' no encontrado. Usa la tool list_agents para ver los IDs válidos."* — no un error genérico.

**Anotaciones MCP:** `readOnlyHint: true`, `idempotentHint: true`

#### 4.3 `get_apb_knowledge`

**Descripción:** Busca en la base de conocimiento corporativo APB (negocio portuario, sistemas, terminología) para dar contexto a un agente en ejecución.

**Input:**
```python
class GetApbKnowledgeInput(BaseModel):
    query: str = Field(description="Consulta en lenguaje natural sobre negocio o sistemas APB")
```

**Output:**
```json
{
  "query": "...",
  "content": "fragmento relevante del documento",
  "source": "context/apb/knowledge/APB_KNOWLEDGE_BASE.md"
}
```

**Implementación v1 (simplificada, sin RAG todavía):** cargar el documento completo `APB_KNOWLEDGE_BASE.md` y devolverlo tal cual, o hacer un match simple por keyword. **No implementar búsqueda semántica/embeddings en esta fase** — es over-engineering para un documento único. Si el documento crece mucho, eso se resuelve en una fase posterior, no ahora.

**Anotaciones MCP:** `readOnlyHint: true`, `idempotentHint: true`

### 5. Dependencias

```
mcp>=1.0.0
pydantic>=2.0
pyyaml>=6.0
```

No añadir más dependencias sin justificarlo explícitamente.

### 6. Dockerfile — requisitos

- Imagen base: `python:3.12-slim`
- Debe exponer el servidor vía `streamable-http` en un puerto configurable (default 8000)
- El repo APB-IA-FRAMEWORK se monta como volumen en `/repo` (read-only) — **no se copia dentro de la imagen**
- Variable de entorno `APB_REPO_PATH=/repo` para que el código sepa dónde leer

Ejemplo de arranque esperado:
```bash
docker run -p 8000:8000 -v /ruta/local/APB-IA-FRAMEWORK:/repo:ro apb-mcp-server
```

### 7. Testing

1. **Compilación/sintaxis:** `python -m py_compile src/server.py` antes de considerar cualquier tool terminado.
2. **MCP Inspector:** `npx @modelcontextprotocol/inspector` conectado al servidor local — verificar que las 3 tools aparecen con sus schemas correctos y que cada una devuelve output válido con al menos un agente real del repo (ej. probar con `apb-agent-ddd-v1.0`).
3. **Prueba real con Claude Code:** configurar el servidor MCP local en la configuración de Claude Code y pedir explícitamente: *"Usa la tool get_agent_instructions para cargar el agente apb-agent-ddd-v1.0 y resume su propósito"* — verificar que el flujo completo funciona end-to-end.

### 8. Checklist de "hecho" (antes de reportar como completo)

- [ ] Las 3 tools implementadas, cada una con su Pydantic model de input
- [ ] Ningún tool añadido fuera de los 3 especificados
- [ ] Ninguna gestión de estado implementada
- [ ] Ninguna autenticación implementada
- [ ] `python -m py_compile` pasa sin errores en todos los archivos
- [ ] MCP Inspector muestra las 3 tools correctamente
- [ ] Al menos una llamada real a cada tool devuelve datos reales del repo (no mocks)
- [ ] Dockerfile construye y el contenedor arranca sin errores
- [ ] README.md del proyecto explica cómo levantar el contenedor y conectarlo a Claude Code

### 9. Fuera de esta fase — para que Claude Code NO lo toque salvo instrucción explícita

- Despliegue a Azure Container Apps
- Autenticación Entra ID
- Telemetría a Azure Monitor
- Integración con GitHub Copilot (requiere config adicional en el cliente, no en el servidor)
- Forge App para Rovo (arquitectura completamente distinta — REST/webhook, no MCP)
- Cualquier forma de estado o memoria entre llamadas

### 10. Pregunta abierta para Débora (no para Claude Code)

Si durante la implementación aparece una necesidad real y concreta de estado (no especulativa), Claude Code debe **detenerse y documentar el caso de uso específico** antes de implementar nada — Débora decide si se añade en v1 o se pospone.

---

## Fases 1-7 (contenido íntegro de `PLAN_MCP_SERVER_APB_FASES_1-7.md`)

> **Relación con la Fase 0:** este bloque complementa la Fase 0 de arriba. No la
> duplica.
> **Autor:** sesión de arquitectura con Débora (Arquitectura APB), 2026-07-07.
> **Advertencia de origen:** las Fases 1-7 de este documento se escribieron ANTES de tener evidencia del comportamiento real del MVP. Cada sección está etiquetada según su nivel de certeza. Claude Code y Débora deben revalidar cada fase `[Suposición]` con evidencia real antes de implementarla — no ejecutar directamente sobre fe.

### Leyenda de confianza usada en este documento

- **[Seguro]** — verificado contra documentación oficial (Microsoft Learn, GitHub Docs, Atlassian Docs) o contra el repo real de APB, con fecha de verificación.
- **[Probable]** — inferencia razonable a partir de evidencia parcial, pero no confirmada al 100%.
- **[Suposición]** — decisión de diseño sin caso de uso real confirmado. Debe tratarse como borrador, no como especificación cerrada.

### Fase 0 — MVP local (referencia)

Ver sección "Fase 0 — MVP local" arriba en este mismo documento. No se repite aquí. Debe completarse y validarse (checklist de esa fase) antes de empezar la Fase 1.

### Fase 1 — Autenticación + Despliegue a Azure Container Apps

#### 1.1 Despliegue del contenedor **[Seguro]**

Azure Container Apps acepta directamente la imagen Docker construida en Fase 0, sin cambios de código — a diferencia de Azure Functions, no impone restricciones de transporte stateless. Verificado contra documentación de Azure Container Apps (soporta contenedores arbitrarios, ingress HTTP configurable, WebSockets/streaming nativo).

Pasos:
1. Publicar la imagen en Azure Container Registry (ACR)
2. Crear el Container App con ingress externo habilitado, puerto igual al que expone el servidor MCP (8000 por defecto según Fase 0)
3. Configurar réplicas mínimas ≥ 1 si se requiere disponibilidad continua (Container Apps puede escalar a 0, lo cual introduce latencia de arranque en frío — decisión de negocio, no técnica)

#### 1.2 Autenticación con Entra ID **[Probable — mecanismo verificado, integración específica con MCP pendiente de prueba real]**

Verificado: Azure Functions tiene "built-in MCP authentication" con Entra ID out-of-the-box. **No he verificado** que Azure Container Apps tenga un mecanismo equivalente igual de directo — Container Apps sí soporta autenticación integrada ("Easy Auth" / autenticación de plataforma) que valida tokens de Entra ID antes de que la request llegue al contenedor, pero la integración específica con el flujo de autorización de MCP (que exige devolver un `401` con metadata de recurso protegido, `WWW-Authenticate`, etc.) requiere prueba directa antes de asumir que "simplemente funciona".

**Acción para Claude Code**: antes de implementar esta fase, verificar con un prototipo mínimo si la autenticación de plataforma de Container Apps es compatible con el flujo de autorización MCP tal como lo esperan los clientes (Claude Code, Copilot), o si hace falta implementar el desafío `401`/PRM manualmente dentro del propio servidor MCP.

#### 1.3 Modelo de permisos **[Suposición — grupos concretos sin definir]**

Estructura propuesta de scopes en Entra ID:
- `apb-mcp.read` — puede listar agentes y consultar conocimiento (`list_agents`, `get_apb_knowledge`)
- `apb-mcp.execute` — puede obtener instrucciones completas de agentes (`get_agent_instructions`)

**No están definidos los grupos de Entra ID concretos que recibirán cada scope.** Esto requiere decisión de Débora/Arquitectura sobre qué equipos tienen qué nivel de acceso — no es una decisión técnica que Claude Code deba inventar.

### Fase 2 — Telemetría y auditoría centralizada

#### 2.1 Mecanismo de envío **[Seguro — reutiliza infraestructura ya existente en el repo]**

El repo ya tiene `scripts/emit_telemetry.py`, que envía a Azure Monitor (tabla `APBFrameworkTelemetry_CL`) usando `azure-monitor-ingestion` + `DefaultAzureCredential`. La Fase 2 consiste en instrumentar el servidor MCP para que, tras cada llamada a un tool, invoque esta misma lógica — no reinventar el mecanismo de envío, adaptar el existente.

#### 2.2 Esquema de evento **[Probable — campos base conocidos, campos específicos de MCP sin confirmar con evidencia real]**

Campos que ya usa el framework (conocidos por `emit_telemetry.py` y el `TELEMETRY_BLOCK` documentado en los agentes):
```json
{
  "TimeGenerated": "...",
  "invocation_id": "uuid",
  "component_id": "apb-agent-ddd-v1.0",
  "outcome": "success | failure",
  "user_id": "...",
  "ai_generated": true
}
```

**[Suposición]** — campos específicos que probablemente haga falta añadir para el contexto MCP (`tool_name`, `client_type: claude_code | copilot | rovo`, `latency_ms`) no están confirmados contra ningún caso de uso real. Definir tras observar las primeras invocaciones reales en Fase 0/1, no antes.

#### 2.3 Gap conocido — heredado del propio repo **[Seguro]**

El propio `docs/manual-arquitectura.md` de Débora ya documenta este gap (§2.3): la telemetría hoy es manual, depende de que el agente "decida" emitir el bloque. Con el MCP server, esto se resuelve de raíz porque la instrumentación pasa a ser automática en el servidor, no dependiente del agente. Esta fase cierra un gap ya diagnosticado previamente, no es trabajo nuevo sin precedente.

### Fase 3 — Ampliación de tools (catálogo completo)

#### 3.1 Candidatos a nuevas tools **[Probable — basado en el inventario real del repo, no en especulación]**

Basado en el inventario verificado del repo (`docs/manual-arquitectura.md` §1.2 en su momento; el inventario real a 2026-07-06 es de 347 componentes, ver `CONTINUIDAD_PROYECTO.md` §23 — el número exacto debe reverificarse con `scripts/generate_catalog.py --check` en el momento de implementar esta fase, no asumir la cifra de este párrafo). No se exponen todos de golpe — criterio de priorización sugerido:

1. `list_skills(domain?)` — análogo a `list_agents`, para las skills APB-owned
2. `get_skill_definition(skill_id)` — análogo a `get_agent_instructions`
3. `list_workflows()` — los workflows, con sus `human_checkpoints`
4. `query_domain_catalog(query)` — cuando `APB-DOMAIN-CATALOG` tenga contenido real (gap 2.5 del informe de arquitectura — **no tiene sentido exponer esta tool antes de que el catálogo tenga dominios reales**; ver estado real en `PLAN_FASES_FUTURAS.md` fila DDD/#38 F0, dominios en estado `proposed` pendientes de aprobación de Arquitectura)

#### 3.2 Orden de prioridad **[Suposición — sin confirmar con Débora]**

Prioridad propuesta: skills de `development` primero (dominio con más volumen), luego `governance` (incluye `apb-gov-ai-risk-gate-v1.0` que ya usan varios agentes). **Débora debe confirmar o corregir este orden** — no hay evidencia de qué necesita el departamento de IT primero.

### Fase 4 — Integración con GitHub Copilot

#### 4.1 Configuración del lado cliente **[Seguro — verificado contra documentación oficial de GitHub, julio 2026]**

No requiere cambios en el servidor MCP más allá de lo ya construido en Fase 0-1. GitHub Copilot soporta servidores MCP remotos vía HTTP con OAuth, configurables en VS Code, Visual Studio, JetBrains y Copilot CLI.

Configuración esperada en `.vscode/mcp.json` o equivalente por IDE:
```json
{
  "servers": {
    "apb-agents": {
      "type": "http",
      "url": "https://<container-app-fqdn>/mcp",
      "headers": { "Authorization": "Bearer ${input:apb_token}" }
    }
  }
}
```

#### 4.2 Límite importante — no ignorar **[Seguro — confirmado contra documentación oficial de GitHub]**

**Copilot Cloud Agent y Copilot Code Review NO soportan `resources` ni `prompts` de MCP — solo `tools`.** Como las 3 tools de Fase 0 ya están diseñadas como `tools` (no como `resources`/`prompts`), esto no bloquea nada, pero es la razón de diseño por la que se evitó depender de esas primitivas desde el principio. No cambiar esto en fases posteriores sin volver a verificar compatibilidad.

#### 4.3 Política de organización **[Suposición — depende de administración GitHub de APB, fuera del control de Arquitectura]**

La política "MCP servers in Copilot" está deshabilitada por defecto a nivel organización/enterprise. Alguien con rol de administrador de la organización GitHub de APB debe habilitarla explícitamente y añadir el servidor a la allowlist. **Esto no lo puede resolver Claude Code ni Arquitectura — requiere al administrador de GitHub Enterprise/Business de APB.**

### Fase 5 — Forge App para Rovo

#### 5.1 Estado — bloqueada, no implementar sin verificación previa **[Suposición — pendiente de verificación explícita]**

**No confirmado**: si Rovo (como cliente de chat en Jira/Confluence) puede conectarse a un servidor MCP de terceros de la misma forma que Claude Code o Copilot. Lo que sí está confirmado es que el "Rovo MCP Server" oficial de Atlassian es **su** servidor (para que cualquier IA consuma datos de Jira/Confluence), no un mecanismo para publicar agentes de terceros dentro de Rovo.

**Acción previa obligatoria**: verificar contra un tenant real de Atlassian (Débora o alguien con acceso) si Forge soporta declarar un `rovo:agent` que consuma un MCP server externo como tool, o si la única vía sigue siendo el patrón REST/webhook que ya está scaffolded en `forge/manifest.yml`.

> **Nota de consolidación (2026-07-07):** desde que se escribió este párrafo, el
> framework aclaró (Sesión 26, Workstream 3/4 de `CONTINUIDAD_PROYECTO.md`) que
> **ni `prov-atlassian-v1.0` ni `prov-jira-software-v1.0` usan MCP ni Rovo como
> transporte** — son REST CRUD puro. La integración real de Rovo vive en
> `adapters/rovo/adapter-rovo-v1.0.md` (pendiente de activación en APB, julio
> 2026). Esta Fase 5.1 sigue sin resolverse: la pregunta de si Forge puede
> declarar un `rovo:agent` que consuma este MCP server externo (en vez de REST)
> no se ha verificado contra un tenant real. Ver también el punto **#78** de
> `PLAN_FASES_FUTURAS.md` (tagging de agentes que pueden apoyarse en Rovo).

#### 5.2 Si la verificación confirma que Forge = REST/webhook únicamente **[Probable, condicional al resultado de 5.1]**

En ese caso, esta fase **no reutiliza el servidor MCP en absoluto**. Es una integración aparte:
- El `forge/manifest.yml` ya existente define `rovo:agents` con prompts embebidos que llaman a `POST /agents/{id}/invoke` en la API REST (`openapi/apb-framework-api.yaml`)
- Esto implica que, para Rovo, **sí necesitas construir el backend REST que se descartó como prioridad en esta conversación** — es una arquitectura paralela al MCP server, no una extensión de él
- Alcance mínimo: solo los agentes que Débora priorice para uso desde Jira/Confluence (no todos los agentes de golpe)

#### 5.3 Consecuencia para el orden de trabajo **[Seguro — es lógica de dependencia, no opinión]**

Si 5.1 confirma que Rovo necesita REST y no MCP, esto significa que "los 3 canales en paralelo" que se pidió en esta sesión implica **dos arquitecturas de backend distintas construidas simultáneamente**, no una. Debe decidirse si se secuencia (MCP primero para Claude Code/Copilot, REST después para Rovo) o se reparten entre dos personas/sesiones de Claude Code en paralelo.

### Fase 6 — Routing a LLM específico por skill

#### 6.1 Estado — sin caso de uso confirmado **[Suposición — Débora no confirmó ningún caso concreto]**

Esta fase se documenta como **arquitectura preparada, no como necesidad validada**. En la sesión de origen se mencionó la idea general ("si un agente sabe que tiene que hacer análisis de código, que vaya a un LLM adecuado"), pero no se identificó ninguna skill específica con esa necesidad real hoy.

#### 6.2 Mecanismo propuesto, condicional a que aparezca un caso real **[Suposición]**

Si en el futuro aparece una skill que necesite forzar un modelo específico (independientemente del cliente que la invoque), el mecanismo sería:

```python
# Dentro de la implementación de una tool específica, NO en el servidor MCP en general
async def run_specialized_analysis(input: SpecializedAnalysisInput):
    # Esta tool, a diferencia de las 3 de Fase 0, SÍ hace una llamada de servidor a servidor
    result = await call_anthropic_api(model="claude-sonnet-4-6", prompt=...)
    return result
```

Esto es una decisión **por tool individual**, no una capa de "routing" genérica y centralizada. No construir un motor de routing especulativo — cuando aparezca la primera tool real que lo necesite, se implementa para esa tool concretamente.

#### 6.3 Coste no resuelto **[Suposición — depende de la Fase 1 de tokenización que Débora dejó en "depende de quién asuma los tokens"]**

Si esta fase se activa, **APB paga esos tokens directamente** (llamada servidor a servidor con su propia API key), a diferencia de las 3 tools de Fase 0 donde el modelo lo paga el cliente (Copilot/Claude Code con su propia licencia). Esto tiene implicación de costo que Débora debe aceptar explícitamente antes de implementar, no algo que se decida en código.

### Fase 7 — Gobernanza del catálogo del MCP server

#### 7.1 Ciclo de publicación **[Probable — coherente con el ciclo draft→candidate→approved ya vigente en el repo, pero no probado en este contexto específico]**

El framework ya define el ciclo `draft → candidate → under_review → approved` (`SYSTEM.md §2.4`, `GOVERNANCE.md`). Propuesta de aplicación al MCP server:

- Un agente en estado `draft` o `candidate` **no aparece** en `list_agents()` salvo que el usuario tenga un scope especial de "preview"
- Solo agentes en `approved` son visibles por defecto para el departamento de IT general
- Esto requiere que `list_agents` filtre por `status` — cambio menor sobre la Fase 0, pero **no implementarlo en Fase 0** porque hoy el 100% de los componentes del repo están en `draft` (0 aprobados, ver `CONTINUIDAD_PROYECTO.md` §23/§24) y filtrar por `approved` dejaría el catálogo vacío. Esta fase solo tiene sentido después de que Arquitectura apruebe formalmente al menos algunos componentes.

#### 7.2 Quién decide qué se publica **[Seguro — ya está definido en el propio repo, no es una decisión nueva]**

Ya confirmado: solo Arquitectura publica; otros equipos proponen vía meta-builder + Jira. El MCP server no cambia esa gobernanza — es un canal de distribución adicional del mismo catálogo gobernado, no una vía paralela para saltarse el proceso.

### Resumen de bloqueantes reales antes de avanzar más allá de Fase 0

| Fase | Bloqueante | Quién debe resolverlo |
|---|---|---|
| 1.2 | Verificar compatibilidad real de auth MCP + Entra ID en Container Apps | Claude Code, con prototipo |
| 1.3 | Definir grupos de Entra ID por scope | Débora / Arquitectura |
| 3.2 | Confirmar orden de prioridad de skills a exponer | Débora |
| 5.1 | Verificar si Rovo consume MCP externo o requiere REST | Débora, con acceso a tenant Atlassian |
| 6.1 | Identificar caso de uso real de routing a LLM específico | Débora |

**Ninguna de estas 5 filas debe resolverse "por defecto" en código. Son decisiones, no bugs.**

---

## Vínculos con el resto del framework APB (añadido al consolidar, 2026-07-07)

- **N8** (`PLAN_FASES_FUTURAS.md` Sección A): este MCP server **es** el mecanismo
  de invocación real por runtime que hoy falta — actualmente solo existe
  `scripts/invoke_agent.py`, un simulador. La Fase 0 de este documento resuelve
  N8 para Claude Code local; las Fases 1 y 4 lo extienden a producción y a
  GitHub Copilot respectivamente. Rovo queda aparte (ver Fase 5).
- **#78** (tagging de agentes `runtime: rovo`) y `adapters/rovo/adapter-rovo-v1.0.md`:
  relacionados con la Fase 5 (Forge/Rovo) de este documento — ambos bloqueados
  por la misma pregunta de fondo (¿Rovo consume MCP externo o requiere REST?).
- **P1-P6** (`PLAN_FASES_FUTURAS.md` Sección B.2, "Providers/MCP sin cubrir"):
  no se solapan con este documento — aquellos son providers hacia sistemas
  externos (JSM, Intune, Power BI, backup, Document Intelligence, Power
  Automate); este MCP server expone el propio catálogo de agentes/skills APB
  como tools, en la dirección contraria.
- **HANDOFF_TECNICOS.md**: el despliegue real a Azure Container Apps (Fase 1)
  es trabajo de producción que requiere a Plataforma/Ciberseguridad — se
  registra ahí una vez haya decisión de motor de orquestación (#77) y del
  resto de bloqueantes de la tabla de arriba, no antes.
- **Skill de terceros añadida en la misma sesión, sin relación con este MCP
  server:** `skills/third_party/roboflow/third-roboflow-supervision-v1.0.md`
  (visión artificial, Roboflow `supervision`) — incorporada a petición
  explícita de Débora, sin caso de uso ni conexión con este servidor MCP. Se
  documenta aquí solo para que quede constancia de que ambas peticiones de la
  misma sesión (2026-07-07) se resolvieron por separado, tal como se decidió
  explícitamente en la aclaración de alcance previa a este documento.
