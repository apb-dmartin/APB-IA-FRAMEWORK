---
id: "bc-depotsis-v1"
name: "Depotsis"
description: |
  Gestión del depósito en muelle libre T6: solicitudes y operaciones de
  desconsolidación de mercancías.
status: "discovered"
parent_domain: "dom-mercancias-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "DepotsisSolicitud"
entities:
  - "DepotsisOperacion"
  - "DepotsisSolicitudVersio"
value_objects: []
domain_events:
  - "SolicitudDepotsisRegistrada"
ubiquitous_language:
  - term: "Solicitud"
    definition: "Solicitud de depósito en muelle libre T6."
  - term: "Operació"
    definition: "Operación de desconsolidación asociada a una solicitud."
integration_patterns:
  - pattern: "ACL"
    with_context: "bc-datos-maestros-equipamiento-v1"
    direction: "upstream"
  - pattern: "conformist"
    with_context: "bc-liquidacion-v1"
    direction: "downstream"
upstream_contexts:
  - "bc-datos-maestros-equipamiento-v1"
downstream_contexts:
  - "bc-liquidacion-v1"
related_systems:
  - "SOSTRAT-Sostrat-MJ8"
tech_stack:
  - ".NET"
  - "Azure SQL"
proposed_date: "2026-07-11"
approved_date: null
source: "apb-sub-ddd-code-v1.0"
notes: "El bounded context más aislado del clúster de Mercancías y Aduanas — struts-config propio, único acoplamiento detectado es la lectura del dato maestro de Equipamiento. Buen candidato de extracción temprana (ver decomposition-roadmap.md Fase 1)."
---

# Depotsis

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.

## Responsabilidad

Responsable de la gestión de solicitudes y operaciones de depósito en muelle libre T6, incluyendo la desconsolidación de mercancías.

## Lo que NO incluye

No gestiona el manifiesto original de la mercancía (eso es Manifiestos) ni el control aduanero (eso es PIF/Aduanas).

## Modelo de Dominio

### Aggregates

| Aggregate | Responsabilidad |
|-----------|----------------|
| DepotsisSolicitud | Raíz de agregado de la solicitud de depósito en muelle libre. |

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| SolicitudDepotsisRegistrada | emitido | Se ha registrado una nueva solicitud de depósito. |

## Relaciones con Otros Bounded Contexts

Consumirá el futuro servicio de Datos Maestros de Equipamiento; alimenta a Liquidación.

## Implementación Actual

Implementado en SÒSTRAT bajo `service/depotsis/CN_Depotsis.java`, con `struts-config-depotsis.xml` propio — el módulo mejor delimitado de todo el clúster de Mercancías y Aduanas.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-11 | APB AI Framework (apb-agent-ddd-v1.0) | Propuesta inicial a partir de análisis DDD de SOSTRAT-Sostrat-MJ8 |
