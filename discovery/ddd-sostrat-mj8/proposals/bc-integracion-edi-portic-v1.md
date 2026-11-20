---
id: "bc-integracion-edi-portic-v1"
name: "Integración EDI / Portic (Gateway de Transporte)"
description: |
  Capa de transporte y traducción entre SÒSTRAT/DOCKS y Portic (hub EDIFACT de la
  comunidad portuaria de Barcelona). Posee el modelo de auditoría genérico de
  mensajería EDI (cabecera de mensaje, catálogo de circuitos, tipo de mensaje,
  registro de errores, líneas de detalle) y el contrato SOAP real con Portic.
  No parsea ni valida el contenido de negocio de ningún mensaje — eso es
  responsabilidad de cada bounded context de negocio consumidor (published-language).
status: "discovered"
parent_domain: "dom-integraciones-edi-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "MissatgeEdi"
entities:
  - "TipusMissatgeEdi"
  - "CircuitEdi"
  - "ProcesEdi"
  - "ErrorEdi"
  - "LiniaDeMissatgeEdi"
  - "TipusDAlarmaEdi"
  - "AlarmaEDI"
  - "BustiaEDI"
  - "UsuariCircuitEDI"
value_objects:
  - "EstatEdi"
domain_events:
  - "MensajeEdiEnviado"
  - "MensajeEdiRechazado"
  - "ErrorEdiRegistrado"
ubiquitous_language:
  - term: "Circuito EDI"
    definition: "Familia de mensaje EDIFACT/XML con un propósito de negocio concreto (COARRI, CODECO, WASDIS, PAXLST...), modelada como dato en CircuitEdi/TipusMissatgeEdi, no como código."
  - term: "Sentit"
    definition: "Dirección del mensaje (entrada/salida), campo real de MissatgeEdi y de TipusMissatgeEdi — hoy string libre, candidato a enum tipado en el modelo destino."
  - term: "APERAK"
    definition: "Mensaje EDIFACT de acuse/confirmación de aplicación. En SÒSTRAT hay 7 implementaciones distintas, una por circuito de negocio — este bounded context no las posee, solo transporta la respuesta."
integration_patterns:
  - pattern: "published-language"
    with_context: "bc-marpol-residuos-v1"
    direction: "downstream"
  - pattern: "published-language"
    with_context: "bc-mmpp-v1"
    direction: "downstream"
  - pattern: "published-language"
    with_context: "bc-manifiestos-v1"
    direction: "downstream"
  - pattern: "published-language"
    with_context: "bc-transporte-terrestre-v1"
    direction: "downstream"
  - pattern: "published-language"
    with_context: "bc-aduanas-contenedores-v1"
    direction: "downstream"
  - pattern: "published-language"
    with_context: "bc-cruceros-v1"
    direction: "downstream"
  - pattern: "published-language"
    with_context: "bc-facturacion-v1"
    direction: "downstream"
  - pattern: "ACL"
    with_context: "Portic (sistema externo, EDIFACT)"
    direction: "upstream"
upstream_contexts: []
downstream_contexts:
  - "bc-marpol-residuos-v1"
  - "bc-mmpp-v1"
  - "bc-manifiestos-v1"
  - "bc-transporte-terrestre-v1"
  - "bc-aduanas-contenedores-v1"
  - "bc-cruceros-v1"
  - "bc-facturacion-v1"
related_systems:
  - "SOSTRAT-Sostrat-MJ8 (mvc.control.MissatgeEDI/CircuitEDI/AlarmaEDI/ErrorEDI, service/edi)"
  - "Portic (hub EDIFACT de la comunidad portuaria de Barcelona)"
tech_stack:
  - ".NET"
  - "Azure SQL"
  - "Azure Service Bus"
  - "APIM"
proposed_date: "2026-07-15"
approved_date: null
source: "apb-agent-ddd-v1.0"
notes: "Creado a partir de discovery/ddd-sostrat-mj8/edi-event-architecture-analysis.md, a petición explícita del usuario ('analiza la mejor forma de transformar la mensajería EDI/ventana única a una arquitectura de eventos y en qué dominio encajaría'). Resuelve la divergencia abierta en catalog-comparison.md:44 ('¿EDI es un dominio propio o un patrón repartido?'): ambos, en capas distintas — este bounded context posee solo transporte/traducción; el parsing de negocio se queda repartido en los 7 dominios consumidores. dom-integraciones-edi-v1 tenía bounded_contexts: [] vacío antes de esta propuesta."
---

# Integración EDI / Portic (Gateway de Transporte)

## Responsabilidad

Este bounded context es responsable de: (1) mantener la conexión física/protocolo con Portic (SOAP, WSDL `ApbEdiWS.wsdl`/`PortICWS.wsdl`), (2) persistir y auditar cada mensaje EDI que entra o sale (`MissatgeEdi`, `ErrorEdi`, `LiniaDeMissatgeEdi`), (3) enrutar cada mensaje entrante hacia el bounded context de negocio correcto según el catálogo `CircuitEdi`/`TipusMissatgeEdi` (dato, no código), y (4) recibir comandos de envío desde los BCs de negocio y traducirlos a la llamada SOAP real hacia Portic.

## Lo que NO incluye

No parsea el contenido de negocio de ningún mensaje EDIFACT/XML (eso vive en cada BC de negocio: WASDIS en `bc-marpol-residuos-v1`, HAZMAT/IFTDGN en `bc-mmpp-v1`, IFCSUM/CUSCAR-familia en `bc-manifiestos-v1`, CODECO/COPINO en `bc-transporte-terrestre-v1`, COARRI en `bc-aduanas-contenedores-v1`, PAXLST en `bc-cruceros-v1`, INVOIC en `bc-facturacion-v1`). No genera ninguna de las 7 respuestas APERAK de negocio existentes — solo transporta el mensaje de respuesta que cada BC de negocio construye. No incluye VUA/SAPL ni DMS — ninguno de los dos usa el modelo `MissatgeEdi`/`CircuitEdi` (persistencia y mecanismo de transporte propios, ver `bc-vua-sapl-v1`/`bc-dms-emswe-v1`). No incluye el circuito de Posicionamiento (18 sub-flujos) — hallazgo pendiente de investigación dedicada, `PLAN_FASES_FUTURAS.md #102`.

## Modelo de Dominio

### Aggregates

| Aggregate | Responsabilidad |
|-----------|----------------|
| `MissatgeEdi` | Cabecera de mensaje EDI: `nummissatge` (PK), `sentit` (dirección), `estmissatge`, `nummisorigen` (encadena respuesta↔original), `busemissor`/`busreceptor`, `nomfitxer` |

### Entidades de soporte

`TipusMissatgeEdi` (tabla de ruteo real circuito→sentido, ya modelada como datos), `CircuitEdi` (catálogo de circuitos), `ProcesEdi` (última ejecución por circuito, hoy alimenta el cron dinámico de los batch), `ErrorEdi`/`LiniaDeMissatgeEdi` (genuinamente compartidas y reutilizadas hoy por COARRI/PAXLST/otros), `TipusDAlarmaEdi`/`AlarmaEDI`/`BustiaEDI`/`UsuariCircuitEDI` (parametrización/mantenimiento, hoy 26 rutas Struts CRUD).

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| `MensajeEdiEnviado` | emitido | Confirmación de que un mensaje solicitado vía comando se envió correctamente a Portic. |
| `MensajeEdiRechazado` | emitido | El envío a Portic falló (validación, rechazo del hub, timeout). |
| `ErrorEdiRegistrado` | emitido | Nuevo registro en `ErrorEdi` — alimenta un dashboard de errores EDI transversal. |
| *(un evento por mensaje entrante, filtrable por `circuito`)* | emitido | Ver `edi-event-architecture-analysis.md §5` para la topología de topic/filtro — no se modela como un único evento fijo porque el payload varía por circuito; se resuelve con un canal único + filtro SQL por propiedad `circuito`. |

## Relaciones con Otros Bounded Contexts

Patrón `published-language`/ACL hacia los 7 bounded contexts de negocio consumidores (ver frontmatter) — publica el mensaje EDI ya traducido a CloudEvent, cada consumidor decide su propia interpretación de negocio. Patrón `ACL` hacia Portic (sistema externo): traduce el modelo EDIFACT/XML de Portic al modelo interno DOCKS y viceversa, sin que ningún BC de negocio conozca el protocolo SOAP real.

## Implementación Actual

Implementado en SÒSTRAT bajo `org.apb.sostrat.mvc.control.{MissatgeEDI,CircuitEDI,AlarmaEDI,ErrorEDI,BustiaEDI,ProcesEDI,TipusSentitEDI,TipusDAlarmaEDI,EstatEDI,LiniaMissatgeEDI}Action` (~26 rutas Struts del paquete raíz, mantenimiento/parametrización) + `service/edi/` (lógica de transporte: `CN_EDI_HELPER_COMMONS_Impl.enviar()` invoca `TraductorEDIWebServicesService.sendMessageOracle()`, WSDL `service/edi/ws/wsdl/ApbEdiWS.wsdl`; `PortICWS.wsdl` como cliente de consulta síncrona usado también por transporte terrestre, `CN_Portic_Impl.java:111-146`). El punto de entrada genérico que hace el primer `INSERT` en `MISSATGE_EDI` para los circuitos de solo-batch (COARRI/CODECO/WASDIS/HAZMAT/IFTDGN/IFCSUM/PAXLST/BERMAN) no se localizó en el checkout disponible — posible límite de esta investigación (podría vivir en `sostratWSCXF` bajo un endpoint Axis 1.x no cubierto, o requerir acceso a librerías compiladas). Confirmar con el equipo antes de fijar el diseño de ingesta definitivo del nuevo servicio.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-15 | APB AI Framework | Propuesta inicial, a petición explícita del usuario. Grounded en investigación de código real (`edi-event-architecture-analysis.md`) — MissatgeEdi/TipusMissatgeEdi/CircuitEdi/ProcesEdi/ErrorEdi/LiniaDeMissatgeEdi confirmados como modelo genuinamente compartido; parsing de negocio confirmado como 100% repartido (7 implementaciones de APERAK sin clase base común). |
