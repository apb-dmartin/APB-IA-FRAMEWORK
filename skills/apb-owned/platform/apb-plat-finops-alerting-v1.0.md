---
id: "apb-plat-finops-alerting-v1.0"
name: "Alertas FinOps con Azure Cost Management"
description: "Configura alertas de coste en Azure Cost Management para APB: presupuestos por subscription/resource group/tag, alertas de anomalías, notificaciones por equipo propietario y dashboard de coste por proyecto. Previene sorpresas en la factura Azure."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
created_date: "2026-06-29"
review_date: "2026-12-29"
---

# Alertas FinOps con Azure Cost Management

## Propósito
Implementar una estrategia de alertas de coste en Azure Cost Management que permita a APB detectar desviaciones de presupuesto antes de que se materialicen en la factura. Configura presupuestos por suscripción, grupo de recursos y tag de proyecto/equipo, alertas de anomalías de coste, y notificaciones dirigidas al equipo propietario del recurso para responsabilizar del gasto a cada área.

## Contexto de Uso
- Alta de un nuevo proyecto o sistema: definir el presupuesto mensual esperado.
- Revisión mensual de costes: ¿algún recurso está disparado respecto al mes anterior?
- Detección de recursos olvidados en dev/staging que siguen corriendo sin uso.
- Preparación del informe de coste mensual para la dirección APB.
- Onboarding de un equipo nuevo en Azure: qué alertas deben configurar desde el primer día.

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `operation` | Enum | `configurar-presupuesto` / `configurar-anomalias` / `generar-dashboard` / `revisar-costes` | ✅ |
| `scope` | Texto | Ámbito: subscription ID, resource group, o tag (ej. `proyecto=gispem`) | ✅ |
| `monthly_budget_eur` | Número | Presupuesto mensual esperado en euros | ❌ |
| `notification_contacts` | Lista | Emails de los responsables que deben recibir las alertas | ❌ |
| `cost_data` | JSON | Export de Azure Cost Management (para `revisar-costes`) | ❌ |

## Estructura de Alertas APB

### Presupuestos por ámbito recomendado
```
Nivel 1 — Subscription: presupuesto total APB Azure mensual
Nivel 2 — Resource Group: presupuesto por entorno (rg-apb-prod, rg-apb-staging, rg-apb-dev)
Nivel 3 — Tag: presupuesto por proyecto/sistema (tag: apb-proyecto=gispem)
```

### Umbrales de alerta en cada presupuesto
| Umbral | % del presupuesto | Acción |
|---|---|---|
| Informativo | 50% | Email al equipo propietario |
| Advertencia | 80% | Email urgente + revisión de recursos |
| Crítico | 100% | Email a dirección TI + análisis inmediato |
| Anomalía | >3σ respecto a media | Alerta de anomalía (Azure Cost Anomaly Detection) |

## Flujo de Trabajo

### Configuración de presupuesto

1. **Definir el presupuesto mensual**:
   - Si no hay histórico: estimar según el sizing de recursos (AKS node pools, VMs, DBs, Storage, egress).
   - Si hay histórico: media de los últimos 6 meses + 20% de margen de seguridad.

2. **Generar el recurso Budget en Azure** (Bicep):
   ```bicep
   resource budget 'Microsoft.Consumption/budgets@2023-05-01' = {
     name: 'budget-{scope}-mensual'
     properties: {
       timePeriod: { startDate: '2026-01-01', endDate: '2030-12-31' }
       timeGrain: 'Monthly'
       amount: {monthly_budget_eur}
       notifications: {
         atFiftyPercent: {
           enabled: true
           operator: 'GreaterThan'
           threshold: 50
           contactEmails: [{notification_contacts}]
         }
         atEightyPercent: {
           enabled: true
           operator: 'GreaterThan'
           threshold: 80
           contactEmails: [{notification_contacts}]
         }
         atOneHundredPercent: {
           enabled: true
           operator: 'GreaterThan'
           threshold: 100
           contactEmails: [{notification_contacts}]
         }
       }
     }
   }
   ```

3. **Configurar detección de anomalías**:
   - Activar Azure Cost Anomaly Detection en el scope.
   - Configurar alerta de anomalía para enviar al mismo grupo de contactos.

4. **Tags obligatorios APB para imputación de costes**:
   ```
   apb-proyecto:    {nombre-proyecto}
   apb-entorno:     {dev|staging|prod}
   apb-equipo:      {nombre-equipo-propietario}
   apb-criticidad:  {low|medium|high|critical}
   ```
   Sin estos tags, los recursos no pueden asignarse a un presupuesto de proyecto.

5. **Dashboard de coste recomendado** (Azure Cost Management):
   - Vista por servicio: ¿qué servicios consumen más? (AKS suele ser el mayor)
   - Vista por tag de proyecto: coste por sistema APB
   - Tendencia mensual: ¿el coste crece, decrece o es estable?
   - Top 10 recursos más caros

### Análisis de revisión mensual

1. Comparar coste actual vs. mes anterior y vs. presupuesto.
2. Identificar recursos con crecimiento >20% mensual sin justificación.
3. Detectar recursos en dev/staging activos 24x7 que podrían apagarse fuera de horario.
4. Verificar que todos los recursos tienen los tags obligatorios APB.

## Salida Esperada

```markdown
# Plan FinOps — Alertas de Coste — [Sistema/Scope] — [Fecha]
> ⚠️ Borrador generado por IA (APB AI Framework - apb-plat-finops-alerting-v1.0) — pendiente revisión del equipo de plataforma APB.

## Presupuestos configurados
| Scope | Presupuesto mensual | Contactos alerta | Estado |
|---|---|---|---|

## Anomalías detectadas (si hay datos de coste)
| Recurso | Coste actual | Media histórica | Variación | Acción |
|---|---|---|---|---|

## Código Bicep de presupuestos
[...]

## Recursos sin tags APB (riesgo de imputación incorrecta)
| Recurso | Resource Group | Tags faltantes |
|---|---|---|
```

## Criterios de Calidad
- [ ] Todos los resource groups de producción tienen presupuesto configurado.
- [ ] Los contactos de alerta incluyen al responsable técnico del sistema Y al responsable de negocio.
- [ ] La detección de anomalías está activada en el scope de producción.
- [ ] Todos los recursos tienen los 4 tags obligatorios APB.

## Dependencias
- `apb-plat-finops-chargeback-v1.0` — las alertas alimentan el proceso de chargeback mensual
- `apb-plat-finops-reservations-v1.0` — las alertas de coste deben compararse con el ahorro por reservas

## Ejemplo de Uso

```
Configura alertas de coste para el proyecto GISPEM (rg-gispem-prod y rg-gispem-staging).
Presupuesto estimado: 3.500 €/mes en prod, 500 €/mes en staging.
Responsable técnico: plataforma@portdebarcelona.cat
Responsable de negocio: operaciones@portdebarcelona.cat
```

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento B |

## ⚠️ Comportamiento ante inputs incompletos

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `operation` | Pregunta: "¿Qué necesitas: configurar presupuesto, alertas de anomalía, dashboard o revisión de costes?" | Sí |
| `scope` | Pregunta: "¿A qué nivel quieres la alerta: subscription, resource group o tag de proyecto?" | Sí |
| `monthly_budget_eur` | Pregunta: "¿Cuál es el presupuesto mensual esperado en euros?" (sin esto no puede configurar el umbral) | Sí (para `configurar-presupuesto`) |
| `notification_contacts` | Usa arquitectura@portdebarcelona.cat como contacto por defecto e indica la asunción | No |
| `cost_data` | Solo requerido para `revisar-costes` — indica cómo obtenerlo si falta | Condicional |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** — callout inmediatamente tras el título H1:
  > ⚠️ Borrador generado por IA (APB AI Framework - apb-plat-finops-alerting-v1.0) — pendiente revisión del equipo de plataforma APB.
