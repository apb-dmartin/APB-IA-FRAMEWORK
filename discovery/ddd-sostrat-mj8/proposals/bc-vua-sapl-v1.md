---
id: "bc-vua-sapl-v1"
name: "Ventanilla Única Aduanera (VUA/SAPL)"
description: |
  Coordinación con la Ventanilla Única Aduanera española (AEAT) para el
  posicionamiento/precintado de contenedores sujetos a control aduanero: alta,
  baja y notificación de entrada/salida de un SAPL (Sistema de Anticipación de
  Precintado en Lonja/Aduanas). Intercambio de ficheros XML con esquema formal
  publicado por la AEAT, independiente del gateway EDI genérico (no comparte
  tabla, modelo de estado ni mecanismo de transporte con MISSATGE_EDI).
status: "discovered"
parent_domain: "dom-inspeccion-control-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "Sapl"
entities:
  - "SaplContenidor"
  - "MissatgeVua"
  - "SancrtPosIns"
value_objects: []
domain_events:
  - "SaplAltaRegistrada"
  - "SaplBajaRegistrada"
  - "NotificacionSalidaVuaRecibida"
  - "NotificacionEntradaVuaEnviada"
ubiquitous_language:
  - term: "SAPL"
    definition: "Sistema de Anticipación de Precintado en Lonja/Aduanas — expediente de coordinación aduanera sobre uno o varios contenedores."
  - term: "VUA"
    definition: "Ventanilla Única Aduanera de la AEAT (España) — NO es la EMSWe europea, es un sistema nacional distinto. Ver bc-dms-emswe-v1 para el circuito FAL/EMSWe real."
  - term: "NotifEntrada"
    definition: "Único mensaje OUTBOUND del circuito — SÒSTRAT notifica a la VUA la entrada de un contenedor. Invariante de negocio confirmada en código: un SAPL solo se responde una vez."
integration_patterns:
  - pattern: "ACL"
    with_context: "AEAT (Ventanilla Única Aduanera, sistema externo)"
    direction: "bidirectional"
upstream_contexts: []
downstream_contexts: []
related_systems:
  - "SOSTRAT-Sostrat-MJ8 (service/pif/impl/sapl)"
  - "AEAT (Agencia Estatal de Administración Tributaria — Ventanilla Única Aduanera)"
tech_stack:
  - ".NET"
  - "Azure SQL"
  - "Azure Blob Storage (posible reemplazo del intercambio de ficheros por directorio)"
proposed_date: "2026-07-15"
approved_date: null
source: "apb-agent-ddd-v1.0"
notes: "Creado a partir de discovery/ddd-sostrat-mj8/edi-event-architecture-analysis.md. Corrige una imprecisión ya presente en domain-catalog/domains/integraciones-edi/domain.md, que describe este circuito como si fuera la EMSWe europea — no lo es: es la Ventanilla Única Aduanera NACIONAL española (AEAT). El circuito FAL/EMSWe real es DMS, ver bc-dms-emswe-v1. Separado de bc-pif-v1 (mismo paquete Java, service/pif) por el mismo criterio que ya separó bc-pif-v1 de bc-inspeccion-scpp-v1: persistencia y modelo de estado propios, sin nada compartido con el resto del código de PIF ni con el gateway EDI genérico."
---

# Ventanilla Única Aduanera (VUA/SAPL)

## Responsabilidad

Gestionar el ciclo de vida de un expediente SAPL: recibir el alta y la baja de un SAPL desde la AEAT, recibir la notificación de salida, y notificar la entrada de un contenedor a la AEAT cuando corresponda — con la garantía de que cada SAPL se notifica como máximo una vez.

## Lo que NO incluye

No gestiona la inspección física del contenedor en sí (eso es `bc-pif-v1`/`bc-inspeccion-scpp-v1`, aunque `SancrtPosIns` — posicionamiento sanitario/aduanero — es la entidad puente entre ambos mundos). No es la Ventanilla Única Marítima europea (EMSWe) — ese circuito es `bc-dms-emswe-v1`. No usa el modelo genérico de mensajería EDI (`MissatgeEdi`/`CircuitEdi`) — tiene su propia tabla `MissatgeVua` y su propio modelo de estado (`"A"`/`"B"`/`"N"`), independiente de `EstatEdi`.

## Modelo de Dominio

### Aggregates

| Aggregate | Responsabilidad |
|-----------|----------------|
| `Sapl` | Expediente de coordinación aduanera. Estados confirmados en código: `"A"` (alta), `"B"` (baja/anulado), `"N"` (notificado salida). |

### Entidades

`SaplContenidor` (contenedores asociados a un SAPL; campo `nummissatgenotif` — si ya está seteado, el SAPL no se vuelve a notificar, invariante de idempotencia confirmada en código), `MissatgeVua` (registro de mensaje VUA, modelo de estado propio, no reutiliza `MissatgeEdi`), `SancrtPosIns` (posicionamiento sanitario/aduanero del contenedor, puente hacia PIF/SCPP).

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| `SaplAltaRegistrada` | emitido | Alta de un SAPL recibida de la AEAT (XSD `CoordinacionAltaV1Sal`). |
| `SaplBajaRegistrada` | emitido | Baja/anulación de un SAPL recibida de la AEAT (XSD `CoordinacionAnulacionV1Sal`). |
| `NotificacionSalidaVuaRecibida` | emitido | Notificación de salida recibida de la AEAT (XSD `NotificacionAltaV1Sal`). |
| `NotificacionEntradaVuaEnviada` | emitido | Notificación de entrada enviada a la AEAT (XSD `NotificacionAltaV1Ent`) — único mensaje outbound del circuito. |

## Relaciones con Otros Bounded Contexts

Patrón `ACL` bidireccional con la AEAT (sistema externo, fuera de DOCKS) — intercambio de ficheros XML validados contra los 4 XSD reales publicados por la AEAT. Relación de dominio (no de código) con `bc-pif-v1`/`bc-inspeccion-scpp-v1` vía `SancrtPosIns` — el resultado de la coordinación VUA condiciona si un contenedor pasa por inspección física, pero no hay tabla ni agregado compartido.

## Implementación Actual

Implementado en SÒSTRAT bajo `service/pif/impl/sapl/{alta,baja,notificacionent,notificacionsal}` (`CN_SAPL_Impl.java`). Mecanismo: intercambio de ficheros XML asíncrono vía directorios convencionales (`portic.cargaVUAPortic.inbox/recibidos/error/outbox`), no SOAP síncrono pese a vivir en un paquete llamado "servicio". Batch Quartz cada 1 minuto (`sostrat-batch-GestionVUA.xml:77`) — el intervalo más agresivo de todo el sistema EDI. Contratos formales: `CoordinacionAltaV1Sal.xsd`, `CoordinacionAnulacionV1Sal.xsd`, `NotificacionAltaV1Sal.xsd`, `NotificacionAltaV1Ent.xsd` (tomados directamente del esquema publicado por la AEAT — buen candidato a reutilizar tal cual en el ACL del nuevo servicio, sin reinventar el contrato).

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-15 | APB AI Framework | Propuesta inicial, a petición explícita del usuario. Grounded en `edi-event-architecture-analysis.md`. Corrige la imprecisión de `domain-catalog/domains/integraciones-edi/domain.md` que trataba este circuito como EMSWe europea — es la Ventanilla Única Aduanera nacional (AEAT). |
