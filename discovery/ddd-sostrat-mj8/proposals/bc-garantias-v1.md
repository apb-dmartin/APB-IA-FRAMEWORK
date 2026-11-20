---
id: "bc-garantias-v1"
name: "Garantias"
description: |
  Gestión de garantías económicas vinculadas a títulos de ocupación/actividad
  portuaria.
status: "discovered"
parent_domain: "dom-concesiones-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates: []
entities:
  - "Garantia"
  - "Evidencia"
  - "GarantiaAudit"
value_objects: []
domain_events:
  - "GarantiaActualizada"
ubiquitous_language:
  - term: "Garantia"
    definition: "Garantía económica asociada a un título."
  - term: "GarantiaEstat"
    definition: "Estado de una garantía en su ciclo de vida."
integration_patterns:
  - pattern: "conformist"
    with_context: "bc-titulo-v1"
    direction: "downstream"
upstream_contexts:
  - "bc-titulo-v1"
downstream_contexts: []
related_systems:
  - "SOSTRAT-Sostrat-MJ8"
tech_stack:
  - ".NET"
  - "Azure SQL"
proposed_date: "2026-07-11"
approved_date: null
source: "apb-sub-ddd-code-v1.0"
notes: "NO tiene identidad de agregado propia en el código actual — depende de IDTITOL (filtra y opera siempre sobre un título). Evaluar en el diseño destino si debe modelarse como entidad dentro de Titulo en lugar de bounded context independiente."
---

# Garantias

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.

## Responsabilidad

Responsable de la gestión de garantías económicas asociadas a un título de ocupación/actividad portuaria: su registro, evidencias documentales y auditoría.

## Lo que NO incluye

No gestiona el título en sí — toda garantía existe en función de un título (`IDTITOL`), sin identidad de agregado propia detectada en el código.

## Modelo de Dominio

### Aggregates

*Sin agregado raíz propio confirmado — pendiente de decisión de diseño (ver nota de "Lo que NO incluye"). Entidades relevantes: Garantia, Evidencia, GarantiaAudit.*

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| GarantiaActualizada | emitido | Se ha actualizado el estado de una garantía. |

## Relaciones con Otros Bounded Contexts

Downstream directo de Título — importa `TitolDades`/`TitolPk` y filtra por `IDTITOL` en toda su lógica.

## Implementación Actual

Implementado en SÒSTRAT bajo `service/gestiogaranties/` (`CN_Garantias_Impl.java`, 811 líneas — el más razonable en tamaño de todo este dominio), `CN_Evidencias_Impl.java`, `CN_GarantiaAudit_Impl.java`.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-11 | APB AI Framework (apb-agent-ddd-v1.0) | Propuesta inicial a partir de análisis DDD de SOSTRAT-Sostrat-MJ8 |
