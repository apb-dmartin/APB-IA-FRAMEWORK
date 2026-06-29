---
id: "apb-plat-finops-reservations-v1.0"
name: "Análisis de Reserved Instances y Azure Hybrid Benefit"
description: "Analiza el uso de recursos Azure de APB para recomendar Reserved Instances (RI), Savings Plans y Azure Hybrid Benefit (AHB). Calcula el ahorro estimado frente al pago por uso (pay-as-you-go) y genera el plan de compra de reservas optimizado para el presupuesto anual."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
created_date: "2026-06-29"
review_date: "2026-12-29"
---

# Análisis de Reserved Instances y Azure Hybrid Benefit

## Propósito
Identificar y cuantificar las oportunidades de ahorro en el gasto Azure de APB mediante la compra de Reserved Instances (RI) para recursos con uso estable y la aplicación de Azure Hybrid Benefit (AHB) para licencias de Windows Server y SQL Server existentes. Genera un análisis coste-beneficio por recurso o familia de recursos y una recomendación de compra priorizada por ROI y periodo de amortización.

## Contexto de Uso
- Planificación presupuestaria anual: optimizar el gasto Azure del próximo ejercicio.
- Revisión trimestral FinOps: ¿hay recursos nuevos candidatos a Reserved Instance?
- Evaluación del Azure Hybrid Benefit: ¿estamos aprovechando las licencias SA que ya tiene APB?
- Antes de escalar un sistema: ¿comprar reserva de la nueva capacidad o pagar PAYG?

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `usage_data` | JSON | Datos de uso de los últimos 30-90 días (Azure Advisor recommendations o Cost Management export) | ✅ |
| `reservation_term` | Enum | `1-year` / `3-year` | ❌ |
| `commitment_flexibility` | Booleano | ¿Puede APB comprometerse con el recurso durante 1-3 años sin cambios? | ❌ |
| `current_licenses` | JSON | Licencias Windows Server / SQL Server con Software Assurance disponibles para AHB | ❌ |

## Tipos de Compromiso Azure

| Tipo | Descripción | Ahorro típico | Flexibilidad |
|---|---|---|---|
| **Reserved Instance (RI)** | Compromiso de uso de 1 o 3 años de un recurso específico (VM, SQL DB, PostgreSQL...) | 20-65% vs. PAYG | Baja — recurso específico |
| **Azure Savings Plan** | Compromiso de gasto ($X/hora) aplicable a cualquier compute | 11-17% vs. PAYG | Alta — multi-servicio |
| **Azure Hybrid Benefit (AHB)** | Usar licencias SA propias en Azure en lugar de pagar la licencia en el precio de Azure | 40-85% en VMs Windows/SQL | Inmediato — sin compromiso |

## Candidatos Típicos en APB para Reserved Instances

| Servicio | Condición para RI | Ahorro esperado (3 años) |
|---|---|---|
| AKS node pools (VMs) | Uso >80% de la capacidad del pool de forma constante | 40-60% |
| Azure SQL Database | Base de datos de producción con uso 24x7 | 30-55% |
| PostgreSQL Flexible Server | Instancias de producción con uptime 24x7 | 25-40% |
| Azure Container Instances | No candidato — uso esporádico | — |
| Azure Functions | No candidato — modelo serverless, ya optimizado | — |

## Flujo de Trabajo

1. **Análisis de utilización** (desde Azure Advisor o Cost Management):
   - Identificar recursos con uso >70% durante los últimos 30 días.
   - Separar recursos estables (prod 24x7) de recursos variables (dev, batch).
   - Calcular el ahorro potencial para 1 año y 3 años.

2. **Cálculo de ahorro por RI**:
   ```
   Ahorro anual = (Precio PAYG/hora - Precio RI/hora) × horas/año
   
   Ejemplo (Azure SQL S3 en West Europe):
   PAYG: 0.19 €/hora → 1.664 €/año
   RI 1 año: 0.13 €/hora → 1.139 €/año
   Ahorro: 525 €/año (32%)
   
   RI 3 años: 0.09 €/hora → 788 €/año
   Ahorro total 3 años: 2.628 € (53%)
   ```

3. **Evaluación de Azure Hybrid Benefit**:
   - Inventariar licencias Windows Server y SQL Server con SA activo en APB.
   - Calcular cuántas VMs de AKS y Azure SQL pueden beneficiarse del AHB.
   - Ahorro: en AKS, AHB elimina el coste de licencia Windows (~40% del precio de la VM).

4. **Plan de compra priorizado** (por ROI):
   - Ordenar candidatos por periodo de amortización (payback period).
   - Primero: AHB (inmediato, sin coste adicional — solo configuración).
   - Segundo: RI de los recursos más caros y estables (mayor ahorro absoluto).
   - Tercero: Savings Plan si hay uso compute diverso y difícil de predecir.

5. **Consideraciones de flexibilidad**:
   - RI de 1 año para recursos que podrían cambiar de tier en 12-18 meses.
   - RI de 3 años para recursos estables y maduros (bases de datos de producción).
   - Las RI de Azure son transferibles entre subscriptions dentro del mismo Enterprise Agreement.

6. **⚠️ CHECKPOINT HUMANO**: La compra de Reserved Instances requiere aprobación de Dirección TI y puede requerir proceso de compra LCSP si el importe supera los umbrales.

## Salida Esperada

```markdown
# Análisis de Reservas Azure — APB — [Período]
> ⚠️ Borrador generado por IA (APB AI Framework - apb-plat-finops-reservations-v1.0) — pendiente validación por Plataforma TI APB y aprobación de compra.

## Resumen de Oportunidades
| Tipo | Ahorro anual estimado | Inversión | Payback |
|---|---|---|---|
| Azure Hybrid Benefit | | €0 (ya licenciado) | Inmediato |
| Reserved Instances (1 año) | | | |
| Reserved Instances (3 años) | | | |

## Detalle por Recurso/Familia
| Recurso | Coste PAYG actual | Coste con RI | Ahorro anual | Término recomendado |
|---|---|---|---|---|

## Azure Hybrid Benefit
| VM / SQL | Licencias SA disponibles | Ahorro mensual |
|---|---|---|

## Plan de Compra Priorizado
1. AHB en [lista de recursos] → ahorro inmediato sin inversión
2. RI 1 año para [recurso X] → payback en [N meses]
3. RI 3 años para [recurso Y] → mayor ahorro total
```

## Criterios de Calidad
- [ ] Solo se recomiendan RI para recursos con uso >70% demostrado en los últimos 30 días.
- [ ] El AHB está evaluado para todas las VMs Windows y Azure SQL de APB.
- [ ] El payback period está calculado explícitamente para cada recomendación.
- [ ] Las RI de 3 años solo se recomiendan para recursos con baja probabilidad de cambio.

## Dependencias
- `apb-plat-finops-alerting-v1.0` — las alertas de coste son prerequisito para identificar candidatos
- `apb-plat-finops-chargeback-v1.0` — el ahorro de reservas debe reflejarse en el informe de chargeback

## Ejemplo de Uso

```
Analiza las oportunidades de Reserved Instances para APB.
Tenemos AKS con 5 nodos D4s_v3 (prod), Azure SQL S3 (GISPEM), PostgreSQL Flexible B4ms (3 instancias).
Todo en uso 24x7 en producción. Periodo de análisis: últimos 3 meses.
¿Cuánto ahorraríamos con RI de 1 año y de 3 años?
```

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento B |

## ⚠️ Comportamiento ante inputs incompletos

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `usage_data` | Pregunta: "Necesito datos de uso de los últimos 30-90 días. ¿Puedes exportar las recomendaciones de Azure Advisor o el export de Cost Management?" | Sí |
| `reservation_term` | Genera análisis para 1 año Y 3 años, indicando cuál recomienda para cada recurso | No |
| `commitment_flexibility` | Asume flexibilidad media (posibles cambios en 18 meses) e indica la asunción | No |
| `current_licenses` | Indica que sin este dato no puede evaluar AHB; genera el resto del análisis sin esa sección | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** — callout inmediatamente tras el título H1:
  > ⚠️ Borrador generado por IA (APB AI Framework - apb-plat-finops-reservations-v1.0) — pendiente validación por Plataforma TI APB y aprobación de compra.
