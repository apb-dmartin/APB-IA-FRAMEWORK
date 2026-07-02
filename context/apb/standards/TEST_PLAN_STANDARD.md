---
id: "std-test-plan-v1.0"
name: "Estándar Corporativo de Planes de Pruebas"
version: "1.0.0"
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

## 3. Unificación sin duplicados

Cuando concurren varias visiones del mismo plan (p. ej. una por Jira, otra enriquecida con AF, otra por
código):

1. Se funde **por intención de la prueba**, no por número de caso (numeraciones distintas pueden colisionar).
2. Se conservan **todas** las pruebas; los solapamientos se unifican en un caso con **procedencia múltiple**.
3. Se asigna un **ID canónico estable** y se publica una **tabla de mapeo** desde las numeraciones de origen,
   para no perder trazabilidad.

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

---

## 7. Almacenamiento de resultados y evidencias

- **El plan y sus resultados de ejecución se guardan en el repo de cada aplicación**, no en el repo del
  framework. El framework guarda **estándar + plantilla + ejemplo canónico**.
- Las **evidencias** (capturas, trazas, vídeo, informe) se vinculan bidireccionalmente al plan y se
  **enlazan a Jira**. El destino de las evidencias es **seleccionable en ejecución**:
  - **Paquete descargable** (ZIP con informe HTML), y/o
  - **Subida a Jira** como adjuntos vinculados al ticket (vía `adapter-rovo-v1.0` / API Jira).

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
- [ ] Presentes las 12 secciones obligatorias (§5).
- [ ] Histórico y aprobados por cambio actualizados.
- [ ] Evidencias vinculadas bidireccionalmente y a Jira.
- [ ] No-regresión de rendimiento evaluada o justificada su ausencia.
- [ ] Marcado IA conforme a [`AI_MARKING_STANDARD`](AI_MARKING_STANDARD.md).

> **Generado por IA:** Claude (Anthropic), Sesión QA-2 del APB AI Framework.
> **Validado por humano:** _pendiente — completar nombre/rol antes de pasar a `candidate`._
