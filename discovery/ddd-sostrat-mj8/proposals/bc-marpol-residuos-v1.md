---
id: "bc-marpol-residuos-v1"
name: "MarpolResiduos"
description: |
  Gestión de la recogida de residuos de buques conforme a normativa MARPOL,
  incluyendo pesaje, contenedores, códigos QR y circuito EDI de declaración
  (WASDIS).
status: "discovered"
parent_domain: "dom-medio-ambiente-marpol-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "ResidusEscala"
entities:
  - "ResidusLot"
  - "ResidusFact"
  - "ResidusLinea"
value_objects: []
domain_events:
  - "ListaResiduosMarpolGenerada"
  - "ResiduoPesado"
ubiquitous_language:
  - term: "Residu"
    definition: "Residuo de buque recogido conforme a normativa MARPOL."
  - term: "Lot"
    definition: "Lote de recogida de residuos."
  - term: "Wasdis"
    definition: "Circuito EDI de declaración de residuos a autoridades."
integration_patterns:
  - pattern: "conformist"
    with_context: "bc-escalas-v1"
    direction: "downstream"
upstream_contexts:
  - "bc-escalas-v1"
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
notes: "El más grande y maduro del dominio Servicios Auxiliares al Buque (114 clases) — se mantiene como bounded context propio, no se agrupa con los pequeños. Corresponde también a la hipótesis 'MEDI' (Medio Ambiente) de la knowledge base, que no tiene paquete propio separado."
---

# MarpolResiduos

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.

## Responsabilidad

Responsable de la gestión de recogida de residuos de buques conforme a normativa MARPOL: lotes, pesaje, contenedores y el circuito EDI de declaración (WASDIS) a autoridades.

## Lo que NO incluye

No gestiona otros servicios auxiliares al buque (agua, marinas, pesca) pese a compartir dominio de negocio — se mantiene separado por tamaño y madurez.

## Modelo de Dominio

### Aggregates

| Aggregate | Responsabilidad |
|-----------|----------------|
| ResidusEscala | Raíz de agregado de los residuos asociados a una escala (tabla `RESIDUS_ESCALA`). |

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| ListaResiduosMarpolGenerada | emitido | Se ha generado la lista de residuos (proceso batch). |
| ResiduoPesado | emitido | Se ha registrado el pesaje de un residuo. |

## Relaciones con Otros Bounded Contexts

Downstream de Escalas vía `EscalaPk`.

## Implementación Actual

Implementado en SÒSTRAT bajo `service/marpol/` (114 clases, subpaquetes `wasdis`, `pesatges`, `contenidor`, `camio`, `codisqr`, `infoBascula`, `informesResidus`), con configuración de seguridad dedicada `applicationContext-spring-security-residuos.xml`. Circuito batch en `sostrat-BATCH` (`MarpolTasklet.java`, `LanzarCircuitoListaDeResiduosMARPOLTasklet.java`).

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-11 | APB AI Framework (apb-agent-ddd-v1.0) | Propuesta inicial a partir de análisis DDD de SOSTRAT-Sostrat-MJ8 |
