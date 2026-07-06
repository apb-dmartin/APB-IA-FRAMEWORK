---
id: "adapter-claude-v1.0"
name: "Claude (Anthropic) Adapter"
description: "Adaptador que permite que los agentes, skills y workflows del framework APB se ejecuten en el runtime de Claude (Anthropic). Soporta Claude Code, Claude Desktop, y API de Anthropic."
version: "1.2.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "orchestration"
runtime_target: "claude"
adapted_components:
  - "apb-dev-code-review-v1.0"
  - "apb-dev-implement-v1.0"
  - "apb-arch-design-v1.0"
  - "apb-sec-threat-model-v1.0"
  - "apb-agent-implementer-v1.0"
  - "apb-wf-sdd-full-v1.0"
  - "prov-azure-v1.0"
created_date: "2026-06-20"
review_date: "2026-07-03"
---

# Claude (Anthropic) Adapter

---

## 🎯 Propósito

Adaptador que permite que los agentes, skills y workflows del framework APB se ejecuten en el runtime de Claude (Anthropic). Soporta Claude Code, Claude Desktop, y API de Anthropic.

**Punto de entrada real:** `CLAUDE.md` (raíz del repo, auto-leído por Claude Code) es
un fichero delgado que remite a [`AGENTS.md`](../../AGENTS.md) — la fuente única de
reglas, agnóstica de LLM y herramienta (`SYSTEM.md §4.3`, `§10.1`). Este adapter
documenta el mapeo de *capacidades* al runtime de Claude; las *reglas* no viven aquí.

## 🔧 Runtime Soportado

Claude 3.5/4 Sonnet/Opus via Anthropic API, Claude Code CLI, Claude Desktop App. Soporta tool use, computer use, y extended thinking.

## 📦 Componentes Adaptados

| Tipo | Componente | ID | Estado |
|------|-----------|-----|--------|
| Skill | `apb-dev-code-review-v1.0` | ✅ Adaptado | Tool use + file context |
| Skill | `apb-dev-implement-v1.0` | ✅ Adaptado | Tool use + file editing |
| Skill | `apb-arch-design-v1.0` | ✅ Adaptado | Extended thinking + context |
| Skill | `apb-sec-threat-model-v1.0` | ✅ Adaptado | Extended thinking |
| Agent | `apb-agent-implementer-v1.0` | ✅ Adaptado | Multi-turn con tool use |
| Workflow | `apb-wf-sdd-full-v1.0` | ✅ Adaptado | Multi-agent orchestration |
| Provider | `prov-azure-v1.0` | ✅ MCP | Azure MCP nativo |
| Provider | `prov-atlassian-v1.0` | ⚠️ Parcial | Sin conector MCP de Atlassian confirmado en este runtime a fecha 2026-07-06 — usar REST directo (api_token vía AKV) hasta confirmar disponibilidad de un servidor MCP de Atlassian en el tenant APB. Actualizar esta fila en cuanto se confirme |
| Provider | `prov-confluence-v1.0` | ⚠️ Parcial | Mismo estado que `prov-atlassian-v1.0` — REST v2/OAuth2 directo hasta confirmar MCP |

## 🔌 Interface de Adaptación

### Mapeo de Skills a Claude Tools
Las skills APB se traducen a herramientas (tools) de Claude con esquemas JSON.

### Contexto de Repositorio
Claude Code accede al contexto mediante:
- `Read` tool para archivos
- `Edit` tool para modificaciones
- `Bash` tool para comandos
- `Glob` tool para búsqueda de archivos

### Invocación de Agentes
Los agentes se invocan mediante:
- Prompts estructurados con system instructions
- Tool use para acciones específicas
- Multi-turn conversations para workflows complejos

### Integración con MCP
- Azure MCP para acceso a recursos Azure
- GitHub MCP para operaciones de repo
- SonarQube MCP para análisis de calidad
- Atlassian (Jira/Confluence): sin servidor MCP confirmado en el tenant APB a fecha
  2026-07-06 — `prov-atlassian-v1.0`/`prov-confluence-v1.0` operan hoy vía REST directo
  (api_token/OAuth2 en AKV). Si en el futuro se confirma un servidor MCP de Atlassian
  disponible para el tenant, migrar aquí siguiendo el mismo patrón que Azure/GitHub/Sonar
  — no confundir con `adapter-rovo-v1.0` (capa de IA de Rovo, mecanismo distinto,
  pendiente de activación julio 2026)

## ⚙️ Configuración

```json
{
  "claude": {
    "model": "claude-sonnet-4-6",
    "max_tokens": 8192,
    "thinking": {
      "enabled": true,
      "budget_tokens": 4096
    },
    "tools": [
      "Read", "Edit", "Bash", "Glob",
      "mcp-azure", "mcp-github", "mcp-sonar"
    ],
    "skills_mapping": {
      "apb-dev-code-review": {
        "tool": "Read",
        "follow_up": ["Edit"]
      },
      "apb-arch-design": {
        "thinking": true,
        "tool": "Bash"
      }
    },
    "agents_context": {
      "system_prompt_template": "claude-agent-template.md",
      "max_context_files": 20
    }
  }
}
```

## 🔄 Mapeo de Capacidades

| Capacidad APB | Capacidad Claude | Mapeo |
|---------------|------------------|-------|
| Code Review | Read + Edit tools | Directo |
| Implementación | Edit + Bash tools | Directo |
| Diseño de Arquitectura | Extended thinking | Nativo |
| Testing | Bash tool (ejecución tests) | Directo |
| Documentación | Write tool | Directo |
| Threat Modeling | Extended thinking | Nativo |
| CI/CD | Bash tool + MCP | Adaptado |
| Infraestructura | MCP Azure + Bash | Adaptado |

## 📥 Formato de Input

### Formato de Input
```yaml
adapter: claude
agent: apb-agent-technical-architect-v1.0
skill: apb-arch-design-v1.0
context:
  files:
    - "ddd-model.md"
    - "system-spec.md"
  thinking: true
  mcp_providers:
    - "azure"
    - "github"
```

## 📤 Formato de Output

### Formato de Output
```yaml
adapter: claude
agent: apb-agent-technical-architect-v1.0
skill: apb-arch-design-v1.0
results:
  thinking_summary: "Análisis de arquitectura completado en 3 pasos..."
  artifacts_generated:
    - file: "architecture-design.md"
      tool: "Write"
    - file: "c4-level1.svg"
      tool: "Bash" (generado via plantuml)
  recommendations:
    - "Considerar API Gateway para centralizar autenticación"
    - "Implementar circuit breaker en comunicación con servicio externo"
  confidence: "high"
```

## 🚫 Limitaciones del Runtime

- Claude Code requiere instalación local y acceso a repositorio
- Extended thinking consume tokens adicionales (coste superior)
- Tool use tiene latencia adicional por llamadas a herramientas
- No soporta ejecución de código en sandbox sin configuración
- Las skills de Nivel 2 requieren confirmación humana para acciones destructivas
- MCP providers requieren configuración de credenciales

## 🔒 Seguridad

- Las credenciales MCP se configuran via AKV references
- No se almacenan secretos en prompts de Claude
- El contexto se filtra para no incluir datos PII
- Cumple con políticas de datos de Anthropic
- Auditoría de interacciones via Claude Console

## 📝 Ejemplo de Uso

```yaml
adapter: Claude (Anthropic)
runtime: Claude (Anthropic)
config:
  adapter: "claude"
  agent: "apb-agent-implementer-v1.0"
  skill: "apb-dev-implement-v1.0"
  context:
    repo: "/repos/tributos-service"
    spec: "system-spec.md"
    architecture: "architecture-design.md"
  tools:
    - "Read"
    - "Edit"
    - "Bash"
  mcp:
    - "github"
    - "azure"
  thinking: false
  output_format: "file-edits"
```

## 🔄 Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-21 | Arquitectura APB | Creación inicial |
| 1.1.0 | 2026-07-03 | Arquitectura APB | Aclarado que `CLAUDE.md` deriva de `AGENTS.md` (routing file raíz agnóstico, `SYSTEM.md §10.1`); check #22 de `validate_repo.py` verifica que no diverjan. |
| 1.2.0 | 2026-07-06 | Claude (Anthropic), a petición de Débora | Corregido un hueco: `prov-atlassian-v1.0`/`prov-confluence-v1.0` no aparecían en este adapter pese a que Azure/GitHub/Sonar sí tenían su mapeo MCP explícito. Añadidos como "⚠️ Parcial" (REST directo, sin conector MCP de Atlassian confirmado en este runtime) — no confundir con `adapter-rovo-v1.0`, un mecanismo distinto y aún no activo en APB. |

---
*Documento generado por el APB AI Framework. Requiere revisión humana antes de aprobación.*
