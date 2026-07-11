# Instrucciones de PR — Bounded Contexts de SÒSTRAT en apb-domain-catalog (v3, reparentado)

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.
> **v3 (2026-07-11)**: tras confirmar que `apb-domain-catalog` remoto (no la copia local, que estaba desactualizada — ver `catalog-comparison.md`) ya tiene 21 dominios de negocio `proposed`, este PR deja de proponer dominios nuevos en bloque y pasa a **añadir bounded contexts, con evidencia de código, a dominios ya existentes**. Se retiraron los 6 dominios inventados en la v1/v2 de este análisis y 2 bounded contexts duplicados (Notificaciones, Autenticación/SSO — ya cubiertos por `dom-transversal-arq-v1`). El núcleo financiero, que en la v2 se había decidido desplegar como un único servicio, **se separa de nuevo** en dos dominios y dos servicios: Concesiones y Facturación (decisión del usuario, 2026-07-11).
> **v4 (2026-07-11, mismo día)**: `bc-mano-estiba-v1` y `bc-clavegueram-v1` habían quedado reparentados por la fuerza bajo dominios que no encajaban bien (Transporte Terrestre y Facturación respectivamente). El usuario confirmó que merecen dominio propio — se crean `dom-mano-estiba-v1` y `dom-clavegueram-v1` como **2 propuestas de dominio nuevas**, además de la adición de bounded contexts a los 13 dominios ya existentes.

> **Restricción `autonomy_level 1`**: este agente **no abre el PR por sí mismo**. Estas son instrucciones para que una persona del equipo lo haga tras validar el contenido.

## 0. Estado real del catálogo (re-verificado 2026-07-11, contra `origin/main` tras `git fetch`)

`apb-domain-catalog` (`https://github.com/apb-dmartin/APB-DOMAIN-CATALOG`) tiene **21 dominios de negocio en estado `proposed`** (commit `e753d3e`), de una sesión de análisis previa top-down (30/06/2026). Ninguno tiene bounded contexts todavía (`bounded_contexts: []` en los 21). Este PR aporta: (a) 19 bounded contexts (con evidencia de código real de `SOSTRAT-Sostrat-MJ8`) para 13 de esos 21 dominios existentes, y (b) 2 dominios de negocio nuevos (`dom-mano-estiba-v1`, `dom-clavegueram-v1`) con su bounded context correspondiente cada uno, para capacidades sin equivalente en los 21 originales.

**Importante para quien abra el PR**: el submodule `domain-catalog` dentro de `APB-IA-FRAMEWORK` tiene commiteado un puntero desactualizado (`c90668d`, el commit inicial, 4 commits por detrás de `origin/main`). Antes de trabajar, actualizar el puntero del submodule (`git submodule update --remote domain-catalog` desde la raíz de `APB-IA-FRAMEWORK`, revisar el diff, y commitear el bump) para que futuras sesiones no repitan el error de esta (ver `session-retro-2026-07-11.md` en este mismo directorio).

## 1. Validación previa (obligatoria antes de cualquier PR)

1. Revisar `catalog-comparison.md` completo — documenta los conflictos de modelado reales (Escalas posiblemente ya cubierta por ARGOS, Contenedores como subdominio vs. bounded context propio, etc.).
2. Confirmar `owner_team` real por bounded context (placeholder `equipo-sostrat` en los 21 ficheros).
3. `bc-mano-estiba-v1` y `bc-clavegueram-v1` ya no tienen reparenting forzado — tienen dominio propio (`dom-mano-estiba-v1`, `dom-clavegueram-v1`), confirmado por el usuario 2026-07-11.
4. **`bc-escalas-v1` NO debe enviarse al catálogo como bounded context de extracción** — evidencia de código confirma que ARGOS (`APB.API.TES`) ya consume la escala de SÒSTRAT en producción (evento real `MSG0004 SOSTRAT→TES`, DTO idéntico al modelo SÒSTRAT). Antes de tocar esto, requiere una sesión formal con el equipo de ARGOS/AOM — ver `decomposition-roadmap.md` Fase 5. Mientras tanto, `escalas.md` NO se añade a `domains/operaciones-maritimas/contexts/` en este PR.

## 2. Dónde colocar cada fichero (estructura real, `domains/<nombre>/domain.md` + `domains/<nombre>/contexts/<contexto>.md`)

### 2.1 Bounded contexts a añadir a dominios ya existentes (no se crea `domain.md`)

| Carpeta existente `domains/<nombre>/` | `contexts/*.md` a añadir (origen en `discovery/ddd-sostrat-mj8/proposals/`) |
|---|---|
| `operaciones-maritimas/` | **NO añadir `escalas.md` en este PR** — ver §1.4, requiere validación con ARGOS primero |
| `cruceros/` | `cruceros.md` ← `bc-cruceros-v1.md` |
| `ferrocarril/` | `ferrocarril-portuario.md` ← `bc-ferrocarril-portuario-v1.md` |
| `concesiones/` | `titulo.md` ← `bc-titulo-v1.md` · `garantias.md` ← `bc-garantias-v1.md` |
| `facturacion/` | `liquidacion.md` ← `bc-liquidacion-v1.md` · `facturacion.md` ← `bc-facturacion-v1.md` |
| `mercancias/` | `manifiestos.md` ← `bc-manifiestos-v1.md` · `aduanas-contenedores.md` ← `bc-aduanas-contenedores-v1.md` · `depotsis.md` ← `bc-depotsis-v1.md` · `datos-maestros-equipamiento.md` ← `bc-datos-maestros-equipamiento-v1.md` |
| `mercancias-peligrosas/` | `mmpp.md` ← `bc-mmpp-v1.md` |
| `inspeccion-control/` | `pif.md` ← `bc-pif-v1.md` |
| `medio-ambiente-marpol/` | `marpol-residuos.md` ← `bc-marpol-residuos-v1.md` |
| `suministros-buques/` | `aguada.md` ← `bc-aguada-v1.md` (⚠️ gap de evidencia — ver `notes` del fichero) |
| `pesca-marinas/` | `marinas-pesca.md` ← `bc-marinas-pesca-v1.md` |
| `transporte-terrestre/` | `transporte-terrestre.md` ← `bc-transporte-terrestre-v1.md` |
| `acceso-seguridad-fisica/` | `pps.md` ← `bc-pps-v1.md` |

### 2.2 Dominios nuevos a crear (con su propio `domain.md` + 1 contexto)

| Carpeta nueva `domains/<nombre>/` | `domain.md` | `contexts/*.md` |
|---|---|---|
| `mano-estiba/` | ← `dom-mano-estiba-v1.md` | `mano-estiba.md` ← `bc-mano-estiba-v1.md` |
| `clavegueram/` | ← `dom-clavegueram-v1.md` | `clavegueram.md` ← `bc-clavegueram-v1.md` |

**No enviar al catálogo**: `bc-carga-inicial-etl-v1.md` (no es un bounded context de negocio) y `bc-escalas-v1.md` (pendiente de validación con ARGOS, ver §1.4 — no es un "no enviar nunca", es "no enviar todavía").

**Total: 18 ficheros de contexto → 13 carpetas de dominio existentes, + 2 dominios nuevos completos (domain.md + contexto).**

## 3. Estado de cada fichero: `discovered`, no `proposed`

Los 21 ficheros ya tienen `status: "discovered"` en su frontmatter (`GOVERNANCE.md` §2: `proposed` solo se asigna al abrir PR). El equipo que abra el PR debe cambiar `status` a `"proposed"` en cada fichero como parte de ese PR.

## 4. Al abrir el PR

- Título sugerido: `[ai-gen] Bounded contexts de SÒSTRAT (SOSTRAT-Sostrat-MJ8) para dominios ya propuestos`.
- Commit con prefijo `[ai-gen]` y `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`.
- Cambiar `status: "discovered"` → `status: "proposed"` en los 21 ficheros.
- **No tocar `catalog/DOMAINS.md`** — lo actualiza Arquitectura APB tras aprobar (`GOVERNANCE.md` §3.1 paso 7).
- Señalar explícitamente en la descripción del PR los 4 puntos de `catalog-comparison.md` categoría B (conflictos de modelado) para que el revisor los vea sin tener que leer todo el análisis.

## 5. Después de la aprobación

- Solo Arquitectura APB puede pasar `proposed` → `approved`, rellenar `approved_date`, y actualizar `catalog/DOMAINS.md`.
- `decomposition-roadmap.md` y `adr-sostrat-decomposition-strategy.md` quedan disponibles para planificar la ejecución, como base separada de este PR de catálogo.
