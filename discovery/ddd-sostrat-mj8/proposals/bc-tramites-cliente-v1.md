---
id: "bc-tramites-cliente-v1"
name: "Trámites de Cliente"
description: |
  Gestión de trámites/gestiones que un cliente inicia ante el puerto (asunto,
  documentación obligatoria por tipo, fechas de creación/lectura/resolución).
  Descubierto en la auditoría de cobertura 2026-07-13 (paquete `carpetaclient`,
  singular — distinto de `carpetaclientes` plural, que es solo portal sin
  modelo de dominio propio).
status: "discovered"
parent_domain: "dom-administracion-electronica-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "TramitClient"
entities: []
value_objects:
  - "TramitClientTipus"
  - "TramitClientEstat"
domain_events:
  - "TramiteClienteIniciado"
  - "TramiteClienteResuelto"
ubiquitous_language:
  - term: "Tràmit"
    definition: "Expediente/gestión que un cliente inicia ante el puerto, con documentación obligatoria según su tipo."
integration_patterns:
  - pattern: "conformist"
    with_context: "bc-operadores-portuarios-v1"
    direction: "downstream"
upstream_contexts:
  - "bc-operadores-portuarios-v1"
downstream_contexts: []
related_systems:
  - "SOSTRAT-Sostrat-MJ8"
tech_stack:
  - ".NET"
  - "Azure SQL"
proposed_date: "2026-07-13"
approved_date: null
source: "auditoria-cobertura-2026-07-13"
notes: "El paquete 'carpetaclientes' (plural, 9 Actions *CCAction) NO se modela como BC — confirmado que solo extiende Actions ya existentes de Facturación/Liquidación (FacturasCCAction extends FacturasAction, etc.) sin DTOs ni tablas propias, es una capa de portal de autoservicio, no un dominio nuevo. Añadida como nota en bc-facturacion-v1, no como BC separado."
---

# Trámites de Cliente

> **Borrador generado por IA** (APB AI Framework — auditoría de cobertura) — pendiente validación humana. No distribuir sin revisión.

## Responsabilidad

Gestiona los trámites/gestiones que un cliente (operador portuario) inicia ante el puerto: asunto, datos adicionales, documentación obligatoria por tipo de trámite, fechas de creación/lectura/resolución.

## Lo que NO incluye

No incluye el portal de autoservicio de facturas/liquidaciones (paquete `carpetaclientes`, plural) — esa capa reutiliza directamente `bc-facturacion-v1`/`bc-liquidacion-v1` sin aportar modelo de dominio propio, no se migra como bounded context independiente.

## Modelo de Dominio

`TramitClient` (tabla `TRAMIT_CLIENT`) + `TramitClientTipus`/`TramitClientEstat` (tablas `TRAMIT_CLIENT_TIPUS`/`TRAMIT_CLIENT_ESTAT`).

## Relaciones con Otros Bounded Contexts

Downstream de Operadores Portuarios (el trámite lo inicia un `Usuari`/tercero).

## Implementación Actual

`mvc/control/carpetaclient/TramitClientAction.java`, `service/carpetaclient/CN_TramitClient*.java`, `dataaccess/dto/TramitClient.java`.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-13 | APB AI Framework (auditoría de cobertura) | Propuesta inicial — bounded context descubierto en auditoría de cobertura |
