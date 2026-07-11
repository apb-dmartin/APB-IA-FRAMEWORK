---
id: "bc-manifiestos-v1"
name: "Manifiestos"
description: |
  Gestión de manifiestos de mercancías y sus partidas, incluyendo conocimientos
  de embarque y tramos. Es el equivalente real de la hipótesis Jira "MERC".
status: "discovered"
parent_domain: "dom-mercancias-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "Manifest"
entities:
  - "Partida"
  - "PartidaVersio"
  - "Coneixement"
  - "Tramo"
value_objects: []
domain_events:
  - "ManifiestoRegistrado"
  - "ManifiestoCircuitoProcesado"
  - "PartidaActualizada"
ubiquitous_language:
  - term: "Manifest"
    definition: "Manifiesto de mercancías de una escala."
  - term: "Partida"
    definition: "Línea/partida de un manifiesto."
  - term: "Coneixement"
    definition: "Conocimiento de embarque asociado a una partida."
integration_patterns:
  - pattern: "ACL"
    with_context: "bc-datos-maestros-equipamiento-v1"
    direction: "upstream"
  - pattern: "conformist"
    with_context: "bc-mmpp-v1"
    direction: "bidirectional"
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
  - "Azure Service Bus"
proposed_date: "2026-07-11"
approved_date: null
source: "apb-sub-ddd-code-v1.0"
notes: "CORRIGE HIPÓTESIS: no existe paquete 'merc'; el nombre real en código es 'manifiestos'. Contiene las mayores god classes de todo el sistema (CN_Manifest_Impl: 3.929 líneas; CN_Partida_Impl: 3.338 líneas) — requiere refactor interno antes de extraerse (ver decomposition-roadmap.md Fase 3)."
---

# Manifiestos

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.

## Responsabilidad

Responsable de la gestión de manifiestos de mercancías, sus partidas, conocimientos de embarque y tramos, incluyendo su circuito EDI de procesamiento.

## Lo que NO incluye

No gestiona mercancías peligrosas de forma independiente (aunque referencia MMPP vía `PartidaMmppDTO`), ni el cálculo de liquidaciones asociadas.

## Modelo de Dominio

### Aggregates

| Aggregate | Responsabilidad |
|-----------|----------------|
| Manifest | Raíz de agregado del manifiesto de mercancías. |

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| ManifiestoRegistrado | emitido | Se ha registrado un nuevo manifiesto. |
| ManifiestoCircuitoProcesado | emitido | El circuito EDI del manifiesto se ha procesado (batch). |
| PartidaActualizada | emitido | Se ha actualizado una partida del manifiesto. |

## Relaciones con Otros Bounded Contexts

Consume el futuro servicio de Datos Maestros de Equipamiento; tiene dependencia bidireccional con MMPP (`CN_PartidaMmpp.java` vive hoy en este paquete pero modela un concepto MMPP); alimenta a Liquidación.

## Implementación Actual

Implementado en SÒSTRAT bajo `service/manifiestos/gestion/`. Contiene las god classes más grandes de todo el sistema: `CN_Manifest_Impl.java` (3.929 líneas) y `CN_Partida_Impl.java` (3.338 líneas). El circuito EDI se procesa también vía batch (`LanzarCircuitoManifiestosTasklet.java`).

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-11 | APB AI Framework (apb-agent-ddd-v1.0) | Propuesta inicial a partir de análisis DDD de SOSTRAT-Sostrat-MJ8 |
