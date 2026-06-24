---
id: "prov-sonar-v1.0"
name: "Provider: SonarQube MCP"
description: "Proveedor de acción para análisis de calidad de código con SonarQube. Permite ejecutar análisis, consultar métricas y gestionar perfiles de calidad."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
provider_type: "action"
access_mode: "read-write"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Provider: SonarQube MCP

---

## Descripción
Proveedor de acción para análisis de calidad de código con SonarQube. Permite ejecutar análisis, consultar métricas y gestionar perfiles de calidad.

## Capacidades
- Ejecución de análisis estático
- Consulta de issues y vulnerabilidades
- Gestión de perfiles de calidad
- Extracción de métricas de deuda técnica
- Comparación entre versiones

## Configuración
```json
{
  "provider_id": "prov-sonar-v1.0",
  "type": "action",
  "endpoint": "https://sonar.apb.internal",
  "auth": "token",
  "token_ref": "AKV://sonar-token",
  "rate_limit": "unlimited",
  "permissions": ["read", "analysis"]
}
```

## Inputs
- `project_key`: clave del proyecto
- `action`: acción (analyze, get_issues, get_metrics)
- `branch`: rama a analizar
- `params`: parámetros adicionales

## Outputs
- `analysis_result`: resultado del análisis
- `issues`: lista de issues
- `metrics`: métricas de calidad
- `quality_gate`: estado del quality gate

## Dependencias
- `third-composio-sonar-v1.0` (skill)
- `apb-dev-sonar-clean-v1.0` (skill APB)
- `apb-wf-code-review-v1.0` (workflow)

## Restricciones
- Token gestionado en Azure Key Vault
- No modifica configuraciones del servidor
- Análisis en branches autorizadas únicamente

## Ejemplo de Uso
```
Invocar: prov-sonar-v1.0
Input: { project_key: "APB.LegacyApp", action: "get_issues", branch: "main" }
Output: Lista de issues con severidad y recomendaciones
```

---
*Registrado en APB AI Framework.*
