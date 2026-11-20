---
id: "std-test-plan-v1.0"
name: "Estándar Corporativo de Planes de Pruebas"
version: "1.7.1"
status: "draft"
owner: "QA Gobierno APB <qa-gobierno@portdebarcelona.cat>"
policy_ref: "STANDARD_QA (context/apb/standards/STANDARD_QA.md)"
created_date: "2026-07-02"
review_date: "2027-07-02"
---

# Estándar Corporativo de Planes de Pruebas

## Propósito

Eleva el plan de pruebas de "artefacto que genera una skill" a **proceso gobernado**: con plantilla
fija, metodología de fuentes, trazabilidad de **procedencia** por prueba, histórico, aprobados,
enlace bidireccional con evidencias y Jira, y verificación de no-regresión de rendimiento.

Aplica a todo plan de pruebas de aplicaciones APB generado o asistido por IA. La skill de referencia
es [`apb-qa-test-plan-v1.0`](../../../skills/apb-owned/qa/apb-qa-test-plan-v1.0.md); la plantilla es
[`TEST_PLAN.md`](../templates/TEST_PLAN.md); el ejemplo canónico aplicado es
[`QA_TRU_TruckCenter_UNIFICADO.md`](../../../docs/qa/examples/QA_TRU_TruckCenter_UNIFICADO.md).

`STANDARD_QA.md` sigue siendo el resumen ejecutivo de calidad; este documento desarrolla en concreto
la disciplina de **planes de pruebas**.

---

## 1. Orden de fuentes (con degradación)

El plan se construye combinando fuentes en este **orden de prioridad funcional** (lo funcional manda;
el código verifica y completa):

1. **Planes de pruebas aportados por el usuario** — en cualquier formato (Markdown, Word, Excel, PDF…).
   Se normalizan a Markdown con [`apb-plat-doc-to-markdown-v1.0`](../../../skills/apb-owned/platform/apb-plat-doc-to-markdown-v1.0.md)
   antes de fundirse. Se conservan **todas** sus pruebas.
2. **Especificación SDD (`spec`)** — cuando el plan se genera dentro de un flujo Spec-Driven Development
   ([`apb-wf-sdd-full-v1.0`](../../../workflows/apb-wf-sdd-full-v1.0.md)), la spec previamente definida
   ([`apb-disc-spec-gen-v1.0`](../../../skills/apb-owned/discovery/apb-disc-spec-gen-v1.0.md)) es **input
   obligatorio** y **fuente funcional autoritativa**: los casos derivan de los **criterios de aceptación**
   de la spec, y cada caso queda trazado a su criterio de origen. La spec manda sobre la ingeniería inversa
   del código cuando ambos discrepan (la discrepancia se registra como observación, ver §1.1).
3. **Rovo (Atlassian)** — tickets de Jira, sus adjuntos, análisis funcional y documentación aportada.
4. **GitHub Copilot** — ingeniería inversa del código, para **completar y contrastar** lo funcional.

### 1.1 Degradación cuando faltan fuentes

Jira o el Análisis Funcional **pueden faltar o estar obsoletos**. En ese caso:

- El plan **no se bloquea**: se apoya en las fuentes disponibles (típicamente el código vía Copilot) y
  **marca cada prueba con su procedencia y confianza real**.
- **Nunca se inventa** respaldo funcional inexistente: si una prueba solo tiene respaldo de código, su
  procedencia dice, en texto legible, "Código fuente verificado (...)" y **no** cita Jira ni Análisis
  Funcional que no existan.
- Si el AF está obsoleto respecto al código, se registra la **discrepancia** como observación de la prueba
  y se marca para revisión funcional humana.

---

## 2. Modelo de procedencia (múltiple y obligatorio)

Toda prueba lleva **≥1 origen** y **≥1 herramienta**. La procedencia es una **lista**, no un valor único.

| Dimensión | Valores canónicos |
|---|---|
| **Herramienta** (quién la propuso) | `rovo` · `github-copilot` · `usuario` · (otras: nombre libre) |
| **Origen** (de dónde sale) | `spec` (SDD, con id de la spec/criterio) · `jira` (con ticket) · `documentacion` (AF) · `codigo` · `usuario` (con formato de origen) |

**Notación de la columna «Procedencia»: texto legible, sin siglas.** Un lector no técnico (QA Lead,
Analista Funcional, Débora) debe poder leer la columna sin necesitar la leyenda. Formato: frase corta que
nombra la herramienta real, el origen y la referencia concreta (ticket, fichero, línea). Ejemplos:

- `Jira a través de Rovo (ticket TRANSTE-1513)` — el conector Rovo consultó el ticket en vivo.
- `Jira aportado por Débora (ticket AOM-2530)` — el ticket se cita dentro de un documento/export de Jira
  que el usuario aportó directamente (sin conector Rovo activo en la sesión).
- `Documentación funcional aportada por Débora` — sin ticket concreto, solo el documento narrativo.
- `Código fuente verificado (repo APB.API.TES, PortCallController.cs:38)` — inspección directa del código
  clonado, citando repo + fichero + línea.
- `Usuario (plan de pruebas aportado directamente)` — cuando la prueba viene de un plan ya redactado por
  el usuario, no de tickets ni de código.

**Prohibido inventar procedencia** (p. ej. escribir "código" cuando no se ha accedido a ningún repositorio) —
sigue aplicando la regla de degradación de §1.1. Combinar procedencias con ` · ` cuando una prueba tiene
más de un respaldo, p. ej.: `Jira aportado por Débora (ticket TRANSTE-1513) · Código fuente verificado (repo
APB.TRU, TruckController.cs:112)`.

Además, cada caso registra:
- **«Desde»** — fecha en que la prueba quedó definida en el plan (permite ver qué se añadió en cada revisión).
- **«OK func.»** — funcional que **aprobó** la prueba (rol/nombre); vacío hasta la validación.

---

## 3. Unificación sin duplicados (con conservación íntegra)

Cuando concurren varias visiones del mismo plan (p. ej. una por Jira, otra enriquecida con AF, otra por
código):

1. Se funde **por intención de la prueba**, no por número de caso (numeraciones distintas pueden colisionar).
2. Se conservan **todas** las pruebas; los solapamientos se unifican en un caso con **procedencia múltiple**.
3. Se asigna un **ID canónico estable** y se publica una **tabla de mapeo** desde las numeraciones de origen,
   para no perder trazabilidad.

### 3.1 Principio de conservación (regla de primer nivel — NO NEGOCIABLE)

> **Unificar ≠ resumir. Unificar NUNCA elimina información.** Fundir = combinar sin duplicar
> **conservándolo todo**: no solo las pruebas, sino **todo el contenido narrativo** de cada fuente.

El documento unificado es un **superconjunto** de sus fuentes. Debe conservar, además de la matriz de casos,
**cada bloque de contenido** presente en cualquiera de ellas, entre otros:

- **Funcionalidad detallada** (API, pantallas, campos, lupas, desplegables, terminales).
- **Modelo de datos** completo (tablas, columnas, tipos, nulabilidad, claves).
- **Máquina de estados y reglas de negocio.**
- **Eventos de auditoría, mensajes y errores funcionales.**
- **Incidencias históricas relevantes.**
- **Proyectos futuros.**
- **Tickets analizados y documentos de referencia.**
- **Checklist ejecutable y plantilla de ejecución**, si alguna fuente los aporta.

Reglas operativas:
- Si un contenido parece **redundante** entre fuentes → se **funde o se referencia**, **nunca se descarta**.
- Ante la duda → **conservar**.
- Antes de dar por bueno un unificado, se hace una **pasada de verificación sección a sección contra cada
  fuente**, confirmando que todo su contenido está representado. Si algo falta, se reincorpora y se anota en
  el histórico (§6).
- La pérdida silenciosa de contenido al unificar es un **defecto bloqueante** del plan (equivale a
  incumplir §5).

### 3.2 Identificador canónico y crecimiento

> **Problema que resuelve:** con una numeración plana (`TRU-T01…T112`), añadir una prueba nueva a un
> bloque ya existente obliga a insertarla en medio (renumerando las siguientes) o a colgarla al final
> (perdiendo su agrupación visual con el bloque). Ambas opciones rompen la correlación estable entre el
> plan y sus informes de ejecución ya emitidos.

**Esquema de ID:** `{APP}-B{NN}-T{NN}` — p. ej. `TRU-B06-T09`.

- **`{APP}`** — código corto de la aplicación (2-5 letras), estable, definido una vez.
- **`B{NN}`** — número de **bloque funcional**, 2 dígitos. **Append-only**: un bloque nuevo siempre recibe
  el siguiente número disponible; un bloque **nunca** se inserta en medio de los existentes ni se
  renumera, aunque su nombre o alcance evolucione.
- **`T{NN}`** — secuencia de la prueba **dentro de su bloque**, 2 dígitos, asignada en el **orden en que se
  definió**. También **append-only**: una prueba nueva en el bloque 6 (que ya tiene `T01…T08`) se numera
  `T09`; ninguna prueba existente de ningún bloque cambia de ID.

**Reglas:**
- Los IDs **nunca se reutilizan ni se renumeran**, ni siquiera cuando una prueba se marca `Obsoleta` (el
  hueco se conserva; no se compacta la secuencia).
- Esto garantiza que el ID de una prueba en el plan **coincide siempre** con su ID en cualquier informe de
  ejecución, presente o futuro, sin importar cuántas pruebas se añadan después.
- **Migración desde numeración plana:** si un plan existente usa IDs planos (`APP-Txx`), se migran una
  sola vez a `APP-Bxx-Txx` conservando el **ID legado** en una columna «Legado» de la matriz, para no
  romper la trazabilidad con informes ya emitidos que referencian el ID antiguo.
- Un bloque **nuevo** (no presente en ninguna fuente previa) recibe el siguiente número de bloque libre;
  nunca se reutiliza el hueco de un bloque eliminado.

---

## 4. Detección de plan previo y actualización incremental

Antes de generar, se comprueba si **ya existe** un plan de pruebas de la aplicación:

- Si existe → **actualización incremental desde su fecha** (no regeneración desde cero): se añaden pruebas
  nuevas, se marcan las obsoletas y se registra el cambio en el histórico (§6).
- Cada prueba conserva su **«Desde»** original; las nuevas llevan la fecha de la revisión actual.

---

## 5. Secciones obligatorias del documento

Todo plan de pruebas incluye, además de la matriz de casos:

**Secciones fijas de contexto** (imprescindibles para la trazabilidad funcional):
1. Descripción general.
2. APIs y endpoints (PRE/PRO).
3. **Arquitectura topológica** (diagrama de componentes/flujo).
4. **Modelo de datos / relación de tablas**.
5. Máquina de estados / reglas de negocio clave.
6. Integraciones (WS, SSO, sistemas externos).
7. Referencia a la **Spec** / Análisis Funcional de origen.

**Secciones de gobernanza:**
8. **Histórico de cambios del plan.**
9. **Aprobados del plan por cambio** (quién aprobó qué versión/cambio).
10. **Enlace bidireccional plan ↔ evidencias** (del plan a las evidencias de resultados y viceversa).
11. **Evidencias vinculadas a Jira.**
12. Criterios de entrada / salida.
13. **Matriz de roles de usuario y usuario de ejecución** (§9.2).
14. **Acta de aprobación del informe de resultados** (§6.2) — en el informe de ejecución, no en el plan base.
15. **Casos NO ejecutados / bloqueados** (obligatoria en el informe de ejecución) — listado explícito por
    **ID canónico** (no solo un recuento agregado por bloque) de los casos que no se ejecutaron en la
    corrida, con el motivo (fuera de alcance de la herramienta, requiere rol/usuario adicional, bloqueado
    por hardware/entorno, pendiente de siguiente sesión…). Un informe que solo reporta lo ejecutado y omite
    lo pendiente no es válido — el lector debe poder ver la cobertura real sin tener que restar contra el
    plan.

---

## 6. Gobernanza y gestión del cambio

- **Versionado:** cada cambio significativo genera una entrada en el histórico (§5.8) y una fila en
  «Aprobados por cambio» (§5.9), coherente con [`GOVERNANCE.md`](../../../GOVERNANCE.md) §3 (ciclo de vida).
- **Responsables:** el plan tiene un `owner` y, para pasar de `draft` a `candidate`/`approved`, un
  validador humano nombrado (QA Lead / Analista Funcional). El agente **nunca** aprueba su propio plan
  (regla `SYSTEM.md` §2.1 / `PROMPTING_STANDARD` §2).
- **Contexto contractual:** si el plan es documento de licitación (LCSP), se archiva en el expediente
  correspondiente además del repositorio (ver `apb-qa-test-plan` §9).

### 6.1 Gobernanza por aplicación

El plan de pruebas de una aplicación no es un artefacto puntual: vive mientras vive la aplicación y
necesita un responsable a lo largo del tiempo, no solo en su versión inicial.

- **Owner nombrado por aplicación:** cada plan tiene un responsable de mantenerlo — QA Lead o Analista
  Funcional, según la fila «QA / Calidad» de la matriz de responsabilidades de
  [`GOVERNANCE.md §2.1`](../../../GOVERNANCE.md). No se crea un rol de gobierno nuevo: se reutiliza el
  existente.
- **Cadencia de revisión:** el plan se revisa en cada **release** de la aplicación (no solo cuando cambia
  Jira/AF/código) — se comprueba si hay pruebas que añadir, marcar obsoletas o cuya procedencia haya
  quedado desactualizada.
- **Ciclo de vida:** el plan sigue el mismo ciclo `draft` → `candidate` → `approved` de
  [`GOVERNANCE.md §3`](../../../GOVERNANCE.md), con las mismas reglas de aprobación de §2.2 (dos ojos,
  el agente nunca aprueba su propio plan).
- **Cambio de owner:** si el owner cambia (rotación de equipo), se registra como entrada en el histórico
  (§6) del plan, igual que cualquier otro cambio significativo.

### 6.2 Aprobación del informe de resultados (autorización persistida)

> El **plan** se aprueba con la gobernanza de §6/§6.1. El **informe de ejecución** (los resultados de una
> corrida concreta) requiere además una **autorización explícita de las personas responsables**, que quede
> **reflejada y persistida** — no basta con generarlo.

- **Acta de aprobación** — todo informe de ejecución incluye una sección **«Acta de aprobación»** con los
  aprobadores nombrados. Como mínimo:

  | Rol | Nombre | Fecha | Decisión | Comentarios |
  |---|---|---|---|---|
  | **Analista Funcional** | | | `Aprobado` / `Rechazado` / `Con reservas` | |
  | **Desarrollador** | | | `Aprobado` / `Rechazado` / `Con reservas` | |
  | QA Lead (si aplica) | | | | |

- **Qué se aprueba:** el **informe de resultados**, no el Pull Request. La aprobación del código (PR) y la
  del informe son actos distintos; esta sección gobierna la del informe.
- **Persistencia (doble registro, obligatorio):**
  1. En el **`.md`** del informe (fuente de verdad, versionada en el repo de la app) — el acta rellena
     queda en el propio documento y su cambio entra en el histórico.
  2. En el **ticket Jira** vinculado — la decisión se refleja como comentario y/o transición de estado vía
     [`prov-atlassian-v1.0`](../../../providers/prov-atlassian-v1.0.md), enlazando al informe.
- **Mecanismo:** un *sign-off* controlado y auditable (nombre + rol + fecha + decisión). **No exige firma
  criptográfica**; si en el futuro se requiere firma digital certificada, se añade sin cambiar este acta.
- **Regla de dos ojos:** el agente **nunca** autoaprueba su propio informe (coherente con `SYSTEM.md §2.1`
  y `POLICY_AI_USAGE §6-7`). La decisión es siempre de una persona nombrada.
- **Estado del informe:** `pendiente-aprobación` → `aprobado` / `rechazado` / `aprobado-con-reservas`. Un
  informe `rechazado` o `con reservas` dispara, si procede, el bucle de corrección de §6.3.

### 6.3 Bucle de corrección tras fallo (fallo → PR → Jira)

Cuando una o más pruebas **fallan** (o el informe se aprueba «con reservas»), el proceso no termina en el
informe: se **propone la corrección** y se deja traza en Jira.

- Lo orquesta el sub-workflow [`apb-sub-qa-fix-loop-v1.0`](../../../subagents/apb-sub-qa-fix-loop-v1.0.md):
  **test FALLA → propone un PR con las correcciones** (vía `apb-dev-pr-doc-v1.0`) **→ anota el ticket Jira**
  correspondiente (vía `prov-atlassian-v1.0`) con el enlace al PR y la evidencia del fallo.
- **Autonomía:** el bucle **propone** el PR; **nunca lo mergea**. La aprobación y el merge son humanos
  (`POLICY_AI_USAGE §6-7`). En flujo SDD, la corrección se contrasta contra la **spec** (§1) origen del caso.

---

## 7. Almacenamiento y entrega de resultados y evidencias

- **El plan y sus resultados de ejecución se guardan en el repo de cada aplicación**, no en el repo del
  framework. El framework guarda **estándar + plantilla + ejemplo canónico**.
- Las **evidencias** (capturas, trazas, vídeo, informe) se vinculan bidireccionalmente al plan y se
  **enlazan a Jira**. El destino de las evidencias es **seleccionable en ejecución**:
  - **Paquete descargable** (ZIP con informe HTML), y/o
  - **Subida a Jira** como adjuntos vinculados al ticket (vía `adapter-rovo-v1.0` / API Jira).

### 7.1 Entrega dual Markdown + HTML (obligatoria)

Tanto el **plan** como el **informe de ejecución** se generan siempre en **dos formatos**:

- **`.md`** — fuente de verdad, versionable en git/repo de la app, diffable entre revisiones.
- **`.html`** — autocontenido, para lectura por stakeholders no técnicos. Requisitos de formato:
  - **Cabecera** con fondo **azul corporativo** (`--azul-corporativo #046DB2`, mismo patrón que
    `design-system/guidelines/brand-cabecera.card.html`) y el **logo de APB** (`logo-horizontal-blanco.png`).
  - **Menú de navegación** lateral: tabla de contenidos con anclas a cada bloque/sección.
  - **Acordeón** por bloque (nativo `<details>/<summary>`, sin necesidad de DevExpress ni CDN externo):
    cada bloque de la matriz de casos es un panel expandible/colapsable; el primero abierto por defecto.
  - Autocontenido y portable (assets de logo copiados junto al HTML, sin dependencias de red para
    renderizar).
- El **destino final** de entrega (descarga directa, Jira, SharePoint, Confluence…) lo resuelve
  [`apb-plat-deliver-artifact-v1.0`](../../../skills/apb-owned/platform/apb-plat-deliver-artifact-v1.0.md)
  (ya pregunta formato y destino); lo que este estándar fija es que el **`.html` deja de ser opcional**
  para el tipo de artefacto «plan de pruebas» / «informe de ejecución» — se genera siempre, aunque el
  usuario no lo pida explícitamente como destino de entrega.
- **El informe de ejecución también es corporativo:** la versión `.html` del **informe** usa el mismo
  formato (cabecera azul + logo, nav, acordeón) y **renderiza el «Acta de aprobación» (§6.2)** como una
  tabla de firmantes con su estado — de modo que la autorización sea visible para el stakeholder que abre
  el HTML, no solo en el `.md`. **Esta obligación de entrega dual aplica igual al plan y al informe de
  ejecución — nunca se entrega un informe solo en `.md`.**

### 7.2 Evidencia visual: vídeo real, no GIF

- La evidencia visual de una sesión de ejecución (navegación agéntica/exploratoria, §9) debe ser **vídeo
  real** (`.mp4`/`.webm`), no un GIF animado. Un GIF generado por herramientas de captura del navegador
  (p. ej. la extensión Claude-in-Chrome) suele tener un **tope duro de fotogramas por grabación** —
  insuficiente y no representativo para cubrir la ejecución de un plan de pruebas completo; los
  fotogramas más antiguos se pierden o la grabación deja de añadir frames antes de cubrir todo el plan,
  sin que quede claro para el lector qué parte de la sesión falta.
- **Alternativa preferente:** cuando la ejecución se conduce vía **Playwright MCP** (una de las
  implementaciones de referencia de [`prov-browser-agent-v1.0`](../../../providers/prov-browser-agent-v1.0.md)),
  usar su grabación de vídeo real. **Corrección 2026-07-10:** no es un flag de arranque `video:'on'` (así
  lo describía esta sección antes de verificarlo) — son dos tools MCP, `browser_start_video` /
  `browser_stop_video`, que hay que invocar explícitamente al empezar/terminar cada bloque, y que solo
  existen si el servidor arrancó con `--caps devtools` y el binario `ffmpeg` está instalado
  (`npx playwright install ffmpeg`). Detalle completo, incluida la ruta relativa del fichero de salida,
  en `prov-playwright-v1.0.md`.
  - Si no hay grabador de vídeo real disponible en el entorno (ni Playwright MCP, ni un grabador de
    pantalla local), **segmentar** la evidencia GIF por bloque de la matriz (parar/exportar/limpiar la
    grabación en cada límite de bloque) en vez de una única grabación continua que pueda truncarse sin
    avisar, y **etiquetar cada fichero con el bloque que cubre**.
  - En ningún caso se presenta un GIF como si cubriera «toda la sesión» sin verificar que efectivamente
    la cubre — si hay duda razonable de truncamiento (sesión larga, muchos pasos), se declara
    explícitamente la limitación en el informe.
- **Verificación pre-vuelo (obligatoria antes de iniciar cualquier sesión de ejecución con evidencia
  visual):** confirmar que las herramientas de Playwright MCP están cargadas en la sesión activa (no
  basta con que `.mcp.json` exista en el repo — si la sesión ya estaba abierta antes de que se
  configurara, o si se abrió sin cargarlo, las tools no aparecen; requiere reabrir/reiniciar la sesión
  sobre este repo). Si tras reabrir la sesión las tools de Playwright MCP siguen sin estar disponibles,
  **no se procede a ejecutar el plan** — se declara el bloqueante y se aplica el fallback de GIF
  segmentado (párrafo anterior) documentando explícitamente por qué no había grabador de vídeo real.
  Esta comprobación quedó incumplida en la sesión QA TruckCenter del 2026-07-03 (punto #88): se ejecutó
  sin reabrir la sesión, resultando en GIF sin segmentar. Fix estructural (elimina la dependencia del
  puesto de trabajo): desplegar `prov-azure-qa-runtime-v1.0` (ver `HANDOFF_TECNICOS.md` QA3-2) — mientras
  no esté desplegado, esta verificación manual es la única salvaguarda.

---

## 8. No-regresión de rendimiento

- Cada ejecución del plan comprueba que el rendimiento **no empeora** respecto a la ejecución anterior.
- **Dónde se consulta el resultado anterior:** en las evidencias vinculadas de la ejecución previa (repo
  de la app / Jira).
- **Si nunca se ejecutó antes:** se ejecuta el plan **sobre la versión anterior del código y luego sobre la
  nueva** para obtener la comparativa base. Cruza con [`prov-k6-v1.0`](../../../providers/prov-k6-v1.0.md)
  (carga/rendimiento) — umbral de referencia: p95 < 2000 ms, error < 1 %.

### 8.1 Verificación pre-vuelo de k6 (obligatoria antes de generar/ejecutar una prueba real)

> `prov-k6-v1.0` no es un MCP real (a diferencia de Playwright) — es un wrapper de CLI (`k6 run`), requiere
> el binario instalado en el entorno que lo ejecuta.

- Confirmar el **destino de ejecución** (§9.1) ANTES de generar el script:
  - Si el destino es **`local`**: limitar el escenario a **`smoke`** (1-2 VUs, verificación básica) —
    **nunca** carga/estrés real contra un entorno compartido (PRE/PRO) desde un portátil individual.
  - Si el plan requiere una prueba de carga real (`load`/`stress`/`spike`/`soak`) contra PRE/PRO, el
    destino **debe** ser `ci-runner` o `azure-qa` (`prov-azure-qa-runtime-v1.0`, k6 preinstalado).
- Si ninguno de los dos destinos está disponible (p. ej. `azure-qa` aún sin desplegar — ver
  `HANDOFF_TECNICOS.md` QA3-2), **no se ejecuta la carga real**: se declara el bloqueante explícitamente en
  el informe. Nunca se sustituye en silencio por un smoke test presentado como si fuera la prueba completa.
- Si el destino es `local` (solo smoke), verificar que k6 está instalado (`k6 version`) antes de proceder;
  si no lo está, guiar la instalación (`docs/qa/EJECUCION_LOCAL.md` §2.3/§3) o preguntar si se prefiere
  otro destino.

---

## 9. Ejecución funcional

- **Scriptada / reproducible (CI, regresión):** Playwright (`prov-playwright-v1.0`) + `apb-qa-test-auto-v1.0`.
- **Exploratoria / en vivo (descubrimiento, QA asistido):** navegación agéntica
  (`prov-browser-agent-v1.0` + `apb-qa-exploratory-nav-v1.0`).
- **Autenticación** (p. ej. EntraID/SSO): capturar `storageState` en un login asistido y reutilizarlo;
  nunca hardcodear credenciales (usar Azure Key Vault por referencia, `GOVERNANCE.md` §5).

### 9.1 Destino de ejecución (quién ejecuta y dónde corren Playwright / k6)

Las pruebas puede lanzarlas **una persona** o **un workflow**. El plan declara el **destino de ejecución**:

| Destino | Quién lanza | Dónde corren Playwright / k6 | Cuándo usarlo |
|---|---|---|---|
| **`local`** | Persona, en su PC | En la máquina del usuario (requiere instalación — ver §9.3 y `docs/qa/EJECUCION_LOCAL.md`). El agente **guía la instalación paso a paso** si falta tooling. | Exploratorio, desarrollo, depuración de un caso puntual. |
| **`ci-runner`** | Workflow (GitHub Actions / Azure DevOps) | En el runner del pipeline (imagen con navegadores/k6). | Regresión automática por PR/nightly. |
| **`azure-qa`** | Workflow **o** persona (dispara el job) | En un **entorno efímero de la suscripción QA de Azure** con Playwright y k6 **pre-instalados** — el usuario/runner **no instala nada** (§9.4, `prov-azure-qa-runtime-v1.0`). | Ejecución completa (funcional + rendimiento + seguridad) reproducible y sin dependencias locales. |

**Reglas de destino:**
- **La carga k6 nunca se lanza desde el portátil** contra infraestructura compartida (PRE/PRO): rendimiento
  y estrés van a `ci-runner` o, preferentemente, `azure-qa`.
- Exploratorio/descubrimiento → `local` (o navegación agéntica). Regresión/rendimiento/seguridad →
  `ci-runner` / `azure-qa`.
- **Default explícito: `local`.** El usuario elige `azure-qa`/`ci-runner` explícitamente cuando lo
  prefiera (rendimiento real, "no quiero instalar nada", regresión reproducible) — no se pregunta a ciegas
  en cada invocación; se asume `local` salvo indicación en contra, respetando siempre la regla de arriba
  (carga real nunca desde `local`). Implementación de referencia para `azure-qa` (Playwright/k6
  preinstalados): [`infra/azure-qa-runtime/`](../../../infra/azure-qa-runtime/README.md) — contenedores ya
  generados, despliegue Azure pendiente de confirmación de Débora.

### 9.2 Roles de usuario y usuario de ejecución

Un plan de pruebas realista no basta con "qué se prueba": necesita **con qué rol** se prueba y **qué usuario
concreto** ejecuta.

- **Matriz de roles (obligatoria, §5.13):** el plan enumera los roles de usuario necesarios para las pruebas,
  con su alcance y qué bloques/casos los requieren:

  | Rol | Alcance / permisos | Bloques / casos que lo requieren |
  |---|---|---|
  | {p. ej. `USER_READ_*`} | Solo lectura | {B02, B05…} |
  | {p. ej. `MANAGE_*`} | Alta/baja/modificación | {B07…} |

- **Columna «Rol requerido» por caso:** cada caso de la matriz de pruebas declara el **rol mínimo** con el
  que debe ejecutarse (permite planificar pasadas por rol y detectar fallos de autorización).
- **Usuario concreto de ejecución** — **dos vías, nunca credenciales en el fichero** (`AGENTS.md §3`,
  `GOVERNANCE.md §5.2`):
  1. **Guardado en Key Vault** — referencia simbólica `AKV://<secret>` resuelta en runtime vía
     [`prov-akv-v1.0`](../../../providers/prov-akv-v1.0.md) (Managed Identity). Es la vía por defecto para
     ejecución autónoma (workflow / `azure-qa`). **No operativa hoy** (vault sin provisionar — ver §9.5,
     enfoque futuro); mientras tanto, usar siempre la vía 2.
  2. **Proporcionado por el usuario** — introducido interactivamente en tiempo de ejecución (p. ej. login
     asistido EntraID que produce un `storageState`). Ni la credencial ni el `storageState` con secretos se
     **persisten** en el repo.
- **Prohibido:** escribir usuarios, contraseñas, tokens o `storageState` con secretos en el plan, el informe,
  el catálogo o cualquier fichero versionado. Solo referencias simbólicas.

### 9.3 Ejecución local: guía de instalación asistida

Si el destino es `local` y la máquina del usuario **no** tiene el tooling (Node/Playwright/k6), la skill
**no falla**: **guía al usuario paso a paso** en la instalación, remitiendo a
[`docs/qa/EJECUCION_LOCAL.md`](../../../docs/qa/EJECUCION_LOCAL.md) (Node vía winget, `@playwright/test`,
`npx playwright install`, k6, verificación y captura de `storageState`).

### 9.4 Entorno QA en Azure (ejecución sin instalar nada)

Para "pruebas completas sin que el usuario ni el workflow instalen nada", el destino `azure-qa` usa
[`prov-azure-qa-runtime-v1.0`](../../../providers/prov-azure-qa-runtime-v1.0.md): un **job efímero** en la
**suscripción QA de Azure** con Playwright + k6 pre-instalados, **Managed Identity → AKV** para credenciales
y `storageState`, acceso de red a PRE/QA y salida de evidencias. **Diseño en `draft`**; el despliegue real
de la infraestructura es trabajo de la sesión QA-3.

### 9.5 Estado real de la infraestructura de ejecución (auditoría 2026-07-10) — inmediato vs. futuro

> Auditoría realizada al cerrar el lote de 32 planes de pruebas (sesión QA-continuación), a petición de
> Débora ("¿tengo todo lo necesario para ejecutar? k6, sonar, unitarias…"). Verificado componente a
> componente contra el repo real, no asumido. Este `§9.5` es la referencia que cualquier plan generado a
> partir de ahora debe citar en su §1.6/§8/§9 en vez de asumir que `AKV://<secret>` o `azure-qa` ya están
> operativos — **no lo están**. Dos enfoques, sin mezclarlos en el mismo plan sin decirlo explícitamente:

#### Enfoque inmediato (hoy — ejecución `local`)

Lo único realmente operativo sin trabajo previo de infraestructura. Cualquier plan que declare destino
`local` debe asumir **estas** limitaciones, no las del enfoque futuro:

| Dimensión | Estado real hoy | Qué significa para el plan |
|---|---|---|
| **Credenciales / usuario de ejecución** | `prov-akv-v1.0` **no tiene vault provisionado** — el `endpoint` en su ficha es un placeholder literal (`https://<vault-name>.vault.azure.net`), sin código resolutor en el repo. La vía 1 de §9.2 (`AKV://<secret>`) **no es usable hoy**. | Usar **siempre la vía 2 de §9.2**: credencial proporcionada por la persona en runtime (login asistido → `storageState`), nunca persistida. Cualquier plan que hoy escriba `AKV://<secret>` como si fuera resoluble debe marcarlo explícitamente como `(no operativo — ver §9.5)`. |
| **k6 (rendimiento)** | `prov-k6-v1.0` es un wrapper CLI local (`endpoint: "local://k6"`, sin cuenta k6 Cloud) — correcto para `local`. `infra/azure-qa-runtime/k6/` es un **runner Docker genérico** (Dockerfile + entrypoint que envuelve la imagen oficial de k6): no incluye ningún script `.js` de ninguna aplicación. | Solo **smoke** (1-2 VUs, §8.1) — nunca carga real desde el portátil. El script `.js` concreto de cada app **no existe todavía**; hay que escribirlo antes de poder ejecutar siquiera el smoke. |
| **SonarQube (calidad de código)** | Conexión REST real y verificada (`prov-sonar-v1.0`, User Token, `http://gisplanolpre.port.apb.es:9001`, 100 proyectos reales listados) — pero es el **token personal de Débora** guardado como variable de entorno local, y hoy solo lo consume `scripts/generate_powerbi_dashboard.py`. No está confirmado qué apps del lote de 32 tienen project key registrado en esa instancia. | Consultable **ad-hoc y manualmente** (no es un gate automático) para las apps que sí tengan project key confirmado — no asumir cobertura Sonar disponible para toda la lista sin comprobarlo app por app antes de citarla en un informe. |
| **Tests unitarios** | **Fuera del alcance de este estándar.** `TEST_PLAN_STANDARD` cubre funcional (Playwright) + rendimiento (k6), no unitarios. El framework **no orquesta** ejecución de tests unitarios de ninguna app — cada repo de aplicación tiene (o no) su propia suite y su propio pipeline (Jenkins/GitHub Actions), ajeno a este framework. Verificado: la mayoría de los repos `APB.API.*` clonados sí tienen carpeta de tests propia; **`APB.INS` es una excepción confirmada sin ningún test automatizado** (ver plan INS §17.3, punto 9). | Si el plan necesita evidencia de cobertura unitaria, **remitir al pipeline propio de la app**, no inventar una ejecución centralizada que no existe. Señalar explícitamente cuándo una app (como INS) no tiene ninguna base de tests unitarios sobre la que apoyarse. |
| **Playwright** | Sí operativo hoy vía `prov-playwright-v1.0` + instalación local guiada (§9.3, `docs/qa/EJECUCION_LOCAL.md`). | Es la única pata de este §9.5 sin gap real — funciona tal como está descrito en §9.3. |

#### Enfoque futuro (infraestructura centralizada — `ci-runner` / `azure-qa`)

Trabajo de aprovisionamiento pendiente, no de generación de planes. No se ejecuta hasta que exista:

1. **AKV real provisionado** — vault + Managed Identity + resolución `AKV://<secret>` en tiempo de
   ejecución (`prov-akv-v1.0` pasa de `draft` con endpoint placeholder a `active` con endpoint real).
   Desbloquea la vía 1 de §9.2 y elimina la dependencia de credenciales manuales por persona.
2. **`azure-qa` desplegado de verdad** — el diseño y los contenedores (`infra/azure-qa-runtime/`, Playwright
   + k6) ya existen; falta el despliegue real en la suscripción QA de Azure (`prov-azure-qa-runtime-v1.0`
   sigue en `draft`; ver `HANDOFF_TECNICOS.md` QA3-2). Con esto, la carga k6 real (`load`/`stress`/`spike`/
   `soak`) deja de estar bloqueada por §8.1.
3. **Scripts k6 reales por aplicación** — el runner Docker es genérico; cada API del lote de 32 necesita su
   propio script `.js` (endpoints, VUs, umbrales) antes de que el punto 2 tenga algo que ejecutar.
4. **Sonar con cuenta de servicio + project keys confirmados** — sustituir el token personal de Débora por
   una credencial de servicio (vía AKV, punto 1), y confirmar/registrar el project key de cada una de las 32
   apps del lote para poder citar cobertura real en cada plan, no solo en el dashboard Power BI.
5. **Tests unitarios: fuera de alcance incluso en el enfoque futuro** — su ejecución sigue viviendo en el
   pipeline propio de cada app; este framework no absorbe esa responsabilidad. Si en el futuro se decide
   centralizar también esto, es una decisión nueva de Débora/Arquitectura, no una extensión implícita de
   `azure-qa`.

**Regla para cualquier plan que cite este §9.5:** declarar explícitamente cuál de los dos enfoques asume, y
si es el inmediato, no describir AKV/k6-carga-real/Sonar-gate como si funcionaran hoy — remitir a esta
sección en vez de repetir el detalle completo en cada documento.

---

## 10. Verificación de cumplimiento

Un plan de pruebas es conforme cuando:

- [ ] Toda prueba tiene procedencia (≥1 herramienta, ≥1 origen) y columna «Desde».
- [ ] Sin duplicados; si hubo unificación, existe la tabla de mapeo.
- [ ] **Conservación íntegra (§3.1):** el unificado es superconjunto de sus fuentes — ningún bloque narrativo
      (incidencias históricas, proyectos futuros, modelo de datos, funcionalidad, documentos de referencia,
      checklist, plantilla) se ha perdido. Verificado sección a sección.
- [ ] Presentes las 12 secciones obligatorias (§5).
- [ ] Histórico y aprobados por cambio actualizados.
- [ ] Evidencias vinculadas bidireccionalmente y a Jira.
- [ ] No-regresión de rendimiento evaluada o justificada su ausencia.
- [ ] Marcado IA conforme a [`AI_MARKING_STANDARD`](AI_MARKING_STANDARD.md).
- [ ] **ID canónico (§3.2):** todo caso usa el esquema `{APP}-B{NN}-T{NN}` append-only; si hubo migración
      desde numeración plana, existe columna «Legado» con el ID anterior.
- [ ] **Owner de gobernanza (§6.1):** el plan tiene un responsable nombrado y su cadencia de revisión
      (por release) está declarada.
- [ ] **Entrega dual (§7.1):** existen versión `.md` y versión `.html` (cabecera azul + logo, nav lateral,
      acordeón por bloque) del plan y, tras ejecutar, del informe. **Nunca solo `.md` en el informe.**
- [ ] **Casos no ejecutados listados (§5.15):** el informe de ejecución lista por ID canónico los casos no
      ejecutados/bloqueados, no solo un recuento por bloque.
- [ ] **Evidencia visual = vídeo, no GIF (§7.2):** si hay evidencia visual de sesión, es vídeo real o, en
      su defecto, GIF segmentado por bloque con la limitación declarada explícitamente.
- [ ] **Verificación pre-vuelo de Playwright MCP (§7.2):** ANTES de empezar, confirmado que las tools de
      Playwright MCP están cargadas en la sesión activa (reabierta si hacía falta). Si no lo están, el
      informe declara el bloqueante explícitamente — no se asume vídeo real sin haberlo comprobado.
- [ ] **Verificación pre-vuelo de k6 (§8.1):** si el plan incluye rendimiento real (no smoke), confirmado
      que el destino de ejecución es `ci-runner`/`azure-qa` (nunca carga real desde un portátil); si no hay
      destino disponible, el bloqueante queda declarado explícitamente, no sustituido en silencio por smoke.
- [ ] **Roles y usuario de ejecución (§9.2):** existe la matriz de roles y cada caso declara su «Rol
      requerido»; el usuario de ejecución se resuelve por referencia AKV o entrada en runtime — **ningún
      secreto ni `storageState` con credenciales está en fichero versionado**.
- [ ] **Destino de ejecución (§9.1):** el plan declara `local` / `ci-runner` / `azure-qa`; la carga k6 no
      se lanza desde el portátil contra infra compartida.
- [ ] **Enfoque inmediato vs. futuro declarado (§9.5):** si el plan asume ejecución hoy, no describe
      `AKV://<secret>`, carga k6 real ni gate de Sonar como operativos — usa credencial en runtime, k6 solo
      smoke y Sonar como consulta manual (project key confirmado), o remite a §9.5 en vez de repetirlo.
- [ ] **Fuente spec en flujo SDD (§1):** si el plan nace de un flujo SDD, la spec es input y cada caso
      traza a su criterio de aceptación.
- [ ] **Acta de aprobación del informe (§6.2):** el informe de ejecución incluye el acta (Funcional +
      Desarrollador), persistida en el `.md` y reflejada en Jira; el agente no se autoaprueba.

> **Generado por IA:** Claude (Anthropic), Sesión QA-2 del APB AI Framework.
> **Validado por humano:** _pendiente — completar nombre/rol antes de pasar a `candidate`._

---

## Historial

| Versión | Fecha | Cambio |
|---------|-------|--------|
| 1.0.0 | 2026-07-02 | Creación del estándar (orden de fuentes, procedencia múltiple, unificación, secciones obligatorias, gobernanza, no-regresión). |
| 1.1.0 | 2026-07-02 | **§3.1 Principio de conservación** (regla no negociable): unificar es un superconjunto — conserva pruebas **y** todo el contenido narrativo; la pérdida silenciosa es defecto bloqueante. Ítem añadido al checklist §10. Refuerza el check #21 del validador. Origen: feedback de Débora tras detectar pérdida de contenido (incidencias históricas) en el ejemplo unificado. |
| 1.2.0 | 2026-07-03 | **§3.2 Identificador canónico y crecimiento** (`{APP}-B{NN}-T{NN}` append-only, migración con columna «Legado» — resuelve la ruptura de correlación plan↔informe al añadir pruebas a un bloque existente). **§6.1 Gobernanza por aplicación** (owner nombrado, cadencia por release, ciclo de vida `GOVERNANCE.md`). **§7.1 Entrega dual Markdown + HTML** obligatoria (cabecera azul + logo APB, nav lateral, acordeón nativo por bloque, sin DevExpress/CDN). 3 ítems añadidos al checklist §10. Origen: feedback de Débora. |
| 1.3.0 | 2026-07-03 | **Fase I** (7 huecos detectados por Débora). **§1** añade `spec` (SDD) como fuente funcional autoritativa de primer nivel; **§2** añade origen canónico `spec`. **§6.2 Aprobación del informe de resultados** (acta Funcional + Desarrollador, persistida en `.md` **y** Jira, sign-off no criptográfico, dos ojos). **§6.3 Bucle de corrección** fallo → PR → Jira (`apb-sub-qa-fix-loop-v1.0`, propone PR sin mergear). **§9.1 Destino de ejecución** (`local`/`ci-runner`/`azure-qa`; k6 nunca desde portátil). **§9.2 Roles de usuario y usuario de ejecución** (matriz de roles, columna «Rol requerido», usuario por AKV o runtime, nunca en fichero). **§9.3 Instalación local asistida** (`docs/qa/EJECUCION_LOCAL.md`). **§9.4 Entorno QA en Azure** (`prov-azure-qa-runtime-v1.0`, draft). Secciones obligatorias §5.13/§5.14 y 4 ítems al checklist §10. Origen: feedback de Débora. |
| 1.4.0 | 2026-07-03 | **§5.15 Casos NO ejecutados/bloqueados** — obligatorio en el informe de ejecución listar por ID canónico (no solo recuento agregado) los casos no ejecutados y su motivo. **§7.1** refuerza que la entrega dual Markdown+HTML nunca se omite en el informe. **§7.2 Evidencia visual: vídeo real, no GIF** — el GIF de herramientas de captura del navegador tiene tope de fotogramas y puede truncar sesiones largas sin avisar; se prefiere vídeo real (Playwright MCP `video:'on'`) o, en su defecto, GIF segmentado por bloque con la limitación declarada. 3 ítems añadidos al checklist §10. Origen: feedback de Débora tras detectar que el informe de ejecución de la sesión QA TruckCenter (2026-07-03) se generó solo en `.md`, sin listar los casos no ejecutados, y con un GIF de cobertura dudosa presentado sin esa advertencia. |
| 1.5.0 | 2026-07-05 | **§2 Notación de procedencia en texto legible, sin siglas** — sustituye la notación abreviada `R[J:...]·C[Cod]` por frases que un lector no técnico entiende sin leyenda (p. ej. `Jira aportado por Débora (ticket AOM-2530)`, `Código fuente verificado (repo APB.API.TES, PortCallController.cs:38)`). Origen: feedback de Débora durante la generación del lote de 32 planes de pruebas (sesión QA-continuación), tras detectar que `R[J]` no se entendía sin la leyenda y que además `R` (Rovo) se usaba de forma imprecisa para tickets citados en documentos aportados por el usuario, no consultados en vivo vía Rovo. |
| 1.5.1 | 2026-07-07 | **§7.2 Verificación pre-vuelo de Playwright MCP** — obligatorio confirmar, antes de iniciar cualquier sesión de ejecución con evidencia visual, que las tools de Playwright MCP están cargadas (reabrir la sesión si hace falta); si no lo están, no se procede y se declara el bloqueante en vez de asumir vídeo real. Ítem añadido al checklist §10. Fix estructural señalado: desplegar `prov-azure-qa-runtime-v1.0` (`HANDOFF_TECNICOS.md` QA3-2) para eliminar la dependencia del puesto de trabajo por completo. Origen: feedback de Débora tras confirmar que la última ejecución de un plan de pruebas volvió a generar solo GIF, no vídeo, por repetir el mismo fallo de sesión no reabierta (punto #88). |
| 1.6.0 | 2026-07-07 | **§8.1 Verificación pre-vuelo de k6** (nueva subsección) — antes de generar/ejecutar una prueba de rendimiento real, confirmar el destino de ejecución: `local` limita a smoke, carga real requiere `ci-runner`/`azure-qa` o se declara el bloqueante explícitamente (nunca sustituido en silencio por un smoke test). Ítem añadido al checklist §10. Origen: Débora preguntó qué hacía falta para que la próxima ejecución de un plan incluyera también rendimiento — se confirmó que el diseño (skill + subagente + bloque B13 de TruckCenter) ya existe, pero falta el mismo runtime de Azure QA (QA3-2) que resuelve también el vídeo. |
| 1.6.1 | 2026-07-07 | **§9.1 Default explícito `local`** para el destino de ejecución — deja de preguntarse a ciegas en cada invocación; `azure-qa`/`ci-runner` se eligen explícitamente. Referencia a la implementación real de `azure-qa` ya generada en `infra/azure-qa-runtime/` (Dockerfiles Playwright + k6). Origen: Débora pidió que el agente de QA permita elegir entre local (predeterminado) y Azure QA, tras confirmar que ya tiene el entorno Container Apps creado. |
| 1.7.0 | 2026-07-10 | **§9.5 Estado real de la infraestructura de ejecución — inmediato vs. futuro** (nueva subsección). Tras el cierre del lote de 32 planes de pruebas, Débora preguntó si había "todo lo necesario para ejecutar: k6, sonar, unitarias…" — auditoría componente a componente confirmó que `prov-akv-v1.0` no tiene vault provisionado (endpoint placeholder), que `infra/azure-qa-runtime/k6/` es un runner Docker genérico sin ningún script `.js` de aplicación, que la conexión Sonar real (`prov-sonar-v1.0`) usa el token personal de Débora y solo la consume el dashboard Power BI (sin gate de calidad ni project keys de las 32 apps confirmados), y que los tests unitarios están fuera del alcance de este estándar (viven en el pipeline propio de cada app — `APB.INS` confirmado sin ninguno). §9.2 y el checklist §10 quedan enlazados a §9.5 para no describir estas piezas como operativas cuando el plan asume ejecución inmediata. Origen: feedback de Débora. |
| 1.7.1 | 2026-07-10 | **§7.2 corrige la suposición de vídeo real vía Playwright MCP.** Débora preguntó si la grabación de vídeo estaba resuelta; al comprobarlo, `video:'on'` (como lo describía esta sección) no existe como tal — son dos tools MCP, `browser_start_video`/`browser_stop_video`, ocultas tras la capability `devtools` (no activa por defecto) y que además requieren el binario `ffmpeg` instalado aparte de los navegadores. Verificado end-to-end con un servidor de prueba aislado: con `--caps devtools` + `ffmpeg` instalado, produce un `.webm` real y válido. `.mcp.json` y `prov-playwright-v1.0.md` actualizados con la configuración real y la instrucción exacta de uso (incluida la ruta relativa del fichero, que se resuelve contra el directorio de trabajo del proceso, no contra `--output-dir`). Origen: pregunta de Débora tras el cierre de la sesión anterior. |
