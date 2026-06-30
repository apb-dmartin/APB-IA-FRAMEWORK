---
id: "ddd-discovery-apim-v1.0"
name: "Discovery DDD — Inventario APIM DOCKS"
description: >-
  Mapa de dominios de negocio candidatos derivado del inventario de APIs DOCKS
  (API_INVENTORY_APIM.md). Salida de la Fase 1-2 del protocolo apb-agent-ddd-v1.0,
  fuentes ["doc","spec"]. Hipótesis de trabajo — pendiente de Fase 3 (checkpoint
  humano / entrevista) y de aprobación de Arquitectura APB.
type: "reference"
source: "apb-agent-ddd-v1.0 (ejecutor: Claude) sobre context/apb/knowledge/API_INVENTORY_APIM.md"
last_updated: "2026-06-30"
status: "draft — pendiente entrevista (Fase 3) + aprobación Arquitectura"
---

# Discovery DDD — Dominios de negocio candidatos (inventario APIM)

> ⚠️ Borrador generado por IA (Claude, Anthropic) — pendiente de validación humana.
> Nivel modelado: **dominio de negocio** únicamente. Los **bounded contexts** se
> difieren a una sesión con acceso a código/BBDD (regla "no inventar sin evidencia").
> Las clasificaciones estratégicas (core/supporting/generic) son hipótesis a confirmar.

## Método

Aplicadas heurísticas de `apb-sub-ddd-spec-v1.0` (agrupar recursos/APIs por área
funcional, prefijos de audiencia como señal de boundary) y `apb-sub-ddd-doc-v1.0`
(lenguaje ubícuo, inconsistencias terminológicas) sobre las ~118 APIs / 36
aplicaciones DOCKS del inventario. El catálogo `domain-catalog/catalog/DOMAINS.md`
está **vacío** → ningún candidato colisiona con dominios existentes (ver
`catalog-comparison.md`).

## Mapa de dominios de negocio (ENRIQUECIDO — 21 dominios)

> Versión final tras la entrevista con Débora (`interview-questions.md`) +
> enriquecimiento con `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (§2-§13),
> que corrigió la hipótesis inicial basada solo en `API_INVENTORY_APIM.md`
> (15 dominios → 21). Materializado en `APB-DOMAIN-CATALOG/domains/` (estado `proposed`).

| # | Dominio | id | Clasif. | Decisión pendiente |
|---|---|---|---|---|
| 1 | Operaciones Marítimas | `dom-operaciones-maritimas-v1` | core | frontera con #2/#3 (experto negocio) |
| 2 | Líneas Regulares | `dom-lineas-regulares-v1` | core | ¿peer o subdominio de #1? |
| 3 | Cruceros | `dom-cruceros-v1` | core | ¿peer o subdominio de #1? |
| 4 | Mercancías (incl. contenedores) | `dom-mercancias-v1` | core | — |
| 5 | Mercancías Peligrosas (MMPP) | `dom-mercancias-peligrosas-v1` | core | — |
| 6 | Concesiones y Ocupaciones | `dom-concesiones-v1` | core | — |
| 7 | Facturación y Tasas | `dom-facturacion-v1` | supporting | unificar P33/P51/REB/RCF |
| 8 | Inspección y Control (INS+PIF+EQV) | `dom-inspeccion-control-v1` | supporting | ¿1 o varios? |
| 9 | Transporte Terrestre | `dom-transporte-terrestre-v1` | supporting | relación con #10 |
| 10 | Ferrocarril Portuario | `dom-ferrocarril-v1` | supporting | ¿dominio propio confirmado? |
| 11 | Suministros a Buques (MDE/OPS/Bunkering/Aiguada) | `dom-suministros-buques-v1` | supporting | ¿1 o 2? |
| 12 | Medio Ambiente y MARPOL | `dom-medio-ambiente-marpol-v1` | supporting | — |
| 13 | Emergencias y Seg. Industrial | `dom-emergencias-v1` | supporting | — |
| 14 | Acceso y Seguridad Física (AUT+PPS) | `dom-acceso-seguridad-fisica-v1` | supporting | relación con PVI |
| 15 | Pesca y Marinas Deportivas | `dom-pesca-marinas-v1` | supporting | — |
| 16 | Estadísticas Portuarias | `dom-estadisticas-v1` | supporting | — |
| 17 | Administración Electrónica | `dom-administracion-electronica-v1` | supporting | — |
| 18 | GIS y Cartografía | `dom-gis-cartografia-v1` | supporting | — |
| 19 | Transversal / ARQ (incl. IAM, SMS/GSM, SIG) | `dom-transversal-arq-v1` | generic | shared kernel técnico |
| 20 | Gestión Corporativa Interna | `dom-corporativo-v1` | generic | identificar GPC/ROSS |
| 21 | Integraciones Externas y EDI (PORTIC/EMSWe/VTS/AIS) | `dom-integraciones-edi-v1` | generic | identificar producto de DGS/ESF/ESM/FLO/IPB/MPA/MST/RESPONSIBLE |

> **Cambios vs. mapa inicial (15 dominios):** se separan como dominios propios
> Concesiones, Mercancías Peligrosas, Medio Ambiente/MARPOL, Pesca y Marinas,
> Estadísticas y Suministros a Buques (antes ausentes o diluidos en "Energía");
> "Gestión de Contenedores" pasa a subdominio de #4 Mercancías; "Acceso al Recinto"
> se fusiona con PPS en #14; **corrección crítica**: SOJA (descarga de granel
> sólido) NO es SMS (envío de SMS corporativo) — error del mapa inicial, corregido
> en `API_INVENTORY_APIM.md` y reflejado en `notes` de #4 y #19; "Integraciones con
> Productos de Mercado" (hipótesis no verificada) se sustituye por #21
> "Integraciones Externas y EDI", basado en evidencia real (PORTIC/EDIFACT, EMSWe,
> VTS Kongsberg, AIS) de la base de conocimiento.

## Señales fuertes detectadas

- **SOSTRAT (66 APIs) no es un dominio** — es un equipo cuyo nombre hereda del
  legacy SÒSTRAT. Probablemente reparte sus APIs entre #1, #2, #3, #4, #5, #6, #7,
  #8, #9. Requiere descomposición en la entrevista.
- **Notificaciones fragmentadas**: GNA + NTA + NOTIFICATION (ARQ) → probable
  candidato a consolidación dentro de #15 (Plataforma).
- **AUT vs PERMIS**: bounded contexts distintos confirmados en el inventario
  (acceso físico al recinto vs. permisos de aplicación DOCKS). AUT → #6; PERMIS → #15.

## APIs sin clasificar (requieren entrevista)

`ROSS`, `GPC`, `DGS`, `ESF`, `ESM`, `FLO`, `IPB`, `MPA`, `MST`, `RESPONSIBLE`,
`APB.API.MIGRACION` (¿herramienta temporal?).

## Próximo paso

`dom-*.md` × 21 generados en `APB-DOMAIN-CATALOG/domains/`. Pendiente: aprobación
de Arquitectura APB vía PR, y resolución por un experto de negocio de las fronteras
Operaciones Marítimas/Líneas Regulares/Cruceros (ver `notes` de cada `domain.md`).
