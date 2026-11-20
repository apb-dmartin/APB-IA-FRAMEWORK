---
id: "bc-titulo-v1"
name: "Titulo"
description: |
  Gestión de títulos de ocupación y actividad portuaria (el concepto real que la
  hipótesis Jira denominaba "Concesión"). Incluye documentación de concesiones y
  planes especiales asociados.
status: "discovered"
parent_domain: "dom-concesiones-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "Titol"
entities:
  - "TitolOcupacio"
  - "TitolActivitat"
  - "TitolMinim"
value_objects:
  - "TitolPk"
domain_events:
  - "TituloOtorgado"
  - "TituloActualizado"
ubiquitous_language:
  - term: "Títol"
    definition: "Título de ocupación o actividad portuaria."
  - term: "Ocupació"
    definition: "Ocupación de dominio público portuario bajo un título."
  - term: "Activitat"
    definition: "Actividad autorizada bajo un título."
integration_patterns:
  - pattern: "shared-kernel"
    with_context: "bc-liquidacion-v1"
    direction: "bidirectional"
  - pattern: "conformist"
    with_context: "bc-garantias-v1"
    direction: "upstream"
upstream_contexts: []
downstream_contexts:
  - "bc-liquidacion-v1"
  - "bc-garantias-v1"
related_systems:
  - "SOSTRAT-Sostrat-MJ8"
tech_stack:
  - ".NET"
  - "Azure SQL"
proposed_date: "2026-07-11"
approved_date: null
source: "apb-sub-ddd-code-v1.0"
notes: "CORRIGE HIPÓTESIS: el paquete 'concesiones' del código está casi vacío; el dominio real es 'Titol', disperso hoy entre service/impl (sin paquete propio), service/titolminim, service/liquidacion, service/documentconcessions y service/plaespecial. Liquidación escribe directamente en tablas de Título (anti-patrón detectado) — el patrón de integración 'shared-kernel' con Liquidación refleja este acoplamiento real, no es el objetivo final deseado."
---

# Titulo

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.

## Responsabilidad

Este bounded context es responsable de gestionar los títulos de ocupación y actividad portuaria: su otorgamiento, ocupaciones, actividades autorizadas y documentación asociada.

## Lo que NO incluye

No incluye el cálculo de liquidaciones ni la facturación — aunque hoy Liquidación escribe directamente sobre tablas de Título, esto es un anti-patrón a corregir, no el diseño objetivo.

## Modelo de Dominio

### Aggregates

| Aggregate | Responsabilidad |
|-----------|----------------|
| Titol | Raíz de agregado del título de ocupación/actividad portuaria. |

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| TituloOtorgado | emitido | Se ha otorgado un nuevo título. |
| TituloActualizado | emitido | Se ha actualizado un título existente (sustituye a la escritura directa de tabla detectada en el legacy). |

## Relaciones con Otros Bounded Contexts

Fuertemente acoplado con Liquidación en la implementación actual (patrón "shared-kernel" de facto, por escrituras cruzadas de tabla) — el objetivo del modelo destino es sustituir esa escritura directa por eventos de dominio. Es upstream de Garantías, que depende de `IDTITOL` sin agregado propio.

## Implementación Actual

Implementado en SÒSTRAT de forma dispersa: `service/impl/CN_Titol_Impl.java` (1.888 líneas, sin paquete propio), `service/titolminim/`, `service/documentconcessions/`, `service/plaespecial/`. God class principal: `CN_Titol_Impl.java`.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-11 | APB AI Framework (apb-agent-ddd-v1.0) | Propuesta inicial a partir de análisis DDD de SOSTRAT-Sostrat-MJ8 |
