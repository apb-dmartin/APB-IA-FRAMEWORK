---
id: "third-composio-sonar-v1.0"
name: "Skill: SonarQube Integration (Composio)"
description: "Integración con SonarQube para análisis estático de código, extracción de métricas de calidad y generación de informes de deuda técnica."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
source_repo: "https://github.com/ComposioHQ"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Skill: SonarQube Integration (Composio)

---

## Descripción
Integración con SonarQube para análisis estático de código, extracción de métricas de calidad y generación de informes de deuda técnica.

## Capacidades
- Ejecución de análisis SonarQube vía API
- Extracción de issues, code smells y vulnerabilidades
- Generación de informes de calidad por proyecto
- Tracking de métricas históricas

## Inputs
- `project_key`: clave del proyecto en SonarQube
- `branch`: rama a analizar
- `quality_profile`: perfil de calidad (opcional)

## Outputs
- `sonar_report.md`
- `technical_debt_summary.md`
- `vulnerability_list.md`

## Restricciones
- Requiere token de autenticación SonarQube (AKV)
- Acceso read-only por defecto
- No modifica configuraciones del servidor

## Adaptaciones APB
- Integración con `apb-dev-sonar-clean-v1.0`
- Mapeo a estándares de calidad APB
- Workflow `apb-wf-code-review-v1.0`

## Ejemplo de Uso
```
Invocar: third-composio-sonar-v1.0
Input: { project_key: "APB.LegacyApp", branch: "main" }
Output: sonar_report.md con métricas y recomendaciones APB
```

---
*Adaptado por APB AI Framework. Licencia MIT original respetada.*
