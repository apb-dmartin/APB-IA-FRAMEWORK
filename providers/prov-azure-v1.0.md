---
id: "prov-azure-v1.0"
name: "Provider: Azure MCP"
description: "Proveedor de acción para gestión de recursos Azure. Permite desplegar infraestructura, consultar métricas, gestionar App Services, Azure SQL y otros servicios."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
provider_type: "action"
access_mode: "read-write"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Provider: Azure MCP

---

## Descripción
Proveedor de acción para gestión de recursos Azure. Permite desplegar infraestructura, consultar métricas, gestionar App Services, Azure SQL y otros servicios.

## Capacidades
- Despliegue de recursos vía ARM/Bicep
- Consulta de métricas y logs
- Gestión de App Services y Functions
- Administración de Azure SQL
- Configuración de Azure Service Bus

## Configuración
```json
{
  "provider_id": "prov-azure-v1.0",
  "type": "action",
  "endpoint": "https://management.azure.com",
  "auth": "managed_identity",
  "subscription_id": "AKV://azure-subscription-id",
  "rate_limit": "12000 req/hour",
  "scope": "read-only"
}
```

## Inputs
- `resource_group`: grupo de recursos
- `action`: acción a ejecutar
- `resource_type`: tipo de recurso
- `params`: parámetros específicos

## Outputs
- `deployment_result`: resultado del despliegue
- `metrics`: métricas consultadas
- `status`: estado del recurso

## Dependencias
- `apb-agent-cloud-architect-v1.0` (consumidor)
- `apb-agent-platform-engineer-v1.0` (consumidor)
- `apb-sub-ops-azure-v1.0` (subagente)

## Restricciones
- Scope read-only por defecto
- Escritura requiere aprobación de Cloud Architect
- Managed Identity requerida
- No gestiona secretos directamente

## Ejemplo de Uso
```
Invocar: prov-azure-v1.0
Input: { resource_group: "RG-APB-Prod", action: "get_metrics", resource_type: "Microsoft.Web/sites" }
Output: Métricas de App Service
```

---
*Registrado en APB AI Framework.*
