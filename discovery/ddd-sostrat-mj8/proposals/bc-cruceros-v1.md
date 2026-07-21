---
id: "bc-cruceros-v1"
name: "Cruceros"
description: |
  Gestión específica de escalas de buques de crucero, incluyendo auditoría de
  la escala de crucero y datos de pasajeros asociados.
status: "discovered"
parent_domain: "dom-cruceros-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "CreuerEscalaAudit"
entities: []
value_objects: []
domain_events:
  - "EscalaCruceroAuditada"
  - "ListaPasajerosDeclarada"
  - "ListaPasajerosConfirmada"
ubiquitous_language:
  - term: "Creuer"
    definition: "Buque de crucero."
integration_patterns:
  - pattern: "conformist"
    with_context: "bc-escalas-v1"
    direction: "downstream"
upstream_contexts:
  - "bc-escalas-v1"
  - "bc-integracion-edi-portic-v1"
downstream_contexts: []
related_systems:
  - "SOSTRAT-Sostrat-MJ8"
tech_stack:
  - ".NET"
  - "Azure SQL"
proposed_date: "2026-07-11"
approved_date: null
source: "apb-sub-ddd-code-v1.0"
notes: "Ya semi-diferenciado en el código actual (paquete propio dataaccess/dto/cruceros/). Expuesto también vía servicio SOAP CrucerosWSPort en sostratWSCXF."
---

# Cruceros

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.

## Responsabilidad

Responsable de la gestión específica de escalas de cruceros: auditoría de la escala y datos asociados a la actividad de cruceros.

## Lo que NO incluye

No gestiona los datos generales de la escala (buque, atraque) — eso pertenece a Escalas; Cruceros es un contexto downstream que añade información específica del segmento crucero.

## ⚠️ Nota crítica (2026-07-14) — implementación .NET ya activa fuera de este documento

Este documento solo cubre el agregado `CreuerEscalaAudit`. **No hay todavía un dossier de aplicación final para `bc-cruceros-v1`.** Una auditoría de consumidores externos (`discovery/ddd-sostrat-mj8/EXTERNAL_CONSUMERS_AUDIT.md §2` fila 8 y §3) confirmó que ya existe un ecosistema .NET real y activo (~3 meses de desarrollo) para la gestión de reservas de atraque de crucero — repos `APB.API.CRE`, `APB.APP.CRE`, `APB.API.VXL`, `APB.API.SLC` (Jenkins `ARQ/TST/SOSTRAT/CRE-Cruceros`) — con su propio modelo (`CreSolicitud`, `CreVaixell`, `CreTerminalBloqueado`, `CreLineaOperativaSolicitud`), API y frontend. Sin solapamiento de datos con `dossier-18-servicios-auxiliares-cruceros.md` (buses/vigilancia es una sub-capacidad distinta), pero **cualquier dossier de aplicación final de `bc-cruceros-v1` que se escriba debe documentar esta implementación ya existente como la realidad operativa del bounded context, no tratarla como trabajo futuro de extracción.**

## Modelo de Dominio

### Aggregates

| Aggregate | Responsabilidad |
|-----------|----------------|
| CreuerEscalaAudit | Auditoría de la escala de crucero. |

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| EscalaCruceroAuditada | emitido | Se ha auditado una escala de crucero. |
| ListaPasajerosDeclarada | emitido | Circuito EDI PAXLST: lista de pasajeros declarada. ⚠️ payload provisional, DTO fuente no confirmado — ver `events-catalog.md §2`. |
| ListaPasajerosConfirmada | emitido | Circuito EDI PAXLST: lista de pasajeros confirmada (respuesta APERAK). ⚠️ mismo gap de evidencia que el evento anterior. |

## Relaciones con Otros Bounded Contexts

Downstream (conformist) de Escalas.

**Añadido 2026-07-21** (materialización `PLAN_FASES_FUTURAS.md #103`): también downstream de `bc-integracion-edi-portic-v1` para el circuito PAXLST (lista de pasajeros), vía suscripción con filtro SQL `circuito = 'PAXLST'` sobre `evt.sostrat.integracion-edi-portic` — ver `edi-event-architecture-analysis.md §5`. **Gap de evidencia pendiente**: el DTO transaccional real de PAXLST (`CN_Escala_PAXLST_Impl.java`) no se ha leído en ninguna sesión de esta serie; el payload de estos dos eventos es provisional hasta recuperar ese código fuente.

## Implementación Actual

Implementado en SÒSTRAT bajo `dataaccess/dto/cruceros/CreuerEscalaAudit.java` y expuesto también mediante el servicio SOAP `CrucerosWSPort` (`sostratWSCXF`), con operaciones `getCruceros`, `getCrucerosAmarrados`, `getCruceroDetalle`, `getBuques`, `getEscalas`.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-11 | APB AI Framework (apb-agent-ddd-v1.0) | Propuesta inicial a partir de análisis DDD de SOSTRAT-Sostrat-MJ8 |
| 1.1.0 | 2026-07-21 | APB AI Framework (apb-agent-ddd-v1.0) | Materialización de `PLAN_FASES_FUTURAS.md #103`: añadidos `ListaPasajerosDeclarada`/`ListaPasajerosConfirmada` (circuito EDI PAXLST, payload provisional por gap de evidencia) y `bc-integracion-edi-portic-v1` como upstream |
