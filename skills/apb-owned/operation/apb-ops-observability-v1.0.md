---
id: "apb-ops-observability-v1.0"
name: "Diseño de Observabilidad"
description: "Diseñar estructuras de observabilidad (métricas, logs, traces, alertas) para servicios y sistemas en Azure. Genera configuraciones de Application Insights, Log Analytics, dashboards y alertas siguiendo las mejores prácticas de observabilidad."
version: "1.0.0"
status: "draft"
owner: "SRE APB <arquitectura@portdebarcelona.cat>"
domain: "operation"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Diseño de Observabilidad

## Propósito
Diseñar estructuras de observabilidad (métricas, logs, traces, alertas) para servicios y sistemas en Azure. Genera configuraciones de Application Insights, Log Analytics, dashboards y alertas siguiendo las mejores prácticas de observabilidad.

## Contexto de Uso
- Onboarding de nuevos servicios a la plataforma de observabilidad.
- Revisión y mejora de observabilidad de servicios existentes.
- Diseño de dashboards y alertas para operación 24/7.
- Integración con workflows de operación y gobierno.

## Entradas Requeridas
| Entrada | Tipo | Descripción | Obligatorio |
|---------|------|-------------|-------------|
| `service_description` | Texto / Markdown | Descripción del servicio y componentes | ✅ |
| `azure_resources` | Lista | Recursos Azure a monitorizar | ✅ |
| `critical_user_journeys` | Lista | Flujos críticos de usuario a trazar | ❌ |
| `alerting_requirements` | Lista | Requisitos de alerta: SLA, escalado, canales | ❌ |

## Flujo de Trabajo (Pasos)
1. **Análisis de componentes**: Identificar todos los recursos Azure y dependencias a monitorizar.
2. **Diseño de métricas**: Definir métricas custom y de plataforma:
   - **Golden signals**: Latency, Traffic, Errors, Saturation.
   - **Métricas de negocio**: Transacciones por minuto, usuarios activos.
   - **Métricas de infraestructura**: CPU, memory, disk, network.
3. **Diseño de logging**: Estructura de logs (structured logging), niveles, correlación con correlation IDs.
4. **Diseño de distributed tracing**: Configuración de Application Insights para end-to-end tracing.
5. **Diseño de dashboards**: Layout de dashboards en Azure Monitor / Grafana:
   - Dashboard de salud del servicio.
   - Dashboard de SLOs.
   - Dashboard de negocio.
6. **Diseño de alertas**: Definir alertas con severidad, umbral, ventana y acción:
   - **Critical**: Paging (PagerDuty, OpsGenie).
   - **Warning**: Ticket de alta prioridad.
   - **Info**: Dashboard o log.
7. **Configuración de Log Analytics**: Queries KQL para análisis comunes y troubleshooting.
8. **Documentación**: Guía de observabilidad con enlaces a dashboards, queries y runbooks.
9. **Registro de evidencia**: Metadatos para gobierno.

## Salida Esperada
### Archivos Generados
```
observability/
├── observability-design.md
├── dashboards/
│   ├── health-dashboard.json
│   ├── slo-dashboard.json
│   └── business-dashboard.json
├── alerts/
│   ├── critical-alerts.json
│   └── warning-alerts.json
├── kql-queries/
│   ├── troubleshooting.kql
│   └── slo-monitoring.kql
└── README-observability.md
```

### Estructura del Diseño
```markdown
# Diseño de Observabilidad — [Nombre Servicio]
> Fecha: [YYYY-MM-DD] | Autor: SRE Agent | Plataforma: Azure Monitor

## 1. Alcance y Componentes
## 2. Métricas
## 3. Logging
## 4. Distributed Tracing
## 5. Dashboards
## 6. Alertas
| Nombre | Métrica | Umbral | Ventana | Severidad | Acción |
## 7. KQL Queries
## 8. Runbooks Vinculados
## 9. Evidencia y Metadatos
```

## Criterios de Calidad
- [ ] Todos los componentes del servicio tienen métricas, logs o traces definidos.
- [ ] Las alertas cubren los 4 golden signals.
- [ ] Cada alerta tiene severidad, acción de escalado y runbook vinculado.
- [ ] Los dashboards son actionable (indican estado, tendencia y detalle).
- [ ] Las queries KQL son reutilizables y documentadas.
- [ ] El diseño es revisable por el equipo de operaciones sin intervención del agente.

## Stack y Tecnologías
- Azure Monitor, Application Insights, Log Analytics Workspace
- Azure Dashboards, Grafana
- KQL (Kusto Query Language)
- Alerting: Azure Monitor Alerts, Action Groups, PagerDuty/OpsGenie
- Formatos: JSON para dashboards/alerts, Markdown para documentación

## Dependencias
- `apb-ops-slo-design-v1.0` — para alineación de alertas con SLOs
- `apb-ops-operability-v1.0` — para contexto de evaluación operacional
- `apb-plat-terraform-v1.0` — para generación de infraestructura de observabilidad

## Ejemplo de Uso
**Prompt de invocación:**
```
Diseña la observabilidad para nuestro microservicio de facturación:
- Servicio: ASP.NET Core 8, Azure Container Apps, Azure SQL, Service Bus
- Recursos: Container App, SQL Database, Service Bus Namespace, Key Vault
- Flujos críticos: Generación de factura, envío por email, notificación a SAP
- Requisitos: Alerta en < 2 minutos para errores críticos, dashboard de SLOs
```

## Notas y Advertencias
- **Nivel 1**: El agente diseña configuraciones; no las despliega en Azure Monitor directamente.
- **Revisión humana obligatoria** antes de desplegar alertas críticas.
- Los umbrales de alerta deben calibrarse con datos reales de producción.
- El agente no tiene acceso a suscripciones de Azure; las configuraciones son plantillas.

## Historial de Cambios
| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-20 | Arquitectura APB | Creación inicial |
