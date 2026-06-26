---
id: "third-ccusage-analytics-v1.0"
name: "Skill: Claude Code Usage Analytics (ccusage)"
description: "Análisis de uso y costes de Claude Code con métricas de productividad, identificación de patrones de uso y recomendaciones de optimización."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
source_repo: "https://github.com/ccusage"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Skill: Claude Code Usage Analytics (ccusage)

---

## Descripción
Análisis de uso y costes de Claude Code con métricas de productividad, identificación de patrones de uso y recomendaciones de optimización.

## Capacidades
- Tracking de tokens y costes por sesión
- Métricas de productividad (tokens/resultado)
- Identificación de patrones de uso ineficiente
- Recomendaciones de optimización de prompts

## Inputs
- `usage_logs`: logs de uso de Claude Code
- `time_range`: rango temporal del análisis
- `team_id`: identificador del equipo (opcional)

## Outputs
- `usage_report.md`
- `cost_analysis.md`
- `optimization_recommendations.md`

## Restricciones
- Requiere acceso a logs de uso
- Datos agregados únicamente
- No identifica individuos sin consentimiento

## Adaptaciones APB
- Integración con `apb-agent-finops-v1.0`
- Dashboard de gobierno de IA
- Métricas de ROI de agentes APB

## Ejemplo de Uso
```
Invocar: third-ccusage-analytics-v1.0
Input: { usage_logs: "...", time_range: "2026-06-01/2026-06-21" }
Output: usage_report.md con costes y recomendaciones
```

---
*Adaptado por APB AI Framework. Licencia MIT original respetada.*
