# APB AI Framework — Índice Maestro

> **ID:** `apb-index-v1.0`
> **Versión:** 1.0.0
> **Estado:** draft
> **Fecha de actualización:** 2026-06-29
> **Framework:** APB AI v1.0.0-draft

---

## 🎯 Propósito

Índice maestro del APB AI Framework. Registro vivo de todos los componentes, su estado y ubicación.

---

## 📊 Resumen Ejecutivo

| Métrica | Valor |
|---------|-------|
| Skills APB | 175 / 175 |
| Skills terceros | 51 / 51 |
| Agentes | 35 / 35 |
| Subagentes | 33 / 33 |
| Workflows | 17 / 17 |
| Providers | 19 / 19 |
| Wrappers | 7 / 7 |
| Adaptadores | 4 / 4 |
| **Total** | **341** |

---

> ℹ️ La tabla anterior se regenera automáticamente (`scripts/generate_catalog.py`)
> y cubre únicamente componentes con frontmatter YAML (los 8 tipos de
> `SCHEMA.md`). El siguiente inventario adicional es de mantenimiento manual:

| Elemento | Valor |
|---|---|
| Documentos base (README, SYSTEM, GOVERNANCE, CONTRIBUTING, LICENSE) | 5 / 5 |
| Templates (`context/apb/templates/`) | 7 / 7 |
| Scripts (`scripts/`) | 3 / 3 |
| Contexto APB (`context/apb/`) | 3 standards + `SCHEMA.md` + 8 carpetas de políticas |
| Scaffolds (`repo-scaffold/`) | 2 / 2 |
| Ejemplos (`examples/`) | 2 / 2 |

---

## 📁 Estructura del Repositorio

```
APB-IA-FRAMEWORK/
├── README.md, SYSTEM.md, GOVERNANCE.md, CONTRIBUTING.md, LICENSE.md
├── INDEX.md
├── DOMAIN_REGISTRY.md
├── agents/                     # 35 agentes
├── subagents/                  # 33 subagentes
├── workflows/                  # 17 workflows
├── skills/
│   ├── apb-owned/             # 175 skills
│   └── third-party/           # 51 skills
├── providers/                  # 19 providers
├── wrappers/                   # 7 wrappers
├── adapters/                   # 4 adaptadores
│   ├── copilot/
│   └── claude/
├── catalog/CATALOG.md
├── context/apb/
│   ├── standards/             # 3 estándares
│   ├── templates/             # 7 plantillas
│   └── policies/              # 24 documentos oficiales APB (8 dominios)
│       ├── security/          # 5 políticas + 6 guías
│       ├── ai/                # 1 política
│       ├── quality/           # 1 política + 1 procedimiento
│       ├── infrastructure/    # 2 políticas
│       ├── capacity/          # 2 guías
│       ├── procurement/       # 1 política
│       ├── compliance/        # 1 procedimiento
│       └── docks/             # 1 guía + 1 licitación
├── scripts/
│   ├── validate_repo.py
│   └── invoke_agent.py
├── examples/
│   ├── dotnet-review/
│   └── spec-generation/
├── repo-scaffold/
│   ├── sdd-ready/
│   └── legacy-ready/
└── discovery/
```

---

## ✅ Skills APB por Dominio (175)

| Dominio | Cantidad | Patrón ID |
|---------|----------|-----------|
| development | 27 | `apb-dev-*` |
| governance | 20 | `apb-gov-*` |
| operation | 19 | `apb-ops-*` |
| platform | 19 | `apb-plat-*` |
| qa | 17 | `apb-qa-*` |
| architecture | 16 | `apb-arch-*` |
| discovery | 16 | `apb-disc-*` |
| security | 12 | `apb-sec-*` |
| documentation | 11 | `apb-doc-*` |
| pm | 11 | `apb-pm-*` |
| design | 4 | `apb-design-*` |
| orchestration | 3 | `apb-orch-*` |

---

## ✅ Agentes (35)

`apb-agent-accessibility-auditor`, `apb-agent-api-product-manager`, `apb-agent-business-analyst`, `apb-agent-catalog-manager`, `apb-agent-change-manager`, `apb-agent-cloud-architect`, `apb-agent-code-reviewer`, `apb-agent-compliance-audit`, `apb-agent-data-governance`, `apb-agent-db`, `apb-agent-ddd`, `apb-agent-documentation`, `apb-agent-domain-architect`, `apb-agent-finops`, `apb-agent-governance`, `apb-agent-implementer`, `apb-agent-incident-support`, `apb-agent-knowledge-manager`, `apb-agent-meta-builder`, `apb-agent-modernization`, `apb-agent-observability`, `apb-agent-platform-engineer`, `apb-agent-pm`, `apb-agent-problem-manager`, `apb-agent-qa-auto`, `apb-agent-release-manager`, `apb-agent-risk-exception`, `apb-agent-security-architect`, `apb-agent-spec-engineer`, `apb-agent-sre`, `apb-agent-tech-debt`, `apb-agent-tech-discovery`, `apb-agent-technical-architect`, `apb-agent-ux-mockup`, `apb-agent-vendor-manager`

---

## ✅ Workflows (17)

`apb-wf-accessibility-audit-v1.0`, `apb-wf-api-lifecycle-v1.0`, `apb-wf-change-management-v1.0`, `apb-wf-cloud-migration-v1.0`, `apb-wf-code-review-v1.0`, `apb-wf-data-governance-v1.0`, `apb-wf-finops-review-v1.0`, `apb-wf-incident-l1-v1.0`, `apb-wf-incident-l2-v1.0`, `apb-wf-legacy-onboarding-v1.0`, `apb-wf-problem-management-v1.0`, `apb-wf-qa-evidence-v1.0`, `apb-wf-risk-exception-v1.0`, `apb-wf-sdd-full-v1.0`, `apb-wf-security-patch-v1.0`, `apb-wf-spec-from-legacy-v1.0`, `apb-wf-vendor-procurement-v1.0`

---

## 🏷️ Convenciones de Nomenclatura

- **Skills APB:** `apb-{dominio}-{nombre}-v{major}.{minor}`
- **Skills Terceros:** `third-{ecosistema}-{nombre}-v{major}.{minor}`
- **Agentes:** `apb-agent-{nombre}-v{major}.{minor}`
- **Subagentes:** `apb-sub-{especialidad}-v{major}.{minor}`
- **Workflows:** `apb-wf-{nombre}-v{major}.{minor}`
- **Providers:** `prov-{nombre}-v{major}.{minor}`
- **Wrappers:** `wrap-{nombre}-v{major}.{minor}`

---

## 🔄 Historial de Cambios

| Versión | Fecha | Cambio |
|---------|-------|--------|
| 1.0.0 | 2026-06-21 | Consolidación de INDEX_v5 → INDEX.md definitivo |
| 1.1.0 | 2026-06-23 | Regenerado automáticamente por `scripts/generate_catalog.py` (Sesión 3) tras incorporación de dominios qa/platform/security/operation/pm y normalización completa de nomenclatura |

---
*Documento generado por el APB AI Framework. Requiere revisión humana antes de aprobación.*
