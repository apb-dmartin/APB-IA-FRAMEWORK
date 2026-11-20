---
id: "bc-servicios-auxiliares-cruceros-v1"
name: "Servicios Auxiliares de Cruceros"
description: |
  Servicios en tierra para escalas de cruceros: buses de traslado de pasajeros,
  vigilancia/seguridad en muelle y tarifas asociadas. Descubierto en la auditoría
  de cobertura 2026-07-13 (paquete Struts `serviciosAuxiliares`, sin ticket Jira
  propio).
status: "discovered"
parent_domain: "dom-cruceros-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "CreuerBus"
  - "CreuerVigilancia"
entities:
  - "CreuerBusDetall"
  - "CreuerVigilanciaPunt"
  - "CreuerVigilanciaPuntMoll"
  - "CreuerVigilanciaServei"
  - "CreuerServeiTarifa"
value_objects: []
domain_events:
  - "ServicioBusCruceroAsignado"
  - "ServicioVigilanciaCruceroRegistrado"
ubiquitous_language:
  - term: "Creuer Bus"
    definition: "Servicio de traslado de pasajeros de crucero en bus, con control de ocupación."
  - term: "Punt de Vigilància"
    definition: "Punto de vigilancia/seguridad en muelle asociado a una escala de crucero."
integration_patterns:
  - pattern: "conformist"
    with_context: "bc-cruceros-v1"
    direction: "downstream"
upstream_contexts:
  - "bc-cruceros-v1"
downstream_contexts:
  - "bc-facturacion-v1"
related_systems:
  - "SOSTRAT-Sostrat-MJ8"
tech_stack:
  - ".NET"
  - "Azure SQL"
proposed_date: "2026-07-13"
approved_date: null
source: "auditoria-cobertura-2026-07-13"
notes: "Confirmado import directo de Vaixell/OcupacioMoll desde CreuerEscala.java. Tablas: CREUER_BUS, CREUER_BUS_DETALL, CREUER_VIGILANCIA, CREUER_VIGILANCIA_PUNT, CREUER_VIGILANCIA_PUNT_MOLL, CREUER_VIGILANCIA_SERVEI, CREUER_SERVEI_TARIFA, CREUER_OCUPACIO_BUS. Toca tangencialmente Facturación vía ComprobarFacturasAction (exportación Excel de facturas asociadas)."
---

# Servicios Auxiliares de Cruceros

> **Borrador generado por IA** (APB AI Framework — auditoría de cobertura) — pendiente validación humana. No distribuir sin revisión.

## Responsabilidad

Gestiona los servicios en tierra prestados durante una escala de crucero: buses de traslado de pasajeros (con ocupación), puntos y servicios de vigilancia/seguridad en muelle, y sus tarifas asociadas.

## Lo que NO incluye

No gestiona la escala de crucero en sí (`bc-cruceros-v1`) ni emite la factura final (`bc-facturacion-v1`) — solo genera la base de datos de consumo del servicio auxiliar.

## Modelo de Dominio

- `CreuerBus` (tabla `CREUER_BUS`) + `CreuerBusDetall` (`CREUER_BUS_DETALL`, ocupación).
- `CreuerVigilancia` (`CREUER_VIGILANCIA`) + `CreuerVigilanciaPunt`/`CreuerVigilanciaPuntMoll`/`CreuerVigilanciaServei`.
- `CreuerServeiTarifa` (`CREUER_SERVEI_TARIFA`) — tarifas de los servicios anteriores.

## Relaciones con Otros Bounded Contexts

Downstream de Cruceros (una escala de crucero programa estos servicios). Alimenta a Facturación para la comprobación/exportación de facturas asociadas.

## Implementación Actual

`mvc/control/serviciosAuxiliares/` (`CruceroBusAction`, `CruceroVigilanciaAction`, `TarifasServAuxAction`, `ComprobarFacturasAction`), `service/serviciosAuxiliares/`, `dataaccess/dto/serviciosAuxiliares/`.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-13 | APB AI Framework (auditoría de cobertura) | Propuesta inicial — bounded context descubierto en auditoría de cobertura |
