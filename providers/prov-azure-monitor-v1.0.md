---
id: "prov-azure-monitor-v1.0"
name: "Provider: Azure Monitor Logs Ingestion API"
description: "Proveedor de acción para ingestión de eventos de telemetría en Azure Monitor vía Logs Ingestion API (DCR-based). Usado por apb-ops-telemetry-emit-v1.0 para registrar invocaciones de componentes del framework y por apb-agent-observability-v1.0 para consultar métricas existentes."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
provider_type: "action"
access_mode: "read-write"
created_date: "2026-06-25"
review_date: "2026-06-25"
---

# Provider: Azure Monitor Logs Ingestion API

## Descripción

Proveedor dedicado a la Logs Ingestion API de Azure Monitor (endpoint DCR-based). Diferente de `prov-azure-v1.0` (gestión general de infraestructura Azure): este provider es específico para ingestión y consulta de telemetría del framework de IA, con su propia tabla Log Analytics y esquema de evento.

## Casos de Uso

- **Telemetría del framework:** ingestión de eventos de invocación de agentes/skills desde `apb-ops-telemetry-emit-v1.0` y `scripts/emit_telemetry.py`.
- **Consulta de métricas para dashboards:** lectura de datos existentes en el workspace de Log Analytics desde `apb-agent-observability-v1.0`.
- **Cobertura pendiente:** usuarios que solo interactúan por chat y nunca hacen commit — la telemetría automática no es alcanzable con el runtime actual sin instrumentar la plataforma de chat. Anotado en `discovery/PLAN_FASES_FUTURAS.md`.

## Configuración

```json
{
  "provider_id": "prov-azure-monitor-v1.0",
  "type": "action",
  "ingestion_endpoint": "AKV://azure-monitor-dce-endpoint",
  "dcr_immutable_id": "AKV://azure-monitor-dcr-id",
  "stream_name": "Custom-APBFrameworkTelemetry_CL",
  "workspace_id": "AKV://log-analytics-workspace-id",
  "auth": "managed_identity",
  "auth_fallback": "service_principal",
  "client_id": "AKV://azure-monitor-client-id",
  "client_secret": "AKV://azure-monitor-client-secret",
  "tenant_id": "AKV://azure-tenant-id",
  "rate_limit": "up to 1 GB/min por DCE",
  "region": "westeurope"
}
```

> **Nota de aprovisionamiento:** requiere crear en Azure Monitor:
> 1. Un Data Collection Endpoint (DCE) en la misma región que el workspace.
> 2. Una Data Collection Rule (DCR) con la tabla `APBFrameworkTelemetry_CL` como destino.
> 3. Rol **Monitoring Metrics Publisher** asignado a la Managed Identity o Service Principal.
> Los valores de configuración se almacenan en Azure Key Vault (`prov-akv-v1.0`).

## Esquema de Evento de Telemetría

Cada evento enviado a la tabla `APBFrameworkTelemetry_CL` sigue este esquema:

```json
{
  "TimeGenerated": "2026-06-25T10:30:00Z",
  "component_id": "apb-agent-observability-v1.0",
  "component_type": "agent",
  "component_domain": "operation",
  "invocation_id": "uuid-v4",
  "runtime": "claude-code",
  "user_profile": "developer",
  "outcome": "success",
  "human_approved": true,
  "duration_seconds": 142,
  "artifact_type": "dashboard-spec",
  "session_id": "optional-session-identifier",
  "notes": "texto libre opcional"
}
```

| Campo | Tipo | Obligatorio | Valores posibles |
|---|---|---|---|
| `TimeGenerated` | ISO 8601 | Sí | timestamp del momento de emisión |
| `component_id` | string | Sí | ID del componente invocado |
| `component_type` | string | Sí | `skill`, `agent`, `subagent`, `workflow` |
| `component_domain` | string | Sí | dominio del componente |
| `invocation_id` | UUID v4 | Sí | identificador único de la invocación |
| `runtime` | string | Sí | `claude-code`, `copilot`, `unknown` |
| `user_profile` | string | Sí | `developer`, `functional`, `admin` |
| `outcome` | string | Sí | `success`, `human_override`, `cancelled`, `error` |
| `human_approved` | boolean | Sí | si el output pasó revisión humana explícita |
| `duration_seconds` | int | No | tiempo de ejecución aproximado |
| `artifact_type` | string | No | tipo de artefacto generado |
| `session_id` | string | No | identificador de sesión de trabajo |
| `notes` | string | No | texto libre para contexto adicional |

## Queries KQL de Referencia

```kql
// Invocaciones por componente (últimos 30 días)
APBFrameworkTelemetry_CL
| where TimeGenerated > ago(30d)
| summarize count() by component_id
| order by count_ desc

// Tasa de aprobación humana por agente
APBFrameworkTelemetry_CL
| where component_type == "agent"
| summarize
    total = count(),
    approved = countif(human_approved == true)
    by component_id
| extend approval_rate = round(100.0 * approved / total, 1)

// Outcomes por dominio
APBFrameworkTelemetry_CL
| summarize count() by component_domain, outcome
| order by component_domain, count_ desc
```

## Inputs

- `action`: `ingest` (enviar evento) o `query` (ejecutar KQL)
- `event`: objeto JSON con el esquema de evento (para `ingest`)
- `kql_query`: string con la query KQL (para `query`)

## Outputs

- `ingest`: HTTP 204 (éxito) o error con código y mensaje
- `query`: tabla de resultados en formato JSON

## Dependencias

- `prov-akv-v1.0` — todos los valores de configuración se leen de Azure Key Vault
- `apb-ops-telemetry-emit-v1.0` — skill que define la convención de uso de este provider
- `apb-agent-observability-v1.0` — agente principal consumidor para dashboards

## Restricciones

- Todos los secretos de configuración se leen de Azure Key Vault, nunca en texto plano.
- La Managed Identity es el método de autenticación preferido; el Service Principal es fallback para entornos sin identidad gestionada.
- No se almacenan datos personales en el evento — solo metadatos de uso del componente.
- La tabla `APBFrameworkTelemetry_CL` debe configurarse con retención mínima de 90 días para poder calcular KPIs trimestrales.

## Ejemplo de Uso

```
Invocar: prov-azure-monitor-v1.0
Action: ingest
Event: {
  "component_id": "apb-agent-tech-debt-v1.0",
  "component_type": "agent",
  "outcome": "success",
  "human_approved": true,
  "runtime": "claude-code"
}
→ HTTP 204: evento registrado en APBFrameworkTelemetry_CL
```

---

> **Generado por IA:** Claude (Anthropic/Claude Code), Sesión 17 — Observabilidad, 2026-06-25.
> **Validado por humano:** _pendiente — completar nombre/rol del validador antes de pasar a `candidate`._
