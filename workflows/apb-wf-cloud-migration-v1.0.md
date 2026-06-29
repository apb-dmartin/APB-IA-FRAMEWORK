---
id: "apb-wf-cloud-migration-v1.0"
name: "Cloud Migration"
description: "Migrar una aplicación legacy a cloud con validación completa de infraestructura, seguridad, operabilidad y costes."
version: "1.0.0"
status: "draft"
owner: "Arquitectura Cloud APB <arquitectura@portdebarcelona.cat>"
domain: "orchestration"
autonomy_level: 1
agents:
  - "apb-agent-cloud-architect-v1.0"
  - "apb-agent-technical-architect-v1.0"
  - "apb-agent-security-architect-v1.0"
  - "apb-agent-platform-engineer-v1.0"
  - "apb-agent-qa-auto-v1.0"
  - "apb-agent-sre-v1.0"
  - "apb-agent-finops-v1.0"
  - "apb-agent-governance-v1.0"
  - "apb-agent-release-manager-v1.0"
human_checkpoints:
  - "Validación humana antes de cada fase crítica del workflow"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Cloud Migration

---

## 🎯 Objetivo

Migrar una aplicación legacy a cloud con validación completa de infraestructura, seguridad, operabilidad y costes.

## 📊 Diagrama de Flujo

```mermaid
graph TD
    A[Aplicación Legacy] --> B[Cloud Architect Agent]
    B --> C[Technical Architect]
    C --> D[Security Architect Agent]
    D --> E[Platform Engineer Agent]
    E --> F[QA Automation Agent]
    F --> G[SRE Agent]
    G --> H[FinOps Agent]
    H --> I[Governance Agent]
    I --> J[Release Manager Agent]
```

## 🎭 Agentes Participantes

| Orden | Agente | Rol | Skills Utilizadas |
|-------|--------|-----|-------------------|
| 1 | Cloud Architect Agent | Diseño cloud y readiness | `apb-plat-cloud-ready`, `apb-plat-terraform`, `apb-plat-finops` |
| 2 | Technical Architect | Arquitectura de migración | `apb-arch-decompose`, `apb-arch-cloud-infra` |
| 3 | Security Architect Agent | Seguridad cloud | `apb-sec-threat-model`, `apb-sec-ens`, `apb-arch-security-design` |
| 4 | Platform Engineer Agent | Infraestructura y CI/CD | `apb-plat-docker`, `apb-plat-cicd`, `apb-plat-db-migration` |
| 5 | QA Automation Agent | Validación post-migración | `apb-qa-post-migration`, `apb-qa-test-plan` |
| 6 | SRE Agent | Operabilidad y observabilidad | `apb-ops-operability`, `apb-ops-observability`, `apb-ops-prr` |
| 7 | FinOps Agent | Optimización de costes | `apb-plat-finops` |
| 8 | Governance Agent | Validación de gobierno | `apb-gov-compliance` |
| 9 | Release Manager Agent | Coordinación de release | `apb-qa-release-ready` |

## 📋 Fases del Workflow

### Fase 1: Evaluación de Readiness
- Análisis de preparación para cloud
- Identificación de dependencias y bloqueadores
- Gap analysis

### Fase 2: Diseño de Arquitectura Cloud
- Diseño de infraestructura cloud-native
- Definición de estrategia de migración (lift-and-shift, re-platform, re-architect)
- Diseño de networking y seguridad cloud

### Fase 3: Seguridad Cloud
- Threat modeling para entorno cloud
- Validación ENS en configuración cloud
- Diseño de IAM y network segmentation

### Fase 4: Infraestructura y CI/CD
- Generación de templates Terraform
- Dockerización de aplicaciones
- Configuración de pipelines CI/CD cloud
- Migración de base de datos

### Fase 5: Validación QA
- Tests de validación post-migración
- Comparación de resultados legacy vs cloud
- Tests de rendimiento y carga

### Fase 6: Operabilidad
- Diseño de observabilidad (métricas, logs, traces)
- Configuración de alertas y runbooks
- Production Readiness Review

### Fase 7: FinOps
- Estimación de costes cloud
- Configuración de budgets y alertas
- Recomendaciones de optimización

### Fase 8: Gobierno y Release
- Validación de cumplimiento
- Decisión de go/no-go para migración

## 📥 Input Inicial

- Aplicación legacy a migrar
- Base de datos legacy
- Requisitos de disponibilidad y rendimiento
- Presupuesto para cloud
- Requisitos de compliance (ENS, etc.)

## 📤 Output Final

- Aplicación migrada y operativa en cloud
- Infraestructura como código (Terraform)
- Pipelines CI/CD configurados
- Observabilidad configurada
- Informe de validación post-migración
- Análisis FinOps con budgets
- Documentación de migración y ADRs

## 🔄 Puntos de Decisión

- **DP1:** ¿La evaluación de readiness es favorable? Si no, requiere remediación.
- **DP2:** ¿El diseño cloud pasa threat modeling? Si no, iterar con Security Architect.
- **DP3:** ¿La migración de datos es exitosa? Validar con QA.
- **DP4:** ¿Los costes estimados están dentro del presupuesto? Si no, optimizar.
- **DP5:** ¿Pasa PRR de SRE? Si no, corregir findings.
- **DP6:** ¿Decisión de go/no-go? Requiere aprobación humana.

## 📡 Contratos de Output Inter-Agente

Cada agente produce un output estructurado que el siguiente agente consume como input. Los handoffs críticos de la cadena de 9 agentes son:

| Handoff | De | A | Artefacto de entrega | Campos obligatorios |
|---------|----|----|---------------------|---------------------|
| H1 | Cloud Architect | Technical Architect | `cloud-readiness-report.md` | `readiness_score`, `blockers[]`, `migration_strategy` (lift-and-shift/re-platform/re-architect), `target_azure_services[]` |
| H2 | Technical Architect | Security Architect | `architecture-design.md` | `components[]`, `data_flows[]`, `external_integrations[]`, `network_topology` |
| H3 | Security Architect | Platform Engineer | `security-requirements.md` | `threat_model_ref`, `ens_level` (Básico/Medio/Alto), `iam_requirements[]`, `network_segmentation_rules[]`, `approved_for_infra: bool` |
| H4 | Platform Engineer | QA Automation | `infrastructure-ready.md` | `terraform_modules[]`, `ci_cd_pipeline_url`, `db_migration_status` (success/partial/failed), `environments_available[]` |
| H5 | QA Automation | SRE | `qa-validation-report.md` | `test_results_summary`, `performance_baseline`, `blocking_issues[]`, `approved_for_sre: bool` |
| H6 | SRE | FinOps | `operability-report.md` | `observability_setup`, `slo_definitions[]`, `prr_status` (pass/fail), `monthly_log_volume_gb` |
| H7 | FinOps | Governance | `cost-estimate.md` | `monthly_cost_estimate_eur`, `budget_compliance: bool`, `cost_optimizations[]`, `approved_for_governance: bool` |
| H8 | Governance | Release Manager | `governance-validation.md` | `compliance_status` (PASS/FAIL), `open_findings[]`, `go_no_go_recommendation` |

> **Regla de bloqueo:** Si cualquier campo `approved_for_*: bool` viene en `false`, el workflow detiene la progresión al agente siguiente y espera gate de validación humana. No se puede avanzar a la fase siguiente con un handoff en estado `FAIL`.

## 🚫 Límites y Escapes

- NO puede ejecutar migración en producción sin aprobación
- NO puede ignorar findings de seguridad críticos
- La migración debe incluir plan de rollback
- Requiere validación humana para decisiones críticas

## 🔒 Seguridad y Cumplimiento

- Threat modeling específico para cloud
- Validación ENS en configuración cloud
- Uso de Azure Key Vault para secretos
- Network segmentation y private endpoints
- Auditoría de cambios en infraestructura

## 📝 Ejemplo de Ejecución

```yaml
workflow: apb-wf-cloud-migration-v1.0
inputs:
  workflow: "apb-wf-cloud-migration-v1.0"
  inputs:
    legacy_app:
      repo: "/repos/legacy-system"
      database: "ref:akv/legacy-db-conn"
    cloud_provider: "Azure"
    migration_strategy: "re-platform"
    target_services:
      - "Azure App Service"
      - "Azure SQL"
      - "Azure Service Bus"
    budget_eur: 10000
    availability_target: "99.9%"
    compliance:
      - "ENS"
    output_format: "cloud-migration-package"
```

## 🔄 Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-21 | Arquitectura APB | Creación inicial |

---
*Documento generado por el APB AI Framework. Requiere revisión humana antes de aprobación.*
