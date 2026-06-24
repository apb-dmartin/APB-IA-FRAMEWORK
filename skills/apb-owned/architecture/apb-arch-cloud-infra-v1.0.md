---
id: "apb-arch-cloud-infra-v1.0"
name: "Diseño de Infraestructura Cloud"
description: "Diseñar infraestructuras cloud en Azure que sean escalables, seguras, cost-eficientes y operables. Incluye diseño de redes, compute, storage, bases de datos, identidad y observabilidad."
version: "1.0.0"
status: "draft"
owner: "Arquitectura Cloud <arquitectura@portdebarcelona.cat>"
domain: "architecture"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Diseño de Infraestructura Cloud

---

## 🎯 Propósito

Diseñar infraestructuras cloud en Azure que sean escalables, seguras, cost-eficientes y operables. Incluye diseño de redes, compute, storage, bases de datos, identidad y observabilidad.

---

## ⚡ Trigger

Al desplegar un nuevo sistema en Azure, migrar un sistema on-premise, o rediseñar infraestructura existente por cambios de requisitos (escalabilidad, coste, compliance).

---

## 📥 Input

- Requisitos no funcionales (RNF): disponibilidad, RTO, RPO, throughput, latencia
- Requisitos de seguridad y compliance (ENS, GDPR, etc.)
- Estimación de carga y patrones de tráfico
- Presupuesto aproximado
- Topología de red actual (si aplica)
- Decisiones arquitectónicas previas (estilo, patrones)

---

## 📤 Output

- Diagrama de arquitectura de infraestructura
- Especificación de recursos Azure (tipos, tiers, configuraciones)
- Diseño de red virtual (VNet, subnets, NSGs, peering)
- Estrategia de identidad y acceso (Entra ID, RBAC, Managed Identities)
- Plan de backup y disaster recovery
- Estimación de costes mensual (FinOps preliminar)
- Código Terraform/Bicep de infraestructura (si aplica)

---

## 🔄 Proceso

1. **Análisis de requisitos**: Traducir RNF a características técnicas (ej: 99.99% SLA = multi-region + load balancer + health probes).
2. **Diseño de red**: Definir VNets, subnets (DMZ, app, data), NSGs, Azure Firewall, VPN Gateway/ExpressRoute.
3. **Diseño de compute**: Seleccionar entre App Service, ACI, AKS, Functions, VM (justificar elección).
4. **Diseño de datos**: Seleccionar Azure SQL, PostgreSQL, Cosmos DB, Storage Account, Redis. Definir estrategia de replicación y backup.
5. **Diseño de identidad**: Entra ID, Managed Identities, RBAC, Key Vault para secretos.
6. **Diseño de integración**: API Management, Service Bus, Event Grid.
7. **Observabilidad**: Application Insights, Log Analytics, Azure Monitor, alertas.
8. **Seguridad**: WAF, DDoS Protection, encryption at rest/transit, private endpoints.
9. **Cost estimation**: Calcular coste mensual con Azure Pricing Calculator. Identificar oportunidades de ahorro (reserved instances, spot VMs, auto-scaling).
10. **Documentación**: Generar diagramas y especificaciones.

---

## 📋 Reglas y Constraints

- Todos los recursos deben estar en un resource group con naming convention estándar APB.
- NUNCA exponer bases de datos directamente a internet; usar private endpoints.
- Todos los secretos en Azure Key Vault; NUNCA en variables de entorno planas.
- Habilitar encryption at rest por defecto (CMK para datos sensibles).
- Diseñar para auto-scaling horizontal, no vertical.
- Usar Availability Zones para alta disponibilidad; multi-region solo si el RTO lo justifica.
- Tags obligatorios en todos los recursos: Environment, Owner, Project, CostCenter.
- No usar VM para workloads stateless; preferir PaaS (App Service, AKS, Functions).
- Documentar decisiones de infraestructura en ADRs.

---

## 🛠 Stack Tecnológico Relevante

- Azure (core platform)
- Terraform / Bicep (IaC)
- Azure DevOps / GitHub Actions (pipelines)
- Azure Monitor / Application Insights
- Azure Key Vault
- Azure Service Bus / Event Grid
- Azure API Management
- AKS / App Service / Azure Functions

---

## 💡 Ejemplos de Uso

**Ejemplo 1 — Microservicio de alta disponidad:**
> App Service (Premium v3) en 3 Availability Zones
> Azure SQL (Business Critical, geo-replica)
> Redis (Enterprise, clustering)
> Service Bus Premium
> API Management con VNet integration
> Coste estimado: ~€2.500/mes

**Ejemplo 2 — Sistema batch de procesamiento:**
> Azure Container Instances para jobs efímeros
> Azure Storage (cool tier) para datos de entrada/salida
> Azure Functions (consumption) para orquestación
> Coste estimado: ~€200/mes (variable con uso)

---

## 🔗 Dependencias

- `apb-plat-terraform-v1.0` (generación de código IaC)
- `apb-plat-finops-v1.0` (optimización de costes)
- `apb-ops-observability-v1.0` (diseño de monitorización)
- `apb-sec-ens-v1.0` (cumplimiento seguridad)
- `prov-azure-v1.0

---

## 📝 Notas

- Revisar siempre la Azure Well-Architected Framework como referencia.
- Para workloads críticos, incluir Chaos Engineering en el plan (Azure Chaos Studio).
- Documentar RTO/RPO objetivos y validar con drills periódicos.

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*
