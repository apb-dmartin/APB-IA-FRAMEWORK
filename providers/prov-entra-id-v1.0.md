---
id: "prov-entra-id-v1.0"
name: "Provider: Microsoft Entra ID (Azure Active Directory)"
description: "Proveedor de consulta sobre Microsoft Entra ID vía Microsoft Graph API: usuarios, grupos, conditional access policies y registros de auditoría de identidad. Usado por agentes de seguridad y operaciones para validación de identidades y accesos en el entorno APB."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
provider_type: "action"
access_mode: "read-only"
created_date: "2026-06-29"
review_date: "2026-06-29"
---

# Provider: Microsoft Entra ID (Azure Active Directory)

## Descripción

Proveedor de acceso a Microsoft Entra ID (anteriormente Azure Active Directory) mediante la Microsoft Graph API. Permite a los agentes del framework consultar información de usuarios, membresías de grupos, políticas de acceso condicional y logs de auditoría de identidad. El acceso es de solo lectura por defecto — las modificaciones de identidad quedan fuera del scope del framework y requieren procesos de RRHH/IT.

## Casos de Uso

- **Validación de accesos:** verificar que los usuarios de un proyecto tienen los grupos y roles correctos en Entra ID antes de un despliegue.
- **Auditoría de identidad:** consultar logs de inicio de sesión y cambios de acceso para análisis de incidentes de seguridad.
- **Revisión de conditional access:** validar que las políticas de acceso condicional APB están activas y correctamente configuradas.
- **Inventario de identidades:** listar usuarios y grupos de un departamento para informes de governance.

## Configuración

```json
{
  "provider_id": "prov-entra-id-v1.0",
  "type": "action",
  "graph_api_base": "https://graph.microsoft.com/v1.0",
  "tenant_id": "AKV://azure-tenant-id",
  "auth": "managed_identity",
  "auth_fallback": "service_principal",
  "client_id": "AKV://entra-sp-client-id",
  "client_secret": "AKV://entra-sp-client-secret",
  "default_scope": "https://graph.microsoft.com/.default",
  "rate_limit": "10.000 req/10 min (throttling automático con retry)"
}
```

> **Nota de aprovisionamiento:**
> 1. La Managed Identity o Service Principal debe tener los permisos de aplicación Graph API:
>    - `User.Read.All` — lectura de usuarios
>    - `Group.Read.All` — lectura de grupos y membresías
>    - `Policy.Read.All` — lectura de conditional access policies
>    - `AuditLog.Read.All` — lectura de logs de auditoría
> 2. Todos los permisos requieren consentimiento de administrador global de Entra ID.
> 3. Los valores de configuración se almacenan en Azure Key Vault (`prov-akv-v1.0`).

## Acciones Disponibles

| Acción | Descripción | Permiso Graph requerido |
|--------|-------------|-------------------------|
| `get_user` | Obtiene perfil de usuario por UPN o ID | User.Read.All |
| `list_users` | Lista usuarios de la organización con filtros | User.Read.All |
| `list_group_members` | Lista miembros de un grupo por ID o nombre | Group.Read.All |
| `get_user_groups` | Obtiene los grupos a los que pertenece un usuario | Group.Read.All |
| `get_conditional_access_policies` | Lista políticas de acceso condicional activas | Policy.Read.All |
| `get_audit_logs` | Consulta logs de inicio de sesión y auditoría por usuario o periodo | AuditLog.Read.All |
| `get_service_principals` | Lista service principals (apps registradas) | Application.Read.All |

## Inputs

- `action`: nombre de la acción
- `user_upn`: User Principal Name (email) del usuario (para `get_user`, `get_user_groups`, `get_audit_logs`)
- `group_id`: ID del grupo Entra (para `list_group_members`)
- `group_name`: nombre del grupo (alternativa a `group_id`)
- `filter`: expresión OData para filtrar resultados (para `list_users`)
- `period`: objeto `{start: "YYYY-MM-DD", end: "YYYY-MM-DD"}` — para `get_audit_logs`
- `top`: número máximo de resultados (default: 100, max: 999)

## Outputs

- `get_user`: objeto `{id, displayName, upn, department, jobTitle, accountEnabled, lastSignIn}`
- `list_users`: array de objetos usuario con los mismos campos
- `list_group_members`: array de `{id, displayName, upn, userType}`
- `get_conditional_access_policies`: array de `{id, displayName, state, conditions, grantControls}`
- `get_audit_logs`: array de `{timestamp, userUpn, appDisplayName, ipAddress, status, location}`

## Dependencias

- `prov-akv-v1.0` — todos los secretos de configuración se leen de Azure Key Vault
- `apb-agent-security-architect-v1.0` — revisión de políticas de acceso
- `apb-agent-governance-v1.0` — auditoría de identidades para compliance

## Restricciones

- El provider es de solo lectura — no puede crear, modificar ni eliminar usuarios, grupos ni políticas.
- Los datos de identidad (emails, nombres, logs de acceso) son datos personales sujetos a RGPD — no incluir en artefactos de salida sin anonimización.
- El acceso a `get_audit_logs` debe limitarse a periodos y usuarios específicos; evitar consultas masivas sin justificación.
- Los resultados de este provider no deben almacenarse en ficheros del repositorio.

## Ejemplo de Uso

```
Invocar: prov-entra-id-v1.0
Action: get_user_groups
UserUPN: jlopez@portdebarcelona.cat
→ [{id: "abc123", displayName: "GRP-ARQUITECTURA"}, {id: "def456", displayName: "GRP-AZURE-DEVS"}]
```

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado mediante este provider debe incluir marca de origen IA:

- **Documentos Markdown** (informes de auditoría de identidad, revisiones de acceso):
  > ⚠️ **Borrador generado por IA** (APB AI Framework — prov-entra-id-v1.0) — pendiente validación humana. No distribuir sin revisión.
- **Commits**: prefijo `[ai-gen]` + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`.

---
*Documento generado por el APB AI Framework. Requiere revisión humana antes de aprobación.*
