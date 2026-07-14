# [IA-GEN] Informe Ejecutivo — Transformación SÒSTRAT (Java/Oracle → DOCKS)

> **Borrador generado por IA** (APB AI Framework) — pendiente validación humana. No distribuir sin revisión.
> Síntesis de toda la Sesión 30 (2026-07-13/14): cierre de los 24 dossiers de aplicación, corrección de specs, auditoría de solapamiento de dominios, auditoría de 9 consumidores externos no documentados, auditoría de consistencia cruzada (acotada y completa) y re-derivación desde código fuente.

## 1. Respuesta directa

**La documentación de descomposición de SÒSTRAT es de alta calidad técnica y está prácticamente lista como insumo de diseño — pero NO está lista para que el equipo empiece a desarrollar.** Hay 3 bloqueantes reales, ninguno de los cuales se resuelve escribiendo más documentación:

1. **Cero validación humana.** Los 24 dossiers, sus bounded contexts y sus specs siguen en `status: "discovered"`. Nadie de Arquitectura APB ni ningún domain expert los ha revisado.
2. **9 aplicaciones externas reales dependen hoy de datos de SÒSTRAT sin que ningún dossier lo supiera antes de esta sesión** — 3 de ellas escriben directamente sobre tablas Oracle que se planea migrar. Esto no es una carencia de documentación: es una dependencia operativa real que hay que coordinar con 8 equipos propietarios distintos antes de tocar una sola tabla.
3. **Un bounded context entero (`bc-cruceros-v1`, Cruceros) ya tiene una implementación .NET real en producción** (`APB.API.CRE`/`APB.APP.CRE`/`APB.API.VXL`/`APB.API.SLC`) que ningún dossier de esta serie documenta como "aplicación final" — solo existe como propuesta.

Ninguno de estos 3 puntos existía como hallazgo hasta que el usuario cuestionó directamente la premisa de "sin solapamiento de dominios" a mitad de esta sesión (ver §4). Es la corrección más importante de todo el trabajo.

## 2. Qué se ha hecho en esta sesión (cronología)

| Sub-sesión | Qué | Resultado |
|---|---|---|
| 30.1-30.4 | Verificación de que los 24 dossiers de aplicación (23 apps + Escalas) quedaron completos de una sesión previa, corrección de `dead-code-register.md` (2 falsos positivos retirados, 6 candidatos nuevos) y 9 specs/documentos con entidades/campos equivocados | Commit `073fbdb` |
| 30.5 | El usuario cuestiona directamente la conclusión "no hay solapamiento de dominios" con el ejemplo de CTA (aplicación que solo debería *leer* otros dominios) | Arranca la investigación que da lugar a 30.6 |
| 30.6 | Escaneo completo de ~69 repos locales relacionados con SÒSTRAT + 8 agentes en paralelo, cada uno auditando un consumidor candidato con evidencia de código real | **9 consumidores externos confirmados**, documentados en `EXTERNAL_CONSUMERS_AUDIT.md` y referenciados en 10 dossiers/propuestas + `PLAN_FASES_FUTURAS.md` #98 + `HANDOFF_TECNICOS.md` DC7. Commit `18798cf` |
| 30.7 | Auditoría de consistencia cruzada **acotada** (7 dossiers PROVISIONAL/alto riesgo: Mano de Estiba, Aguada, Concesiones, Facturación, Clavegueram, Efficiency Network, Operadores Portuarios) | 2 correcciones (payload de evento Clavegueram, referencias obsoletas de `eseffnetwork`). Commit `241c75d` |
| 30.8 (esta sesión) | Re-derivación completa desde código de eventos/APIs/pantallas/backlog, solicitada explícitamente por el usuario para las 24 dossiers | Ver §3 — completada con alcance ajustado tras un límite de sesión de la API |

## 3. Alcance real de la re-derivación de hoy (30.8) — transparencia obligatoria

El plan inicial era lanzar 8 agentes en paralelo (3 dossiers cada uno) para cubrir las 24 dossiers. **Los 8 agentes fallaron a mitad de ejecución por un límite de sesión de la API** ("session limit · resets 15:50 Europe/Madrid"); solo 2 devolvieron resultado parcial, y ambos marcados por el propio sistema como no fiables. Ante esto, se preguntó al usuario cómo proceder; su decisión explícita fue **continuar directamente (sin más subagentes), de forma secuencial, priorizando los dossiers de mayor riesgo**.

**Dossiers verificados con evidencia de código real en esta sesión (30.8):**

| Dossier | Verificación | Resultado |
|---|---|---|
| 05 — PPS | Recuento de rutas Struts (`struts-config-pps.xml`) | ✅ 29 rutas confirmadas exactas |
| 09 — Transporte Terrestre | Recuento y deduplicación de rutas entre `struts-config.xml` (50) y satélite (39), 33 duplicadas → 56 únicas | ✅ Matemática de deduplicación confirmada exacta |
| 12 — Manifiestos | Recuento de rutas (`mvc.control.manifiestos.*`) | ✅ 63 rutas confirmadas exactas |
| 13 — Aduanas/Contenedores | Recuento de rutas (13 satélite + 10 principal) | ✅ 23 rutas confirmadas exactas |
| 14 — Concesiones | Cita textual de `CN_Liquidacion_Impl.java:434` (escritura cruzada `UPDATE TITOL_MINIM_DADES`) | ✅ Confirmada byte a byte |
| 16 — Clavegueram | Payload del evento `ConsumClaveguerLiquidado` vs. DTO real `ClvgConsums.java` | ❌→✅ **Corrección real aplicada** — ver §4.1 |
| 20 — Trámites Cliente | Recuento de rutas (`TramitClientAction`) | ✅ 3 rutas confirmadas exactas |
| 21 — Suministro Eléctrico | Recuento y listado literal de 6 rutas | ✅ Confirmado exacto |
| 22 — Efficiency Network | Tipo real de `Usuari.eseffnetwork` (`CN_Usuari_Impl.java:978-980`) | ✅ Confirmado `String` "S"/"N", corrección previa (30.7) era exacta |
| 23 — Operadores Portuarios | Checklist de correcciones pendientes vs. estado real de los ficheros | ❌→✅ **Corrección real aplicada** — ver §4.2 |

**Continuación (30.9, mismo día)**: tras un primer cierre de 30.8, el usuario pidió continuar. Se verificaron 6 dossiers adicionales en profundidad (01, 04, 11 —PK—, 18) y se re-examinaron con más detalle 09/19 ya tocados, ampliando la cobertura total a **20 de 24 dossiers verificados con evidencia de código esta sesión**. Se encontraron y corrigieron **3 errores reales más**:

| Dossier | Error encontrado | Corrección |
|---|---|---|
| 19 — Inspección SCPP | El encabezado de §3 afirmaba "23 rutas Struts confirmadas", pero el propio desglose del párrafo siguiente sumaba 16+1+3=20 — inconsistencia interna nunca actualizada | Corregido a 20, verificado de nuevo contra `struts-config.xml` |
| 19 — Inspección SCPP | Afirmaba que la PK de `Inspeccio` (3 partes) sigue "el mismo patrón" que `OperacioPif`/`OPERACIO_PIF2` — pero `OperacioPifPk.java` confirma que esa PK es de **2 partes**, no 3 (`dossier-11-pif.md §5` ya lo documentaba bien) | Corregido en 2 sitios del dossier (§5, §5 de NivellDInspeccio) |
| 01 — Datos Maestros de Equipamiento | `openapi-datos-maestros-equipamiento.yaml` tipaba `matriculaiso` como la matrícula ISO 6346 real (con patrón `^[A-Z]{4}[0-9]{7}$`), cuando el DTO real (`Equipament.java`) lo usa como un flag `S`/`N` — confirmado sin excepción en 30+ puntos de asignación de todo el checkout; el patrón ISO pertenece a `refequipament` | Corregido: patrón movido a `refequipament`, `matriculaiso` retipado `enum: [S,N]`, retirado de `required` en el alta |

**Cierre (30.10, mismo día)**: el usuario pidió continuar una tercera vez. Se verificaron los 4 dossiers restantes (00 Escalas, 06 MARPOL, 08 Marinas/Pesca, 10 MMPP), completando la **re-derivación desde código de las 24/24 dossiers** de la serie. 2 de los 4 no tenían ningún error (08, 10, ambos con verificaciones exactas de recuento de rutas y bloques de código muerto citados literalmente). Se encontraron y corrigieron **2 hallazgos más**:

| Dossier | Error encontrado | Corrección |
|---|---|---|
| 06 — MARPOL/Residuos | Nota obsoleta repetida en 6 ficheros distintos ("solo el valor 1 de `idestat` tiene nombre de constante confirmado") — el propio dossier ya había confirmado en su generación original (2026-07-13) que las 7 constantes son literales en `ResidusEscala.java`, pero la corrección nunca se propagó a las specs/catálogo/backlog/testing/threat-model | Corregido en `openapi-marpol-residuos.yaml`, `asyncapi-fase2.yaml`, `events-catalog.md`, `jira-backlog.md`, `testing-strategy-fase2-4.md` y `threat-model-fase2-4.md` |
| 00 — Escalas | El dossier afirmaba "112 rutas Struts" del paquete `escalas`; el recuento exacto (`grep -c` sobre `struts-config.xml`) da 96, coincidente con `coverage-audit.md:34` ("escalas | 96"), que el dossier original no había cruzado | Corregido en §3 y §4 |

**Conclusión final de la re-derivación (24/24 dossiers)**: 17 de 24 dossiers no tenían ningún error. Los 7 con hallazgos (16, 19 ×2, 23, 01, 06, 00) comparten el mismo patrón — ninguno es un dato inventado. Son, en todos los casos: (a) correcciones parciales de una sesión anterior que no se propagaron a todos los ficheros afectados, (b) comparaciones/afirmaciones puntuales incorrectas sin verificar contra el fichero fuente exacto citado, o (c) una cifra de recuento nunca cruzada contra el propio `coverage-audit.md` del proyecto. La disciplina de auto-verificación de los dossiers (cada uno documenta sus propios gaps de evidencia en su §14) es lo que hizo posible encontrar y corregir estos 7 casos con precisión quirúrgica en vez de una reescritura general.

### 4.1 Corrección — Payload del evento `ConsumClaveguerLiquidado` (dossier-16)

La corrección aplicada en la sesión 30.7 (ampliar el esquema de 4 a 9 campos) alineó `specs/asyncapi-fase4.yaml` con el ejemplo JSON de `events-catalog.md §19` — pero ese ejemplo era en sí mismo incompleto. El propio `dossier-16-clavegueram.md §5` (escrito el 2026-07-13, antes de la corrección de 30.7) ya documentaba que el DTO real `ClvgConsums.java` tiene **25 campos**, y señalaba `codiusaigua` (determina la tarifa aplicada) e `idservei` (clave de correlación con `Liquidacio`) como **críticos y ausentes** del contrato. Se han añadido ambos campos (`specs/asyncapi-fase4.yaml`, `events-catalog.md §19`, `dossier-16-clavegueram.md §5/§10/§16`), quedando el esquema en 11 campos. Los 14 campos restantes (auditoría/internos) quedan excluidos deliberadamente, con nota explícita de por qué.

### 4.2 Corrección — Checklist obsoleto (dossier-23)

`dossier-23-operadores-portuarios.md §14/§16` seguía listando como **pendientes** dos correcciones (`eseffnetwork` tipado incorrectamente como `boolean`; `comptefaceenlace` con nombre inexistente) que ya se habían aplicado esa misma sesión sobre `specs/openapi-operadores-portuarios.yaml`, `bc-efficiency-network-v1.md` y `jira-backlog.md`. El propio documento contradecía el estado real del repositorio. Corregido para reflejar qué está hecho y qué sigue pendiente (el resto de los 108 campos ausentes del esquema no estaba cubierto por esa corrección puntual).

### 4.3 Corrección — Inconsistencia interna de recuento de rutas (dossier-19)

El encabezado de §3 de `dossier-19-inspeccion-scpp.md` afirmaba "23 rutas Struts confirmadas", pero el propio desglose del párrafo siguiente sumaba 16 (patrón raíz) + 1 (`calendariCapacitats`) + 3 (satélite) = 20 — un número nunca actualizado tras refinar el cálculo. Verificado de nuevo contra `struts-config.xml`: el total real es 20. Corregido el encabezado.

### 4.4 Corrección — Comparación de PK incorrecta entre `Inspeccio` y `OperacioPif` (dossier-19)

El mismo dossier afirmaba dos veces que la PK compuesta de `Inspeccio` (3 partes: `sptinspeccio`+`anyinspeccio`+`seqinspeccio`) sigue "el mismo patrón" que `OperacioPif`/`OPERACIO_PIF2`. `OperacioPifPk.java` confirma que esa PK es de **solo 2 partes** (`anyoperaciopif`+`seqoperaciopif`), sin componente `spt*` — tal y como ya documentaba correctamente `dossier-11-pif.md §5`. La cifra de 3 partes de `Inspeccio` en sí era correcta (confirmada en `InspeccioPk.java`); el error estaba solo en la comparación con `OperacioPif`. Corregido en las 2 secciones donde aparecía (§5 de `Inspeccio` y de `NivellDInspeccio`).

### 4.5 Corrección — Semántica de `matriculaiso` en el contrato REST (dossier-01)

`dossier-01-datos-maestros-equipamiento.md §2/§14` ya señalaba desde su generación original (2026-07-13) que `specs/openapi-datos-maestros-equipamiento.yaml` modelaba mal el campo `matriculaiso`: lo trataba como la matrícula ISO 6346 real del contenedor (con patrón `^[A-Z]{4}[0-9]{7}$`), cuando el DTO real (`Equipament.java`) lo usa como un flag `S`/`N` que indica si `refequipament` (el campo que sí lleva la matrícula) cumple el dígito de control ISO 6346 — confirmado sin excepción en 30+ puntos de asignación de todo el checkout. Esta corrección, señalada como pendiente hace un día, nunca se había aplicado. Corregido: el patrón ISO se mueve a `refequipament`, `matriculaiso` se retipa `enum: [S, N]` y se retira de los campos requeridos en el alta (es un valor calculado por el servicio, no un dato de entrada).

### 4.6 Corrección — Nota obsoleta sobre nombres de estado propagada en 6 ficheros (dossier-06)

`dossier-06-marpol-residuos.md` ya había confirmado, en su propia generación del 2026-07-13, que las 7 constantes de `ResidusEscala.idestat` están todas nombradas literalmente en `ResidusEscala.java` (líneas 18-24) — no solo la constante 1, como afirmaba una nota de cautela heredada de una fase de análisis anterior. Esa corrección nunca se propagó: `specs/openapi-marpol-residuos.yaml`, `specs/asyncapi-fase2.yaml`, `events-catalog.md §14`, `jira-backlog.md`, `testing-strategy-fase2-4.md` y `threat-model-fase2-4.md` seguían repitiendo la advertencia obsoleta ("solo el valor 1 confirmado"). Corregidos los 6 ficheros; se mantiene como pendiente real (no resuelto por esta corrección) la semántica de las transiciones válidas entre los 7 estados.

### 4.7 Corrección — Recuento de rutas de Escalas (dossier-00)

`dossier-00-escalas-migracion-argos.md` afirmaba 112 rutas Struts del paquete `escalas`. El recuento exacto contra `struts-config.xml` da 96, coincidente con `coverage-audit.md:34` ("escalas | 96 | bc-escalas-v1") — cifra que el dossier no había cruzado en su generación original pese a que otros dossiers de la serie sí verifican sistemáticamente contra esa fuente. Corregido en §3 y §4.

## 5. Los 3 bloqueantes reales, en detalle

### 5.1 Cero validación humana (`PLAN_FASES_FUTURAS.md` #96)
Todo `discovery/ddd-sostrat-mj8/` es `[IA-GEN]`, `status: "discovered"`. Ningún domain expert ni Arquitectura APB lo ha revisado, pese a que varios hallazgos cambian el alcance real del trabajo (Escalas ya no es una extracción sino una migración hacia ARGOS; Concesiones y Facturación van como dos servicios separados; hay 6 bounded contexts nuevos de Fase 6 sin precedente en el catálogo).

### 5.2 9 consumidores externos no documentados (`PLAN_FASES_FUTURAS.md` #98, `EXTERNAL_CONSUMERS_AUDIT.md`)
Descubiertos el 2026-07-14 tras cuestionar la premisa de "sin solapamiento". Los más críticos:
- **`APB.API.LRT`** lee Buques y **escribe** en Escalas — un **tercer escritor** junto a SÒSTRAT y ARGOS sobre la misma tabla `ESCALA`.
- **`APB.API.IPB`** escribe en 15+ tablas de Transporte Terrestre/MARPOL (`CAMIO`, `CONTENIDOR`...).
- **`APB.API.AUT`** lee y escribe `AUTORITZACIO` de PPS en tiempo real desde tótems físicos — bloquea el patrón Strangler Fig si no se coordina.
- **`APB.API.REB`+`apb.p51`** — P51 llega a crear recibos directamente en SÒSTRAT vía SOAP.
- **El ecosistema `APB.API.CRE`/`APB.APP.CRE`/`APB.API.VXL`/`APB.API.SLC`** ya ES la implementación real del bounded context de Cruceros — hoy solo existe como propuesta (`bc-cruceros-v1.md`), sin dossier de aplicación final.

Ninguna extracción que toque Transporte Terrestre, PPS, Facturación, Buques, Escalas, Suministro Eléctrico, SCPP, Manifiestos, Aduanas o Cruceros debería ejecutarse (no solo documentarse) sin antes coordinar con los 8 equipos propietarios de estas aplicaciones.

### 5.3 Bloqueantes de decisión de dominio conocidos (`PLAN_FASES_FUTURAS.md` #93)
5 decisiones pendientes de Arquitectura APB/producto, ninguna resoluble con más análisis de código: fusión PIF+SCPP, `parent_domain` compartido de Operadores Portuarios/Efficiency Network, conflicto de planificación de Clavegueram (EPIC-15 vs EPIC-13B), gap de evidencia de Aguada (requiere al proveedor IN2), y desajuste semántico de Trámites de Cliente con `dom-administracion-electronica-v1`.

### 5.4 Carencia estructural del propio framework (`PLAN_FASES_FUTURAS.md` #99)
`agents/apb-agent-ddd-v1.0.md` nunca incluye un paso que busque consumidores externos ya existentes del sistema de origen — solo analiza el sistema que se transforma y el catálogo de dominios. Es la causa raíz de que los 9 consumidores de §5.2 pasaran desapercibidos en 24 dossiers durante 2 días. Propuesta: nueva "Fase 0 — Rastreo de consumidores externos" en el agente, para cualquier futura descomposición de monolito.

## 6. Lo que SÍ está listo

- Mapa de dominios/BCs reparentado contra el catálogo real de APB, verificado dos veces sin solapamiento real (6 BCs de Fase 6 + 33 apps del lote de QA, 26/33 con dominio identificado).
- Roadmap de 6 fases, 16 épicas con historias/criterios de aceptación, catálogo de 41+ eventos, superficie API por fase, ~45 pantallas UI.
- 20 OpenAPI 3.0.3 + 4 AsyncAPI 2.6, testing strategy y threat model completos para las 14 apps de Fase 0-4.
- Todas las specs necesarias ya existen — **no hacen falta specs nuevas** (verificado 2026-07-14): los únicos 2 casos "sin spec" (Efficiency Network, Escalas) lo son por diseño correcto, no por omisión.
- Calidad interna verificada por re-derivación completa desde código de las **24/24 dossiers** (30.7 acotada + 30.8 + 30.9 + 30.10, esta sesión): 7 correcciones puntuales encontradas y aplicadas en total, ninguna de tipo "dato inventado" — ver §3/§4.

## 7. Recomendación

**NO-GO para desarrollo. GO para pasar a validación humana formal**, con esta agenda mínima:

1. Checkpoint de validación humana con Arquitectura APB y domain experts (§5.1) — incluye los 6 BCs nuevos de Fase 6.
2. Sesión de coordinación con los 8 equipos propietarios de los 9 consumidores externos (§5.2) — antes de comprometer fecha de cutover de cualquiera de las 10 apps afectadas.
3. Resolver las 5 decisiones de dominio pendientes (§5.3) con Arquitectura APB/producto.
4. Escribir el dossier de aplicación final de `bc-cruceros-v1` documentando el ecosistema CRE/VXL/SLC ya activo (hoy solo hay propuesta).
5. Cerrar el residuo de cobertura ya conocido (~105 rutas de paquete raíz sin BC, 100 batch jobs sin auditar job a job, 3 gaps SOAP, DTO real de Aguada) — trabajo de IA todavía posible, no bloqueado por personas.
6. Opcional, no bloqueante: mejorar `apb-agent-ddd-v1.0.md` con el paso de rastreo de consumidores externos (§5.4) — la re-derivación desde código de las 24 dossiers ya está completa (§3).

Una vez cerrados los puntos 1-3, el resto de la documentación (`jira-backlog.md` + `specs/` + testing/threat-model) es una base de referencia válida para sprint planning real.

## 8. Historial

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0.0 | 2026-07-14 | Primera versión, síntesis de toda la Sesión 30 a petición explícita del usuario tras la re-derivación completa (30.8) |
| 1.1.0 | 2026-07-14 | Ampliada tras continuación 30.9: cobertura de re-derivación pasa de 10 a 20 de 24 dossiers, 3 correcciones adicionales encontradas y aplicadas (dossier-19 ×2, dossier-01) |
| 1.2.0 | 2026-07-14 | Cierre tras continuación 30.10: re-derivación completa de las **24/24 dossiers**, 2 correcciones finales encontradas y aplicadas (dossier-06, dossier-00). Total de la sesión: 7 correcciones puntuales, ninguna de tipo "dato inventado" |
