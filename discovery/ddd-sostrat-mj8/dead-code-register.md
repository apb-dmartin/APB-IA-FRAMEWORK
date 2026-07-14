# [IA-GEN] Registro de código muerto / no usado — SÒSTRAT

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.
>
> Generado 2026-07-13 en respuesta a la pregunta: *"¿hemos verificado código existente que en realidad no se utiliza y no sería necesario migrar?"* — ver [`coverage-audit.md`](coverage-audit.md) para el contexto completo: este registro es la mitad "código muerto" de esa auditoría; la otra mitad (paquetes nunca analizados) se trata aparte porque **no es lo mismo** — código muerto se excluye de la migración, un paquete no analizado sigue necesitando análisis, no exclusión.
>
> **Corregido 2026-07-14** (continuación de Sesión 30, tras la re-verificación campo a campo de los 24 dossiers de aplicación final): 3 hallazgos reclasificados como falsos positivos (ver §Correcciones aplicadas), 6 hallazgos nuevos incorporados desde los dossiers 12/13/21 (5 de confianza ALTA + 1 de confianza MEDIA). Numeración original preservada — no se ha renumerado ningún ítem para no romper las referencias cruzadas por número desde otros dossiers (`#2`, `#3`, `#6`, `#7`, `#14`, `#19`).

## Cómo leer este registro

- **Confianza ALTA**: el propio desarrollador dejó una declaración textual inequívoca ("NO SE USA", "obsoleto") o el fichero está objetivamente desconectado del arranque de la aplicación (no cargado por `web.xml`/`spring-batch.xml`). Se puede excluir de la migración citando esta evidencia.
- **Confianza MEDIA**: hay una señal fuerte pero no una declaración explícita — requiere una confirmación puntual con el equipo de SÒSTRAT antes de excluirlo definitivamente de la migración.
- Ningún hallazgo de este registro se ha usado para "explicar" el gap de cobertura detectado en `coverage-audit.md` — el volumen de código muerto confirmado (tras la corrección de 2026-07-14: **24 hallazgos numerados de confianza ALTA** — de los 27 originales/nuevos, 3 reclasificados como falsos positivos — más 2 filas adicionales sin numerar que agrupan 6 ficheros de rutas/tiles comentadas, y **10 de confianza MEDIA**; recuento verificado línea a línea sobre las tablas de este documento, no estimado) sigue siendo marginal frente a las >1250 unidades funcionales reales del inventario.

---

## Confianza ALTA — excluible de la migración con esta evidencia

### Métodos/bloques de código comentados con justificación explícita

| # | Fichero | Línea | Cita | Veredicto |
|---|---|---|---|---|
| 1 | `sostrat/src/org/apb/sostrat/service/impl/CN_TitolOcupacio_Impl.java` | 1725 | *"este metodo no se llamaba en ninguna parte y la sql esta mal formada"* — método `obtenerRenovacionVigente` sobrecargado (26 líneas) comentado | No migrar |
| 2 | `sostrat/src/org/apb/sostrat/service/escalas/impl/CN_Escala_Impl.java` | 10321-10371 | *"ESCA-1328: (...) Este bloque de código está obsoleto"* (~50 líneas) | No migrar |
| 3 | `sostrat/src/org/apb/sostrat/service/escalas/impl/CN_Escala_Impl.java` | 10389-10420+ | *"ESCA-1654: (...) ANULAMOS EL COMPORTAMIENTO DE LA ESCA-480"* | No migrar |
| 4 | `sostrat/src/org/apb/sostrat/service/escalas/impl/CN_EscalaValidaciones_Impl.java` | 1030 | *"NO SE USA."* — método `validar278` completo (~30 líneas) comentado | No migrar |
| 5 | `sostrat/src/org/apb/sostrat/service/escalas/impl/CN_EscalaValidaciones_Impl.java` | 2788 | *"NO SE USA"* — método `validar307` completo (~30 líneas) comentado | No migrar |
| 6 | `sostrat/src/org/apb/sostrat/service/marpol/wasdis/edi/dto/Dgs01DTO.java` | 53 | *"Este metodo ya no se usa (...) pero se mantiene por si se modificara en el futuro"* | No migrar (revisar si "por si acaso" sigue vigente con negocio) |
| 7 | `sostrat/src/org/apb/sostrat/service/mmpp/maestros/impl/CN_CargaIMDGExcel_Impl.java` | 350 | *"ya no se usa debido a la MMPP-390"* | No migrar |
| 8 | `sostrat/src/org/apb/sostrat/service/factestandar/rebuts/impl/CN_Rebut_Impl.java` | 1659 | *"El tipo de recibo cepos parece obsoleto. No se utiliza con la nueva funcionalidad"* | No migrar (verbo "parece" — confirmar con negocio antes de excluir el tipo de recibo del modelo) |
| 9 | `sostrat/src/org/apb/sostrat/service/liquidadormm/impl/CN_LiquidadorMM_Pasajeros_Impl.java` | 245 | *"NO USAR"* — método `preliquidarEquipo` con cuerpo vacío | ~~No migrar~~ — **❌ FALSO POSITIVO, corregido 2026-07-14** (ver §Correcciones aplicadas #1) |
| 10 | `sostrat/src/org/apb/sostrat/service/liquidadormm/reglas/impl/LiquidadorMM_Reglas_L2.java` | 823 | *"NO SE USA PARA LA L2"* — dentro de `calcularQUOTA(...)` | ~~No migrar~~ — **❌ FALSO POSITIVO, corregido 2026-07-14** (ver §Correcciones aplicadas #1) |
| 11 | `sostrat/src/org/apb/sostrat/service/liquidadormm/reglas/impl/LiquidadorMM_Reglas_L2.java` | 828 | *"NO SE USA PARA LA L2"* — dentro de `calcularIMPANTESBONIF(ManifestEquipamentDTO)`, método completo comentado en bloque `/* */` | No migrar — **confirmado genuino** (método realmente comentado, no invocable) |
| 12 | `sostrat/src/org/apb/sostrat/service/liquidadormm/reglas/impl/LiquidadorMM_Reglas_L2.java` | 833 | *"NO SE USA PARA LA L2"* — dentro de `calcularIMPANTESBONIF(BigDecimal, BigDecimal)`, sobrecarga comentada línea a línea con `//` | No migrar — **confirmado genuino** (método realmente comentado, no invocable) |
| 13 | `sostrat/src/org/apb/sostrat/service/liquidadormm/reglas/impl/LiquidadorMM_Reglas_L2.java` | 838 | *"NO SE USA PARA LA L2"* — dentro de `calcularNUM9(...)` | ~~No migrar~~ — **❌ FALSO POSITIVO, corregido 2026-07-14** (ver §Correcciones aplicadas #1) |
| 14 | `sostrat/src/org/apb/sostrat/service/mmpp/hazmat/impl/CN_MMPP_Hazmat_Impl.java` | 701 | *"NO SE USA"* — llamada comentada a `CommonUtil.creaContactoSinCTA(...)` | No migrar |

### Rutas Struts / definiciones de tiles comentadas (código no activo, no requiere confirmación adicional — ya inertes)

| # | Fichero | Línea | Path/definición | 
|---|---|---|---|
| 15 | `sostrat/WebContent/WEB-INF/struts-config.xml` | 318 | `/vaixellsCertificadoAltresAudit` (comentada) |
| 16 | `sostrat/WebContent/WEB-INF/struts-config.xml` | 816 | `/pda/residusLineaCamio` (comentada) |
| 17 | `sostrat/WebContent/WEB-INF/struts-config.xml` | 1160 | `/peticioFBDDoc_popup` (comentada) |
| 18 | `sostrat/WebContent/WEB-INF/struts-config.xml` | 1402-1403 | `/residusLineaCamio` + `/residusLineaCamio_popup` (comentadas) |
| — | `sostrat/WebContent/WEB-INF/tiles/tiles-defs.xml` | 6227-6233, 10778-10784, 2966, 4558 | `lListaResiduosWASDISDades`, `lEvidenciaspopup`, `presentaciongraficatabla`, `generarjustificantepopup` (comentadas) |
| — | `sostrat/WebContent/WEB-INF/tiles/tiles-errores.xml` | 37, 44 | `errorpopupEspecial`, `errorIralistado` (comentadas) |

### Fichero de configuración completo huérfano

| # | Fichero | Evidencia | Veredicto |
|---|---|---|---|
| 19 | `sostrat/WebContent/WEB-INF/struts/struts-config-terminales.xml` | Contiene 1 `<action path="/errorsTerminals">` (`TConErrorsTerminalsAction`). **No aparece en el parámetro `config` del servlet `action` en `web.xml`** (líneas 141-150) — nunca se carga en producción. | No migrar — código inerte, confirmado objetivamente (no depende de interpretar un comentario) |

### Batch — imports de job desactivados

| # | Fichero | Línea | Job afectado | Veredicto |
|---|---|---|---|---|
| 20 | `sostrat-BATCH/src/spring-batch.xml` | 70 | `<!-- <import resource="sostrat-batch-EnvioPortCDM.xml"/-->` | No migrar (job completo definido pero desconectado) |
| 21 | `sostrat-BATCH/src/spring-batch.xml` | 90 | `<!-- <import resource="sostrat-batch-GarantiasLotus.xml"/> -->` | No migrar (job completo definido pero desconectado) |

### Directorio de test marcado para eliminar

| # | Ruta | Evidencia | Veredicto |
|---|---|---|---|
| 22 | `sostrat/test/resources/archivos_antiguos_eliminar/` | Nombre del directorio + 13 ficheros Spring de test duplicados/obsoletos (~650 KB) junto al único fichero activo (`applicationContext-datasourcetest.xml`, en el directorio padre) | No migrar |

### Nuevos hallazgos incorporados en la verificación de dossiers de aplicación final (2026-07-14)

Detectados durante la re-verificación campo a campo de los dossiers 12 (Manifiestos), 13 (Aduanas/Contenedores) y 21 (Suministro Eléctrico a Buques) — ver `app-dossiers/INDEX.md §4`. Verificados de nuevo contra el checkout real al aplicar esta corrección.

| # | Fichero | Línea | Cita/Evidencia | Veredicto |
|---|---|---|---|---|
| 23 | `sostrat/src/org/apb/sostrat/service/manifiestos/edi/manifiestos/impl/CN_EDI_Helper_Procesar_Manifiestos_Impl.java` | 996-1030 | Método `decisionMensajeEnviarCUSREP()`, `private` y `@Deprecated`. Su único punto de invocación está comentado (línea 425: `//MERC-72 if(decisionMensajeEnviarCUSREP(lIfcsumDTO)) return enviarCUSREP(lIfcsumDTO);`) — al ser `private`, no puede tener otros llamadores fuera de la clase | No migrar (Dossier 12 §4.1) |
| 24 | `sostrat/src/org/apb/sostrat/service/manifiestos/edi/manifiestos/impl/ProcesarMensaje_Impl.java` | 368-370 | Código tras `return pTramoMess;` explícito (línea 366): 3 líneas comentadas (`pTramoBD.setConocimientos(...)`, `pTramoBD.setManifestDTO(...)`, `return pTramoBD;`), objetivamente inalcanzable | No migrar (Dossier 12 §4.2) — trivial, sin impacto funcional |
| 25 | `sostrat/src/org/apb/sostrat/service/suministres/electricitat/impl/CN_SeElectricitat_Impl.java` | 529-536 | Método `getConsumosUltimos7Dias(String, String)` completo comentado con `//`; su lógica fue sustituida por `obtenerConsumosElecDeWS` | No migrar (Dossier 21 §4) |
| 26 | `sostrat/src/org/apb/sostrat/mvc/control/aduanas/{CErrorEquipoAction,CErrorNivelEquipoAction,CErrorNivelTramoAction}.java` | — | Las 3 clases existen y compilan, pero ninguna tiene `<action path>` en `struts-config-aduanas.xml` ni en `struts-config.xml` principal (grep exhaustivo sin resultado) — huérfanas, objetivamente desconectadas del routing | No migrar (Dossier 13 §14) |
| 27 | `sostrat/WebContent/WEB-INF/spring-config/applicationContext-beans.xml` | 1129-1132 | 4 `<property>` comentadas (`cnProfercont`, `cnProtercont`, `cnCodeco`, `cnDatosMovimientoContenedor`) — wiring Spring desconectado, consistente con que sus Actions asociadas (#26) tampoco tienen ruta activa | No migrar (Dossier 13 §14) |

---

## Confianza MEDIA — requieren confirmación con el equipo SÒSTRAT antes de excluir

| # | Ítem | Evidencia | Por qué no es ALTA |
|---|---|---|---|
| 1 | `/vaixellLloydsEmergente` → `VaixellLloydsEmergenteAction` | Action activa en `struts-config.xml:322`, la clase `.java` no existe en el checkout | Podría existir solo compilada fuera de esta copia (como pasa con Aguada) — no es prueba de que no se use |
| 2 | `/incidenciaEQInspeccio` → `IncidenciaEQInspeccioAction` | Action activa en `struts-config.xml:803`, clase no encontrada | Igual que arriba |
| 3 | `/posicionamentlloc` → `PosicionamentLlocAction` | Action activa en `struts-config.xml:804`, clase no encontrada | Igual que arriba |
| 4 | `sostrat-batch-CargaIncremental.xml` (tasklet `LanzarCargaIncrementalTasklet`, cron `0 59 23 ? * MON-FRI`) | Job completo definido, sin `import` en `spring-batch.xml` ni en ninguna de las 12 plantillas de entorno | Podría importarse en un fichero de entorno de producción no incluido en esta copia |
| 5 | `sostrat-batch-intercanviNivellInspeccioAduana.xml` | Job completo, mismo patrón que #4 | Igual que arriba |
| 6 | `sostrat-batch-XXX.xml` (nombre literal "XXX", usa tasklet `LanzarCircuitoNotificacionMPTasklet`) | Mismo tasklet ya usado por `sostrat-batch-MMPPNotificacionEDI.xml` (éste sí activo) — indicio de duplicado/borrador abandonado | Nombre de fichero sugiere borrador, pero no hay declaración explícita |
| 7 | Módulos Jira documentados sin ninguna referencia de ticket en código: `MEDI, TERC, EST, TREDI, PESCA, CTA, OTS, BUNKER, MILL, INTDBPRO, ESCAIIB` | 0 ocurrencias de `PROYECTO-NNNN` en los 4 módulos | La ausencia de convención de ticket no prueba ausencia de código — MEDI y PESCA, por ejemplo, sí tienen código real identificado bajo otros nombres (ver `discovery-summary.md`) |
| 8 | `sostratWSCXF/.../manifiestogrimaldi/ManifiestoGrimaldiImpl` (variante NO segura) | Clase presente en el código pero no registrada en `cxf-servlet.xml` — solo la variante `ManifiestoGrimaldiSecureImpl` está publicada | Consistente con "reemplazada por la versión segura", no confirmado con el equipo |
| 9 | ~90 paths de Struts sin referencia literal `.do` en ningún JSP/JS | Construcción dinámica de URL vía librería de tags `tcBotones` hace que la ausencia de referencia literal sea muy probablemente un falso positivo | **No se listan individualmente** — el agente que hizo esta búsqueda concluyó que la mayoría son falsos positivos; no se usan como evidencia de código muerto en este registro |
| 10 | `sostrat/src/org/apb/sostrat/service/suministres/electricitat/impl/CN_SeElectricitat_Impl.java:337` — método `obtenerConsumosElecFake(String)` | Sin llamador activo confirmado (único uso está dentro del bloque comentado de #25, línea 532) | Sin declaración textual explícita tipo "NO SE USA" — señal objetiva de ausencia de llamador, pero no una confirmación inequívoca del desarrollador (Dossier 21 §4) |

---

## Correcciones aplicadas (2026-07-14, continuación de Sesión 30)

> Verificación directa contra el checkout real (`GitHub-Repos/otros/SOSTRAT-Sostrat-MJ8/`), no solo contra el resumen de `dossier-15-facturacion-liquidaciones.md §4/§12` — cada línea citada abajo se ha releído carácter a carácter en esta corrección.

### 1. Los 3 falsos positivos de Facturación/Liquidaciones (items #9, #10, #13)

Los tres son overrides activos (no comentados) del patrón Strategy que implementa `ILiquidadorMM_Reglas_Comunes` para el nivel tarifario L2 — el comentario `NO SE USA PARA LA L2`/`NO USAR` documenta una decisión de negocio (esta operación no aplica a ese nivel/tipo de tráfico), no código inalcanzable:

- **`CN_LiquidadorMM_Pasajeros_Impl.java:245-248`** (item #9): método `preliquidarEquipo(...)` con cuerpo real `//EN PASAJEROS NO SE PRELIQUIDAN LOS EQUIPOS` — es una especialización deliberada por tipo de tráfico (mercancía vs. pasajeros), invocada polimórficamente por el orquestador `CN_LiquidadorMM_Gen_*Etapa_Impl`.
- **`LiquidadorMM_Reglas_L2.java:822-825`** (item #10): método `calcularQUOTA(...)` — cuerpo activo `return null;`, comentario interno documenta el no-op, no está comentado como código.
- **`LiquidadorMM_Reglas_L2.java:837-840`** (item #13): método `calcularNUM9(...)` — mismo patrón, cuerpo activo `return null;`.

Contraste verificado en el mismo fichero: los items **#11** (líneas 827-830, `calcularIMPANTESBONIF(ManifestEquipamentDTO)`) y **#12** (líneas 832-835, `calcularIMPANTESBONIF(BigDecimal, BigDecimal)`) sí están genuinamente comentados (bloque `/* */` y línea a línea `//` respectivamente) — se mantienen como código muerto confirmado, sin cambios.

**Acción tomada**: items #9, #10, #13 marcados `~~No migrar~~ ❌ FALSO POSITIVO` en sus filas de tabla (no eliminados de la numeración, para no romper referencias cruzadas de otros documentos a números de este registro). No deben excluirse de la migración a DOCKS — su lógica (no-op condicionado por nivel tarifario) forma parte del contrato de la interfaz `ILiquidadorMM_Reglas_Comunes` y debe preservarse en el diseño del motor de reglas destino.

---

## Lo que este registro NO cubre (evitar sobre-interpretar la exclusión)

- Los 279 `<action path>` del paquete raíz `org.apb.sostrat.mvc.control` (Vaixell, TARIC, EDI, Usuari/Operador, Inspeccio) y los módulos satélite (`efficiencyNetwork`, `serviciosAuxiliares`, `carpetaclientes`) **no están aquí** — no son código muerto, son código **nunca analizado**. Se investigan por separado en `coverage-audit.md` §Fase B, y varios de ellos probablemente sí necesitan migrarse.
- El menú de SÒSTRAT se genera dinámicamente desde una tabla de BBDD (`MenuDelegate.java` → `ServiceLocatorCore.getMenuService()`), no desde un fichero estático. Esta copia local no incluye esa tabla, por lo que **ninguna acción activa se ha marcado como huérfana solo por no aparecer en el menú** — solo se listan aquí las que están objetivamente desconectadas del arranque (comentadas o no cargadas por `web.xml`/`spring-batch.xml`).
