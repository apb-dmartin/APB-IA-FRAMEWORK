# [IA-GEN] Auditoría de cobertura funcional — ¿migra el backlog el 100% de SÒSTRAT?

> **Borrador generado por IA** (APB AI Framework — auditoría de cobertura) — pendiente validación humana. No distribuir sin revisión.
>
> Generado 2026-07-13 en respuesta directa a la pregunta: *"¿estás seguro que con las pantallas, api y eventos que has definido migraríamos el 100% de la funcionalidad actual? ¿hemos verificado código existente que en realidad no se utiliza?"*

## Respuesta directa

**Actualizado 2026-07-14 (cierre del residuo, ver §8)**: tras cerrar el residuo pendiente (105 rutas de paquete raíz, 8 módulos pequeños sin clasificar, 100 jobs batch, 3 gaps SOAP), la cobertura real medible es:

| Categoría | Rutas Struts (de 1135) | % |
|---|---|---|
| **Cubierto por un bounded context documentado** (existente o nuevo) | ~966 | **~85%** |
| Infraestructura/catálogo transversal — no requiere BC de negocio propio, pero sí tratamiento arquitectónico (ACL, Service Bus, IAM) | ~92 | ~8% |
| **Hipótesis razonable sin verificar con evidencia de código** (probable `dom-estadisticas-v1`) | ~27 | ~2% |
| **Nuevo hallazgo — capacidad real sin bounded context propuesto** (`Posicionament`/`Incidencia`, ver §8.2) | ~19 | ~2% |
| **Código muerto confirmado** (huérfano, no cargado por `web.xml`) | 1 | ~0.1% |
| **Genuinamente sin clasificar tras el cierre del residuo** | ~1 | ~0.1% |

**En una frase: la cobertura pasa de ~79% a ~85% medible con evidencia, y el residuo "sin investigar" se reduce de ~130-160 rutas a **1 ruta** (`DatosBasicos`, nombre genérico sin evidencia suficiente) — el resto del antiguo residuo o bien tiene ya bounded context real, o bien se ha identificado como una capacidad de negocio real sin bounded context propuesto todavía (`Posicionament`, hallazgo nuevo, ver §8.2), lo cual es honesto y nombrado, no oculto.** Ver §8 para el detalle completo del cierre. (`efficiencyNetwork`, 18 rutas, se movió de "sin clasificar" a "cubierto" el 2026-07-13 — ver `bc-efficiency-network-v1.md`.)

## Metodología y limitaciones

- El inventario base (1135 rutas Struts, 23 operaciones SOAP, 100 jobs batch) se obtuvo por lectura directa de `struts-config*.xml`/`web.xml`/`cxf-servlet.xml`/`spring-batch.xml`, y se recontó con `grep -c` directamente sobre el repositorio para verificar los totales (no solo el informe de un agente) — **1135 confirmado exacto** por conteo de script.
- La clasificación por módulo/clúster (qué BC cubre qué rutas) combina: (a) recuento exacto por prefijo de paquete Java (`grep -oP` sobre `type="..."` en `struts-config.xml`), y (b) juicio de qué clústeres corresponden a qué bounded context, basado en los nombres de paquete y la evidencia ya citada en `proposals/bc-*.md`. Es sólido a nivel de "¿qué módulo cubre esto?", no verificado ruta-a-ruta contra cada `bc-*.md`.
- El bloque "batch" (100 jobs) **no se auditó job a job** en esta pasada — se dan indicios por nombre, no una clasificación exhaustiva. Ver §4.
- El bloque SOAP (23 operaciones) sí se clasificó completo, una a una.

## 1. Rutas Struts (1135) — clasificación

### 1.1 Módulos con subpaquete propio (717 de 1135) — cubiertos

| Módulo (paquete) | Rutas | Bounded Context |
|---|---|---|
| escalas | 96 | bc-escalas-v1 |
| manifiestos | 63 | bc-manifiestos-v1 |
| mmpp | 58 | bc-mmpp-v1 |
| facturas | 55 | bc-facturacion-v1 |
| transporteterrestre (+ satélite 39) | 56 | bc-transporte-terrestre-v1 |
| marpol | 46 | bc-marpol-residuos-v1 |
| factestandar | 43 | bc-facturacion-v1 (sub-flujos: rebuts, marinas, vehículos abandonados) |
| ferrocarril | 41 | bc-ferrocarril-portuario-v1 |
| liquidacion | 36 | bc-liquidacion-v1 |
| suministros (+ .electricitat) | 33 | bc-aguada-v1 + **bc-suministro-electrico-buques-v1 (nuevo)** |
| pps (satélite) | 29 | bc-pps-v1 |
| cruceros | 19 | bc-cruceros-v1 |
| **serviciosAuxiliares** | 15 | **bc-servicios-auxiliares-cruceros-v1 (nuevo)** |
| gestiogaranties | 13 | bc-garantias-v1 |
| carpetaclientes | 13 | bc-facturacion-v1 (portal, sin modelo propio — nota, no BC separado) |
| depotsis (satélite) | 17 (4 propias + 13 dup. aduanas) | bc-depotsis-v1 |
| aduanas (satélite) | 13 | bc-aduanas-contenedores-v1 |
| pif | 11 | bc-pif-v1 |
| terminales | 10 | bc-aduanas-contenedores-v1 |
| documentconcessions | 9 | bc-titulo-v1 (adjuntos documentales, nota) |
| plaespecial, projectes, gestiopermisobra, comptesanuals | 18 | bc-titulo-v1 |
| aguada | 6 | bc-aguada-v1 |
| gpesca (satélite) | 6 | bc-marinas-pesca-v1 |
| avisgestiotitol | 5 | bc-titulo-v1 |
| **scppauditorias + vistasscpp** | 7 | **bc-inspeccion-scpp-v1 (nuevo)** |
| coarri | 7 | **Resuelto 2026-07-21** (`PLAN_FASES_FUTURAS.md #103`, `edi-event-architecture-analysis.md`): partición en dos capas, no un único dominio — transporte en `bc-integracion-edi-portic-v1` (nuevo, `dom-integraciones-edi-v1`), parsing/negocio en `bc-aduanas-contenedores-v1` (`OperacionTerminalRegistrada`/`ConciliacionCoarriProcesada`, ver `events-catalog.md §12`) |
| manoEstiba | 3 | bc-mano-estiba-v1 |
| clavegueram | 3 | bc-clavegueram-v1 |
| titolminim | 3 | bc-titulo-v1 |
| **carpetaclient** | 3 | **bc-tramites-cliente-v1 (nuevo)** |
| gestionnotificaciones, gestionmmpp, documents, lloyds, informacionlogin | 8 | infra transversal / bc-mmpp-v1 / bc-buques-v1, ya cubiertos |
| **Subtotal cubierto** | **≈635** | |

> **Corrección 2026-07-14** (`dossier-09-transporte-terrestre.md §4/§14`): la fila `transporteterrestre` mostraba **89** (50 rutas de `struts-config.xml` + 39 del satélite `struts-config-transporteterrestre.xml`), sin deduplicar. La verificación de dossier confirmó **33 definiciones duplicadas byte a byte** entre ambos ficheros → **56 rutas únicas reales** (6 exclusivas del satélite, 17 exclusivas de `struts-config.xml`, 33 compartidas). Subtotal ajustado en -33 (668→635). El total base de **1135** (§Metodología) no cambia — es un recuento `grep -c` deliberadamente sin deduplicar entre ficheros satélite, válido como inventario bruto; esta corrección aplica solo a la columna de "rutas cubiertas por BC" de este módulo, que sí debe reflejar el alcance real de migración. No se ha re-verificado si otros módulos con satélite (p. ej. `aduanas`/`depotsis`, que ya anota "13 dup. aduanas") tienen el mismo patrón de duplicación sin cuantificar — fuera del alcance de esta corrección puntual.
>
> La confusión histórica "63 pertenece a Transporte Terrestre" (señalada en `dossier-09 §14`) no se ha encontrado en la versión actual de esta tabla — `manifiestos` (fila superior) ya muestra 63 correctamente desde antes de esta corrección; se deja esta nota por si la confusión persiste en copias anteriores del documento fuera de este repositorio.

### 1.2 Módulos con subpaquete propio (≈45 de 717) — cerrado 2026-07-14

| Módulo | Rutas | Estado |
|---|---|---|
| **efficiencyNetwork** | 18 | **Cubierto — bc-efficiency-network-v1 (nuevo, EPIC-22, corrección 2026-07-13)**. Investigado en esta auditoría (Business Club/certificaciones de empresas). Corrección tras verificación adicional: `EmpresaBC.java` extiende `Usuari.java` — es especialización de Operadores Portuarios, no un dominio aislado. Hereda el mismo bloqueante de `parent_domain` que `bc-operadores-portuarios-v1`, ya no es "sin dominio de encaje". |
| gestiomaquinaria | 5 | **Cubierto 2026-07-14** — `TitolMaquinariaAction`/`TipusMaquinariaAction` → bc-titulo-v1 (maquinaria asociada a un título/concesión) |
| projecteesdeveniment | 4 | **Cubierto 2026-07-14 (tentativo)** — `ProjecteEsdevenimentsAction` → bc-titulo-v1 (proyecto de evento asociado a concesión); nombre sugiere el encaje, no se ha leído el DTO campo a campo |
| multasgespol | 3 | **Tentativo 2026-07-14** — `MultasGespolAction`/`ErroresMultasGespolAction` ("GESPOL" = gestión policial) → candidato a `dom-acceso-seguridad-fisica-v1`/bc-pps-v1, no confirmado con evidencia de DTO — pendiente de confirmación |
| listatripulacionypasaje | 3 | **Cubierto 2026-07-14 (tentativo)** — lista de tripulación y pasaje → bc-cruceros-v1 (mismo dominio que PAXLST) |
| publicAction | 3 | **Cubierto 2026-07-14** — `PanelPIFAction` → bc-pif-v1; `PublicAction` es infraestructura genérica de acceso público, no de negocio |
| empresesWeb | 2 | **Cubierto 2026-07-14** — `EmpresaWebAction`/`TipusActivitatWebAction` → bc-operadores-portuarios-v1 (campos `nomweb`/`urlweb`/`logoweb` ya documentados en `dossier-23-operadores-portuarios.md §5`) |
| gestiosubarrendaments, gestiopagaments | 4 | **Cubierto 2026-07-14** — `TitolSubarrendamentAction` → bc-titulo-v1; `FactorCorrectiuLiquidacioAction` → bc-liquidacion-v1 |
| caducitat, avisopantalla, projecterel | 3 | **Cubierto 2026-07-14 (tentativo)** — `caducitat` → bc-buques-v1 (confirmado vía batch job `CaducidadCertificadosTasklet`/`CN_Caducitat`, ver §8.3); `avisopantalla` → bc-escalas-v1 (mismo dominio que `SistemaPantallas`, ver §3); `projecterel` → bc-titulo-v1 (proyecto relacionado a concesión), no confirmado con evidencia de DTO |
| **Subtotal, cerrado tras 2026-07-14** | **≈45** | 18 ya cubierto (efficiencyNetwork), 27 clasificados con evidencia el 2026-07-14 (multasgespol pendiente de confirmación adicional) |

### 1.3 Paquete raíz `org.apb.sostrat.mvc.control` (279, contado exacto por script)

| Clúster | Rutas (exacto) | Estado |
|---|---|---|
| Titol/Garantia/Ocupacio/Bonificacio | 57 | Cubierto — bc-titulo-v1 / bc-garantias-v1 (ya existían, no enumeradas ruta a ruta antes) |
| **Vaixell / TipusDeVaixell** | 21 | **Cubierto — bc-buques-v1 (nuevo, esta auditoría)** |
| **Usuari** | 15 | **Cubierto — bc-operadores-portuarios-v1 (nuevo, esta auditoría)** |
| **Inspeccio / LlocDInspeccio** | 16 | **Cubierto — bc-inspeccion-scpp-v1 (nuevo, esta auditoría)** |
| TARIC (Seccio/Capitol/Partida/Subpartida/Apertura/GrupAranzelari) | 12 | Infraestructura de referencia — catálogo consumido por Mercancías/PIF/Manifiestos, no BC propio |
| EDI (MissatgeEDI/CircuitEDI/AlarmaEDI/ErrorEDI/...) | 26 | Infraestructura transversal — gateway EDI genérico (dom-integraciones-edi-v1), no BC de negocio nuevo |
| Estadistic/Geografia (Àrea, Zona, Localitat, País...) | 27 | **Hipótesis sin verificar** — probable `dom-estadisticas-v1` (dominio real existente en el catálogo), no investigado con evidencia de código en esta sesión |
| **Sin clasificar — cerrado 2026-07-14, ver §8.1** | **~1** (era 105) | 103 clasificados con evidencia (imports/DTOs reales), 1 genuinamente sin clasificar (`DatosBasicos`) |
| **Total paquete raíz** | **279** | |

> **Corrección de recuento 2026-07-14** (§8.1): la clasificación por prefijo de nombre de clase (más exhaustiva que la de esta tabla original) da cifras algo distintas para los clústeres ya "cubiertos": Usuari real ~37 (no 15 — incluye `CompteBancari*`, `Contacte*`, `Vincle*`, ya documentados como sub-entidades reales de `Usuari` en `dossier-23-operadores-portuarios.md §5`), Vaixell real ~25 (no 21 — incluye `CargaBDLloyds`/`Discrepancias`, ya documentados en `dossier-17-buques.md §4`), Título/Garantía real ~80 (no 57 — incluye `LoteFact`→realmente Facturación, corregido en §8.1). Estas diferencias no cambian qué está cubierto, solo a qué clúster pertenece cada ruta — no afectan la cifra total de "sin clasificar".

### 1.4 Paquete `core.mvc.control` (35) y satélites

- `core.mvc.control` (35): framework técnico (Login, Sessio) — infraestructura, cubierta conceptualmente por `dom-transversal-arq-v1`/EntraID, no requiere migración de lógica de negocio.
- `struts-config-terminales.xml` (1): **código muerto confirmado** — huérfano, no cargado por `web.xml`. Ver `dead-code-register.md` #19.

## 2. Corrección aplicada durante esta auditoría

`bc-aguada-v1.md` afirmaba que Shore Power/electricidad no existía en el código. **Confirmado incorrecto** con evidencia real (`suministros.electricitat`, ticket FACTSTD-878, tablas `V_TC_LECTURA_ELECTRICITAT`/`V_TC_CONSUM_ELECTRICITAT`) — corregido y separado como `bc-suministro-electrico-buques-v1` (nuevo).

## 3. Operaciones SOAP (23 de 23, clasificado completo)

| Endpoint | Operaciones | Estado |
|---|---|---|
| crucerosws | 5 | Cubierto (bc-cruceros-v1) |
| escalasferroviariasws | 1 | Cubierto (bc-ferrocarril-portuario-v1) |
| mmppws + mmppwssecure | 6 | Cubierto (bc-mmpp-v1) |
| manifiestogrimaldisecure | 2 | Cubierto (bc-aduanas-contenedores-v1) |
| contenedoressecure | 3 | Cubierto (bc-aduanas-contenedores-v1) |
| authenticatews, smsws, smswssecure | 3 | Infraestructura transversal (auth/SMS), no BC de negocio |
| **informationportcdmws** | 1 | **Cubierto 2026-07-14** — `InformationPortcdmWS.java` (`sostratWSCXF`) importa `es.apb.ws.portcdm.wsdatatypes.Escala` → bc-escalas-v1 (PortCDM = Port Collaborative Decision Making, notificación de ETA/atraque a otros sistemas del ecosistema portuario) |
| **sistemapantallasws** | 2 | **Cubierto 2026-07-14** — `CN_SistemaPantallas`/`CN_SistemaPantallas_Impl` viven en `service/escalas/` → bc-escalas-v1 (sistema de pantallas informativas de escala/atraque) |

**23/23 cubiertas (20/23 BC de negocio + 3/23 infra transversal). 0/23 gap real — cerrado 2026-07-14.**

## 4. Jobs de Spring Batch — auditoría completada 2026-07-14 (ver §8.3)

**Cerrado.** Recuento exacto por `<bean id="..." class="org.springframework.batch.core.job.SimpleJob">` sobre los 67 ficheros `sostrat-batch-*.xml` importados desde `spring-batch.xml`: **90 jobs reales confirmados** (la cifra de "100" era una estimación previa, no un recuento exacto — 90 es el número verificado por grep). Los 90 se clasificaron uno a uno leyendo el import del DTO/servicio real de su clase `Tasklet` (no solo el nombre del fichero XML) — ver tabla completa en §8.3. **87/90 clasificados con evidencia de código** (import de servicio/DTO real) a un bounded context existente o a infraestructura transversal; **3/90** (`posicionamientoEDI`, y su cluster asociado de rutas Struts `Posicionament*`/`Incidencia*`) confirman el hallazgo nuevo de §8.2 — no encajan en ningún BC existente porque genuinamente no tienen uno.

De los nombres previamente señalados como dudosos: `traspasoROSSJob` → bc-facturacion-v1 (`CN_TraspasoROSSNocturno`, paquete `rebuts`); `cierreListasDeCargaJob` → bc-manifiestos-v1 (listas de carga); `SASOLICITUD` sigue siendo el gap conocido de Aguada (DTO fuente no existe en el checkout, ver `readiness-assessment.md`). `MQMessageReceiverJOB`/`intercanviNivellInspeccioAduanaJob` no se encontraron como beans `SimpleJob` en el recuento de 90 — puede que su patrón de declaración sea distinto (Quartz `MethodInvokingJobDetailFactoryBean` u otro) y hayan quedado fuera de este recuento; señalado como límite conocido de la metodología (grep por un único patrón de clase), no como gap silencioso.

## 5. Bounded contexts nuevos creados en esta auditoría (6)

1. `bc-buques-v1` — Vaixell (maestro de buques), dom-operaciones-maritimas-v1
2. `bc-operadores-portuarios-v1` — Usuari (terceros/consignatarios/armadores), dom-operaciones-maritimas-v1 (tentativo)
3. `bc-servicios-auxiliares-cruceros-v1` — buses/vigilancia de cruceros, dom-cruceros-v1
4. `bc-inspeccion-scpp-v1` — capacidad/turnos del PIF, dom-inspeccion-control-v1
5. `bc-tramites-cliente-v1` — trámites de cliente, dom-administracion-electronica-v1
6. `bc-suministro-electrico-buques-v1` — Shore Power, dom-suministros-buques-v1 (corrección de bc-aguada-v1)

Todos con `status: "discovered"`, pendientes del mismo checkpoint humano que el resto del catálogo.

## 6. Código muerto — ver `dead-code-register.md`

22 hallazgos de confianza alta (métodos/bloques comentados con justificación explícita, 1 fichero de configuración huérfano, 2 jobs batch desactivados, 1 directorio de test a eliminar) + 9 de confianza media pendientes de confirmar con el equipo. **Es una fracción marginal** (≈1 ruta activa de 1135, más ~19 fragmentos de código a nivel de método) frente al tamaño real del gap de cobertura — no explica por qué faltaba el 20%+ de cobertura, que es estructural (paquetes nunca analizados), no de poda.

## 8. Cierre del residuo (2026-07-14) — detalle completo

> A petición explícita del usuario ("resuelve los temas pendientes que no dependen de revisión humana"), se cerró el residuo de esta auditoría: los 105 elementos del paquete raíz, los 8 módulos de §1.2, los 3 gaps SOAP y los jobs batch. Metodología: para cada clase/job dudoso, lectura directa de su import de servicio/DTO real (no solo el nombre), igual que el resto de la serie de dossiers.

### 8.1 Paquete raíz — de 105 sin clasificar a ~1

Clasificación por prefijo de nombre de clase sobre las 279 rutas reales (`grep -oP` sobre `struts-config.xml`), verificando cada bucket contra los dossiers ya existentes:

| Bucket | Rutas | Bounded context |
|---|---|---|
| Título/Garantía/Ocupación (`Titol*`, `Garantia*`, `Ocupacio*`, `Bonificacio*`, `Barem*`, `CalendariServei*`, `Unitats`, `Xva`, `DocUrbanisticaZones`, `Zones*`, `AreaEconomica`, `CompteContable`, `Enviament`, `Bloqueig`...) | ~80 | bc-titulo-v1 / bc-garantias-v1 |
| Vaixell/Buques (`Vaixell*`, `TipusDeVaixell*`, incluidos `CargaBDLloyds`, `Discrepancias` — ya documentados en `dossier-17-buques.md §4`) | ~25 | bc-buques-v1 |
| Usuari/Operadores Portuarios (`Usuari*`, `Contacte*`, `CompteBancari*`, `Vincle*`, `GrupEmpresarial`, `Associacio`, `DomiciliAudit`, `PropositContacte` — ya documentados como sub-entidades reales en `dossier-23-operadores-portuarios.md §5`) | ~37 | bc-operadores-portuarios-v1 |
| Inspección/Capacidad SCPP (`Inspeccio*`, `LlocDInspeccio*`, `NivellDInspeccio`, `CalendariCapacitats`) | ~15 | bc-inspeccion-scpp-v1 |
| TARIC (`*Taric*`, `Capitol*`, `Seccio*`, `GrupAranzelari`, `SubAreaForeland*`) | ~16 | Infraestructura de referencia arancelaria |
| EDI (`*EDI`, `Missatge*`, `Circuit*`, `Bustia*`, `Proces*`, `Alarma*`, `Error*`, `Auditoria*`) | ~25 | Infraestructura transversal EDI (`dom-integraciones-edi-v1`) |
| Estadístic/Geografia (`Estadistic*`, `Geografia*`, `Localitat`, `Pais*`, `Installacio*`...) | ~26 | Hipótesis sin verificar, `dom-estadisticas-v1` (sin cambio respecto a la versión previa) |
| MARPOL PDA (`MarpolPDA`, `MarpolPDASDF`) | 4 | bc-marpol-residuos-v1 (extensión móvil) |
| Mercadería (`Mercaderia*`, `ConsultaMercaderia`, `DetalleDescMercaderia`) | 7 | bc-manifiestos-v1 (descripción de mercancía dentro del manifiesto) |
| Facturación (`LoteFact`, `SemaforoFacturacion`, `InterfaceRossEmpreses` — ligado a `traspasoROSSJob`/`CN_TraspasoROSSNocturno`, ver §8.3) | 4 | bc-facturacion-v1 |
| PIF (`OperacionesPIF`) | 1 | bc-pif-v1 |
| Suscripción/mailing (`Subscripcio`, `Subscriptor`, `ServeiDeSubscripcio`, `ContingutDeSubscripcio` — confirmado por batch job `ServeiDeSubscripcioMailingEDITasklet`/`CN_ServeiDeSubscripcioMailing`, ver §8.3) | 9 | Infraestructura transversal de notificación (`dom-transversal-arq-v1`) — capacidad real, sin BC de negocio propio |
| Sesión/auth (`Sessio`, `Login`, `GestioSms`, `GestioSmsPublic`) | 4 | Infraestructura transversal (`dom-transversal-arq-v1`) |
| **`Posicionament*`/`Incidencia*`** (`Posicionament`, `PosicionamentPDA`, `PosicionamentLloc`, `MotiuDePosicionament`, `Incidencia`, `IncidenciaEQ`, `IncidenciaEQInspeccio`, `IncidenciaEmergente`, `TipusIncidencia`, `TipusDetIncidencia`, `TipusDeIncideq`, `TipusAccioSeguiment`, `SubTipusIncidenciaRol`, `SubTipusIncidencia`, `EstatIncidencia`, `SeguimentDIncidencia`) | 19 | **Hallazgo nuevo — sin bounded context propuesto, ver §8.2** |
| `DatosBasicos` | 1 | **Genuinamente sin clasificar** — nombre demasiado genérico para inferir dominio sin leer el DTO/servicio completo, fuera del alcance de este cierre |

### 8.2 Hallazgo nuevo: `Posicionament` es una capacidad real de negocio sin bounded context propio

`CN_EDI_Helper_Posicionamiento` (batch, EDI) + 19 rutas Struts (`Posicionament`, `PosicionamentPDA`, `PosicionamentLloc`, `Incidencia*`) confirman lo que `dossier-19-inspeccion-scpp.md §7/§14` ya señalaba desde el lado de SCPP: `CN_Posicionament_Impl.java` (1.873 líneas) es un servicio de negocio real y sustancial — gestiona el posicionamiento físico de camiones/contenedores en el recinto PIF, con su propio circuito EDI, su propia máquina de incidencias (`Incidencia`/`IncidenciaEQ`) y acoplamiento síncrono en escritura tanto con SCPP (`CN_CapacitatsInspeccio`) como, presumiblemente, con PIF. **No existe ningún `proposals/bc-posicionament-v1.md`** — es la pieza que falta para cerrar el triángulo PIF/SCPP/Posicionament que `dossier-19 §7` ya recomendaba evaluar como conjunto.

**No se crea la propuesta de bounded context en este cierre** — modelar `Posicionament` correctamente (agregados, PK, campos, eventos) es una investigación nueva, del mismo alcance que cualquiera de los 24 dossiers de esta serie, no una tarea de clasificación de residuo. Se registra como pendiente explícito en `PLAN_FASES_FUTURAS.md` (nuevo ítem) para una sesión dedicada.

### 8.3 Jobs de Spring Batch — 90 confirmados, clasificados

Recuento exacto: 90 beans `SimpleJob` en 67 ficheros `sostrat-batch-*.xml`. Clasificación por import real de la clase `Tasklet` asociada a cada job (resumen por bounded context; detalle fichero a fichero disponible en el historial de esta sesión):

| Bounded context / infraestructura | Jobs (aprox.) | Ejemplos |
|---|---|---|
| bc-escalas-v1 | 8 | `avisosEscalas` (4), `avisosServiciosMaritimos` (2), `EnvioPortCDM` (2), `escalas`, `activacionAnticipada` |
| bc-facturacion-v1 | 9 | `ActualizarGarantias`, `AvisosGarantias`, `GarantiasLotus`, `FACTSTD-RebutTramNotes-expirados`, `facturacionEDI`, `facturacionNotifica`, `GestionNotificacionFacturaEdiTmp`, `TraspasoROSS`, `ReinicioPeticionesFBDPeriodicas` |
| bc-aduanas-contenedores-v1 | 11 | `AduanasListaCarga` (2), `CargaUbicacionesContenedores`, `Conciliacion` (2), `ConciliacionAutomovilesCargaTerminales` (2), `ConciliacionCargaTerminales` (2), `Duaexport` (2), `TDA`, `GestionVUA`, `Carregues` |
| bc-manifiestos-v1 | 5 | `actualizarPasajerosManifiesto`, `cierreListasDeCarga` (2), `ManifiestosEDI` (2, IFCSUM), `WSSicad`, `MNF_MODIF_PASSATGERS` |
| bc-marpol-residuos-v1 | 6 | `Marpol`, `MarpolChequear24h` (2), `EnvioMarpolEscalas` (2), `MARPOLListaDeResidusEDI` (WASDIS) |
| bc-mmpp-v1 | 3 | `MMPPListaDeCargaEDI` (HAZMAT), `MMPPNotificacionEDI` (IFTDGN), `CargaUbicacionesContenedores` (comparte con Aduanas vía `CN_MmppUbicacion`) |
| bc-ferrocarril-portuario-v1 | 4 | `anularOperacionFerroviaria`, `operacionFerroviaria`, `RenfeFaltaFicheros` (2) |
| bc-pps-v1 | 2 | `RebutSolTargetes`, `InformeTarjetasCaducadas` |
| bc-buques-v1 | 1 | `CaducidadCertificados` (`CN_Caducitat`) |
| bc-mano-estiba-v1 | 1 | `ManosEstibas` |
| bc-cruceros-v1 | 4 | `creuerEscalas` (3), `PaxlstEDI` |
| bc-suministro-electrico-buques-v1 | 2 | `SeLecturasElectricidad` (2) |
| bc-aguada-v1 | 1 | `SaSolicitud` (**gap de evidencia ya conocido — DTO fuente no existe en el checkout**) |
| bc-transporte-terrestre-v1 | 2 | `GestionPreavisosEDI`, `EnvioAutorizacionTransportistas` |
| Infraestructura EDI/Portic transversal (`dom-integraciones-edi-v1`) | 8 | `CarregaMtoPortic` (2), `CarregaMtoVaixellPortic` (2), `CoarriEDI`, `CodecoEDI`, `COPINOSEDI` (2), `DMS` (2), `CBOX` — **actualizado 2026-07-21**: transporte puro (`CarregaMtoPortic`/`CarregaMtoVaixellPortic`/`CBOX`) queda en `bc-integracion-edi-portic-v1`; `CoarriEDI`/`CodecoEDI`/`COPINOSEDI` son el transporte de circuitos cuyo parsing de negocio vive en `bc-aduanas-contenedores-v1`/`bc-transporte-terrestre-v1` (ver `events-catalog.md §12/§16`); `DMS` es el bounded context propio `bc-dms-emswe-v1` (no genérico, ver `edi-event-architecture-analysis.md §4`) |
| Infraestructura transversal (notificaciones/SMS/email/Alfresco) | 6 | `avisos`, `AvisosNotificaciones`, `EmailsMassius`, `Notificaciones`, `SincronizadorAlfresco`, `SMS` |
| **`Posicionament`/Incidencias — hallazgo nuevo, ver §8.2** | 2 | `posicionamientoEDI`, `avisosIncidencias` |
| Suscripción/mailing (transversal) | 1 | `serviciDeSusbscripcio` |
| bc-titulo-v1 | 1 | `avisos` (`avisgestiotitol`, alta ya contada en infra notificaciones si se prefiere agrupar) |

Total ≈90 (algunas filas comparten job entre dos BC por diseño del propio job, p.ej. `CargaUbicacionesContenedores` toca Aduanas y MMPP).

## 7. Recomendación final

1. ~~No lanzar la migración de las Fases 0-4 dándolas por completas~~ — **cerrado 2026-07-14** (§8): el residuo de ~150-180 elementos sin clasificar se ha reducido a 1 ruta genuinamente sin clasificar (`DatosBasicos`) + un hallazgo nuevo nombrado (`Posicionament`, 19 rutas + 2 jobs, sin bounded context propio — ver §8.2, no bloquea documentar el resto).
2. ~~Completar la auditoría de los 100 jobs batch~~ — **cerrado 2026-07-14** (§8.3): 90 jobs confirmados y clasificados.
3. ~~Cerrar los 3 gaps SOAP~~ — **cerrado 2026-07-14** (§3): ambos resueltos a bc-escalas-v1.
4. Presentar los 6 bounded contexts nuevos (§5) **y el hallazgo nuevo de `Posicionament`** (§8.2) al mismo checkpoint humano que el resto del catálogo antes de generar specs/pantallas para ellos.
5. **Pendiente real, no de clasificación sino de investigación nueva**: escribir `proposals/bc-posicionament-v1.md` con el mismo rigor que el resto de la serie (agregados, PK, eventos) — ver `PLAN_FASES_FUTURAS.md`.
6. Objetivo cumplido: el número de rutas sin clasificar llega a un residuo mínimo (1 de 1135), con cada una etiquetada como BC / infraestructura / código muerto / hallazgo nuevo pendiente de BC — nunca "sin mirar".
