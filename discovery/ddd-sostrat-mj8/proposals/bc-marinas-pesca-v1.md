---
id: "bc-marinas-pesca-v1"
name: "MarinasPesca"
description: |
  Gestión de marinas deportivas (atraques, liquidación anual) y de la actividad
  pesquera (albaranes de descarga). Separado de Aguada tras reparentar contra el
  catálogo real de dominios (dom-pesca-marinas-v1 agrupa Marinas+Pesca como
  dominio propio, clasificado generic, distinto de Suministros a Buques).
status: "discovered"
parent_domain: "dom-pesca-marinas-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "MarinaDadesAtracada"
  - "Albara"
entities:
  - "MarinaLiquidacioAny"
value_objects: []
domain_events:
  - "AtracadaMarinaRegistrada"
  - "AlbaranPescaImportado"
ubiquitous_language:
  - term: "Marina"
    definition: "Marina deportiva, con sus datos de atraque y liquidación anual."
  - term: "Albarà"
    definition: "Albarán de descarga de actividad pesquera."
integration_patterns: []
upstream_contexts: []
downstream_contexts: []
related_systems:
  - "SOSTRAT-Sostrat-MJ8"
tech_stack:
  - ".NET"
  - "Azure SQL"
proposed_date: "2026-07-11"
approved_date: null
source: "apb-sub-ddd-code-v1.0"
notes: "REPARENTADO 2026-07-11 de un bounded context inventado (bc-servicios-auxiliares-buque-v1) a dom-pesca-marinas-v1, el dominio real ya existente en el catálogo (clasificado 'generic', agrupa Marinas y Pesca como actividad no comercial-carga — nota propia del dominio: 'a validar si deben separarse'). A diferencia de Aguada, ni Marinas ni Pesca muestran acoplamiento a Escalas en el código (sin import de dataaccess.dto.escalas)."
---

# MarinasPesca

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.

## Responsabilidad

Responsable de la gestión de atraques en marinas deportivas (con su liquidación anual) y de los albaranes de descarga de actividad pesquera.

## Lo que NO incluye

No incluye Aguada (bounded context separado, `bc-aguada-v1`, bajo `dom-suministros-buques-v1`).

## Modelo de Dominio

### Aggregates

| Aggregate | Responsabilidad |
|-----------|----------------|
| MarinaDadesAtracada | Atraque de una embarcación en marina deportiva (tabla `MARINA_DADES_ATRACADA`). |
| Albara | Albarán de descarga de actividad pesquera (tabla `ALBARA`). |

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| AtracadaMarinaRegistrada | emitido | Se ha registrado un atraque en marina deportiva. |
| AlbaranPescaImportado | emitido | Se ha importado un albarán de pesca. |

## Relaciones con Otros Bounded Contexts

Sin acoplamiento detectado a otros dominios de negocio de SÒSTRAT — el propio catálogo marca este dominio como pendiente de validar si Marinas y Pesca deben separarse en dos dominios distintos.

## Implementación Actual

Implementado en SÒSTRAT bajo `service/factestandar/marinas/` (`MarinaDadesAtracada.java`) y `service/gpesca/` (`Albara.java`/`AlbaraBase.java`, tabla `ALBARA`).

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-11 | APB AI Framework (apb-agent-ddd-v1.0) | Propuesta inicial, como parte de bc-servicios-auxiliares-buque-v1 |
| 1.1.0 | 2026-07-11 | APB AI Framework (apb-agent-ddd-v1.0) | Separado como bounded context propio y reparentado a dom-pesca-marinas-v1 (dominio real del catálogo) |
