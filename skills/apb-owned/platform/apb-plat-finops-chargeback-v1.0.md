---
id: "apb-plat-finops-chargeback-v1.0"
name: "Chargeback y Asignación de Costes Azure"
description: "Genera el informe de asignación de costes Azure por proyecto, equipo y entorno para el proceso de chargeback interno de APB. Usa los tags de recursos para imputar el coste a cada área de negocio y genera el desglose mensual listo para comunicar a dirección."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
created_date: "2026-06-29"
review_date: "2026-12-29"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# Chargeback y Asignación de Costes Azure


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Propósito
Proporcionar el informe mensual de asignación de costes Azure por proyecto, equipo y entorno para el proceso de chargeback interno de APB. Transforma el export de Azure Cost Management (datos brutos de coste por recurso) en un informe estructurado que permite a cada área de negocio conocer cuánto gasta en infraestructura Azure y tomar decisiones informadas de optimización o inversión.

## Contexto de Uso
- Cierre mensual: generar el informe de chargeback para cada área de APB.
- Inicio de año: definir los presupuestos anuales por área basándose en el histórico de gasto.
- Proyecto nuevo: estimar el coste mensual esperado y asignarlo al área de negocio correspondiente.
- Auditoría interna: verificar que el gasto Azure está correctamente imputado por proyecto.

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `cost_export` | JSON/CSV | Export de Azure Cost Management del período | ✅ |
| `period` | Texto | Período del informe: ej. "Mayo 2026" | ✅ |
| `allocation_rules` | JSON | Reglas de asignación para costes compartidos (ej. AKS cluster compartido → % por namespace) | ❌ |
| `previous_period_data` | JSON | Datos del período anterior para comparativa de tendencia | ❌ |

## Modelo de Asignación de Costes APB

### Costes directamente imputables (por tag)
Recursos con tag `apb-proyecto` → coste 100% al proyecto indicado.

```
Tags que permiten imputación directa:
  apb-proyecto:  {nombre-proyecto}
  apb-equipo:    {equipo-propietario}
  apb-entorno:   {dev|staging|prod}
```

### Costes compartidos (requieren reglas de asignación)
Recursos que sirven a múltiples proyectos → requieren reparto:

| Recurso compartido | Regla de reparto recomendada |
|---|---|
| AKS cluster | % de CPU/memoria consumida por namespace |
| Azure Service Bus namespace | % de mensajes enviados/recibidos por sistema |
| Azure Monitor / Log Analytics | % de volumen de logs ingestado por proyecto |
| Redes (VNet, ExpressRoute) | Proporcional al número de recursos en cada proyecto |
| Key Vault compartido | Proporcional al número de secretos por proyecto |

### Costes no imputables / overhead TI
Costes de infraestructura base que no pueden asignarse a un proyecto específico:
- Licencias de seguridad (Defender for Cloud, Sentinel).
- Herramientas de gestión (Azure Policy, Cost Management).
- Costes de conectividad (ExpressRoute a Barcelona).

Estos costes se imputan al centro de coste de Infraestructura TI APB.

## Flujo de Trabajo

1. **Procesamiento del export de Cost Management**:
   - Filtrar recursos sin tags — identificar como "Sin imputar" y alertar.
   - Agrupar por tag `apb-proyecto`.
   - Separar costes directos de costes compartidos.

2. **Aplicación de reglas de reparto** (costes compartidos):
   - Para cada recurso compartido, aplicar la regla de reparto definida.
   - Si no hay datos de uso disponibles (ej. CPU por namespace de AKS), usar reparto proporcional por número de recursos.

3. **Generación del informe por área de negocio**:
   - Coste total del período vs. presupuesto del período.
   - Desglose: costes directos + parte proporcional de costes compartidos.
   - Comparativa vs. período anterior.
   - Top 3 servicios de mayor coste en el área.

4. **Identificación de oportunidades de optimización**:
   - Recursos en dev/staging con uptime 24x7 que podrían apagarse.
   - Recursos con uso <10% de la capacidad provisionada (oversized).
   - Candidatos a Reserved Instances o Savings Plans.

5. **⚠️ CHECKPOINT HUMANO**: El responsable de plataforma valida el reparto de costes compartidos antes de comunicar el chargeback a las áreas.

## Salida Esperada

```markdown
# Informe de Chargeback Azure — [Período]
> ⚠️ Borrador generado por IA (APB AI Framework - apb-plat-finops-chargeback-v1.0) — pendiente validación por Plataforma TI APB antes de comunicar a las áreas.

## Resumen Ejecutivo
| Área | Coste directo | Coste compartido | Total | Presupuesto | Variación vs. mes anterior |
|---|---|---|---|---|---|

## Detalle por Proyecto
### Proyecto: {nombre}
| Servicio | Recurso | Coste | % del total del proyecto |
|---|---|---|---|

## Costes sin imputar (recursos sin tags)
| Recurso | Resource Group | Coste | Acción requerida |
|---|---|---|---|

## Oportunidades de Optimización
| Oportunidad | Ahorro estimado/mes | Esfuerzo | Prioridad |
|---|---|---|---|
```

## Criterios de Calidad
- [ ] Los recursos sin tags están identificados y tienen acción de remediación asignada.
- [ ] Los costes compartidos están repartidos con una regla documentada y reproducible.
- [ ] El total del informe de chargeback coincide con la factura Azure del período.
- [ ] Las oportunidades de optimización tienen estimación de ahorro cuantificada.

## Dependencias
- `apb-plat-finops-alerting-v1.0` — las alertas de presupuesto alimentan este informe
- `apb-plat-finops-reservations-v1.0` — el análisis de reservas es una optimización recurrente en este informe

## Ejemplo de Uso

```
Genera el informe de chargeback de mayo 2026 para APB.
Adjunto el export de Azure Cost Management (CSV).
Tenemos 3 proyectos principales: GISPEM, Portal Ciudadano, Plataforma IA.
El AKS cluster es compartido entre los 3 proyectos — reparte por CPU consumida.
```

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento B |

## ⚠️ Comportamiento ante inputs incompletos

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `cost_export` | Pregunta: "Necesito el export de Azure Cost Management. ¿Puedes exportarlo desde Azure Portal → Cost Management → Export?" | Sí |
| `period` | Pregunta: "¿De qué período es el informe (mes y año)?" | Sí |
| `allocation_rules` | Usa reparto proporcional por número de recursos para costes compartidos e indica la asunción | No |
| `previous_period_data` | Genera informe sin comparativa de tendencia e indica que falta el dato | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** — callout inmediatamente tras el título H1:
  > ⚠️ Borrador generado por IA (APB AI Framework - apb-plat-finops-chargeback-v1.0) — pendiente validación por Plataforma TI APB antes de comunicar a las áreas.
