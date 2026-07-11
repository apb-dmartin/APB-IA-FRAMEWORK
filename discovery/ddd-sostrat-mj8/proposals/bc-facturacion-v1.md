---
id: "bc-facturacion-v1"
name: "Facturacion"
description: |
  Emisión de facturas (estándar y Facturae/firma XML) a partir de liquidaciones
  y recibos, incluyendo suministros facturables, peticiones FBD y vehículos
  abandonados.
status: "discovered"
parent_domain: "dom-facturacion-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "Factura"
entities:
  - "Rebut"
value_objects: []
domain_events:
  - "FacturaEmitida"
  - "FacturaEdiGenerada"
ubiquitous_language:
  - term: "Factura"
    definition: "Documento de facturación emitido, en formato estándar o Facturae."
  - term: "Rebut"
    definition: "Recibo asociado a facturación estándar."
  - term: "Lot de Facturació"
    definition: "Lote de facturación agrupando varias facturas para su procesamiento conjunto."
integration_patterns:
  - pattern: "ACL"
    with_context: "bc-liquidacion-v1"
    direction: "downstream"
upstream_contexts:
  - "bc-liquidacion-v1"
downstream_contexts: []
related_systems:
  - "SOSTRAT-Sostrat-MJ8"
tech_stack:
  - ".NET"
  - "Azure SQL"
proposed_date: "2026-07-11"
approved_date: null
source: "apb-sub-ddd-code-v1.0"
notes: "Comparte utilidades base con Liquidación (LiquidacionGenericDependenciasUtil) — acoplamiento a resolver antes de extracción independiente."
---

# Facturacion

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.

## Responsabilidad

Responsable de la emisión de facturas (estándar y electrónicas Facturae) a partir de liquidaciones, así como de la gestión de recibos, suministros facturables y procesos asociados (peticiones FBD, vehículos abandonados, marinas).

## Lo que NO incluye

No calcula el importe a liquidar (eso es responsabilidad de Liquidación); Facturación consume liquidaciones ya calculadas.

## Modelo de Dominio

### Aggregates

| Aggregate | Responsabilidad |
|-----------|----------------|
| Factura | Raíz de agregado del documento de facturación. |

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| FacturaEmitida | emitido | Se ha emitido una factura. |
| FacturaEdiGenerada | emitido | Se ha generado una factura vía circuito EDI (proceso batch). |

## Relaciones con Otros Bounded Contexts

Downstream de Liquidación, de la que consume los importes a facturar. Requiere anti-corruption layer para desacoplar la dependencia actual de `LiquidacionGenericDependenciasUtil`.

## Implementación Actual

Implementado en SÒSTRAT bajo `service/facturas/` (23 clases + ~90 de Facturae/firma XML) y `service/factestandar/` (subdominios `rebuts`, `peticiofbd`, `suministros`, `vehiclesAbandonats`, `marinas`). God class: `CN_Facturas_Impl.java` (2.111 líneas). El circuito de facturación EDI también se ejecuta vía batch (`FacturacionEDITasklet.java` en `sostrat-BATCH`).

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-11 | APB AI Framework (apb-agent-ddd-v1.0) | Propuesta inicial a partir de análisis DDD de SOSTRAT-Sostrat-MJ8 |
