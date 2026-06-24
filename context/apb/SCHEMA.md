# SCHEMA.md — Esquema de Metadatos del APB AI Framework

> **ID:** `apb-schema-v1.0`
> **Versión:** 1.0.0
> **Estado:** draft
> **Propietario:** Arquitectura APB
> **Fecha:** 2026-06-22

---

## 1. Principio

Todo componente del framework (skill, agent, subagent, workflow, provider, wrapper, adapter)
declara sus metadatos en un bloque **YAML frontmatter** al inicio del archivo, delimitado por
`---`. Este es el **único** formato válido. No se admiten metadatos en texto markdown libre
(p. ej. `> **ID:** ...`) ni en tablas markdown como sustituto del frontmatter.

```yaml
---
id: "apb-dev-code-review-v1.0"
name: "Code Review"
...
---

# Cuerpo del documento en Markdown
```

Razón: el frontmatter YAML es parseable de forma fiable por herramientas (validador, generador
de catálogo, CI), interopera con el estándar usado por Anthropic Skills, OpenSpec y la mayoría
de sistemas documento+metadatos, y es el formato que ya usan los componentes mejor gobernados
de este repositorio.

---

## 2. Campos comunes (obligatorios en los 7 tipos)

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | string | Identificador único. Debe coincidir exactamente con el nombre de archivo (sin extensión). Formato según tipo (sección 4). |
| `name` | string | Nombre legible, corto. |
| `description` | string | 1–3 frases. Qué hace y cuándo usarlo. |
| `version` | string | Semántico: `1.0.0`, `1.0.0-draft`. |
| `status` | enum | Uno de: `draft`, `candidate`, `under_review`, `approved`, `deprecated`, `retired`, `watchlist`, `rejected` (ver `GOVERNANCE.md` §1). |
| `owner` | string | Nombre + email del responsable. |
| `domain` | string | Dominio funcional (ver `DOMAIN_REGISTRY.md`). |
| `created_date` | string (`YYYY-MM-DD`) | Fecha de creación. |
| `review_date` | string (`YYYY-MM-DD`) | Fecha de última revisión. |

## 3. Campos específicos por tipo

### 3.1 Skill (`apb-owned` y `third_party`)
| Campo | Tipo | Obligatorio | Descripción |
|---|---|---|---|
| `autonomy_level` | int (0–4) | Sí | Ver `SYSTEM.md` §5. |
| `inputs` | list | Sí | Definidos en el cuerpo si la lista es compleja; al menos referenciados aquí por nombre. |
| `outputs` | list | Sí | Idem. |
| `consumed_by` | list[string] | No | IDs de agentes que la usan. |
| `depends_on` | list[string] | No | IDs de otras skills/providers/wrappers. |
| `source_repo` | string (URL) | Solo `third_party` | Repositorio de origen. |
| `source_license` | string | Solo `third_party` | Licencia del origen. |
| `source_commit` | string | Solo `third_party` | Commit o tag **real**, nunca `HEAD`. Si no se dispone de acceso para verificar el SHA exacto, usar `"unverified"` y declarar `verified_date` con la fecha de la última revisión manual del contenido (ver convención en GOVERNANCE.md §4.2). |
| `verified_date` | string (`YYYY-MM-DD`) | Solo `third_party`, cuando `source_commit: "unverified"` | Fecha en que se revisó manualmente que el contenido sigue vigente respecto al repo de origen. Debe refinarse a un SHA real con `git ls-remote` o `git log -1` en cuanto se disponga de acceso de red al repositorio. |

### 3.2 Agent
| Campo | Tipo | Obligatorio | Descripción |
|---|---|---|---|
| `autonomy_level` | int (0–4) | Sí | |
| `skills` | list[string] | Sí | IDs de skills disponibles. |
| `subagents` | list[string] | No | IDs de subagentes que puede invocar. |
| `runtime` | list[string] | Sí | Subconjunto de `["copilot", "claude"]`. |
| `human_review_points` | list[string] | Sí | Fases con validación humana obligatoria. |

### 3.3 Subagent
| Campo | Tipo | Obligatorio | Descripción |
|---|---|---|---|
| `parent_agent` | string | Sí | ID del agente que lo especializa. |
| `specialty` | string | Sí | Tecnología o contexto concreto (.NET, Django, Azure...). |

### 3.4 Workflow
| Campo | Tipo | Obligatorio | Descripción |
|---|---|---|---|
| `autonomy_level` | int (0–4) | Sí | |
| `agents` | list[string] | Sí | IDs de agentes orquestados, en orden. |
| `human_checkpoints` | list[string] | Sí | Puntos de control humano. |

### 3.5 Provider
| Campo | Tipo | Obligatorio | Descripción |
|---|---|---|---|
| `provider_type` | enum | Sí | `knowledge`, `action`, `secret`. |
| `access_mode` | string | Sí | P.ej. `read-only`, `read-write`. |

### 3.6 Wrapper
| Campo | Tipo | Obligatorio | Descripción |
|---|---|---|---|
| `wraps` | string | Sí | Componente/repo de terceros envuelto. |
| `source_repo`, `source_license`, `source_commit` | string | Sí | Igual que en skill de terceros. |

### 3.7 Adapter
| Campo | Tipo | Obligatorio | Descripción |
|---|---|---|---|
| `runtime_target` | string | Sí | `copilot` o `claude`. |
| `adapted_components` | list[string] | No | IDs de skills/agentes ya adaptados. |

---

## 4. Patrones de ID por tipo

| Tipo | Patrón | Ejemplo |
|---|---|---|
| Skill APB | `apb-{dominio}-{nombre}-v{major}.{minor}` | `apb-dev-code-review-v1.0` |
| Skill terceros | `third-{fuente}-{nombre}-v{major}.{minor}` | `third-anthropic-mcp-builder-v1.0` |
| Agent | `apb-agent-{nombre}-v{major}.{minor}` | `apb-agent-spec-engineer-v1.0` |
| Subagent | `apb-sub-{dominio}-{especialidad}-v{major}.{minor}` | `apb-sub-dev-django-v1.0` |
| Workflow | `apb-wf-{nombre}-v{major}.{minor}` | `apb-wf-sdd-full-v1.0` |
| Provider | `prov-{nombre}-v{major}.{minor}` | `prov-github-v1.0` |
| Wrapper | `wrap-{fuente}-{nombre}-v{major}.{minor}` | `wrap-hkuds-lightrag-v1.0` |
| Adapter | `adapter-{runtime}-v{major}.{minor}` | `adapter-claude-v1.0` |

**Regla de oro:** el `id` declarado en el frontmatter debe ser **idéntico** al nombre de archivo
(sin extensión `.md`). El validador rechaza cualquier discrepancia.

---

## 5. Referencias
- `GOVERNANCE.md` — estados y aprobadores.
- `CONTRIBUTING.md` — checklist de PR (debe citar este esquema).
- `scripts/validate_repo.py` — implementación del validador basado en este esquema.
