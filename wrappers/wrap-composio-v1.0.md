---
id: "wrap-composio-v1.0"
name: "Composio"
description: "Wrapper para integrar herramientas Composio con los MCP corporativos del APB AI Framework. Filtra permisos, gestiona autenticación y adapta formatos de salida."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
wraps: "Composio"
source_repo: "https://github.com/ComposioHQ"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Composio

## Descripción
Wrapper para integrar herramientas Composio con los MCP corporativos del APB AI Framework. Filtra permisos, gestiona autenticación y adapta formatos de salida.

## Funciones del Wrapper

### 1. Integración con MCP Corporativos
- Mapeo de herramientas Composio → MCP APB
- Gestión de conectores autorizados
- Normalización de respuestas

### 2. Filtrado de Permisos
- Verificación de permisos por herramienta
- Restricción de acciones no autorizadas
- Auditoría de operaciones

### 3. Gestión de Autenticación
- Delegación a Azure Key Vault
- Rotación de tokens
- Validación de scopes

### 4. Adaptación de Formatos
- Conversión de formatos Composio → APB
- Normalización de errores
- Mapeo de códigos de estado

## Skills Cubiertos
| Skill Tercero | Skill APB Relacionada | Estado |
|---------------|----------------------|--------|
| `third-composio-sonar-v1.0` | `apb-dev-sonar-clean-v1.0` | draft |

## Configuración
```json
{
  "wrapper_id": "wrap-composio-v1.0",
  "source": "Composio",
  "license": "MIT",
  "allowed_tools": ["sonar", "github", "jira"],
  "blocked_tools": ["slack", "discord", "twitter"],
  "auth_delegate": "AKV",
  "runtimes": ["copilot", "claude"]
}
```

## Inputs
- `tool_request`: solicitud de herramienta Composio
- `auth_context`: contexto de autenticación
- `security_policy`: política de seguridad

## Outputs
- `tool_response`: respuesta adaptada
- `permission_log`: log de permisos verificados
- `audit_trail`: traza de auditoría

## Restricciones
- Solo herramientas en lista blanca
- No acceso a redes sociales corporativas
- Autenticación delegada a AKV
- Auditoría completa de operaciones

## Ejemplo de Uso
```
Invocar: wrap-composio-v1.0
Input: { tool_request: "sonar.analyze", auth_context: "..." }
Output: Respuesta Sonar adaptada con auditoría completa
```

---
*Wrapper APB AI Framework.*
