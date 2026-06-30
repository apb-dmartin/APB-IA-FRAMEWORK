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

## Mapa de dominios de negocio (REVISADO tras entrevista — 15 dominios)

> Versión final tras la entrevista con Débora (ver `interview-questions.md`).
> Materializado en `APB-DOMAIN-CATALOG/domains/` (estado `proposed`).

| # | Dominio | id | Clasif. | Aplicaciones | Confianza | Decisión pendiente |
|---|---|---|---|---|---|---|
| 1 | Escalas Marítimas | `dom-escalas-maritimas-v1` | core | ESC (+ ARGOS, SOSTRAT) | Media | frontera con #2/#4 (experto negocio) |
| 2 | Cruceros | `dom-cruceros-v1` | core | CRE | Media | ¿peer o subdominio de #1? |
| 3 | Gestión de Contenedores | `dom-contenedores-v1` | core | CTA | Alta | sale de SOSTRAT |
| 4 | Líneas Regulares | `dom-lineas-regulares-v1` | core | LRG | Media | ¿subdominio de #1? |
| 5 | Transporte Terrestre | `dom-transporte-terrestre-v1` | core | FER, TRU, PVI, EQV | Media | ¿FER aparte? |
| 6 | Inspección de Mercancías | `dom-inspeccion-mercancias-v1` | supporting | INS, PIF | Media | ¿1 o 2? |
| 7 | Acceso al Recinto | `dom-acceso-recinto-v1` | supporting | AUT | Alta | relación con PVI |
| 8 | Emergencias y Seg. Industrial | `dom-emergencias-v1` | supporting | PEM, HEM | Alta | — |
| 9 | Energía y Suministros | `dom-energia-portuaria-v1` | supporting | MDE, OPS | Media | ¿1 o 2? |
| 10 | Facturación y Tasas | `dom-facturacion-v1` | supporting | P33, P51, REB, RCF | Media | unificar; ¿core? |
| 11 | Administración Electrónica | `dom-administracion-electronica-v1` | supporting | PAD, AGE, GEISER, AEAT | Alta | — |
| 12 | Gestión Corporativa Interna | `dom-corporativo-v1` | generic | MPS, OSMA | Media | identificar GPC/ROSS |
| 13 | GIS y Plano del Puerto | `dom-gis-plano-v1` | supporting | GPS, PLANOLS | Baja | 1 API hoy |
| 14 | Transversal / ARQ | `dom-transversal-arq-v1` | generic | APBAPI-Arq, FLC, GNA, NTA, FEL, SIG, FLU | Alta | shared kernel técnico |
| 15 | Integraciones con Productos de Mercado | `dom-integraciones-mercado-v1` | generic | ROSS, GPC, DGS, ESF, ESM, FLO, IPB, MPA, MST, RESPONSIBLE | Baja | identificar producto de cada API |

> **Cambios vs. mapa inicial:** Escalas y Cruceros separados (antes "Operaciones
> Marítimas"); SOSTRAT **disuelto** (monolito Java → `related_systems`, no dominio);
> Firma integrada en #14 Transversal/ARQ ("varios", respuesta D3); AEAT fusionado en
> #11; nuevo #15 para las APIs de integración desconocidas; #14 formalizado como
> subdominio genérico/técnico (concepto "transversal/ARQ" de APB).

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

Fase 3 — checkpoint humano: entrevista a Débora (ver `interview-questions.md`)
para resolver las decisiones pendientes antes de generar los `dom-*.md`.
