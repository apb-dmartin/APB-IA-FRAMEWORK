# [IA-GEN] Dossier — MMPP (Mercancías Peligrosas)

> **Borrador generado por IA** (APB AI Framework — síntesis de apb-disc-spec-gen-v1.0/apb-pm-product-analysis-v1.0/apb-arch-c4-model-v1.0/apb-arch-decompose-v1.0) — pendiente validación humana. No distribuir sin revisión.

## 1. Cabecera

- **Nombre**: MMPP (Mercancías Peligrosas)
- **Dominio DDD**: `dom-mercancias-peligrosas-v1` (bounded context origen `bc-mmpp-v1`)
- **Fase del roadmap**: 3 (EPIC-09, junto con PIF)
- **Estado**: `discovered`, borrador IA — pendiente validación humana
- **Documentos base**: `proposals/bc-mmpp-v1.md`, `specs/openapi-mmpp.yaml`, `specs/asyncapi-fase3.yaml`, `jira-backlog.md` EPIC-09, `ui-screens-backlog.md` (App: MMPP, Fase 3), `testing-strategy-fase2-4.md` §Fase 3, `threat-model-fase2-4.md` amenaza #14, `decomposition-roadmap.md` §Fase 0 y §Fase 3, `dead-code-register.md` #7 y #14, `events-catalog.md` §9 y §13, `discovery-summary.md`, `coverage-audit.md`

## 2. Resumen ejecutivo

MMPP gestiona el ciclo de vida regulatorio de las mercancías peligrosas que transitan por el puerto: notificación a las autoridades, autorización de manipulación e inspección, con un circuito EDI propio (subcarpeta `edi/`) que conecta con `sostrat-BATCH`. Es, según `discovery-summary.md`, uno de los pocos contextos "sólidos y autocontenidos" del monolito, con implementación real bajo `sostrat/src/org/apb/sostrat/service/mmpp/{gestion,hazmat,inspecciones,maestros,edi,util}`.

El hallazgo más relevante de esta extracción no es funcional sino estructural: MMPP es **dueño accidental** del dato maestro de Equipamiento (`Equipament.java`, tabla `EQUIPAMENT`), que vive físicamente en `dataaccess/dto/mmpp/maestros/` pero es consumido directamente por 54 ficheros de 6 dominios distintos (Manifiestos, Coarri, Aduanas, Depotsis, Liquidación, Terminales). El roadmap de descomposición trata esta extracción como **prerequisito de Fase 0** (`bc-datos-maestros-equipamiento-v1`), antes de poder extraer MMPP con propiedad limpia. Este dossier cubre MMPP como negocio (autorizaciones/notificaciones); el maestro de Equipamiento se documenta como dependencia externa, no como parte de este dominio.

Se han confirmado en el código dos bloques de código muerto propios de este ámbito (`CN_CargaIMDGExcel_Impl.java:350`, `CN_MMPP_Hazmat_Impl.java:701`) que no deben migrarse.

## 3. Análisis funcional

### Actores
- Gestor de mercancías peligrosas (negocio interno APB) — solicita autorizaciones.
- Autoridad competente — receptora de la notificación EDI (`viaedi=S`).
- Consignatario MMPP (`idconsignatarimmpp`, campo real de `MmppNotif`).
- Circuito batch EDI (`LanzarCircuitoNotificacionMPTasklet.java`, confirmado en `sostrat-BATCH/src/org/apb/sostrat/batch/tasklet/`), disparado por los jobs `sostrat-batch-MMPPNotificacionEDI.xml` y `sostrat-batch-MMPPListaDeCargaEDI.xml` (ambos confirmados presentes en `sostrat-BATCH/src/`).

### Casos de uso grounded
1. **Registrar notificación de mercancía peligrosa** (`MmppNotifAction`, ruta `/mmppNotif`) — alta de `MmppNotif` con datos de transporte de entrada (y, si aplica, de salida).
2. **Enviar notificación por circuito EDI** (`viaedi=S` en `MmppNotif`) — dispara el circuito batch hacia las autoridades.
3. **Solicitar autorización de manipulación** (`MmppAutoritzacioAction`, ruta `/mmppAutoritzacio`) — alta de `MmppAutoritzacio` referenciando `idnotificacio`.
4. **Consultar motivo de rechazo** — campos reales `idmotiurebuig`/`descmotiurebuig` de `MmppAutoritzacio`.
5. **Registrar partida asociada a la notificación** (`MmppNotifPartidaAction`, ruta `/mmppNotifPartida`) — vínculo con `PartidaMmpp` (ver dependencia bidireccional, §7).
6. **Gestionar equipamiento asociado a la notificación** (`MmppNotifEquipamentAction`, ruta `/mmppNotifEquipament`).
7. **Inspección de MMPP en contenedor/granel/documental/cisterna** (`service/mmpp/inspecciones/`, 5 Action classes confirmadas: `InspeccionMMPPAction`, `InspeccionContenedorMMPPAction`, `InspeccionGranelMMPPAction`, `InspeccionDocumentalMMPPAction`, `InspeccionCisternaMMPPAction`, `InspeccionDocsAdjuntosMMPPAction`).
8. **Circuito EDI Hazmat (IFTDGN)** — `service/mmpp/edi/{hazmat,iftdgn,mpautt,notificacion,consolidacion}`, con DTOs `HazmatE*`/`HazmatS*` (segmentos EDIFACT: BGM, CNI, COM, CTA, DGS, DTM, EQD, FTX, GID, LOC, MEA, NAD, PCI, RFF, SGP, TDT, UNH, UNT) bajo `dataaccess/dto/mmpp/hazmat/`.
9. **Consulta del catálogo de clases MMPP y motivos de rechazo** (`service/mmpp/maestros/`: `ClaseMMPPAction`, `MotivoRechazoAction`, `CondicionSeguridadAction`, `ContactoGeneralAction`, `CisternaCertificadoAction`, `MaestroMMPPAction`, `ExpedidorReceptorMMPPAction`, `CargaIMDGExcelAction`).

### Reglas de negocio confirmadas
- `MmppAutoritzacio.viaedi` por defecto `"N"`; `automatic` por defecto `"N"`; `envaut` por defecto `"N"` — hay un flujo de autorización automática distinto del manual (campo `automatic`, tabla auxiliar `MmppAutoritzacioAutomatica` confirmada en `dataaccess/dto/mmpp/gestion/`).
- `MmppNotif.bloquejat` por defecto `"N"` y `semiautomatica` por defecto `"N"` — existe un tercer modo de tramitación (semiautomática) no documentado en la propuesta original, descubierto al leer el DTO real.
- El DTO `MmppNotif` duplica literalmente el bloque de datos de transporte para "entrada" (`idtipustransentrada`, `numviatgeentrada`, `idvaixellentrada`, `matvehentrada`, …) y "sortida" (`idtipustranssortida`, `numviatgesortida`, `idvaixellsortida`, `matvehsortida`, …) — confirmado en el propio código fuente (61 campos totales en `MmppNotif.java`) y ya señalado como patrón a rediseñar en `events-catalog.md` §9 y `ui-screens-backlog.md` (pestañas "Entrada"/"Salida" en la ficha).
- El circuito EDI de notificación no debe ser invocable si `idnotificacio` no está en un estado previo válido (`testing-strategy-fase2-4.md` §Fase 3).

### Qué NO incluye
- No es propietario del dato maestro de Equipamiento (`Equipament.java`) en el modelo objetivo — lo aloja hoy por herencia histórica (ver §7).
- No incluye PIF (control fronterizo, `bc-pif-v1`) — comparte fase y dependencia de Equipamiento pero es un bounded context propio, con régimen regulatorio distinto (`discovery-summary.md`: "confirma hipótesis, naturaleza regulatoria distinta de MMPP").
- No incluye la clasificación arancelaria/ONU de la partida en sí (`numonu`, `classemmpp` viven en `PartidaVersio.java`, propiedad de Manifiestos — ver dependencia bidireccional en §7).

## 4. Alcance de migración — qué se migra y qué NO por no estar en uso

**Se migra:**
- Los subpaquetes `gestion`, `hazmat`, `inspecciones`, `edi` de `service/mmpp/` (tarea técnica explícita de EPIC-09: *"Migrar los subpaquetes `hazmat`, `inspecciones`, `edi` de MMPP a la nueva estructura de servicio"*).
- Los agregados `MmppAutoritzacio` (tabla `MMPP_AUTORITZACIO`) y `MmppNotif` (tabla `MMPP_NOTIF`), con sus entidades hijas (`MmppNotifPartida`, `MmppNotifEquipament`, `MmppHazmatPartida`, `MmppHazmatEquipament`, confirmadas en `dataaccess/dto/mmpp/{gestion,hazmat}/`).
- El subpaquete `maestros` **excepto** el dato `Equipament.java` (que se extrae a `bc-datos-maestros-equipamiento-v1`, no se migra dentro de MMPP).

**Código muerto confirmado en este ámbito — NO se migra bajo ningún escenario** (`dead-code-register.md` #7 y #14, verificados directamente contra el código fuente en esta sesión):

| # | Fichero | Línea | Evidencia textual | Estado verificado |
|---|---------|-------|--------------------|--------------------|
| 1 | `sostrat/src/org/apb/sostrat/service/mmpp/maestros/impl/CN_CargaIMDGExcel_Impl.java` | 350 | Comentario del desarrollador: *"ya no se usa debido a la MMPP-390"*, sobre el método comentado `todasRepeticionesMismaDenominacion(...)` | **Confirmado presente**, bloque comentado completo, verificado línea por línea en esta sesión |
| 2 | `sostrat/src/org/apb/sostrat/service/mmpp/hazmat/impl/CN_MMPP_Hazmat_Impl.java` | 701 | Comentario del desarrollador: *"NO SE USA"* junto a *"MMPP-185 buscar y crear un contacto tambien si no existe el segmento CTA"*, sobre la llamada comentada `CommonUtil.creaContactoSinCTA(...)` | **Confirmado presente**, verificado línea por línea en esta sesión |

**No se migra (fuera de MMPP, aunque hoy resida en su paquete)**: `Equipament.java` (tabla `EQUIPAMENT`, PK `idequipament`) — se extrae como dato maestro compartido hacia `bc-datos-maestros-equipamiento-v1`, prerequisito de Fase 0 (`decomposition-roadmap.md` §Fase 0). MMPP pasa a **consumirlo** vía `/api/v1/container-equipment` en lugar de alojarlo.

**Corrección de conteo frente a la propuesta original**: `bc-mmpp-v1.md` estima "~35 rutas Struts propias". La verificación directa contra `struts-config.xml` en esta sesión encuentra **58 entradas `<action>`** bajo `org.apb.sostrat.mvc.control.mmpp*` (incluyendo variantes `_popup` de la misma pantalla), que mapean a **36 clases Action distintas**. `discovery-summary.md` (línea 36) ya recogía el conteo de 58 rutas para el módulo `mmpp`, consistente con esta verificación — el número "~35" de la propuesta original probablemente contaba solo clases Action, no rutas. Se usa 58 rutas / 36 clases como cifra verificada para el resto de este documento.

## 5. Modelo de datos

Grounded en `dataaccess/dto/mmpp/gestion/MmppAutoritzacio.java` y `MmppNotif.java`, leídos íntegramente en esta sesión contra `SOSTRAT-Sostrat-MJ8`.

### `MmppAutoritzacio` (tabla `MMPP_AUTORITZACIO`, PK `idautoritzacio`)

| Campo | Tipo Java | Columna origen | Notas |
|---|---|---|---|
| idautoritzacio | Long | IDAUTORITZACIO | PK |
| idnotificacio | Long | IDNOTIFICACIO | FK a `MmppNotif` |
| idresolucio | String | IDRESOLUCIO | |
| dataautoritzada | Date | DATAAUTORITZADA | |
| datafiautoritzada | Date | DATAFIAUTORITZADA | |
| textinsadicional | String | TEXTINSADICIONAL | |
| idalineacio | Integer | IDALINEACIO | |
| llocdeposit | String | LLOCDEPOSIT | |
| idmotiurebuig | String | IDMOTIUREBUIG | |
| descmotiurebuig | String | DESCMOTIUREBUIG | |
| viaedi | String | VIAEDI | default `"N"` |
| automatic | String | AUTOMATIC | default `"N"` — flujo de autorización automática |
| document | byte[] | DOCUMENT | BLOB |
| datalta / datmodificacio | Date | DATALTA / DATMODIFICACIO | auditoría |
| idopealta / idopemodificacio | String | IDOPEALTA / IDOPEMODIFICACIO | auditoría |
| idprocalta / idprocmodificacio | String | IDPROCALTA / IDPROCMODIFICACIO | auditoría |
| guid | Long | GUID | |
| envaut | String | ENVAUT | default `"N"` |

Tabla auxiliar confirmada pero no leída en profundidad: `MmppAutoritzacioAutomatica.java` (autorización automática), `MmppAutoritzacioCondicions.java` (condiciones asociadas), `MmppAutoritzacioEnviament.java` (envío).

### `MmppNotif` (tabla `MMPP_NOTIF`, PK `idnotificacio`)

61 campos confirmados; se listan los funcionalmente relevantes (el resto son duplicados simétricos "entrada"/"sortida" o auditoría estándar):

| Campo | Tipo Java | Columna origen | Notas |
|---|---|---|---|
| idnotificacio | Long | IDNOTIFICACIO | PK |
| idestat | String | IDESTAT | |
| idsubport / anyescala / numescala | String / Integer / Integer | IDSUBPORT / ANYESCALA / NUMESCALA | referencia a la escala (`Escala`, `dom-operaciones-maritimas-v1`) |
| seqnotificacio | Integer | SEQNOTIFICACIO | |
| numreferencia / numrefrenciaoriginal | String | NUMREFERENCIA / NUMREFRENCIAORIGINAL | |
| idnotificaciooriginal | Long | IDNOTIFICACIOORIGINAL | auto-referencia (rectificaciones) |
| datarecdocument / dataemidocument | Date | DATARECDOCUMENT / DATAEMIDOCUMENT | |
| idtipustransentrada, numviatgeentrada, numvehientrada, coditransentrada, idvaixellentrada, matvehentrada, nomtransentrada, idpaisvaixellentrada, idsubportescentrada, anyescalaentrada, numescalaentrada, idserveiferentrada | (bloque "entrada", 12 campos) | | duplicado simétrico de "sortida" |
| idtipustranssortida, numviatgesortida, numvehisortida, coditranssortida, idvaixellsortida, matvehsortida, nomtranssortida, idpaisvaixellsortida, idsubportescsortida, anyescsortida, numescsortida, idserveifersortida | (bloque "sortida", 12 campos) | | duplicado simétrico de "entrada" |
| escentaveria, escentrcert54, escentaptitud, escentdocumentacio | String | (bloque "entrada" avería/certificados) | |
| escsortaveria, escsortcert154, escsortaptitud, escsortdocumentacio | String | (bloque "sortida" avería/certificados) | |
| idlocportanterior / idlocportseguent | Integer | IDLOCPORTANTERIOR / IDLOCPORTSEGUENT | |
| dataarribada / datasortida | Date | DATAARRIBADA / DATASORTIDA | |
| horesdescarrega / horescarrega / tempsestada | Integer / Integer / Long | HORESDESCARREGA / HORESCARREGA / TEMPSESTADA | |
| idconsignatarimmpp | String | IDCONSIGNATARIMMPP | |
| viaedi | String | VIAEDI | |
| art15 | String | ART15 | referencia normativa explícita en el propio nombre de campo |
| datacancelacio / dataactivacio / dataresolucio / dataanulacio | Date | (ciclo de vida) | 4 fechas de estado distintas |
| numdocument | String | NUMDOCUMENT | |
| idestatnotificaciooriginal | String | IDESTATNOTIFICACIOORIGINAL | |
| bloquejat | String | BLOQUEJAT | default `"N"` |
| semiautomatica | String | SEMIAUTOMATICA | default `"N"` |
| guid, datalta, datmodificacio, idopealta, idopemodificacio, idprocalta, idprocmodificacio | (auditoría estándar) | | |

### Mapeo Azure SQL

Sin diseño físico confirmado — `openapi-mmpp.yaml` expone únicamente los campos usados en los endpoints reales (subconjunto de los de arriba); no hay evidencia de un DDL Azure SQL ya definido. **Gap explícito**: el mapeo campo-a-campo completo hacia Azure SQL queda pendiente de diseño físico (ver §14).

### Dato maestro NO propio (dependencia externa)

`Equipament.java` (tabla `EQUIPAMENT`, PK `idequipament`) — 6 campos confirmados (`idequipament`, `refequipament`, `matriculaiso`, `idtipequipament`, `propietari`, `idoridade`), deliberadamente sin peso/tara/dimensiones/estado (`events-catalog.md` §13). MMPP consume este maestro vía `/api/v1/container-equipment`, no lo aloja.

## 6. Arquitectura técnica

Microservicio DOCKS independiente (`.NET` / Azure SQL / Azure Service Bus, según `tech_stack` de `bc-mmpp-v1.md`), expuesto vía Azure API Management, autenticado con Entra ID (client credentials, scopes `mmpp.read`/`mmpp.write`, confirmado en `openapi-mmpp.yaml`). Consume el servicio de Datos Maestros de Equipamiento (Fase 0) en lugar de alojar el maestro de contenedores directamente. El circuito EDI de notificación a autoridades se mantiene como integración asíncrona con reintento y backoff (ver §10, §13).

## 7. Dominio DDD

- **Bounded context**: `bc-mmpp-v1` → dominio `dom-mercancias-peligrosas-v1`.
- **Confirmación cruzada catálogo top-down / código bottom-up**: `catalog-comparison.md` señala "coincidencia casi exacta" entre `bc-mmpp-v1` y el dominio existente `dom-mercancias-peligrosas-v1` del catálogo — ambos análisis, independientes, aíslan MMPP por su régimen regulatorio ADR/IMO.
- **No es propietario del dato maestro de Equipamiento**: aunque `Equipament.java` vive físicamente en `dataaccess/dto/mmpp/maestros/`, es consumido por 6 dominios distintos (54 ficheros confirmados: Manifiestos, Coarri, Aduanas, Depotsis, Liquidación, Terminales — `coverage-audit.md`, `discovery-summary.md`). El modelo objetivo lo extrae a `bc-datos-maestros-equipamiento-v1` (`parent_domain: dom-mercancias-v1`), con relación `published-language` downstream desde MMPP.
- **No hay solapamiento entre `bc-mmpp-v1` y `bc-datos-maestros-equipamiento-v1`**: `bc-datos-maestros-equipamiento-v1.md` declara explícitamente que "no gestiona el traslado, tránsito, manifiesto ni ninguna operación de negocio sobre el contenedor — solo su identidad y atributos maestros" (6 campos). MMPP conserva toda la lógica de negocio (notificación, autorización, inspección); el maestro solo aporta identidad de equipamiento. La relación está declarada en ambos ficheros de propuesta como `pattern: published-language`, `direction: downstream` (desde el maestro hacia MMPP).
- **Dependencia bidireccional confirmada con Manifiestos**: `PartidaMmpp.java` (tabla `PARTIDA_MMPP`) vive en `dataaccess/dto/manifiestos/gestion/`, no en el paquete de MMPP — es decir, el dato que vincula una notificación MMPP con una partida de manifiesto es propiedad física de Manifiestos, no de MMPP, exactamente al revés del caso de Equipamiento. Confirmado por lectura directa de `PartidaMmpp.java` en esta sesión (campos `notificaciopartida`, `partida`, más auditoría estándar). `bc-mmpp-v1.md` ya documentaba esta relación como `pattern: conformist`, `direction: bidirectional` con `bc-manifiestos-v1`. La clasificación arancelaria/ONU de la partida (`numonu`, `classemmpp`) es propiedad de `PartidaVersio.java` en Manifiestos, no de MMPP — MMPP consulta, no posee, ese dato (ver historia de usuario 3 de EPIC-10 en `jira-backlog.md`).
- **Relación con PIF**: mismo EPIC-09, misma dependencia de EPIC-00 (Equipamiento), pero bounded context propio — sin agregados compartidos confirmados en el código entre `service/mmpp/` y `service/pif/`.

## 8. Pantallas UI

Grounded en `ui-screens-backlog.md` §Fase 3, "App: MMPP":

1. **Listado de Notificaciones MMPP** (`dxDataGrid`) — columnas: `idnotificacio`, `idestat`, `idsubport/anyescala/numescala`, `datarecdocument`.
2. **Ficha de Notificación** (`dxForm` + `dxTabPanel`) — pestaña "Entrada" y pestaña "Salida", reflejando el duplicado real del DTO (`events-catalog.md` §9).
3. **Listado de Autorizaciones MMPP** (`dxDataGrid`) — columnas: `idautoritzacio`, `idresolucio`, `dataautoritzada/datafiautoritzada`, `idmotiurebuig`.

**Referencia cruzada confirmada**: la pantalla de Manifiestos incluye un "Indicador visual de mercancía peligrosa" (badge condicional cuando `numonu`/`classemmpp` no están vacíos) con enlace cruzado a la ficha MMPP correspondiente — evidencia adicional de la dependencia bidireccional del §7.

No se han identificado pantallas propias para inspecciones (`service/mmpp/inspecciones/`) ni para el circuito EDI Hazmat en `ui-screens-backlog.md` — **gap de evidencia**, ver §14.

## 9. APIs

Grounded en `specs/openapi-mmpp.yaml` (`x-source-evidence: MmppAutoritzacio.java, MmppNotif.java`).

| Método | Ruta | Operación | Fuente de campos |
|---|---|---|---|
| GET | `/dangerous-goods-notifications` | listNotifications (filtros `idestat`, `numescala`, `cursor`) | `MmppNotif` |
| POST | `/dangerous-goods-notifications` | createNotification | `MmppNotif` |
| POST | `/dangerous-goods-notifications/{idnotificacio}/send` | sendNotification (dispara circuito EDI, `viaedi=S`) | `MmppNotif` |
| POST | `/dangerous-goods-authorizations` | createAuthorization | `MmppAutoritzacio` |
| GET | `/dangerous-goods-authorizations/{idautoritzacio}` | getAuthorization | `MmppAutoritzacio` |

Seguridad: OAuth2 client credentials vía Entra ID, scopes `mmpp.read`/`mmpp.write`. Ver especificación completa en `specs/openapi-mmpp.yaml`.

**Nota de alcance**: la especificación OpenAPI actual solo cubre `gestion` (notificaciones/autorizaciones). Los subpaquetes `hazmat`, `inspecciones` y `edi` no tienen contrato API diseñado todavía — ver §14.

## 10. Eventos

Grounded en `specs/asyncapi-fase3.yaml` (canal `evt.sostrat.mmpp`, DLQ `evt.sostrat.mmpp.dlq`).

| Evento | Payload (`x-data-schema`) | Campos clave | Manejo de error |
|---|---|---|---|
| `AutorizacionMMPPConcedida` | `AutorizacionMmppData` | `idautoritzacio` (req.), `idnotificacio`, `idresolucio` | DLQ estándar del canal |
| `NotificacionMMPPEnviada` | `NotificacionMmppData` | `idnotificacio`+`idestat` (req.), `idsubport`, `anyescala`, `numescala`, `viaedi` | Reintento con backoff; tras agotar reintentos, DLQ + alerta a operaciones (plazo regulatorio en juego) |

Ambos envueltos en `CloudEventEnvelope` (CloudEvents 1.0). Ver especificación completa en `specs/asyncapi-fase3.yaml`.

## 11. Diagrama topológico (C4 nivel 1)

```mermaid
flowchart LR
    subgraph MMPP["MMPP (DOCKS, nuevo)"]
        API[API REST<br/>dangerous-goods-*]
        EDI[Circuito EDI<br/>notificación autoridades]
        EVT[evt.sostrat.mmpp]
    end
    subgraph EQUIP["bc-datos-maestros-equipamiento-v1<br/>(Fase 0, prerequisito)"]
        EQAPI[/api/v1/container-equipment]
    end
    subgraph MANIF["bc-manifiestos-v1"]
        PART[PartidaMmpp<br/>tabla PARTIDA_MMPP]
    end
    subgraph AUT["Autoridad competente"]
        REG[Receptor EDI]
    end
    GESTOR[Gestor MMPP] --> API
    API --> EDI
    EDI -- "viaedi=S, reintento+backoff" --> REG
    API -- "consulta idequipament" --> EQAPI
    MANIF -- "conformist, bidireccional" --> API
    API -.-> PART
    API --> EVT
    EVT -- "AutorizacionMMPPConcedida" --> DOWNSTREAM1[Consumidores internos]
    EVT -- "NotificacionMMPPEnviada" --> DOWNSTREAM1
```

## 12. Estrategia de convivencia con el modelo actual

1. **Dependencia dura de EPIC-00**: MMPP no puede extraerse con propiedad de dato limpia hasta que `/api/v1/container-equipment` esté en producción (criterio de éxito explícito de EPIC-00: *"al menos 1 dominio piloto"* consumiéndolo en modo lectura). Hasta entonces, MMPP sigue leyendo `Equipament.java` directamente.
2. **Réplica CDC Oracle → Azure SQL** de `MMPP_NOTIF`/`MMPP_AUTORITZACIO` como paso intermedio, mismo patrón que el resto de Fase 3 (`decomposition-roadmap.md` §Fase 0: "Réplica de lectura Oracle → Azure SQL (CDC) para los primeros servicios extraídos").
3. **Coexistencia del circuito EDI**: mientras dure la transición, el job `sostrat-batch-MMPPNotificacionEDI.xml` (tasklet `LanzarCircuitoNotificacionMPTasklet.java`, confirmado) sigue siendo la referencia de comportamiento esperado para el nuevo endpoint `POST .../send` (`testing-strategy-fase2-4.md` §Fase 3).
4. **Resolución de la dependencia bidireccional con Manifiestos**: dado que `PartidaMmpp` es propiedad física de Manifiestos, la extracción de MMPP debe secuenciarse considerando el estado de EPIC-10 (Manifiestos) — no es una dependencia técnica dura documentada, pero sí un acoplamiento de datos real que requiere decidir de qué lado vive el contrato (`bc-mmpp-v1.md`: `pattern: conformist`, MMPP como conformista de Manifiestos).
5. **Carga Inicial / ETL**: el código de entidad `MAMMPP` en `CargaInicial.java` requiere un plan de retirada explícito una vez MMPP complete su migración a Azure SQL, para no dejar el proceso batch huérfano contra un AS400 que ya no sería fuente de verdad (`jira-backlog.md`, tarea técnica #7 de EPIC-12/Carga Inicial).

## 13. Testing y seguridad

**Testing** (`testing-strategy-fase2-4.md` §Fase 3):
- Unit: `POST .../send` (circuito EDI) no debe ser invocable si `idnotificacio` no está en un estado previo válido.
- E2E: notificación → autorización → envío EDI, con el circuito batch real de `LanzarCircuitoNotificacionMPTasklet.java` como referencia de comportamiento esperado.
- Test de contrato compartido transversal (Fase 2-4): MMPP (junto con Manifiestos, PIF, Aduanas) no debe fallar si el maestro de Equipamiento devuelve solo sus 6 campos reales — no asumir campos operativos inexistentes.
- Ningún test de MMPP debe apuntar a Oracle directamente — siempre contra la réplica CDC en Azure SQL de test.

**Seguridad** (`threat-model-fase2-4.md`, amenaza #14):
- **Denial of Service**: el circuito EDI de MMPP (notificación a autoridades) sin política de reintento acotada podría generar reintentos infinitos que saturen la cola ante un fallo del sistema externo. Severidad: **Media**. Mitigación: máximo de reintentos con backoff exponencial y DLQ explícita — ya reflejado en `specs/asyncapi-fase3.yaml` (`x-error-handling` de `NotificacionMMPPEnviada`).
- Checklist de verificación previa a producción incluye explícitamente: *"Política de reintento/DLQ del circuito EDI de MMPP definida y probada"*.

## 14. Riesgos y gaps de evidencia

- **Mapeo físico a Azure SQL no diseñado**: `openapi-mmpp.yaml` solo expone el subconjunto de campos usado en los endpoints; el DDL completo de destino no está confirmado.
- **Subpaquetes `hazmat`, `inspecciones`, `edi` sin contrato API diseñado**: `openapi-mmpp.yaml` cubre únicamente `gestion` (notificaciones/autorizaciones). La tarea técnica de EPIC-09 de migrar estos subpaquetes está pendiente de diseño de contrato.
- **Pantallas de inspección y EDI Hazmat no confirmadas en `ui-screens-backlog.md`**: solo hay 3 pantallas documentadas (notificaciones, ficha, autorizaciones); no hay evidencia de pantallas propias para `service/mmpp/inspecciones/` (5-6 Action classes confirmadas en código) ni para el circuito EDI Hazmat — puede ser un vacío de análisis o funcionalidad ya cubierta por otra pantalla no diferenciada.
- **Dependencia con Manifiestos no resuelta en el diseño de contrato**: `PartidaMmpp` es propiedad física de Manifiestos; no hay decisión documentada de qué servicio expone el vínculo notificación-partida en el modelo objetivo.
- **Corrección de conteo de rutas**: la propuesta original estimaba ~35 rutas; la verificación de esta sesión confirma 58 entradas `<action>` / 36 clases distintas (ver §4). No cambia el alcance funcional, pero sí el esfuerzo de migración de UI.
- **Catálogo `MmppAutoritzacioAutomatica`/`MmppAutoritzacioCondicions`/`MmppAutoritzacioEnviament` no leído en profundidad**: se confirma su existencia en `dataaccess/dto/mmpp/gestion/`, pero no se han extraído sus campos — el flujo de autorización automática (`automatic="S"`) puede tener reglas de negocio adicionales no documentadas aquí.
- **Confirmar con negocio**: si el motivo de rechazo de autorización (`idmotiurebuig`) tiene un catálogo cerrado de valores o es texto libre — no confirmado en el DTO.

## 15. Estimación de esfuerzo

Ver `jira-backlog.md` EPIC-09 — historias de usuario estimadas en story points para MMPP y PIF conjuntamente:
1. Solicitar autorización (`POST /dangerous-goods-authorizations`) — 8 pts.
2. Notificación EDI automática a autoridades (`viaedi=S`) — 8 pts.
3. Consultar motivo de rechazo — 3 pts.
(Las historias 4 y 5 de EPIC-09 corresponden a PIF, no a MMPP.)

Tareas técnicas adicionales no puntuadas individualmente: migración de subpaquetes `hazmat`/`inspecciones`/`edi` (esfuerzo no desglosado — depende del diseño de contrato pendiente, ver §14). Dependencia dura de EPIC-00 (Datos Maestros de Equipamiento), cuyo esfuerzo se estima por separado en su propia épica.

## 16. Checklist de validación

**Funcional**:
- [ ] Confirmar el catálogo completo de valores de `idestat` (notificación) e `idresolucio` (autorización) con negocio — solo se conocen ejemplos puntuales (`"PENDENT"`, `"APROVADA"`), no el enum cerrado.
- [ ] Confirmar si `idmotiurebuig` es un catálogo cerrado o texto libre.
- [ ] Confirmar el alcance funcional real de las pantallas de inspección MMPP (5-6 Action classes en código, sin pantalla documentada en `ui-screens-backlog.md`).
- [ ] Validar con negocio la relación exacta entre `art15` y el resto del ciclo de vida de la notificación.

**Desarrollo**:
- [ ] Confirmar que EPIC-00 (`/api/v1/container-equipment`) está en producción antes de iniciar la extracción de MMPP.
- [ ] Diseñar el contrato API/evento para `hazmat`, `inspecciones` y `edi` (no cubierto en `openapi-mmpp.yaml`/`asyncapi-fase3.yaml` actuales).
- [ ] Decidir de qué lado (MMPP o Manifiestos) vive el contrato del vínculo `PartidaMmpp`.
- [ ] Confirmar el DDL Azure SQL completo para `MMPP_NOTIF`/`MMPP_AUTORITZACIO` y tablas hijas.
- [ ] Verificar en PR que los 2 bloques de código muerto confirmados (§4) no se copian al nuevo servicio.

## 17. Historial de cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-13 | APB AI Framework | Dossier inicial, síntesis de `discovery/ddd-sostrat-mj8/` y verificación directa contra `SOSTRAT-Sostrat-MJ8` (MmppAutoritzacio.java, MmppNotif.java, PartidaMmpp.java, struts-config.xml, CN_CargaIMDGExcel_Impl.java, CN_MMPP_Hazmat_Impl.java, sostrat-BATCH) |
