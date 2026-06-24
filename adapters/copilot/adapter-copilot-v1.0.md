---
id: "adapter-copilot-v1.0"
name: "GitHub Copilot Adapter"
description: "Adaptador que permite que los agentes, skills y workflows del framework APB se ejecuten en el runtime de GitHub Copilot. Traduce las capacidades del framework al formato de instrucciones y contexto de Copilot."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "orchestration"
runtime_target: "copilot"
adapted_components:
  - "apb-dev-code-review-v1.0"
  - "apb-dev-implement-v1.0"
  - "apb-arch-design-v1.0"
  - "apb-agent-implementer-v1.0"
  - "apb-wf-code-review-v1.0"
  - "prov-github-v1.0"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# GitHub Copilot Adapter

---

## 🎯 Propósito

Adaptador que permite que los agentes, skills y workflows del framework APB se ejecuten en el runtime de GitHub Copilot. Traduce las capacidades del framework al formato de instrucciones y contexto de Copilot.

## 🔧 Runtime Soportado

GitHub Copilot (VS Code, Visual Studio, JetBrains, Neovim). Soporta modo chat, inline completions, y Copilot Workspace.

## 📦 Componentes Adaptados

| Tipo | Componente | ID | Estado |
|------|-----------|-----|--------|
| Skill | `apb-dev-code-review-v1.0` | ✅ Adaptado | Review inline en PR |
| Skill | `apb-dev-implement-v1.0` | ✅ Adaptado | Inline completions + chat |
| Skill | `apb-arch-design-v1.0` | ✅ Adaptado | Chat con contexto de archivo |
| Agent | `apb-agent-implementer-v1.0` | ✅ Adaptado | Modo chat con contexto repo |
| Workflow | `apb-wf-code-review-v1.0` | ✅ Adaptado | Integración con GitHub PRs |
| Provider | `prov-github-v1.0` | ✅ Nativo | GitHub MCP nativo |

## 🔌 Interface de Adaptación

### Mapeo de Skills a Copilot Instructions
Las skills APB se traducen a archivos `.github/copilot-instructions.md` o prompts de chat contextuales.

### Contexto de Repositorio
Copilot accede al contexto del repositorio mediante:
- `@workspace` para contexto de todo el repo
- `@file` para contexto de archivo específico
- `@terminal` para contexto de comandos

### Invocación de Agentes
Los agentes se invocan mediante comandos de chat:
- `/apb-review` → Code Review Agent
- `/apb-arch` → Technical Architect Agent
- `/apb-qa` → QA Automation Agent

### Integración con GitHub
- Pull requests: comentarios automáticos con findings
- Issues: generación automática desde análisis
- Actions: integración con workflows CI/CD

## ⚙️ Configuración

```json
{
  "copilot": {
    "instructions_path": ".github/copilot-instructions.md",
    "skills_mapping": {
      "apb-dev-code-review": "review_instructions",
      "apb-dev-implement": "implement_instructions",
      "apb-arch-design": "design_instructions"
    },
    "agents_commands": {
      "review": "/apb-review",
      "arch": "/apb-arch",
      "qa": "/apb-qa",
      "security": "/apb-security"
    },
    "context_providers": [
      "@workspace",
      "@file",
      "@terminal"
    ],
    "github_integration": {
      "pr_comments": true,
      "issue_generation": true,
      "actions_integration": true
    }
  }
}
```

## 🔄 Mapeo de Capacidades

| Capacidad APB | Capacidad Copilot | Mapeo |
|---------------|-------------------|-------|
| Code Review | Inline PR comments | Directo |
| Implementación | Inline completions | Directo |
| Diseño de Arquitectura | Chat con contexto | Adaptado |
| Testing | Terminal commands | Adaptado |
| Documentación | File generation | Directo |
| Threat Modeling | Chat con contexto | Adaptado |
| CI/CD | GitHub Actions | Nativo |

## 📥 Formato de Input

### Formato de Input
```yaml
adapter: copilot
skill: apb-dev-code-review-v1.0
context:
  repo: "/repos/project"
  pr_number: 42
  files_changed:
    - "src/TributoService.cs"
    - "tests/TributoServiceTests.cs"
instructions: "review_instructions"
```

## 📤 Formato de Output

### Formato de Output
```yaml
adapter: copilot
skill: apb-dev-code-review-v1.0
results:
  - file: "src/TributoService.cs"
    findings:
      - severity: "warning"
        line: 23
        message: "Considerar validación de input contra null"
        rule: "apb-nullable-check"
      - severity: "info"
        line: 45
        message: "Documentar excepción lanzada"
        rule: "apb-xml-doc"
  summary:
    total_findings: 2
    warnings: 1
    infos: 1
    passed: true
```

## 🚫 Limitaciones del Runtime

- Copilot no tiene acceso a sistemas externos (Jira, SonarQube) sin MCP
- El contexto está limitado a tokens de ventana del modelo
- No soporta ejecución de código directamente
- Las skills de Nivel 2 (autocorrección) requieren intervención humana
- No puede generar infraestructura cloud directamente

## 🔒 Seguridad

- No se almacenan secretos en instrucciones de Copilot
- Las credenciales se referencian via AKV y se resuelven en runtime
- El contexto sensible se filtra antes de enviar a Copilot
- Cumple con políticas de datos de GitHub Copilot Business
- Auditoría de interacciones mediante GitHub Copilot Analytics

## 📝 Ejemplo de Uso

```yaml
adapter: GitHub Copilot
runtime: GitHub Copilot
config:
  adapter: "copilot"
  agent: "apb-agent-implementer-v1.0"
  skill: "apb-dev-implement-v1.0"
  context:
    repo: "/repos/tributos-service"
    current_file: "src/TributoService.cs"
    cursor_position: "line 45"
  instructions: "implement-tributo-service"
  output_format: "inline-completion"
```

## 🔄 Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-21 | Arquitectura APB | Creación inicial |

---
*Documento generado por el APB AI Framework. Requiere revisión humana antes de aprobación.*
