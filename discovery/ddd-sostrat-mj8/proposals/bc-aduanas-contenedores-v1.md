---
id: "bc-aduanas-contenedores-v1"
name: "AduanasControlContenedores"
description: |
  Control de tránsito y traslado de contenedores en régimen aduanero. Equivalente
  real de la hipótesis Jira "CTA", hoy sin paquete propio en el código.
status: "discovered"
parent_domain: "dom-mercancias-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "TrasllatContenidor"
entities:
  - "TransitContenidor"
  - "CreuamentDadesTerminal"
value_objects: []
domain_events:
  - "TrasladoContenedorActualizado"
  - "DatosTerminalConciliados"
ubiquitous_language:
  - term: "Trasllat"
    definition: "Traslado de un contenedor entre ubicaciones/terminales."
  - term: "Trànsit"
    definition: "Tránsito aduanero de un contenedor."
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
  - "Azure Service Bus"
proposed_date: "2026-07-11"
approved_date: null
source: "apb-sub-ddd-code-v1.0"
notes: "CORRIGE HIPÓTESIS: no existe paquete 'cta' en el código; la funcionalidad está repartida entre service/aduanas y service/terminales. REQUIERE CONSOLIDACIÓN INTERNA (fusionar ambos paquetes en un único bounded context coherente) antes de poder extraerse — ver decomposition-roadmap.md Fase 0/3. También se expone parcialmente vía sostratWSCXF (ContenedoresSecureSOAP) hacia consumidores externos."
---

# AduanasControlContenedores

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.

## Responsabilidad

Responsable del control de tránsito y traslado de contenedores en régimen aduanero, incluyendo la conciliación de datos de terminales.

## Lo que NO incluye

No gestiona el manifiesto de mercancías (eso es Manifiestos) ni la inspección física fronteriza (eso es PIF).

## Modelo de Dominio

### Aggregates

| Aggregate | Responsabilidad |
|-----------|----------------|
| TrasllatContenidor | Raíz de agregado del traslado de un contenedor. |

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| TrasladoContenedorActualizado | emitido | Se ha actualizado el traslado de un contenedor. |
| DatosTerminalConciliados | emitido | Se han conciliado datos de terminal (proceso batch). |

## Relaciones con Otros Bounded Contexts

Consumirá el futuro servicio de Datos Maestros de Equipamiento. Se expone parcialmente hoy hacia consumidores externos vía el servicio SOAP `ContenedoresSecureSOAP` (`sostratWSCXF`), candidato a open-host-service en el modelo objetivo.

## Implementación Actual

Implementado de forma **dispersa** en SÒSTRAT entre `service/aduanas/` (`CN_ConsultaContenedor`, `CN_TrasllatContenidor`, `CN_TransitContenidor`, `CN_CreuamentDadesTerminal`) y `service/terminales/` (`CN_ProtermCont_Impl`, `CN_CodecoCont_Impl`). No existe hoy un límite físico de bounded context — es la razón por la que este contexto requiere un paso de consolidación interna antes de cualquier extracción.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-11 | APB AI Framework (apb-agent-ddd-v1.0) | Propuesta inicial a partir de análisis DDD de SOSTRAT-Sostrat-MJ8 |
