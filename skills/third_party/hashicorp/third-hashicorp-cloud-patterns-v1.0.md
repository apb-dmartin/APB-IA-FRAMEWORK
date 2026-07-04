---
id: "third-hashicorp-cloud-patterns-v1.0"
name: "Cloud Readiness Patterns"
description: "Patrones de preparación cloud y búsqueda/importación de recursos Terraform."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
created_date: "2026-06-22"
review_date: "2026-06-22"
autonomy_level: 1
source_repo: "https://github.com/hashicorp/terraform-search-import"
source_license: "MPL-2.0"
source_commit: "unverified"
verified_date: "2026-06-23"
---

# Cloud Ready Assessment para APB

## ⚠️ Intento de re-identificación de SHA (2026-07-04) — sin resultado

`hashicorp/terraform-search-import` **no existe** como repositorio en GitHub (404 vía API, tanto
en la URL del repo como en su listado de commits). "Terraform Search & Import" es el nombre de
una **funcionalidad de producto** de HCP Terraform (aparece citada en repos de terceros como
ejemplo de uso), no un repositorio publicado. No se ha podido determinar con evidencia qué
repositorio real dio origen a este componente — no se fabrica una URL/SHA de sustitución
(norma "no inventar sin evidencia", `GOVERNANCE.md`). `source_commit` permanece `unverified`.
**Pendiente:** que el autor original o Débora identifiquen el repo/commit real, o se reconsidere
el origen citado del componente.

## Overview
Evaluación de preparación para cloud de aplicaciones legacy, identificando dependencias on-prem, deuda técnica, y generando plan de modernización con priorización de riesgos y esfuerzo.

## When to Use
- Evaluación pre-migración de aplicación legacy
- Planificación de modernización de portfolio
- Due diligence de adquisición de aplicación
- Revisión periódica de estado de aplicaciones

## Core Pattern

### Fase 1: Inventario de Dependencias
| Tipo | Ejemplos | Impacto Cloud |
|------|----------|---------------|
| Hardware específico | Mainframe, AS/400 | Requiere reescritura |
| Licencias vendor-lock | Oracle DB, Windows Server | Coste/licensing |
| Protocolos propietarios | DCOM, Named Pipes | Requiere adaptación |
| File shares | UNC paths, NAS | Azure Files / Blob |
| Active Directory | LDAP, Kerberos | Entra ID |
| Servicios locales | Print servers, fax | Requiere alternativa |

### Fase 2: Evaluación de 12 Factores

| Factor | Estado | Acción |
|--------|--------|--------|
| 1. Codebase | One codebase, one app | Separar si monolito |
| 2. Dependencies | Explicitly declare | Package managers |
| 3. Config | Store in environment | Azure Key Vault, App Config |
| 4. Backing services | Treat as attached | Connection strings |
| 5. Build/release/run | Strict separation | CI/CD pipeline |
| 6. Processes | Stateless, share-nothing | Session externalization |
| 7. Port binding | Self-contained | Containerize |
| 8. Concurrency | Scale via processes | App Service / AKS |
| 9. Disposability | Fast startup, graceful shutdown | Health checks |
| 10. Dev/prod parity | Keep environments similar | IaC, containers |
| 11. Logs | Stream, don't store | Application Insights |
| 12. Admin processes | Run as one-off | Azure Functions, jobs |

### Fase 3: Plan de Modernización

| Prioridad | Estrategia | Esfuerzo | Riesgo |
|-----------|-----------|----------|--------|
| P0 | Rehost (lift-and-shift) | Bajo | Bajo |
| P1 | Refactor (containerize) | Medio | Medio |
| P2 | Replatform (PaaS) | Medio | Medio |
| P3 | Rebuild (cloud-native) | Alto | Alto |
| P4 | Replace (SaaS) | Variable | Variable |

## Adapted From
- **Source:** hashicorp/terraform-search-import (cloud patterns)
- **License:** MIT
- **Attribution:** Patrones de evaluación de preparación cloud y estrategias de migración inspirados en HashiCorp. Reescrito para Azure y contexto APB.

## References
- Microsoft Azure Well-Architected Framework
- 12-Factor App methodology
- context/apb/standards/cloud-standards.md
