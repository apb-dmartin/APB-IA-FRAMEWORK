---
id: "dom-clavegueram-v1"
name: "Clavegueram"
description: |
  Liquidación de consumos de alcantarillado (servicio municipal) a usuarios
  del puerto. Capacidad de facturación de un suministro específico, distinta
  de las tasas/tarifas portuarias (T0-T5) que cubre el dominio Facturación.
status: "discovered"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
subdomains:
  - "Liquidación de consumos de alcantarillado"
bounded_contexts:
  - "bc-clavegueram-v1"
related_systems:
  - "SOSTRAT-Sostrat-MJ8 (service/clavegueram/)"
strategic_classification: "generic"
ubiquitous_language:
  - term: "Consum"
    definition: "Consumo de alcantarillado facturado a un usuario del puerto."
proposed_date: "2026-07-11"
approved_date: null
source: "apb-agent-ddd-v1.0"
notes: "Creado 2026-07-11 tras confirmar con el usuario que forzar este bounded context bajo dom-facturacion-v1 era un encaje conceptual pobre — aunque es facturación, es facturación de un suministro municipal (alcantarillado) a usuarios del puerto, no una tasa/tarifa portuaria (T0-T5) como las que cubre dom-facturacion-v1. Tampoco encaja en dom-corporativo-v1 (definido como 'no ligado a la operativa portuaria'), porque Clavegueram factura a usuarios externos del puerto, no es gasto interno corporativo. Ninguno de los 21 dominios del catálogo original lo menciona — hallazgo exclusivo de este análisis de código. Clasificado 'generic' (commodity, candidato a externalizarse a un proveedor de facturación de utilities) igual que se hizo con dom-pesca-marinas-v1."
---

# Clavegueram

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.

## Descripción

Dominio de la liquidación de consumos de alcantarillado (servicio municipal) a usuarios del recinto portuario.

## Motivación

Identificado en el análisis de código de SÒSTRAT (`service/clavegueram/`) sin equivalente en el catálogo de dominios existente. Se propone como dominio propio en lugar de forzarlo bajo Facturación (tasas/tarifas portuarias T0-T5) o Corporativo (gasto interno no operativo) — ninguno de los dos encaja: es facturación de un suministro municipal específico a usuarios externos del puerto.

## Bounded Contexts Identificados

- **Clavegueram** (`bc-clavegueram-v1`) — liquidación de consumos de alcantarillado.

## Relación con Otros Dominios

Ninguna dependencia de código detectada hacia otros dominios de SÒSTRAT.

## Sistemas Actuales

`service/clavegueram/` en SÒSTRAT (6 clases, tabla `CLVG_CONSUMS`).

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-11 | APB AI Framework (apb-agent-ddd-v1.0) | Propuesta inicial, tras confirmar con el usuario que merece dominio propio en vez de reparenting forzado |
