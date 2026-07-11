---
id: "bc-mano-estiba-v1"
name: "ManoDeEstiba"
description: |
  Gestión de la contratación, comandas y operativa del personal de estiba
  portuaria.
status: "discovered"
parent_domain: "dom-mano-estiba-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "MaestContractacio"
entities:
  - "MaestComanda"
  - "MaestOperativa"
  - "MaestEspecialitat"
  - "MaestEquip"
value_objects: []
domain_events:
  - "ContratacionRegistrada"
  - "ComandaAsignada"
ubiquitous_language:
  - term: "Contractació"
    definition: "Contratación de personal de estiba."
  - term: "Comanda"
    definition: "Comanda/pedido de personal de estiba para una operativa concreta."
integration_patterns:
  - pattern: "open-host"
    with_context: "servicio-externo-mst"
    direction: "upstream"
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
notes: "CANDIDATO A EXTRACCIÓN TEMPRANA (ver decomposition-roadmap.md Fase 1). Ya existe un microservicio externo 'MST' (Mano de Estiba) referenciado desde ticketgranting-api-client — evidencia de strangler fig ya en marcha antes de este análisis formal. Sin acoplamiento detectado a otros dominios de negocio. REPARENTADO 2026-07-11: tras confirmar con el usuario que forzarlo bajo dom-transporte-terrestre-v1 era un encaje pobre, se creó dom-mano-estiba-v1 como dominio de negocio propio (ver ese fichero para la justificación)."
---

# ManoDeEstiba

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.

## Responsabilidad

Responsable de la contratación, comandas y operativa del personal de estiba portuaria (estibadores).

## Lo que NO incluye

No gestiona el transporte terrestre ni los accesos físicos al puerto (aunque comparte dominio de negocio con ellos por el eje "movimiento/operación en muelle").

## Modelo de Dominio

### Aggregates

| Aggregate | Responsabilidad |
|-----------|----------------|
| MaestContractacio | Raíz de agregado de la contratación de personal de estiba. |

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| ContratacionRegistrada | emitido | Se ha registrado una contratación. |
| ComandaAsignada | emitido | Se ha asignado una comanda de personal. |

## Relaciones con Otros Bounded Contexts

Sin acoplamiento detectado a otros dominios de negocio de SÒSTRAT. Ya delega parcialmente en un microservicio externo ("MST") referenciado desde la API gateway de ticket-granting — es, junto con Ferrocarril Portuario, el bounded context con mayor madurez de extracción ya alcanzada.

## Implementación Actual

Implementado en SÒSTRAT bajo `service/manoEstiba/CN_ManoEstiba.java` + impl, `mvc/control/manoEstiba/ManoEstibaAction.java`, ~20 DTOs en `dataaccess/dto/manoEstiba/`. El microservicio externo "MST" se referencia desde `ticketgranting-api-client/README.md`.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-11 | APB AI Framework (apb-agent-ddd-v1.0) | Propuesta inicial a partir de análisis DDD de SOSTRAT-Sostrat-MJ8 |
