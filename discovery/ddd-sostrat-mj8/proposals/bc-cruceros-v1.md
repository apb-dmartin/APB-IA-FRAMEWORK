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

## ⚠️ Nota crítica (2026-07-14) — implementación .NET ya activa fuera de este documento

Este documento solo cubre el agregado `CreuerEscalaAudit`. **No hay todavía un dossier de aplicación final para `bc-cruceros-v1`.** Una auditoría de consumidores externos (`discovery/ddd-sostrat-mj8/EXTERNAL_CONSUMERS_AUDIT.md §2` fila 8 y §3) confirmó que ya existe un ecosistema .NET real y activo (~3 meses de desarrollo) para la gestión de reservas de atraque de crucero — repos `APB.API.CRE`, `APB.APP.CRE`, `APB.API.VXL`, `APB.API.SLC` (Jenkins `ARQ/TST/SOSTRAT/CRE-Cruceros`) — con su propio modelo (`CreSolicitud`, `CreVaixell`, `CreTerminalBloqueado`, `CreLineaOperativaSolicitud`), API y frontend. Sin solapamiento de datos con `dossier-18-servicios-auxiliares-cruceros.md` (buses/vigilancia es una sub-capacidad distinta), pero **cualquier dossier de aplicación final de `bc-cruceros-v1` que se escriba debe documentar esta implementación ya existente como la realidad operativa del bounded context, no tratarla como trabajo futuro de extracción.**

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
