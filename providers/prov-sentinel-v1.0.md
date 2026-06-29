---
id: "prov-sentinel-v1.0"
name: "Provider: Microsoft Sentinel"
description: "Proveedor de acceso al SIEM Microsoft Sentinel de APB: ejecución de queries KQL sobre logs de seguridad, consulta de alertas activas e incidentes en investigación, y activación de playbooks de respuesta. Usado por agentes de seguridad para análisis de amenazas y respuesta a incidentes."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
provider_type: "action"
access_mode: "read-write"
created_date: "2026-06-29"
review_date: "2026-06-29"
---

# Provider: Microsoft Sentinel

## Descripción

Proveedor de acceso al SIEM corporativo Microsoft Sentinel de APB. Permite a los agentes de seguridad ejecutar queries KQL sobre los logs centralizados, consultar alertas e incidentes activos, y (con gate humano obligatorio) activar playbooks de respuesta automatizada. El acceso de lectura es el modo operativo normal; la escritura (activación de playbooks, actualización de incidentes) requiere confirmación humana explícita.

## Casos de Uso

- **Análisis de amenazas:** ejecutar queries KQL para investigar alertas de seguridad, detectar patrones de ataque y correlacionar eventos.
- **Gestión de incidentes de seguridad:** consultar incidentes activos en Sentinel y obtener el contexto completo para el equipo de CSIRT.
- **Verificación de cobertura:** comprobar que las reglas de detección (analytic rules) están activas y cubren los casos de uso de seguridad APB.
- **Respuesta automatizada:** activar playbooks de respuesta (con gate humano) para contención de amenazas.

## Configuración

```json
{
  "provider_id": "prov-sentinel-v1.0",
  "type": "action",
  "azure_management_api": "https://management.azure.com",
  "log_analytics_api": "https://api.loganalytics.io/v1",
  "subscription_id": "AKV://azure-subscription-id",
  "resource_group": "AKV://sentinel-resource-group",
  "workspace_name": "AKV://sentinel-workspace-name",
  "workspace_id": "AKV://sentinel-workspace-id",
  "auth": "managed_identity",
  "auth_fallback": "service_principal",
  "client_id": "AKV://sentinel-sp-client-id",
  "client_secret": "AKV://sentinel-sp-client-secret",
  "tenant_id": "AKV://azure-tenant-id",
  "rate_limit": "200 queries/min (Log Analytics standard)"
}
```

> **Nota de aprovisionamiento:**
> 1. La Managed Identity o Service Principal necesita:
>    - Rol **Microsoft Sentinel Reader** para lectura de incidentes, alertas y reglas.
>    - Rol **Microsoft Sentinel Responder** para actualizar incidentes y activar playbooks.
>    - Rol **Log Analytics Reader** para ejecutar queries KQL en el workspace.
> 2. Los playbooks son Azure Logic Apps — la Managed Identity debe tener permisos de ejecución sobre ellos.
> 3. Todos los valores se almacenan en Azure Key Vault (`prov-akv-v1.0`).

## Acciones Disponibles

| Acción | Descripción | Rol mínimo | Gate humano |
|--------|-------------|------------|-------------|
| `run_kql` | Ejecuta una query KQL en el workspace Log Analytics de Sentinel | Reader | No |
| `list_incidents` | Lista incidentes activos con severidad, estado y entidades | Reader | No |
| `get_incident` | Obtiene el detalle completo de un incidente por ID | Reader | No |
| `list_alert_rules` | Lista reglas de detección (analytic rules) activas | Reader | No |
| `get_alert_rule` | Obtiene el detalle de una regla por ID o nombre | Reader | No |
| `list_bookmarks` | Lista bookmarks de investigación activos | Reader | No |
| `update_incident` | Actualiza el estado o asignación de un incidente | Responder | **Sí** |
| `trigger_playbook` | Activa un playbook de respuesta sobre un incidente | Responder | **Sí** |

## Queries KQL de Referencia

```kql
// Alertas de alta severidad en las últimas 24h
SecurityAlert
| where TimeGenerated > ago(24h) and AlertSeverity in ("High", "Critical")
| project TimeGenerated, AlertName, AlertSeverity, Entities, ProviderName
| order by TimeGenerated desc

// Intentos de acceso fallidos por usuario (últimas 4h)
SigninLogs
| where TimeGenerated > ago(4h) and ResultType != "0"
| summarize FailedAttempts = count() by UserPrincipalName, IPAddress
| where FailedAttempts > 10
| order by FailedAttempts desc

// Actividad de service principals sospechosa
AuditLogs
| where TimeGenerated > ago(7d)
| where Category == "ServicePrincipal" and Result == "failure"
| project TimeGenerated, OperationName, InitiatedBy, TargetResources
```

## Inputs

- `action`: nombre de la acción
- `kql_query`: string con la query KQL (para `run_kql`)
- `timespan`: periodo de la query en formato ISO 8601 (p. ej. `PT24H`, `P7D`) — para `run_kql`
- `incident_id`: ID del incidente (para `get_incident`, `update_incident`, `trigger_playbook`)
- `incident_status`: nuevo estado (`Active`, `Closed`, `InProgress`) — para `update_incident`
- `playbook_name`: nombre del Azure Logic App a activar — para `trigger_playbook`
- `severity_filter`: array de severidades (`High`, `Critical`, `Medium`, `Low`) — para `list_incidents`

## Outputs

- `run_kql`: array de filas resultado de la query (estructura variable según la query)
- `list_incidents`: array de `{id, title, severity, status, entities[], createdTime, lastModifiedTime}`
- `get_incident`: objeto completo con timeline, entidades, alertas relacionadas y comentarios
- `list_alert_rules`: array de `{id, displayName, severity, enabled, tactics[], queryFrequency}`
- `trigger_playbook`: objeto `{playbook_run_id, status, message}`

## Dependencias

- `prov-akv-v1.0` — todos los secretos de configuración se leen de Azure Key Vault
- `apb-agent-security-architect-v1.0` — análisis de amenazas y revisión de reglas de detección
- `apb-agent-sre-v1.0` — correlación de alertas de seguridad con incidentes operacionales

## Restricciones

- Las acciones de escritura (`update_incident`, `trigger_playbook`) requieren confirmación humana explícita antes de ejecutarse (autonomía nivel 1).
- Los logs de Sentinel pueden contener datos personales (IPs, UPNs) — tratar con las mismas restricciones RGPD que `prov-entra-id-v1.0`.
- Los resultados de queries KQL no deben almacenarse en ficheros del repositorio.
- El provider no puede crear ni modificar reglas de detección (analytic rules) — operación reservada al equipo de seguridad.
- El acceso a `trigger_playbook` debe estar limitado a playbooks aprobados por el CISO APB.

## Ejemplo de Uso

```
Invocar: prov-sentinel-v1.0
Action: run_kql
KQLQuery: |
  SecurityAlert
  | where TimeGenerated > ago(1h) and AlertSeverity == "High"
  | project TimeGenerated, AlertName, Entities
Timespan: PT1H
→ [{TimeGenerated: "2026-06-29T10:15:00Z", AlertName: "Suspicious PowerShell execution", Entities: ["host: apb-srv-01"]}]
```

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado mediante este provider debe incluir marca de origen IA:

- **Documentos Markdown** (informes de seguridad, análisis de incidentes):
  > ⚠️ **Borrador generado por IA** (APB AI Framework — prov-sentinel-v1.0) — pendiente validación humana. No distribuir sin revisión.
- **Commits**: prefijo `[ai-gen]` + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`.

---
*Documento generado por el APB AI Framework. Requiere revisión humana antes de aprobación.*
