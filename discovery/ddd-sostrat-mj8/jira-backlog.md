# [IA-GEN] Backlog de Transformación — Descomposición SÒSTRAT (v2, grounded)

> **Borrador generado por IA** (APB AI Framework - apb-disc-epic-mono-v1.0 / apb-disc-backlog-v1.0) — pendiente validación humana. No distribuir sin revisión.
> **Label Jira obligatorio en todo ticket creado a partir de este backlog:** `ia-generado`. **Footer de descripción:** `Generado por IA (APB AI Framework — apb-disc-epic-mono-v1.0 / apb-disc-backlog-v1.0). Requiere validación humana antes de ejecutar.`
> **v2 respecto a la versión anterior**: los criterios de aceptación ahora citan campos y valores de estado reales (extraídos de las DTOs en `events-catalog.md`/`api-surface-by-phase.md`) en vez de descripciones genéricas. Se han añadido historias de transición de estado explícitas y tareas técnicas nuevas derivadas de los gaps de evidencia encontrados (Aguada, PIF, conciliación de terminales).
> **v3**: decisión inicial del usuario (2026-07-11) — núcleo financiero como un único servicio. **v4 (2026-07-11, mismo día)**: revertida tras reparentar contra el catálogo real de dominios de APB — Concesiones (Título/Garantías) y Facturación (Liquidación/Facturación) son dos dominios de negocio ya existentes y distintos en `apb-domain-catalog` (`dom-concesiones-v1`, `dom-facturacion-v1`), así que se separan en dos épicas (EPIC-13A, EPIC-13B) y dos servicios. Mano de Estiba y Clavegueram pasan a tener dominio propio (`dom-mano-estiba-v1`, `dom-clavegueram-v1`) en vez de reparenting forzado. **v5**: EPIC-14 (Escalas) deja de ser una extracción a servicio nuevo — evidencia de código confirma que ARGOS (`APB.API.TES`) ya consume la escala de SÒSTRAT en producción; se redefine como migración de maestría de dato. Total de servicios backend del roadmap: **15**. Todas se integran en un portal operativo único a nivel de presentación — ver `ui-screens-backlog.md`.

**Proyecto Jira destino:** pendiente de asignar — no existe hoy un proyecto Jira de "modernización SÒSTRAT" en la knowledge base.
**Base:** `decomposition-roadmap.md` (6 fases) + `proposals/bc-*.md` + `events-catalog.md` + `api-surface-by-phase.md`.
**Regla aplicada** (`apb-disc-backlog-v1.0`): historias INVEST, máximo 13 story points (si una historia real supera ese tamaño en refinamiento, se divide). **Regla aplicada** (`apb-disc-epic-mono-v1.0`): cada épica de extracción incluye diseño, implementación, migración de datos, tests, deploy y validación; la primera épica de cada bloque de riesgo es un quick win.
**Este backlog sigue siendo una primera pasada de planificación** (t-shirt sizing a nivel de épica, story points ilustrativos a nivel de historia) — requiere refinamiento real con los equipos antes de sprint planning, tal como exige `apb-disc-backlog-v1.0`.

---

## EPIC-00 — Fundamentos de plataforma

- **Fase:** 0 | **Valor de negocio:** habilitador | **Riesgo técnico:** medio | **Dependencias:** ninguna
- **Objetivo:** construir la infraestructura compartida (datos maestros de Equipamiento, ACL/APIM, CDC Oracle→Azure SQL) sin la cual ninguna extracción posterior es segura.
- **Criterios de éxito (DoD):** `/api/v1/container-equipment` desplegado con los 6 campos reales de `Equipament.java` (`idequipament, refequipament, matriculaiso, idtipequipament, propietari, idoridade`) y consumido en modo lectura por al menos 1 dominio piloto; réplica CDC Oracle→Azure SQL funcionando; fachada APIM publicada.

**Historias de usuario**
1. *Como* servicio de Manifiestos, *quiero* consultar `GET /api/v1/container-equipment/{idequipament}` en lugar de leer la tabla `EQUIPAMENT` directamente, *para* dejar de depender de acceso compartido a BBDD. (8 pts) — **Criterio de aceptación**: la respuesta contiene exactamente los 6 campos del maestro real, sin campos operativos (peso, estado) que pertenecen a otros contextos.
2. *Como* Arquitectura APB, *quiero* una réplica de solo lectura de Oracle en Azure SQL para el esquema de Equipamiento, *para* validar el nuevo servicio sin tocar el sistema productivo. (13 pts)
3. *Como* consumidor externo de SÒSTRAT, *quiero* acceder a los servicios ya extraídos a través de una única fachada APIM, *para* no depender de la topología interna del monolito. (5 pts)
4. *Como* arquitecto de integración, *quiero* que `POST /container-equipment` valide que `idtipequipament` existe en el catálogo `TipusEquipament` (tabla `TIPUS_EQUIPAMENT`), *para* no crear equipamiento con tipo inválido. (5 pts)

**Tareas técnicas**
- Aprovisionar namespace de Service Bus (`evt.sostrat.*`) y política de Dead Letter Queue por topic.
- Diseñar el contrato definitivo de `EquipamientoRegistrado`/`EquipamientoActualizado` en OpenAPI/AsyncAPI real a partir del schema grounded de `events-catalog.md` §13.
- Evaluar con el equipo de plataforma si `Autenticación/SSO` puede mapearse directamente sobre `APB.API.USUARIOS`/`ROL`/`PERMIS` sin desarrollo nuevo — confirmar qué devuelve realmente `authenticateSostrat` (el tipo de retorno `String` no está documentado, ver `events-catalog.md` §19).
- **[NUEVA]** Solicitar a IN2 (proveedor del legacy) o localizar en otro repositorio el código fuente de `org.apb.sostrat.dataaccess.dto.aguada.SaSolicitud`, `SaSolicitudPk`, `SaSolicitudAudit`, `SaRegistreSuministre` — confirmado ausente en este checkout (solo compilado en `sostrat-BATCH/lib/sostrat.jar`). Bloquea el diseño real de EPIC-06.
- ~~Leer `dataaccess/dto/pif/*.java`~~ — ✅ **Cerrado 2026-07-11**: no existe esa ruta; las clases reales son `dataaccess/dto/OperacioPif.java` (tabla `OPERACIO_PIF2`) y `dataaccess/views/dto/VDataSelectorareapif.java`. Ver `events-catalog.md` §10.

---

## EPIC-01 — Extracción Ferrocarril Portuario

- **Fase:** 1 (quick win) | **Valor de negocio:** medio | **Riesgo técnico:** bajo | **Dependencias:** EPIC-00
- **Objetivo:** formalizar como microservicio DOCKS la funcionalidad de tráfico ferroviario portuario.
- **Criterios de éxito:** `/api/v1/rail-operations` en producción con los campos reales de `OperacioFerroviaria.java`; ACL con Escalas mediante mapeo `portescalatren+anyescalatren+numescalatren` ↔ `EscalaPk`; god class `EscalasFerroviariasAction.java` retirada; time-to-deploy &lt; 15 min.

**Historias de usuario**
1. *Como* operador portuario, *quiero* registrar una operación ferroviaria (`POST /rail-operations` con `idtipoperacio`, `lontren`, `taratren`), *para* dejar de depender de la pantalla legacy de Struts. (8 pts)
2. *Como* operador portuario, *quiero* anular una operación ferroviaria ya registrada (`POST /rail-operations/{id}/cancel`), *para* corregir errores sin reprocesar en el monolito. (3 pts) — **Criterio de aceptación**: `idtipoperacio` solo transiciona entre los 4 valores reales de `Constantes.OPERACIONES_FERROVIARIAS_TIPO_OPERACION_*` (ENTRADA/SALIDA/MANIOBRA/INTERVENCION).
3. *Como* sistema de Escalas, *quiero* que el servicio de Ferrocarril consuma mi identificador de escala vía ACL, *para* no acoplar mi modelo interno al nuevo servicio. (5 pts)
4. *Como* operador de terminal ferroviaria, *quiero* consultar las operaciones de una escala concreta (`GET /rail-operations?portescalatren=...&anyescalatren=...&numescalatren=...`), *para* planificar maniobras del día. (5 pts)

**Tareas técnicas**
- Migrar el cliente `OpFerroviariaApi`/`CameraPassTrainsApi` para que apunte al nuevo servicio DOCKS.
- Confirmar el mapeo exacto de nombres de campo entre `portescalatren/anyescalatren/numescalatren` (Ferrocarril) e `idsubport/anyescala/numescala` (`EscalaPk` real en `Escala.java`) — no es 1:1 por nombre, solo semántico.
- Retirar progresivamente las rutas Struts `/ferrocarril*` del monolito tras validar paridad funcional.

---

## EPIC-02 — Extracción Mano de Estiba

- **Fase:** 1 (quick win) | **Valor de negocio:** medio | **Riesgo técnico:** bajo | **Dependencias:** EPIC-00
- **Objetivo:** formalizar como microservicio DOCKS el servicio externo "MST" ya referenciado en `ticketgranting-api-client`.
- **Criterios de éxito:** `/api/v1/stevedore-contracts` y `/api/v1/stevedore-work-orders` en producción con los campos reales de `MaestContractacio.java`/`MaestComanda.java`.

**Historias de usuario**
1. *Como* gestor de estiba, *quiero* registrar una contratación de personal (`POST /stevedore-contracts` con `idtipuscontractacio`), *para* dejar de usar `ManoEstibaAction.java`. (8 pts)
2. *Como* gestor de estiba, *quiero* asignar una comanda a una contratación existente (`POST /stevedore-work-orders` con `idcontractacio`, `idtipuscomanda`, `nifempresa`), *para* planificar la operativa del día. (5 pts)
3. *Como* gestor de estiba, *quiero* consultar el estado de una comanda (`idestatcomanda`), *para* saber si ya ha sido asignada o está pendiente. (3 pts)

**Tareas técnicas**
- Confirmar con el equipo propietario de "MST" el alcance real ya cubierto por ese servicio externo.
- Migrar las entidades reales (ubicadas en `dataaccess/views/dto/manoEstiba/`, no en `dataaccess/dto/manoEstiba/` que solo contiene las PK) al nuevo modelo de datos Azure SQL — nota de arquitectura: en el monolito, la entidad completa vive en un paquete distinto (`views.dto`) al de su propia PK (`dto`); confirmar si esto revela una capa de vistas de solo lectura sobre otra tabla base antes de migrar.

---

## EPIC-03 — Extracción Depotsis

- **Fase:** 1 (quick win) | **Valor de negocio:** medio | **Riesgo técnico:** bajo | **Dependencias:** EPIC-00
- **Objetivo:** extraer el depósito en muelle libre T6.
- **Criterios de éxito:** `/api/v1/free-yard-requests` en producción con los campos reales de `DepotsisSolicitud.java`/`DepotsisSolicitudVersio.java`; `struts-config-depotsis.xml` retirado.

**Historias de usuario**
1. *Como* operador de terminal, *quiero* registrar una solicitud de depósito (`POST /free-yard-requests` con `idocupacio`, `codaranzprod`, `quantitat`), *para* iniciar el proceso de desconsolidación. (8 pts)
2. *Como* operador de terminal, *quiero* consultar las versiones de una solicitud (`GET /free-yard-requests/{id}` incluye `versio`, `estat`), *para* dar seguimiento al proceso. (3 pts)
3. *Como* servicio de Liquidación, *quiero* recibir el evento `SolicitudDepotsisRegistrada`, *para* calcular la liquidación correspondiente sin acceso directo a la BBDD de Depotsis. (5 pts)

**Tareas técnicas**
- Diseñar y publicar el contrato definitivo del evento `SolicitudDepotsisRegistrada` (ya grounded en `events-catalog.md` §11, falta formalizar en AsyncAPI).
- Confirmar si `DepotsisSolicitudVersio` referencia contenedores (`idequipament`) — no se encontró ese campo en la extracción realizada; verificar antes de asumir dependencia con el servicio de datos maestros.

---

## EPIC-04 — Extracción PPS (Pases y Permisos)

- **Fase:** 2 | **Valor de negocio:** medio | **Riesgo técnico:** bajo-medio | **Dependencias:** EPIC-00
- **Objetivo:** extraer la gestión de solicitudes, tarjetas y permisos de acceso.
- **Criterios de éxito:** `/api/v1/access-requests` y `/api/v1/access-cards` en producción con los campos reales de `Solicitud.java`/`SolicitudAudit.java`; integraciones Kaba/PortIC re-cableadas; god class `TarjetasPasesAction.java` retirada.

**Historias de usuario**
1. *Como* solicitante externo, *quiero* iniciar una solicitud de pase (`POST /access-requests` con `idempresa`, `ntargetes`, `iddepaval`), *para* obtener autorización de entrada al puerto. (8 pts)
2. *Como* administrador de accesos, *quiero* ver tarjetas caducadas (`GET /access-cards?estado=caducada`, grounded en `SolicitudAudit.idestat`), *para* gestionar su renovación o baja. (5 pts)
3. *Como* sistema PPS, *quiero* integrar el conector Kaba detrás de mi nueva API, *para* que los consumidores no dependan de ese sistema físico directamente. (8 pts)
4. *Como* solicitante, *quiero* consultar el precio de mi solicitud (`preu`, campo real de `Solicitud.java`), *para* conocer el coste antes de confirmar. (3 pts)

**Tareas técnicas**
- Migrar `CN_KabaConnector`, `CN_PorticConnector`, `CN_GPCNConnector` al nuevo servicio.
- Confirmar el dominio de valores real de `tipoavalador` y `idestat` (no se extrajeron como enum explícito en el DTO, solo como `String` libre) antes de fijar el contrato de API definitivo.

---

## EPIC-05 — Extracción MARPOL/Residuos

- **Fase:** 2 | **Valor de negocio:** medio-alto | **Riesgo técnico:** medio | **Dependencias:** EPIC-00, ACL con Escalas validada en EPIC-01
- **Objetivo:** extraer la gestión de recogida de residuos MARPOL.
- **Criterios de éxito:** `/api/v1/ship-waste-collections` en producción con los campos reales de `ResidusEscala.java`/`ResidusLot.java`/`ResidusLinea.java`; los 7 estados reales (`idestat` 1-7) implementados como máquina de estados; circuito WASDIS/EDI reconectado.

**Historias de usuario**
1. *Como* operador de recogida, *quiero* registrar una recogida de residuos asociada a una escala (`POST /ship-waste-collections` con `idmitja`, `empresa`, `iniservei`, `fiservei`), *para* cumplir con la normativa MARPOL. (8 pts)
2. *Como* operador de báscula, *quiero* registrar el pesaje de un residuo (`POST /ship-waste-collections/{id}/weighings` con `idtipus`, `quantitat`, `ncamions`), *para* completar el expediente de la recogida. (5 pts)
3. *Como* autoridad portuaria, *quiero* que se genere y envíe automáticamente la declaración WASDIS, *para* cumplir el circuito EDI regulatorio. (8 pts)
4. *Como* gestor de residuos, *quiero* que una recogida transicione correctamente entre sus 7 estados reales (Recibido→Confirmado→Enviado→Pagado, o Anulado/No pagado/Reclamado), *para* reflejar el ciclo de vida real del proceso. (8 pts) — **Criterio de aceptación**: transiciones inválidas (p.ej. de "Pagado" a "Recibido") devuelven 409 con RFC 7807.

**Tareas técnicas**
- Migrar los subpaquetes `pesatges`, `contenidor`, `camio`, `codisqr` a la nueva estructura de servicio.
- Reconectar `LanzarCircuitoListaDeResiduosMARPOLTasklet.java` como job del nuevo servicio.
- Confirmar los nombres exactos de las constantes de estado 2-7 de `ResidusEscala.idestat` (solo `ID_ESTAT_RECIBIDO=1` se confirmó literalmente en el código fuente leído; los nombres 2-7 son interpretación, no cita textual — releer el fichero completo antes de codificar la máquina de estados).

---

## EPIC-06 — Extracción Servicios Auxiliares al Buque (agrupado)

- **Fase:** 2 | **Valor de negocio:** bajo-medio | **Riesgo técnico:** bajo, salvo Aguada (ver gap) | **Dependencias:** EPIC-00
- **Objetivo:** extraer Aguada, Marinas y Pesca como un único microservicio.
- **Criterios de éxito:** `marina-berths` y `fishing-landing-notes` desplegados con campos reales de `MarinaDadesAtracada.java`/`Albara.java`; `water-supply-requests` **bloqueado hasta resolver el gap de código fuente**.

**Historias de usuario**
1. *Como* gestor de marina deportiva, *quiero* registrar el atraque de una embarcación (`POST /marina-berths` con `nomvaixell`, `matricula`, `eslora`, `maniga`), *para* iniciar su liquidación anual. (5 pts)
2. *Como* gestor de actividad pesquera, *quiero* importar un albarán de descarga (`POST /fishing-landing-notes` con `idarmador`, `idvaixell`, `importtotal`), *para* registrar la actividad pesquera del día. (5 pts)
3. *Como* buque visitante, *quiero* solicitar suministro de agua potable, *para* abastecerme durante la escala. (5 pts) — **BLOQUEADA**: no se puede refinar completamente hasta recuperar el DTO fuente real (ver tarea técnica).

**Tareas técnicas**
- **[CRÍTICA, bloqueante]** Recuperar el código fuente real de `SaSolicitud`, `SaSolicitudPk`, `SaSolicitudAudit`, `SaRegistreSuministre` (paquete `dataaccess.dto.aguada`) — confirmado ausente de este checkout, solo existe compilado en `sostrat-BATCH/lib/sostrat.jar`. Sin esto, el contrato de `water-supply-requests` solo puede basarse en la vista de solo lectura `VTcSaSolicitud` (ver `api-surface-by-phase.md` Fase 2), que no es fiable como contrato de escritura.
- Confirmar con negocio si BUNKER debe añadirse como cuarto sub-recurso (no encontrado en el código) o excluirse definitivamente.

---

## EPIC-07 — Descomposición interna y extracción de Transporte Terrestre

- **Fase:** 2 | **Valor de negocio:** medio | **Riesgo técnico:** medio | **Dependencias:** EPIC-00
- **Objetivo:** descomponer internamente Parquing, después extraer el conjunto.
- **Criterios de éxito:** `/api/v1/land-transport-preadvices` y `/api/v1/land-transport-authorizations` en producción con campos reales de `Preavis.java`/`AutorizacionGenerica.java`; circuito CODECO reconectado.

**Historias de usuario**
1. *Como* transportista, *quiero* registrar un preaviso (`POST /land-transport-preadvices` con `idconsignatari`, `tipuspreavis`, `matcontenidor`), *para* solicitar acceso al recinto portuario con mi carga. (8 pts)
2. *Como* autoridad portuaria, *quiero* conceder o denegar una autorización genérica/específica (`emptransport`, `nifemppeticionari`, `datfiautoritzacio`), *para* controlar el acceso de transportistas. (8 pts)
3. *Como* transportista, *quiero* consultar el motivo de rechazo de mi preaviso (`motivorechazo`, campo real de `Preavis.java`), *para* corregir y reenviar. (3 pts)
4. *Como* gestor de parquing, *quiero* asignar una plaza a un vehículo autorizado, *para* gestionar el espacio físico disponible. (5 pts)

**Tareas técnicas**
- Refactorizar `PreavisAction.java` (1.347 líneas) sacando lógica de negocio a la capa de servicio antes de la extracción.
- Diseñar el sub-recurso `parquing` como posible servicio independiente en una fase posterior.

---

## EPIC-08 — Refactor interno de Manifiestos (pre-extracción)

- **Fase:** 3 (paso previo obligatorio) | **Valor de negocio:** habilitador | **Riesgo técnico:** alto | **Dependencias:** ninguna (puede empezar en paralelo)
- **Objetivo:** romper `CN_Manifest_Impl.java` (3.929 líneas) y `CN_Partida_Impl.java` (3.338 líneas) antes de exponerlos como microservicio.
- **Criterios de éxito:** ninguna clase de servicio de Manifiestos supera las 500 líneas; cobertura de tests de regresión antes de tocar el código.

**Historias de usuario**
1. *Como* equipo de desarrollo, *quiero* tests de caracterización sobre `CN_Manifest_Impl`, *para* poder refactorizar con seguridad. (13 pts)
2. *Como* equipo de desarrollo, *quiero* separar la lógica EDI de la lógica de negocio de manifiestos, *para* reducir el tamaño de las clases god. (13 pts)
3. *Como* equipo de desarrollo, *quiero* aislar la gestión de `PartidaVersio` (versión de partida) del resto de `CN_Partida_Impl`, *para* que el modelo versionado quede explícito en el código, no implícito. (8 pts)

**Tareas técnicas**
- Épica puramente técnica (foundation) — sin entrega de valor de usuario directo, excepción documentada por `apb-disc-epic-mono-v1.0`.

---

## EPIC-09 — Extracción MMPP y PIF

- **Fase:** 3 | **Valor de negocio:** alto (regulatorio) | **Riesgo técnico:** medio | **Dependencias:** EPIC-00
- **Objetivo:** extraer Mercancías Peligrosas y control fronterizo.
- **Criterios de éxito:** `/api/v1/dangerous-goods-authorizations`, `/api/v1/dangerous-goods-notifications` y `/api/v1/border-inspection-operations` en producción con campos reales de `MmppAutoritzacio.java`/`MmppNotif.java`/`OperacioPif.java`.

**Historias de usuario**
1. *Como* gestor de mercancías peligrosas, *quiero* solicitar una autorización (`POST /dangerous-goods-authorizations` con `idnotificacio`, `idresolucio`), *para* cumplir la normativa antes de operar la mercancía. (8 pts)
2. *Como* autoridad competente, *quiero* recibir la notificación EDI de mercancía peligrosa automáticamente (`viaedi=S`), *para* cumplir el plazo regulatorio. (8 pts)
3. *Como* gestor de mercancías peligrosas, *quiero* consultar el motivo de rechazo de una autorización (`idmotiurebuig`, `descmotiurebuig`, campos reales), *para* corregir y volver a solicitar. (3 pts)
4. *Como* inspector fronterizo, *quiero* registrar una operación de inspección en un área PIF (`POST /border-inspection-operations` con `matriculacamio`, `finger`), *para* dejar constancia del control aduanero. (5 pts)
5. *Como* inspector fronterizo, *quiero* que la operación transicione entre sus 6 estados reales (`CR`/`AP`/`PF`/`FI`/`AN`/`AF`), *para* reflejar el ciclo de vida real de la inspección. (5 pts) — nombres completos de los estados pendientes de confirmar con negocio (solo se conocen los códigos).

**Tareas técnicas**
- Migrar los subpaquetes `hazmat`, `inspecciones`, `edi` de MMPP a la nueva estructura de servicio.
- ~~Leer `dataaccess/dto/pif/*.java`~~ — ✅ **Cerrado 2026-07-11**, ver `events-catalog.md` §10.
- Confirmar con negocio el catálogo completo de ~40 constantes `CODERR_*` de `ErrorProcConc.java` antes de fijar el enum definitivo de errores de inspección (si aplica a PIF; confirmado que existe para conciliación de terminales, ver EPIC-11).

---

## EPIC-10 — Extracción Manifiestos

- **Fase:** 3 | **Valor de negocio:** alto | **Riesgo técnico:** alto | **Dependencias:** EPIC-08, EPIC-00
- **Objetivo:** extraer la gestión de manifiestos y partidas ya refactorizada internamente.
- **Criterios de éxito:** `/api/v1/cargo-manifests` en producción con campos reales de `Manifest.java`/`PartidaVersio.java`; circuito EDI reconectado; cero incidentes de disponibilidad.

**Historias de usuario**
1. *Como* agente de aduanas, *quiero* registrar un manifiesto (`POST /cargo-manifests` con `codedi`, `idtipdeclaracio`), *para* iniciar el proceso de descarga. (13 pts)
2. *Como* agente de aduanas, *quiero* actualizar una partida existente (`PATCH /cargo-manifests/{id}/items/{itemId}` con `estat`, `pes`, `volum`), *para* corregir datos antes del despacho. (8 pts)
3. *Como* agente de aduanas, *quiero* consultar el código ONU/clase MMPP de una partida (`numonu`, `classemmpp`, campos reales de `PartidaVersio.java`), *para* saber si requiere tratamiento como mercancía peligrosa. (5 pts)
4. *Como* servicio de Liquidación, *quiero* recibir el evento `ManifiestoCircuitoProcesado`, *para* calcular las liquidaciones asociadas. (5 pts)

**Tareas técnicas**
- Migración de datos histórica de `PARTIDA_VERSIO`/`MERCADERIA` a Azure SQL, con estrategia de doble escritura durante la transición.
- Confirmar el detalle real de `MercaderiaDades`/`MercaderiaDadesIdioma` (no leídas en esta extracción, `Mercaderia.java` en sí es solo la PK `codaranzelari`) antes de completar el contrato de partidas.

---

## EPIC-11 — Consolidación y extracción de Aduanas/Control de Contenedores

- **Fase:** 3 | **Valor de negocio:** medio | **Riesgo técnico:** medio-alto | **Dependencias:** EPIC-00
- **Objetivo:** unificar `service/aduanas` + `service/terminales`, después extraer.
- **Criterios de éxito:** lógica consolidada; `/api/v1/container-movements` en producción con campos reales de `MovimientoContenedor.java`; integración con Grimaldi migrada o mantenida vía ACL.

**Historias de usuario**
1. *Como* equipo de desarrollo, *quiero* unificar `service/aduanas` y `service/terminales` en un único paquete de dominio, *para* poder extraerlo como servicio limpio. (13 pts)
2. *Como* operador de terminal, *quiero* registrar el traslado de un contenedor (`POST /container-movements` con `identificador`, `tipoMovimiento`), *para* actualizar su ubicación en el sistema. (8 pts)
3. *Como* naviera Grimaldi (consumidor externo), *quiero* seguir consultando cambios de equipos por código EDI, *para* no interrumpir mi integración actual durante la migración. (8 pts)
4. *Como* auditor aduanero, *quiero* consultar el estado de un contenedor en tránsito (`GET /container-movements?matricula=...`, grounded en la vista `VTcMAduanaContenidor`), *para* verificar su situación aduanera. (5 pts)

**Tareas técnicas**
- Coordinar con la naviera Grimaldi la ventana de migración de su integración SOAP actual.
- ~~Leer los DTOs asociados al proceso `ConciliarDades.java`~~ — ✅ **Cerrado 2026-07-11**: `ProtermCont.java` (tabla `PROTERM_CONT`) y `ErrorProcConc.java` (errores/warnings de conciliación). Ver `events-catalog.md` §12 (evento `DatosTerminalConciliados` + `ErrorConciliacionDetectado`).

---

## EPIC-12 — Desacoplamiento Título↔Liquidación (evento-driven)

- **Fase:** 4 (prerequisito de EPIC-13A/EPIC-13B) | **Valor de negocio:** habilitador | **Riesgo técnico:** alto | **Dependencias:** ninguna, pero debe completarse antes de EPIC-13A/EPIC-13B — ahora es un requisito duro, no solo arquitectónico, porque Concesiones y Facturación son servicios separados con bases de datos separadas.
- **Objetivo:** sustituir la escritura directa de Liquidación sobre tablas de Título (`UPDATE TITOL_MINIM_DADES`, `CN_Liquidacion_Impl.java:434`) por el evento `TituloActualizado`.
- **Criterios de éxito:** cero escrituras cruzadas de tabla; evento publicado y consumido en staging ≥2 semanas antes de retirar el código legacy.

**Historias de usuario**
1. *Como* equipo de desarrollo, *quiero* identificar todos los puntos de escritura cruzada de Liquidación sobre Título, *para* planificar su sustitución completa. (8 pts)
2. *Como* servicio de Título, *quiero* publicar `TituloActualizado` (con `idestattitol`, `idtitolprecedent`) en cada cambio relevante, *para* que Liquidación deje de escribir directamente en mis tablas. (13 pts)
3. *Como* servicio de Liquidación, *quiero* consumir `TituloActualizado` en lugar de ejecutar `UPDATE TITOL_MINIM_DADES`, *para* eliminar el anti-patrón detectado en el código legacy. (8 pts)

**Tareas técnicas**
- Auditoría exhaustiva de las 13 clases `*Dependencias_Impl` de Liquidación para confirmar que no quedan más escrituras cruzadas sin identificar.
- Confirmar el dominio de valores real de `idestattitol` (vive en tabla relacionada `TITOL_ESTAT`, no confirmada en esta extracción) antes de diseñar la máquina de estados del evento.

---

## EPIC-13A — Extracción de Concesiones (Título / Garantías)

> **Revisado 2026-07-11**: se separa de la antigua EPIC-13 única tras reparentar los bounded contexts al catálogo real de dominios de APB — `dom-concesiones-v1` ya existe como dominio de negocio propio, distinto de Facturación. Ver `catalog-comparison.md`.

- **Fase:** 4 | **Valor de negocio:** muy alto | **Riesgo técnico:** alto | **Dependencias:** EPIC-12, EPIC-00
- **Objetivo:** extraer Título y Garantías como el servicio **Concesiones** (mapea a `dom-concesiones-v1`).
- **Criterios de éxito:** `/api/v1/port-occupation-titles` y `/api/v1/port-occupation-titles/{id}/guarantees` en producción con campos reales de `Titol.java`/`Garantia.java`; evento `TituloActualizado` publicado y consumido en staging ≥2 semanas antes del corte (prerequisito de EPIC-13B); cero incidentes durante el corte.

**Historias de usuario**
1. *Como* gestor de títulos, *quiero* otorgar un nuevo título de ocupación portuaria (`POST /port-occupation-titles` con `idperiodicitat`, `garantia`), *para* formalizar una concesión. (13 pts)
2. *Como* gestor de títulos, *quiero* que el título transicione correctamente de estado (`idestattitol`), *para* reflejar su ciclo de vida (otorgado, vigente, caducado). (8 pts)
3. *Como* gestor de garantías, *quiero* consultar las garantías asociadas a un título (`GET /port-occupation-titles/{id}/guarantees`), *para* verificar su cobertura económica (`impgarexiactual`, `impgarconstituit`). (5 pts)
4. *Como* servicio de Facturación y Liquidaciones, *quiero* consumir el evento `TituloActualizado` en lugar de escribir directamente en tablas de Título, *para* que ambos servicios puedan desplegarse de forma independiente. (8 pts)

**Tareas técnicas**
- Migración de datos de `TITOL`, `GARANTIA` a Azure SQL propio de este servicio (no compartido con Facturación).
- Resolver la ambigüedad de documentación del campo `exprovisional` en `Garantia.java` (Javadoc duplicado del campo `idmotiu`) con el equipo funcional antes de fijar el schema final del recurso `guarantees`.

---

## EPIC-13B — Extracción de Facturación y Liquidaciones

> **Revisado 2026-07-11**: separada de Concesiones — `dom-facturacion-v1` es un dominio de alcance todo el puerto (T0-T5, P33, REB, ODP), no solo lo que vive en SÒSTRAT.

- **Fase:** 4 | **Valor de negocio:** muy alto | **Riesgo técnico:** muy alto | **Dependencias:** EPIC-13A (evento `TituloActualizado` en producción), EPIC-12, EPIC-00
- **Objetivo:** extraer Liquidación y Facturación como el servicio **Facturación y Liquidaciones** (mapea a `dom-facturacion-v1`), consumiendo Título vía evento en lugar de acceso directo a BBDD.
- **Criterios de éxito:** `/api/v1/settlements` y `/api/v1/invoices` en producción con campos reales de `Liquidacio.java`/`Factura.java`; los 6 estados reales de Liquidación (`GE/SE/AC/FA/AN/ES`) implementados como máquina de estados con transiciones validadas; cero escrituras directas sobre tablas de Título; cero incidentes durante el corte.

**Historias de usuario**
1. *Como* servicio de Liquidación, *quiero* generar una liquidación (`POST /settlements`) a partir de eventos de Escalas, Título y Manifiestos, *para* calcular el importe a cobrar sin acceso directo a sus BBDD. (13 pts)
2. *Como* gestor financiero, *quiero* que una liquidación transicione correctamente `GE→SE→AC→FA` (o `→AN` desde cualquier estado no terminal), *para* respetar el ciclo de vida real confirmado en `Liquidacio.idestatliq`. (8 pts) — **Criterio de aceptación**: `POST /settlements/{id}/accept` desde estado `FA` o `AN` devuelve 409.
3. *Como* gestor financiero, *quiero* emitir una factura Facturae a partir de una liquidación aceptada (`POST /invoices`), *para* cumplir con la normativa de facturación electrónica. (13 pts)
4. *Como* gestor financiero, *quiero* descargar el PDF firmado de una factura (`GET /invoices/{id}/pdf`), *para* enviarlo al cliente — el binario nunca viaja en el JSON de la API principal. (5 pts)
5. *Como* gestor de utilities, *quiero* que las liquidaciones de Clavegueram (`ConsumClaveguerLiquidado`) se integren en este mismo servicio de Facturación, *para* no mantener un servicio de facturación separado para un módulo tan pequeño. (5 pts) — reparentado provisionalmente, ver `bc-clavegueram-v1.md`.

**Tareas técnicas**
- Migración de datos de `LIQUIDACIO`, `LIQUIDACIO_LINIA`, `FACTURA` a Azure SQL propio de este servicio (no compartido con Concesiones).
- Verificar que ninguna escritura directa sobre `TITOL`/`TITOL_MINIM_DADES` sobrevive tras consumir el evento `TituloActualizado` (auditoría de las 13 clases `*Dependencias_Impl`, ver EPIC-12).

---

## EPIC-14 — Migración de Escalas hacia ARGOS (ya NO es una extracción a servicio nuevo)

> **Redefinida 2026-07-11** tras confirmar con evidencia de código que ARGOS (`APB.API.TES`/`MS_PORTCALL`) ya consume en producción los eventos de escala/atraque emitidos por SÒSTRAT (`MSG0004 PortcallUpdated`, `MSG0017 BerthUpdated`) con un DTO que replica el modelo exacto de SÒSTRAT (`Origin=SOSTRAT`, campos `Aspecte`/`IdSubPort`/`YearPortCall`/`NumPortCall`). No son sistemas complementarios — es la misma capacidad de negocio en transición. Ver `decomposition-roadmap.md` Fase 5.

- **Fase:** 5 (última) | **Valor de negocio:** muy alto | **Riesgo técnico:** alto | **Dependencias:** EPIC-01, EPIC-05, EPIC-06 (contratos ACL ya maduros), validación previa con el equipo de ARGOS/AOM
- **Objetivo:** migrar la maestría del dato de escala/atraque hacia `APB.API.TES`/`APB.API.TBE` (ya existentes), no construir un microservicio "Escalas" nuevo. Antes de tocar esto, separar la lógica de liquidación/facturación hoy entrelazada en `EscalaAction.java` (81 referencias a `Liquidacion`/`Facturacio` encontradas) hacia el servicio de Facturación y Liquidaciones — no puede migrar junto con la escala.
- **Criterios de éxito:** decisión formal con el equipo de ARGOS documentada (ADR); lógica de liquidación separada de `EscalaAction.java` antes de cualquier migración; flujo `SOSTRAT→TES` invertido o retirado según lo acordado; los consumidores ya extraídos (Ferrocarril, MARPOL, Servicios Auxiliares) apuntando a ARGOS/TES, no a un servicio SÒSTRAT nuevo; god class `EscalaAction.java` (7.549 líneas) retirada tras completar la migración.

**Historias de usuario**
1. *Como* Arquitectura APB, *quiero* una sesión formal con el equipo de ARGOS/AOM (Alberto Ponseti, Jose Joaquin Mena) para confirmar el plan de migración de maestría del dato de escala, *para* no diseñar esta fase unilateralmente desde el lado SÒSTRAT. (8 pts — spike de decisión, no de desarrollo)
2. *Como* equipo de desarrollo, *quiero* extraer la lógica de liquidación/facturación de `EscalaAction.java` hacia el servicio de Facturación y Liquidaciones, *para* que la escala pueda migrar a ARGOS sin arrastrar responsabilidades que no le corresponden. (13 pts)
3. *Como* servicio de Cruceros (`dom-cruceros-v1`), *quiero* apuntar mi ACL hacia ARGOS/TES en lugar de a un hipotético servicio "Escalas" de SÒSTRAT, *para* alinearme con el sistema operativo real de destino. (5 pts)
4. *Como* técnico de operaciones, *quiero* que los datos técnicos del buque (`EscalaAspecte.java`, ~90 campos: eslora, manga, certificados ISPS) tengan un plan de migración claro hacia el modelo de ARGOS, *para* no perder esa información en la transición. (8 pts)

**Tareas técnicas**
- Migrar los consumidores ya extraídos (Ferrocarril, MARPOL, Servicios Auxiliares) del contrato provisional `/api/v1/port-calls` (diseñado antes de este hallazgo) hacia el contrato real de `APB.API.TES`/`APB.API.TBE`.
- Plan de corte (cutover) coordinado con el equipo de ARGOS — es el sistema con más consumidores simultáneos del roadmap.
- Corregir `proposals/bc-escalas-v1.md`: su sección "Lo que NO incluye" afirma una separación limpia de facturación/liquidación que el código real no respalda (81 referencias cruzadas en `EscalaAction.java`).

---

## EPIC-15 — Servicios Transversales de Plataforma (Clavegueram, Notificaciones, Autenticación/SSO, Carga Inicial/ETL)

> **Añadida en la revisión de completitud del backlog** — las 4 bounded contexts de `dom-servicios-transversales-plataforma-v1` no tenían épica propia en la versión anterior de este documento (solo una mención suelta de Autenticación dentro de una tarea de EPIC-00). Se corrige aquí.

- **Fase:** 0-2 (oportunista, sin bloquear el resto del roadmap) | **Valor de negocio:** bajo (Clavegueram, Carga Inicial) a habilitador (Notificaciones, Auth) | **Riesgo técnico:** bajo, salvo Auth (alcance real incierto, ver nota) | **Dependencias:** EPIC-00 (fachada APIM)
- **Objetivo:** resolver los 4 componentes "genéricos" del sistema — dos son sustituciones directas por APIs DOCKS ya existentes, uno es una extracción pequeña y autocontenida, y el cuarto es la retirada de un proceso de migración, no una extracción de negocio.
- **Criterios de éxito (DoD):** `/api/v1/sewage-consumptions` en producción (Clavegueram); decisión documentada y ejecutada sobre Notificaciones (sustitución vs. servicio propio); decisión documentada sobre Autenticación/SSO (mapeo a `APB.API.USUARIOS/ROL/PERMIS` vs. desarrollo nuevo); plan de retirada de `sostrat-CARGASINICIALES` una vez completada la migración de datos de cada dominio.

**Historias de usuario**

*Clavegueram (grounded en `ClvgConsums.java`, tabla `CLVG_CONSUMS`):*
1. *Como* gestor de facturación de utilities, *quiero* registrar una lectura de consumo de alcantarillado (`POST /sewage-consumptions` con `polissa`, `lecturaant`, `lecturaact`), *para* poder liquidar el consumo del periodo. (5 pts)
2. *Como* gestor de facturación de utilities, *quiero* consultar el histórico de consumos de una póliza (`GET /sewage-consumptions?polissa=...`), *para* revisar la evolución del consumo. (3 pts)

*Notificaciones (grounded en la firma real de `ISmsWS.enviarSMS`):*
3. *Como* Arquitectura APB, *quiero* decidir si Notificaciones se sustituye directamente por `APB.API.SMS`/`APB.API.EMAIL` o si necesita un servicio propio de orquestación, *para* no construir un microservicio innecesario. (3 pts — spike de decisión, no de desarrollo)
4. *Como* cualquier servicio ya extraído, *quiero* poder enviar un SMS reutilizando los parámetros reales de `enviarSMS` (`destinataris`, `text`, `id_objecte`), *para* no perder funcionalidad de confirmación de envío (`demanarconfirmacion`) al migrar. (5 pts)

*Autenticación/SSO (grounded en la firma real de `IAuthenticateWs.authenticateSostrat`):*
5. *Como* Arquitectura APB, *quiero* confirmar qué contiene realmente el `String` de retorno de `authenticateSostrat` (token, código, o ambos — no documentado en el código), *para* poder diseñar la migración a EntraID con seguridad. (5 pts — spike de investigación, no de desarrollo)
6. *Como* equipo de plataforma, *quiero* evaluar si los microservicios ya expuestos en `ticketgranting-api-client` (USR, GRP, MNU, ADT) cubren ya el alcance de este bounded context, *para* evitar duplicar autenticación/autorización. (8 pts)

*Carga Inicial / ETL (grounded en `CargaInicial.java`, no es negocio — es infraestructura de migración):*
7. *Como* equipo de datos, *quiero* un plan de retirada de cada código de entidad (`T`, `A`, `O`, `F`, `CONDSEG`, `MAMMPP`, `CARGAINICIAL`) a medida que su dominio correspondiente (Título, Manifiestos, MMPP, Facturación) complete su propia migración a Azure SQL, *para* no dejar un proceso batch huérfano contra un AS400 que ya no es la fuente de verdad. (8 pts) — no es una "extracción" como las demás épicas; es la contrapartida de retirada que cierra el ciclo de cada una.

**Tareas técnicas**
- Confirmar con negocio la prioridad real de Clavegueram — es candidato explícito a externalizarse (subdominio `generic`), podría no merecer ni siquiera un microservicio DOCKS propio sino delegarse a un proveedor de facturación de utilities.
- Documentar la decisión de Notificaciones/Auth en un ADR corto (usar `apb-doc-adr-v1.0`), dado que ambas son decisiones de "reusar vs. construir", no de descomposición DDD.
- Este backlog **no asigna número de fase fijo** a Clavegueram/Notificaciones/Auth/CargaInicial porque, a diferencia del resto de épicas, no están en la ruta crítica del roadmap — pueden ejecutarse en paralelo a cualquier fase, oportunistamente, sujeto a capacidad de equipo disponible.

---

## EPIC-16 — Extracción Buques (Ship Master Data)

> **Añadida en la auditoría de cobertura 2026-07-13** — `bc-buques-v1` vivía en el paquete raíz de Struts sin ticket Jira de módulo asociado, por eso no tenía épica hasta ahora.

- **Fase:** 6 | **Valor de negocio:** alto (dato maestro consumido por 3 dominios) | **Riesgo técnico:** medio (cambio de maestría de dato consumido transversalmente) | **Dependencias:** EPIC-00
- **Objetivo:** extraer el maestro de buques (`Vaixell`) como servicio de referencia, consumido por Escalas, Cruceros y MMPP.
- **Criterios de éxito (DoD):** `/api/v1/vessels` en producción con los campos reales de `Vaixell.java`; Escalas/Cruceros/MMPP consumen el maestro vía API en vez de acceso directo a `VAIXELL`; caso de uso "01.01.13 Mantenimiento de Buques" (ABM completo) migrado.

**Historias de usuario**
1. *Como* operador portuario, *quiero* dar de alta un buque (`POST /vessels` con `nomvaixell`, `callsign`, `bandera`, `mmsi`, `numlloyds`), *para* dejar de usar `VaixellAction.java`. (8 pts)
2. *Como* sistema de Cruceros, *quiero* recibir el evento `BuqueActualizado` cuando cambien `maxcalat`/`maxeslora`/`maxmaniga`/`nomvaixell`, *para* revalidar la planificación de escalas de crucero afectadas (mismo comportamiento que `arrModifCruEscOOPP` en el legacy). (5 pts) — **Criterio de aceptación**: solo estos 4 campos disparan el evento, no cualquier cambio del maestro.
3. *Como* sistema de MMPP, *quiero* consultar la ficha técnica de un buque por IMO, *para* validar transporte de mercancías peligrosas sin duplicar el maestro. (5 pts)
4. *Como* operador portuario, *quiero* dar de baja/restaurar un buque (`darDeBaja`/`restaurar`), *para* gestionar el ciclo de vida del maestro sin borrado físico. (3 pts)

**Tareas técnicas**
- Confirmar si PIF debe consumir también este maestro — no se encontró evidencia de consumo directo en el código, pero el dominio de negocio podría requerirlo.
- Migrar certificados/ISPS/Lloyd's (`VaixellCertificat*`, `VaixellISPS`, `VaixellLloyds`) como sub-recursos o entidades propias — a decidir en diseño detallado.

---

## EPIC-17 — Extracción Operadores Portuarios / Terceros (Usuari)

> **Añadida en la auditoría de cobertura 2026-07-13.** `bc-operadores-portuarios-v1` tiene `parent_domain` tentativo — **requiere confirmación de Arquitectura APB antes de sprint planning** (ver nota en el propio `bc-operadores-portuarios-v1.md`).

- **Fase:** 6 | **Valor de negocio:** alto (sujeto facturado + asignación a escalas) | **Riesgo técnico:** medio | **Dependencias:** EPIC-00
- **Objetivo:** extraer el maestro de negocio de "terceros" (consignatarios, armadores, agentes de aduanas) — **no confundir con IAM/login**, que ya cubre `dom-transversal-arq-v1`/EntraID sin necesidad de migración de lógica.
- **Criterios de éxito (DoD):** `/api/v1/port-operators` en producción con NIF/EORI/CNAE/direcciones; Escalas y Liquidación consumen este maestro para asignar consignatario/armador y sujeto facturado respectivamente.

**Historias de usuario**
1. *Como* operador portuario, *quiero* dar de alta un tercero (`POST /port-operators` con `NIF`, `EORI`, `CNAE`, `CODIAGENT`), *para* dejar de usar `UsuariAction.java`. (8 pts) — **Criterio de aceptación**: valida DNI/EORI/código de agente igual que `comprobarDNI`/`comprobarEORI`/`comprobarCodiAgent` en el legacy.
2. *Como* sistema de Escalas, *quiero* asignar un consignatario/armador a un servicio marítimo (`ServeiMaritimVaixellUsuari`), *para* saber quién es responsable de la escala. (5 pts)
3. *Como* sistema de Liquidación, *quiero* obtener los datos fiscales/dirección del sujeto facturado, *para* generar la liquidación sin duplicar el maestro. (5 pts)

**Tareas técnicas**
- **[BLOQUEANTE DE DISEÑO]** Confirmar con Arquitectura APB el `parent_domain` real — candidato tentativo `dom-operaciones-maritimas-v1`, pero es consumido también por Facturación (mismo patrón cross-domain que `bc-datos-maestros-equipamiento-v1`, EPIC-00).
- Confirmar si la capa IAM (`Operador`/`Rol`, fuera de este checkout) necesita algún puente con este maestro más allá de los campos de auditoría genérica (`IDOPEALTA`/`IDOPEMODIFICACIO`).

---

## EPIC-18 — Extracción Servicios Auxiliares de Cruceros

> **Añadida en la auditoría de cobertura 2026-07-13.**

- **Fase:** 6 | **Valor de negocio:** medio | **Riesgo técnico:** bajo | **Dependencias:** EPIC-00, extracción de Cruceros (no tiene épica propia — Cruceros sigue en Fase 5/ARGOS junto a Escalas)
- **Objetivo:** extraer buses de traslado, vigilancia en muelle y tarifas asociadas a escalas de crucero.
- **Criterios de éxito (DoD):** `/api/v1/cruise-buses` y `/api/v1/cruise-security-points` en producción con los campos reales de `CreuerBus.java`/`CreuerVigilanciaPunt.java`.

**Historias de usuario**
1. *Como* gestor de servicios de crucero, *quiero* registrar un bus de traslado con su ocupación (`CreuerBusDetall`), *para* planificar el transporte de pasajeros. (5 pts)
2. *Como* gestor de seguridad portuaria, *quiero* registrar puntos de vigilancia en muelle para una escala de crucero, *para* coordinar el servicio de seguridad. (5 pts)
3. *Como* gestor de facturación, *quiero* exportar las facturas asociadas a servicios auxiliares de crucero (`ComprobarFacturasAction`), *para* conciliar contra Facturación. (3 pts)

**Tareas técnicas**
- Confirmar con negocio si esto se despliega como parte del mismo servicio que Cruceros (Fase 5/ARGOS) o como servicio independiente — ambos comparten dominio pero no tienen por qué compartir despliegue.

---

## EPIC-19 — Extracción Capacidad e Inspección Fronteriza (SCPP)

> **Añadida en la auditoría de cobertura 2026-07-13.** `bc-inspeccion-scpp-v1` recomienda evaluar fusión con EPIC-09 (MMPP y PIF) — ver nota.

- **Fase:** 6 (evaluar mover a Fase 3, junto a EPIC-09, si se confirma la fusión) | **Valor de negocio:** medio | **Riesgo técnico:** bajo | **Dependencias:** EPIC-09
- **Objetivo:** extraer la gestión de capacidad del Puesto de Inspección Fronteriza (calendario, turnos, tipos/niveles de inspección) — distinto del registro operativo de cada inspección (`bc-pif-v1`).
- **Criterios de éxito (DoD):** `/api/v1/border-inspection-sites` en producción con capacidad diaria (`CAPMAXSTDDIA`) y calendario de turnos.

**Historias de usuario**
1. *Como* gestor del PIF, *quiero* consultar la capacidad diaria disponible de un lugar de inspección, *para* planificar turnos. (5 pts)
2. *Como* gestor del PIF, *quiero* registrar un resultado de inspección (`ResultatDInspeccio`), *para* cerrar el ciclo de control fronterizo. (5 pts)

**Tareas técnicas**
- **[DECISIÓN DE DISEÑO]** Evaluar con Arquitectura APB si este BC debe fusionarse con `bc-pif-v1` (EPIC-09) en un único servicio — comparten dominio (`dom-inspeccion-control-v1`) y ticket de origen (PIF-1429).

---

## EPIC-20 — Extracción Trámites de Cliente

> **Añadida en la auditoría de cobertura 2026-07-13.**

- **Fase:** 6 | **Valor de negocio:** bajo | **Riesgo técnico:** bajo | **Dependencias:** EPIC-17 (Operadores Portuarios)
- **Objetivo:** extraer la gestión de trámites/gestiones que un cliente inicia ante el puerto.
- **Criterios de éxito (DoD):** `/api/v1/client-procedures` en producción con los campos reales de `TramitClient.java`.

**Historias de usuario**
1. *Como* cliente/operador, *quiero* iniciar un trámite con su documentación obligatoria, *para* gestionar una solicitud ante el puerto sin papel. (5 pts)
2. *Como* gestor del puerto, *quiero* consultar y resolver trámites pendientes, *para* dar respuesta a los clientes. (5 pts)

**Tareas técnicas**
- Confirmar que el portal `carpetaclientes` (plural, sin modelo de dominio propio) puede sustituirse directamente reutilizando las APIs de Facturación/Liquidación ya extraídas, sin desarrollo adicional — así lo indica la evidencia de código (`FacturasCCAction extends FacturasAction`, etc.).

---

## EPIC-21 — Extracción Suministro Eléctrico a Buques (Shore Power)

> **Añadida en la auditoría de cobertura 2026-07-13** — corrige `bc-aguada-v1.md`, que afirmaba (incorrectamente) que esta funcionalidad no existía en el código.

- **Fase:** 6 (evaluar agrupar con EPIC-06, Aguada — mismo dominio padre `dom-suministros-buques-v1`) | **Valor de negocio:** medio | **Riesgo técnico:** bajo | **Dependencias:** EPIC-00
- **Objetivo:** extraer el suministro eléctrico a buques atracados (cold-ironing/Shore Power): lecturas, consumo, tarifación, liquidación.
- **Criterios de éxito (DoD):** `/api/v1/shore-power-readings` en producción con los campos reales de `SeLectura.java` (`V_TC_LECTURA_ELECTRICITAT`).

**Historias de usuario**
1. *Como* operador de suministro eléctrico, *quiero* registrar una lectura de consumo (`lecturainici`, `lecturafi`, `tiempoconexion`), *para* calcular el consumo real del buque atracado. (8 pts)
2. *Como* gestor de facturación, *quiero* liquidar/desliquidar/anular una lectura (`liquidacionMasiva`/`desliquidar`/`anular`), *para* gestionar el ciclo de facturación del suministro. (5 pts) — **Criterio de aceptación**: no hay enum de estados confirmado en el código, requiere spike de confirmación con negocio antes de implementar la máquina de estados.

**Tareas técnicas**
- **[SPIKE]** Confirmar con negocio el enum real de estados de una lectura (el código expone acciones pero no un campo de estado explícito documentado).
- Evaluar desplegar como sub-recurso de Aguada (EPIC-06) o como servicio independiente — mismo dominio padre, agregados distintos.

---

## EPIC-22 — Efficiency Network (Business Club)

> **Añadida en la auditoría de cobertura 2026-07-13. CORREGIDA el mismo día tras verificación adicional solicitada explícitamente por el usuario** ("asegúrate de que los nuevos dominios y apps no duplican o solapan con los identificados previamente"). La clasificación original decía *"no tiene bounded context formal, no encaja en ningún dominio revisado"* — era **incorrecta**: `EmpresaBC.java` (la entidad central de Efficiency Network) **extiende `Usuari.java`** (herencia real de clase, no solo relación FK) — es una especialización de Operadores Portuarios (EPIC-17), no un dominio aislado. Ya existe `proposals/bc-efficiency-network-v1.md`. 18 rutas Struts (conteo exacto), tablas `BC_CERTIFICACIONS`/`BC_AUDITORIA_USUARI`/`TIPUS_AUDITORIA_BC`/`TIPUS_CONEIXEMENT_BC`.

- **Fase:** 6 (nueva) | **Valor de negocio:** bajo-medio | **Riesgo técnico:** bajo | **Dependencias:** EPIC-17 (Operadores Portuarios) — **hereda su mismo bloqueante de `parent_domain`, ya no es un bloqueante nuevo/distinto**.
- **Objetivo:** extraer la gestión de empresas adheridas al programa Efficiency Network, sus certificaciones y auditorías, como extensión de Operadores Portuarios.
- **Criterios de éxito (DoD):** `/api/v1/efficiency-network-companies` en producción, marcando `Usuari.eseffnetwork="S"` (String, no boolean — corregido 2026-07-14, ver `dossier-23-operadores-portuarios.md §2`) al dar de alta una empresa BC.

**Historias de usuario**
1. *Como* gestor del programa Efficiency Network, *quiero* dar de alta una empresa adherida (`POST /efficiency-network-companies` con `raosocialbc`, `codibc`, `codiactivitatbc`), *para* dejar de usar `EmpresaENAction.java`. (5 pts)
2. *Como* gestor del programa, *quiero* registrar una certificación (`POST /efficiency-network-companies/{idusuari}/certifications` con `idtipactivitat`, `codicertif`, `datacertif`), *para* llevar el histórico de certificaciones de la empresa. (5 pts)
3. *Como* gestor del programa, *quiero* importar auditorías/certificados/conocimientos masivamente desde fichero, *para* no perder el flujo de importación ya existente (`ImportarAuditoriaENAction`/`ImportarCertificatENAction`/`ImportarConeixementENAction`). (8 pts)

**Tareas técnicas**
- **Ya NO bloqueado por falta de dominio** — bloqueado únicamente por la misma decisión pendiente de EPIC-17 (`parent_domain` de Operadores Portuarios). Resolver EPIC-17 resuelve este también.
- Confirmar con Arquitectura APB si `EmpresaBC` debe modelarse en destino como una tabla de extensión de `Usuari` (mismo patrón que el legacy) o como un perfil/rol dentro del mismo agregado.

---

## Resumen de secuenciación

| Fase | Épicas |
|---|---|
| 0 | EPIC-00, EPIC-15 (oportunista, en paralelo) |
| 1 | EPIC-01, EPIC-02, EPIC-03 |
| 2 | EPIC-04, EPIC-05, EPIC-06, EPIC-07 |
| 3 | EPIC-08, EPIC-09, EPIC-10, EPIC-11, EPIC-19 (evaluar fusión con EPIC-09) |
| 4 | EPIC-12, EPIC-13A, EPIC-13B |
| 5 | EPIC-14 |
| 6 (nueva, auditoría de cobertura 2026-07-13) | EPIC-16, EPIC-17, EPIC-18, EPIC-19, EPIC-20, EPIC-21, EPIC-22 (corregida, ya no "sin asignar") |

**Total de servicios backend: 15 + hasta 7 nuevos de la auditoría de cobertura = hasta 22** (EPIC-22 se suma tras corregirse — no es un dominio nuevo, es extensión de EPIC-17), sujeto a las decisiones de diseño marcadas como "[DECISIÓN DE DISEÑO]"/"[BLOQUEANTE DE DISEÑO]" en EPIC-17/EPIC-18/EPIC-19/EPIC-21/EPIC-22 (varias podrían fusionarse con servicios ya existentes en vez de desplegarse independientes; EPIC-22 probablemente se despliega junto a EPIC-17, no como servicio separado). Mano de Estiba y Clavegueram cuentan cada uno con dominio de negocio propio (`dom-mano-estiba-v1`, `dom-clavegueram-v1`). **Este backlog sigue sin cubrir el 100% de SÒSTRAT** — ver `coverage-audit.md` para el residuo de ~150-180 rutas Struts aún sin bounded context asignado.

## Resumen de bloqueos activos (no inventados, confirmados por evidencia)

| Bloqueo | Épica afectada | Acción requerida |
|---|---|---|
| DTO fuente de Aguada ausente del checkout | EPIC-06 | Recuperar código fuente de IN2 o localizarlo en otro repo |
| ~~DTO de PIF no leído~~ | EPIC-09 | ✅ Cerrado 2026-07-11 |
| ~~DTO de conciliación de terminales no identificado~~ | EPIC-11 | ✅ Cerrado 2026-07-11 |
| Dominio de valores de `idestattitol` no confirmado | EPIC-12, EPIC-13A | Leer `TitolEstat.java` (tabla `TITOL_ESTAT`) |
| Javadoc ambiguo en `Garantia.exprovisional` | EPIC-13A | Confirmar columna real con el equipo funcional |
| `dom-operaciones-maritimas-v1`/ARGOS **confirmado** que ya cubre Escalas (evento real `MSG0004 SOSTRAT→TES` en producción, DTO idéntico al modelo SÒSTRAT) | EPIC-14 | Ya no es "confirmar si" sino "diseñar cómo" — sesión formal con el equipo de ARGOS/AOM antes de tocar código, ver `decomposition-roadmap.md` Fase 5 |

**Nota de alcance:** este backlog no incluye historias de QA/testing, observabilidad ni seguridad como historias separadas — se asumen como parte del Definition of Done de cada historia y deben detallarse con `apb-qa-testing-strategy-v1.0` y `apb-sec-threat-model-v1.0` antes de sprint planning real.
