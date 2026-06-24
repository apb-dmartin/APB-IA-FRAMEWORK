---
id: "prov-ms365-v1.0"
name: "Provider: Microsoft 365 (Graph API)"
description: "Proveedor de acción bidireccional para el ecosistema Microsoft 365 de APB: Teams (canales y mensajes directos), Outlook/Exchange (envío y lectura de correo) y SharePoint (lectura y escritura de documentos). Usa Microsoft Graph API como capa unificada de acceso, con soporte para MCP de Microsoft Graph cuando esté disponible en el runtime."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
provider_type: "action"
access_mode: "read-write"
created_date: "2026-06-24"
review_date: "2026-06-24"
---

# Provider: Microsoft 365 (Graph API)

---

## Descripción

Proveedor unificado para los tres servicios Microsoft 365 de uso más frecuente en APB:

| Producto | Capacidades |
|----------|-------------|
| **Microsoft Teams** | Enviar mensajes a canales y usuarios; leer mensajes de canal; reaccionar a aprobaciones |
| **Outlook / Exchange** | Enviar correos con adjuntos; leer correos entrantes; marcar como procesados |
| **SharePoint** | Leer documentos de bibliotecas; subir/actualizar ficheros; gestionar metadatos |

Todos los servicios se acceden mediante **Microsoft Graph API v1.0** con autenticación OAuth 2.0 (Client Credentials para operaciones de sistema; Delegated para operaciones en nombre del usuario).

El provider soporta **MCP de Microsoft Graph** (`@microsoft/graph-mcp-server` o equivalente aprobado por Arquitectura APB) cuando el runtime del agente lo permita, evitando llamadas HTTP directas en ese caso.

---

## Configuración

```json
{
  "provider_id": "prov-ms365-v1.0",
  "type": "action",
  "graph_endpoint": "https://graph.microsoft.com/v1.0",
  "auth": {
    "type": "oauth2",
    "flow": "client_credentials",
    "tenant_id_ref": "AKV://apb-m365-tenant-id",
    "client_id_ref": "AKV://apb-m365-client-id",
    "client_secret_ref": "AKV://apb-m365-client-secret"
  },
  "scopes": [
    "https://graph.microsoft.com/Chat.ReadWrite",
    "https://graph.microsoft.com/Channel.ReadBasic.All",
    "https://graph.microsoft.com/ChannelMessage.Send",
    "https://graph.microsoft.com/Mail.ReadWrite",
    "https://graph.microsoft.com/Mail.Send",
    "https://graph.microsoft.com/Sites.ReadWrite.All",
    "https://graph.microsoft.com/Files.ReadWrite.All"
  ],
  "rate_limit": "10000 req/10min",
  "timeout_ms": 30000,
  "mcp_server": "optional — @microsoft/graph-mcp-server si disponible en runtime"
}
```

Todas las credenciales residen en **Azure Key Vault**. Ningún secreto se almacena en texto plano en el framework ni en el runtime del agente.

---

## Capacidades por producto

### Teams

| Operación | Descripción | Permiso requerido |
|-----------|-------------|-------------------|
| `send_channel_message` | Enviar mensaje a un canal de Teams | `ChannelMessage.Send` |
| `send_direct_message` | Enviar mensaje directo a un usuario | `Chat.ReadWrite` |
| `read_channel_messages` | Leer mensajes de un canal (para detectar respuestas de aprobación) | `ChannelMessage.Read.All` |
| `create_adaptive_card` | Enviar tarjeta interactiva con botones de aprobación/rechazo | `ChannelMessage.Send` |
| `list_channels` | Listar canales de un team | `Channel.ReadBasic.All` |

### Mail (Outlook / Exchange)

| Operación | Descripción | Permiso requerido |
|-----------|-------------|-------------------|
| `send_mail` | Enviar correo con cuerpo HTML y adjuntos opcionales | `Mail.Send` |
| `read_inbox` | Leer correos de una carpeta (detección de respuestas de aprobación) | `Mail.ReadWrite` |
| `mark_processed` | Mover correo a carpeta procesada o marcar como leído | `Mail.ReadWrite` |
| `reply_mail` | Responder a un correo existente | `Mail.ReadWrite` |

### SharePoint

| Operación | Descripción | Permiso requerido |
|-----------|-------------|-------------------|
| `read_document` | Leer contenido de un fichero de una biblioteca | `Sites.Read.All` |
| `upload_document` | Subir o actualizar un fichero en una biblioteca | `Sites.ReadWrite.All` |
| `list_documents` | Listar ficheros de una carpeta/biblioteca | `Sites.Read.All` |
| `get_metadata` | Leer metadatos de un ítem (columnas de lista SharePoint) | `Sites.Read.All` |
| `set_metadata` | Actualizar metadatos (columnas de lista) | `Sites.ReadWrite.All` |
| `download_as_bytes` | Descargar fichero para procesarlo (PDF, Word, Excel) | `Files.ReadWrite.All` |

---

## Inputs

- `product`: servicio destino (`teams`, `mail`, `sharepoint`)
- `operation`: operación a ejecutar (ver tabla por producto)
- `params`: parámetros específicos de la operación
- `on_behalf_of`: UPN del usuario si se usa flujo Delegated (opcional — por defecto usa Client Credentials)

## Outputs

- `success`: booleano
- `result`: objeto con la respuesta de Graph API (mensaje enviado, ID de ítem, contenido leído, etc.)
- `graph_request_id`: ID de traza de Graph API para auditoría
- `error`: código y descripción si `success: false`

---

## Dependencias

- `apb-plat-ms-notify-v1.0` (skill consumidora — notificaciones en revisiones y entregas)
- `apb-plat-sharepoint-io-v1.0` (skill consumidora — lectura/escritura documental)
- `adapter-m365-copilot-v1.0` (adapter — integración bidireccional con M365 Copilot)

---

## Restricciones

- Credenciales gestionadas exclusivamente en Azure Key Vault — nunca en código ni en frontmatter
- Permisos mínimos necesarios: no se conceden permisos de borrado permanente (`Mail.Send` no implica `Mail.Delete`)
- No procesa información clasificada como RESERVADA en SharePoint sin aprobación explícita de Ciberseguridad APB
- Los mensajes de Teams con contenido de artefactos de IA deben incluir el aviso corporativo de generación por IA (`SYSTEM.md §7.2`)
- Toda escritura en SharePoint genera entrada de auditoría en el log de actividad de Microsoft 365
- El flujo Delegated (on_behalf_of) requiere que el usuario haya dado consentimiento explícito a la app en Azure AD APB

---

## Ejemplo de Uso

```yaml
Invocar: prov-ms365-v1.0
Input:
  product: "teams"
  operation: "send_channel_message"
  params:
    team_id: "apb-arquitectura-team"
    channel_id: "General"
    message: "📋 Mockup de pantalla 'Lista de Buques' listo para revisión. Generado por apb-agent-ux-mockup-v1.0. Pendiente de validación funcional antes de pasar a desarrollo."
    attachments:
      - type: "file"
        name: "mockup-lista-buques.md"
Output:
  success: true
  result:
    message_id: "1719271234567"
    channel: "General"
    team: "Arquitectura APB"
  graph_request_id: "8e2f1a3b-..."
```

---

> **Generado por IA:** Claude (Anthropic/Claude Code), Sesión 15 del plan APB-IA-FRAMEWORK.
> **Validado por humano:** _pendiente — completar nombre/rol del validador antes de pasar a `candidate`._
