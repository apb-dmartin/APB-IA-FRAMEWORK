# [IA-GEN] Registro de código muerto / no usado — SÒSTRAT

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.
>
> Generado 2026-07-13 en respuesta a la pregunta: *"¿hemos verificado código existente que en realidad no se utiliza y no sería necesario migrar?"* — ver [`coverage-audit.md`](coverage-audit.md) para el contexto completo: este registro es la mitad "código muerto" de esa auditoría; la otra mitad (paquetes nunca analizados) se trata aparte porque **no es lo mismo** — código muerto se excluye de la migración, un paquete no analizado sigue necesitando análisis, no exclusión.

## Cómo leer este registro

- **Confianza ALTA**: el propio desarrollador dejó una declaración textual inequívoca ("NO SE USA", "obsoleto") o el fichero está objetivamente desconectado del arranque de la aplicación (no cargado por `web.xml`/`spring-batch.xml`). Se puede excluir de la migración citando esta evidencia.
- **Confianza MEDIA**: hay una señal fuerte pero no una declaración explícita — requiere una confirmación puntual con el equipo de SÒSTRAT antes de excluirlo definitivamente de la migración.
- Ningún hallazgo de este registro se ha usado para "explicar" el gap de cobertura detectado en `coverage-audit.md` — el volumen de código muerto confirmado (19 hallazgos) es marginal frente a las >1250 unidades funcionales reales del inventario.

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
| 9 | `sostrat/src/org/apb/sostrat/service/liquidadormm/impl/CN_LiquidadorMM_Pasajeros_Impl.java` | 245 | *"NO USAR"* — método `preliquidarEquipo` con cuerpo vacío | No migrar |
| 10-13 | `sostrat/src/org/apb/sostrat/service/liquidadormm/reglas/impl/LiquidadorMM_Reglas_L2.java` | 823, 828, 833, 838 | *"NO SE USA PARA LA L2"* (x4) | No migrar |
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

---

## Lo que este registro NO cubre (evitar sobre-interpretar la exclusión)

- Los 279 `<action path>` del paquete raíz `org.apb.sostrat.mvc.control` (Vaixell, TARIC, EDI, Usuari/Operador, Inspeccio) y los módulos satélite (`efficiencyNetwork`, `serviciosAuxiliares`, `carpetaclientes`) **no están aquí** — no son código muerto, son código **nunca analizado**. Se investigan por separado en `coverage-audit.md` §Fase B, y varios de ellos probablemente sí necesitan migrarse.
- El menú de SÒSTRAT se genera dinámicamente desde una tabla de BBDD (`MenuDelegate.java` → `ServiceLocatorCore.getMenuService()`), no desde un fichero estático. Esta copia local no incluye esa tabla, por lo que **ninguna acción activa se ha marcado como huérfana solo por no aparecer en el menú** — solo se listan aquí las que están objetivamente desconectadas del arranque (comentadas o no cargadas por `web.xml`/`spring-batch.xml`).
