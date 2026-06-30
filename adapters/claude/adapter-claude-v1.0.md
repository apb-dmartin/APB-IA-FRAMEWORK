---
id: "adapter-claude-v1.0"
name: "Claude (Anthropic) Adapter"
description: "Adaptador que permite que los agentes, skills y workflows del framework APB se ejecuten en el runtime de Claude (Anthropic). Soporta Claude Code, Claude Desktop, y API de Anthropic."
version: "1.0.0"
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
review_date: "2026-06-22"
---

# Claude (Anthropic) Adapter

---

## 🎯 Propósito

Adaptador que permite que los agentes, skills y workflows del framework APB se ejecuten en el runtime de Claude (Anthropic). Soporta Claude Code, Claude Desktop, y API de Anthropic.

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

---
*Documento generado por el APB AI Framework. Requiere revisión humana antes de aprobación.*
