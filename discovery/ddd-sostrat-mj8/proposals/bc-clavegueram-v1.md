---
id: "bc-clavegueram-v1"
name: "Clavegueram"
description: |
  Liquidación de consumos de alcantarillado (servicio municipal) a usuarios
  del puerto.
status: "discovered"
parent_domain: "dom-clavegueram-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "ClvgConsums"
entities:
  - "ClvgFitxers"
value_objects: []
domain_events:
  - "ConsumClaveguerLiquidado"
ubiquitous_language:
  - term: "Consum"
    definition: "Consumo de alcantarillado facturado a un usuario del puerto."
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
notes: "Pequeño y autocontenido — clasificación 'generic', candidato a externalizarse o sustituirse por un servicio de facturación de utilities genérico en lugar de una extracción DDD dedicada. REPARENTADO 2026-07-11: tras confirmar con el usuario que forzarlo bajo dom-facturacion-v1 era un encaje pobre, se creó dom-clavegueram-v1 como dominio de negocio propio (ver ese fichero para la justificación)."
---

# Clavegueram

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.

## Responsabilidad

Responsable de la liquidación de consumos de alcantarillado (servicio municipal) a usuarios del recinto portuario.

## Lo que NO incluye

No forma parte de la facturación/liquidación portuaria core — es un servicio municipal gestionado dentro de SÒSTRAT por conveniencia histórica.

## Modelo de Dominio

### Aggregates

| Aggregate | Responsabilidad |
|-----------|----------------|
| ClvgConsums | Raíz de agregado del consumo de alcantarillado (tabla `CLVG_CONSUMS`). |

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| ConsumClaveguerLiquidado | emitido | Se ha liquidado un consumo de alcantarillado. |

## Relaciones con Otros Bounded Contexts

Sin acoplamiento detectado a otros dominios de negocio de SÒSTRAT.

## Implementación Actual

Implementado en SÒSTRAT bajo `service/clavegueram/` (6 clases: `CN_Clvg_Consums`, `CN_Clvg_Fitxers`, `CN_LiquidadorConsums`).

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-11 | APB AI Framework (apb-agent-ddd-v1.0) | Propuesta inicial a partir de análisis DDD de SOSTRAT-Sostrat-MJ8 |
