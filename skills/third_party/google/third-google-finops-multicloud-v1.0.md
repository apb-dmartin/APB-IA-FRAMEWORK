---
id: "third-google-finops-multicloud-v1.0"
name: "FinOps Multi-cloud"
description: "Optimización de costes cloud multi-proveedor (AWS, Azure, GCP) y on-premise híbrido, adaptado del enfoque WAF de optimización de costes de Google Cloud."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
created_date: "2026-06-22"
review_date: "2026-06-22"
autonomy_level: 1
source_repo: "https://github.com/google/skills"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
---

# SKILL_PLAT_FINOPS — FinOps & Cost Optimization

## 1. Propósito y Alcance

Esta skill aplica el pilar de **Optimización de Costos** del framework Well-Architected,
extendido a entornos multi-cloud y on-premise híbrido. Proporciona un enfoque estructurado
para optimizar costos de cargas de trabajo cloud maximizando el valor de negocio.

**Diferencia clave vs. on-premise:** Los costos cloud (OpEx) difieren significativamente
del modelo CapEx tradicional, requiriendo un cambio hacia la gestión de gasto operacional
y una cultura de responsabilidad (FinOps).

## 2. Principios Core FinOps (adaptados APB)

1. **Alinear gasto cloud con valor de negocio**: Asegurar que los recursos cloud entreguen
   valor medible de negocio, alineando el gasto IT con objetivos de negocio. Priorizar
   inversiones que contribuyan directamente a ingresos, satisfacción del cliente o eficiencia operacional.

2. **Fomentar cultura de conciencia de costos**: Garantizar que personas en toda la
   organización consideren el impacto de costo de sus decisiones. Proporcionar a los
   equipos visibilidad e información para tomar decisiones informadas y conscientes de costos.

3. **Optimizar uso de recursos**: Provisionar solo los recursos necesarios y pagar solo
   por lo consumido. Seleccionar los tipos, tamaños y ubicaciones de recursos más
   costo-efectivos que cumplan requisitos técnicos y de negocio.

4. **Optimizar continuamente**: Monitorear continuamente el uso de recursos cloud y costos,
   y ajustar proactivamente según sea necesario. Este enfoque iterativo ayuda a identificar
   y abordar ineficiencias antes de que se vuelvan significativas.

5. **Responsabilidad compartida (FinOps Foundation)**: Todos los equipos (Engineering,
   Finance, Product, Business) comparten responsabilidad por el gasto cloud.

6. **Decisions driven by business value**: Cada decisión de optimización debe evaluarse
   contra el valor de negocio, no solo reducción de costos.

## 3. Taxonomía de Costos Cloud

### 3.1 Dimensiones de Análisis
- **Por servicio**: Compute, Storage, Network, Database, Serverless, ML/AI
- **Por entorno**: Development, Testing, Staging, Production, DR
- **Por equipo/proyecto**: Labels/tags obligatorios (`env`, `team`, `app`, `cost-center`)
- **Por región**: Costos diferenciados por ubicación geográfica
- **Por temporalidad**: On-demand vs. Committed vs. Spot/Preemptible

### 3.2 Jerarquía de Optimización (orden de impacto)
1. **Arquitectura**: Serverless, microservicios, event-driven (mayor impacto)
2. **Rightsizing**: Ajuste de tipo/tamaño de instancia basado en métricas reales
3. **Reservas/Compromisos**: CUDs (GCP), Reserved Instances (AWS), Savings Plans (AWS/Azure)
4. **Spot/Preemptible**: Instancias interrumpibles para cargas tolerantes a fallos
5. **Autoscaling**: Escalado automático basado en demanda real
6. **Storage tiers**: Políticas de lifecycle para mover datos a tiers más baratos
7. **Network**: Optimización de transferencias, CDN, inter-region

## 4. Preguntas de Evaluación de Carga de Trabajo

Seleccionar y adaptar preguntas según el contexto del proyecto:

- ¿Cómo incorporan consideraciones de costo en el proceso de diseño de arquitectura cloud?
- ¿Cómo fomentan una cultura de conciencia de costos entre los equipos de desarrollo?
- ¿Cómo monitorean y gestionan costos cloud entre diferentes proyectos o departamentos?
- ¿Qué estrategias usan para optimizar el costo de recursos compute (CPU, RAM, GPU)?
- ¿Cómo balancean optimización de costos con la necesidad de agilidad e innovación?
- ¿Cómo aseguran que no están sobre-provisionando recursos cloud?
- ¿Cómo usan datos y analytics para impulsar decisiones de optimización de costos?
- ¿Cómo optimizan costos en diferentes entornos (dev, test, staging, prod)?
- ¿Cómo aseguran que los esfuerzos de optimización son sostenibles y continuos?
- ¿Cómo miden el éxito de las iniciativas de optimización de costos cloud?
- ¿Qué porcentaje de su gasto compute está cubierto por descuentos por compromiso?
- ¿Utilizan instancias Spot/Preemptible para cargas de trabajo no críticas?
- ¿Tienen políticas de apagado automático para entornos de desarrollo/test fuera de horario?

## 5. Checklist de Validación FinOps

### 5.1 Atribución y Visibilidad
- [ ] **100% de recursos etiquetados**: Todos los recursos tienen metadata clave (`env`, `team`, `app`, `cost-center`, `owner`).
- [ ] **Visibilidad granular**: Exportación de billing a data warehouse (BigQuery, Athena, Cost Management) habilitada y usada para revisiones regulares.
- [ ] **Dashboards compartidos**: Dashboards de costos accesibles a equipos de ingeniería, no solo finanzas.
- [ ] **Budgets y Alertas**: Cada proyecto o unidad de negocio tiene budgets definidos y alertas activas (umbral 50%, 80%, 100%).
- [ ] **Anomaly detection**: Detección automática de anomalías de gasto habilitada.

### 5.2 Optimización de Recursos Compute
- [ ] **Rightsizing**: Recursos ajustados regularmente basados en recomendaciones de rightsizing (Recommender, Compute Optimizer, Advisor).
- [ ] **Estrategia de compromisos**: Gasto revisado mensualmente para optimizar cobertura de CUDs/RIs/Savings Plans.
- [ ] **Spot/Preemptible**: Uso de instancias interrumpibles para cargas tolerantes a fallos (batch, CI/CD, ML training).
- [ ] **Managed services**: Opciones serverless preferidas para nuevas cargas (Cloud Run, Lambda, Azure Functions) a menos que existan restricciones técnicas específicas.
- [ ] **Autoscaling**: Políticas de autoscaling configuradas basadas en métricas reales (CPU, memoria, colas, latencia).

### 5.3 Optimización de Storage
- [ ] **Lifecycle policies**: Políticas de lifecycle activas para buckets/containers principales, moviendo datos a tiers más baratos (Nearline, Coldline, Archive / S3 IA, Glacier / Cool, Archive).
- [ ] **Eliminación de datos obsoletos**: Proceso definido para eliminar datos innecesarios o duplicados.
- [ ] **Compresión**: Uso de compresión habilitado donde sea aplicable.

### 5.4 Gestión de Recursos Idle
- [ ] **Recursos idle identificados**: Discos no utilizados, IPs no asignadas, VMs idle identificados y removidos mensualmente.
- [ ] **Snapshots obsoletos**: Política de retención de snapshots definida y aplicada.
- [ ] **Load balancers huérfanos**: LB sin backends identificados y eliminados.

### 5.5 Network
- [ ] **Transferencias inter-region**: Minimizadas; datos procesados en la misma región cuando sea posible.
- [ ] **CDN**: Uso de CDN para contenido estático y cacheable.
- [ ] **NAT Gateway optimization**: Uso de NAT Gateway compartido o VPC endpoints donde aplique.

## 6. Productos y Herramientas Relevantes (Multi-cloud)

### Visibilidad y Monitoreo
- **GCP**: Cloud Billing reports, BigQuery billing export, Recommender, Active Assist, FinOps Hub
- **AWS**: Cost Explorer, AWS Budgets, Cost Anomaly Detection, AWS Compute Optimizer, Savings Plans
- **Azure**: Cost Management + Billing, Azure Advisor, Azure Reservations, Budgets
- **Multi-cloud**: CloudHealth, CloudCheckr, Finout, Kubecost (Kubernetes), Vantage

### Automatización y Optimización
- **Rightsizing**: Recommender (GCP), Compute Optimizer (AWS), Advisor (Azure)
- **Autoscaling**: Managed Instance Groups (GCP), ASG (AWS), VMSS (Azure)
- **Serverless**: Cloud Run, Cloud Functions (GCP); Lambda, Fargate (AWS); Functions, Container Instances (Azure)
- **Spot**: Preemptible VMs (GCP), Spot Instances (AWS), Spot VMs (Azure)

## 7. Workflow de Evaluación FinOps (APB)

```
1. DESCUBRIMIENTO
   └── Recopilar datos de billing (últimos 3-6 meses)
   └── Identificar top 10 servicios por gasto
   └── Mapear recursos sin etiquetar
   └── Entrevistar stakeholders (Engineering, Finance, Product)

2. ANÁLISIS
   └── Calcular métricas FinOps: % de cobertura de compromisos, % de spot usage,
       costo por transacción, costo por usuario, waste percentage
   └── Identificar oportunidades de optimización por jerarquía de impacto
   └── Benchmark contra industria/indicadores similares

3. RECOMENDACIÓN
   └── Generar plan de optimización con ROI estimado por iniciativa
   └── Priorizar por impacto/eforto (Quick wins primero)
   └── Definir KPIs y métricas de éxito

4. IMPLEMENTACIÓN
   └── Ejecutar cambios con validación de no-impacto en performance
   └── Automatizar donde sea posible (políticas de lifecycle, autoscaling, shutdown schedules)
   └── Documentar decisiones de trade-off (costo vs. performance vs. disponibilidad)

5. MONITOREO CONTINUO
   └── Revisión semanal de dashboards de costos
   └── Revisión mensual de rightsizing y compromisos
   └── Revisión trimestral de arquitectura y estrategia FinOps
   └── Ajustar budgets y alertas según evolución del negocio
```

## 8. Métricas Clave (KPIs)

| Métrica | Descripción | Target |
|---------|-------------|--------|
| Tagging Coverage | % de recursos con etiquetado completo | > 95% |
| Commitment Coverage | % de gasto compute cubierto por descuentos | > 70% |
| Spot Usage | % de carga compute en instancias spot | > 20% (cargas elegibles) |
| Waste Percentage | % de gasto en recursos idle/sobre-provisionados | < 10% |
| Cost per Transaction | Costo infraestructura por transacción de negocio | Tendencia decreciente |
| Budget Variance | Desviación vs. budget mensual | < 5% |
| MTTD Anomaly | Tiempo medio para detectar anomalías de costo | < 24 horas |

## 9. Integración con otras Skills APB

- **SKILL_ARCH_CLOUD_INFRA**: Diseño de arquitectura cloud costo-eficiente
- **SKILL_OPS_OBSERVABILITY**: Dashboards de costos en herramientas de observabilidad
- **SKILL_GOV_EVIDENCES**: Evidencia de controles de costo para auditorías
- **SKILL_DEV_CODE_BASE**: Optimización de código para reducir consumo de recursos

## 10. Anti-patrones FinOps (Qué NO hacer)

- **Optimización prematura**: Optimizar costos antes de alcanzar product-market fit
- **Sobre-optimización**: Reducir costos a expensas de disponibilidad o performance crítica
- **Silos de costos**: Delegar responsabilidad de costos solo al equipo de finanzas
- **Análisis sin acción**: Generar reportes de costos sin plan de acción ejecutable
- **Ignoring shared costs**: No distribuir costos compartidos (VPC, networking, logging) a equipos
- **Manual-only optimization**: Depender solo de optimización manual sin automatización

## 11. Referencias y Recursos

- [Google Cloud Well-Architected: Cost Optimization](https://cloud.google.com/architecture/framework/cost-optimization)
- [AWS Well-Architected: Cost Optimization Pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html)
- [Azure Well-Architected: Cost Optimization](https://learn.microsoft.com/en-us/azure/well-architected/cost-optimization/)
- [FinOps Foundation Framework](https://www.finops.org/framework/)
- [Google Cloud Cost Optimization Best Practices](https://cloud.google.com/architecture/framework/cost-optimization)
- [AWS Cost Optimization Hub](https://aws.amazon.com/aws-cost-management/)
- [Azure Cost Management Best Practices](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/cost-mgt-best-practices)
