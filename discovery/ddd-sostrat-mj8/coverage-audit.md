# [IA-GEN] Auditoría de cobertura funcional — ¿migra el backlog el 100% de SÒSTRAT?

> **Borrador generado por IA** (APB AI Framework — auditoría de cobertura) — pendiente validación humana. No distribuir sin revisión.
>
> Generado 2026-07-13 en respuesta directa a la pregunta: *"¿estás seguro que con las pantallas, api y eventos que has definido migraríamos el 100% de la funcionalidad actual? ¿hemos verificado código existente que en realidad no se utiliza?"*

## Respuesta directa

**No, no era el 100% cuando se hizo la pregunta.** Con el trabajo de esta auditoría (7 bounded contexts nuevos tras la corrección de `efficiencyNetwork` + 1 corrección factual sobre Aguada + registro de código muerto), la cobertura real medible es:

| Categoría | Rutas Struts (de 1135) | % |
|---|---|---|
| **Cubierto por un bounded context documentado** (existente o nuevo, creado en esta auditoría) | ~899 | **~79%** |
| Infraestructura/catálogo transversal — no requiere BC de negocio propio, pero sí tratamiento arquitectónico (ACL, Service Bus, IAM) | ~73 | ~6% |
| **Hipótesis razonable sin verificar con evidencia de código** (probable `dom-estadisticas-v1`) | ~27 | ~2% |
| **Código muerto confirmado** (huérfano, no cargado por `web.xml`) | 1 | ~0.1% |
| **Genuinamente sin clasificar — gap real, pendiente de investigación** | ~132-159 | **~12-14%** |

**En una frase: la cobertura pasó de una cifra no medida a ~79-85% medible con evidencia, y queda un ~12-14% (≈130-160 rutas Struts) identificado y nombrado como pendiente — no oculto, no asumido como cubierto.** Los números de esta tabla son aproximados (ver §Metodología) porque la clasificación se hizo a nivel de módulo/clúster, no ruta a ruta; el orden de magnitud es fiable, el segundo decimal no. (`efficiencyNetwork`, 18 rutas, se movió de "sin clasificar" a "cubierto" el mismo día tras una corrección — ver `bc-efficiency-network-v1.md`.)

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
| transporteterrestre (+ satélite 39) | 89 | bc-transporte-terrestre-v1 |
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
| coarri | 7 | infraestructura EDI (dom-integraciones-edi-v1), nota |
| manoEstiba | 3 | bc-mano-estiba-v1 |
| clavegueram | 3 | bc-clavegueram-v1 |
| titolminim | 3 | bc-titulo-v1 |
| **carpetaclient** | 3 | **bc-tramites-cliente-v1 (nuevo)** |
| gestionnotificaciones, gestionmmpp, documents, lloyds, informacionlogin | 8 | infra transversal / bc-mmpp-v1 / bc-buques-v1, ya cubiertos |
| **Subtotal cubierto** | **≈668** | |

### 1.2 Módulos con subpaquete propio SIN clasificar (≈45 de 717) — gap real

| Módulo | Rutas | Estado |
|---|---|---|
| **efficiencyNetwork** | 18 | **Cubierto — bc-efficiency-network-v1 (nuevo, EPIC-22, corrección 2026-07-13)**. Investigado en esta auditoría (Business Club/certificaciones de empresas). Corrección tras verificación adicional: `EmpresaBC.java` extiende `Usuari.java` — es especialización de Operadores Portuarios, no un dominio aislado. Hereda el mismo bloqueante de `parent_domain` que `bc-operadores-portuarios-v1`, ya no es "sin dominio de encaje". |
| gestiomaquinaria | 5 | Sin investigar |
| projecteesdeveniment | 4 | Sin investigar (nombre sugiere "proyecto de evento", posible relación con bc-titulo-v1, no confirmado) |
| multasgespol | 3 | Sin investigar |
| listatripulacionypasaje | 3 | Sin investigar (nombre sugiere relación con Cruceros/PAXLST, no confirmado con evidencia) |
| publicAction | 3 | Sin investigar |
| empresesWeb | 2 | Sin investigar |
| gestiosubarrendaments, gestiopagaments | 4 | Sin investigar (nombres sugieren Concesiones/Título, no confirmado) |
| caducitat, avisopantalla, projecterel | 3 | Sin investigar |
| **Subtotal sin clasificar** | **≈45** | |

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
| **Sin clasificar (residuo, no investigado)** | **105** | **Gap real** |
| **Total paquete raíz** | **279** | |

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
| **informationportcdmws** | 1 | **GAP — sin cita en ningún documento previo** |
| **sistemapantallasws** | 2 | **GAP — sin cita en ningún documento previo (planificación de cruceros/lista de buques, posible solape con bc-cruceros-v1, no confirmado)** |

**17/23 cubiertas, 3/23 infra, 3/23 gap real.**

## 4. Jobs de Spring Batch (100) — auditoría PARCIAL, no completada

**Esto no se hizo job a job en esta pasada** — es la limitación más importante de esta auditoría, y se señala explícitamente en vez de darla por hecha. `events-catalog.md` documenta 41 eventos, lo que sugiere que la mayoría de los 100 jobs tienen su circuito de negocio ya identificado dentro de algún BC cubierto (MARPOL, Facturación EDI, Garantías, notificación MMPP, PIF, COARRI/CODECO/WASDIS ya bajo Aduanas/Transporte Terrestre/MARPOL), pero no se ha verificado 1 a 1. Nombres de job que **no encajan obviamente en ningún BC cubierto** y requieren investigación dedicada: `traspasoROSSJob`, `MQMessageReceiverJOB`, `cierreListasDeCargaJob`, `intercanviNivellInspeccioAduanaJob` (posiblemente bc-inspeccion-scpp-v1, no confirmado). `SASOLICITUD` ya es el gap conocido de Aguada.

**Recomendación explícita**: repetir el mismo ejercicio de clasificación (agente dedicado, mapeo job→evento→BC) antes de considerar cerrado el catálogo de eventos.

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

## 7. Recomendación final

1. **No lanzar la migración de las Fases 0-4 dándolas por completas** — antes de eso: investigar los ≈150-180 elementos aún sin clasificar (§1.2, §1.3 residuo, §4) y el residuo de 105 rutas del paquete raíz. (`efficiencyNetwork` ya no forma parte de este residuo — corregido 2026-07-13, ver `bc-efficiency-network-v1.md`.)
2. Completar la auditoría de los 100 jobs batch (job → evento → BC), pendiente.
3. Cerrar los 3 gaps SOAP (`informationportcdmws`, `sistemapantallasws`).
4. Presentar los 6 bounded contexts nuevos (§5) al mismo checkpoint humano que el resto del catálogo antes de generar specs/pantallas para ellos.
5. Una vez cerrado esto, repetir el cálculo de §"Respuesta directa" — el objetivo realista no es "demostrar 100%" sino que el número de rutas sin clasificar llegue a 0, con cada una etiquetada como BC / infraestructura / código muerto, nunca "sin mirar".
