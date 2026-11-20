# [IA-GEN] Auditoría de consumidores externos no documentados de SÒSTRAT

> **Borrador generado por IA** (APB AI Framework — 8 subagentes independientes siguiendo la metodología de `apb-agent-ddd-v1.0`) — pendiente validación humana. No distribuir sin revisión.
>
> **Origen (2026-07-14):** Débora cuestionó la conclusión de "sin solapamiento de dominios" de la Sesión 30 con un ejemplo concreto (CTA, aplicación existente que solo visualiza elementos de otros dominios). Verificar ese ejemplo destapó un problema mucho mayor: la verificación de solapamiento anterior solo cruzaba contra `apb-domain-catalog` y las propias secciones §7 de los dossiers — nunca se rastrearon los ~69 repos de aplicaciones reales ya clonados en `GitHub-Repos\otros\` en busca de consumidores directos de la base de datos Oracle de SÒSTRAT. Esta auditoría lo hace.

## 1. Metodología

- Rastreo de contenido (`grep -rli "sostrat"`) sobre los ~69 repos de `GitHub-Repos\otros\` (excluidos los dos checkouts del propio monolito), filtrado manualmente para descartar falsos positivos (constantes de idioma `IdiomaCatalanSostrat = "CT"`, comentarios genéricos, IDs de referencia sin acceso directo a BBDD).
- De ~42 repos con alguna mención textual, se identificaron **9 con dependencia real y directa** (conexión Oracle/Entity Framework directa a la BBDD de SÒSTRAT, o integración SOAP/REST activa) — verificados uno a uno por 8 subagentes independientes (uno cubrió 2 repos del mismo ecosistema).
- Cada subagente: (a) leyó el código fuente real (Program.cs, DbContext, Repositories, Controllers), (b) confirmó lectura vs. escritura citando fichero:línea, (c) buscó el repo/dossier de la serie SÒSTRAT al que correspondería, (d) donde fue posible, revisó `git log` para verificar actividad reciente.

## 2. Resumen ejecutivo

**9 aplicaciones .NET reales, ya construidas y en su mayoría activamente desplegadas (Jenkins CI a TST), tienen una dependencia directa y no documentada sobre datos de SÒSTRAT que los 24 dossiers de la serie DDD están a punto de extraer/transformar.** Ninguna de las 24 dossiers menciona a ninguna de estas 9 aplicaciones. 3 de las 9 tienen **escritura directa** confirmada (no solo lectura) sobre tablas Oracle de SÒSTRAT — el riesgo más alto, porque una extracción sin coordinar rompería esas escrituras de forma silenciosa.

| # | Repo(s) | Qué es | Lectura/Escritura | Dossier(s) afectado(s) | Riesgo |
|---|---|---|---|---|---|
| 1 | `APB.API.CPR` (Precintos) | Gestión de precintos aduaneros de contenedores (app móvil GoCleaver) durante inspección PIF | **Lectura + escritura** sobre `INSPECCIO`/`INSPECCIO_AUDIT` (vía EF Core) + SOAP a Portic (`ConsultaCodecosPrecinto`) | **dossier-19-inspeccion-scpp.md** (no dossier-11 PIF: `INSPECCIO` es de SCPP) | 🔴 Alto |
| 2 | `APB.API.IPB` (Pesaje/báscula) | Pesaje MARPOL de camiones/contenedores | **Escritura** directa (INSERT/UPDATE) sobre 15+ tablas: `PESATGE`, `CAMIO`, `CONTENIDOR`, `CAMIO_HIST_TARA`, `CONTENIDOR_HIST_TARA`, `PESATGE_INSPECCIO`, `SERVEI_PESATGE`, `CODI_QR` | **dossier-09-transporte-terrestre.md** (tablas `CAMIO`/`CONTENIDOR`) — candidato a sub-dominio propio "Pesaje/MARPOL" | 🔴 Alto |
| 3 | `APB.API.CTS` + `APB.APP.CTA` ("Gestión de Contenedores") | Dashboard de clientes portuarios (importadores/exportadores) — el ejemplo original de Débora | **Solo lectura** (confirmado, 0 escrituras), pero toca ~50 tablas/vistas: `MANIFEST*`, `CONEIXEMENT*`, `PARTIDA*` (Manifiestos); `DTA_*`, `V_TC_TRASLLAT` (Aduanas); `V_TC_MMPP_NOTIF` (MMPP); `V_TC_ESCALAS` (Buques/Escalas); tablas de Ferrocarril y Transporte Terrestre | **dossier-12-manifiestos.md** + **dossier-13-aduanas-contenedores.md** (principales) | 🔴 Alto (activo — commit de mayo 2026 sobre tablas `DTA_*`) |
| 4 | `APB.API.AUT` | Autorizaciones de acceso físico por puertas (tótems) | **Lectura + escritura en tiempo real** sobre `AUTORITZACIO`/`HIST_AUTORITZACIO`/`AUTORITZACIO_ESTAT_RESUM`, en cada paso físico por una puerta | **dossier-05-pps.md** | 🔴 Crítico (bloqueante del patrón Strangler Fig) |
| 5 | `APB.API.REB` + `apb.p51` | Gestión de recibos (REB) + expedientes/PDF (P51) | REB: lectura `REBUT`/tarifas + **escritura** `REBUT_TRAM_NOTES`. P51: **crea recibos en SÒSTRAT** vía SOAP (`altaReciboAsync`) + genera PDF | **dossier-15-facturacion-liquidaciones.md** | 🔴 Alto (P51 es el más invasivo: escritura activa) |
| 6 | `APB.API.LRT` (+ `APB.API.LRG` como cliente indirecto) | Líneas Regulares — Barcos/Escalas | LRT: lectura `VAIXELL` + **escritura** en `ESCALA` (`UpdateEscalaNomLinea`/`UpdateEscalasLinea`). LRG no toca SÒSTRAT directo, solo llama a la API de LRT | **dossier-17-buques.md** + **dossier-00-escalas-migracion-argos.md** (riesgo de doble escritor con ARGOS) | 🔴 Alto |
| 7 | `APB.API.OPS` ("Gestión de Suministro de Electricidad") | Réplica de solo lectura vía Data Warehouse de sesiones de suministro eléctrico | **Solo lectura**, vista `OPS_V_B_SESSIONS_SOSTRAT` sobre `DSS_DWH` (réplica batch, no tiempo real) | **dossier-21-suministro-electrico-buques.md** | 🟡 Medio (no es duplicación de build, pero requiere decisión de a quién alimenta el nuevo servicio) |
| 8 | `APB.API.CRE` + `APB.APP.CRE` + `APB.API.VXL` + `APB.API.SLC` ("Cruceros") | Sistema .NET activo de reservas de atraque para cruceros (sustituye gestión manual por Excel) | Mixto — VXL/SLC leen `VAIXELL`/`ARMADOR`/`USUARI` vía `DbSostratContext`; CRE/APP.CRE gestionan `CreSolicitud`/`CreVaixell` (modelo propio, no legacy) | **`bc-cruceros-v1`** (dossier de aplicación final **todavía no escrito** — ver §3) | 🔴 Alto (desarrollo activo, ~3 meses, con alcance mayor al único agregado hoy documentado en la propuesta) |

## 3. Hallazgo más importante: `bc-cruceros-v1` no tiene dossier de aplicación final, y ya existe una implementación .NET activa

`proposals/bc-cruceros-v1.md` solo documenta el agregado `CreuerEscalaAudit` (fuente: `CreuerEscalaAudit.java` + SOAP `CrucerosWSPort`), y declara explícitamente que la gestión de atraque/reserva de crucero **no** es su alcance ("eso pertenece a Escalas"). Pero el ecosistema `APB.API.CRE`/`APB.APP.CRE`/`APB.API.VXL`/`APB.API.SLC` **ya es, en producción activa desde hace ~3 meses, precisamente esa funcionalidad de reserva de atraque para cruceros** — con su propio modelo de datos (`CreSolicitud`, `CreVaixell`, `CreTerminalBloqueado`, `CreLineaOperativaSolicitud`), su propia API y su propio frontend MVC.

Esto significa que **el dominio `dom-cruceros-v1` ya tiene una implementación .NET real en marcha, más amplia que lo que cualquier dossier de la serie SÒSTRAT documenta**. No hay conflicto de datos con `dossier-18` (Servicios Auxiliares — buses/vigilancia, sub-capacidad distinta), pero sí hay un vacío de gobernanza: nadie ha escrito el dossier de aplicación final de `bc-cruceros-v1` teniendo en cuenta que gran parte de lo que debería documentar **ya existe construido**, no es un candidato a extracción futura.

## 4. Por qué esto no se detectó antes (causa raíz)

El proceso de descubrimiento DDD de esta serie (`apb-agent-ddd-v1.0` + subagentes) analizó exclusivamente: (a) el código fuente de `SOSTRAT-Sostrat-MJ8`, (b) el catálogo `apb-domain-catalog`, y (c) documentación/backlog aportados por Débora. **Nunca se incluyó como fuente de entrada el propio catálogo de ~69 repos de aplicaciones ya clonadas en `GitHub-Repos\otros\`**, pese a que varias de ellas leen/escriben directamente la misma base de datos Oracle que SÒSTRAT. La instrucción del agente (`agents/apb-agent-ddd-v1.0.md`) no incluye ningún paso que busque específicamente consumidores externos de la BBDD de origen — es una carencia real del propio framework, no solo de esta ejecución (ver `PLAN_FASES_FUTURAS.md` para la mejora propuesta al agente).

## 5. Recomendación general

**Antes de dar por buena la serie de 24 dossiers para desarrollo**, cada uno de los 9 casos de la tabla §2 debe:
1. Confirmarse con el equipo propietario de la aplicación externa (no solo con evidencia de código — puede haber contexto de negocio no visible aquí).
2. Decidir la estrategia de convivencia: ¿la app externa migra a la nueva API DOCKS?, ¿se mantiene un puente/vista de compatibilidad durante la transición?, ¿se retira si queda redundante (caso OPS)?
3. Añadirse explícitamente al backlog de la extracción correspondiente (`jira-backlog.md`) como tarea de coordinación, no solo como nota de riesgo.

Ningún caso de los 9 bloquea *documentar* la extracción — pero **todos bloquean *ejecutar* la extracción sin coordinación previa**, especialmente los 3 casos de escritura directa (IPB, AUT, REB/P51) y el caso de doble escritor (LRT sobre `ESCALA`).

## 6. Historial

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-14 | APB AI Framework (8 subagentes + síntesis) | Creación — origen: pregunta de Débora sobre CTA |
