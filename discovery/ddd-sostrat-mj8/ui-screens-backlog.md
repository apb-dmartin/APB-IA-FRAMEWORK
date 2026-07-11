# [IA-GEN] Inventario de Pantallas — Descomposición SÒSTRAT

> **Borrador generado por IA** (APB AI Framework - apb-design-frontend-design-system-v1.0 / apb-design-wcag-v1.0) — pendiente validación humana. No distribuir sin revisión.

**Stack de frontend aplicado** (obligatorio, `context/apb/standards/STANDARD_DEVELOPMENT.md`): **DevExtreme JavaScript puro** (nada de React ni TypeScript salvo excepción justificada), **WCAG 2.1 AA mínimo** en todas las pantallas.
**Base:** campos y recursos reales ya definidos en `api-surface-by-phase.md` y `events-catalog.md` — ninguna pantalla propone un campo que no exista ya en esos documentos.
**Arquitectura de presentación (decidida por el usuario, 2026-07-11)**: cada uno de los **15 servicios backend** (Concesiones y Facturación separados de nuevo; Escalas retirada del recuento por ser migración hacia ARGOS — ver `decomposition-roadmap.md` Fases 4-5) tiene **su propio frontend independiente** — es una aplicación propia en el catálogo DOCKS, con su propio ciclo de vida, pipeline y despliegue. Todos esos frontends **se integran en un portal operativo único** de cara al usuario final, exclusivamente a efectos de visualización/navegación (no de arquitectura ni de despliegue). Ver §"Portal Operativo" al final de este documento.
**Patrón de pantalla estándar aplicado** (salvo excepción anotada): **Listado** (`dxDataGrid` con filtros y paginación) → **Ficha** (`dxForm` en `dxPopup` o página propia) → **Acciones específicas** (transiciones de estado, sub-recursos).

---

## Fase 0

### App: Datos Maestros de Equipamiento
1. **Listado de Equipamiento** (`dxDataGrid`) — columnas: `refequipament`, `matriculaiso`, `idtipequipament`, `propietari`. Filtro rápido por `refequipament`/`matriculaiso`.
2. **Ficha de Equipamiento** (`dxForm` en `dxPopup`) — campos: `refequipament`, `matriculaiso`, `idtipequipament` (`dxSelectBox` contra catálogo `TipusEquipament`), `propietari`, `idoridade`.

*(Clavegueram se trata en la sección Fase 0-2 / EPIC-15 más abajo, junto al resto de servicios transversales.)*

---

## Fase 1

### App: Ferrocarril Portuario
1. **Listado de Operaciones Ferroviarias** (`dxDataGrid`) — columnas: `seqoperacio`, `datoperacio`, `idtipoperacio`, `portescalatren/anyescalatren/numescalatren`, `facturable`. Filtro por escala y por tipo de operación.
2. **Alta de Operación Ferroviaria** (`dxForm`) — campos: `idtipoperacio` (`dxSelectBox`: Entrada/Salida/Maniobra/Intervención), `lontren`, `taratren`, `idopeferroviari`, `carrega`/`descarrega` (`dxCheckBox`), `observacions`.
3. **Acción "Anular operación"** — `dxButton` + `dxConfirm` sobre la fila del listado; deshabilitado si `idtipoperacio` ya está en estado terminal.

### App: Mano de Estiba
1. **Listado de Contrataciones** (`dxDataGrid`) — columnas: `idcontractacio`, `datacontractacio`, `idtipuscontractacio`, `idestatcontractacio`.
2. **Ficha de Contratación** (`dxForm` + `dxTabPanel`) — pestaña "Datos" (campos base) + pestaña "Comandas" con `dxDataGrid` maestro-detalle: `idcomanda`, `nifempresa`, `idtipuscomanda`, `idestatcomanda`.
3. **Alta de Comanda** (`dxForm` en `dxPopup`, lanzado desde la ficha de contratación) — campos: `idcomandaportic`, `nifempresa`, `idtipuscomanda`.

### App: Depotsis
1. **Listado de Solicitudes de Depósito** (`dxDataGrid`) — columnas: `idsolicitud`, `versio`, `estat`, `numescala/anyescala`.
2. **Ficha de Solicitud** (`dxForm`) — campos: `idocupacio`, `idestibador`, `codaranzprod`, `quantitat`, `datainioperacions`/`datafioperacions`, `comentaris`.

---

## Fase 2

### App: PPS (Pases y Permisos)
1. **Listado de Solicitudes de Acceso** (`dxDataGrid`) — columnas: `idsolicitud`, `idempresa`, `ntargetes`, `datsol`, `preu`.
2. **Listado de Tarjetas Caducadas** (`dxDataGrid`, vista filtrada dedicada) — columnas: `numeracionTargeta`, `idestat`, `dataaudit` — botón de acceso rápido desde el dashboard del servicio.
3. **Alta de Solicitud** (`dxForm`) — campos: `idempresa`, `ntargetes`, `iddepaval` (`dxSelectBox`), `tipoavalador`, `emailnotificacio`.

### App: MARPOL/Residuos
1. **Listado de Recogidas de Residuos** (`dxDataGrid`) — columnas: `idresidu`, `idestat` (renderizado como badge de color, 7 estados posibles), `idsubport/anyescala/numescala`, `empresa`.
2. **Ficha de Recogida** (`dxForm` + `dxTabPanel`) — pestaña "Datos" + pestaña "Líneas de Residuo" con `dxDataGrid` maestro-detalle: `idtipus`, `idsubtipus`, `quantitat`, `ncamions`, `ncont`, `importe`.
3. **Pantalla de Pesaje** (`dxForm` específico, lanzado desde una línea) — captura de `quantitat` (integración con báscula si aplica).
4. **Widget de estado** (stepper simple, no un componente DevExtreme estándar — construir con `dxDataGrid`/CSS) mostrando la posición actual dentro de los 7 estados reales de `ResidusEscala.idestat` y bloqueando transiciones inválidas.

### App: Aguada — mapea a `dom-suministros-buques-v1`
1. **Aguada** — ⚠️ **pantalla bloqueada**: sin DTO fuente confirmado, no se define el formulario de alta hasta recuperar `SaSolicitud`/`SaRegistreSuministre` (ver `jira-backlog.md` EPIC-06). Placeholder con aviso.

### App: Marinas y Pesca — mapea a `dom-pesca-marinas-v1`
1. **Panel con 2 pestañas** (`dxTabPanel`): Marinas / Pesca.
2. **Listado de Atraques en Marina** (`dxDataGrid`) — columnas: `seqdades`, `nomvaixell`, `matricula`, `dataentrada/datasortida`.
3. **Ficha de Atraque en Marina** (`dxForm`) — campos: `nomvaixell`, `matricula`, `nompropietari`, `eslora`, `maniga`.
4. **Listado de Albaranes de Pesca** (`dxDataGrid`) — columnas: `idalbara`, `idport`, `importtotal`, `numalbara`, `dataliquidacio`.
5. **Ficha de Albarán de Pesca** (`dxForm`) — campos: `idarmador`, `idvaixell`, `importtotal`, `numalbara`.

*(Aguada y Marinas+Pesca se agrupaban antes en una única app "Servicios Auxiliares al Buque" — separadas 2026-07-11 tras reparentar contra el catálogo real, que las trata como dos dominios de negocio distintos.)*

### App: Transporte Terrestre
1. **Listado de Preavisos** (`dxDataGrid`) — columnas: `portpreavis/seqpreavis`, `tipuspreavis`, `estat`, `datlimit`, con columna condicional mostrando `motivorechazo` si el preaviso fue rechazado.
2. **Alta de Preaviso** (`dxForm`) — campos: `idconsignatari`, `tipuspreavis`, `trasllat` (`dxCheckBox`), `matcontenidor`, `refcontenidor`.
3. **Listado de Autorizaciones** (`dxDataGrid`) — columnas: `emptransport`, `nifemppeticionari`, `datfiautoritzacio`, `estat`.
4. **Pantalla de Parquing** (`dxScheduler` o `dxDataGrid` de asignación de plazas) — pendiente decidir si es sub-pantalla de esta app o app propia tras la descomposición interna prevista en `jira-backlog.md` EPIC-07.

---

## Fase 3

*(EPIC-08, refactor interno de Manifiestos: sin pantallas nuevas — épica puramente técnica.)*

### App: MMPP
1. **Listado de Notificaciones MMPP** (`dxDataGrid`) — columnas: `idnotificacio`, `idestat`, `idsubport/anyescala/numescala`, `datarecdocument`.
2. **Ficha de Notificación** (`dxForm` + `dxTabPanel`) — pestaña "Entrada" y pestaña "Salida" (el DTO real duplica estos datos, ver `events-catalog.md` §9).
3. **Listado de Autorizaciones MMPP** (`dxDataGrid`) — columnas: `idautoritzacio`, `idresolucio`, `dataautoritzada/datafiautoritzada`, `idmotiurebuig`.

### App: PIF — mapea a `dom-inspeccion-control-v1`
> Gap cerrado 2026-07-11 — grounded en `dataaccess/dto/OperacioPif.java` (tabla `OPERACIO_PIF2`).
1. **Listado de Operaciones PIF** (`dxDataGrid`) — columnas: `anyoperaciopif/seqoperaciopif`, `idestatoperaciopif` (badge, 6 estados: CR/AP/PF/FI/AN/AF), `matriculacamio`, `finger`.
2. **Ficha de Operación PIF** (`dxForm`) — campos: `dataassignaciomoll`, `tempstotal`, `tempsoperativa`, `importtotal`.
3. **Consulta de Área PIF** (`dxDataGrid`, solo lectura sobre la vista `VDataSelectorareapif`) — columnas: `numcontenidor`, `horaasignada`, `finger`, `estado`.

### App: Manifiestos
1. **Listado de Manifiestos** (`dxDataGrid`) — columnas: `idmanifest`, `codedi`, `idtipdeclaracio`, `idsubport/anyescala/numescala`.
2. **Ficha de Manifiesto** (`dxForm` + `dxDataGrid` maestro-detalle de Partidas) — columnas de partida: `idpartida`, `versio`, `estat`, `embalums`, `pes`, `volum`, `codaranzelari`, `numonu`, `classemmpp`.
3. **Indicador visual de mercancía peligrosa** — badge condicional cuando `numonu`/`classemmpp` no están vacíos, con enlace cruzado a la ficha MMPP correspondiente.

### App: Aduanas / Control de Contenedores
1. **Listado de Movimientos de Contenedor** (`dxDataGrid`) — columnas: `identificador`, `tipoMovimiento`, `fechaCargaDescarga`, `fechaEntradaSalida`.
2. **Consulta de Situación Aduanera** (`dxDataGrid`, solo lectura sobre la vista `VTcMAduanaContenidor`) — columnas: `matricula`, `dua`, `estado`, `muelle`, `mercancia`.

---

## Fase 4

*(EPIC-12, desacoplamiento Título↔Liquidación: sin pantallas nuevas — épica técnica.)*

### App: Concesiones (Título / Garantías) — mapea a `dom-concesiones-v1`
1. **Listado de Títulos** (`dxDataGrid`) — columnas: `idsubport/idtitol`, `datatorgament`, `idestattitol`, `idperiodicitat`.
2. **Ficha de Título** (`dxForm` + `dxTabPanel`) — pestaña "Datos generales" + pestaña "Garantías" con `dxDataGrid` maestro-detalle: `nomgarantia`, `tipus`, `impgarexiactual`, `impgarconstituit`, `datfivigencia`.

### App: Facturación y Liquidaciones — mapea a `dom-facturacion-v1`
1. **Listado de Liquidaciones** (`dxDataGrid`) — columnas: `portliquidacio/anyliquidacio/numliquidacio`, `idestatliq` (badge con los 6 estados reales GE/SE/AC/FA/AN/ES), `nomvaixell`, `imptotalc`. Filtro rápido por estado.
2. **Ficha de Liquidación** (`dxForm` + `dxDataGrid` maestro-detalle de Líneas) — columnas de línea: `concepte`, `unitats1`, `quota`, `impbase`, `impiva`.
3. **Acciones de transición de estado** — `dxButton` "Aceptar" / "Anular", deshabilitados según `idestatliq` actual (p.ej. "Aceptar" deshabilitado si ya está en `FA` o `AN`).
4. **Listado de Facturas** (`dxDataGrid`) — columnas: `numfactura`, `nomclient`, `nif`, `datvenciment`, `idestfacturacio`, `imptotal`.
5. **Ficha de Factura** (`dxForm` + visor de documento) — visor de PDF embebido apuntando a `GET /invoices/{id}/pdf` (el binario nunca se carga como campo de formulario, solo como recurso enlazado).

### App: Clavegueram — mapea a `dom-clavegueram-v1` (dominio propio, separado de Facturación 2026-07-11)
1. **Listado de Consumos** (`dxDataGrid`) — columnas: `idconsum`, `polissa`, `titular`, `consum`, `lecturaant/lecturaact`, `estat`.
2. **Alta de Lectura de Consumo** (`dxForm`) — campos: `polissa`, `nif`, `titular`, `lecturaact`.

---

## Fase 5 — Escalas: NO es una app nueva (revisado 2026-07-11)

> **Cambio de naturaleza confirmado por evidencia de código** (ver `decomposition-roadmap.md` Fase 5): ARGOS (`APB.API.TES`) ya consume en producción los eventos de escala/atraque de SÒSTRAT. Esta fase deja de ser "construir un frontend de Escalas nuevo" y pasa a ser "migrar la maestría del dato hacia el ecosistema ARGOS ya existente (`APB.APP.ARG`)". **No se proponen pantallas nuevas para Escalas en este documento** — cualquier pantalla de escalas/atraques/cruceros que haga falta debe evaluarse dentro del frontend de ARGOS (`APB.APP.ARG`, ya en producción), no como una app nueva del portal SÒSTRAT.
>
> `dom-cruceros-v1` sigue siendo un dominio de negocio real y separado en el catálogo (no una pestaña de Escalas) — si merece frontend propio dentro del portal es una decisión pendiente con el equipo de ARGOS, no de este análisis.

---

## Servicios transversales — actualizado tras reparentar contra el catálogo real (2026-07-11)

> La sección "EPIC-15: Servicios Transversales de Plataforma" de versiones anteriores de este documento queda retirada: Clavegueram y Mano de Estiba tienen ahora dominio propio (arriba y en Fase 1 respectivamente), y Notificaciones/Autenticación se retiraron por duplicar `dom-transversal-arq-v1`. Solo queda pendiente:

### Carga Inicial / ETL (no es una app del portal)
**Pantalla opcional de monitorización de retirada** (`dxDataGrid`) — columnas: `entidad` (T/A/O/F/CONDSEG/MAMMPP/CARGAINICIAL), `estado_migracion`, `fecha_ultima_ejecucion` — únicamente si el equipo de datos necesita visibilidad del proceso de retirada; no es una pantalla operativa de negocio, no cuenta como app del portal.

### Notificaciones / Autenticación (retirado — cubierto por `dom-transversal-arq-v1`)
Sin pantallas de negocio propias en SÒSTRAT — infraestructura ya cubierta por el dominio transversal `dom-transversal-arq-v1` (IAM: USUARIOS/ROL/PERMIS; SMS/EMAIL/NOTIFICACION/AVI), que ya existe en el catálogo con más detalle del que aportaba este análisis.

---

## Resumen cuantitativo

| Fase | Apps con pantallas propuestas | Pantallas nuevas (aprox.) | Bloqueadas por falta de evidencia |
|---|---|---|---|
| 0 | Datos Maestros de Equipamiento | 2 | — |
| 1 | Ferrocarril, Mano de Estiba, Depotsis | 8 | — |
| 2 | PPS, MARPOL, Aguada, Marinas y Pesca, Transporte Terrestre | 15 | Aguada (1 pantalla bloqueada) |
| 3 | MMPP, Manifiestos, Aduanas, PIF | 11 | — |
| 4 | Concesiones (Título+Garantías) + Facturación y Liquidaciones + Clavegueram — **3 apps separadas** | 9 | — |
| 5 | Escalas — **ya no cuenta como app nueva**, ver nota arriba | 0 | — |

**Total: 15 aplicaciones backend confirmadas** (Concesiones y Facturación separados; Mano de Estiba y Clavegueram con dominio propio; Escalas retirada del recuento por ser migración hacia ARGOS, no extracción — decisiones del 2026-07-11), cada una con su propio frontend independiente, **~45 pantallas de negocio propuestas** (PIF ya no bloqueada, gap cerrado 2026-07-11), todas integradas en el portal operativo único descrito a continuación.

---

## Portal Operativo (arquitectura de presentación, decidida 2026-07-11)

**Decisión del usuario**: los 15 frontends son aplicaciones independientes (despliegue, pipeline y ciclo de vida propios — cada una registrada como app propia en el catálogo DOCKS, análogo a como `APB.API.APPS` cataloga las APIs), pero **se integran en un portal operativo único** de cara al usuario final, **solo a efectos de visualización** — la integración es de presentación, no de arquitectura.

### Las 15 aplicaciones que se integran en el portal (con su dominio real de `apb-domain-catalog`)

| # | Aplicación | Dominio (`apb-domain-catalog`) | Fase |
|---|---|---|---|
| 1 | Datos Maestros de Equipamiento | `dom-mercancias-v1` (transversal, propuesta nueva) | 0 |
| 2 | Ferrocarril Portuario | `dom-ferrocarril-v1` | 1 |
| 3 | Mano de Estiba | `dom-mano-estiba-v1` (dominio propio, nuevo) | 1 |
| 4 | Depotsis | `dom-mercancias-v1` | 1 |
| 5 | PPS (Pases y Permisos) | `dom-acceso-seguridad-fisica-v1` | 2 |
| 6 | MARPOL/Residuos | `dom-medio-ambiente-marpol-v1` | 2 |
| 7 | Aguada | `dom-suministros-buques-v1` ⚠️ bloqueada (gap DTO) | 2 |
| 8 | Marinas y Pesca | `dom-pesca-marinas-v1` | 2 |
| 9 | Transporte Terrestre | `dom-transporte-terrestre-v1` | 2 |
| 10 | MMPP | `dom-mercancias-peligrosas-v1` | 3 |
| 11 | PIF | `dom-inspeccion-control-v1` | 3 |
| 12 | Manifiestos | `dom-mercancias-v1` | 3 |
| 13 | Aduanas/Control de Contenedores | `dom-mercancias-v1` | 3 |
| 14 | Concesiones (Título+Garantías) | `dom-concesiones-v1` | 4 |
| 15 | Facturación y Liquidaciones | `dom-facturacion-v1` | 4 |

**No forman parte de esta lista de 15**: Clavegueram tiene dominio propio (`dom-clavegueram-v1`) pero se ha integrado como app dentro del portal en Fase 4 junto a Facturación por simplicidad operativa — revisar si debe contarse como 16ª app independiente antes de comprometer el recuento final. Escalas/Cruceros no forma parte de esta lista — ver nota de Fase 5 arriba (migración hacia ARGOS, no app nueva). Notificaciones y Autenticación/SSO se reutilizan de `dom-transversal-arq-v1`, no son apps propias.

### Qué implica "integración solo de presentación" (a definir técnicamente, no decidido aún)

El **mecanismo técnico** concreto de integración queda pendiente de diseño — opciones típicas para este patrón (portal único + apps independientes) que Arquitectura APB deberá evaluar:
- **Shell + micro-frontends** (p.ej. Module Federation o equivalente) — cada app se registra como módulo cargado dinámicamente en un shell común.
- **Portal de navegación con iframes/enlaces** — más simple, menor acoplamiento técnico, experiencia de usuario algo menos fluida entre apps.
- **Design system y componentes DevExtreme compartidos** (`apb-design-frontend-design-system-v1.0`) para que las apps se vean coherentes aunque se ejecuten como aplicaciones separadas, independientemente del mecanismo de integración elegido.
- Además, cualquier pantalla relacionada con Escalas/Cruceros debería evaluarse como integración con el portal de ARGOS (`APB.APP.ARG`), no como app propia de este portal SÒSTRAT — pendiente de decidir con el equipo de ARGOS.

**Elementos transversales del portal** (no contados en las pantallas de negocio de arriba, porque pertenecen al shell del portal, no a ningún bounded context):
- Login/SSO único (apoyado en la decisión de Autenticación/SSO — mapeo a EntraID / `APB.API.USUARIOS`).
- Dashboard de inicio con acceso a las apps del portal.
- Buscador global (si se decide implementarlo — no hay evidencia de que exista hoy en SÒSTRAT).
- Notificaciones in-app (distinto de "Notificaciones" como bounded context de SMS/email transversal).

Esto es diseño de solución, no descubrimiento DDD — se recomienda tratarlo como un discovery técnico propio con las skills `apb-arch-c4-model-v1.0` (para el diagrama de contenedores del portal) y `apb-design-frontend-design-system-v1.0` (para el sistema de diseño compartido) antes de comprometer el mecanismo de integración.
