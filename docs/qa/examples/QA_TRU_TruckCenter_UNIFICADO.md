# Plan de Pruebas UNIFICADO — TRU TruckCenter (APB.API.LGP + APB.API.TRU)

> **Borrador generado por IA** (APB AI Framework — apb-qa-test-plan-v1.2.0) — pendiente validación humana. No distribuir sin revisión.
>
> **Fecha de unificación:** 2026-07-02 · **Aplicación:** TruckCenter (DOCKS .NET) · **APIs:** `APB.API.LGP` (control de puertas LPR) + `APB.API.TRU` (web)
>
> Ejemplo canónico de aplicación de [`TEST_PLAN_STANDARD`](../../../context/apb/standards/TEST_PLAN_STANDARD.md).

---

## 0. Método de unificación y procedencia

Este plan **fusiona sin duplicar** tres visiones del plan de pruebas de TruckCenter, conservando
**todas** las pruebas y anotando, para cada una, **quién la propuso** y **de qué origen** (procedencia
múltiple). Fuentes archivadas en [`sources/`](sources/):

| Cód. | Archivo fuente | Herramienta | Origen | Casos |
|---|---|---|---|---|
| **A** | `QA_TRU_TruckCenter_A_rovo-jira.md` | **Rovo** (Atlassian) | Jira (~50 tickets) | 38 |
| **B** | `QA_TRU_TruckCenter_B_rovo-jira-af.md` | **Rovo** | Jira + Análisis Funcional AF v1.1 | 112 |
| **C** | `QA_TRU_TruckCenter_C_copilot-codigo.md` | **GitHub Copilot** | Ingeniería inversa del código | 112 |

**Reconciliación:** B declara en cabecera ser la evolución de A ⇒ **B ⊇ A**. C declara `Fuente base:
ENRIQUECIDO` y reutiliza los 112 IDs de B, añadiendo la clasificación **Tipo**, el estado ejecutable y la
estructura formal. ⇒ **Unión sin duplicados = 112 casos** (`TRU-T01…T112`), enriquecidos con Tipo/estructura
de C y anotados con procedencia. La numeración de A **no** coincide con la de B/C (misma etiqueta, distinta
prueba) — la unión se hizo **por intención**, no por número; ver [§4 Mapeo A→unificado](#4-mapeo-a-unificado).

**Leyenda de la columna «Procedencia»:**
- Herramientas: **`R`** = Rovo · **`C`** = GitHub Copilot.
- Orígenes: **`J`** = Jira (con ticket cuando consta) · **`AF`** = Documentación / Análisis Funcional · **`Cod`** = Código.
- Ejemplo: `R[J:TRANSTE-1513·AF] · C[Cod]` = propuesta por Rovo desde el ticket Jira TRANSTE-1513 y el AF, validada contra código por Copilot.
- **Multiplicidad:** toda prueba lleva ≥1 herramienta y ≥1 origen; la mayoría llevan varios.

**Columna «Desde»:** fecha en que la prueba quedó definida en el plan (2026-06-30 si venía ya de la visión
A/Jira; 2026-07-01 si se añadió en el enriquecimiento AF de B). **«OK func.»:** funcional que aprobó la
prueba (se rellena en validación; `—` = pendiente). **«Estado»:** `Pendiente` hasta su ejecución (ver
[`QA_TRU_TruckCenter_UNIFICADO` en el repo de la app] para resultados de ejecución y evidencias).

---

## 1. Descripción general

**TRU** (Truck Center) gestiona el **control de acceso, registro y seguimiento de camiones** en el parking
del Truck Center de la APB. Integra lecturas automáticas de matrículas (LPR) de cámaras **IKUSI** con un
panel web de gestión de entradas, salidas, asignación a terminales, conductores y empresas.

### 1.1 APIs y endpoints

| API | Función | Endpoint PRE | Endpoint PRO |
|-----|---------|-------------|-------------|
| **APB.API.LGP** | Control de puertas (recepción LPR/IKUSI) | `https://apipre.portdebarcelona.cat/trc/` | `https://api.portdebarcelona.cat/trc/` |
| **APB.API.TRU** | Aplicación web (frontend + backend) | `https://dockspre.portdebarcelona.cat/tru/` | `https://docks.portdebarcelona.cat/tru/` |

> Renombrado abril 2025 (ARQ-2444): `APB.API.TRU.LGP`→`APB.API.LGP`, `APB.API.TRU.TRC`→`APB.API.TRU`.
> Repositorio GitHub: `APB.TRU` (TRANSTE-1527). Autenticación: **Microsoft EntraID** (External ID, 2025).

### 1.2 Arquitectura topológica

```
Cámaras LPR IKUSI (Controlacceso)
   │  JSON {acceso, carril, fecha, lecturasMatricula}
   │  Regla: acceso=24 & carril=90 → ENTRADA · acceso=24 & carril=91 → SALIDA
   ▼
APB.API.LGP (.NET)  ── POST /api/v1/TruckCenter/ControlPuertas ──┐  Permiso: API_CALL_TRU_CONTROL_PUERTAS
   │  Lógica duplicados: si matrícula sin HORA_SORTIDA → cierra anterior (now-1s) + alta nueva
   ▼
Oracle DB: TRUCK_CENTER · PERSONES · CAMIONS · TIPUS_VEHICLE
   ▲
APB.API.TRU (.NET web DOCKS): GRID · Mantenimiento · Lupas (F/J) · Desplegable Terminales ·
   Tabla maestra vehículos · "Salir del Parking" · Exportación Excel · Auth EntraID · Multiidioma (CA)
   │
   ▼  WS ARQ Docks: APPFASES, EVENTOS, MENSAJES, ERRORES, LOGIN_CAS, LOGIN_TOKEN, FASES
```

### 1.3 Modelo de datos (relación de tablas)

- **TRUCK_CENTER** (expedientes): `ID`(PK), `NOMINTERN`, `HORA_ENTRADA`, `HORA_SORTIDA`, `FASE`
  (def. `EN EL PARKING`), `MATRICULA_CAMIO`(FK→CAMIONS), `TERMINAL`/`CONDUCTOR`/`EMPRESA_TRANSPORT`
  (FK→PERSONES), `CONEXIO_ELECTRICITAT`/`ITV`/`MERCADERIES_PERILLOSES` (0/1), `OBSERVACIONS`, + auditoría
  `APB_CREADOR`/`APB_MODIFICADOR`/`APB_CREAT`/`APB_MODIFICAT`.
- **PERSONES** (conductores y empresas): `ID`(PK), `NOMINTERN`, `TIPUS_PERSONA` (**F**=conductor, **J**=empresa),
  `NIF`, `NOM`, `COGNOM1`, `COGNOM2`, `IDUSUARI_SOSTRAT`, `TELEFON`.
- **CAMIONS**: `MATRICULA_CAMIO`(PK), `NOMINTERN`, `TIPUS_VEHICLE`(FK→TIPUS_VEHICLE).
- **TIPUS_VEHICLE** (maestra): 1 Portacontenedores · 2 Portavehículos · 3 Lonas · 4 Cisternas · 5 Bañeras.

### 1.4 Máquina de estados (fases del expediente)

```
[Creación LPR/API o manual Web] → EN EL PARKING → (Salir del Parking | LPR salida | alta duplicado) → FORA DEL PARKING (final)
```

**Regla de duplicados:** al crear (manual o API) con matrícula ya presente sin `HORA_SORTIDA` — vía **Web**:
aviso y confirmación (cierra anterior `now-1s` + alta nueva, o cancela); vía **API/LPR**: cierra anterior y
crea nuevo automáticamente.

### 1.5 Roles EntraID (TRANSTE-1520)

`USER_READ_TRUCK_CENTER` (solo lectura) · `MANAGE_TRUCK_CENTER` (gestión completa) · `USER_TRUCK_CENTER`
(estándar) · `API_CALL_TRU_CONTROL_PUERTAS` (permiso de llamada al WS de control de puertas).

### 1.6 Integraciones

WS ARQ Docks (7 servicios) · WS Listar Usuarios Sòstrat (lupas y terminales) · EntraID SSO · cámaras IKUSI ·
pipelines Jenkins/GitHub. Precondición global: fallo de transacción → **ROLLBACK** + aviso, sin reintentos.

---

## 2. Matriz unificada de pruebas (112 casos)

> `Prio`: Crítica/Alta/Media. `Tipo`: clasificación de la visión formal (C). Estado inicial: `Pendiente`.

### Bloque 1 — API ControlPuertas / Recepción LPR (12)

| ID | Caso | Tipo | Prio | Resultado esperado | Procedencia | Desde | OK func. | Estado |
|----|------|------|------|--------------------|-------------|-------|----------|--------|
| TRU-T01 | Entrada normal con matrícula | Funcional | Crítica | Nuevo registro `EN EL PARKING`, elec=0, ITV=0, HORA_ENTRADA=fecha; evento `TRU_CREACION..._OK` | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T02 | Salida normal con matrícula | Funcional | Crítica | Registro activo → `HORA_SORTIDA`=fecha, `FORA DEL PARKING`; evento `TRU_SALIR_PARKING_OK` | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T03 | Entrada duplicada — camión aún en parking | Funcional | Crítica | Cierra anterior (now-1s) + crea nuevo; dos eventos | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T04 | Salida sin registro previo | Funcional | Alta | Sin error, no modifica datos, sin evento KO | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T05 | Lectura sin matrícula (NOMATRI) | Funcional | Crítica | Evento `TRU_CONTROL_PUERTAS_KO` con texto `Matricula:NOMATRI` | R[J:TRANSTE-1513·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T06 | idCamara 17 dígitos (nuevo formato) | Integración | Alta | La API acepta el parámetro sin error de parsing | R[J:TRANSTE-1522·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T07 | idCamara 8 dígitos (legacy) | Compatibilidad | Alta | Compatibilidad con formato antiguo, sin error | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T08 | Campos no utilizados con valores extremos | Integración | Media | Solo se validan los 4 campos usados; resto ignorado | R[J:TRANSTE-1523·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T09 | JSON malformado | API | Alta | Error HTTP 400 controlado (no 500) | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T10 | Llamada sin permiso `API_CALL_TRU_CONTROL_PUERTAS` | Seguridad | Crítica | Rechazo 401/403 | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T11 | HORA_SORTIDA anterior = now − 1s exacto | Lógica | Alta | El cierre del anterior registra salida con diferencia exacta de 1s | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T12 | Campos de salida de la API | API | Media | Respuesta consistente con la lógica de negocio y el contrato | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |

### Bloque 2 — GRID Principal (14)

| ID | Caso | Tipo | Prio | Resultado esperado | Procedencia | Desde | OK func. | Estado |
|----|------|------|------|--------------------|-------------|-------|----------|--------|
| TRU-T13 | Columnas por defecto visibles | UI | Crítica | 9 columnas en orden: Id, Matrícula, Entrada, Salida, Terminal, Nombre, Apellido1, Apellido2, Empresa | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T14 | Ordenación por defecto | UI | Alta | Registros de más nuevo a más viejo | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T15 | Selector de columnas — campos añadibles | UI | Alta | Aparecen Fase, NIFs, Ids Sòstrat, elec., ITV, Observaciones | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T16 | Columnas auditoría en selector | UI | Alta | APB_CREADOR/MODIFICADOR/CREAT/MODIFICAT disponibles y filtrables | R[J:TRANSTE-1515·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T17 | Filtro por lupa en cada columna | UI | Alta | Filtrado correcto en todas las columnas visibles | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T18 | Botón refresco GRID | UI | Alta | GRID actualizado sin recargar la página completa | R[J:TRANSTE-1511·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T19 | Acción "Salir del Parking" desde GRID | Funcional | Crítica | HORA_SORTIDA=now, fase final; evento `TRU_SALIR_PARKING_OK` | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T20 | "Salir del Parking" sin registro seleccionado | UI | Alta | Acción no disponible o aviso | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T21 | "Salir del Parking" en registro ya FORA | UI | Alta | Acción no permitida | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T22 | Exportar a Excel — todos los campos | Funcional | Alta | Excel con 9 defecto + 10 añadibles + 4 auditoría, datos correctos | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T23 | Exportar a Excel — GRID vacío | Funcional | Media | Excel generado sin error (cabeceras/vacío) | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T24 | Acceso GRID con USER_READ | Permisos | Crítica | Consulta sí; acción "Salir del Parking" no disponible | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T25 | Acceso GRID con MANAGE | Permisos | Crítica | Consulta + acciones de gestión disponibles | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T26 | Pestaña navegador | UI | Media | Título = "Truck Center" (no "Aplicación de Arquitectura APB") | R[J:TRANSTE-1517·AF] · C[Cod] | 2026-06-30 | — | Pendiente |

### Bloque 3 — Mantenimiento / Alta (16)

| ID | Caso | Tipo | Prio | Resultado esperado | Procedencia | Desde | OK func. | Estado |
|----|------|------|------|--------------------|-------------|-------|----------|--------|
| TRU-T27 | Alta mínima (solo obligatorios) | Funcional | Crítica | Registro `EN EL PARKING`, checkboxes 0; evento creación OK | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T28 | Alta completa (todos los campos) | Funcional | Crítica | Registro con todos los datos; verificar cada columna en BD | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T29 | Alta sin matrícula | Validación | Crítica | No permite guardar; error de obligatorio | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T30 | Alta sin tipo vehículo | Validación | Alta | Bloquea guardado | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T31 | Alta sin hora entrada | Validación | Alta | Bloquea guardado | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T32 | Alta duplicado — usuario CONFIRMA | Regla negocio | Crítica | Cierra anterior (now-1s) + crea nuevo | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T33 | Alta duplicado — usuario CANCELA | Regla negocio | Crítica | No crea; mensaje "El registro del camión en el parking no se ha hecho" | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T34 | Matrícula existente en CAMIONS | Integración | Alta | Tipo de vehículo auto-recuperado, editable | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T35 | Matrícula nueva (no en CAMIONS) | Integración | Alta | Tipo vacío a seleccionar; nueva entrada en CAMIONS al guardar | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T36 | Modificar tipo vehículo recuperado | Integración | Alta | Se actualiza expediente y tabla CAMIONS | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T37 | Botón reloj entrada | UI | Media | Hora entrada = hora actual del sistema | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T38 | Checkbox conexión eléctrica | UI | Media | Valor 1/0 en BD según estado | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T39 | Checkbox ITV | UI | Media | Valor 1/0 en BD según estado | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T40 | Checkbox mercancías peligrosas | UI | Media | Valor 1/0 en BD (`MERCADERIES_PERILLOSES`) | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T41 | Observaciones 4000 caracteres | Validación | Media | Se guarda completo sin truncar | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T42 | Rol USER_READ no puede crear | Permisos | Crítica | Botón alta no visible / acción denegada | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |

### Bloque 4 — Mantenimiento / Modificación y Baja (8)

| ID | Caso | Tipo | Prio | Resultado esperado | Procedencia | Desde | OK func. | Estado |
|----|------|------|------|--------------------|-------------|-------|----------|--------|
| TRU-T43 | Modificar registro existente | Funcional | Crítica | Datos actualizados; evento modificación OK | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T44 | Campos solo lectura no editables | UI | Alta | ID, Fase, Empresa (razón social), Ids Sòstrat no editables | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T45 | "Salir del Parking" desde mantenimiento | Funcional | Crítica | HORA_SORTIDA=now, fase final; evento salir OK | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T46 | Botón no visible en FORA DEL PARKING | UI | Alta | Botón oculto para registros cerrados | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T47 | Baja de registro | Funcional | Alta | Registro eliminado; evento correspondiente | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T48 | Modificar con USER_READ | Permisos | Crítica | Modificación denegada; solo consulta | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T49 | Rollback en error transaccional | Integridad | Crítica | ROLLBACK completo; sin cambios parciales persistidos | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T50 | Sin reintento automático tras error | Comportamiento | Alta | No reintenta; el usuario reejecuta manualmente | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |

### Bloque 5 — Lupas / Conductores y Empresas (12)

| ID | Caso | Tipo | Prio | Resultado esperado | Procedencia | Desde | OK func. | Estado |
|----|------|------|------|--------------------|-------------|-------|----------|--------|
| TRU-T51 | Lupa conductores — búsqueda y selección | Integración | Crítica | Recupera NIF, nombre, apellidos, teléfono, ID Sòstrat (tipo F) | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T52 | Lupa conductores — nuevo en PERSONES | Integración | Crítica | Inserta automáticamente como `TIPUS_PERSONA=F` | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T53 | Lupa conductores — ya existente | Integración | Alta | Recupera de PERSONES, no duplica | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T54 | Lupa conductores — filtrado funciona | UI | Crítica | Resultados filtrados correctamente | R[J:TRANSTE-1534·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T55 | Lupa empresas — búsqueda y selección | Integración | Crítica | Recupera NIF, razón social, ID Sòstrat (sin filtro tipo) | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T56 | Lupa empresas — nueva en PERSONES | Integración | Crítica | Inserta como `TIPUS_PERSONA=J` | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T57 | Lupa empresas — ya existente | Integración | Alta | Recupera datos, no duplica | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T58 | Lupa empresas — filtrado funciona | UI | Crítica | Resultados filtrados correctamente | R[J:TRANSTE-1534·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T59 | WS Sòstrat no disponible | Error handling | Alta | Error controlado, sin excepción no manejada | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T60 | Datos duplicados WS usuarios | Integración | Alta | Lista sin duplicados | R[J:SOSO-2075·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T61 | Escritura manual conductor (sin lupa) | Funcional | Media | Permite ingreso manual, datos guardados | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T62 | Escritura manual empresa (sin lupa) | Funcional | Media | Permite ingreso manual | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |

### Bloque 6 — Desplegable Terminales (8)

| ID | Caso | Tipo | Prio | Resultado esperado | Procedencia | Desde | OK func. | Estado |
|----|------|------|------|--------------------|-------------|-------|----------|--------|
| TRU-T63 | Desplegable solo actividad TU | UI | Crítica | Solo usuarios con actividad TU (no todos) | R[J:TRANSTE-1509·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T64 | Desplegable no bloquea página | Rendimiento | Crítica | Página responde con fluidez, sin bloqueo | R[J:TRANSTE-1509·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T65 | Asignar PORTCEMENT SA | Funcional | Alta | Asignación correcta, guardado OK | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T66 | Asignar APM TERMINALS | Funcional | Alta | Asignación correcta | R[J:TRANSTE-1510·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T67 | Asignar GRIMALDI | Funcional | Alta | Asignación correcta | R[J:TRANSTE-1510·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T68 | Asignar AUTOTERMINAL SA | Funcional | Alta | Asignación correcta | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T69 | Asignar cada una de las 13 terminales | Funcional | Alta | Todas asignables sin error | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T70 | Desplegable sin servicio Sòstrat | Error handling | Media | Fallo manejado sin bloquear interfaz | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |

### Bloque 7 — Tabla Maestra / Tipos de Vehículo (6)

| ID | Caso | Tipo | Prio | Resultado esperado | Procedencia | Desde | OK func. | Estado |
|----|------|------|------|--------------------|-------------|-------|----------|--------|
| TRU-T71 | GRID tipos vehículo — 5 registros iniciales | Datos | Alta | Portacontenedores, Portavehículos, Lonas, Cisternas, Bañeras | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T72 | Alta nuevo tipo vehículo | Funcional | Alta | Nuevo tipo visible en GRID y desplegable | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T73 | Modificar tipo existente | Funcional | Media | Descripción actualizada | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T74 | Eliminar tipo sin dependencias | Funcional | Media | Eliminado sin error | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T75 | Eliminar tipo con dependencias | Integridad | Alta | Impide eliminación por integridad referencial | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T76 | USER_READ no puede modificar maestro | Permisos | Alta | Solo consulta permitida | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |

### Bloque 8 — Autenticación y Permisos EntraID (10)

| ID | Caso | Tipo | Prio | Resultado esperado | Procedencia | Desde | OK func. | Estado |
|----|------|------|------|--------------------|-------------|-------|----------|--------|
| TRU-T77 | Login EntraID exitoso | Autenticación | Crítica | Acceso según rol asignado | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T78 | Rol USER_READ — solo lectura completa | Permisos | Crítica | Ver GRID + consultar; sin alta/baja/mod/salir | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T79 | Rol MANAGE — gestión completa | Permisos | Crítica | Alta, baja, mod, asignar terminal, salir, maestros | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T80 | Rol USER — usuario estándar | Permisos | Alta | Acceso conforme al perfil estándar | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T81 | Sin rol TRU | Autorización | Crítica | Acceso denegado, sin menú TRU | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T82 | Token expirado | Seguridad | Alta | Redirección a login EntraID | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T83 | Idioma predeterminado catalán | Internacionalización | Media | Interfaz en catalán para usuario sin preferencia | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T84 | Cambio de idioma en perfil | Internacionalización | Media | Interfaz en idioma seleccionado | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T85 | AppRegistration External ID configurada | Configuración | Alta | AppRegistration TRU correcta en External ID | R[AF·J:ARQ-2157] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T86 | Tokens correctos tras renombrado API | Integración | Alta | Tokens apuntan a la app TRU correcta | R[AF·J:TRANSTE-1527] · C[Cod] | 2026-07-01 | — | Pendiente |

### Bloque 9 — Eventos de Auditoría (8)

| ID | Caso | Tipo | Prio | Resultado esperado | Procedencia | Desde | OK func. | Estado |
|----|------|------|------|--------------------|-------------|-------|----------|--------|
| TRU-T87 | Evento creación OK | Auditoría | Crítica | `TRU_CREACION_TRUCK_CENTER_OK` con ID en eventos dominio TRU | R[AF·J:TRANSTE-1524] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T88 | Evento creación KO | Auditoría | Alta | `TRU_CREACION_TRUCK_CENTER_KO` ante error | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T89 | Evento modificación OK | Auditoría | Alta | `TRU_MODIFICACION_TRUCK_CENTER_OK` | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T90 | Evento modificación KO | Auditoría | Alta | `TRU_MODIFICACION_TRUCK_CENTER_KO` | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T91 | Evento control puertas OK | Auditoría | Crítica | `TRU_CONTROL_PUERTAS_OK` con tarjeta/acceso/carril/fecha/matrícula | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T92 | Evento control puertas KO | Auditoría | Alta | `TRU_CONTROL_PUERTAS_KO` con NOMATRI | R[J:TRANSTE-1513·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T93 | Evento salir parking OK | Auditoría | Alta | `TRU_SALIR_PARKING_OK` con matrícula e ID | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T94 | Eventos visibles en dominio TRU | Auditoría | Alta | En sección TRU propia, no en pantalla ARQ genérica | R[J:TRANSTE-1524·AF] · C[Cod] | 2026-06-30 | — | Pendiente |

### Bloque 10 — Integración WS ARQ Docks (6)

| ID | Caso | Tipo | Prio | Resultado esperado | Procedencia | Desde | OK func. | Estado |
|----|------|------|------|--------------------|-------------|-------|----------|--------|
| TRU-T95 | Expediente Docks creado | Integración | Alta | Visible en pantalla común de expedientes Docks | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T96 | Fases expediente correctas | Integración | Alta | Solo `EN EL PARKING` → `FORA DEL PARKING` | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T97 | Menú contextual funcional | Integración | Media | Menú contextual Docks operativo | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T98 | Pantalla errores Docks | Integración | Media | Error visible en pantalla común de errores | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T99 | Mensajes Docks funcionales | Integración | Alta | Aviso de duplicado con el mensaje esperado | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T100 | WS ARQ todos operativos | Integración | Alta | APPFASES/EVENTOS/MENSAJES/ERRORES/LOGIN_CAS/LOGIN_TOKEN/FASES OK | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |

### Bloque 11 — Seguridad y Calidad de Código (6)

| ID | Caso | Tipo | Prio | Resultado esperado | Procedencia | Desde | OK func. | Estado |
|----|------|------|------|--------------------|-------------|-------|----------|--------|
| TRU-T101 | SonarQube sin vulnerabilidades altas | Calidad | Crítica | Sin vulnerabilidades altas | R[J:TRANSTE-1530·AF·Cod] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T102 | No inyección SQL en lupas | Seguridad | Crítica | Input sanitizado, sin efecto en consultas | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T103 | No XSS en observaciones | Seguridad | Crítica | Contenido malicioso no ejecutado | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T104 | No XSS en matrícula | Seguridad | Alta | Input no genera ejecución de script | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T105 | Validación de largo de campos según modelo | Validación | Alta | Rechazo/control de valor fuera de rango, sin error BD | R[AF·Cod] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T106 | HTTPS en todos los endpoints | Seguridad | Alta | PRE y PRO usan HTTPS exclusivamente | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |

### Bloque 12 — Regresión, Despliegue y E2E (6)

| ID | Caso | Tipo | Prio | Resultado esperado | Procedencia | Desde | OK func. | Estado |
|----|------|------|------|--------------------|-------------|-------|----------|--------|
| TRU-T107 | Health check API LGP | Despliegue | Crítica | GET endpoint TRC → 200 OK | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T108 | Health check APP TRU | Despliegue | Crítica | GET endpoint web → 200 OK | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T109 | Nomenclatura APIs post-renombrado | Despliegue | Alta | Se observan `APB.API.LGP` y `APB.API.TRU` (no nombres antiguos) | R[J:ARQ-2444·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T110 | Repositorio APB.TRU | Despliegue | Alta | Repo y pipelines apuntan al nuevo nombre | R[J:TRANSTE-1527·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-T111 | E2E: Entrada LPR → GRID → Terminal → Salida LPR | E2E | Crítica | Registro completo con entrada, terminal, conductor, empresa, salida; todos los eventos | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-T112 | E2E: Alta manual → Modificar → Salir Parking | E2E | Crítica | Flujo completo manual; eventos creación + modificación + salida | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |

---

## 3. Resumen del plan

| Bloque | Descripción | Casos | Crítica | Alta | Media |
|--------|-------------|-------|---------|------|-------|
| 1 | API ControlPuertas — LPR | 12 | 4 | 5 | 3 |
| 2 | GRID Principal | 14 | 4 | 7 | 3 |
| 3 | Mantenimiento — Alta | 16 | 7 | 5 | 4 |
| 4 | Mantenimiento — Modif./Baja | 8 | 4 | 3 | 1 |
| 5 | Lupas | 12 | 6 | 4 | 2 |
| 6 | Desplegable Terminales | 8 | 2 | 5 | 1 |
| 7 | Tabla Maestra Vehículos | 6 | 0 | 4 | 2 |
| 8 | Autenticación EntraID | 10 | 4 | 4 | 2 |
| 9 | Eventos de Auditoría | 8 | 2 | 6 | 0 |
| 10 | Integración WS ARQ | 6 | 0 | 4 | 2 |
| 11 | Seguridad y Calidad | 6 | 3 | 2 | 1 |
| 12 | Regresión/Despliegue/E2E | 6 | 4 | 2 | 0 |
| **TOTAL** | | **112** | **40** | **51** | **21** |

**Procedencia (resumen):** 39 casos con respaldo directo en **Jira** (visión A/Rovo, desde 2026-06-30);
73 añadidos desde el **Análisis Funcional** (visión B/Rovo, desde 2026-07-01); **los 112** validados contra
**código** por GitHub Copilot (visión C). 0 duplicados.

**Automatización (para Fase de ejecución):** por navegador (Playwright/agéntico) → Bloques 2–10 y E2E
(T111/T112); por API HTTP → Bloque 1; manual/otra herramienta (SonarQube, revisión) → Bloque 11 parcial y
despliegue (T107–T110 vía health-check HTTP).

---

## 4. Mapeo A→unificado

Los 38 casos de la visión A (Rovo/Jira, numeración propia `A-T01…A-T38`) se corresponden por **intención**
con los IDs canónicos de este plan:

| A (Jira) | Caso A | → Unificado | | A (Jira) | Caso A | → Unificado |
|---|---|---|---|---|---|---|
| A-T01 | Lectura entrada | TRU-T01 | | A-T20 | Asignar todas terminales | TRU-T69 |
| A-T02 | Lectura salida | TRU-T02 | | A-T21 | Login EntraID | TRU-T77 |
| A-T03 | Lectura sin matrícula | TRU-T05 | | A-T22 | Rol USER_READ | TRU-T78 |
| A-T04 | idCamara 17 díg. | TRU-T06 | | A-T23 | Rol MANAGE | TRU-T79 |
| A-T05 | idCamara 8 díg. | TRU-T07 | | A-T24 | Rol USER | TRU-T80 |
| A-T06 | Campos no usados | TRU-T08 | | A-T25 | Token expirado | TRU-T82 |
| A-T07 | JSON malformado | TRU-T09 | | A-T26 | Sin rol TRU | TRU-T81 |
| A-T08 | Visualizar GRID | TRU-T13 | | A-T27 | Evento entrada | TRU-T91 |
| A-T09 | Columnas auditoría | TRU-T16 | | A-T28 | Evento salida | TRU-T93 |
| A-T10 | Filtro lupa auditoría | TRU-T17 | | A-T29 | Evento KO sin matrícula | TRU-T92 |
| A-T11 | Botón refresco | TRU-T18 | | A-T30 | Vulnerab. SonarQube | TRU-T101 |
| A-T12 | Lupa conductores filtra | TRU-T54 | | A-T31 | No inyección SQL | TRU-T102 |
| A-T13 | Lupa empresas filtra | TRU-T58 | | A-T32 | No XSS en campos | TRU-T103/T104 |
| A-T14 | Desplegable TU | TRU-T63 | | A-T33 | Pestaña navegador | TRU-T26 |
| A-T15 | Desplegable no bloquea | TRU-T64 | | A-T34 | WS usuarios sin duplicados | TRU-T60 |
| A-T16 | Asignar PORTCEMENT | TRU-T65 | | A-T35 | Health check API LGP | TRU-T107 |
| A-T17 | Asignar APM | TRU-T66 | | A-T36 | Health check APP TRU | TRU-T108 |
| A-T18 | Asignar GRIMALDI | TRU-T67 | | A-T37 | Despliegue Jenkins | TRU-T110 (pipelines) |
| A-T19 | Asignar AUTOTERMINAL | TRU-T68 | | A-T38 | Nomenclatura APIs | TRU-T109 |

> Ningún caso de A queda sin correspondencia; A ⊂ B confirmado. La numeración de A no se conserva en el
> plan unificado (colisiona con la de B/C); esta tabla preserva su trazabilidad.

---

## 5. Criterios de entrada / salida

- **Entrada:** entorno PRE accesible y operativo · datos base cargados · servicios/dependencias disponibles
  (WS Sòstrat, WS ARQ, EntraID) · usuarios y roles configurados.
- **Salida:** todos los casos **Crítica** aprobados o aceptados con riesgo justificado · 0 defectos críticos
  sin resolver · evidencia de ejecución documentada y vinculada (ver §6 del estándar) · sin regresión de
  rendimiento respecto a la ejecución anterior.

## 6. Histórico de cambios del plan

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| Unificado 1.0 | 2026-07-02 | APB AI Framework (IA) | Unificación sin duplicados de A (Rovo/Jira, 38), B (Rovo/Jira+AF, 112) y C (Copilot/código, 112) → 112 casos con procedencia múltiple, Tipo y mapeo A→unificado. |

## 7. Aprobados del plan (por cambio)

| Versión | Cambio | Aprobado por (rol) | Fecha |
|---------|--------|--------------------|-------|
| Unificado 1.0 | Creación del plan unificado | _pendiente — QA Lead / Analista Funcional_ | — |

---

*Documento del APB AI Framework. Requiere revisión humana antes de aprobación (draft → candidate).*
