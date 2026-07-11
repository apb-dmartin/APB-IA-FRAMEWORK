---
id: "bc-mmpp-v1"
name: "MercanciasPeligrosas"
description: |
  Gestión de autorizaciones, notificaciones e inspecciones de mercancías
  peligrosas (MMPP), con circuito EDI propio.
status: "discovered"
parent_domain: "dom-mercancias-peligrosas-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "MmppAutoritzacio"
  - "MmppNotif"
entities:
  - "MmppNotifPartida"
  - "MmppNotifEquipament"
  - "MmppHazmatPartida"
  - "MmppHazmatEquipament"
value_objects: []
domain_events:
  - "AutorizacionMMPPConcedida"
  - "NotificacionMMPPEnviada"
ubiquitous_language:
  - term: "Autorització"
    definition: "Autorización de manipulación de mercancía peligrosa."
  - term: "Notificació"
    definition: "Notificación de mercancía peligrosa a las autoridades."
  - term: "Hazmat"
    definition: "Clasificación de mercancía peligrosa (naming en inglés usado en el propio código)."
integration_patterns:
  - pattern: "ACL"
    with_context: "bc-datos-maestros-equipamiento-v1"
    direction: "upstream"
  - pattern: "conformist"
    with_context: "bc-manifiestos-v1"
    direction: "bidirectional"
upstream_contexts:
  - "bc-datos-maestros-equipamiento-v1"
downstream_contexts: []
related_systems:
  - "SOSTRAT-Sostrat-MJ8"
tech_stack:
  - ".NET"
  - "Azure SQL"
  - "Azure Service Bus"
proposed_date: "2026-07-11"
approved_date: null
source: "apb-sub-ddd-code-v1.0"
notes: "Contexto sólido y autocontenido, confirma la hipótesis Jira. Dueño accidental hoy del dato maestro Equipament (contenedor), que se propone extraer a bc-datos-maestros-equipamiento-v1."
---

# MercanciasPeligrosas

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.

## Responsabilidad

Responsable de la gestión de autorizaciones, notificaciones e inspecciones de mercancías peligrosas, incluyendo su circuito EDI de notificación a autoridades.

## Lo que NO incluye

No es propietario del dato maestro de Equipamiento (contenedores) en el modelo objetivo, aunque hoy lo aloja físicamente por herencia histórica — se propone extraerlo a un contexto de datos maestros compartido.

## Modelo de Dominio

### Aggregates

| Aggregate | Responsabilidad |
|-----------|----------------|
| MmppAutoritzacio | Autorización de manipulación de mercancía peligrosa (tabla `MMPP_AUTORITZACIO`). |
| MmppNotif | Notificación de mercancía peligrosa (tabla `MMPP_NOTIF`). |

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| AutorizacionMMPPConcedida | emitido | Se ha concedido una autorización. |
| NotificacionMMPPEnviada | emitido | Se ha enviado una notificación (también vía circuito batch EDI). |

## Relaciones con Otros Bounded Contexts

Dependencia bidireccional con Manifiestos (comparten `PartidaMmpp`); consumirá el futuro servicio de Datos Maestros de Equipamiento en lugar de alojarlo directamente.

## Implementación Actual

Implementado en SÒSTRAT bajo `service/mmpp/{gestion,hazmat,inspecciones,maestros,edi}`, con ~35 rutas Struts propias. El dato maestro `Equipament.java` (tabla `EQUIPAMENT`) vive hoy en `dataaccess/dto/mmpp/maestros/` pero es consumido por 6 dominios distintos — ver `bc-datos-maestros-equipamiento-v1`.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-11 | APB AI Framework (apb-agent-ddd-v1.0) | Propuesta inicial a partir de análisis DDD de SOSTRAT-Sostrat-MJ8 |
