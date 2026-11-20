# [IA-GEN] Análisis de arquitectura — Transformación de la mensajería EDI/Ventanilla Única a eventos

> **Borrador generado por IA** (APB AI Framework — apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.
>
> **Origen (2026-07-15)**: tras cerrar la re-derivación de los 24 dossiers y el residuo de `coverage-audit.md`, el usuario preguntó si los batch de SÒSTRAT y la mensajería EDI/Ventanilla Única eran aplicaciones independientes en la nueva arquitectura. La respuesta fue que no está diseñado — es un vacío real, sin ninguna mención en `decomposition-roadmap.md`/`STANDARD_ARCHITECTURE.md`, y con una pregunta explícitamente abierta en `catalog-comparison.md:44` ("¿EDI es un dominio propio o un patrón repartido? Ambos enfoques son DDD-válidos"). Este documento resuelve esa pregunta con evidencia de código.

## 1. Resumen ejecutivo

**No hay un único "gateway EDI" en SÒSTRAT — coexisten 3 arquitecturas distintas bajo el mismo nombre.** La transformación correcta no es "todo a un gateway" ni "todo repartido": es una **partición en dos capas + dos excepciones**.

1. **Capa de transporte (nueva, transversal)** — un bounded context `bc-integracion-edi-portic-v1` que posee *solo* la conexión física con Portic (traducción EDIFACT, envío/recepción) y el modelo de auditoría genérico (`MissatgeEdi`, `TipusMissatgeEdi`, `CircuitEdi`, `ProcesEdi`, `ErrorEdi`, `LiniaDeMissatgeEdi`) — estos SÍ son genuinamente compartidos hoy en el código.
2. **Capa de negocio (repartida, sin mover nada)** — el parsing, la validación y la generación de respuesta (APERAK) de cada circuito EDI concreto (WASDIS, HAZMAT, IFTDGN, IFCSUM, COPINO, CODECO...) se queda dentro del bounded context de negocio que ya lo posee (MARPOL, MMPP, Manifiestos, Transporte Terrestre...) — porque hoy **ya está así**, sin ninguna clase base compartida entre circuitos (7 implementaciones de "APERAK" distintas, ninguna reutiliza código de otra).
3. **Excepción 1 — VUA/SAPL** (Ventanilla Única Aduanera española, AEAT): no comparte tabla, modelo de estado ni mecanismo de transporte con el resto. Bounded context propio, `bc-vua-sapl-v1`.
4. **Excepción 2 — DMS** (Declaración Marítima de Sanidad — este es el circuito real de la **EMSWe europea**, no VUA): mismo argumento. Bounded context propio, `bc-dms-emswe-v1`.

**Hallazgo colateral importante**: `domain-catalog/domains/integraciones-edi/domain.md` (ya existe en el catálogo real, `status: "proposed"`, `bounded_contexts: []` vacío) describe hoy la Ventanilla Única Aduanera (VUA/SAPL) como si fuera la EMSWe europea. Es una imprecisión: **VUA/SAPL es aduana nacional española (AEAT)**; el circuito que corresponde realmente a la *European Maritime Single Window environment* (Directiva UE 2019/1239, formularios FAL) es **DMS** (Declaración Marítima de Sanidad — uno de los formularios FAL). Ver §4.

## 2. Por qué no las otras dos opciones

**Se descarta un gateway EDI monolítico que también parsee negocio.** La evidencia de código (`sostrat/src/org/apb/sostrat/service/{coarri,marpol/wasdis,mmpp/edi,manifiestos/edi,paxlst,transporteterrestre/codeco}/edi/*`) muestra que la lógica de negocio de cada circuito está ya 100% duplicada por dominio, sin ninguna clase base común — hay **7 implementaciones de "APERAK" distintas** (`CN_EDI_Helper_WASDIS_APERAK`, `CN_EDI_Helper_Posicionamiento_APERAK`, `CN_EDI_Helper_Factura_APERAK`, `CN_EDI_Helper_Consolidacion_APERAK`, `CN_EDI_Helper_Notificacion_APERAK`, `CN_EDI_Helper_Preaviso_APERAK`, y la de `paxlst`), cada una desde cero. Meter todo eso en un único servicio .NET recrearía un segundo monolito detrás de una fachada nueva, ahora con el agravante de que ese servicio tendría que conocer el modelo de datos de 7 dominios de negocio distintos.

**Se descarta también "sin gateway, cada dominio con su propio adaptador SOAP completo".** El mecanismo de salida está genuinamente centralizado hoy: `CN_EDI_HELPER_COMMONS_Impl.enviar()` invoca una única operación SOAP (`sendMessageOracle`, WSDL `ApbEdiWS.wsdl`, endpoint Portic `192.168.5.52`) — SÒSTRAT persiste el mensaje en `MISSATGE_EDI` y le dice a Portic "traduce y envía este ID". Existe también un WSDL cliente compartido (`PortICWS.wsdl`: `getPendingMessages`/`getMessage`/`sendMessage`/`authenticate`) usado para consultas síncronas (transporte terrestre). Descentralizar esto obligaría a reimplementar 7-10 veces el mismo cliente SOAP, el mismo motor de reintentos y el mismo modelo de auditoría de errores (`ErrorEdi`, `LiniaDeMissatgeEdi` — estas dos sí son genuinamente compartidas y reutilizadas hoy por COARRI, PAXLST y otros circuitos por igual).

**Conclusión**: la pregunta de `catalog-comparison.md:44` ("¿dominio propio o patrón repartido? Ambos son DDD-válidos") tiene una respuesta concreta con esta evidencia — **ambos a la vez, en capas distintas**, no una disyuntiva.

## 3. Veredicto circuito a circuito

| Circuito | Dirección / mecanismo actual | Veredicto | Bounded context de negocio | Evidencia |
|---|---|---|---|---|
| **COARRI** (operaciones de terminal contenedor) | Inbound vía `MISSATGE_EDI`, batch Quartz cada 5 min | Parsing va al dominio de negocio | `bc-aduanas-contenedores-v1` (nuevo agregado `OperacionTerminal`, consolidando `service/coarri` junto con `service/aduanas`+`service/terminales`, ya pendiente de consolidación) | `sostrat-BATCH/src/sostrat-batch-CoarriEDI.xml:77`; `sostrat/src/.../service/coarri/edi/impl/CN_EDI_Helper_Procesar_COARRI_Impl.java:141-227`; `dossier-13-aduanas-contenedores.md §229` |
| **CODECO** (transporte terrestre) | Mixto: batch + consulta SOAP síncrona (`PortICWS`) | Se queda | `bc-transporte-terrestre-v1` (ya tiene `PreavisoRegistrado`/`AutorizacionConcedida`; gap `MensajeCodecoProcesado` ya anotado ahí, ver §4/§5) | `sostrat-BATCH/src/sostrat-batch-CodecoEDI.xml:78`; `sostrat/src/.../service/transporteterrestre/impl/CN_Portic_Impl.java:111-146` |
| **COPINO** (recogida/entrega mercancía, con APERAK) | Bidireccional, batch cada 5 min | Se queda | `bc-transporte-terrestre-v1` | `sostrat-BATCH/src/sostrat-batch-COPINOSEDI.xml:116`; `.../tasklet/ProcesarEdiCopinoTasklet.java:118-184` |
| **WASDIS** (MARPOL) | Inbound + APERAK propia, batch cada 5 min | Sin cambio | `bc-marpol-residuos-v1` (ya tiene `ListaResiduosMarpolGenerada`/`ResiduoPesado`; recomendación ya existente en `dossier-06-marpol-residuos.md §12`) | `sostrat-BATCH/src/sostrat-batch-MARPOLListaDeResidusEDI.xml:17` |
| **HAZMAT / IFTDGN** (MMPP) | Inbound + APERAK, batch cada 5 min | Sin cambio | `bc-mmpp-v1` (ya tiene `AutorizacionMMPPConcedida`/`NotificacionMMPPEnviada`) | `sostrat-BATCH/src/sostrat-batch-MMPPListaDeCargaEDI.xml:17`, `-MMPPNotificacionEDI.xml:17` |
| **IFCSUM / CUSCAR / CUSREP / CUSRES / CUSRP2** (Manifiestos) | Inbound, batch cada 5 min | Se queda, se completa el detalle | `bc-manifiestos-v1` (`ManifiestoRegistrado` cubre la raíz, falta evento de partida — ver §5) | `sostrat-BATCH/src/sostrat-batch-ManifiestosEDI.xml:23,108` |
| **PAXLST** (lista de pasajeros) | Inbound + APERAK propia, batch cada 5 min | Parsing va al dominio de negocio | `bc-cruceros-v1` | `sostrat-BATCH/src/sostrat-batch-PaxlstEDI.xml:17,77` |
| **BERMAN** (asociación mercancía-escala) | Inbound, vive en `serviceNoAOP` (deuda técnica, fuera del proxy transaccional estándar) | Parsing va al dominio de negocio, pendiente de la creación del BC | Futuro `bc-escalas-v1` (`dom-operaciones-maritimas-v1`), hoy bloqueado por la sesión con ARGOS | `sostrat/src/.../serviceNoAOP/berman/edi/impl/CN_EDI_Helper_BERMAN_Impl.java` |
| **DMS** (Declaración Marítima de Sanidad — circuito FAL/EMSWe real) | Bidireccional asíncrono por fichero XML (schema JAXB `MDHResponse`), NO usa `MISSATGE_EDI`, batch cada 5 min + 2 min | **Bounded context propio, nuevo** | `bc-dms-emswe-v1` — ver §4 | `sostrat-BATCH/src/sostrat-batch-DMS.xml:109,115`; `sostrat/src/.../service/escalas/dms/impl/CN_DMS_Impl.java:1019-1064` |
| **VUA/SAPL** (Ventanilla Única Aduanera, AEAT) | Bidireccional por fichero XML, 4 XSD reales de la AEAT, batch cada **1 minuto** (el más agresivo del sistema), persistencia propia | **Bounded context propio, nuevo** | `bc-vua-sapl-v1` — ver §4 | `sostrat-BATCH/src/sostrat-batch-GestionVUA.xml:77`; `sostrat/src/.../service/pif/impl/CN_SAPL_Impl.java`; ya citado (sin agregado propio) en `domain-catalog/domains/inspeccion-control/contexts/pif.md:75` |
| **Portic/CBOX + CarregaMtoPortic/CarregaMtoVaixellPortic** (sync de catálogos/maestros) | Outbound puro, batch cada 1 min, ficheros planos posicionales | Se queda en el gateway | `bc-integracion-edi-portic-v1` — sin tabla de negocio propia, solo vistas `V_CBOX_*` de solo lectura de 4+ dominios | `sostrat-BATCH/.../tasklet/CargaCBOXTasklet.java:75-151` |
| **Facturas** (INVOIC/APERAK) | Bidireccional, batch | Sin cambio | `bc-facturacion-v1` | `sostrat/src/.../service/facturas/impl/CN_EDI_Helper_Factura_Comun_Impl.java` |
| **Posicionamiento** (18 sub-flujos de respuesta) | Bidireccional, vía `MISSATGE_EDI` | **Fuera de alcance de este documento** | Ya registrado como hallazgo pendiente de investigación dedicada (`coverage-audit.md §8.2`, `PLAN_FASES_FUTURAS.md #102`) — el gateway seguiría siendo su transporte una vez se diseñe su bounded context | `sostrat-BATCH/.../tasklet/PosicionamientoEDITasklet.java:79-218` |

## 4. VUA (AEAT) vs. EMSWe (DMS) — resolución de la ambigüedad

Son **dos bounded contexts distintos, en dos dominios distintos**:

- **VUA/SAPL** → `bc-vua-sapl-v1`, `parent_domain: dom-inspeccion-control-v1`. Vive físicamente en `service/pif/impl/sapl` (dentro del paquete PIF; `FileXMLVUA.java` ya aparece citado en `domain-catalog/domains/inspeccion-control/contexts/pif.md:75`, sin agregado propio). Se separa de `bc-pif-v1` por el mismo criterio que ya separó `bc-pif-v1` de `bc-inspeccion-scpp-v1` (persistencia y modelo de estado propios, sin nada compartido), pero se mantiene en el mismo dominio porque su función real (alta/baja/notificación de entrada-salida de contenedores para aduana) condiciona si un contenedor requiere inspección física — coherencia de dominio de negocio, no de código.
- **DMS** → `bc-dms-emswe-v1`, `parent_domain: dom-operaciones-maritimas-v1`. Vive en `service/escalas/dms`, ligado al ciclo de vida de la escala. Se propone como bounded context independiente hoy (no como agregado dentro de un `bc-escalas-v1` que todavía no existe por el bloqueante ARGOS), con nota explícita de que su relación (¿fusión o `conformist` downstream de `bc-escalas-v1`?) debe revisarse una vez ese bounded context se cree.

**Acción pendiente** (registrada en `PLAN_FASES_FUTURAS.md #103`, no ejecutada en este documento): `domain-catalog/domains/integraciones-edi/domain.md` describe hoy VUA como si fuera la EMSWe europea — su `description`/`subdomains`/`ubiquitous_language` deben corregirse para reflejar que EMSWe = DMS, y VUA = AEAT (aduana nacional).

## 5. Diseño del patrón de eventos

**Convención existente reutilizada** (`events-catalog.md` §0): `type: com.apb.sostrat.<bc>.<Evento>.v1`, topic Service Bus `evt.sostrat.<bc>`, `source: /sostrat/<bc>`, envelope CloudEvents 1.0.

### Topología de topics

- `bc-integracion-edi-portic-v1` publica **todo** mensaje EDI entrante ya traducido a CloudEvent en un topic propio, `evt.sostrat.integracion-edi-portic`, con una propiedad de aplicación `circuito` (`COARRI`/`CODECO`/`COPINO`/`WASDIS`/`HAZMAT`/`IFTDGN`/`CUSCAR`/`PAXLST`/`BERMAN`/`INVOIC`) en la metadata del mensaje de Service Bus.
- Cada bounded context de negocio **no** se suscribe al topic entero: crea una suscripción con **filtro SQL** (`circuito IN ('CODECO','COPINO')`, etc.). Esto es la traducción literal de la tabla real `TipusMissatgeEdi` (que hoy vincula mensaje→circuito→sentido **como datos**, `dataaccess/dto/TipusMissatgeEdi.java:10-25`) a configuración de ruteo de plataforma — el mismo dato, un mecanismo distinto.
- Para las respuestas salientes (APERAK, NotifEntrada VUA...), el BC de negocio no llama a Portic directamente: publica un **comando** `cmd.sostrat.integracion-edi-portic.enviar` con el payload; el gateway lo traduce, persiste `MissatgeEdi` (`sentit`=sortida), invoca `sendMessageOracle`, y confirma con `MensajeEdiEnviado`/`MensajeEdiRechazado`.

### Correlación petición↔respuesta

Hoy se resuelve con `MissatgeEdi.nummisorigen` (referencia al mensaje original, permite encadenar respuesta↔original). Se traduce a dos extensiones CloudEvents (nombres en minúsculas/alfanumérico, según la spec):
- `edimessageid` = `nummissatge` propio del mensaje actual — trazabilidad directa contra `MissatgeEdi`/`LiniaDeMissatgeEdi`/`ErrorEdi` sin duplicar esas tablas en cada BC de negocio.
- `edicorrelationid` = `nummisorigen` del mensaje original — mismo valor estable que hoy usa Portic (lo ecoa), sin inventar un UUID interno nuevo.

El campo CloudEvents core `subject` sigue llevando la clave de negocio (escala, partida, contenedor...) como ya hace el catálogo actual.

### Eventos de dominio nuevos

**`bc-integracion-edi-portic-v1`** (topic `evt.sostrat.integracion-edi-portic`)
- `MensajeEdiEnviado` / `MensajeEdiRechazado` — confirmación de envío tras el comando `cmd.sostrat.integracion-edi-portic.enviar`.
- `ErrorEdiRegistrado` — `{nummissatge, idcircuit, codierror, descripcio}` — de la tabla `ErrorEdi`, para un dashboard de errores EDI transversal sin que cada BC de negocio replique lógica de error.

**`bc-vua-sapl-v1`** (topic `evt.sostrat.vua-sapl`)
- `SaplAltaRegistrada` — `{numsapl, matcontenidor, idterminal, dataalta, idestat}` — inbound Alta (XSD `CoordinacionAltaV1Sal`).
- `SaplBajaRegistrada` — `{numsapl, databaixa, motiubaixa}` — inbound Baja (XSD `CoordinacionAnulacionV1Sal`).
- `NotificacionSalidaVuaRecibida` — `{numsapl, datasortida, idestatsortida}` — inbound NotifSalida (XSD `NotificacionAltaV1Sal`).
- `NotificacionEntradaVuaEnviada` — `{numsapl, dataentrada, idestatentrada, edicorrelationid}` — outbound NotifEntrada (XSD `NotificacionAltaV1Ent`); mantiene la invariante de negocio ya confirmada en código — *"un SAPL solo se responde una vez"* (`SaplContenidor.nummissatgenotif` ya seteado → no reenviar).

**`bc-dms-emswe-v1`** (topic `evt.sostrat.dms-emswe`)
- `DeclaracionSanitariaMaritimaRecibida` — `{idsubport, anyescala, numescala, numdms, datadeclaracio, idestatsanitari}` — inbound MDH XML.
- `PosicionamientoSanitarioActualizado` — `{numdms, idposicionament, dataactualitzacio, idestat}` — fuente `SancrtPosIns`.

**Eventos a añadir a bounded contexts existentes** (diferido a `PLAN_FASES_FUTURAS.md #103`, no creados en `events-catalog.md` en este documento):
- `bc-aduanas-contenedores-v1`: `OperacionTerminalRegistrada`, `ConciliacionCoarriProcesada`.
- `bc-cruceros-v1`: `ListaPasajerosDeclarada`, `ListaPasajerosConfirmada`.
- `bc-transporte-terrestre-v1`: `PreavisoCodecoProcesado` (cierra el gap ya documentado `MensajeCodecoProcesado`, `events-catalog.md:608`/`818`, `specs/asyncapi-fase2.yaml:90`), `PreavisoCopinoRespondido`.
- `bc-manifiestos-v1`: `PartidaManifestadaViaEdi`.
- Futuro `bc-escalas-v1`: `MercanciaAsociadaAEscalaRegistrada` (BERMAN).

## 6. Qué queda pendiente

Este documento y las 3 propuestas de bounded context que lo acompañan (`bc-integracion-edi-portic-v1.md`, `bc-vua-sapl-v1.md`, `bc-dms-emswe-v1.md`) son la decisión de arquitectura y el diseño de eventos. **No se han creado todavía** (registrado como `PLAN_FASES_FUTURAS.md #103`):
- Los eventos nuevos en `events-catalog.md` para los 5 bounded contexts de negocio existentes (§5).
- Las actualizaciones a los proposals existentes (`bc-aduanas-contenedores-v1.md`, `bc-cruceros-v1.md`, `bc-transporte-terrestre-v1.md`, `bc-manifiestos-v1.md`).
- Un `specs/asyncapi-integraciones-edi.yaml` nuevo + actualización de `asyncapi-fase2.yaml` (cerrar el placeholder `MensajeCodecoProcesado`).
- La corrección de `catalog-comparison.md:44` (cerrar la divergencia con referencia a este documento) y de `coverage-audit.md` (fila `coarri`).
- La preparación local (sin push) de los 3 bounded contexts nuevos en el submodule `domain-catalog`, y la corrección de `domain-catalog/domains/integraciones-edi/domain.md` (VUA≠EMSWe, poblar `bounded_contexts`).

## 7. Historial de cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-15 | APB AI Framework | Análisis inicial, a petición explícita del usuario. Investigación de código por agente Explore (circuitos EDI, gateway genérico, VUA/SAPL, DMS) + diseño de arquitectura por agente Plan, revisados y verificados (citas fichero:línea confirmadas) antes de esta versión. |
