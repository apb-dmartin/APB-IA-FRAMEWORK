# Cobertura de dominio — repositorios locales vs. apb-domain-catalog

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.
> Cruce entre los ~69 repositorios clonados localmente en `GitHub-Repos\otros\` (para el lote de 32 planes de pruebas, ver memoria `project_32_test_plans_lote`) y los 21 dominios reales de `apb-domain-catalog` (`origin/main`, commit `e753d3e`, verificado con `git fetch` antes de leer — ver `session-retro-2026-07-11.md`).

## Resumen

- **69 repos locales** en `GitHub-Repos\otros\`.
- **21 dominios** en el catálogo, cruzados por el campo `related_systems` de cada `domain.md` (no por `ubiquitous_language` ni notas sueltas, para evitar falsos positivos).
- **39 repos con dominio identificado** (explícito o con discrepancia menor de nombre/namespace).
- **5 repos "candidatos no confirmados"** — el propio catálogo ya los marca como pendientes de asignar.
- **25 repos sin ningún rastro en el catálogo** — necesitan análisis DDD si se quiere cerrar la cobertura.

## Repos sin dominio identificado (25) — priorizados por probabilidad de encaje

### Prioridad alta — comparten familia de prefijo con dominios ya cubiertos (probablemente el mismo dominio, otro sufijo funcional)

| Repo | Familia relacionada ya cubierta | Dominio candidato |
|---|---|---|
| `APB.API.EQD` | `APB.API.EQL`/`APB.HST.EQV` (Inspección y Control) | `dom-inspeccion-control-v1` |
| `APB.API.EQI` | ídem | `dom-inspeccion-control-v1` |
| `APB.API.EQS` | ídem | `dom-inspeccion-control-v1` |
| `APB.API.LRD` | `APB.API.LRG`/`APB.APP.LRG` (Líneas Regulares) | `dom-lineas-regulares-v1` |
| `APB.API.LRL` | ídem | `dom-lineas-regulares-v1` |
| `APB.API.LRT` | ídem | `dom-lineas-regulares-v1` |

### Prioridad media — "candidatos no confirmados" ya anotados por el propio catálogo

El dominio `dom-integraciones-edi-v1` dice literalmente en sus notas: *"Las APIs desconocidas del inventario APIM (DGS/ESF/ESM/FLO/IPB/MPA/MST/RESPONSIBLE/GPC/ROSS) probablemente son adaptadores que caen aquí o en su dominio de negocio — pendiente de identificar producto por API."*

| Repo | Nota |
|---|---|
| `APB.API.DGS` | Candidato a `dom-integraciones-edi-v1`, sin confirmar |
| `APB.API.ESF` | ídem |
| `APB.API.ESM` | ídem |
| `APB.API.IPB` | ídem |
| `APB.API.MST` | ídem — **cuidado**: no confundir con el "MST" de Mano de Estiba mencionado en `ticketgranting-api-client` (ver `dom-mano-estiba-v1.md`); no está claro si son el mismo sistema o una coincidencia de siglas. Confirmar antes de asumir relación. |

### Prioridad baja — sin ningún rastro textual en el catálogo, análisis DDD desde cero

`APB.API.BKO`, `APB.API.CPR`, `APB.API.CRL`, `APB.API.MAD`, `APB.API.MES`, `APB.API.MPC`, `APB.API.MPT`, `APB.API.MSH`, `APB.API.NTA`, `APB.API.PAL`, `APB.API.PEL`, `APB.API.PVD`, `APB.API.SLC`, `APB.API.VXL`, `APB.API.WDE`, `APB.CLOUD.MPS`, `APB.DGT`, `APB.GNA`, `APB.HEM`.

**Nota**: `APB.API.MPT` ya tiene un plan de pruebas completo del lote de 32 (ver memoria `project_32_test_plans_lote` — "único repo del lote junto a TRU con proyecto de tests xUnit ya existente"). Tener plan de pruebas no implica tener dominio identificado en el catálogo — son dos inventarios independientes que conviene mantener sincronizados.

## Discrepancias menores encontradas (nombre de repo ≠ nombre citado en `related_systems`)

| Repo real | Nombre citado en el dominio | Dominio |
|---|---|---|
| `APB.API.ARG` | `APB.APP.ARG` (solo la app está citada) | Operaciones Marítimas |
| `APB.API.EQV` | `APB.HST.EQV` | Inspección y Control |
| `APB.API.PSR` | `APB.MSG.PSR` | Administración Electrónica |
| `APB.API.REB` | `APB.HST.REB` | Facturación y Tasas Portuarias |
| `APB.INS` | `APB.APP.INS` | Inspección y Control |
| `APB.LIB.ARG` | (librería del ecosistema, no citada literalmente) | Operaciones Marítimas (por asociación) |

Son probablemente el mismo sistema con namespace/capa distinta (API vs APP vs HST vs MSG vs LIB), pero **no se ha confirmado 1:1** — verificar antes de asumir que ya están cubiertos.

## Cómo usar este informe

1. **Antes de proponer análisis DDD nuevo sobre cualquiera de los 25 "sin dominio"**, confirmar con Arquitectura APB si alguno ya tiene dominio de negocio identificado en otro sitio (Jira, documentación funcional) que no esté todavía reflejado en `apb-domain-catalog` — el catálogo mismo es reciente (una sola sesión de análisis, 30/06/2026) y puede no estar completo.
2. Los 6 de "prioridad alta" son los más baratos de resolver — probablemente ya encajan en un dominio existente, solo falta confirmar y añadir el `related_system`.
3. Los 5 "candidatos no confirmados" ya están en el radar del propio catálogo — coordinarse con quien hizo esa sesión (30/06/2026) antes de re-analizarlos desde cero.
4. Los 19 de "prioridad baja" son el trabajo real pendiente si se quiere cobertura completa del inventario de repos.
