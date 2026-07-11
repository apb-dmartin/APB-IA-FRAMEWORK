---
id: "bc-pif-v1"
name: "Pif"
description: |
  Control fronterizo/aduanero de mercancías en muelle (SCPP — posicionamiento
  de contenedores para inspección aduanera).
status: "discovered"
parent_domain: "dom-inspeccion-control-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "Pif"
entities:
  - "AreaPif"
  - "OperacioPif"
  - "MollsPIF"
value_objects: []
domain_events:
  - "OperacionPifRegistrada"
ubiquitous_language:
  - term: "PIF"
    definition: "Puesto de Inspección Fronteriza; también SCPP — posicionamiento de contenedores para inspección aduanera."
  - term: "Àrea PIF"
    definition: "Área física destinada a inspección fronteriza."
integration_patterns:
  - pattern: "ACL"
    with_context: "bc-datos-maestros-equipamiento-v1"
    direction: "upstream"
upstream_contexts:
  - "bc-datos-maestros-equipamiento-v1"
downstream_contexts: []
related_systems:
  - "SOSTRAT-Sostrat-MJ8"
tech_stack:
  - ".NET"
  - "Azure SQL"
proposed_date: "2026-07-11"
approved_date: null
source: "apb-sub-ddd-code-v1.0"
notes: "Confirma la hipótesis Jira. Naturaleza regulatoria distinta de MMPP — se mantiene como bounded context separado pese a cierta cercanía temática."
---

# Pif

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.

## Responsabilidad

Responsable del control fronterizo/aduanero de mercancías: gestión de áreas de inspección física en muelle y sus operaciones asociadas.

## Lo que NO incluye

No gestiona mercancías peligrosas (eso es MMPP) ni el manifiesto en sí (eso es Manifiestos), aunque coordina con ambos.

## Modelo de Dominio

### Aggregates

| Aggregate | Responsabilidad |
|-----------|----------------|
| Pif | Raíz de agregado del puesto de inspección fronteriza. |

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| OperacionPifRegistrada | emitido | Se ha registrado una operación de inspección fronteriza. |

## Relaciones con Otros Bounded Contexts

Consumirá el futuro servicio de Datos Maestros de Equipamiento para identificar los contenedores inspeccionados.

## Implementación Actual

Implementado en SÒSTRAT bajo `service/pif/` (`CN_Pif.java`, `CN_AreaPif.java`, `CN_OperacioPif.java`, `CN_MollsPIF.java`, `FileXMLVUA.java`).

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-11 | APB AI Framework (apb-agent-ddd-v1.0) | Propuesta inicial a partir de análisis DDD de SOSTRAT-Sostrat-MJ8 |
