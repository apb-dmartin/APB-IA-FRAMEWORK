---
id: "bc-pps-v1"
name: "PasesYPermisos"
description: |
  Gestión de solicitudes, autorizaciones, tarjetas y permisos de acceso al
  recinto portuario.
status: "discovered"
parent_domain: "dom-acceso-seguridad-fisica-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "Solicitud"
entities:
  - "Autoritzacio"
  - "Targeta"
  - "Permis"
value_objects: []
domain_events:
  - "SolicitudRegistrada"
  - "TarjetaCaducadaDetectada"
ubiquitous_language:
  - term: "Sol·licitud"
    definition: "Solicitud de pase o permiso de acceso al recinto portuario."
  - term: "Targeta"
    definition: "Tarjeta de acceso físico."
integration_patterns:
  - pattern: "open-host"
    with_context: "sistema-externo-kaba-portic"
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
notes: "Sin acoplamiento detectado a Escalas (a diferencia de otros dominios supporting) — gira en torno a persona/vehículo/tarjeta. Integra con conectores externos Kaba y PortIC."
---

# PasesYPermisos

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.

## Responsabilidad

Responsable de la gestión de solicitudes, autorizaciones, tarjetas y permisos de acceso físico al recinto portuario.

## Lo que NO incluye

No gestiona el transporte terrestre de mercancías (eso es Transporte Terrestre), aunque ambos comparten el eje de "acceso/movimiento físico".

## Modelo de Dominio

### Aggregates

| Aggregate | Responsabilidad |
|-----------|----------------|
| Solicitud | Raíz de agregado de la solicitud de pase/permiso (tabla `SOLICITUD`). |

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| SolicitudRegistrada | emitido | Se ha registrado una nueva solicitud. |
| TarjetaCaducadaDetectada | emitido | Se ha detectado una tarjeta caducada (proceso batch). |

## Relaciones con Otros Bounded Contexts

Sin acoplamiento a otros dominios de negocio de SÒSTRAT. Integra con conectores externos: `CN_KabaConnector.java`, `CN_PorticConnector.java`, `CN_GPCNConnector.java`.

## Implementación Actual

Implementado en SÒSTRAT bajo `service/pps/` (`CN_Autoritzacio`, `CN_Solicituds`, `CN_Targetas`, `CN_Permis`, `CN_DocumentSolicitud`). God classes: `CN_Solicituds_Impl.java` (2.200 líneas) y `mvc/control/pps/TarjetasPasesAction.java` (2.647 líneas).

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-11 | APB AI Framework (apb-agent-ddd-v1.0) | Propuesta inicial a partir de análisis DDD de SOSTRAT-Sostrat-MJ8 |
