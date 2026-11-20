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
  - "PreavisoCodecoProcesado"
  - "PreavisoCopinoRespondido"
ubiquitous_language:
  - term: "Preavís"
    definition: "Preaviso de transporte terrestre de mercancías."
  - term: "Autorització Genèrica/Específica"
    definition: "Autorización de acceso/operación de transporte terrestre."
  - term: "RPI"
    definition: "Registro/permiso específico de transporte terrestre (siglas usadas en el código)."
integration_patterns:
  - pattern: "conformist"
    with_context: "bc-integracion-edi-portic-v1"
    direction: "downstream"
upstream_contexts:
  - "bc-integracion-edi-portic-v1"
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
| PreavisoCodecoProcesado | emitido | Circuito EDI CODECO: respuesta a un preaviso ya registrado (cierra el gap antes llamado `MensajeCodecoProcesado`). |
| PreavisoCopinoRespondido | emitido | Circuito EDI COPINO: respuesta (con APERAK) a un preaviso de recogida/entrega de mercancía. |

## Relaciones con Otros Bounded Contexts

Sin acoplamiento detectado hacia otros dominios de negocio del sistema; sí hacia integraciones EDI/CBOX externas (PortIC).

**Corregido 2026-07-21** (materialización `PLAN_FASES_FUTURAS.md #103`): esa integración EDI ya no es un acoplamiento directo con PortIC — pasa por el nuevo bounded context `bc-integracion-edi-portic-v1` (upstream, patrón conformist), que traduce EDIFACT↔CloudEvent. Este contexto se suscribe con filtro SQL `circuito IN ('CODECO', 'COPINO')` sobre `evt.sostrat.integracion-edi-portic`. Ver `edi-event-architecture-analysis.md §5`.

## Implementación Actual

Implementado en SÒSTRAT bajo `service/transporteterrestre/` y `mvc/control/transporteterrestre/`, con sub-contexto propio `parquing/` (`VTcListAssignacionsDao`, `VTcPlacesParquingDao`). God class en la Action: `PreavisAction.java` (1.347 líneas). Circuito EDI vía batch (`LanzarCircuitoCodecoTasklet.java`).

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-11 | APB AI Framework (apb-agent-ddd-v1.0) | Propuesta inicial a partir de análisis DDD de SOSTRAT-Sostrat-MJ8 |
| 1.1.0 | 2026-07-21 | APB AI Framework (apb-agent-ddd-v1.0) | Materialización de `PLAN_FASES_FUTURAS.md #103`: `MensajeCodecoProcesado` renombrado/diseñado como `PreavisoCodecoProcesado`, añadido `PreavisoCopinoRespondido`, y `bc-integracion-edi-portic-v1` como upstream (conformist) en vez de acoplamiento directo con PortIC |
