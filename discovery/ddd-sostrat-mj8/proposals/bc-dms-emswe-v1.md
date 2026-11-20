---
id: "bc-dms-emswe-v1"
name: "Declaración Marítima de Sanidad (DMS/EMSWe)"
description: |
  Gestión de la Declaración Marítima de Sanidad (Maritime Declaration of Health)
  de un buque en escala — uno de los formularios FAL de la European Maritime
  Single Window environment (EMSWe, Directiva UE 2019/1239). Este es el circuito
  real de "ventanilla única europea" del sistema, distinto de la Ventanilla
  Única Aduanera española (VUA/SAPL, ver bc-vua-sapl-v1). Intercambio
  bidireccional asíncrono de ficheros XML (schema MDH), independiente del
  gateway EDI genérico.
status: "discovered"
parent_domain: "dom-operaciones-maritimas-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "DeclaracionSanitariaMaritima"
entities:
  - "SancrtPosIns"
value_objects: []
domain_events:
  - "DeclaracionSanitariaMaritimaRecibida"
  - "PosicionamientoSanitarioActualizado"
ubiquitous_language:
  - term: "DMS"
    definition: "Declaración Marítima de Sanidad / Maritime Declaration of Health — formulario FAL de la EMSWe europea."
  - term: "EMSWe"
    definition: "European Maritime Single Window environment (Directiva UE 2019/1239). En este código, DMS es el circuito real que la implementa — no VUA/SAPL, que es un sistema aduanero nacional distinto (AEAT)."
  - term: "SancrtPosIns"
    definition: "Posicionamiento sanitario/aduanero del contenedor o buque, entidad puente también usada por bc-vua-sapl-v1."
integration_patterns:
  - pattern: "ACL"
    with_context: "Sistema europeo EMSWe (sistema externo)"
    direction: "bidirectional"
  - pattern: "conformist"
    with_context: "bc-escalas-v1"
    direction: "downstream"
upstream_contexts: []
downstream_contexts: []
related_systems:
  - "SOSTRAT-Sostrat-MJ8 (service/escalas/dms)"
  - "EMSWe (European Maritime Single Window environment)"
tech_stack:
  - ".NET"
  - "Azure SQL"
  - "Azure Blob Storage (posible reemplazo del intercambio de ficheros por directorio)"
proposed_date: "2026-07-15"
approved_date: null
source: "apb-agent-ddd-v1.0"
notes: "Creado a partir de discovery/ddd-sostrat-mj8/edi-event-architecture-analysis.md. Se propone como bounded context independiente hoy porque bc-escalas-v1 todavía no existe (bloqueado por la sesión pendiente con el equipo de ARGOS, ver dossier-00-escalas-migracion-argos.md) — su relación final (¿fusión dentro de bc-escalas-v1, o conformist downstream permanente?) debe revisarse una vez ese bounded context se cree. No confundir con bc-vua-sapl-v1: comparten la entidad SancrtPosIns como puente pero no tabla de mensaje ni mecanismo de negocio."
---

# Declaración Marítima de Sanidad (DMS/EMSWe)

## Responsabilidad

Recibir y procesar la Declaración Marítima de Sanidad de un buque en una escala concreta, y mantener actualizado el posicionamiento sanitario asociado.

## Lo que NO incluye

No gestiona la Ventanilla Única Aduanera española (eso es `bc-vua-sapl-v1`, sistema distinto pese a compartir la entidad puente `SancrtPosIns`). No gestiona la escala en sí (buque, atraque) — eso es `bc-escalas-v1`; este bounded context solo consume `EscalaPk` como referencia, igual que MARPOL/Aguada/Ferrocarril. No usa el modelo genérico de mensajería EDI (`MissatgeEdi`) — tiene su propio esquema XML (JAXB `MDHResponse`) e intercambio de ficheros.

## Modelo de Dominio

### Aggregates

| Aggregate | Responsabilidad |
|-----------|----------------|
| `DeclaracionSanitariaMaritima` | Declaración recibida por escala (`idsubport`+`anyescala`+`numescala`+`numdms`), formato FAL/EMSWe real. |

### Entidades

`SancrtPosIns` (posicionamiento sanitario/aduanero, entidad puente también usada por `bc-vua-sapl-v1`).

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| `DeclaracionSanitariaMaritimaRecibida` | emitido | Declaración MDH recibida e incorporada al posicionamiento de la escala. |
| `PosicionamientoSanitarioActualizado` | emitido | Cambio de estado de `SancrtPosIns` tras procesar la declaración. |

## Relaciones con Otros Bounded Contexts

Patrón `ACL` bidireccional con el sistema europeo EMSWe (fuera de DOCKS). Patrón `conformist` downstream de `bc-escalas-v1` (referencia a `EscalaPk`, sin escritura cruzada) — mismo patrón ya usado por MARPOL/Aguada/Ferrocarril hacia Escalas.

## Implementación Actual

Implementado en SÒSTRAT bajo `service/escalas/dms` (`CN_DMS_Impl.java:1019-1064`). Mecanismo: intercambio bidireccional asíncrono por fichero — SÒSTRAT envía declaraciones (`enviarDeclaraciones`→`lanzarEnviosMDH`) y lee ficheros de respuesta de un directorio convencional (`portic.cargaMDHPortic.inbox/recibidos/error`). Formato: XML propio con schema JAXB (`jaxbmdh.response.MDHResponse`, incluye `CaseDisposalType`), no EDIFACT. Batch Quartz cada 5 minutos (proceso) + cada 2 minutos (temporizador), `sostrat-batch-DMS.xml:109,115`.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-15 | APB AI Framework | Propuesta inicial, a petición explícita del usuario. Grounded en `edi-event-architecture-analysis.md`. Identifica este circuito como el correspondiente real a la EMSWe europea, corrigiendo la descripción de `domain-catalog/domains/integraciones-edi/domain.md` que atribuía ese rol a VUA/SAPL. |
