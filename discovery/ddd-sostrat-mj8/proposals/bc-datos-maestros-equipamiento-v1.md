---
id: "bc-datos-maestros-equipamiento-v1"
name: "DatosMaestrosEquipamiento"
description: |
  Contexto de datos maestros compartidos de equipamiento (contenedores y otros
  equipos de transporte de mercancías), propuesto para eliminar el acoplamiento
  detectado hoy entre seis dominios distintos que acceden directamente a la
  misma tabla EQUIPAMENT.
status: "discovered"
parent_domain: "dom-mercancias-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "Equipament"
entities: []
value_objects: []
domain_events:
  - "EquipamientoRegistrado"
  - "EquipamientoActualizado"
ubiquitous_language:
  - term: "Equipament"
    definition: "Contenedor u otro equipo de transporte de mercancías."
integration_patterns:
  - pattern: "published-language"
    with_context: "bc-manifiestos-v1"
    direction: "downstream"
  - pattern: "published-language"
    with_context: "bc-mmpp-v1"
    direction: "downstream"
  - pattern: "published-language"
    with_context: "bc-pif-v1"
    direction: "downstream"
  - pattern: "published-language"
    with_context: "bc-depotsis-v1"
    direction: "downstream"
  - pattern: "published-language"
    with_context: "bc-aduanas-contenedores-v1"
    direction: "downstream"
  - pattern: "published-language"
    with_context: "bc-liquidacion-v1"
    direction: "downstream"
upstream_contexts: []
downstream_contexts:
  - "bc-manifiestos-v1"
  - "bc-mmpp-v1"
  - "bc-pif-v1"
  - "bc-depotsis-v1"
  - "bc-aduanas-contenedores-v1"
  - "bc-liquidacion-v1"
related_systems:
  - "SOSTRAT-Sostrat-MJ8"
tech_stack:
  - ".NET"
  - "Azure SQL"
  - "Azure API Management"
proposed_date: "2026-07-11"
approved_date: null
source: "apb-agent-ddd-v1.0"
notes: "PROPUESTA NUEVA (no corresponde a un paquete Java existente 1:1) — nace del anti-patrón detectado: la clase Equipament.java (tabla EQUIPAMENT) vive físicamente en el paquete de MMPP pero es consumida directamente por 54 ficheros de 6 dominios distintos. Se propone como prerequisito de la Fase 0 del roadmap de descomposición, antes de extraer cualquiera de sus 6 consumidores. Pendiente confirmar dueño de negocio con Arquitectura APB (ver discovery-summary.md §5)."
---

# DatosMaestrosEquipamiento

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.

## Responsabilidad

Responsable de mantener el dato maestro de equipamiento (contenedores y otros equipos) como fuente única de verdad, expuesta como servicio a los dominios que hoy acceden directamente a la tabla `EQUIPAMENT`.

## Lo que NO incluye

No gestiona el traslado, tránsito, manifiesto ni ninguna operación de negocio sobre el contenedor — solo su identidad y atributos maestros.

## Modelo de Dominio

### Aggregates

| Aggregate | Responsabilidad |
|-----------|----------------|
| Equipament | Raíz de agregado del dato maestro de contenedor/equipo. |

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| EquipamientoRegistrado | emitido | Se ha registrado un nuevo equipo/contenedor. |
| EquipamientoActualizado | emitido | Se han actualizado los atributos maestros de un equipo. |

## Relaciones con Otros Bounded Contexts

Es upstream (published language) de Manifiestos, MMPP, PIF, Depotsis, Aduanas/Control de Contenedores y Liquidación — todos ellos consumidores directos hoy de la tabla `EQUIPAMENT` sin pasar por ningún servicio.

## Implementación Actual

**No existe como bounded context independiente hoy.** La clase `Equipament.java` vive físicamente en `dataaccess/dto/mmpp/maestros/` (dentro del paquete de MMPP), pero es consumida directamente por 54 ficheros de 6 dominios distintos (`service/manifiestos/gestion/impl/CN_ManifestEquipament_Impl.java`, `service/coarri/impl/CN_OperacionTerminal_Impl.java`, `service/aduanas/impl/CN_TrasllatContenidor_Impl.java`, entre otros). Esta propuesta formaliza la extracción de ese dato maestro como servicio propio, prerequisito de la Fase 0 del roadmap.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-11 | APB AI Framework (apb-agent-ddd-v1.0) | Propuesta inicial a partir de análisis DDD de SOSTRAT-Sostrat-MJ8 |
