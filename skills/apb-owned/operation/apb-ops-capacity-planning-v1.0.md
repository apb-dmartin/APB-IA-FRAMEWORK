---
id: "apb-ops-capacity-planning-v1.0"
name: "Capacity Planning y Forecasting"
description: "Forecasting de demanda de infraestructura basado en métricas históricas y proyecciones de negocio. Especialmente orientado a la estacionalidad del tráfico portuario APB (cruceros en verano, campañas logísticas). Produce recomendaciones de right-sizing y planificación de capacidad a 3-12 meses."
version: "1.0.0"
status: "draft"
owner: "SRE APB <arquitectura@portdebarcelona.cat>"
domain: "operation"
autonomy_level: 1
created_date: "2026-06-27"
review_date: "2026-06-27"
---

# Capacity Planning y Forecasting

## Propósito
Analizar el consumo histórico de recursos de infraestructura y proyectar la demanda futura, considerando la estacionalidad del negocio portuario APB. Produce recomendaciones de right-sizing, alertas de capacidad y plan de escalado para los próximos 3-12 meses.

## Contexto de Uso
- Planificación presupuestaria anual de infraestructura cloud.
- Preparación ante períodos de alta demanda (temporada de cruceros, campañas de logística).
- Right-sizing de recursos Azure sobreaprovisionados.
- Decisiones de compra de Reserved Instances (1 año / 3 años).

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `service_name` | Texto | Servicio o conjunto de servicios a analizar | ✅ |
| `historical_metrics` | JSON / CSV | Métricas de CPU, memoria, storage, red — mínimo 90 días | ✅ |
| `forecast_horizon` | Enum | `3m`, `6m`, `12m` | ✅ (default: 6m) |
| `business_events` | Lista | Eventos de negocio conocidos con impacto en tráfico (fechas, tipo) | ❌ |
| `current_sizing` | JSON | Configuración actual: SKU, nodos, réplicas, tiers | ❌ |
| `budget_constraint` | Número | Presupuesto máximo mensual en EUR (si existe) | ❌ |

## Flujo de Trabajo

1. **Análisis de datos históricos**:
   - Identificar patrones de uso: diario (hora punta), semanal, mensual, estacional.
   - Calcular percentiles: p50, p90, p99 de CPU, memoria y tráfico de red.
   - Detectar outliers y eventos especiales que distorsionen la media.

2. **Identificación de patrones de estacionalidad APB**:
   - Temporada alta de cruceros: junio-septiembre (pico de actividad en portales ciudadanos y sistemas logísticos).
   - Campañas logísticas: períodos de alta carga de contenedores.
   - Horario laboral vs. nocturno: sistemas batch vs. tiempo real.

3. **Modelado de demanda futura**:
   - Aplicar trend analysis (tendencia de crecimiento mensual/anual).
   - Superponer estacionalidad histórica sobre la tendencia.
   - Incorporar eventos de negocio conocidos (nuevas rutas, proyectos IT planificados).
   - Producir 3 escenarios: conservador (p50), base (p75), pesimista (p90).

4. **Análisis de capacidad actual**:
   - ¿Cuándo se alcanzará el límite de la configuración actual en cada escenario?
   - Identificar cuellos de botella: ¿CPU, memoria, IOPS, red?
   - Detectar recursos sobreaprovisionados (uso medio <20% del aprovisionado).

5. **Recomendaciones de right-sizing**:
   - Downsizing para recursos sobreaprovisionados.
   - Upscaling preventivo antes de períodos de alta demanda.
   - Recomendaciones de Auto-scaling (HPA en AKS, Azure Scale Sets).
   - Análisis de coste: ahorro estimado por right-sizing vs. coste de upscaling.

6. **Plan de escalado**:
   - Calendario de acciones de capacidad con fechas y responsables.
   - Recomendaciones de Reserved Instances si el uso proyectado es estable >70%.
   - Alertas de capacidad: umbrales de monitorización a configurar.

7. **⚠️ CHECKPOINT HUMANO**: Las decisiones de compra de reservas (compromisos financieros 1-3 años) requieren aprobación de dirección TI y FinOps.

## Salida Esperada

```markdown
# Capacity Planning — [Servicio/Sistema]
> Período analizado: [inicio] → [fin] | Horizonte: [3m/6m/12m]
> Generado: [fecha] | Revisión requerida: [fecha]

## Resumen Ejecutivo
| Métrica | Actual | P90 en [horizonte] | Capacidad límite |

## Patrones de Uso Detectados
| Patrón | Descripción | Impacto en capacidad |

## Proyecciones de Demanda
| Escenario | CPU p90 | Memoria p90 | Tráfico p90 | Alcance límite |

## Recursos Sobreaprovisionados (candidatos a right-sizing)
| Recurso | Uso medio actual | SKU actual | SKU recomendado | Ahorro estimado/mes |

## Plan de Escalado
| Acción | Fecha | Responsable | Coste estimado |

## Recomendaciones Reserved Instances
| Recurso | Compromiso | Ahorro vs. pay-as-you-go | Condición |
```

## Criterios de Calidad
- [ ] El análisis usa al menos 90 días de datos históricos.
- [ ] Las proyecciones contemplan al menos 3 escenarios (conservador, base, pesimista).
- [ ] Los períodos de estacionalidad APB están explícitamente modelados.
- [ ] Las recomendaciones de right-sizing cuantifican el ahorro estimado.
- [ ] El plan de escalado tiene fechas y owners concretos.

## Stack y Tecnologías
- Datos: Azure Monitor (métricas de AKS, ACA, Azure SQL, App Service)
- Análisis: trend modeling, percentiles, seasonality decomposition
- Costes: Azure Cost Management, Azure Pricing Calculator

## Dependencias
- `apb-ops-slo-design-v1.0` — para alinear capacidad con objetivos de servicio
- `apb-ops-observability-v1.0` — para disponer de métricas de base

## Ejemplo de Uso

```
Analiza la capacidad del cluster AKS de producción APB.
Tenemos métricas de Azure Monitor de los últimos 6 meses (adjunto CSV).
La temporada de cruceros empieza el 1 de julio y esperamos un 40% más de tráfico
en el portal ciudadano. Necesito saber si el cluster aguanta y si debo comprar
reservas para los nodos.
Horizonte de planificación: 12 meses.
```

## Notas y Advertencias
- **Nivel 1**: El agente produce el plan; las decisiones de compra de reservas requieren aprobación humana.
- La fiabilidad del forecast aumenta con más datos históricos: mínimo 90 días, óptimo 12 meses.
- La estacionalidad portuaria APB es específica del dominio: incorporar el calendario de operaciones portuarias de cada año.
- Las proyecciones son estimaciones; deben revisarse mensualmente y ajustarse con datos reales.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-27 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento A, Bloque 2 |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-ops-capacity-planning-v1.0) - pendiente validacion humana. No distribuir sin revision.
