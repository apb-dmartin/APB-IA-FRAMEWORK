---
id: "prov-azure-cost-v1.0"
name: "Provider: Azure Cost Management API"
description: "Proveedor de acción para consulta y gestión de costes cloud en Azure Cost Management API. Soporta exportaciones de coste por periodo, configuración de budgets y alertas, y análisis de reservas y savings plans. Usado por apb-agent-finops-v1.0."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
provider_type: "action"
access_mode: "read-write"
created_date: "2026-06-29"
review_date: "2026-06-29"
---

# Provider: Azure Cost Management API

## Descripción

Proveedor dedicado a la Azure Cost Management and Billing API. Diferente de `prov-azure-v1.0` (gestión general de infraestructura): este provider es específico para consultas financieras, exportación de datos de coste, configuración de budgets y análisis de eficiencia de reservas. Es el provider bloqueante del `apb-agent-finops-v1.0` para automatizar el análisis de costes sin exportaciones manuales CSV.

## Casos de Uso

- **Exportación de costes:** consultar el consumo cloud por periodo, suscripción, resource group o etiqueta desde `apb-agent-finops-v1.0`.
- **Gestión de budgets:** crear y actualizar budgets con alertas automáticas para proyectos o departamentos APB.
- **Análisis de reservas:** evaluar el uso de Reserved Instances y Savings Plans para identificar oportunidades de ahorro.
- **Revisión periódica FinOps:** input principal para `apb-wf-finops-review-v1.0` (revisión mensual/trimestral de costes).

## Configuración

```json
{
  "provider_id": "prov-azure-cost-v1.0",
  "type": "action",
  "api_base_url": "https://management.azure.com",
  "api_version": "2023-11-01",
  "subscription_id": "AKV://azure-subscription-id",
  "auth": "managed_identity",
  "auth_fallback": "service_principal",
  "client_id": "AKV://azure-sp-client-id",
  "client_secret": "AKV://azure-sp-client-secret",
  "tenant_id": "AKV://azure-tenant-id",
  "default_scope": "https://management.azure.com/.default",
  "region": "westeurope",
  "rate_limit": "12 llamadas/min (throttling automático con retry exponencial)"
}
```

> **Nota de aprovisionamiento:**
> 1. La Managed Identity (o Service Principal) debe tener el rol **Cost Management Reader** a nivel de suscripción o Management Group APB.
> 2. Para `set_budget` y `set_alert` se requiere adicionalmente el rol **Cost Management Contributor**.
> 3. Los valores de configuración se almacenan en Azure Key Vault (`prov-akv-v1.0`).

## Acciones Disponibles

| Acción | Descripción | Rol mínimo requerido |
|--------|-------------|----------------------|
| `get_cost_export` | Exporta costes por periodo, granularidad y dimensión (resource group, etiqueta, servicio) | Cost Management Reader |
| `get_cost_summary` | Resumen de costes del mes en curso vs. mes anterior | Cost Management Reader |
| `list_budgets` | Lista budgets configurados en la suscripción | Cost Management Reader |
| `set_budget` | Crea o actualiza un budget con umbral y periodo | Cost Management Contributor |
| `list_alerts` | Lista alertas de coste activas y su estado | Cost Management Reader |
| `set_alert` | Configura alerta de coste asociada a un budget | Cost Management Contributor |
| `get_reservations` | Lista Reserved Instances y Savings Plans activos con % de uso | Cost Management Reader |
| `get_recommendations` | Recomendaciones de Azure Advisor sobre coste (rightsizing, reservas) | Cost Management Reader |

## Inputs

- `action`: nombre de la acción (ver tabla anterior)
- `period`: objeto `{start: "YYYY-MM-DD", end: "YYYY-MM-DD"}` — para `get_cost_export` y `get_cost_summary`
- `granularity`: `Daily` | `Monthly` — para `get_cost_export`
- `group_by`: dimensión de agrupación (`ResourceGroup`, `ServiceName`, `Tag:proyecto`) — para `get_cost_export`
- `budget_name`: nombre del budget — para `set_budget` y `set_alert`
- `budget_amount`: importe en EUR — para `set_budget`
- `alert_threshold_pct`: porcentaje del budget para disparar la alerta — para `set_alert`

## Outputs

- `get_cost_export`: array de filas `{date, resource_group, service, amount_eur, currency}`
- `get_cost_summary`: objeto `{current_month_eur, previous_month_eur, delta_pct, top_services[]}`
- `list_budgets`: array de budgets `{name, amount, current_spend, forecast_spend, period}`
- `get_reservations`: array `{type, sku, scope, utilization_pct, savings_vs_payg_eur}`
- `get_recommendations`: array `{type, resource, impact, estimated_savings_eur}`

## Dependencias

- `prov-akv-v1.0` — todos los valores de configuración se leen de Azure Key Vault
- `apb-agent-finops-v1.0` — agente principal consumidor de este provider
- `apb-wf-finops-review-v1.0` — workflow de revisión periódica de costes

## Restricciones

- Todos los secretos de configuración se leen de Azure Key Vault; nunca en texto plano.
- La Managed Identity es el método de autenticación preferido; el Service Principal es fallback.
- Las acciones de escritura (`set_budget`, `set_alert`) requieren confirmación humana explícita antes de ejecutarse (autonomía nivel 1).
- Los datos de coste contienen información financiera confidencial — no incluir en logs ni en artefactos de salida sin anonimización previa.
- El provider no accede a datos de clientes ni a información de facturación con detalle de identidad.

## Ejemplo de Uso

```
Invocar: prov-azure-cost-v1.0
Action: get_cost_export
Period: {start: "2026-06-01", end: "2026-06-29"}
Granularity: Monthly
GroupBy: ResourceGroup
→ [{resource_group: "rg-apb-prod", service: "Azure App Service", amount_eur: 1240.50}, ...]
```

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado mediante este provider debe incluir marca de origen IA:

- **Documentos Markdown** (informes FinOps, análisis de coste):
  > ⚠️ **Borrador generado por IA** (APB AI Framework — prov-azure-cost-v1.0) — pendiente validación humana. No distribuir sin revisión.
- **Commits**: prefijo `[ai-gen]` + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`.

---
*Documento generado por el APB AI Framework. Requiere revisión humana antes de aprobación.*
