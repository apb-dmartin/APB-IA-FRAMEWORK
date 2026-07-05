# Plan de Pruebas — {NOMBRE_APLICACIÓN} ({APIs/módulos})

> **Borrador generado por IA** (APB AI Framework — apb-qa-test-plan) — pendiente validación humana. No distribuir sin revisión.
>
> **Plantilla** conforme a [`TEST_PLAN_STANDARD`](../standards/TEST_PLAN_STANDARD.md). Rellenar los `{marcadores}`.
> Guardar el plan y sus resultados **en el repo de la aplicación**, no en el del framework.
> **Conservación (§3.1):** al unificar varias fuentes, esta plantilla se rellena **completa** — ninguna
> sección se omite ni se resume; lo redundante se funde, nunca se descarta.
>
> **Fecha:** {AAAA-MM-DD} · **Aplicación:** {app} · **Entorno(s):** {PRE/PRO} · **Owner:** {rol/email — §6.1 gobernanza}

---

## 0. Método de unificación y procedencia

> Rellenar solo si el plan funde varias fuentes; si no, indicar la fuente única.

| Cód. | Fuente | Herramienta | Origen | Casos |
|---|---|---|---|---|
| A | {archivo/ticket} | {rovo/github-copilot/usuario} | {jira/documentacion/codigo/usuario} | {N} |
| … | | | | |

**Leyenda «Procedencia»:** `R`=Rovo · `C`=GitHub Copilot · `U`=Usuario · orígenes `J`=Jira(+ticket) ·
`AF`=Documentación/Análisis Funcional · `Cod`=Código. Toda prueba lleva ≥1 herramienta y ≥1 origen.
**«Desde»:** fecha en que se definió la prueba. **«OK func.»:** funcional que la aprobó (vacío hasta validar).

**Identificador canónico (§3.2):** `{APP}-B{NN}-T{NN}` — bloque append-only + secuencia append-only
dentro del bloque. Si se migra desde una numeración plana previa, se añade columna **«Legado»** con el
ID anterior (nunca se pierde la trazabilidad con informes ya emitidos).

---

## 1. Descripción general
{Qué hace la aplicación, alcance funcional.}

### 1.1 APIs y endpoints
| API | Función | Endpoint PRE | Endpoint PRO |
|-----|---------|-------------|-------------|
| {API} | {función} | {url} | {url} |

### 1.2 Arquitectura topológica
```
{diagrama de componentes / flujo de datos}
```

### 1.3 Integraciones
{WS, SSO, sistemas externos, pipelines, precondiciones globales (p. ej. rollback sin reintento).}

### 1.4 Modelo de datos (relación de tablas)
{Tablas principales, con columnas/tipos/nulabilidad/PKs/FKs — no solo los nombres de tabla.}

#### 1.4.1 {Tabla principal}
| Columna | Tipo | Nulable | Descripción |
|---------|------|---------|-------------|
| {col} | {tipo} | {PK/NOT NULL/Nullable} | {descripción} |

### 1.5 Máquina de estados / reglas de negocio clave
{Estados y transiciones; reglas críticas (p. ej. duplicados, confirmaciones).}

### 1.6 Roles de usuario y usuario de ejecución (§9.2)
> Roles necesarios para las pruebas + qué bloques los requieren. El **usuario concreto** que ejecuta se
> resuelve por **referencia AKV** (`AKV://<secret>`, vía `prov-akv-v1.0`) **o** se **proporciona en runtime**
> (login asistido → `storageState`). **Nunca** se escribe usuario/contraseña/token/`storageState` con
> secretos en este documento ni en ningún fichero versionado (`AGENTS.md §3`, `GOVERNANCE.md §5.2`).

| Rol / Permiso | Alcance | Bloques / casos que lo requieren |
|---|---|---|
| {rol} | {qué puede hacer} | {B02, B05…} |

**Usuario de ejecución:** {`AKV://<secret>` (por defecto, ejecución autónoma) | proporcionado por el
usuario en runtime}. **Destino de ejecución (§9.1):** {`local` | `ci-runner` | `azure-qa`}.

### 1.7 Referencia a Spec / Análisis Funcional
{Documentos de origen, versión, fecha. Si el plan nace de un flujo SDD, **enlazar la spec** —
`apb-disc-spec-gen-v1.0` — que es la fuente funcional autoritativa (§1); cada caso traza a su criterio
de aceptación.}

---

## 2. Funcionalidad detallada

> Desarrollo funcional completo por pantalla/endpoint — campos, comportamientos, columnas por defecto y
> añadibles, mensajes, errores. **No resumir**: esta sección es la que más se pierde al condensar (§3.1).

### 2.1 {Endpoint/pantalla A}
{Parámetros, lógica de negocio, casos borde.}

### 2.2 {Endpoint/pantalla B}
{Campos, obligatoriedad, editabilidad, valores por defecto.}

### 2.3 Eventos de auditoría
| Evento | Descripción |
|--------|-------------|
| {EVENTO_OK} | {texto} |
| {EVENTO_KO} | {texto} |

### 2.4 Mensajes funcionales
| Pantalla | Motivo | Mensaje |
|----------|--------|---------|
| {pantalla} | {motivo} | {texto exacto} |

### 2.5 Errores funcionales
| Motivo | Error |
|--------|-------|
| {motivo} | {texto exacto} |

---

## 3. Incidencias históricas relevantes

> Bugs/tickets ya corregidos que condicionan el comportamiento esperado — se conservan siempre, no se
> eliminan al unificar (§3.1).

| Ticket | Descripción | Causa raíz | Impacto |
|--------|-------------|------------|---------|
| {ticket} | {descripción} | {causa} | {impacto} |

---

## 4. Proyectos futuros

> Iniciativas conocidas que afectarán a esta aplicación (para contexto de priorización, no para probar hoy).

| Ticket | Proyecto | Alcance |
|--------|----------|---------|
| {ticket} | {proyecto} | {alcance} |

---

## 5. Matriz de pruebas

> Un bloque por área funcional. Estado inicial `Pendiente`. IDs con esquema **§3.2** (`{APP}-B{NN}-T{NN}`,
> append-only). Añadir columna «Legado» solo si el plan migra desde numeración plana previa.

### Bloque B{NN} — {área}

| ID | Legado | Caso | Tipo | Prio | Rol requerido | Resultado esperado | Procedencia | Desde | OK func. | Estado | Evidencia |
|----|--------|------|------|------|---------------|--------------------|-------------|-------|----------|--------|-----------|
| {APP}-B{NN}-T{NN} | {ID plano si migró, si no —} | {caso} | {Funcional/UI/Integración/Seguridad/…} | {Crítica/Alta/Media} | {rol mínimo, p. ej. USER_READ_*} | {resultado} | {R[J:TICKET·AF]·C[Cod] / S[spec:CRIT-id]} | {AAAA-MM-DD} | {rol o —} | Pendiente | {enlace} |

---

## 6. Resumen del plan
| Bloque | Descripción | Casos | Crítica | Alta | Media |
|--------|-------------|-------|---------|------|-------|
| B{NN} | {área} | {N} | | | |
| **TOTAL** | | | | | |

**Procedencia (resumen):** {N con Jira} · {N desde AF} · {N validados en código} · {N duplicados = 0}.

---

## 7. Mapeo de numeraciones de origen → canónico
> Solo si hubo unificación de varias fuentes y/o migración desde IDs planos.

| Origen | Caso | → ID canónico (§3.2) |
|---|---|---|
| {A-Tnn / ID plano} | {caso} | {APP}-B{NN}-T{NN} |

---

## 8. Criterios de entrada / salida
- **Entrada:** {entorno, datos, servicios, usuarios/roles}.
- **Salida:** {criticos aprobados, 0 críticos abiertos, evidencia documentada, sin regresión de rendimiento}.

---

## 9. Checklist ejecutable
> Un ítem por caso, agrupado por bloque, con el ID canónico. Marcar `[x]` al ejecutar.

**Bloque B{NN} — {área}:** ☐ {APP}-B{NN}-T01 ☐ {APP}-B{NN}-T02 …

---

## 10. Plantilla de ejecución
- **Fecha de ejecución:**
- **Entorno:** (PRE / PRO)
- **Responsable:**
- **Rol utilizado:**
- **Resultado general:**
- **Observaciones:**
- **Firma:**

---

## 11. Tickets / fuentes analizadas
{Lista de tickets Jira, documentos o commits revisados para construir el plan.}

## 12. Documentos de referencia
| Documento | Versión | Fecha | Fuente |
|-----------|---------|-------|--------|
| {doc} | {v} | {fecha} | {AF / Jira / archivo aportado / repo de código} |

---

## 13. Histórico de cambios del plan
| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| {v} | {fecha} | {autor} | {cambio} |

## 14. Aprobados del plan (por cambio)
| Versión | Cambio | Aprobado por (rol) | Fecha |
|---------|--------|--------------------|-------|
| {v} | {cambio} | {rol} | {fecha} |

## 14bis. Acta de aprobación del informe de resultados (§6.2)
> **Rellenar en el informe de ejecución** (no en el plan base). Autoriza los **resultados** de una corrida.
> El agente **no** se autoaprueba: cada fila la firma una persona nombrada. La decisión se persiste aquí
> **y** se refleja en el ticket Jira vinculado (`prov-jira-software-v1.0`).

- **Estado del informe:** {`pendiente-aprobación` | `aprobado` | `rechazado` | `aprobado-con-reservas`}

| Rol | Nombre | Fecha | Decisión | Comentarios |
|---|---|---|---|---|
| **Analista Funcional** | {nombre} | {AAAA-MM-DD} | {Aprobado / Rechazado / Con reservas} | {texto} |
| **Desarrollador** | {nombre} | {AAAA-MM-DD} | {Aprobado / Rechazado / Con reservas} | {texto} |
| QA Lead (si aplica) | {nombre} | {AAAA-MM-DD} | {decisión} | {texto} |

> Si hay decisión `Rechazado` / `Con reservas` con pruebas en fallo → se dispara el **bucle de corrección**
> `apb-sub-qa-fix-loop-v1.0` (§6.3): propone PR con correcciones y anota el ticket Jira.

## 15. Evidencias y vínculo a Jira
- **Ubicación de resultados/evidencias:** {repo de la app / ruta}.
- **Enlace bidireccional:** plan → evidencias {enlace} · evidencias → plan {enlace}.
- **Jira:** {clave de proyecto / tickets con adjuntos de evidencia}.
- **No-regresión de rendimiento:** {resultado anterior consultado en… / comparativa base ejecutada}.

## 16. Entregables
- **Gobernanza (§6.1):** owner nombrado `{rol/email}`; revisión en cada release de `{app}`.
- **Formatos (§7.1, obligatorio):** este documento se entrega siempre en **Markdown** (`.md`, fuente de
  verdad) **y HTML** (`.html`, cabecera azul + logo APB, menú de navegación, acordeón por bloque —
  generado con `scripts/generate_test_plan_html.py`, sin DevExpress ni CDN).
- **Destino de entrega:** resuelto por `apb-plat-deliver-artifact-v1.0` (descarga / Jira / SharePoint / Confluence).

---

*Documento del APB AI Framework. Requiere revisión humana antes de aprobación (draft → candidate).*
