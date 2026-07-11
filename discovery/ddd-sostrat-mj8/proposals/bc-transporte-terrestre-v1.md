---
id: "bc-transporte-terrestre-v1"
name: "TransporteTerrestre"
description: |
  Gestión del transporte terrestre de mercancías: preavisos, autorizaciones
  genéricas/específicas, RPI, parquing, transportistas, vehículos y conductores,
  con circuito CODECO/EDI propio.
status: "discovered"
parent_domain: "dom-transporte-terrestre-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "Preavis"
  - "AutorizacionGenerica"
entities:
  - "OperacioPuntual"
  - "PlacesParquing"
  - "Transportista"
  - "Vehicle"
  - "Conductor"
value_objects: []
domain_events:
  - "PreavisoRegistrado"
  - "AutorizacionConcedida"
  - "MensajeCodecoProcesado"
ubiquitous_language:
  - term: "Preavís"
    definition: "Preaviso de transporte terrestre de mercancías."
  - term: "Autorització Genèrica/Específica"
    definition: "Autorización de acceso/operación de transporte terrestre."
  - term: "RPI"
    definition: "Registro/permiso específico de transporte terrestre (siglas usadas en el código)."
integration_patterns: []
upstream_contexts: []
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
notes: "Segundo módulo más grande del sistema tras MARPOL. Contiene un sub-bounded-context propio (Parquing) que debería descomponerse internamente antes de la extracción completa — ver decomposition-roadmap.md Fase 2. Sin acoplamiento detectado hacia otros dominios de negocio (sí hacia integraciones EDI/CBOX externas)."
---

# TransporteTerrestre

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.

## Responsabilidad

Responsable de la gestión del transporte terrestre de mercancías dentro y hacia el recinto portuario: preavisos, autorizaciones, parquing, y datos de transportistas/vehículos/conductores.

## Lo que NO incluye

No gestiona el control de accesos personales (eso es PPS) ni la mercancía en sí (eso es Manifiestos/MMPP).

## Modelo de Dominio

### Aggregates

| Aggregate | Responsabilidad |
|-----------|----------------|
| Preavis | Preaviso de transporte terrestre. |
| AutorizacionGenerica | Autorización genérica o específica de operación. |

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| PreavisoRegistrado | emitido | Se ha registrado un preaviso. |
| AutorizacionConcedida | emitido | Se ha concedido una autorización. |
| MensajeCodecoProcesado | emitido | Se ha procesado un mensaje CODECO (circuito EDI batch). |

## Relaciones con Otros Bounded Contexts

Sin acoplamiento detectado hacia otros dominios de negocio del sistema; sí hacia integraciones EDI/CBOX externas (PortIC).

## Implementación Actual

Implementado en SÒSTRAT bajo `service/transporteterrestre/` y `mvc/control/transporteterrestre/`, con sub-contexto propio `parquing/` (`VTcListAssignacionsDao`, `VTcPlacesParquingDao`). God class en la Action: `PreavisAction.java` (1.347 líneas). Circuito EDI vía batch (`LanzarCircuitoCodecoTasklet.java`).

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-11 | APB AI Framework (apb-agent-ddd-v1.0) | Propuesta inicial a partir de análisis DDD de SOSTRAT-Sostrat-MJ8 |
