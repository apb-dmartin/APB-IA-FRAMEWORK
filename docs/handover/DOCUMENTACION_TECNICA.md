# APB AI Framework — Documentación técnica (handover)

## 1. Estructura del repositorio
| Carpeta | Contenido |
|---|---|
| `agents/`, `subagents/`, `workflows/` | Componentes `.md` con frontmatter |
| `skills/apb-owned`, `skills/third-party` | 184 + 57 skills |
| `providers/`, `wrappers/` | Acceso a herramientas externas |
| `adapters/` | claude, copilot, m365, rovo |
| `catalog/` | `CATALOG.md` generado |
| `context/apb/` | `SCHEMA.md`, standards, templates, policies, knowledge |
| `scripts/` | Python de validación/generación/invocación |
| `forge/` | App Forge (Atlassian Rovo): `manifest.yml`, `src/functions`, `src/resolvers` |
| `openapi/` | `apb-framework-api.yaml`, `ai-plugin.json` |
| `infra/azure-qa-runtime/` | Runtime QA (k6, playwright) |
| `repo-scaffold/` | `harness-ready`, `sdd-ready`, `legacy-ready` |
| `discovery/` | Planes, handoffs, dossiers DDD SÒSTRAT (~137 ficheros) |
| `telemetry/` | `events.jsonl` |
| `tests/`, `examples/`, `qa-evidence/`, `docs/` | Pruebas, ejemplos, evidencias, guías |
| `design-system/`, `domain-catalog/` | Submódulos git |

## 2. Esquema de componentes
Definido en `context/apb/SCHEMA.md` (8 tipos). Campos mínimos: `id`, `type`, `version`, `status`, `owner`, `autonomy_level` (agentes), dependencias. Patrón de ID: `apb-{dominio}-{nombre}-v{M}.{m}`.

## 3. Scripts (`scripts/`)
| Script | Función |
|---|---|
| `validate_repo.py [--strict]` | Valida frontmatter, IDs, referencias cruzadas |
| `generate_catalog.py` | Regenera `INDEX.md`/`catalog/CATALOG.md` |
| `invoke_agent.py` | Invoca un agente |
| `orchestrate_checkpoint_gate.py` | Puerta de validación humana |
| `emit_telemetry.py` | Emite eventos a `telemetry/events.jsonl` / Azure Monitor |

Requisitos: Python 3.x + PyYAML. Ejecutar desde la raíz.

## 4. CI/CD (`.github/workflows/`)
- `validate.yml`: validación estricta en PR/push.
- `human-checkpoint-poc.yml`: PoC de checkpoint humano.
- `review-reminder.yml`: recordatorios de revisión periódica.
- `telemetry.yml`: sincroniza eventos pendientes (`sent:false`) a Azure Monitor (push a `telemetry/events.jsonl` y cron 02:00 UTC).

## 5. MCP y secretos
- `.mcp.json`: servidores `playwright`, `ms365`, `sonar`.
- `.env` (gitignorado) contiene `SONARQUBE_URL`, `SONARQUBE_TOKEN`, `SONAR_TOKEN`. **Nunca commitear ni compartir**; el equipo receptor debe generar sus propios tokens y rotar los existentes.
- Existe `PLAN_MCP_SERVER_APB.md` con el diseño de un MCP Server propio (MVP local; 3 tools; fases 1–6).

## 6. Submódulos
```
git clone --recurse-submodules <repo>
git submodule update --remote domain-catalog design-system   # tras revisar diff
```
El submódulo `domain-catalog` está desfasado respecto a `origin/main` (ver pendiente #95).

## 7. Integración con Mother Portal
Mother lee el framework en disco (`Framework:RepositoryPath`), parsea frontmatter YAML y construye el catálogo. Cambios en `SCHEMA.md` pueden romper el parser de Mother (`Mother.Infrastructure`); coordinar ambos.

## 8. Cómo añadir un componente
1. Copiar plantilla de `context/apb/templates/`.
2. Rellenar frontmatter (`status: draft`).
3. `python scripts/validate_repo.py --strict`.
4. `python scripts/generate_catalog.py`.
5. PR; revisión de Arquitectura APB (two-eyes si procede). Un agente nunca aprueba.

## 9. Observaciones técnicas
- Repo **público** en GitHub (`apb-dmartin/APB-IA-FRAMEWORK`): no publicar contenido confidencial (ver #94).
- Algunos ficheros muestran problemas de codificación (UTF-8 mal interpretado) en workflows; guardar siempre en UTF-8.
- No hay tests de comportamiento de agentes; `tests/` cubre validación estructural.
- Telemetría: retrofit a componentes existentes pendiente (Fase #43).
- Operaciones git sobre OneDrive son lentas; preferible clonar fuera de OneDrive.
