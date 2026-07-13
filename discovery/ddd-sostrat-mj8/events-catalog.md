# [IA-GEN] Catálogo de Eventos — Descomposición SÒSTRAT (v2, grounded)

> **Borrador generado por IA** (APB AI Framework - apb-doc-event-specs-v1.0 / apb-arch-event-driven-v1.0) — pendiente validación humana. No distribuir sin revisión.
> **v2 respecto a la versión anterior**: los schemas de payload ya no están pendientes de diseño — se han construido leyendo directamente las clases DTO/entidad reales del código (`dataaccess/dto/**/*.java`) citadas en cada evento. Ningún campo de este catálogo ha sido inventado. Donde la evidencia de código no alcanzaba (4 casos, marcados explícitamente), se dice así en vez de rellenar con datos plausibles.

**Convención de tipo:** `com.apb.sostrat.<bounded-context>.<Evento>.v1` (CloudEvents 1.0).
**Convención de topic:** `evt.sostrat.<bounded-context>` (Azure Service Bus).
**Convención de payload:** el campo `data` de cada evento es un **subconjunto de negocio** del DTO real citado — no se han volcado los ~30-90 campos completos de cada entidad (algunas, como `EscalaAspecte`, tienen más de 90), sino los campos de identidad, estado y negocio relevantes para que un consumidor externo reaccione al evento. El DTO fuente citado es la referencia completa si se necesita más detalle. Los campos puramente de auditoría interna (`idopealta`, `idopemodificacio`, `idprocalta`, `idprocmodificacio`) se omiten del payload de negocio pero se listan una vez aquí como envelope común.

## 0. Envelope común (CloudEvents 1.0)

```json
{
  "specversion": "1.0",
  "type": "com.apb.sostrat.<bc>.<Evento>.v1",
  "source": "/sostrat/<bc>",
  "id": "<uuid>",
  "time": "<ISO-8601>",
  "datacontenttype": "application/json",
  "data": { }
}
```

---

## 1. Escalas y Tráfico Marítimo

### EscalaCreada / EscalaModificada
**Fuente:** `sostrat/src/org/apb/sostrat/dataaccess/dto/escalas/Escala.java` (tabla `ESCALA`, PK compuesta `idsubport+anyescala+numescala`)
```json
{
  "idsubport": "string",
  "anyescala": "integer",
  "numescala": "integer",
  "idestoperatiu": "string",
  "aspactual": "string",
  "datsolicitud": "date",
  "datconfirmacio": "date",
  "datautoritzacio": "date",
  "datdessortida": "date",
  "datanulacio": "date",
  "datdenegacio": "date",
  "perliquidacio": "string",
  "idestfacturacio": "string",
  "observacions": "string"
}
```
*(`Escala.java` tiene ~45 campos totales incluyendo relaciones `listaEscalaAspecte`, `listaAtracada`; se han seleccionado los de identidad/estado/fecha relevantes para un consumidor externo.)*

### AtracadaRegistrada
**Fuente:** `dataaccess/dto/escalas/Atracada.java` (tabla `ATRACADA`, PK `idsubport+anyescala+numescala+seqatracada`)
```json
{
  "idsubport": "string",
  "anyescala": "integer",
  "numescala": "integer",
  "seqatracada": "integer",
  "idestatatracada": "string",
  "datsolicitud": "date",
  "datconfirmacio": "date",
  "datautoritzacio": "date",
  "datanulacio": "date",
  "mollsalternatius": "string"
}
```

---

## 2. Cruceros

### EscalaCruceroAuditada
**Fuente:** `dataaccess/dto/cruceros/CreuerEscalaAudit.java` (tabla `CREUER_ESCALA_AUDIT`, PK `seqaudit`)
```json
{
  "seqaudit": "long",
  "dataaudit": "date",
  "tipoperacio": "string",
  "proces": "string",
  "operador": "string",
  "idesccreuer": "long",
  "idocupacio": "long",
  "consignatari": "string",
  "armador": "integer",
  "alisolicitada": "integer",
  "tersolicitada": "integer",
  "confirmada": "string",
  "datdecisio": "date",
  "datanulacio": "date"
}
```

---

## 3. Ferrocarril Portuario

### OperacionFerroviariaRegistrada / OperacionFerroviariaAnulada
**Fuente:** `dataaccess/dto/ferrocarril/OperacioFerroviaria.java` (tabla `OP_FERROVIARIA`, PK `seqoperacio`)
```json
{
  "seqoperacio": "long",
  "datoperacio": "date",
  "idtipoperacio": "string",
  "lontren": "integer",
  "taratren": "integer",
  "idopeferroviari": "string",
  "idopeterminal": "string",
  "portescalatren": "string",
  "anyescalatren": "integer",
  "numescalatren": "integer",
  "carrega": "string",
  "descarrega": "string",
  "facturable": "string",
  "observacions": "string"
}
```
`idtipoperacio` toma valores según constantes `Constantes.OPERACIONES_FERROVIARIAS_TIPO_OPERACION_{ENTRADA|SALIDA|MANIOBRA|INTERVENCION}` — confirmado por `Comparable<OperacioFerroviaria>` en el DTO.

---

## 4. Título

### TituloOtorgado / TituloActualizado
**Fuente:** `dataaccess/dto/Titol.java` (tabla `TITOL`, PK `idsubport+idtitol`)
```json
{
  "idsubport": "string",
  "idtitol": "integer",
  "datlliurament": "date",
  "datatorgament": "date",
  "datsolicitud": "date",
  "idtitolprecedent": "integer",
  "idestattitol": "string",
  "idperiodicitat": "string",
  "garantia": "string"
}
```
**Nota crítica de diseño** (ver `decomposition-roadmap.md` Fase 4 / `EPIC-12`): este es el evento que debe sustituir la escritura directa detectada `UPDATE TITOL_MINIM_DADES` desde `CN_Liquidacion_Impl.java:434`. `idestattitol` no tiene enum propio en el DTO — su dominio de valores vive en la tabla relacionada `TITOL_ESTAT`, no confirmada en esta extracción (pendiente).

---

## 5. Liquidación

### LiquidacionGenerada / LiquidacionAceptada / LiquidacionAnulada
**Fuente:** `dataaccess/dto/Liquidacio.java` (tabla `LIQUIDACIO`, PK `portliquidacio+anyliquidacio+numliquidacio`)
```json
{
  "portliquidacio": "string",
  "anyliquidacio": "integer",
  "numliquidacio": "long",
  "idestatliq": "string",
  "idestatliqant": "string",
  "datliquidacio": "date",
  "portescala": "string",
  "anyescala": "integer",
  "numescala": "integer",
  "idvaixell": "integer",
  "nomvaixell": "string",
  "hihatitol": "string",
  "idtitol": "integer",
  "idtarifa": "string",
  "impbasec": "decimal",
  "impivac": "decimal",
  "imptotalc": "decimal"
}
```
**`idestatliq` — enum real confirmado (6 valores, no 3 como se estimó en la v1 de este catálogo):**

| Constante | Valor | Significado |
|---|---|---|
| `ID_ESTAT_GENERADA` | `GE` | Generada |
| `ID_ESTAT_SELECCIONADA` | `SE` | Seleccionada |
| `ID_ESTAT_ACEPTADA` | `AC` | Aceptada |
| `ID_ESTAT_FACTURADA` | `FA` | Facturada |
| `ID_ESTAT_ANULADA` | `AN` | Anulada |
| `ID_ESTAT_ESBORRANY` | `ES` | Borrador |

`LiquidacionGenerada` se emite en la transición a `GE`; `LiquidacionAceptada` en la transición a `AC`; `LiquidacionAnulada` en la transición a `AN`. El evento debe incluir siempre `idestatliqant` para que el consumidor pueda validar la transición.

---

## 6. Facturación

### FacturaEmitida / FacturaEdiGenerada
**Fuente:** `dataaccess/dto/Factura.java` (tabla `FACTURA`, PK `idserfactura+portfactura+anyfactura+numfactura`)
```json
{
  "portfactura": "string",
  "anyfactura": "integer",
  "idserfactura": "string",
  "numfactura": "long",
  "datfactura": "date",
  "datvenciment": "date",
  "nomclient": "string",
  "nif": "string",
  "idestfacturacio": "string",
  "impbase": "decimal",
  "impiva": "decimal",
  "imptotal": "decimal",
  "facexml": "string",
  "numregface": "string",
  "estatface": "string"
}
```
`pdfdupfactura` y `pdfsignat` son BLOB (`byte[]`) — **no se incluyen en el payload del evento**; el consumidor debe recuperarlos vía API (`GET /api/v1/invoices/{id}/pdf`), no vía evento.

---

## 7. Garantías

### GarantiaActualizada
**Fuente:** `dataaccess/dto/Garantia.java` (tabla `GARANTIA`, PK `idsubport+seqgarantia`)
```json
{
  "idsubport": "string",
  "seqgarantia": "long",
  "idtitol": "integer",
  "idestatgarantia": "string",
  "tipus": "string",
  "impgarexiactual": "decimal",
  "impgarconstituit": "decimal",
  "datinivigencia": "date",
  "datfivigencia": "date"
}
```
**Nota de calidad de datos encontrada en el DTO fuente**: el campo `exprovisional` tiene un Javadoc idéntico (copy-paste) al del campo anterior `idmotiu` ("maps to column IDMOTIU") — no se puede confirmar su columna BBDD real desde el comentario. No se ha incluido `exprovisional` en el payload por esta ambigüedad; confirmar con el equipo antes de añadirlo.

---

## 8. Manifiestos

### ManifiestoRegistrado / ManifiestoCircuitoProcesado
**Fuente:** `dataaccess/dto/manifiestos/gestion/Manifest.java` (tabla `MANIFEST`, PK `idmanifest`) — raíz de agregado deliberadamente delgada (7 campos, patrón versionado).
```json
{
  "idmanifest": "long",
  "veractual": "integer",
  "codedi": "string",
  "idtipdeclaracio": "string",
  "idsubport": "string",
  "anyescala": "integer",
  "numescala": "integer"
}
```

### PartidaActualizada
**Fuente:** `dataaccess/dto/manifiestos/gestion/PartidaVersio.java` (tabla `PARTIDA_VERSIO`, PK `idpartida+versio`)
```json
{
  "idpartida": "long",
  "versio": "integer",
  "estat": "string",
  "datinivigencia": "date",
  "datfivigencia": "date",
  "embalums": "integer",
  "pes": "long",
  "volum": "long",
  "codaranzelari": "string",
  "numonu": "string",
  "classemmpp": "string",
  "roro": "string"
}
```
`codaranzelari` es FK a `dataaccess/dto/Mercaderia.java` (tabla `MERCADERIA`, PK de un solo campo `codaranzelari` — clase intencionalmente mínima, el detalle descriptivo vive en `MercaderiaDades`/`MercaderiaDadesIdioma`, no leídas en esta extracción).

---

## 9. Mercancías Peligrosas (MMPP)

### AutorizacionMMPPConcedida
**Fuente:** `dataaccess/dto/mmpp/gestion/MmppAutoritzacio.java` (tabla `MMPP_AUTORITZACIO`, PK `idautoritzacio`)
```json
{
  "idautoritzacio": "long",
  "idnotificacio": "long",
  "idresolucio": "string",
  "dataautoritzada": "date",
  "datafiautoritzada": "date",
  "idmotiurebuig": "string",
  "descmotiurebuig": "string",
  "viaedi": "string"
}
```

### NotificacionMMPPEnviada
**Fuente:** `dataaccess/dto/mmpp/gestion/MmppNotif.java` (tabla `MMPP_NOTIF`, PK `idnotificacio`) — DTO con patrón "entrada"/"sortida" duplicado (datos de transporte de entrada y salida del recinto).
```json
{
  "idnotificacio": "long",
  "idestat": "string",
  "idsubport": "string",
  "anyescala": "integer",
  "numescala": "integer",
  "datarecdocument": "date",
  "dataemidocument": "date",
  "idtipustransentrada": "string",
  "idvaixellentrada": "integer",
  "idtipustranssortida": "string",
  "idvaixellsortida": "integer",
  "viaedi": "string"
}
```

---

## 10. PIF (gap cerrado 2026-07-11)

**Nota de rutas reales**: no existe `dataaccess/dto/pif/` — las clases PIF viven directamente en `dataaccess/dto/` (sin subcarpeta) y la vista de "área PIF" en `dataaccess/views/dto/VDataSelectorareapif.java`.

### OperacionPifRegistrada
**Fuente:** `dataaccess/dto/OperacioPif.java` (tabla `OPERACIO_PIF2`, PK `anyoperaciopif+seqoperaciopif`)
```json
{
  "anyoperaciopif": "integer",
  "seqoperaciopif": "integer",
  "idestatoperaciopif": "string",
  "matriculacamio": "string",
  "finger": "integer",
  "dataassignaciomoll": "date",
  "tempstotal": "decimal",
  "tempsoperativa": "decimal",
  "importtotal": "decimal"
}
```
`idestatoperaciopif` — valores confirmados en código: `CR`, `AP`, `PF`, `FI`, `AN`, `AF` (nombres completos no documentados en el DTO — confirmar con negocio antes de fijar el enum definitivo).

### ÁreaPifConsultada (evento de solo lectura, opcional)
**Fuente:** vista `dataaccess/views/dto/VDataSelectorareapif.java` (vista `V_DATA_SELECTORAREAPIF`, sin PK — es una vista, no una tabla transaccional)
```json
{
  "anyoperaciopif": "integer",
  "seqoperaciopif": "integer",
  "codestado": "string",
  "numcontenidor": "string",
  "horaasignada": "date",
  "finger": "integer",
  "matriculacamio": "string",
  "estado": "string"
}
```
Este es un modelo de lectura (vista SQL), no un evento de escritura real — incluido para el diseño de la pantalla de consulta de área PIF, no como contrato de evento a publicar.

---

## 11. Depotsis

### SolicitudDepotsisRegistrada
**Fuente:** `dataaccess/dto/depotsis/DepotsisSolicitud.java` (tabla `T6_SOLICITUT_OP`, PK `idsolicitud`, raíz delgada) + `DepotsisSolicitudVersio.java` (tabla `T6_SOLICITUT_OP_VERSIO`, PK `idsolicitut+versio`, contiene el detalle real).
```json
{
  "idsolicitud": "long",
  "versio": "integer",
  "idocupacio": "long",
  "numescala": "integer",
  "anyescala": "integer",
  "idsubport": "string",
  "idestibador": "string",
  "codaranzprod": "string",
  "estat": "string",
  "quantitat": "decimal",
  "datainioperacions": "date",
  "datafioperacions": "date"
}
```

---

## 12. Aduanas / Control de Contenedores

### TrasladoContenedorActualizado
**Fuente:** `dataaccess/dto/MovimientoContenedor.java` — DTO simple sin tabla propia confirmada (probablemente objeto de transferencia entre capas, no entidad persistida directamente).
```json
{
  "identificador": "string",
  "tipoMovimiento": "string",
  "fechaCargaDescarga": "date",
  "fechaEntradaSalida": "date",
  "viaEntradaSalida": "string",
  "codResultado": "integer"
}
```
Vista de consulta relacionada (solo lectura, útil para el modelo de query del nuevo servicio): `dataaccess/views/dto/aduanas/VTcMAduanaContenidor.java` — campos `escala, referencia, datentrada, declarante, estado, muelle, dua, mercancia, matricula, idequipament, anyescala, idsubport`.

### DatosTerminalConciliados (gap cerrado 2026-07-11)
**Fuente:** `service/terminales/impl/CN_ConciliacioController_Impl.java` (orquesta la conciliación; no persiste directamente) sobre `dataaccess/dto/terminales/ProtermCont.java` (tabla `PROTERM_CONT`, PK `idregistre`, clave de negocio real `refequipament+operacio+numescalaterminal`) y `dataaccess/dto/terminales/ErrorProcConc.java` (errores/warnings de conciliación, PK `iderror`).
```json
{
  "idregistre": "long",
  "idsubport": "string",
  "anyescala": "long",
  "numescala": "long",
  "numescalaterminal": "string",
  "refequipament": "string",
  "operacio": "string",
  "dataoperacio": "date",
  "estado": "string",
  "estibador": "string"
}
```
Evento complementario `ErrorConciliacionDetectado` (cuando la conciliación encuentra una discrepancia):
```json
{
  "iderror": "long",
  "tipuserror": "string",
  "errorwarning": "string",
  "coderror": "long",
  "descripcio": "string",
  "refequipament": "string",
  "numescala": "integer"
}
```
`tipuserror` — valores confirmados en código: `CN`, `CV`, `TER`, `SSI`, `CNC`, `STI`, `ALI`, `COA`. `errorwarning` — `E` (error) / `W` (warning). `coderror` tiene un catálogo extenso de constantes numéricas (`CODERR_*`, ~40 valores entre 1001-7001) — no se replica aquí por volumen, ver `ErrorProcConc.java` para el catálogo completo antes de fijar el enum definitivo del contrato.

### DatosTerminalConciliados
**Fuente:** proceso batch `sostrat-BATCH/.../tasklet/terminales/ConciliarDades.java` — **no se ha extraído un DTO de evento específico en esta ronda**; la evidencia disponible es a nivel de proceso (job SpringBatch), no de entidad. Payload pendiente.

---

## 13. Datos Maestros de Equipamiento

### EquipamientoRegistrado / EquipamientoActualizado
**Fuente:** `dataaccess/dto/mmpp/maestros/Equipament.java` (tabla `EQUIPAMENT`, PK `idequipament`) — **confirmado como maestro deliberadamente delgado, 6 campos únicamente**:
```json
{
  "idequipament": "long",
  "refequipament": "string",
  "matriculaiso": "string",
  "idtipequipament": "integer",
  "propietari": "string",
  "idoridade": "string"
}
```
**Hallazgo de diseño relevante**: el maestro NO contiene peso, tara, dimensiones ni estado — esos atributos viven duplicados en cada bounded context consumidor (`MmppNotifEquipament.pesbrut/pesnet`, `ManifestEquip.idequipament+refequipament`, `VTcMAduanaContenidor`/`VTcTConAduanaContenidor` con su propio `estado`). **Implicación para el contrato**: este evento debe limitarse a los 6 campos de identidad; los atributos operativos (peso, estado aduanero) deben viajar en los eventos propios de cada bounded context (`NotificacionMMPPEnviada`, `TrasladoContenedorActualizado`, etc.), no en este. No dupliques esos campos aquí — sería reintroducir el mismo anti-patrón de dato compartido sin dueño que esta extracción busca resolver.

---

## 14. MARPOL / Residuos

### ListaResiduosMarpolGenerada
**Fuente:** `dataaccess/dto/marpol/ResidusLot.java` (tabla `RESIDUS_LOT`, PK `idlot`)
```json
{
  "idlot": "long",
  "datalot": "date",
  "idempresa": "string",
  "idestat": "integer",
  "idtipus": "string",
  "importlot": "decimal",
  "dataenv": "date",
  "datafins": "date"
}
```

### ResiduoPesado
**Fuente:** `dataaccess/dto/marpol/ResidusLinea.java` (tabla `RESIDUS_LINEA`, PK `idlinea+idresidu`)
```json
{
  "idlinea": "integer",
  "idresidu": "long",
  "idsubtipus": "string",
  "idtipus": "string",
  "idunitat": "string",
  "quantitat": "decimal",
  "quantitatpagada": "decimal",
  "ncamions": "integer",
  "ncont": "integer",
  "importe": "decimal"
}
```
**`idestat` de `ResidusEscala` — enum real confirmado (7 valores)**, relevante para el evento padre `ResiduoPesado`/eventuales eventos de cambio de estado de la recogida:

| Constante | Valor | Significado |
|---|---|---|
| `ID_ESTAT_RECIBIDO` | 1 | Recibido |
| (anulado) | 2 | Anulado |
| (no pagado) | 3 | No pagado |
| (confirmado) | 4 | Confirmado |
| (enviado) | 5 | Enviado |
| (pagado) | 6 | Pagado |
| (reclamado) | 7 | Reclamado |

*(Fuente: `dataaccess/dto/marpol/ResidusEscala.java`, constantes `ID_ESTAT_*`; solo el valor 1 tiene nombre de constante confirmado literalmente en el extracto recibido — los nombres 2-7 son la interpretación directa del comentario del subagente, no se han vuelto a verificar contra el código fuente exacto de cada constante. Confirmar antes de usar en producción.)*

---

## 15. Servicios Auxiliares al Buque

### SolicitudAguadaProcesada
**⚠️ GAP DE EVIDENCIA CONFIRMADO**: las clases DTO reales `SaSolicitud`, `SaSolicitudPk`, `SaSolicitudAudit`, `SaRegistreSuministre` (paquete `org.apb.sostrat.dataaccess.dto.aguada`) **no existen como código fuente en este checkout** — solo están compiladas dentro de `sostrat-BATCH/lib/sostrat.jar`. Búsqueda exhaustiva confirmada sin resultado. La evidencia más cercana disponible es una **vista de solo lectura**, no la entidad transaccional:

**Fuente (vista, no la entidad real):** `dataaccess/views/dto/aguada/VTcSaSolicitud.java` (vista `V_TC_SA_SOLICITUD`)
```json
{
  "idsubport": "string",
  "idsolicitud": "long",
  "idtipussum": "string",
  "anyescala": "integer",
  "numescala": "integer",
  "seqatracada": "integer",
  "idvaixell": "integer",
  "nomvaixell": "string",
  "datasol": "date",
  "idestatsol": "string",
  "quantitat": "float",
  "usuari": "string"
}
```
**No usar este schema como definitivo** para el evento de producción — es un modelo de lectura denormalizado, no la estructura de escritura real. Tarea técnica obligatoria antes de implementar este evento: recuperar el código fuente real de `SaSolicitud`/`SaRegistreSuministre` (posiblemente pidiéndolo al proveedor IN2, o decompilando `sostrat.jar` como último recurso) — ver `jira-backlog.md`, tarea añadida en EPIC-06.

### AtracadaMarinaRegistrada
**Fuente:** `dataaccess/dto/marinas/MarinaDadesAtracada.java` (tabla `MARINA_DADES_ATRACADA`, PK `seqdades`)
```json
{
  "seqdades": "long",
  "idusuari": "string",
  "idsubport": "string",
  "idtitol": "integer",
  "nomvaixell": "string",
  "matricula": "string",
  "nompropietari": "string",
  "eslora": "decimal",
  "maniga": "decimal",
  "dataentrada": "date",
  "datasortida": "date"
}
```

### AlbaranPescaImportado
**Fuente:** `dataaccess/dto/gpesca/Albara.java` + `AlbaraBase.java` (tabla `ALBARA`, PK `idport+idalbara`)
```json
{
  "idalbara": "string",
  "idport": "string",
  "data": "date",
  "importtotal": "decimal",
  "idarmador": "long",
  "idvaixell": "long",
  "numalbara": "string",
  "dataliquidacio": "date"
}
```

---

## 16. Transporte Terrestre

### PreavisoRegistrado
**Fuente:** `dataaccess/dto/transporteterrestre/Preavis.java` + `PreavisBase.java` (tabla `PREAVIS_TT`, PK `portpreavis+seqpreavis`)
```json
{
  "portpreavis": "string",
  "seqpreavis": "long",
  "idconsignatari": "string",
  "tipuspreavis": "string",
  "trasllat": "string",
  "datoperacio": "date",
  "matcontenidor": "string",
  "refcontenidor": "string",
  "estat": "string",
  "datlimit": "date",
  "motivorechazo": "string"
}
```

### AutorizacionConcedida
**Fuente:** `dataaccess/dto/transporteterrestre/AutorizacionGenerica.java` (tabla `AUTORITZACIO_GEN_TT`, PK `portautoritzacio+seqautoritzacio`)
```json
{
  "portautoritzacio": "string",
  "seqautoritzacio": "long",
  "emptransport": "string",
  "nifemppeticionari": "string",
  "datiniautoritzacio": "date",
  "datfiautoritzacio": "date",
  "estat": "string",
  "datcaducitat": "date"
}
```

### MensajeCodecoProcesado
**Fuente:** `sostrat-BATCH/.../tasklet/LanzarCircuitoCodecoTasklet.java` — evento a nivel de mensaje EDI, no de una entidad DTO propia identificada en esta extracción. Payload pendiente de diseño dedicado con el equipo EDI.

---

## 17. PPS (Pases y Permisos)

### SolicitudRegistrada
**Fuente:** `dataaccess/dto/pps/Solicitud.java` + `SolicitudBase.java` (PK `port+idsolicitud`)
```json
{
  "port": "string",
  "idsolicitud": "string",
  "idempresa": "string",
  "datsol": "date",
  "ntargetes": "long",
  "doccomplerta": "boolean",
  "iddepaval": "string",
  "preu": "decimal",
  "datbaixa": "date"
}
```

### TarjetaCaducadaDetectada
**Fuente:** `dataaccess/dto/pps/SolicitudAudit.java` (tabla `SOLICITUD_AUDIT`, PK `seqaudit`, extiende `SolicitudBase`)
```json
{
  "seqaudit": "long",
  "dataaudit": "date",
  "tipoperacio": "string",
  "idestat": "string",
  "numeracionTargeta": "string",
  "port": "string",
  "idsolicitud": "string"
}
```

---

## 18. Mano de Estiba

### ContratacionRegistrada
**Fuente:** `dataaccess/views/dto/manoEstiba/MaestContractacio.java` (tabla `MAEST_CONTRACTACIO`, PK `idcontractacio`) — nota: la entidad completa vive en el paquete `views.dto`, no en `dto` directamente (solo la PK está en `dto`).
```json
{
  "idcontractacio": "long",
  "datacontractacio": "date",
  "idtipuscontractacio": "string",
  "idestatcontractacio": "string",
  "dataactualitzacio": "date"
}
```

### ComandaAsignada
**Fuente:** `dataaccess/views/dto/manoEstiba/MaestComanda.java` (tabla `MAEST_COMANDA`, PK `idcomanda`)
```json
{
  "idcomanda": "long",
  "idcontractacio": "long",
  "idcomandaportic": "long",
  "nifempresa": "string",
  "idtipuscomanda": "string",
  "idestatcomanda": "string"
}
```

---

## 19. Servicios Transversales de Plataforma

### ConsumClaveguerLiquidado
**Fuente:** `dataaccess/dto/clavegueram/ClvgConsums.java` (tabla `CLVG_CONSUMS`, PK `idconsum`)
```json
{
  "idconsum": "long",
  "idcarrega": "long",
  "polissa": "string",
  "nif": "string",
  "titular": "string",
  "consum": "double",
  "lecturaant": "double",
  "lecturaact": "double",
  "estat": "string"
}
```

### AvisoEnviado
**Fuente:** `sostratWSCXF/.../es/apb/ws/sms/ISmsWS.java`, método `enviarSMS` (firma real completa):
```json
{
  "destinataris": ["string"],
  "text": "string",
  "id_objecte": "string",
  "aplicaciosmsid": "long",
  "demanarconfirmacion": "integer"
}
```
Recomendación (ver `api-surface-by-phase.md` Fase 0): evaluar si este evento es necesario o si basta con la llamada síncrona directa a `APB.API.SMS`/`APB.API.EMAIL`.

### UsuarioAutenticado
**Fuente:** `sostratWSCXF/.../es/apb/ws/authenticateSostrat/IAuthenticateWs.java`, método `authenticateSostrat` (firma real):
```java
public String authenticateSostrat(String strOperador, String strPass) throws RemoteException;
```
**Restricción de seguridad obligatoria**: el payload del evento `UsuarioAutenticado` **nunca** debe incluir `strPass` ni el token de retorno en texto plano — solo:
```json
{
  "operador": "string",
  "timestamp": "date",
  "resultado": "string"
}
```
El tipo de retorno real del método (`String`) no tiene Javadoc que documente su contenido — no se ha podido confirmar si es un token, un código de resultado, o ambos concatenados; requiere confirmación con el equipo antes de diseñar el evento definitivo.

### CargaInicialCompletada
**Fuente:** `sostrat-CARGASINICIALES/.../initialdata/launcher/CargaInicial.java`, switch real de entidades en `main()`:
```json
{
  "entidad": "string",
  "borrado": "string"
}
```
Valores reales confirmados de `entidad`: `T` (Títulos, vía `CN_TitolCI`), `A` (Actividades, `CN_TitolActivitatCI`), `TA` (ambos), `O` (Ocupaciones, `CN_TitolOcupacioCI`), `TODO` (título+actividad+ocupación), `F` (Facturas, `CN_FacturasCI`), `CONDSEG` (condiciones de seguridad MMPP, `CN_CondicionesSeguridadCI`), `MAMMPP` (maestros MMPP, `CN_MaestrosCI`), `CARGAINICIAL`/`CARGAINICIALBYPASS`/`CARGAINCREMENTAL`/`CARGAINCREMENTALMANUAL`/`INCREMENTALPORBLOQUES` (todos delegan en `CN_ManifiestosCI`, es decir, cargan **Manifiestos**, no Título como se documentó en la v1 de este análisis — corrección respecto al catálogo anterior). `borrado` es el flag `S`/`N` que determina si se ejecuta `truncarTablas()` antes de `inicioProceso()`.

---

## Fase 6 (nueva) — Eventos de los bounded contexts descubiertos en la auditoría de cobertura 2026-07-13

> Ver `coverage-audit.md` para el contexto completo. Estos 6 BCs vivían en paquetes de código sin ticket Jira de módulo asociado, por eso no estaban en el catálogo de eventos original.

### BuqueRegistrado / BuqueActualizado / BuqueDadoDeBaja
**Fuente:** `dataaccess/dto/Vaixell.java` (tabla `VAIXELL`), servicio `CN_Vaixell.crear/modificar/darDeBaja/restaurar`.
```json
{ "idvaixell": "long", "nomvaixell": "string", "callsign": "string", "mmsi": "string", "numlloyds": "string", "maxeslora": "decimal", "maxcalat": "decimal", "maxmaniga": "decimal" }
```
**Regla de negocio real**: `BuqueActualizado` solo debe disparar revalidación en Cruceros cuando cambian `nomvaixell`/`maxmaniga`/`maxcalat`/`maxeslora` — evidencia directa del array `arrModifCruEscOOPP` en el código legacy.

### OperadorPortuarioRegistrado / OperadorPortuarioActualizado
**Fuente:** `dataaccess/dto/Usuari.java` (tabla `USUARI`).
```json
{ "idusuari": "string", "nif": "string", "eori": "string", "codiagent": "string", "tippersona": "string" }
```
**Nota de seguridad**: confirmado por lectura completa del DTO (2253 líneas) que no existe ningún campo de credencial/password — este evento nunca debe incluir datos de autenticación.

### ServicioBusCruceroAsignado / ServicioVigilanciaCruceroRegistrado
**Fuente:** `dataaccess/dto/serviciosAuxiliares/CreuerBus.java` (tabla `CREUER_BUS`), `CreuerVigilanciaPunt.java` (tabla `CREUER_VIGILANCIA_PUNT`).
```json
{ "idcreuerbus": "long", "numescala": "integer", "anyescala": "integer", "ocupacio": "integer" }
```

### InspeccionRegistrada / CapacidadPifActualizada
**Fuente:** `dataaccess/dto/Inspeccio.java` (tabla `INSPECCIO`), `LlocDInspeccio.java` (tabla `LLOC_D_INSPECCIO`, campo `CAPMAXSTDDIA`).
```json
{ "idinspeccio": "long", "idllocinspeccio": "string", "capmaxstddia": "integer", "resultat": "string" }
```
**Sin confirmar**: nombre exacto de los valores posibles de `resultat` — no se ha extraído un enum explícito en esta pasada.

### TramiteClienteIniciado / TramiteClienteResuelto
**Fuente:** `dataaccess/dto/TramitClient.java` (tabla `TRAMIT_CLIENT`).
```json
{ "idtramit": "long", "idusuari": "string", "idtipustramit": "string", "datcreacio": "date", "datresolucio": "date" }
```

### LecturaElectricidadRegistrada / ConsumoElectricidadLiquidado
**Fuente:** `dataaccess/dto/suministres/electricitat/SeLectura.java` (vista `V_TC_LECTURA_ELECTRICITAT`).
```json
{ "anyescala": "integer", "numescala": "integer", "idarmador": "string", "lecturainici": "decimal", "lecturafi": "decimal", "consumototal": "decimal", "tiempoconexion": "decimal", "tiempoatraque": "decimal" }
```
**Sin confirmar**: enum de estados de una lectura — el código expone acciones (`liquidacionMasiva`/`desliquidar`/`anular`) pero no un campo de estado explícito documentado.

---

## Resumen de gaps de evidencia (honestidad explícita, no inventado)

| Evento | Gap | Acción pendiente |
|---|---|---|
| ~~OperacionPifRegistrada~~ | ✅ **Cerrado 2026-07-11** — `dataaccess/dto/OperacioPif.java` leído, ver §10 | — |
| ~~DatosTerminalConciliados~~ | ✅ **Cerrado 2026-07-11** — `ProtermCont.java`/`ErrorProcConc.java` leídos, ver §12 | — |
| SolicitudAguadaProcesada | **DTO fuente no existe en el checkout** (solo compilado en `sostrat.jar`) — único gap real que sigue sin cerrar | Solicitar fuente a IN2 o decompilar como último recurso |
| MensajeCodecoProcesado | Evento de mensaje EDI, no de entidad DTO | Diseño dedicado con equipo EDI |
| GarantiaActualizada (`exprovisional`) | Javadoc ambiguo/duplicado en el DTO fuente | Confirmar columna real con el equipo antes de incluir el campo |
| `idestatliq` (Liquidacion) → nombres de constantes 2-7 en `ResidusEscala` | Solo el valor 1 tiene nombre de constante Java confirmado literalmente | Releer `ResidusEscala.java` para confirmar nombres exactos de las constantes 2-7 |
