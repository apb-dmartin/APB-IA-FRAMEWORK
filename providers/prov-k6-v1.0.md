---
id: "prov-k6-v1.0"
name: "Provider: k6 MCP"
description: "Proveedor de acción para pruebas de rendimiento con k6. Permite ejecutar tests de carga, estrés y picos con generación de informes detallados."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
provider_type: "action"
access_mode: "read-write"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Provider: k6 MCP

---

## Descripción
Proveedor de acción para pruebas de rendimiento con k6. Permite ejecutar tests de carga, estrés y picos con generación de informes detallados.

## Capacidades
- Ejecución de scripts k6
- Tests de carga, estrés y picos
- Generación de métricas de rendimiento
- Comparación con umbrales SLO
- Exportación a Grafana Cloud

## Configuración
```json
{
  "provider_id": "prov-k6-v1.0",
  "type": "action",
  "endpoint": "local://k6",
  "auth": "none",
  "rate_limit": "unlimited",
  "environments": ["local", "staging", "production"]
}
```

## Inputs
- `script_path`: ruta al script k6
- `environment`: entorno de ejecución
- `vus`: número de usuarios virtuales
- `duration`: duración del test
- `thresholds`: umbrales de aceptación

## Outputs
- `test_results`: resultados del test
- `metrics`: métricas de rendimiento
- `report`: informe HTML
- `comparison`: comparación con SLOs

## Dependencias
- `apb-ops-slo-design-v1.0` (skill)
- `apb-agent-sre-v1.0` (agente)
- `apb-wf-qa-evidence-v1.0` (workflow)

## Restricciones
- No ejecuta en producción sin aprobación
- Requiere entorno con k6 instalado
- Datos de producción anonimizados en tests

## Ejemplo de Uso
```
Invocar: prov-k6-v1.0
Input: { script_path: "tests/perf/api-load.js", vus: 100, duration: "5m", environment: "staging" }
Output: test_results.json + report.html con métricas de rendimiento
```

---
*Registrado en APB AI Framework.*
