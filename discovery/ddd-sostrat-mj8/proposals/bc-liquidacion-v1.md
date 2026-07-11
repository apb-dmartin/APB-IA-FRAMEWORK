---
id: "bc-liquidacion-v1"
name: "Liquidacion"
description: |
  Cálculo y gestión de liquidaciones de tasas portuarias y otros conceptos
  facturables, a partir de hechos imponibles generados en Escalas, Título,
  Manifiestos, Depotsis y Suministros.
status: "discovered"
parent_domain: "dom-facturacion-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "Liquidacio"
entities:
  - "LiquidacioLinia"
value_objects: []
domain_events:
  - "LiquidacionGenerada"
  - "LiquidacionAceptada"
  - "LiquidacionAnulada"
ubiquitous_language:
  - term: "Liquidació"
    definition: "Cálculo y registro de un importe a cobrar/pagar."
  - term: "LiquidacioLinia"
    definition: "Línea de detalle de una liquidación."
integration_patterns:
  - pattern: "shared-kernel"
    with_context: "bc-titulo-v1"
    direction: "bidirectional"
  - pattern: "conformist"
    with_context: "bc-escalas-v1"
    direction: "downstream"
  - pattern: "conformist"
    with_context: "bc-manifiestos-v1"
    direction: "downstream"
  - pattern: "conformist"
    with_context: "bc-depotsis-v1"
    direction: "downstream"
  - pattern: "ACL"
    with_context: "bc-facturacion-v1"
    direction: "upstream"
upstream_contexts:
  - "bc-escalas-v1"
  - "bc-titulo-v1"
  - "bc-manifiestos-v1"
  - "bc-depotsis-v1"
downstream_contexts:
  - "bc-facturacion-v1"
related_systems:
  - "SOSTRAT-Sostrat-MJ8"
tech_stack:
  - ".NET"
  - "Azure SQL"
  - "Azure Service Bus"
proposed_date: "2026-07-11"
approved_date: null
source: "apb-sub-ddd-code-v1.0"
notes: "HUB DE MAYOR ACOPLAMIENTO DEL SISTEMA. 13 clases *Dependencias_Impl detectadas; escritura directa confirmada en tabla TITOL_MINIM_DADES desde CN_Liquidacion_Impl.java:434. Última fase de extracción del roadmap (Fase 4) — requiere sustituir escrituras cruzadas por eventos de dominio antes de extraerse."
---

# Liquidacion

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.

## Responsabilidad

Responsable de calcular y gestionar liquidaciones de tasas y conceptos portuarios facturables, a partir de hechos imponibles originados en otros dominios (escalas, títulos, manifiestos, depósitos, suministros).

## Lo que NO incluye

No emite la factura final (eso es responsabilidad de Facturación) ni gestiona el título en sí (solo lo referencia).

## Modelo de Dominio

### Aggregates

| Aggregate | Responsabilidad |
|-----------|----------------|
| Liquidacio | Raíz de agregado de la liquidación, con sus líneas de detalle. |

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| LiquidacionGenerada | emitido | Se ha generado una nueva liquidación. |
| LiquidacionAceptada | emitido | La liquidación ha sido aceptada. |
| LiquidacionAnulada | emitido | La liquidación ha sido anulada. |

## Relaciones con Otros Bounded Contexts

Es el contexto con más dependencias del sistema: consume datos de Escalas, Título, Manifiestos y Depotsis (patrón shared-kernel de facto con Título, por las escrituras cruzadas detectadas) y alimenta a Facturación. **Requiere anti-corruption layer antes de extraerse**, dado que hoy escribe directamente en tablas propiedad de Título.

## Implementación Actual

Implementado en SÒSTRAT bajo `service/liquidacion/` (28 clases), con `CN_Liquidacion_Impl.java` (2.057 líneas) y `CN_LiqLC_Impl.java` (+3.600 líneas) como god classes. 13 clases `*Dependencias_Impl` codifican explícitamente las dependencias cruzadas con Escalas, Marina, Manifest, Depotsis, Suministros Buques/Fijas y Título.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-11 | APB AI Framework (apb-agent-ddd-v1.0) | Propuesta inicial a partir de análisis DDD de SOSTRAT-Sostrat-MJ8 |
