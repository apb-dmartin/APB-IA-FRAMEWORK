---
id: "bc-escalas-v1"
name: "Escalas"
description: |
  Responsable del ciclo de vida de la escala de un buque en el puerto: datos del
  buque, atraque, y versiones/aspectos de la escala a lo largo del tiempo.
status: "discovered"
parent_domain: "dom-operaciones-maritimas-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "Escala"
  - "Atracada"
entities:
  - "EscalaAspecte"
value_objects:
  - "EscalaPk"
domain_events:
  - "EscalaCreada"
  - "EscalaModificada"
  - "AtracadaRegistrada"
ubiquitous_language:
  - term: "Escala"
    definition: "Visita de un buque al puerto."
  - term: "Atracada"
    definition: "Operación de atraque de un buque a un muelle durante una escala."
  - term: "Aspecte de l'Escala"
    definition: "Versión/estado de los datos de la escala."
integration_patterns:
  - pattern: "conformist"
    with_context: "bc-cruceros-v1"
    direction: "upstream"
  - pattern: "conformist"
    with_context: "bc-ferrocarril-portuario-v1"
    direction: "upstream"
  - pattern: "conformist"
    with_context: "bc-marpol-residuos-v1"
    direction: "upstream"
upstream_contexts: []
downstream_contexts:
  - "bc-cruceros-v1"
  - "bc-ferrocarril-portuario-v1"
  - "bc-marpol-residuos-v1"
  - "bc-aguada-v1"
related_systems:
  - "SOSTRAT-Sostrat-MJ8"
  - "APB.API.TES (ARGOS — MS_PORTCALL, ya consume esta escala en producción, ver notes)"
tech_stack:
  - ".NET"
  - "Azure SQL"
proposed_date: "2026-07-11"
approved_date: null
source: "apb-sub-ddd-code-v1.0"
notes: "⚠️ CAMBIO DE PLAN 2026-07-11 (evidencia de código, ver decomposition-roadmap.md Fase 5): NO extraer como microservicio nuevo. ARGOS (APB.API.TES/MS_PORTCALL) ya consume en producción el evento MSG0004 PortcallUpdated emitido por SÒSTRAT, con un DTO (PortCallCreatedDto.cs) que replica el modelo exacto de este bounded context (Origin=SOSTRAT por defecto, campos IdSubPort/YearPortCall/NumPortCall/Aspecte). Es una migración de maestría de dato hacia dom-operaciones-maritimas-v1/ARGOS, no una extracción DDD nueva. Además, la 'separación limpia' descrita en 'Lo que NO incluye' (abajo) no se sostiene en el código real: EscalaAction.java tiene 81 referencias a Liquidacion/Facturacio — esa lógica debe separarse hacia dom-facturacion-v1 ANTES de cualquier migración hacia ARGOS. God class detectada: EscalaAction.java (7.549 líneas)."
---

# Escalas

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.

## Responsabilidad

Este bounded context es responsable de gestionar el ciclo de vida completo de una escala de buque: sus datos, su atraque, y las versiones/aspectos que va tomando la escala a lo largo del tiempo.

## Lo que NO incluye

No debería incluir la gestión de residuos (MARPOL), suministro de agua (Aguada), facturación ni liquidación — estos dominios deberían consumir datos de Escala manteniendo su propia lógica. **Corrección 2026-07-11**: esta separación es el diseño objetivo, pero el código real de `EscalaAction.java` NO la respeta — tiene 81 referencias literales a `Liquidacion`/`Facturacio`. Antes de cualquier migración hacia ARGOS (ver `notes`), hay que extraer esa lógica hacia `dom-facturacion-v1`.

## Modelo de Dominio

### Aggregates

| Aggregate | Responsabilidad |
|-----------|----------------|
| Escala | Representa la visita del buque; raíz de agregado principal (tabla `ESCALA`). |
| Atracada | Representa el atraque asociado a una escala (tabla `ATRACADA`). |

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| EscalaCreada | emitido | Se ha registrado una nueva escala. |
| EscalaModificada | emitido | Cambio de aspecto/versión de una escala existente. |
| AtracadaRegistrada | emitido | Se ha registrado un atraque para una escala. |

## Relaciones con Otros Bounded Contexts

Es upstream (conformist) de Cruceros, Ferrocarril Portuario, MARPOL/Residuos y Servicios Auxiliares al Buque — todos ellos referencian la escala vía `EscalaPk` en el código actual.

## Implementación Actual

Implementado en SÒSTRAT bajo `service/escalas/` (67 interfaces `CN_*`), `dataaccess/dto/escalas/Escala.java` y `Atracada.java`, con lógica de negocio parcialmente filtrada a la capa de presentación (`mvc/control/escalas/EscalaAction.java`, 7.549 líneas — god class a refactorizar antes o durante la extracción).

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-11 | APB AI Framework (apb-agent-ddd-v1.0) | Propuesta inicial a partir de análisis DDD de SOSTRAT-Sostrat-MJ8 |
