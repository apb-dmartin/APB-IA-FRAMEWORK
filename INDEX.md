# APB AI Framework — Índice Maestro

> **ID:** `apb-index-v1.0`
> **Versión:** 1.0.0
> **Estado:** draft
> **Fecha de actualización:** 2026-06-24
> **Framework:** APB AI v1.0.0-draft

---

## 🎯 Propósito

Índice maestro del APB AI Framework. Registro vivo de todos los componentes, su estado y ubicación.

---

## 📊 Resumen Ejecutivo

| Métrica | Valor |
|---------|-------|
| Skills APB | 119 / 119 |
| Skills terceros | 51 / 51 |
| Agentes | 23 / 23 |
| Subagentes | 13 / 13 |
| Workflows | 7 / 7 |
| Providers | 11 / 11 |
| Wrappers | 7 / 7 |
| Adaptadores | 4 / 4 |
| **Total** | **235** |

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
├── agents/                     # 23 agentes
├── subagents/                  # 13 subagentes
├── workflows/                  # 7 workflows
├── skills/
│   ├── apb-owned/             # 119 skills
│   └── third-party/           # 51 skills
├── providers/                  # 11 providers
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

## ✅ Skills APB por Dominio (119)

| Dominio | Cantidad | Patrón ID |
|---------|----------|-----------|
| development | 25 | `apb-dev-*` |
| architecture | 12 | `apb-arch-*` |
| discovery | 12 | `apb-disc-*` |
| platform | 12 | `apb-plat-*` |
| governance | 12 | `apb-gov-*` |
| qa | 12 | `apb-qa-*` |
| operation | 9 | `apb-ops-*` |
| pm | 8 | `apb-pm-*` |
| security | 8 | `apb-sec-*` |
| documentation | 7 | `apb-doc-*` |
| design | 1 | `apb-design-*` |
| orchestration | 1 | `apb-orch-*` |

---

## ✅ Agentes (23)

`apb-agent-business-analyst`, `apb-agent-catalog-manager`, `apb-agent-cloud-architect`, `apb-agent-code-reviewer`, `apb-agent-compliance-audit`, `apb-agent-documentation`, `apb-agent-domain-architect`, `apb-agent-finops`, `apb-agent-governance`, `apb-agent-implementer`, `apb-agent-meta-builder`, `apb-agent-modernization`, `apb-agent-platform-engineer`, `apb-agent-qa-auto`, `apb-agent-release-manager`, `apb-agent-risk-exception`, `apb-agent-security-architect`, `apb-agent-spec-engineer`, `apb-agent-sre`, `apb-agent-tech-debt`, `apb-agent-tech-discovery`, `apb-agent-technical-architect`, `apb-agent-ux-mockup`

---

## ✅ Workflows (7)

`apb-wf-cloud-migration-v1.0`, `apb-wf-code-review-v1.0`, `apb-wf-legacy-onboarding-v1.0`, `apb-wf-qa-evidence-v1.0`, `apb-wf-risk-exception-v1.0`, `apb-wf-sdd-full-v1.0`, `apb-wf-spec-from-legacy-v1.0`

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
