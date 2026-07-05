---
id: "prov-otel-v1.0"
name: "Provider: OpenTelemetry (instrumentación y telemetría)"
description: "Proveedor de instrumentación estándar OpenTelemetry (trazas, métricas y logs) para las aplicaciones APB y el propio framework. Cubre el gap diferido en Sesión 17 (#39/#40): la telemetría real que alimenta los dashboards de observabilidad y los KPIs de proyecto.md §6. Exporta a Azure Monitor vía prov-azure-monitor-v1.0. Agnóstico de LLM y de backend (OTLP)."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
provider_type: "action"
access_mode: "read-write"
source_repo: "https://github.com/open-telemetry/opentelemetry-specification"
source_license: "Apache-2.0"
source_commit: "unverified"
verified_date: "2026-07-04"
created_date: "2026-07-04"
review_date: "2026-07-04"
---

# Provider: OpenTelemetry (instrumentación y telemetría)

> **Herramienta de instrumentación.** Estándar abierto (CNCF) para trazas, métricas y logs. No es
> un backend: instrumenta el código y exporta vía OTLP al backend elegido (en APB, Azure Monitor
> a través de `prov-azure-monitor-v1.0`). Agnóstico de LLM, de lenguaje y de backend.

---

## Descripción

OpenTelemetry (OTel, Apache-2.0) es el estándar CNCF de instrumentación de aplicaciones. Da a APB
una forma **uniforme y agnóstica de proveedor** de generar telemetría (trazas distribuidas,
métricas y logs) desde las aplicaciones .NET/Azure del stack DOCKS y desde el propio framework.

Cubre el gap identificado y **diferido en Sesión 17** (`PLAN_FASES_FUTURAS.md` §F, «Telemetría
automática → OpenTelemetry Python»; §K/R7 «Telemetría no instrumentada → KPIs imposibles de
medir»): hoy `scripts/emit_telemetry.py` y `apb-ops-telemetry-emit-v1.0` emiten eventos a Azure
Monitor de forma puntual, pero no hay instrumentación OTel que capture trazas/métricas
automáticamente para alimentar los dashboards de `apb-agent-observability-v1.0` ni los KPIs de
`proyecto.md` §6.

## Activación (norma del framework — conceptual → real)

Conforme a la norma fijada por Débora (memoria `feedback_mcp_framework_activacion`), al activar de
verdad esta instrumentación:
1. Añadir los SDK/exporters OTel a las aplicaciones (por lenguaje) y configurar el **OTLP
   endpoint** hacia Azure Monitor (Application Insights) o el Collector corporativo.
2. Actualizar este descriptor con la configuración real verificada (hoy `draft`, sin activar) y
   **fijar `source_commit` a un SHA/tag real** de la versión de la especificación/SDK adoptada
   (hoy `unverified` por falta de acceso de red — deuda de supply-chain documentada, GOVERNANCE §4.2).

```
# Configuración de referencia (variables de entorno OTLP → Azure Monitor)
OTEL_EXPORTER_OTLP_ENDPOINT   = https://<region>.applicationinsights.azure.com  # o Collector APB
OTEL_SERVICE_NAME             = <app-o-componente>
OTEL_RESOURCE_ATTRIBUTES      = service.namespace=apb,deployment.environment=<PRE|PRO>
# Autenticación vía Managed Identity → AKV (nunca secreto en fichero)
```

## Capacidades

- **Trazas distribuidas:** seguimiento de una petición a través de servicios/APIs (correlación end-to-end).
- **Métricas:** latencia, throughput, tasa de error, saturación (base de los SLO de `apb-ops-slo-design-v1.0`).
- **Logs correlacionados:** logs enlazados a la traza/span que los originó.
- **Exportación OTLP** al backend elegido (Azure Monitor vía `prov-azure-monitor-v1.0`; Prometheus/Grafana para los subagentes de observabilidad).

## Restricciones

- **No es un backend de almacenamiento ni de dashboards:** instrumenta y exporta; el almacenamiento y la visualización son de Azure Monitor / Grafana / Power BI.
- No sustituye a `apb-ops-telemetry-emit-v1.0` (telemetría de gobernanza del framework: quién invocó qué componente) — son complementarios: OTel = telemetría técnica de aplicación; telemetry-emit = telemetría de uso/gobernanza.
- Autenticación siempre por Managed Identity → Azure Key Vault; **nunca** claves en ficheros ni en este descriptor.
- La activación real requiere decisión de Plataforma sobre backend (Application Insights vs. Collector propio) y entornos — pendiente (bloqueo de Plataforma, no del framework).

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-04 | Arquitectura APB | Incorporación (cobertura de hueco #39/#40, diferido en Sesión 17) — provider de instrumentación, `draft` sin activar; `source_commit` unverified pendiente de fijar |

---
*Registrado en APB AI Framework. Requiere revisión humana antes de aprobación.*
