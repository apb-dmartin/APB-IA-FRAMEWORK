---
id: "std-test-plan-v1.0"
name: "Estándar Corporativo de Planes de Pruebas"
version: "1.2.0"
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
2. **Rovo (Atlassian)** — tickets de Jira, sus adjuntos, análisis funcional y documentación aportada.
3. **GitHub Copilot** — ingeniería inversa del código, para **completar y contrastar** lo funcional.

### 1.1 Degradación cuando faltan fuentes

Jira o el Análisis Funcional **pueden faltar o estar obsoletos**. En ese caso:

- El plan **no se bloquea**: se apoya en las fuentes disponibles (típicamente el código vía Copilot) y
  **marca cada prueba con su procedencia y confianza real**.
- **Nunca se inventa** respaldo funcional inexistente: si una prueba solo tiene respaldo de código, su
  procedencia dice `Cod` (código) y **no** `J`/`AF`.
- Si el AF está obsoleto respecto al código, se registra la **discrepancia** como observación de la prueba
  y se marca para revisión funcional humana.

---

## 2. Modelo de procedencia (múltiple y obligatorio)

Toda prueba lleva **≥1 origen** y **≥1 herramienta**. La procedencia es una **lista**, no un valor único.

| Dimensión | Valores canónicos |
|---|---|
| **Herramienta** (quién la propuso) | `rovo` · `github-copilot` · `usuario` · (otras: nombre libre) |
| **Origen** (de dónde sale) | `jira` (con ticket) · `documentacion` (AF/spec) · `codigo` · `usuario` (con formato de origen) |

**Notación recomendada en la columna «Procedencia»** de la matriz de casos:
`R[J:TICKET·AF] · C[Cod]` donde `R`=Rovo, `C`=Copilot, `U`=Usuario; orígenes `J`/`AF`/`Cod`.
Ejemplo: `R[J:TRANSTE-1513·AF] · C[Cod]` = propuesta por Rovo desde el ticket y el AF, validada contra código por Copilot.

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

---

## 8. No-regresión de rendimiento

- Cada ejecución del plan comprueba que el rendimiento **no empeora** respecto a la ejecución anterior.
- **Dónde se consulta el resultado anterior:** en las evidencias vinculadas de la ejecución previa (repo
  de la app / Jira).
- **Si nunca se ejecutó antes:** se ejecuta el plan **sobre la versión anterior del código y luego sobre la
  nueva** para obtener la comparativa base. Cruza con [`prov-k6-v1.0`](../../../providers/prov-k6-v1.0.md)
  (carga/rendimiento) — umbral de referencia: p95 < 2000 ms, error < 1 %.

---

## 9. Ejecución funcional

- **Scriptada / reproducible (CI, regresión):** Playwright (`prov-playwright-v1.0`) + `apb-qa-test-auto-v1.0`.
- **Exploratoria / en vivo (descubrimiento, QA asistido):** navegación agéntica
  (`prov-browser-agent-v1.0` + `apb-qa-exploratory-nav-v1.0`).
- **Autenticación** (p. ej. EntraID/SSO): capturar `storageState` en un login asistido y reutilizarlo;
  nunca hardcodear credenciales (usar Azure Key Vault por referencia, `GOVERNANCE.md` §5).

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
      acordeón por bloque) del plan y, tras ejecutar, del informe.

> **Generado por IA:** Claude (Anthropic), Sesión QA-2 del APB AI Framework.
> **Validado por humano:** _pendiente — completar nombre/rol antes de pasar a `candidate`._

---

## Historial

| Versión | Fecha | Cambio |
|---------|-------|--------|
| 1.0.0 | 2026-07-02 | Creación del estándar (orden de fuentes, procedencia múltiple, unificación, secciones obligatorias, gobernanza, no-regresión). |
| 1.1.0 | 2026-07-02 | **§3.1 Principio de conservación** (regla no negociable): unificar es un superconjunto — conserva pruebas **y** todo el contenido narrativo; la pérdida silenciosa es defecto bloqueante. Ítem añadido al checklist §10. Refuerza el check #21 del validador. Origen: feedback de Débora tras detectar pérdida de contenido (incidencias históricas) en el ejemplo unificado. |
| 1.2.0 | 2026-07-03 | **§3.2 Identificador canónico y crecimiento** (`{APP}-B{NN}-T{NN}` append-only, migración con columna «Legado» — resuelve la ruptura de correlación plan↔informe al añadir pruebas a un bloque existente). **§6.1 Gobernanza por aplicación** (owner nombrado, cadencia por release, ciclo de vida `GOVERNANCE.md`). **§7.1 Entrega dual Markdown + HTML** obligatoria (cabecera azul + logo APB, nav lateral, acordeón nativo por bloque, sin DevExpress/CDN). 3 ítems añadidos al checklist §10. Origen: feedback de Débora. |
