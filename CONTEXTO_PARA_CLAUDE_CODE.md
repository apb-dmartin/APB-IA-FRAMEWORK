# CONTEXTO_PARA_CLAUDE_CODE.md

> **Generado por IA:** Claude (Anthropic), sesión de migración chat → Claude Code, APB-IA-FRAMEWORK.
> **Validado por humano:** _pendiente — completar nombre/rol antes de tratar este documento como referencia operativa._

---

## Propósito de este documento

Este archivo está pensado para que **Claude Code lo lea al iniciar trabajo en este
repositorio**. No es documentación de usuario final — es contexto operativo: qué es este
proyecto, qué arquitectura sigue, qué existe ya, y qué reglas no se deben romper al seguir
trabajando.

Si eres una instancia de Claude Code leyendo esto por primera vez: lee también
`discovery/CONTINUIDAD_PROYECTO.md` y `discovery/PLAN_FASES_FUTURAS.md` antes de proponer
cualquier cambio — contienen el historial sesión por sesión y las decisiones explícitas de
Debora que no deben revertirse sin confirmación suya.

---

## 1. Qué es `APB-IA-FRAMEWORK`

Framework corporativo de agentes de IA para la Autoritat Portuària de Barcelona (APB):
skills, agentes, subagentes, workflows, providers, wrappers y adapters organizados en
dominios funcionales, con gobernanza, validación automática y catálogo auto-generado. Es
infraestructura de desarrollo asistido por IA para el resto de proyectos de APB — no es,
en sí mismo, una aplicación de negocio.

**Stack que este framework ayuda a construir** (no el stack del framework en sí, que es
solo Markdown + Python): .NET 8/C# (backend), DevExpress/DevExtreme + JavaScript o Blazor
(frontend), Django/DRF/GeoDjango (servicios GIS), Azure SQL (almacén relacional principal),
Cosmos DB (cuando se justifica), PostgreSQL/PostGIS (geoespacial), Oracle (solo
on-premise), Azure Service Bus (mensajería corporativa estándar), Jenkins + GitHub Actions
(CI/CD). Debe cumplir LCSP, ENS (mixto Alto/Medio), RGPD y WCAG 2.1 AA.

## 2. Arquitectura del framework

- **Formato de componente:** YAML frontmatter + cuerpo Markdown. **Fuente única de verdad
  del esquema:** `context/apb/SCHEMA.md`. No existen formatos alternativos válidos para
  ninguno de los 7 tipos de componente (skill, agent, subagent, workflow, provider,
  wrapper, adapter).
- **Runtime inicial:** GitHub Copilot. **Adapters:** `adapters/claude/`,
  `adapters/copilot/` — el framework es runtime-agnóstico por diseño (`SYSTEM.md` §4.3).
- **Validación:** `scripts/validate_repo.py --strict` (basado en `pyyaml`). Estado verde
  esperado: **0 errores, ~59 warnings exentos** (los exentos son `source_commit:
  unverified` en componentes de terceros sin acceso de red para verificar el commit exacto
  — política deliberada, `GOVERNANCE.md` §4.2, nunca se inventa un SHA).
- **Catálogo:** `catalog/CATALOG.md`, `INDEX.md`, `DOMAIN_REGISTRY.md` son **siempre
  auto-generados** por `scripts/generate_catalog.py`. Nunca se editan a mano. El CI
  (`.github/workflows/validate.yml`) bloquea el PR si el catálogo está desincronizado — sin
  auto-commit, decisión explícita de Debora en Sesión 6.
- **Tests:** `tests/test_validate_repo.py`, 19 tests de dogfooding del propio validador.
- **3 comandos de salud, ejecutar siempre antes y después de cualquier cambio:**
  ```bash
  python3 scripts/validate_repo.py --strict
  python3 scripts/generate_catalog.py --check
  python3 -m unittest tests.test_validate_repo -v
  ```

## 3. Reglas que no se deben romper (decisiones ya tomadas por Debora)

- **Nunca auto-aprobar ni auto-commitear** outputs de agentes — toda salida de IA requiere
  revisión humana antes de pasar de `draft` a `candidate`/`approved` (`SYSTEM.md` §2.1).
- **Nunca inventar un SHA** de `source_commit` para componentes de terceros — usar
  `"unverified"` + `verified_date` si no hay acceso de red para verificarlo
  (`GOVERNANCE.md` §4.2).
- **Discovery obligatorio antes de crear una skill nueva** — buscar en `catalog/CATALOG.md`
  e `INDEX.md` si ya existe algo que cubra la necesidad, total o parcialmente, antes de
  proponer un componente nuevo (Principio Fundamental #10, `CONTRIBUTING.md`).
- **Disciplina de codificación agéntica** (Principio #11): pensar antes de codificar,
  simplicidad ante todo (sin abstracciones no solicitadas), cambios quirúrgicos (tocar solo
  lo que el cambio requiere), ejecución dirigida a objetivos verificables. Implementado en
  `apb-dev-grill-before-code-v1.0`, `apb-dev-atomic-plan-v1.0`,
  `apb-dev-simplicity-first-v1.0`, `apb-dev-surgical-changes-v1.0`,
  `apb-dev-verify-before-done-v1.0`.
- **Normalización a Markdown** (Principio #12): cualquier adjunto ofimático (Word, Excel,
  PowerPoint, PDF) que se use como input a un componente se normaliza a Markdown primero
  (`apb-plat-doc-to-markdown-v1.0`).
- **Identificación explícita de IA + validador humano** (`SYSTEM.md` §7.2, política de
  Debora): todo artefacto generado por un agente/skill debe declarar visiblemente, en el
  propio documento, que fue generado por IA y qué humano lo validó — no basta un campo de
  metadatos interno. Bloque estándar a incluir al final de cada componente nuevo:
  ```
  > **Generado por IA:** Claude (Anthropic/Claude Code), [contexto/fecha].
  > **Validado por humano:** _pendiente — completar nombre/rol del validador antes de pasar a `candidate`._
  ```
- **No crear componentes fuera del esquema** de `SCHEMA.md`, incluso si se pide una
  "versión rápida" sin todos los metadatos.

## 4. Estructura real del repositorio (verificada, no de memoria)

```
APB-IA-FRAMEWORK/
├── .github/workflows/validate.yml     # CI: valida cada PR
├── .gitignore
├── README.md                          # 12 Principios Fundamentales
├── SYSTEM.md                          # reglas globales, autonomía, trazabilidad
├── GOVERNANCE.md                      # ciclo de vida, aprobadores, terceros §4.2
├── CONTRIBUTING.md                    # checklist de PR, discovery obligatorio
├── LICENSE.md                         # uso interno APB
│
├── catalog/CATALOG.md                 # AUTO-GENERADO
├── INDEX.md                           # AUTO-GENERADO
├── DOMAIN_REGISTRY.md                 # AUTO-GENERADO
│
├── context/apb/
│   ├── SCHEMA.md                      # fuente única de verdad del frontmatter
│   ├── policies/                      # ai, security, quality, infrastructure, procurement, capacity, compliance, docks
│   ├── standards/                     # STANDARD_ARCHITECTURE.md, STANDARD_DEVELOPMENT.md, STANDARD_QA.md
│   └── templates/                     # plantilla por tipo de componente (AGENT.md desactualizada, ver nota abajo)
│
├── skills/
│   ├── apb-owned/                     # skills propias APB, 22 dominios (governance, architecture,
│   │                                  # development, discovery, qa, security, operation, platform, pm...)
│   └── third_party/                   # skills de terceros, organizadas por organización GitHub de origen
│
├── agents/                            # agentes
├── subagents/                         # subagentes especializados por stack/función
├── workflows/                         # workflows multi-componente
├── providers/                         # conectores (Jira/Atlassian, Sonar, Playwright, k6, Azure Key Vault...)
├── wrappers/                          # wrappers de skills de terceros
├── adapters/claude/ y copilot/        # adaptadores de runtime
│
├── scripts/validate_repo.py           # validador --strict
├── scripts/generate_catalog.py        # regenera catálogo
├── tests/test_validate_repo.py        # 19 tests
│
├── discovery/
│   ├── CONTINUIDAD_PROYECTO.md        # bitácora de sesiones cerradas — LEER PRIMERO
│   └── PLAN_FASES_FUTURAS.md          # puntos pendientes/resueltos, mapeo a sesiones
│
├── docs/sdd-getting-started.md
├── examples/                          # dotnet-review, spec-generation
└── repo-scaffold/                     # legacy-ready, sdd-ready
```

**Nota de inconsistencia conocida, no corregida:** `context/apb/templates/AGENT.md` usa un
formato antiguo (metadatos en blockquote) que **ya no es válido** según `SCHEMA.md` — los
agentes reales del repo usan YAML frontmatter. Si vas a crear un agente nuevo, sigue el
formato real observado en `agents/*.md`, no la plantilla de `templates/AGENT.md` tal cual
está hoy. Corregir esa plantilla es trabajo pendiente, no asumido en ninguna sesión todavía.

## 5. Estado de componentes (verificado por ejecución, no estimado)

A la fecha de este export: **226 componentes, 0 errores, ~59 warnings exentos, 0 drift de
catálogo, 19/19 tests en verde.**

| Tipo | Cantidad |
|---|---|
| Skills APB (`skills/apb-owned/`) | 114 |
| Skills de terceros (`skills/third_party/`) | 52 |
| Agentes | 21 |
| Subagentes | 13 |
| Workflows | 7 |
| Providers | 10 |
| Wrappers | 7 |
| Adapters | 2 |

Todos los componentes están en `status: "draft"` — válidos a nivel de esquema, **no
aprobados** por revisión humana sustantiva. Pasar de `draft` a `candidate`/`approved` es
trabajo de Debora, no de Claude Code de forma autónoma.

## 6. Repositorio relacionado, ahora deprecado

`apb-ai-skills` (GitHub Copilot-oriented, testing/QA) **queda deprecado** — decisión de
Debora tomada en la Sesión QA de este proyecto. Su contenido de valor real ya fue fusionado
dentro de este repo (ver sección 9 de `discovery/CONTINUIDAD_PROYECTO.md`). No se ha tocado
ese repositorio físicamente; sus referencias internas a las skills fusionadas
(`apb-unit-test-generator`, `apb-ens-security-audit`, `apb-test-plan-lcsp`,
`apb-test-data-rgpd`) quedaron desactualizadas y sus 2 GitHub Actions
(`sync-skills.yml`, `validate-skills.yml`) seguirán ejecutándose salvo que alguien los
desactive manualmente en ese repo.

## 7. Pendiente fuera del alcance de cualquier sesión de chat

El documento `proyecto.md` (fuente normativa del proyecto, vive fuera de este repositorio
de código, en gestión documental de Debora) tiene una fila de la tabla de puntos de
validación obligatoria ("Release → responsable: ¿?") que sigue sin actualizar a "Release
Manager / Arquitectura" — ya corregido en `SYSTEM.md` §6 de este repo, pero Claude (chat) no
tuvo permiso de escritura sobre `proyecto.md`. Si ese documento vive en este repositorio
local, corrígelo; si no, es tarea de Debora fuera de este repo.

## 8. Próximos pasos del plan (ver `discovery/PLAN_FASES_FUTURAS.md` para detalle completo)

En orden recomendado: **Sesión Frontend** (bloqueada hasta aclarar alcance de
`GISPEM__Guía_de_estilos.pdf`) → **punto #38** (catálogo de dominios + descomposición de
monolitos, Fase 0 bloqueada hasta que Debora aporte su listado de APIs) → **Sesión 13**
(cierre de pendientes históricos) → **Sesión 14** (documentación por audiencias en Word,
última sesión "normal") → **Fase #43** (aplicar la política de identificación IA/validador
retroactivamente a todo el catálogo — deliberadamente la última tarea de todas).
