---
id: "prov-atlassian-v1.0"
name: "Provider: Atlassian Rovo MCP"
description: "Proveedor de acción para integración con ecosistema Atlassian (Jira, Confluence, Compass). Permite gestionar tickets, documentación y catálogos de servicios."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
provider_type: "action"
access_mode: "read-write"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Provider: Atlassian Rovo MCP

---

## Descripción
Proveedor de acción para integración con ecosistema Atlassian (Jira, Confluence, Compass). Permite gestionar tickets, documentación y catálogos de servicios.

## Capacidades
- Creación y actualización de tickets Jira
- Consulta de issues y sprints
- Lectura/escritura en Confluence
- Gestión de catálogo Compass
- Registro de evidencias en Jira

## Configuración
```json
{
  "provider_id": "prov-atlassian-v1.0",
  "type": "action",
  "endpoint": "https://apb.atlassian.net",
  "auth": "token",
  "token_ref": "AKV://atlassian-token",
  "rate_limit": "10000 req/hour",
  "products": ["jira", "confluence", "compass"]
}
```

## Inputs
- `product`: producto Atlassian (jira, confluence, compass)
- `action`: acción a ejecutar
- `params`: parámetros específicos

## Outputs
- `ticket`: ticket creado/actualizado
- `page`: página de Confluence
- `evidence`: evidencia registrada

## Dependencias
- `apb-gov-jira-evidence-v1.0` (skill)
- `apb-agent-documentation-v1.0` (agente)
- `apb-wf-sdd-full-v1.0` (workflow)

## Restricciones
- Token gestionado en Azure Key Vault
- Permisos limitados por proyecto
- No elimina datos, solo crea/actualiza
- Auditoría completa de cambios

## Ejemplo de Uso
```
Invocar: prov-atlassian-v1.0
Input: { product: "jira", action: "create_issue", params: { project: "PROJ", summary: "...", type: "Task" } }
Output: Ticket Jira creado con enlace
```

---
*Registrado en APB AI Framework.*
