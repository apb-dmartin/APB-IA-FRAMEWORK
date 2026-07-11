---
id: "bc-cruceros-v1"
name: "Cruceros"
description: |
  Gestión específica de escalas de buques de crucero, incluyendo auditoría de
  la escala de crucero y datos de pasajeros asociados.
status: "discovered"
parent_domain: "dom-cruceros-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "CreuerEscalaAudit"
entities: []
value_objects: []
domain_events:
  - "EscalaCruceroAuditada"
ubiquitous_language:
  - term: "Creuer"
    definition: "Buque de crucero."
integration_patterns:
  - pattern: "conformist"
    with_context: "bc-escalas-v1"
    direction: "downstream"
upstream_contexts:
  - "bc-escalas-v1"
downstream_contexts: []
related_systems:
  - "SOSTRAT-Sostrat-MJ8"
tech_stack:
  - ".NET"
  - "Azure SQL"
proposed_date: "2026-07-11"
approved_date: null
source: "apb-sub-ddd-code-v1.0"
notes: "Ya semi-diferenciado en el código actual (paquete propio dataaccess/dto/cruceros/). Expuesto también vía servicio SOAP CrucerosWSPort en sostratWSCXF."
---

# Cruceros

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.

## Responsabilidad

Responsable de la gestión específica de escalas de cruceros: auditoría de la escala y datos asociados a la actividad de cruceros.

## Lo que NO incluye

No gestiona los datos generales de la escala (buque, atraque) — eso pertenece a Escalas; Cruceros es un contexto downstream que añade información específica del segmento crucero.

## Modelo de Dominio

### Aggregates

| Aggregate | Responsabilidad |
|-----------|----------------|
| CreuerEscalaAudit | Auditoría de la escala de crucero. |

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| EscalaCruceroAuditada | emitido | Se ha auditado una escala de crucero. |

## Relaciones con Otros Bounded Contexts

Downstream (conformist) de Escalas.

## Implementación Actual

Implementado en SÒSTRAT bajo `dataaccess/dto/cruceros/CreuerEscalaAudit.java` y expuesto también mediante el servicio SOAP `CrucerosWSPort` (`sostratWSCXF`), con operaciones `getCruceros`, `getCrucerosAmarrados`, `getCruceroDetalle`, `getBuques`, `getEscalas`.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-11 | APB AI Framework (apb-agent-ddd-v1.0) | Propuesta inicial a partir de análisis DDD de SOSTRAT-Sostrat-MJ8 |
