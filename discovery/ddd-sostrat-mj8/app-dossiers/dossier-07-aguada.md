# Dossier de Aplicación — Aguada

> **Borrador generado por IA** (APB AI Framework — síntesis de apb-disc-spec-gen-v1.0/apb-pm-product-analysis-v1.0/apb-arch-c4-model-v1.0/apb-arch-decompose-v1.0) — pendiente validación humana. No distribuir sin revisión.

| Campo | Valor |
|---|---|
| **Nombre de la app** | Aguada |
| **Dominio DDD** | `dom-suministros-buques-v1` (compartido con Suministro Eléctrico a Buques / Shore Power; ver §7) |
| **Bounded Context** | `bc-aguada-v1` |
| **Fase del roadmap** | Fase 2 — "Dominios supporting de tamaño medio" (`decomposition-roadmap.md`), agrupada operativamente con Marinas y Pesca bajo EPIC-06 |
| **Sistema origen** | SÒSTRAT (SOSTRAT-Sostrat-MJ8), proveedor IN2, criticidad "Muy Alta" |
| **Jira / módulo legacy** | `AIGUADA` (`APB_KNOWLEDGE_BASE.md` §"SÒSTRAT") |
| **Estado del documento** | 🔴 **PROVISIONAL — GAP DE EVIDENCIA SIN CERRAR.** El modelo transaccional real de escritura no existe como código fuente en el checkout auditado. Ver §14. |
| **Fecha de generación** | 2026-07-13 |

---

## 1. Resumen ejecutivo

**Este documento NO puede considerarse completo ni un contrato de implementación válido hasta que se recupere el código fuente real de las clases DTO transaccionales de Aguada.** Es una síntesis honesta de lo que sí se puede observar en el checkout de `SOSTRAT-Sostrat-MJ8` disponible hoy, más lo que se puede inferir indirectamente de una vista de solo lectura y de las interfaces de servicio — no es, y no debe leerse como, la especificación de un sistema completamente entendido.

Aguada es el servicio de SÒSTRAT que gestiona las solicitudes de suministro de agua potable a buques durante su escala en el puerto. Es un dominio de tamaño pequeño-mediano, con bajo acoplamiento estructural hacia Escalas (`bc-escalas-v1`, vía `EscalaPk`/`anyescala`/`numescala`) y sin relación de agregado con Suministro Eléctrico a Buques (mismo dominio padre, agregados y tablas distintos — ver §7).

El hallazgo central de este dossier, confirmado mediante búsqueda exhaustiva propia (no solo heredado de los documentos de discovery) en `C:\Users\martinde\OneDrive - Port de Barcelona\GitHub-Repos\otros\SOSTRAT-Sostrat-MJ8\`, es el siguiente:

- Las clases DTO transaccionales reales — `org.apb.sostrat.dataaccess.dto.aguada.SaSolicitud`, `SaSolicitudPk`, `SaSolicitudAudit`, `SaSolicitudAuditPk`, `SaSolicitudEstats`, `SaRegistreSuministre` — **no existen como código fuente `.java` en ningún módulo del checkout**. Solo están compiladas dentro de `sostrat-BATCH/lib/sostrat.jar` (confirmado presente, 18.678.412 bytes).
- El gap es **más profundo** de lo que documentaba la versión previa del análisis: tampoco existen como fuente las interfaces DAO transaccionales (`org.apb.sostrat.dataaccess.dao.aguada.*` — todo el paquete está ausente), aunque sí existen sus excepciones (`dataaccess/exceptions/aguada/*.java`) y las interfaces de servicio que las referencian (`CN_SolicitudAguada`, `CN_RegistroSuministro`).
- Sí existe, y es la única evidencia indirecta utilizable, la vista de solo lectura `org.apb.sostrat.dataaccess.views.dto.aguada.VTcSaSolicitud` (mapeada a `V_TC_SA_SOLICITUD`), con su DAO y su implementación JDBC completos.

Adicionalmente, esta pasada de verificación **corrige dos afirmaciones previas** de los documentos de discovery (ver detalle en §3 y §14):

1. La cifra de "27 actions de Aguada en `mvc/control/suministros/` (paquete raíz, sin `.electricitat`)" **no se ha podido confirmar**. Ese paquete contiene 7 ficheros, y ninguno es específico de Aguada — pertenecen a un módulo distinto (`service.factestandar.suministros`, facturación estándar de suministros a buque). Las acciones realmente específicas de Aguada (7) están en `mvc/control/aguada/`.
2. La afirmación "Bunkering confirmado ausente tras búsqueda exhaustiva" (de `bc-aguada-v1.md`) es **parcialmente contradicha**: existe una ruta Struts `/bunkering` y dos JSP (`bunkering.jsp`, `lbunkering.jsp`) en el checkout — no es evidencia de ausencia total, aunque tampoco hay clase de servicio o DTO de Bunkering. Ver §14.

**Recomendación**: no asignar esfuerzo de desarrollo a Aguada hasta ejecutar el plan de cierre de gap del §14. Este documento es útil hoy para: (a) que negocio valide si el alcance funcional inferido es correcto, y (b) que desarrollo dimensione el trabajo de recuperación de evidencia — no para empezar a construir el microservicio.

---

## 2. Análisis funcional

> Todo lo que sigue está marcado explícitamente como confirmado, inferido o hipotético. No se presenta ninguna suposición como hecho.

### 2.1 Qué hace Aguada (confirmado por evidencia indirecta + interfaces de servicio)

Aguada gestiona el ciclo de vida de una **solicitud de suministro de agua potable** a un buque durante su escala, desde la petición hasta el registro del suministro efectivamente realizado. La evidencia proviene de:

- `sostrat/src/org/apb/sostrat/service/aguada/CN_SolicitudAguada.java` (interfaz de servicio, **confirmado existente y leído íntegramente**)
- `sostrat/src/org/apb/sostrat/service/aguada/CN_RegistroSuministro.java` (interfaz de servicio, **confirmado existente**)
- `sostrat/src/org/apb/sostrat/dataaccess/views/dto/aguada/VTcSaSolicitud.java` (vista de lectura, **confirmado existente**)

De `CN_SolicitudAguada.java` se **confirma** (por firma de método, no por campo de negocio) que el servicio soporta:

| Operación (confirmada por firma de método) | Evidencia |
|---|---|
| Crear una solicitud (`crear(SaSolicitud, ...)`) | `CN_SolicitudAguada.java:145` |
| Modificar una solicitud (`modificar`, `modificarEntidades`, `modificarDesdeRS`) | `CN_SolicitudAguada.java:165,183,198` |
| Eliminar (borrado físico) una solicitud (`eliminar`) | `CN_SolicitudAguada.java:212` |
| Anular una petición (`anularPeticionCN`) | `CN_SolicitudAguada.java:241` |
| Consultar por clave primaria, por fecha o por subpuerto+fecha (`obtener(...)`, 4 sobrecargas) | `CN_SolicitudAguada.java:78-135` |
| Gestionar documentos asociados: justificante y albarán (`existeJustificante`, `verJustificante`, `generarJustificante`) | `CN_SolicitudAguada.java:250-269`; `CN_RegistroSuministro.java:57-76` (albarán) |
| Selección de una solicitud por pareja de operadores (`seleccionarSolicitud`, `eliminarSeleccion`, `compruebaSolicitudSeleccionadaOtros`) | `CN_RegistroSuministro.java:132`; `CN_SolicitudAguada.java:318,376` |
| Actualización automática de estados (`actualizarEstados`) | `CN_SolicitudAguada.java:47` |
| Tratamiento de cambios de atraque/escala que afectan a solicitudes (`tratarEscalasModificadas`) | `CN_SolicitudAguada.java:349` |
| Actualización del estado de la solicitud al facturar/anular factura (`actualizarFacturaEstado`, `anularFacturaEstado`) | `CN_SolicitudAguada.java:415,428` |
| Notificación por email/SMS al finalizar la solicitud (comentado en el código, ticket ESCADOS-156) | `CN_SolicitudAguada.java:337-341` (método comentado, **no activo**) |

**Registro de suministro** (`CN_RegistroSuministro`) es un sub-proceso distinto dentro del mismo agregado: registra la incidencia y el albarán del suministro físico de agua, ligado a la solicitud (`SaSolicitudPk`) — evidencia en `CN_RegistroSuministro.java:23-149`.

### 2.2 Enumeraciones confirmadas en código (no inventadas)

`CN_SolicitudAguada.java:38-40` define, como tipos internos del propio Java (por tanto, confirmados literalmente, no inferidos de datos):

```java
public enum TipoDocumento {JUSTIFICANTE, ALBARAN, FIRMA, ERES};
public enum OrigenOperacion {ESCALA, MTOSOLICITUDAGUADA};
public enum OperacionAguada {UPDCAMPOS, ALTA, MODIFICACION, BORRADO, INSTALACION, RETIRADA, ANULAR};
```

⚠️ Estos enums describen el *tipo de operación de negocio*, no el campo de estado (`idestatsol`) de la solicitud. El dominio de valores real de `idestatsol` **no está confirmado** — solo se conoce un valor de ejemplo (`"PENDENT"`) tomado del `example:` del spec OpenAPI (`specs/openapi-aguada.yaml:95`), que a su vez es una suposición razonable, no una constante confirmada en código.

### 2.3 Suposiciones explícitas (marcadas como tal)

- **Suposición**: el flujo de negocio es "solicitud → selección de pareja de operadores → registro de suministro → facturación", inferido del orden de aparición de los métodos en las interfaces de servicio. No confirmado con negocio.
- **Suposición**: `consumtotal` (campo de `VTcSaSolicitud`, tipo `String` — no numérico, ver §5) representa litros o m³ de agua suministrada. El tipo de dato `String` en vez de `Float`/`BigDecimal` es inusual y no se puede explicar sin el DTO fuente.
- **Suposición**: `idtipussum` distingue el tipo de suministro (posiblemente para diferenciar Aguada de otros suministros a buque históricamente gestionados por el mismo módulo, ver §2.4). El valor de ejemplo `"AIGUA"` (`openapi-aguada.yaml:90`) no está confirmado como constante de código.

### 2.4 Corrección de alcance frente al análisis previo — verificación propia

El fichero `bc-aguada-v1.md` documenta una corrección del 2026-07-13 reconociendo que **Shore Power / suministro eléctrico SÍ existe** en el código (bajo `service/suministros/electricitat/`), contradiciendo una versión anterior del propio análisis. Esta pasada de verificación confirma esa corrección (los ficheros `SeLecturaAction.java`, `SeConsumoAction.java`, `SeLecturaAuditAction.java` existen efectivamente bajo `sostrat/src/org/apb/sostrat/mvc/control/suministros/electricitat/`) y añade dos correcciones adicionales, ambas relevantes para no repetir el mismo error de "ausencia no verificada":

1. **La cifra "27 actions de Aguada" no se sostiene.** El paquete `mvc/control/suministros/` (raíz, sin `.electricitat`) contiene exactamente 7 ficheros: `SuministreComptadorAction.java`, `SuministreComptadorAuditAction.java`, `SuministreConsumMinimAction.java`, `SuministreOcupacioAction.java`, `SuministreOcupacioAuditAction.java`, `SuministreVaixellAction.java`, `SuministreVaixellAuditAction.java`. Por sus imports (`org.apb.sostrat.service.factestandar.suministros.CN_SuministreVaixell`, `dataaccess.dto.SuministreVaixell` — **no** `dataaccess.dto.aguada.*`), **no son de Aguada**: pertenecen a un módulo distinto de facturación estándar de suministros a buque ("FACTSTD" en el listado de proyectos Jira, `APB_KNOWLEDGE_BASE.md`), que factura consumo de agua/energía leído por contador (`SuministreComptador`) con independencia del flujo de solicitud de Aguada. Las acciones realmente propias de Aguada son las 7 de `mvc/control/aguada/`: `AgendaAction.java`, `RegistroSuministroAction.java`, `SASessionStore.java`, `SaSolicitudHistoricoAction.java`, `SeleccionDeCompaneroAction.java`, `SolicitudAguadaAction.java`, `SolicitudAguadaAuditAction.java` — todas registradas en `sostrat/WebContent/WEB-INF/struts-config.xml:605-612`.
2. **La ruta de menú `/aguada` (`struts-config.xml:657`) apunta a `org.apb.sostrat.core.mvc.control.AguadaAction`, clase que tampoco existe como fuente en este checkout.** Esto NO es una prueba adicional de ausencia de Aguada: el mismo patrón afecta a `org.apb.sostrat.core.mvc.control.MarpolAction`, `ReparacionAction`, `BunkeringAction`, `AlertaAction`, etc. (`struts-config.xml:648-662`) — es decir, todo el paquete `core.mvc.control` de acciones de menú de nivel superior está ausente del checkout de forma sistemática, incluidos módulos que sí están confirmados como reales (Marpol). Se interpreta como un módulo "core" compilado aparte, no incluido en este checkout, y no como evidencia de que Aguada (o Bunkering) no exista.

---

## 3. Alcance de migración

### Se migra (con reservas — ver gap)

| Elemento | Confirmado / Inferido |
|---|---|
| Alta, modificación, anulación y borrado de solicitud de aguada | Inferido de firmas de `CN_SolicitudAguada` |
| Consulta de solicitudes (por subpuerto+fecha, por fecha, por PK) | Inferido de firmas de `CN_SolicitudAguada` |
| Registro de suministro (incidencia + albarán) ligado a una solicitud | Inferido de `CN_RegistroSuministro` |
| Selección de solicitud por pareja de operadores | Inferido de `CN_RegistroSuministro.seleccionarSolicitud` |
| Gestión documental (justificante, albarán, firma) vía Alfresco | Inferido de `CN_SolicitudAguada` (menciones a Alfresco: `eliminacionDocumentosActualizadosEnAlfresco`) y `CN_Document` (interfaz base) |
| Vinculación a la escala/atraque del buque (`anyescala`/`numescala`/`seqatracada`) | Confirmado en `VTcSaSolicitud.java` |
| Histórico de solicitudes (`SaSolicitudHistoricoAction`, `VTcSaSolicitudHistoric`) | Confirmado — acción y vista existen |
| Auditoría de cambios de estado (`SaSolicitudAudit`, `VTcSaSolicitudAudit`) | Vista confirmada; DTO transaccional no |

### NO se migra (o queda fuera de alcance, con distinto grado de certeza)

| Elemento | Certeza | Evidencia |
|---|---|---|
| Bunkering (combustible) como parte de Aguada | ⚠️ **Reabierta, no cerrada** — ver §2.4 y §14. No hay evidencia de código de servicio/DTO, pero sí de una pantalla (`bunkering.jsp`) y una ruta Struts. No se puede afirmar "no existe" con la misma confianza que antes. | `sostrat/WebContent/jsp/bunkering/bunkering.jsp`, `lbunkering.jsp`; `struts-config.xml:656` |
| Shore Power / suministro eléctrico como parte de Aguada | **Alta — confirmado excluido.** Es un bounded context hermano (`bc-suministro-electrico-buques-v1`), mismo dominio padre, agregado y tablas propios (`SeLectura`/`V_TC_LECTURA_ELECTRICITAT`). Sin solapamiento de agregados (ver §7.2). | `bc-suministro-electrico-buques-v1.md` |
| Envío de email/SMS de replanificación automática (ESCADOS-156) | Alta — el método está comentado en el código, no activo | `CN_SolicitudAguada.java:337-341` |
| El módulo `mvc/control/suministros/` (raíz, facturación estándar por contador) | Media — parece pertenecer a un dominio de facturación de suministros distinto al de Aguada, pero no se ha analizado en profundidad su relación real (podría compartir tabla `SuministreVaixell` con Aguada vía `CN_SolicitudAguada.actualizarFacturaEstado`) | `CN_SolicitudAguada.java:415-429` referencia `SuministreVaixell` |

---

## 4. Modelo de datos

> ⚠️ **Ninguna tabla ni campo de este apartado debe usarse como contrato de escritura.** Todo lo aquí descrito procede de la vista de solo lectura `V_TC_SA_SOLICITUD` (vía `VTcSaSolicitud.java`) o de referencias de tipo en las interfaces de servicio — **no** de las clases DTO transaccionales, que no existen como fuente. Cualquier campo NO listado aquí pero referenciado en `crear`/`modificar` (por ejemplo, los campos internos de `SaRegistreSuministre`) es completamente desconocido.

### 4.1 `VTcSaSolicitud` — vista de lectura `V_TC_SA_SOLICITUD` (confirmado, campo a campo)

Fuente: `sostrat/src/org/apb/sostrat/dataaccess/views/dto/aguada/VTcSaSolicitud.java` (leído íntegramente).

| Campo | Tipo Java | Notas |
|---|---|---|
| `idsubport` | String | Subpuerto — clave de partición típica en SÒSTRAT |
| `idsolicitud` | Long | Identificador de solicitud |
| `idtipussum` | String | Tipo de suministro — dominio de valores no confirmado |
| `desctipussum` | String | Descripción del tipo de suministro (probablemente derivado de una tabla idioma) |
| `anyescala`, `numescala` | Integer | Escala/atraque asociado |
| `seqatracada` | Integer | Secuencia de atraque |
| `idvaixell`, `nomvaixell` | Integer, String | Buque |
| `idalineacio`, `codalineacio`, `nomalineacio` | Integer, String, String | Alineación/muelle |
| `datasol` | Date | Fecha de la solicitud |
| `idunitat`, `descunitats` | String, String | Unidad de medida de la cantidad solicitada |
| `observacions` | String | Observaciones libres |
| `idestatsol`, `descestatsol` | String, String | Estado de la solicitud — **dominio de valores no confirmado**, solo `descestatsol` da pista textual |
| `datsubm` | Date | Fecha de sumisión/confirmación |
| `quantitat` | Float | Cantidad solicitada |
| `usuari` | String | Usuario |
| `tipvincle`, `seqvincle` | String, Integer | Vínculo (tipo/secuencia) — semántica no confirmada |
| `seqcontacte` | Integer | Contacto asociado |
| `solicitante` | String | Solicitante |
| `idconsignatari`, `descconsignatari` | String, String | Consignatario |
| `idopealta`, `idopemodificacio` | String, String | Operador de alta/modificación (auditoría) |
| `datalta`, `datmodificacio` | Date, Date | Fechas de alta/modificación |
| `idprocalta`, `idprocmodificacio` | String, String | Proceso de alta/modificación |
| `codidioma` | String | Idioma |
| `consumtotal` | **String** ⚠️ | Consumo total — tipo `String`, no numérico; llamativo y no explicable sin el DTO fuente real |

Existen además, confirmadas como ficheros pero **no leídas campo a campo** en esta pasada (mismo patrón de vista/no-DTO):
- `VTcSaSolicitudAudit.java` (auditoría, vista de `V_TC_SA_SOLICITUD_AUDIT` presumible)
- `VTcSaSolicitudHistoric.java` (histórico)

### 4.2 Clases confirmadas ausentes como fuente (el gap central)

| Clase | Paquete esperado | Resultado de la búsqueda |
|---|---|---|
| `SaSolicitud` | `org.apb.sostrat.dataaccess.dto.aguada` | **No encontrado** en ningún `.java` del checkout |
| `SaSolicitudPk` | ídem | **No encontrado** |
| `SaSolicitudAudit` | ídem | **No encontrado** |
| `SaSolicitudAuditPk` | ídem | **No encontrado** |
| `SaSolicitudEstats` | ídem | **No encontrado** |
| `SaRegistreSuministre` | ídem | **No encontrado** |
| `SaSolicitudDao`, `SaSolicitudAuditDao`, `SaSolicitudEstatsDao`, `SaSolicitudDocDao`, `SaRegistreSuministreDao`, `ActualizacionEstadosSolAguadaDao` | `org.apb.sostrat.dataaccess.dao.aguada` | **Todo el paquete ausente** — ni una sola interfaz DAO transaccional de Aguada existe como fuente (hallazgo nuevo de esta pasada, más amplio que lo documentado previamente) |

Lo único que existe de ese universo de nombres son:
- Las **excepciones** que esas clases lanzarían (`dataaccess/exceptions/aguada/SaSolicitudDaoException.java`, `SaSolicitudAuditDaoException.java`, `SaSolicitudDocDaoException.java`, `SaSolicitudEstatsDaoException.java`, `SaRegistreSuministreDaoException.java`) — confirman que las clases existieron/existen en tiempo de compilación, pero no dan forma de campos.
- Un tasklet batch que las usa: `sostrat-BATCH/src/org/apb/sostrat/batch/tasklet/SaSolicitudTasklet.java` (no abierto en detalle en esta pasada — pendiente).
- El JAR compilado `sostrat-BATCH/lib/sostrat.jar` (18.678.412 bytes, confirmado presente en disco), que contiene las clases `.class` pero no es fuente legible/mantenible.

### 4.3 Implicación práctica

El modelo de escritura real (nombres de columna exactos de la tabla transaccional, tipos, longitudes, nullabilidad, claves foráneas, triggers, valores por defecto) **es completamente desconocido**. La vista `V_TC_SA_SOLICITUD` es un modelo de lectura denormalizado — puede omitir columnas que sí existen en la tabla base, renombrar campos, o aplicar joins que oculten la verdadera clave primaria compuesta (`SaSolicitudPk`, cuya composición exacta tampoco se conoce: se infiere `idsubport` + `idsolicitud` por el patrón de los métodos `obtener(String idsubport, Long idsolicitud)`, pero no está confirmado que esos sean literalmente los únicos campos de la PK).

---

## 5. Arquitectura técnica

**Stack actual (legacy, confirmado):**
- Java, Struts 1.x (MVC), `struts-config.xml` como enrutador
- Acceso a datos vía DAO/JDBC a medida (patrón `*Dao`/`*DaoImpl`), sin ORM estándar visible en las capas inspeccionadas
- Gestión documental delegada en Alfresco (referencias explícitas: `eliminacionDocumentosActualizadosEnAlfresco`)
- Vistas SQL (`V_TC_*`) como capa de lectura desacoplada de las tablas transaccionales

**Stack objetivo propuesto (`bc-aguada-v1.md` frontmatter, sin validar con Arquitectura APB para este BC en concreto):**
- .NET (Container Apps, patrón DOCKS estándar de APB)
- Azure SQL
- API REST vía APIM (`specs/openapi-aguada.yaml`, servidor `https://apim.portdebarcelona.cat/aguada/v1`, provisional)
- Eventos vía Azure Service Bus (`specs/asyncapi-fase2.yaml`, canal `evt.sostrat.aguada`, provisional)
- Autenticación Entra ID / OAuth2 client credentials (spec provisional, scopes `aguada.read`/`aguada.write`)

**Nota de honestidad**: la sección de arquitectura objetivo es una plantilla estándar aplicada a Aguada por el mismo proceso que a otros bounded contexts del roadmap — no es una decisión de arquitectura específica validada por el equipo de Arquitectura APB para este caso, y **no debe empezar a construirse** sin cerrar el gap de datos del §14, porque el diseño de la API/base de datos objetivo depende del modelo real que hoy se desconoce.

---

## 6. (fusionada con §5 por brevedad — ver arriba)

*(Nota: la plantilla de la serie numera "Arquitectura técnica" como sección 6; en este documento se ha fusionado con la introducción de §5 para no duplicar contenido. Ambas secciones cubren el mismo contenido técnico.)*

---

## 7. Dominio DDD

**Dominio padre**: `dom-suministros-buques-v1`

### 7.1 Bounded context `bc-aguada-v1`

| Campo | Valor |
|---|---|
| Aggregate root (nombre inferido, no confirmado campo a campo) | `SaSolicitud` |
| Entity | `SaRegistreSuministre` |
| Domain event | `SolicitudAguadaProcesada` (⚠️ nombre **no confirmado en código** — no hay ninguna ocurrencia literal de esta cadena en el checkout; es un nombre inventado por el proceso de generación de specs para representar la intención de negocio, ver §10) |
| Integration pattern | Conformist, downstream de `bc-escalas-v1` vía `EscalaPk`/`anyescala`/`numescala` |

### 7.2 Relación con `bc-suministro-electrico-buques-v1` (Shore Power) — confirmación de no solapamiento

Ambos bounded contexts comparten dominio padre (`dom-suministros-buques-v1`) pero **no comparten agregado ni tablas**:

| | Aguada (`bc-aguada-v1`) | Shore Power (`bc-suministro-electrico-buques-v1`) |
|---|---|---|
| Aggregate root | `SaSolicitud` (no confirmado campo a campo) | `SeLectura` (confirmado campo a campo, ver `bc-suministro-electrico-buques-v1.md`) |
| Tabla/vista base | `V_TC_SA_SOLICITUD` | `V_TC_LECTURA_ELECTRICITAT` |
| Paquete de servicio | `service.aguada` (`CN_SolicitudAguada`, `CN_RegistroSuministro`) | `service.suministros.electricitat` (`CN_SeElectricitat_Impl`) |
| Paquete de control | `mvc.control.aguada` | `mvc.control.suministros.electricitat` |
| Prefijo de nomenclatura | `Sa*` (Solicitud Aguada) | `Se*` (Suministro Electricitat) |

**Conclusión de la verificación**: no hay solapamiento de agregados. Ambos módulos comparten patrón arquitectónico (Struts Action → CN_* service → DAO) y ambos reutilizan los mismos Actions genéricos de liquidación/facturación (`LiquidacionAction`, `FacturasAction`, según `bc-suministro-electrico-buques-v1.md`), pero eso es acoplamiento hacia un tercer contexto (Liquidación/Facturación), no entre sí. Es razonable evaluar agruparlos operativamente en el roadmap (menos pipelines), pero deben seguir siendo **dos agregados de negocio independientes** en el diseño del nuevo servicio.

### 7.3 Relación con Bunkering

`bc-aguada-v1.md` (frontmatter y cuerpo) afirma que Bunkering (combustible) está confirmado ausente y por tanto **no forma parte** de este dominio. Esta pasada de verificación **matiza, sin poder cerrar**, esa afirmación — ver §2.4 y §14. A efectos de este documento, Bunkering **no se incluye** en el alcance de Aguada, pero se recomienda no cerrar definitivamente esa exclusión sin una decisión explícita de negocio (tarea ya reflejada en `jira-backlog.md` EPIC-06: "Confirmar con negocio si BUNKER debe añadirse... o excluirse definitivamente").

---

## 8. Pantallas UI

Fuente: `ui-screens-backlog.md`, sección "App: Aguada — mapea a `dom-suministros-buques-v1`":

> ⚠️ **Pantalla bloqueada**: sin DTO fuente confirmado, no se define el formulario de alta hasta recuperar `SaSolicitud`/`SaRegistreSuministre`. Placeholder con aviso.

No se puede diseñar el formulario de alta/edición de una solicitud de aguada (campos, validaciones, tipos de input) sin conocer el modelo transaccional real. Cualquier wireframe generado hoy sería una invención sin respaldo de evidencia — se documenta explícitamente que **no se genera** un mockup de pantalla en este dossier, en línea con la instrucción de no inventar datos no evidenciados.

**Lo único verificable indirectamente** es el listado de campos de la vista `VTcSaSolicitud` (§4.1), que podría orientar un listado/consulta de solicitudes (pantalla de solo lectura), pero no el formulario de alta/modificación, que es la pantalla realmente bloqueada.

---

## 9. APIs

Fuente: `specs/openapi-aguada.yaml` — versión `"0.1.0-provisional"`, marcada explícitamente `x-blocking-gap: "DTO fuente real ausente del checkout — ver bc-aguada-v1.md notes"`.

| Endpoint | Estado |
|---|---|
| `GET /water-supply-requests` | Documentado como modelo de **lectura** provisional, grounded en `VTcSaSolicitud` (aceptable como base de un futuro endpoint de consulta, con reservas) |
| `POST /water-supply-requests` | **No implementar.** Responde `501 Not Implemented` explícitamente en el spec (`content: application/problem+json`, `ProblemDetails`). El propio spec dice: *"NO IMPLEMENTAR — no hay evidencia del shape real de escritura (SaSolicitud no está en el checkout). Este endpoint se documenta como placeholder de la intención de negocio, no como contrato."* |

El servidor documentado (`https://apim.portdebarcelona.cat/aguada/v1`) lleva la nota `NO desplegar hasta cerrar el gap de evidencia`. Los scopes OAuth2 incluyen `aguada.write` marcado literalmente `"Escritura — NO USAR hasta cerrar el gap"`.

**Esta pasada de verificación confirma que el spec está correctamente marcado como provisional** y no encuentra motivo para relajar esas advertencias — al contrario, el hallazgo de que también falta el paquete DAO transaccional completo (§4.2) refuerza que el gap es mayor, no menor, de lo que el spec ya advertía.

---

## 10. Eventos

Fuente: `specs/asyncapi-fase2.yaml`, canal `evt.sostrat.aguada`:

> `description: "⚠️ PROVISIONAL — ver x-blocking-gap. No implementar publish/subscribe real hasta cerrar el gap de evidencia."`

El mensaje `SolicitudAguadaProcesada` está marcado:

> `x-blocking-gap: "DTO transaccional real (SaSolicitud) no existe en el checkout — este payload está grounded solo en la vista de lectura VTcSaSolicitud, NO usar como contrato definitivo de escritura."`

**Hallazgo adicional de esta verificación**: se ha buscado la cadena literal `SolicitudAguadaProcesada` en todo el checkout de `SOSTRAT-Sostrat-MJ8` y **no hay ninguna coincidencia**. Esto significa que no es solo el *payload* del evento el que es provisional (como ya advertía el spec) — el **nombre mismo del evento no está grounded en ningún publicador real de código** (no hay llamada a Service Bus, `EventGrid`, cola JMS, ni logging de negocio con ese nombre literal en el código inspeccionado). Es, en el estado actual de evidencia, un nombre de evento *propuesto* para representar la intención de negocio ("una solicitud de aguada ha sido procesada"), no un evento observado. Se recomienda añadir esta precisión al AsyncAPI si se revisa (`x-blocking-gap` podría ampliarse a "ni el nombre del evento está confirmado en código, solo la intención de negocio").

El payload (`SolicitudAguadaReadModelData`) reutiliza un subconjunto de campos de `VTcSaSolicitud` (`idsubport`, `idsolicitud`, `anyescala`, `numescala`, `quantitat`) — consistente con el resto del gap: es lectura, no escritura.

---

## 11. Diagrama topológico

```
                         ┌────────────────────────────┐
                         │      bc-escalas-v1          │
                         │  (EscalaPk / anyescala /    │
                         │      numescala)              │
                         └──────────────┬───────────────┘
                                        │ downstream (conformist)
                                        ▼
   ┌───────────────────────────────────────────────────────────────┐
   │                    dom-suministros-buques-v1                   │
   │                                                                  │
   │  ┌─────────────────────────┐      ┌───────────────────────────┐│
   │  │      bc-aguada-v1        │      │ bc-suministro-electrico-  ││
   │  │                           │      │      buques-v1 (Shore     ││
   │  │  Aggregate: SaSolicitud   │      │      Power)               ││
   │  │  (⚠️ NO confirmado)       │      │  Aggregate: SeLectura     ││
   │  │  Entity: SaRegistreSumin. │      │  (confirmado)             ││
   │  │                           │      │                           ││
   │  │  Sin solapamiento de      │◄────►│  Reutilizan los mismos    ││
   │  │  agregados (§7.2)         │      │  Actions de Liquidación/  ││
   │  │                           │      │  Facturación (no entre sí)││
   │  └─────────────┬─────────────┘      └──────────────┬────────────┘│
   │                │                                    │             │
   │  ┌─────────────▼────────────┐        ┌──────────────▼──────────┐│
   │  │  Bunkering (⚠️ estado     │        │                          ││
   │  │  reabierto, no cerrado —  │        │                          ││
   │  │  NO incluido en alcance)  │        │                          ││
   │  └───────────────────────────┘        └──────────────────────────┘│
   └───────────────────────────────────────────────────────────────┘
                  │                                    │
                  ▼                                    ▼
      ┌────────────────────┐              ┌─────────────────────────┐
      │  bc-liquidacion-v1   │              │  bc-facturacion-v1       │
      │  (downstream, ambos) │              │  (downstream, ambos)     │
      └────────────────────┘              └─────────────────────────┘

   GAP DE EVIDENCIA (bloqueante):
   ┌───────────────────────────────────────────────────────────────┐
   │  SaSolicitud / SaSolicitudPk / SaSolicitudAudit /                │
   │  SaRegistreSuministre / dataaccess.dao.aguada.*                  │
   │  → SOLO existen compiladas en sostrat-BATCH/lib/sostrat.jar      │
   │  → Única evidencia indirecta: vista V_TC_SA_SOLICITUD            │
   │     (VTcSaSolicitud.java, confirmado y leído campo a campo)      │
   └───────────────────────────────────────────────────────────────┘
```

---

## 12. Estrategia de convivencia con el modelo actual

Dado que **no existe contrato de escritura real**, la única estrategia de convivencia responsable hoy es:

1. **No tocar el flujo transaccional actual de Aguada en SÒSTRAT.** El microservicio nuevo no puede sustituir la escritura real porque no se conoce su forma. Cualquier intento de "strangler fig" sobre la escritura sería una migración a ciegas.
2. **Sí es viable** construir, en paralelo y sin impacto, un servicio de **solo lectura** (CQRS de un solo lado) que consuma la vista `V_TC_SA_SOLICITUD` vía CDC o réplica, para dar soporte a consultas/listados mientras se resuelve el gap — esto es coherente con el `GET /water-supply-requests` ya documentado como aceptable en el spec.
3. **No exponer `POST /water-supply-requests`** en ningún entorno hasta cerrar el gap — el propio spec ya lo bloquea con `501`.
4. Cuando se recupere el DTO fuente real (§14), la estrategia de convivencia debe rediseñarse desde cero con el modelo real, no parchear la propuesta actual.

---

## 13. Testing y seguridad

### 13.1 Testing

Cita textual de `testing-strategy-fase2-4.md`, sección "Aguada":

> **"No se puede definir una estrategia de testing real todavía"** — el propio contrato (`specs\openapi-aguada.yaml`) es provisional. Única prueba posible hoy: contra la vista de lectura `VTcSaSolicitud`, no contra un flujo de escritura real.

Esta pasada de verificación no encuentra motivo para matizar esta afirmación — al contrario, confirma que ni siquiera las interfaces DAO transaccionales existen como fuente, lo que hace aún menos viable diseñar tests unitarios de la capa de persistencia real hoy.

### 13.2 Seguridad

Cita textual de `threat-model-fase2-4.md`, sección "Consideración específica: Aguada":

> **"El servicio de Aguada (`specs/openapi-aguada.yaml`) está marcado como provisional — no tiene threat model real todavía, porque no se puede modelar la superficie de ataque de un contrato que no está grounded en el DTO transaccional real. Cualquier amenaza identificada aquí sería especulativa. Bloqueado por el mismo gap de evidencia que bloquea el resto de artefactos de este servicio."**

Checklist de ese mismo documento (pendiente, no marcado):

> - [ ] Threat model de Aguada re-hecho por completo una vez se recupere el DTO fuente real — el actual no es válido, es un placeholder.

---

## 14. Riesgos y gaps de evidencia (sección central)

### 14.1 El gap, resumido

| # | Elemento | Estado confirmado por esta verificación |
|---|---|---|
| 1 | `SaSolicitud`, `SaSolicitudPk`, `SaSolicitudAudit`, `SaSolicitudAuditPk`, `SaSolicitudEstats`, `SaRegistreSuministre` (DTOs transaccionales) | **No encontrados** como `.java` en ningún módulo (`sostrat`, `sostrat-BATCH`, `sostrat-CARGASINICIALES`, `sostrat-gis`, `sostratWSCXF`, `ticketgranting-api-client`, `TestAlive`, `Testing`) |
| 2 | `org.apb.sostrat.dataaccess.dao.aguada.*` (DAOs transaccionales) | **Paquete completo ausente** — hallazgo nuevo de esta pasada, no documentado con este nivel de detalle antes |
| 3 | `SaSolicitudDaoException`, `SaSolicitudAuditDaoException`, `SaSolicitudDocDaoException`, `SaSolicitudEstatsDaoException`, `SaRegistreSuministreDaoException` (excepciones) | **Confirmadas presentes** (`dataaccess/exceptions/aguada/`) |
| 4 | `VTcSaSolicitud`, `VTcSaSolicitudAudit`, `VTcSaSolicitudHistoric` + DAOs + JDBC impl (vistas de lectura) | **Confirmadas presentes y completas** (`dataaccess/views/dto\|dao\|jdbc/aguada/`) |
| 5 | `CN_SolicitudAguada`, `CN_RegistroSuministro` (interfaces de servicio) + sus `impl/` | **Confirmadas presentes** |
| 6 | `mvc/control/aguada/*` (7 Actions) | **Confirmadas presentes y registradas** en `struts-config.xml:605-612` |
| 7 | `org.apb.sostrat.core.mvc.control.AguadaAction` (acción de menú `/aguada`) | **No encontrada** — mismo patrón que otras acciones "core" de menú (Marpol, Bunkering, Reparación...), posible módulo "core" no incluido en este checkout |
| 8 | `sostrat-BATCH/lib/sostrat.jar` | **Confirmado presente** (18.678.412 bytes, `sostrat-BATCH/lib/`) — contiene las clases compiladas |
| 9 | Cadena literal `SolicitudAguadaProcesada` en el código | **No encontrada** — el nombre del evento es propuesto, no observado |

### 14.2 Por qué importa

Sin el DTO fuente real es imposible conocer con certeza: tipos de dato exactos (el caso de `consumtotal: String` en la vista ya es una señal de alerta — podría ser un `NUMBER` con formato especial, o un campo mal tipado en origen), nullabilidad, longitud de campos de texto, claves foráneas reales, triggers de base de datos, valores por defecto, y sobre todo **la composición exacta de la clave primaria** (`SaSolicitudPk`) y las reglas de validación de negocio que hoy viven exclusivamente en el bytecode compilado dentro de `sostrat.jar`.

### 14.3 Plan concreto de cierre de gap (ordenado por preferencia)

1. **Solicitar a IN2 (proveedor de SÒSTRAT) el código fuente completo del paquete `org.apb.sostrat.dataaccess.dto.aguada` y `org.apb.sostrat.dataaccess.dao.aguada`.** Es la opción preferente: recupera fuente real, comentarios, historial de negocio (los tickets `ESCADOS-*` referenciados en `CN_SolicitudAguada.java` sugieren que sí hay historial de cambios documentado en Jira/IN2 aunque el código no esté en este checkout). Responsable sugerido: equipo SÒSTRAT (Xavier Estebanell y equipo, `APB_KNOWLEDGE_BASE.md` §"SÒSTRAT") como interlocutor con IN2.
2. **Buscar en otros repositorios del ecosistema APB** (`SOSTRAT-Sostrat-JEE` mencionado en `APB_KNOWLEDGE_BASE.md` junto a `SOSTRAT-Sostrat-MJ8` — no verificado en esta pasada si contiene el mismo módulo) antes de asumir que el checkout auditado es la única copia existente.
3. **Como último recurso, decompilar `sostrat-BATCH/lib/sostrat.jar`.** Es una medida de emergencia, no una solución elegante: la decompilación pierde comentarios, nombres de variables locales y puede introducir ambigüedad en tipos genéricos. Solo debe emplearse si (1) y (2) fallan, y el resultado debe tratarse como una hipótesis a validar con negocio, no como fuente de verdad — igual que la vista de lectura hoy.
4. **En paralelo, confirmar con negocio** (no es un problema técnico) el estado de BUNKER: ¿debe añadirse como cuarto sub-recurso de Aguada, o queda definitivamente excluido? La evidencia de código (JSP + ruta Struts, sin backend) no permite decidir esto solo — requiere una conversación con el equipo funcional de SÒSTRAT.

### 14.4 Riesgo de no cerrar el gap

Si se implementa el microservicio Aguada usando únicamente `VTcSaSolicitud` como base del modelo de escritura (el atajo más tentador), el riesgo es: (a) omitir campos que existen en la tabla transaccional real pero no en la vista, (b) malinterpretar `consumtotal` u otros campos de tipo dudoso, (c) construir una clave primaria incorrecta, y (d) perder reglas de validación de negocio que hoy solo existen en la lógica Java compilada de `CN_SolicitudAguadaImpl`/`CN_RegistroSuministroImpl` — ambas confirmadas presentes como fuente, por lo que **sí se puede** extraer parte de la lógica de negocio real de esas clases `*Impl`, aunque no la forma exacta del dato persistido. Se recomienda una lectura detallada de `CN_SolicitudAguadaImpl.java` y `CN_RegistroSuministroImpl.java` como tarea complementaria de bajo riesgo mientras se gestiona el punto 1.

---

## 15. Estimación de esfuerzo

**⚠️ No fiable — no se debe usar para comprometer fechas ni story points hasta cerrar el gap del §14.**

`jira-backlog.md` (EPIC-06) ya refleja esta cautela: la historia de usuario de Aguada está marcada **BLOQUEADA** ("no se puede refinar completamente hasta recuperar el DTO fuente real") y se le asigna una estimación provisional de 5 puntos — **la misma cifra que las historias de Marinas (5 pts) y Pesca (5 pts), que sí tienen evidencia de código completa**. Esa paridad de puntos es sospechosa: una historia con gap de evidencia bloqueante estructuralmente no puede costar lo mismo que una historia ya evidenciada, porque incluye trabajo de descubrimiento no acotado. Se recomienda **no heredar esa estimación** y, en su lugar, plantear dos partidas separadas:

1. **Tarea de recuperación de evidencia** (§14.3) — esfuerzo no estimable hoy porque depende de un tercero (IN2) y de la disponibilidad de otros repositorios no auditados.
2. **Implementación del microservicio Aguada** — solo estimable *después* de cerrar (1), y probablemente comparable en orden de magnitud a Shore Power (`bc-suministro-electrico-buques-v1`, evidencia completa) una vez el modelo esté confirmado.

El resto de estimaciones de fase de `decomposition-roadmap.md` (Fase 2 = "Medio") son cualitativas y explícitamente no confirmadas por herramienta automatizada (`decomposition-roadmap.md` §1: *"No se ha tenido acceso a SonarQube\NDepend... debe confirmarse con un análisis estático automatizado antes de comprometer fechas de roadmap"*) — aplica también a Aguada.

---

## 16. Checklist de validación funcional/desarrollo

### Bloqueante (impide continuar con diseño/implementación)

- [ ] **¿Se ha recuperado el DTO fuente real (`SaSolicitud`, `SaSolicitudPk`, `SaSolicitudAudit`, `SaRegistreSuministre`) de IN2 o de otro repositorio?** — Sin esto, ninguno de los puntos siguientes puede cerrarse con garantías.
- [ ] ¿Se ha recuperado también el paquete DAO transaccional (`dataaccess.dao.aguada.*`), confirmado igualmente ausente en esta pasada?
- [ ] ¿Se ha decidido con negocio si BUNKER es parte de Aguada, un servicio propio, o queda fuera (dada la evidencia contradictoria de JSP+ruta sin backend)?

### Funcional (equipo de negocio)

- [ ] ¿El alcance funcional inferido en §2 (alta/modificación/anulación/consulta de solicitud, registro de suministro, selección de operadores, gestión documental) coincide con el proceso de negocio real?
- [ ] ¿El dominio de valores de `idestatsol` (estado de la solicitud) es el esperado? Hoy solo se conoce un valor de ejemplo (`PENDENT`) sin confirmar.
- [ ] ¿`consumtotal` representa lo que se asume (consumo de agua total)? ¿Por qué es de tipo texto en la vista de lectura?
- [ ] ¿Es correcta la separación de Shore Power como bounded context propio (§7.2), o negocio lo percibe como parte del mismo flujo operativo que Aguada?

### Desarrollo (equipo técnico)

- [ ] ¿Se ha leído `CN_SolicitudAguadaImpl.java` y `CN_RegistroSuministroImpl.java` en detalle para extraer reglas de negocio adicionales mientras se espera el DTO fuente (tarea de bajo riesgo, recomendada en §14.4)?
- [ ] ¿Se ha verificado si `SOSTRAT-Sostrat-JEE` (repositorio hermano mencionado en `APB_KNOWLEDGE_BASE.md`) contiene el paquete `dataaccess.dto.aguada` ausente en `SOSTRAT-Sostrat-MJ8`?
- [ ] ¿Se ha evaluado la decompilación de `sostrat-BATCH/lib/sostrat.jar` como medida de último recurso, con la validación de negocio correspondiente sobre el resultado?
- [ ] No desplegar `specs/openapi-aguada.yaml` en ningún entorno (ni siquiera de pruebas) mientras `POST /water-supply-requests` siga devolviendo `501` por diseño.
- [ ] No implementar el publish/subscribe real del canal `evt.sostrat.aguada` hasta confirmar tanto el payload como el nombre del evento (§10).

---

## 17. Historial de cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-07-13 | APB AI Framework (síntesis apb-disc-spec-gen-v1.0/apb-pm-product-analysis-v1.0/apb-arch-c4-model-v1.0/apb-arch-decompose-v1.0) | Generación inicial del dossier. Verificación exhaustiva propia en `SOSTRAT-Sostrat-MJ8`: confirma el gap de las DTOs transaccionales de Aguada (más amplio de lo documentado — también falta el paquete DAO transaccional completo); corrige la cifra "27 actions de Aguada sin `.electricitat`" (no confirmada — el paquete raíz `mvc/control/suministros/` pertenece a un módulo distinto); matiza la afirmación de "Bunkering confirmado ausente" (existe JSP + ruta Struts, no confirma ni descarta backend); confirma que el nombre del evento `SolicitudAguadaProcesada` no tiene ninguna ocurrencia literal en el código. Estado: **PROVISIONAL — gap de evidencia sin cerrar.** |

