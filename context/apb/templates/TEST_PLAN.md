# Plan de Pruebas — {NOMBRE_APLICACIÓN} ({APIs/módulos})

> **Borrador generado por IA** (APB AI Framework — apb-qa-test-plan) — pendiente validación humana. No distribuir sin revisión.
>
> **Plantilla** conforme a [`TEST_PLAN_STANDARD`](../standards/TEST_PLAN_STANDARD.md). Rellenar los `{marcadores}`.
> Guardar el plan y sus resultados **en el repo de la aplicación**, no en el del framework.
>
> **Fecha:** {AAAA-MM-DD} · **Aplicación:** {app} · **Entorno(s):** {PRE/PRO} · **Owner:** {rol/email}

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

### 1.3 Modelo de datos (relación de tablas)
{Tablas principales, PKs/FKs, relaciones.}

### 1.4 Máquina de estados / reglas de negocio clave
{Estados y transiciones; reglas críticas.}

### 1.5 Integraciones
{WS, SSO, sistemas externos, pipelines.}

### 1.6 Referencia a Spec / Análisis Funcional
{Documentos de origen, versión, fecha.}

---

## 2. Matriz de pruebas

> Un bloque por área funcional. Estado inicial `Pendiente`.

### Bloque {n} — {área}

| ID | Caso | Tipo | Prio | Resultado esperado | Procedencia | Desde | OK func. | Estado | Evidencia |
|----|------|------|------|--------------------|-------------|-------|----------|--------|-----------|
| {ID} | {caso} | {Funcional/UI/Integración/Seguridad/…} | {Crítica/Alta/Media} | {resultado} | {R[J:TICKET·AF]·C[Cod]} | {AAAA-MM-DD} | {rol o —} | Pendiente | {enlace} |

---

## 3. Resumen del plan
| Bloque | Descripción | Casos | Crítica | Alta | Media |
|--------|-------------|-------|---------|------|-------|
| {n} | {área} | {N} | | | |
| **TOTAL** | | | | | |

**Procedencia (resumen):** {N con Jira} · {N desde AF} · {N validados en código} · {N duplicados = 0}.

---

## 4. Mapeo de numeraciones de origen → unificado
> Solo si hubo unificación de varias fuentes con numeraciones distintas.

| Origen | Caso | → Unificado |
|---|---|---|
| {A-Tnn} | {caso} | {ID} |

---

## 5. Criterios de entrada / salida
- **Entrada:** {entorno, datos, servicios, usuarios/roles}.
- **Salida:** {criticos aprobados, 0 críticos abiertos, evidencia documentada, sin regresión de rendimiento}.

## 6. Histórico de cambios del plan
| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| {v} | {fecha} | {autor} | {cambio} |

## 7. Aprobados del plan (por cambio)
| Versión | Cambio | Aprobado por (rol) | Fecha |
|---------|--------|--------------------|-------|
| {v} | {cambio} | {rol} | {fecha} |

## 8. Evidencias y vínculo a Jira
- **Ubicación de resultados/evidencias:** {repo de la app / ruta}.
- **Enlace bidireccional:** plan → evidencias {enlace} · evidencias → plan {enlace}.
- **Jira:** {clave de proyecto / tickets con adjuntos de evidencia}.
- **No-regresión de rendimiento:** {resultado anterior consultado en… / comparativa base ejecutada}.

---

*Documento del APB AI Framework. Requiere revisión humana antes de aprobación (draft → candidate).*
