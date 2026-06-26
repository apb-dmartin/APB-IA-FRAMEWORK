---
id: "apb-plat-finops-v1.0"
name: "Evaluación FinOps"
description: "Analizar el gasto en cloud (Azure), identificar oportunidades de optimización de costes y generar recomendaciones de FinOps. Incluye tagging strategy, rightsizing, reserved instances, spot instances, y eliminación de recursos huérfanos."
version: "1.0.0"
status: "draft"
owner: "FinOps APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Evaluación FinOps

## Propósito
Analizar el gasto en cloud (Azure), identificar oportunidades de optimización de costes y generar recomendaciones de FinOps. Incluye tagging strategy, rightsizing, reserved instances, spot instances, y eliminación de recursos huérfanos.

## Contexto de Uso
- Revisión mensual/trimestral de gasto en Azure.
- Optimización de costes post-migración a cloud.
- Establecimiento de prácticas FinOps y cultura de responsabilidad de costes.
- Integración con gobierno y reportes financieros.

## Entradas Requeridas
| Entrada | Tipo | Descripción | Obligatorio |
|---------|------|-------------|-------------|
| `azure_cost_export` | CSV / JSON | Export de costes de Azure Cost Management | ✅ |
| `resource_inventory` | JSON / CSV | Inventario de recursos Azure con tags actuales | ✅ |
| `budget_thresholds` | Lista | Umbrales de presupuesto por subscription, resource group o tag | ❌ |
| `optimization_scope` | Enum | `all`, `compute`, `storage`, `network`, `database`, `devtest` | ❌ (default: all) |

## Flujo de Trabajo (Pasos)
1. **Ingesta de datos**: Cargar export de costes y inventario de recursos.
2. **Análisis de tagging**: Evaluar cobertura de tags obligatorios (proyecto, entorno, owner, cost-center).
3. **Identificación de anomalías**: Detectar picos de gasto, recursos sin tag, suscripciones sobre presupuesto.
4. **Análisis por categoría**:
   - **Compute**: Rightsizing de VMs, uso de reserved instances, Azure Hybrid Benefit.
   - **Storage**: Tiering (hot/cool/archive), eliminación de blobs huérfanos.
   - **Network**: Optimización de data transfer, ExpressRoute vs VPN.
   - **Database**: DTU/vCore optimization, elastic pools, serverless tier.
   - **Dev/Test**: Uso de suscripciones Dev/Test, apagado programado.
5. **Oportunidades de ahorro**: Cuantificar potencial de ahorro por recomendación.
6. **Generación de informe**: Dashboard de costes, recomendaciones priorizadas por ROI.
7. **Plan de acción**: Acciones con responsable, esfuerzo estimado y ahorro esperado.
8. **Registro de evidencia**: Metadatos para gobierno y seguimiento.

## Salida Esperada
### Estructura del Informe
```markdown
# Informe FinOps — [Período]
> Fecha: [YYYY-MM-DD] | Autor: FinOps Agent | Scope: [optimization_scope]

## 1. Resumen Ejecutivo
## 2. Evolución de Gasto
## 3. Análisis de Tagging
## 4. Anomalías Detectadas
## 5. Oportunidades de Optimización
| Categoría | Recurso | Recomendación | Ahorro Estimado/Mes | Esfuerzo | Prioridad |
## 6. Plan de Acción
## 7. Benchmarks y KPIs
## 8. Recomendaciones de Gobierno
## 9. Evidencia y Metadatos
```

## Criterios de Calidad
- [ ] 100% de recursos evaluados tienen cobertura de tags obligatorios verificada.
- [ ] Cada anomalía de gasto tiene explicación técnica o de uso propuesta.
- [ ] Cada recomendación de optimización incluye cálculo de ahorro estimado.
- [ ] Plan de acción priorizado por ROI (mayor ahorro / menor esfuerzo primero).
- [ ] El informe incluye KPIs de FinOps: tagging coverage, budget variance, cost per transaction.
- [ ] El informe es revisable por el equipo financiero y de cloud sin intervención del agente.

## Stack y Tecnologías
- Azure Cost Management + Billing, Azure Advisor
- KQL para análisis de costes
- Power BI / Excel para visualización
- FinOps Foundation Framework
- Formatos: Markdown, Excel, JSON para automatización

## Dependencias
- `apb-plat-cloud-ready-v1.0` — para contexto de recursos migrados
- `apb-gov-evidence-v1.0` — para generación de evidencia
- `apb-gov-catalog-v1.0` — para tracking de recursos en catálogo

## Ejemplo de Uso
**Prompt de invocación:**
```
Analiza nuestro gasto de Azure del último trimestre:
- Export de costes: [adjuntar CSV de Cost Management]
- Inventario de recursos: [adjuntar JSON de Azure Resource Graph]
- Presupuesto mensual: 15.000 EUR
- Anomalía detectada: gasto duplicado en Storage Account de backup
- Scope: compute y storage prioritariamente
```

## Notas y Advertencias
- **Nivel 1**: El agente analiza datos exportados; no tiene acceso directo a suscripciones de Azure ni ejecuta acciones de optimización.
- **Revisión humana obligatoria** antes de aplicar cualquier recomendación que afecte a producción.
- Los cálculos de ahorro son estimaciones basadas en tarifas públicas; pueden variar con descuentos corporativos.
- Las recomendaciones de reserved instances requieren análisis de uso sostenido (≥ 1 año).
- El agente no tiene acceso a datos de facturación confidenciales; trabaja con exports anonimizados.

## Historial de Cambios
| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-20 | Arquitectura APB | Creación inicial |


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-plat-finops-v1.0) - pendiente validacion humana. No distribuir sin revision.
