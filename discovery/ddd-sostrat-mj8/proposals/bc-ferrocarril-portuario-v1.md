---
id: "bc-ferrocarril-portuario-v1"
name: "FerrocarrilPortuario"
description: |
  Gestión del tráfico ferroviario portuario asociado a las escalas: operaciones
  ferroviarias, vías, maniobras y control de contenedores por ferrocarril.
status: "discovered"
parent_domain: "dom-ferrocarril-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "OperacioFerroviaria"
entities:
  - "Via"
  - "Maniobra"
value_objects: []
domain_events:
  - "OperacionFerroviariaRegistrada"
  - "OperacionFerroviariaAnulada"
ubiquitous_language:
  - term: "Via"
    definition: "Vía ferroviaria portuaria, con sus ocupaciones y segmentos."
  - term: "Maniobra"
    definition: "Movimiento ferroviario dentro del recinto portuario."
integration_patterns:
  - pattern: "conformist"
    with_context: "bc-escalas-v1"
    direction: "downstream"
  - pattern: "open-host"
    with_context: "servicio-externo-ferrocarril-camaras"
    direction: "upstream"
upstream_contexts:
  - "bc-escalas-v1"
downstream_contexts: []
related_systems:
  - "SOSTRAT-Sostrat-MJ8"
tech_stack:
  - ".NET"
  - "Azure SQL"
  - "Azure API Management"
proposed_date: "2026-07-11"
approved_date: null
source: "apb-sub-ddd-code-v1.0"
notes: "CANDIDATO A PRIMERA EXTRACCIÓN (quick win, ver decomposition-roadmap.md Fase 1). Ya existe un cliente Swagger (OpFerroviariaApi, CameraPassTrainsApi) consumiendo parte de la funcionalidad desde un servicio externo — evidencia de strangler fig ya en marcha antes de este análisis. No se encontró paquete/término independiente para 'ESCAIIB' de la hipótesis Jira original."
---

# FerrocarrilPortuario

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.

## Responsabilidad

Responsable de la gestión del tráfico ferroviario dentro del recinto portuario: operaciones, vías, maniobras y su relación con la escala del buque.

## Lo que NO incluye

No gestiona los datos generales de la escala del buque — solo referencia su identificador (`EscalaPk`).

## Modelo de Dominio

### Aggregates

| Aggregate | Responsabilidad |
|-----------|----------------|
| OperacioFerroviaria | Operación ferroviaria vinculada a una escala. |

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| OperacionFerroviariaRegistrada | emitido | Se ha registrado una operación ferroviaria. |
| OperacionFerroviariaAnulada | emitido | Se ha anulado una operación ferroviaria previamente registrada. |

## Relaciones con Otros Bounded Contexts

Downstream (conformist) de Escalas vía `EscalaPk`. Ya consume un servicio externo (open-host) para parte de su funcionalidad (control de trenes/cámaras), evidencia de que la extracción ya está en marcha orgánicamente.

## Implementación Actual

Implementado en SÒSTRAT bajo `service/ferrocarril/` (34 interfaces `CN_*`), `mvc/control/ferrocarril/EscalasFerroviariasAction.java` (3.530 líneas), con parte de la funcionalidad ya delegada a un servicio externo vía `swagger/fer/client/api/OpFerroviariaApi.java` y `CameraPassTrainsApi.java`. Por tamaño y acoplamiento mínimo, es el candidato recomendado para la primera extracción formal del roadmap.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-11 | APB AI Framework (apb-agent-ddd-v1.0) | Propuesta inicial a partir de análisis DDD de SOSTRAT-Sostrat-MJ8 |
