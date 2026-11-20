# APB AI Framework — Documentación funcional (handover)

> Destinatario: equipo de desarrollo que continúa la evolución del framework.
> Fuentes: `README.md`, `SYSTEM.md`, `GOVERNANCE.md`, `CONTRIBUTING.md`, `INDEX.md`, `discovery/HANDOFF_TECNICOS.md`.
> Nota: la norma del repo es no crear documentos de handoff sueltos (`discovery/PLAN_FASES_FUTURAS.md` es el canónico). Este conjunto vive en `docs/handover/` y debe enlazarse desde esos documentos canónicos.

## 1. Propósito
Repositorio **fuente de verdad** de los componentes de IA de la Autoritat Portuària de Barcelona (APB): agentes, skills, subagentes, workflows y providers, con gobernanza explícita. Es consumido por el **Mother Portal** (catálogo y ejecución) y por los adaptadores de runtime (Claude, Copilot, M365, Rovo).

## 2. Inventario (según `INDEX.md`, 2026-07-14)
| Tipo | Nº |
|---|---|
| Agentes | 40 |
| Skills (184 APB + 57 terceros) | 241 |
| Subagentes | 35 |
| Workflows | 17 |
| Providers | 23 |
| Wrappers | 7 |
| Adaptadores (claude, copilot, m365, rovo) | 4 |
| **Total componentes catalogados** | **367** |

La tabla se regenera con `scripts/generate_catalog.py`.

## 3. Jerarquía de componentes
Capability → Provider → Wrapper → Skill → Subagente → Agente → Workflow.
- **Skill**: capacidad atómica reutilizable.
- **Subagente**: especialista que compone skills.
- **Agente**: rol con objetivo, restricciones y nivel de autonomía (0–4).
- **Workflow**: orquestación de agentes con checkpoints humanos.
- **Provider/Wrapper**: acceso a herramientas externas (MCP, APIs).

## 4. Convenciones
- IDs: `apb-{dominio}-{nombre}-v{M}.{m}`, `apb-agent-*`, `apb-wf-*`.
- Cada componente es un `.md` con frontmatter YAML validado contra `context/apb/SCHEMA.md` (8 tipos).
- Idioma de contenido: español.

## 5. Ciclo de vida y gobernanza
Estados: `draft → candidate → under_review → approved → deprecated → retired` (más `watchlist`, `rejected`).
Reglas clave (`GOVERNANCE.md`):
- **Ningún agente puede aprobar**; solo personas.
- Principio **two-eyes** (dos revisores) para componentes críticos/de terceros.
- Escalado a 5 días hábiles; revisión periódica cada 6 meses.
- Los componentes de terceros requieren verificación de licencia y supply chain.

## 6. Flujos funcionales principales
1. **Alta/cambio de componente**: rama + PR → CI `validate.yml` (`validate_repo.py --strict`) → revisión Arquitectura APB → merge → regeneración de catálogo.
2. **Descubrimiento DDD**: el agente `apb-agent-ddd` (v1.1.0, con Fase 0 de consumidores externos) y subagentes de entrevista generan dominios/bounded contexts hacia `APB-DOMAIN-CATALOG`.
3. **Ejecución con checkpoint humano**: `orchestrate_checkpoint_gate.py` + workflow `human-checkpoint-poc.yml`.
4. **Telemetría**: `emit_telemetry.py` escribe `telemetry/events.jsonl`; `telemetry.yml` sincroniza a Azure Monitor.
5. **Publicación a runtimes**: adaptadores en `adapters/` y `forge/` (Rovo), `openapi/` (API del framework), `.mcp.json` (playwright, ms365, sonar).

## 7. Contexto corporativo (`context/apb/`)
Estándares (3), plantillas (7), 24 políticas oficiales APB en 8 dominios (seguridad, IA, calidad, infraestructura, capacidad, compras, compliance, DOCKS) y `knowledge/` (`APB_KNOWLEDGE_BASE.md`). Los agentes deben respetarlos.

## 8. Repos relacionados
- `design-system` y `domain-catalog` como submódulos (`.gitmodules`).
- Mother Portal: consume este repo vía `Framework:RepositoryPath`.

## 9. Estado actual
Marco completo en estado `draft`. Gobierno aún no iniciado: 37 componentes aprobados (solo terceros), **0 componentes APB propios aprobados**. Ver `TEMAS_PENDIENTES.md`.
