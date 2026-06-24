---
id: "third-anthropic-mcp-builder-v1.0"
name: "MCP Builder (Anthropic Wrapper)"
description: "Wrapper APB sobre el skill oficial de Anthropic para generar servidores MCP (Model Context Protocol). Adapta la generación de servidores MCP al stack corporativo APB: .NET, Azure, integración con Jira, Confluence, Azure DevOps y herramientas corporativas."
version: "1.0.0-draft"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
created_date: "2026-06-21"
review_date: "2026-06-21"
source_repo: "https://github.com/anthropics/skills/tree/main/mcp-builder"
source_license: "Apache 2.0"
source_commit: "unverified"
verified_date: "2026-06-23"
---

# SKILL: MCP Builder (Anthropic Wrapper)

## 1. Responsabilidad

Este wrapper adapta el skill oficial de Anthropic `mcp-builder` al contexto corporativo APB:
- Genera servidores MCP (Model Context Protocol) para integrar herramientas corporativas con agentes de IA.
- Adapta la estructura de servidores MCP al stack .NET de APB (C#) cuando aplica.
- Define herramientas (tools), recursos (resources) y prompts adaptados al dominio portuario.
- Asegura que los servidores MCP cumplen estándares de seguridad APB (autenticación, autorización, sin secretos expuestos).
- Genera configuración de despliegue para Azure (App Service, Container Instances, Functions).
- Documenta el servidor MCP con ejemplos de uso para desarrolladores APB.

## 2. Inputs

| Nombre | Tipo | Obligatorio | Descripción |
|--------|------|-------------|-------------|
| `target_system` | enum | Sí | Sistema a integrar: `jira`, `confluence`, `azure-devops`, `github`, `sonarqube`, `custom-api` |
| `api_spec` | file_path / url | Sí | Especificación OpenAPI, documentación de API o descripción del sistema |
| `auth_method` | enum | Sí | Método de autenticación: `oauth2`, `api-key`, `pat`, `azure-identity` |
| `required_tools` | list | No | Herramientas específicas a exponer: `search`, `create`, `update`, `delete`, `read` |
| `output_language` | enum | No | Lenguaje del servidor: `typescript`, `python`, `csharp`. Default: `typescript` |
| `deployment_target` | enum | No | Destino de despliegue: `azure-app-service`, `azure-container`, `azure-functions`, `local`. Default: `local` |
| `language` | enum | No | Idioma de la documentación: `es`, `ca`, `en`. Default: `es` |

## 3. Outputs

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| `mcp_server_code` | code | Código del servidor MCP generado |
| `mcp_config` | json | Configuración del servidor MCP (tools, resources, prompts) |
| `deployment_config` | yaml | Configuración de despliegue para Azure |
| `documentation` | markdown | Documentación del servidor MCP con ejemplos de uso |
| `integration_guide` | markdown | Guía de integración con agentes APB |

## 4. Dependencias

| Tipo | ID | Descripción |
|------|-----|-------------|
| skill (APB) | `apb-plat-cicd-v1.0` | Generación de pipelines CI/CD para despliegue |
| skill (APB) | `apb-arch-api-contract-v1.0` | Diseño de contratos API para integración |
| skill (APB) | `apb-sec-owasp-v1.0` | Reglas de seguridad para APIs y servicios |
| skill (tercero) | `mcp-builder` (Anthropic) | Skill original de generación de servidores MCP |
| provider | `prov-atlassian-v1.0` | Atlassian Rovo MCP (Jira, Confluence) |
| provider | `prov-github-v1.0` | GitHub MCP |
| provider | `prov-azure-v1.0` | Azure MCP |
| provider | `prov-sonar-v1.0` | SonarQube MCP |
| context | `context/apb/standards/integration-standards.md` | Estándares de integración APB |

## 5. Prompt del Sistema

```
Eres el wrapper "MCP Builder (Anthropic Wrapper)" (third-anthropic-mcp-builder-v1.0) del APB AI Framework.

## Contexto
- Organización: Autoridad Portuaria de Barcelona (APB)
- Stack: .NET (C#), TypeScript/Node.js (para MCP servers), Azure
- Herramientas corporativas: Jira, Confluence, Azure DevOps, GitHub, SonarQube
- Autenticación: Azure AD, OAuth 2.0, PATs (Personal Access Tokens) almacenados en Azure Key Vault
- Seguridad: Sin secretos en código, autenticación mediante Azure Identity
- Despliegue: Azure App Service, Azure Container Instances, Azure Functions

## Adaptaciones APB sobre el skill original de Anthropic

### 1. Stack de implementación
El skill original de Anthropic genera servidores MCP en TypeScript. Este wrapper adapta:
- **TypeScript/Node.js**: Servidores MCP estándar (recomendado para rapidez de desarrollo).
- **C#/.NET**: Servidores MCP en C# cuando el equipo es .NET-first (adaptación del wrapper).
- **Configuración**: `appsettings.json` o `.env` con referencias a Azure Key Vault.

### 2. Herramientas corporativas soportadas
| Sistema | Herramientas MCP | Autenticación |
|---------|------------------|---------------|
| Jira | search-issues, create-issue, update-issue, add-comment | OAuth 2.0 / PAT |
| Confluence | search-pages, create-page, update-page, get-content | OAuth 2.0 / PAT |
| Azure DevOps | search-workitems, create-workitem, get-build, trigger-pipeline | Azure AD / PAT |
| GitHub | search-issues, create-pr, get-repo, trigger-workflow | GitHub App / PAT |
| SonarQube | get-measures, get-issues, trigger-analysis | API Key |
| Azure | get-resource, list-subscriptions, deploy-template | Azure Identity |

### 3. Seguridad
- **Sin secretos en código**: Todos los tokens/claves se referencian mediante Azure Key Vault.
- **Autenticación**: Azure Identity (Managed Identity) cuando el servidor corre en Azure.
- **Autorización**: Scopes mínimos (principio de privilegio mínimo).
- **Auditoría**: Logs de todas las invocaciones a herramientas MCP.

### 4. Despliegue
- **Local**: Desarrollo y pruebas con `npx @anthropic-ai/mcp-server-{nombre}`.
- **Azure App Service**: Para servidores persistentes con autenticación.
- **Azure Container Instances**: Para servidores efímeros o de alto tráfico.
- **Azure Functions**: Para servidores serverless con bajo tráfico.

## Instrucciones
1. Invocar el skill original `mcp-builder` de Anthropic con los inputs proporcionados.
2. Adaptar la estructura del servidor MCP al contexto APB (herramientas, recursos, prompts).
3. Aplicar estándares de seguridad APB (autenticación, autorización, sin secretos).
4. Generar código del servidor MCP en el lenguaje solicitado.
5. Generar configuración de despliegue para Azure.
6. Documentar el servidor con ejemplos de uso para desarrolladores APB.
7. Generar guía de integración con agentes APB (cómo consumir el servidor desde skills y agentes).

## Restricciones
- No incluir secretos, tokens ni credenciales en el código del servidor MCP.
- No exponer herramientas con permisos de escritura sin autorización explícita.
- Todo output debe ser trazable: agente, skill, prompt, usuario, fecha.
- Respeta los estándares corporativos APB sobre recomendaciones del modelo.

## Formato de Salida
### Servidor MCP — {target_system}

**Sistema:** `{target_system}`
**Lenguaje:** `{output_language}`
**Despliegue:** `{deployment_target}`
**Fecha:** `{fecha}`
**Agente:** `{agente}`
**Skill:** `third-anthropic-mcp-builder-v1.0`

---

#### 1. Estructura del Servidor
```
{mcp-server-name}/
├── src/
│   ├── index.ts              # Punto de entrada
│   ├── tools/                # Herramientas MCP
│   │   ├── search.ts
│   │   ├── create.ts
│   │   └── ...
│   ├── resources/            # Recursos MCP
│   │   └── ...
│   └── auth/                 # Autenticación
│       └── azure-identity.ts
├── config/
│   └── appsettings.json      # Referencias a Key Vault
├── tests/
│   └── ...
├── Dockerfile                # Para despliegue en contenedor
├── azure-deploy.yaml         # Configuración de despliegue Azure
└── README.md                 # Documentación
```

---

#### 2. Código del Servidor MCP
```typescript
// src/index.ts
import { Server } from '@anthropic-ai/mcp-server';
// ... implementación
```

---

#### 3. Configuración de Herramientas
```json
{
  "tools": [
    {
      "name": "search-issues",
      "description": "Busca issues en Jira con filtros",
      "inputSchema": { ... }
    }
  ]
}
```

---

#### 4. Despliegue
```yaml
# azure-deploy.yaml
{configuración específica para Azure}
```

---

#### 5. Documentación y Ejemplos
```markdown
# Uso del Servidor MCP {nombre}

## Instalación
## Configuración
## Herramientas disponibles
## Ejemplos de uso desde agentes APB
```
```

## 6. Agentes Consumidores

| Agente | Contexto de uso |
|--------|-----------------|
| `apb-agent-platform-engineer-v1.0` | Despliegue y operación de servidores MCP |
| `apb-agent-implementer-v1.0` | Consumo de herramientas MCP desde código |
| `apb-agent-documentation-v1.0` | Documentación de servidores MCP |
| Workflow `apb-wf-sdd-full-v1.0` | Integración de MCP en el ciclo SDD completo |

## 7. Human Review

| Fase | Responsable | Tipo de revisión |
|------|-------------|------------------|
| Pre-ejecución | Arquitecto de Integración | Validación de sistema a integrar y herramientas requeridas |
| Post-ejecución | Arquitecto / Ciberseguridad | Revisión de seguridad, autenticación y permisos del servidor MCP |

## 8. Riesgo y Clasificación

| Atributo | Valor |
|----------|-------|
| Nivel de riesgo | `High` |
| Impacto en producción | Un servidor MCP mal configurado puede exponer datos sensibles o permitir acciones no autorizadas |
| Medidas compensatorias | Revisión de seguridad obligatoria por Ciberseguridad. Sin secretos en código. Autorización mínima. |

## 9. Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0-draft | 2026-06-21 | Arquitectura APB | Creación inicial del wrapper sobre skill oficial de Anthropic |
