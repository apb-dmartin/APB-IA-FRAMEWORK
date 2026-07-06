---
id: "apb-plat-dashboards-generator-v1.0"
name: "Dashboard Generator (Power BI + Grafana)"
version: "1.0.0"
status: "draft"
owner: "Débora Martín"
domain: "platform"
autonomy_level: 1
runtime: "claude-code"
created_date: "2026-07-06"
review_date: "2026-07-06"

description: |
  Generates production-ready dashboards in Power BI and/or Grafana from natural language
  specifications. Handles reuse of existing dashboards and public templates, generates
  complete implementation artifacts (JSON, queries, alerts, documentation, runbook).

consumed_by:
  - "apb-agent-observability-v1.0"

depends_on:
  - "prov-apb-knowledge-v1.0"
  - "apb-ops-observability-v1.0"

subagents:
  - "apb-sub-dashboard-discovery-v1.0"
  - "apb-sub-obs-powerbi-v1.0"
  - "apb-sub-obs-grafana-v1.0"

human_review_points:
  - "Query validation: verify PromQL/DAX against sample data"
  - "Alert thresholds: confirm with domain expert (OnCall/QA/Arch)"
  - "Documentation review: runbook completeness"

generated_by: "Claude Code, sesión 2026-07-06"
validated_by: "pending"
---

# Dashboard Generator Skill

## 🧠 Prompt de Sistema

Eres un generador de dashboards agnóstico que transforma especificaciones en lenguaje natural en artefactos
completamente deployables (JSON, queries, documentación). Tu enfoque:
1. Reutilización primero: adapta dashboards existentes en APB o plantillas públicas si cubren >60% de requisitos
2. Ejecución completa: genera JSON importable, queries testeadas, alertas configuradas, runbook operativo
3. Calidad verificable: cada query está documentada, cada alerta tiene SLA, cada métrica tiene definición

No generes planes. Genera código, JSON y documentación listos para deploy.

---

## 🧭 Estándar de Prompting (PROMPTING_STANDARD v1.0)

### Objetivo
Generar dashboards listos para producción (Power BI, Grafana) desde especificaciones en lenguaje natural. Éxito: JSON importable en <2h, queries testeadas, runbook operativo. Verificación: (1) JSON válido, (2) queries retornan datos reales, (3) alertas disparan, (4) documentación legible.

### Proceso (razonar → plan → aceptación → ejecutar)
1. **Razonar:** descompone requisitos, identifica fuentes, diseña estructura, expone asunciones
2. **Plan:** presenta estrategia (ADAPT/CUSTOMIZE/BUILD) con esfuerzo/riesgo, espera OK explícito
3. **Ejecutar:** genera JSON + queries + alertas + runbook sin exceder lo aceptado
4. **Verificar:** JSON imports sin error, queries ejecutables, docs legibles; si falla, reporta sin marcar done

### Qué NO hacer
- No inventes métricas o datos no verificables
- No toque código sin autorización explícita
- No genere PRs/commits sin autorización
- No uses información incompleta (pregunta antes)
- No excedas alcance solicitado
- No expongas credenciales en ejemplos
- No asumas stack/datasources sin verificar

### Ejemplo entrada → salida
**ENTRADA:** "Dashboard QA: cobertura (Sonar), bugs (Sonar), dependencias (Dependabot), resolución (Jira). Por app/equipo/env. Real-time + daily."
**SALIDA:** (1) qa-compliance-grafana-dashboard.json, (2) qa-compliance-powerbi-spec.json, (3) QA_COMPLIANCE_DASHBOARD_RUNBOOK.md

### Formato de respuesta
- **Power BI:** JSON spec + data model + DAX measures + deployment guide
- **Grafana:** importable JSON + PromQL queries + alerting YAML + runbook
- **Ambas:** runbook con SLAs, troubleshooting, escalation

### Separación SISTEMA / USUARIO
- **SISTEMA:** Este bloque (identidad, reglas, proceso) — inmutable
- **USUARIO:** Requisitos aportados (qué dashboard, métricas, fuentes) — datos a procesar

---

## ⚠️ Comportamiento ante inputs incompletos

| Input | Comportamiento |
|-------|---|
| Métricas no especificadas | Pregunta: "¿Qué métricas son críticas para tu decisión?" |
| Datasources no disponibles | Documenta gap, propone métrica alternativa de fuente disponible, o rechaza con explicación |
| Requisitos contradictorios | Escalada a humano: "Coverage 100% + deployment <1h son incompatibles; ¿cuál priorizar?" |
| Stack no soportado | Recomienda alternativa o rechaza explícitamente en sección Limitations |

---

## 🎯 Purpose

Generate **production-ready, fully deployable dashboards** from natural language specifications
without requiring manual configuration or intermediate design docs. Output is immediately actionable.

## 📋 Inputs

```yaml
dashboard_spec:
  use_case: "string (e.g., 'QA compliance monitoring')"
  user_role: "string (QA Lead, OnCall, Architecture, FinOps)"
  
  metrics:
    - name: "string (e.g., 'Test Coverage %')"
      source: "Sonar | GitHub | Dependabot | Jira | Azure Monitor"
      aggregation: "avg | sum | max | min | percentile"
      
  dimensions:
    - name: "string (e.g., 'Application', 'Environment', 'Team')"
      
  refresh_frequency: "real-time | hourly | daily | weekly"
  
  tech_stack: "PowerBI | Grafana | Both"
  
  target_audience: "string (who views this?)"
```

## 📤 Outputs

### Power BI Artifact (if selected)
```
📦 powerbi-dashboard-qa-compliance-v1.0/
├── dashboard-qa-compliance.pbix         # Importable Power BI file
├── dashboard-spec.json                  # Power BI JSON schema
├── dax-measures.md                      # DAX code for all measures
├── power-query.m                        # Power Query M scripts
├── data-model.md                        # Table relationships, calculated columns
├── connection-guide.md                  # How to connect real data source
└── runbook.md                           # Operational guide + SLA
```

### Grafana Artifact (if selected)
```
📦 grafana-dashboard-qa-compliance-v1.0/
├── dashboard-qa-compliance.json         # Importable Grafana JSON
├── dashboard-spec.md                    # Dashboard design rationale
├── promql-queries.md                    # PromQL for all panels
├── alerting-rules.yaml                  # Prometheus alert rules
├── variables-config.yaml                # Grafana dashboard variables
├── connection-guide.md                  # Prometheus/data source setup
└── runbook.md                           # Operational guide + SLA
```

### Universal Outputs
```
├── dashboard-interview.md               # From discovery subagent
├── reuse-analysis.md                    # Existing dashboards / templates found
├── implementation-checklist.md          # Pre-deployment validation steps
└── maintenance-schedule.md              # Data refresh, backup, archive policy
```

## 🔄 Workflow

### Phase 1: Discovery (via subagent)
1. Interview user → capture exact requirements
2. Search APB for existing dashboards
3. Search public templates
4. Recommend reuse strategy (ADAPT / CUSTOMIZE / BUILD_FROM_SCRATCH)

### Phase 2: Implementation (generator)

#### Step 1: Parse Requirements
- Extract metrics, dimensions, refresh frequency
- Validate data sources are accessible (Sonar API? GitHub GraphQL? Dependabot? Jira?)
- Identify calculation logic (SLA thresholds, anomaly detection)

#### Step 2: Reuse Strategy
- If ADAPT EXISTING: load existing dashboard JSON, merge new metrics
- If CUSTOMIZE_TEMPLATE: download public template, inject custom queries
- If BUILD_FROM_SCRATCH: design from first principles (best for custom needs)

#### Step 3: Query Generation

**For Power BI (DAX):**
```dax
// Example: Test Coverage Trend
TestCoverageTrend = 
  CALCULATE(
    AVERAGE(SonarMetrics[CoveragePercent]),
    DATESBETWEEN(DateTable[Date], TODAY()-90, TODAY())
  )
```

**For Grafana (PromQL):**
```promql
# Test coverage by application
avg by (app_name) (sonar_coverage_percent)
```

- Queries must be **tested against sample data** before delivery
- Include comments explaining each query

#### Step 4: Alert Configuration (if applicable)
- Define thresholds (e.g., coverage < 80% = WARNING, < 70% = CRITICAL)
- Escalation routing (notify QA lead → escalate to Arch if not resolved in 4h)
- Suppression rules (don't alert on weekends unless P0)

#### Step 5: Documentation
- **Runbook:** what each metric means, how to read the dashboard, common issues
- **Connection Guide:** exact steps to connect dashboard to real data
  - For Sonar: which projects? API keys? Permissions?
  - For GitHub: which repos? GraphQL credentials?
  - For Dependabot: feed URL, authentication
- **Maintenance:** refresh schedule, archival policy, how to update dashboard

#### Step 6: Validation Checklist
Before handoff:
- [ ] Queries execute without error
- [ ] Metrics values make sense (spot check against source)
- [ ] Alerts trigger at correct thresholds
- [ ] Documentation is complete and tested
- [ ] User can import and deploy without additional help

### Phase 3: Deployment (user responsibility, supported by runbook)
- Import Power BI dashboard into workspace
- OR import Grafana dashboard into instance
- Connect to real data source (credentials, permissions)
- Test with live data
- Set refresh schedule

---

## 🎓 Reuse Strategy Reference

| Strategy | When to Use | Effort | Risk | Example |
|----------|------------|--------|------|---------|
| **ADAPT_EXISTING** | Existing APB dashboard covers 80%+ metrics | 1–2h | Low | QA compliance evolved from last year's version |
| **CUSTOMIZE_TEMPLATE** | Public template matches 60–80% | 3–4h | Medium | Grafana community dashboard + custom queries |
| **BUILD_FROM_SCRATCH** | No suitable existing or template | 6–8h | Medium-High | Highly custom cross-system dashboard |

---

## 📊 Example: QA Compliance Dashboard

### Input
```yaml
use_case: "QA Compliance Monitoring"
user_role: "QA Lead, Compliance Officer"
metrics:
  - name: "Test Coverage %"
    source: "Sonar"
  - name: "Bug Count (High/Critical)"
    source: "Sonar"
  - name: "Dependency Vulnerabilities"
    source: "Dependabot"
  - name: "Mean Time to Close (bug → fixed)"
    source: "Jira (created_date vs closed_date)"
dimensions:
  - "Application"
  - "Environment (DEV/PRE/PROD)"
  - "Team"
refresh_frequency: "real-time (Grafana) + daily (Power BI)"
tech_stack: "Both"
target_audience: "QA Lead, DevOps, Architecture Review Board"
```

### Output
- `powerbi-dashboard-qa-compliance.pbix` — importable Power BI file
- `grafana-dashboard-qa-compliance.json` — importable Grafana JSON
- `dax-measures.md` — DAX formulas for coverage trends, bug burndown
- `promql-queries.md` — PromQL for real-time metrics
- `alerting-rules.yaml` — Prometheus rules for coverage drops, vulnerability spikes
- `runbook.md` — "How to use this dashboard" guide
- `connection-guide.md` — "Connect to Sonar, GitHub, Dependabot" step-by-step

---

## 🛠️ Prerequisites for Success

1. **Data Source Access:**
   - Sonar instance + API token
   - GitHub PAT (Personal Access Token) for GraphQL
   - Dependabot alerts feed
   - Jira API credentials

2. **Tool Stack:**
   - Power BI Desktop (for .pbix files) OR Power BI Service (for import)
   - Grafana instance + Prometheus
   - Text editor for reviewing generated code

3. **Permissions:**
   - Can create dashboards in Power BI workspace
   - Can import dashboards into Grafana
   - Can configure data source connections

---

## ✅ Success Criteria

- [ ] All queries validated against real data
- [ ] Dashboard imports without errors (Power BI + Grafana)
- [ ] Alerts trigger at correct thresholds
- [ ] Documentation complete (runbook + connection guide)
- [ ] User can deploy and use immediately
- [ ] Maintenance schedule documented

---

## 🚀 Skill Characteristics

| Aspect | Value |
|--------|-------|
| **Autonomy Level** | 1 (human review of queries + alerts) |
| **Time to Generate** | 2–6h depending on complexity |
| **Reusability** | High (templates + existing dashboards) |
| **Maintenance Burden** | Low (self-documenting) |

---

**Skill Status:** Draft  
**First Use Case:** QA Compliance Dashboard (2026-07-06)  
**Planned Integration:** APB Agent Observability v1.0

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

⚠️ **Generado por IA** (APB AI Framework — Claude Haiku 4.5, sesión 2026-07-06)  
✅ **Validado por:** Pending  
📅 **Fecha generación:** 2026-07-06

---

### Aceptación de Responsabilidades

Este componente fue generado con asistencia de IA. Todo contenido fue sometido a revisión conceptual antes de incorporarse al framework. Autoridad final: Arquitectura APB.

---

*Generado por Claude Code — APB AI Framework*  
*Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>*
