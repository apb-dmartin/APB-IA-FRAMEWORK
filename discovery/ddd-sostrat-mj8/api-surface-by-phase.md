# [IA-GEN] Superficie de APIs por Fase — Descomposición SÒSTRAT (v2, grounded)

> **Borrador generado por IA** (APB AI Framework - apb-arch-api-contract-v1.0) — pendiente validación humana. No distribuir sin revisión.
> **v2 respecto a la versión anterior**: los cuerpos de request/response ya no están vacíos — se han construido con los campos reales de las DTOs citadas en `events-catalog.md` (misma fuente de evidencia, mismo principio: nada inventado, gaps marcados explícitamente).
> **v3 → v4 (2026-07-11)**: la v3 desplegaba Título/Liquidación/Facturación/Garantías como un único servicio. Revertido tras reparentar contra el catálogo real de dominios de APB: `/api/v1/port-occupation-titles` + `/api/v1/port-occupation-titles/{id}/guarantees` viven en el servicio **Concesiones** (`dom-concesiones-v1`); `/api/v1/settlements` + `/api/v1/invoices` viven en el servicio **Facturación y Liquidaciones** (`dom-facturacion-v1`) — son dos servicios y dos bases de datos Azure SQL distintas, comunicados por el evento `TituloActualizado` (ver `events-catalog.md` §4).

**Convenciones aplicadas** (`apb-arch-api-contract-v1.0`): recursos en `kebab-case` plural, sin verbos en la URL, versionado en path (`/api/v1/`), errores RFC 7807, fechas ISO 8601, paginación cursor-based, header `X-Request-Id`, autenticación EntraID/OAuth 2.0. Todas las APIs se publican vía Azure API Management (APIM).
**Tipos:** se usa la misma notación que en `events-catalog.md` (`string`, `integer`, `long`, `decimal`, `date`, `boolean`) directamente derivada del tipo Java del campo en el DTO fuente.

---

## Fase 0 — Fundamentos

### `/api/v1/container-equipment` — Datos Maestros de Equipamiento
**Fuente:** `dataaccess/dto/mmpp/maestros/Equipament.java` (tabla `EQUIPAMENT`, PK `idequipament`) — maestro de 6 campos, confirmado deliberadamente delgado.

`GET /container-equipment/{idequipament}` → 200:
```json
{ "idequipament": "long", "refequipament": "string", "matriculaiso": "string", "idtipequipament": "integer", "propietari": "string", "idoridade": "string" }
```
`POST /container-equipment` — body: los mismos 6 campos sin `idequipament` (generado por el servicio).
`PATCH /container-equipment/{idequipament}` — body: cualquier subconjunto de `refequipament, matriculaiso, idtipequipament, propietari, idoridade`.

**No incluir** en este recurso: peso, estado aduanero, situación aduanera — esos campos son propios de cada bounded context consumidor (ver `MmppNotifEquipament`, `VTcMAduanaContenidor` en `events-catalog.md` §13), no del maestro.

### `/api/v1/sewage-consumptions` — Clavegueram
**Fuente:** `dataaccess/dto/clavegueram/ClvgConsums.java` (tabla `CLVG_CONSUMS`, PK `idconsum`)

`GET /sewage-consumptions/{idconsum}` → 200:
```json
{ "idconsum": "long", "idcarrega": "long", "polissa": "string", "nif": "string", "titular": "string", "direccio": "string", "consum": "double", "lecturaant": "double", "lecturaact": "double", "codiusaigua": "string", "estat": "string" }
```
`POST /sewage-consumptions` — body: mismos campos sin `idconsum`.

---

## Fase 1 — Quick wins

### `/api/v1/rail-operations` — Ferrocarril Portuario
**Fuente:** `dataaccess/dto/ferrocarril/OperacioFerroviaria.java` (tabla `OP_FERROVIARIA`, PK `seqoperacio`)

`POST /rail-operations` — body:
```json
{ "datoperacio": "date", "idtipoperacio": "string", "lontren": "integer", "taratren": "integer", "idopeferroviari": "string", "portescalatren": "string", "anyescalatren": "integer", "numescalatren": "integer", "carrega": "string", "descarrega": "string" }
```
`POST /rail-operations/{seqoperacio}/cancel` — sin body (transición de estado vía `idtipoperacio`).
`GET /rail-operations/{seqoperacio}` → 200: mismo shape + `facturable`, `observacions`.

ACL con Escalas: `portescalatren+anyescalatren+numescalatren` es la traducción prevista de `EscalaPk` (`idsubport+anyescala+numescala` en `Escala.java`) — confirmar el mapeo exacto de nombres de campo con el equipo antes de implementar (`portescalatren` ↔ `idsubport` no está confirmado 1:1 por nombre, solo por posición semántica).

### `/api/v1/stevedore-contracts`, `/api/v1/stevedore-work-orders` — Mano de Estiba
**Fuente:** `dataaccess/views/dto/manoEstiba/MaestContractacio.java` (tabla `MAEST_CONTRACTACIO`) y `MaestComanda.java` (tabla `MAEST_COMANDA`)

`POST /stevedore-contracts` — body:
```json
{ "datacontractacio": "date", "idtipuscontractacio": "string" }
```
`GET /stevedore-contracts/{idcontractacio}` → 200: + `idestatcontractacio`, `dataactualitzacio`.
`POST /stevedore-work-orders` — body:
```json
{ "idcontractacio": "long", "idcomandaportic": "long", "nifempresa": "string", "idtipuscomanda": "string" }
```

### `/api/v1/free-yard-requests` — Depotsis
**Fuente:** `dataaccess/dto/depotsis/DepotsisSolicitud.java` (raíz, PK `idsolicitud`) + `DepotsisSolicitudVersio.java` (detalle, PK `idsolicitut+versio`)

`POST /free-yard-requests` — body (campos de la versión inicial):
```json
{ "idocupacio": "long", "numescala": "integer", "anyescala": "integer", "idsubport": "string", "idestibador": "string", "codaranzprod": "string", "quantitat": "decimal", "datainioperacions": "date", "datafioperacions": "date" }
```
`GET /free-yard-requests/{idsolicitud}` → 200: incluye `estat`, `versio`.
Consume `/api/v1/container-equipment` solo si la solicitud referencia un contenedor concreto — no confirmado en el DTO leído (`DepotsisSolicitudVersio` no tiene campo `idequipament` explícito en la extracción recibida; verificar antes de asumir la dependencia).

---

## Fase 2 — Dominios supporting de tamaño medio

### `/api/v1/access-requests`, `/api/v1/access-cards` — PPS
**Fuente:** `dataaccess/dto/pps/Solicitud.java`/`SolicitudBase.java` (PK `port+idsolicitud`) y `SolicitudAudit.java` (PK `seqaudit`)

`POST /access-requests` — body:
```json
{ "idempresa": "string", "ntargetes": "long", "doccomplerta": "boolean", "iddepaval": "string", "tipoavalador": "string", "emailnotificacio": "string" }
```
`GET /access-cards?estado=caducada` → 200 (paginado): array de `{ "port": "string", "idsolicitud": "string", "numeracionTargeta": "string", "idestat": "string", "dataaudit": "date" }` (grounded en `SolicitudAudit.java`).

### `/api/v1/ship-waste-collections` — MARPOL
**Fuente:** `dataaccess/dto/marpol/ResidusEscala.java` (raíz, PK `idresidu`), `ResidusLot.java`, `ResidusLinea.java`

`POST /ship-waste-collections` — body:
```json
{ "idsubport": "string", "anyescala": "integer", "numescala": "integer", "idmitja": "string", "empresa": "string", "iniservei": "date", "fiservei": "date" }
```
`idestat` (integer, 1-7, ver enum en `events-catalog.md` §14) se gestiona por transición de estado, no se envía directamente en el `POST`.
`POST /ship-waste-collections/{idresidu}/weighings` — body (grounded en `ResidusLinea.java`):
```json
{ "idtipus": "string", "idsubtipus": "string", "idunitat": "string", "quantitat": "decimal", "ncamions": "integer", "ncont": "integer" }
```

### `/api/v1/water-supply-requests`, `/api/v1/marina-berths`, `/api/v1/fishing-landing-notes` — Servicios Auxiliares al Buque
**`/api/v1/water-supply-requests`** — ⚠️ **sin DTO fuente real disponible** (ver gap confirmado en `events-catalog.md` §15). Schema provisional basado en la vista `VTcSaSolicitud.java` (solo lectura, no confirmar como contrato de escritura):
```json
{ "idsubport": "string", "idtipussum": "string", "anyescala": "integer", "numescala": "integer", "seqatracada": "integer", "idvaixell": "integer", "quantitat": "float" }
```
**No implementar este endpoint hasta recuperar el DTO transaccional real** (tarea técnica en `jira-backlog.md` EPIC-06).

**`/api/v1/marina-berths`** — grounded en `dataaccess/dto/marinas/MarinaDadesAtracada.java` (PK `seqdades`):
```json
{ "idusuari": "string", "idsubport": "string", "idtitol": "integer", "nomvaixell": "string", "matricula": "string", "nompropietari": "string", "eslora": "decimal", "maniga": "decimal", "dataentrada": "date" }
```

**`/api/v1/fishing-landing-notes`** — grounded en `dataaccess/dto/gpesca/Albara.java`/`AlbaraBase.java` (PK `idport+idalbara`):
```json
{ "idarmador": "long", "idvaixell": "long", "importtotal": "decimal", "numalbara": "string", "origen": "long" }
```

### `/api/v1/land-transport-preadvices`, `/api/v1/land-transport-authorizations` — Transporte Terrestre
**Fuente:** `dataaccess/dto/transporteterrestre/Preavis.java`/`PreavisBase.java` (PK `portpreavis+seqpreavis`), `AutorizacionGenerica.java` (PK `portautoritzacio+seqautoritzacio`)

`POST /land-transport-preadvices` — body:
```json
{ "idconsignatari": "string", "tipuspreavis": "string", "trasllat": "string", "datoperacio": "date", "matcontenidor": "string", "refcontenidor": "string" }
```
`POST /land-transport-preadvices/{id}/authorize` — sin body, transiciona `estat`.
`POST /land-transport-authorizations` — body:
```json
{ "emptransport": "string", "nifemppeticionari": "string", "datiniautoritzacio": "date", "datfiautoritzacio": "date" }
```

---

## Fase 3 — Mercancías y Aduanas

### `/api/v1/cargo-manifests`, `/api/v1/cargo-manifests/{id}/items` — Manifiestos
**Fuente:** `dataaccess/dto/manifiestos/gestion/Manifest.java` (raíz delgada, PK `idmanifest`), `PartidaVersio.java` (PK `idpartida+versio`)

`POST /cargo-manifests` — body:
```json
{ "codedi": "string", "idtipdeclaracio": "string", "idsubport": "string", "anyescala": "integer", "numescala": "integer" }
```
`PATCH /cargo-manifests/{id}/items/{itemId}` — body (subconjunto de `PartidaVersio`):
```json
{ "estat": "string", "embalums": "integer", "pes": "long", "volum": "long", "codaranzelari": "string", "numonu": "string", "classemmpp": "string" }
```

### `/api/v1/dangerous-goods-authorizations`, `/api/v1/dangerous-goods-notifications` — MMPP
**Fuente:** `dataaccess/dto/mmpp/gestion/MmppAutoritzacio.java` (PK `idautoritzacio`), `MmppNotif.java` (PK `idnotificacio`)

`POST /dangerous-goods-notifications` — body (subconjunto, campos "entrada"):
```json
{ "idsubport": "string", "anyescala": "integer", "numescala": "integer", "idtipustransentrada": "string", "idvaixellentrada": "integer" }
```
`POST /dangerous-goods-notifications/{id}/send` — sin body, dispara circuito EDI.
`POST /dangerous-goods-authorizations` — body:
```json
{ "idnotificacio": "long", "idresolucio": "string", "dataautoritzada": "date", "datafiautoritzada": "date" }
```

### `/api/v1/border-inspection-operations` — PIF
**Gap cerrado 2026-07-11** — grounded en `dataaccess/dto/OperacioPif.java` (tabla `OPERACIO_PIF2`, PK `anyoperaciopif+seqoperaciopif`).

`POST /border-inspection-operations` — body:
```json
{ "matriculacamio": "string", "finger": "integer", "dataassignaciomoll": "date" }
```
`GET /border-inspection-operations/{anyoperaciopif}/{seqoperaciopif}` → 200: + `idestatoperaciopif` (valores confirmados: `CR`/`AP`/`PF`/`FI`/`AN`/`AF`), `tempstotal`, `tempsoperativa`, `importtotal`.

### `/api/v1/container-movements` — Aduanas / Control de Contenedores
**Fuente:** `dataaccess/dto/MovimientoContenedor.java` (DTO simple, sin tabla propia confirmada) + vista `VTcMAduanaContenidor.java` para el modelo de lectura.

`POST /container-movements` — body:
```json
{ "identificador": "string", "tipoMovimiento": "string", "fechaCargaDescarga": "date", "fechaEntradaSalida": "date", "viaEntradaSalida": "string" }
```
`GET /container-movements?matricula=...` → 200 (grounded en la vista): array de `{ "matricula": "string", "dua": "string", "estado": "string", "muelle": "string", "idequipament": "string" }`.

`GET /container-movements/reconciliation?numescala=...` → 200 (gap cerrado 2026-07-11, grounded en `ProtermCont.java`/`ErrorProcConc.java`): array de datos de terminal conciliados `{ "idregistre": "long", "refequipament": "string", "operacio": "string", "estado": "string" }` + errores asociados `{ "iderror": "long", "tipuserror": "string", "errorwarning": "string", "coderror": "long" }`.

---

## Fase 4 — Concesiones y Facturación (dos servicios separados, ver v4)

### `/api/v1/port-occupation-titles` — Título
**Fuente:** `dataaccess/dto/Titol.java` (PK `idsubport+idtitol`)

`POST /port-occupation-titles` — body:
```json
{ "datsolicitud": "date", "idtitolprecedent": "integer", "idperiodicitat": "string", "garantia": "string" }
```
`GET /port-occupation-titles/{id}` → 200: + `datlliurament`, `datatorgament`, `idestattitol`.
**No exponer `PATCH` abierto** — las actualizaciones desde Liquidación deben llegar vía el evento `TituloActualizado`, no por llamada síncrona (ver `events-catalog.md` §4).

### `/api/v1/settlements` — Liquidación
**Fuente:** `dataaccess/dto/Liquidacio.java` (PK `portliquidacio+anyliquidacio+numliquidacio`), `LiquidacioLinia.java` (PK + `numlinliquidacio`)

`POST /settlements` — body:
```json
{ "portescala": "string", "anyescala": "integer", "numescala": "integer", "idvaixell": "integer", "nomvaixell": "string", "idtarifa": "string", "hihatitol": "string", "idtitol": "integer" }
```
`POST /settlements/{id}/accept` — transición `idestatliq: GE|SE → AC`.
`POST /settlements/{id}/cancel` — transición `→ AN`.
`GET /settlements/{id}` → 200: + `idestatliq`, `impbasec`, `impivac`, `imptotalc`.
`POST /settlements/{id}/lines` — body (grounded en `LiquidacioLinia.java`):
```json
{ "idtarifa": "string", "idsubtarifa": "string", "concepte": "string", "unitats1": "decimal", "quota": "decimal", "impbase": "decimal", "idtipiva": "string" }
```

### `/api/v1/invoices` — Facturación
**Fuente:** `dataaccess/dto/Factura.java` (PK `idserfactura+portfactura+anyfactura+numfactura`)

`POST /invoices` — body:
```json
{ "datfactura": "date", "datvenciment": "date", "nomclient": "string", "nif": "string", "adreca": "string", "impbase": "decimal", "idtipiva": "string" }
```
`GET /invoices/{id}` → 200: + `idestfacturacio`, `imptotal`, `numregface`, `estatface`.
`GET /invoices/{id}/pdf` → 200 `application/pdf` (streaming de `pdfdupfactura`/`pdfsignat`, campos BLOB — nunca en el JSON).

### `/api/v1/title-guarantees` — Garantías
**Fuente:** `dataaccess/dto/Garantia.java` (PK `idsubport+seqgarantia`) — evaluar modelar como sub-recurso `/port-occupation-titles/{id}/guarantees` dado que no tiene agregado propio.

`POST /port-occupation-titles/{idtitol}/guarantees` — body:
```json
{ "iddepgestor": "string", "nomgarantia": "string", "tipus": "string", "impgarexiactual": "decimal", "impgarconstituit": "decimal", "datinivigencia": "date", "datfivigencia": "date" }
```

---

## Fase 5 — Escalas (hub central)

### `/api/v1/port-calls`, `/api/v1/port-calls/{id}/berthings` — Escalas
**Fuente:** `dataaccess/dto/escalas/Escala.java` (PK `idsubport+anyescala+numescala`), `Atracada.java` (PK + `seqatracada`)

`POST /port-calls` — body (subconjunto de `Escala.java`, ~45 campos totales, aquí solo identidad + fechas clave):
```json
{ "idestoperatiu": "string", "datsolicitud": "date", "datconfirmacio": "date", "datautoritzacio": "date" }
```
`POST /port-calls/{id}/berthings` — body (grounded en `Atracada.java`):
```json
{ "idestatatracada": "string", "datsolicitud": "date", "mollsalternatius": "string" }
```
`GET /port-calls/{id}` → 200: incluye referencia a `EscalaAspecte` (tabla `ESCALA_ASPECTE`, ~90 campos técnicos de buque — ver `events-catalog.md` para el detalle completo; **no se replica aquí por volumen**, se referencia como sub-recurso `GET /port-calls/{id}/aspects/{aspecte}`).

### `/api/v1/port-calls/{id}/cruise-details` — Cruceros
**Fuente:** `dataaccess/dto/cruceros/CreuerEscalaAudit.java` (PK `seqaudit`)
```json
{ "idesccreuer": "long", "idocupacio": "long", "consignatari": "string", "armador": "integer", "confirmada": "string" }
```

---

## Resumen de gaps de evidencia (igual que en `events-catalog.md`, aplicado a nivel de API)

| Recurso | Gap | No implementar hasta |
|---|---|---|
| `/api/v1/water-supply-requests` | DTO transaccional de Aguada no existe en el checkout — único gap real sin cerrar | Recuperar fuente real de `SaSolicitud`/`SaRegistreSuministre` |
| ~~`/api/v1/border-inspection-operations`~~ | ✅ Cerrado 2026-07-11 | — |
| ~~`/api/v1/container-movements` (conciliación)~~ | ✅ Cerrado 2026-07-11 | — |
