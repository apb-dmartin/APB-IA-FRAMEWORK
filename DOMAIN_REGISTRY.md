# Domain Registry

> **ID:** `apb-domain-registry-v1.0`
> **Versión:** 1.0.0
> **Estado:** draft

---

## 📋 Dominios Registrados

| ID | Nombre | Skills | Color |
|----|--------|--------|-------|
| `dev` | Development | 27 | 🔵 |
| `qa` | Quality Assurance | 14 | 🟢 |
| `arch` | Architecture | 12 | 🟣 |
| `disc` | Discovery | 12 | 🟡 |
| `plat` | Platform | 12 | 🟠 |
| `sec` | Security | 8 | 🔴 |
| `gov` | Governance | 12 | ⚫ |
| `ops` | Operation | 13 | 🔵 |
| `doc` | Documentation | 7 | ⚪ |
| `orch` | Orchestration | 1 | 🟤 |
| `pm` | Project Management | 8 | 🟢 |
| `design` | Design & UX | 2 | 🎨 |

---

## 🔗 Mapeo Dominio → Carpeta

| Dominio | Carpeta Skills | Carpeta Políticas |
|---------|---------------|-------------------|
| development | `skills/apb-owned/development/` | — |
| qa | `skills/apb-owned/qa/` | `context/apb/policies/quality/` |
| architecture | `skills/apb-owned/architecture/` | `context/apb/policies/security/` |
| discovery | `skills/apb-owned/discovery/` | — |
| platform | `skills/apb-owned/platform/` | `context/apb/policies/infrastructure/` |
| security | `skills/apb-owned/security/` | `context/apb/policies/security/` |
| governance | `skills/apb-owned/governance/` | `context/apb/policies/compliance/` |
| operation | `skills/apb-owned/operation/` | `context/apb/policies/capacity/` |
| documentation | `skills/apb-owned/documentation/` | — |
| orchestration | `skills/apb-owned/orchestration/` | — |
| pm | `skills/apb-owned/pm/` | — |
| design | `skills/apb-owned/design/` | — |

---

> **Nota de gobernanza:** los conteos de la tabla de dominios y este mapeo
> son **derivados automáticamente** por `scripts/generate_catalog.py`
> (Sesión 3) a partir del frontmatter real de cada skill. No editar el
> conteo manualmente; cualquier valor aquí que no coincida con
> `scripts/validate_repo.py` se considera desactualizado.

---
*Documento generado por el APB AI Framework.*
