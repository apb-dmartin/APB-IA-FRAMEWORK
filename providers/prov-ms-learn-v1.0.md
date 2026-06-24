---
id: "prov-ms-learn-v1.0"
name: "Provider: Microsoft Learn MCP"
description: "Proveedor de conocimiento que proporciona acceso a la documentación técnica de Microsoft Learn vía MCP (Model Context Protocol). Permite consultar documentación oficial de .NET, Azure, DevOps y otros productos Microsoft."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
provider_type: "knowledge"
access_mode: "read-write"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Provider: Microsoft Learn MCP

---

## Descripción
Proveedor de conocimiento que proporciona acceso a la documentación técnica de Microsoft Learn vía MCP (Model Context Protocol). Permite consultar documentación oficial de .NET, Azure, DevOps y otros productos Microsoft.

## Capacidades
- Búsqueda en documentación Microsoft Learn
- Recuperación de artículos técnicos por tema
- Acceso a ejemplos de código oficiales
- Sincronización con versiones más recientes

## Configuración
```json
{
  "provider_id": "prov-ms-learn-v1.0",
  "type": "knowledge",
  "endpoint": "https://learn.microsoft.com/api/",
  "auth": "none",
  "rate_limit": "1000 req/day",
  "cache_ttl": "24h"
}
```

## Inputs
- `query`: término de búsqueda
- `product`: producto Microsoft (ej: dotnet, azure, devops)
- `version`: versión específica (opcional)

## Outputs
- `results`: lista de artículos relevantes
- `snippets`: fragmentos de código asociados
- `urls`: enlaces a documentación oficial

## Dependencias
- `wrap-anthropic-skills-v1.0` (para formateo)
- `apb-agent-technical-architect-v1.0` (consumidor)

## Restricciones
- Solo documentación pública de Microsoft
- No accede a documentación interna o preview
- Rate limiting aplicado

## Ejemplo de Uso
```
Invocar: prov-ms-learn-v1.0
Input: { query: "ASP.NET Core middleware pipeline", product: "dotnet" }
Output: Artículos oficiales con ejemplos de código
```

---
*Registrado en APB AI Framework.*
