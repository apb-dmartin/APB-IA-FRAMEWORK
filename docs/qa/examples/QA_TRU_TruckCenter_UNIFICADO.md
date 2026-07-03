# Plan de Pruebas UNIFICADO — TRU TruckCenter (APB.API.LGP + APB.API.TRU)

> **Borrador generado por IA** (APB AI Framework — apb-qa-test-plan-v1.2.0) — pendiente validación humana. No distribuir sin revisión.
>
> **Fecha de unificación:** 2026-07-02 (v1.0) · **v1.2 (2026-07-03):** renumeración a ID canónico §3.2 ·
> **v1.5 (2026-07-03):** primera ejecución real en PRE (44 casos, 4 hallazgos — ver [§15](#15-resultados-de-ejecución--sesión-qa-navegador-2026-07-03)) ·
> **v1.6 (2026-07-03, II):** segunda sesión de ejecución en PRE (17 casos adicionales, 3 hallazgos nuevos H5-H7 — ver [§16](#16-resultados-de-ejecución--sesión-qa-navegador-2026-07-03-ii)) ·
> **Aplicación:** TruckCenter (DOCKS .NET) · **APIs:** `APB.API.LGP` (control de puertas LPR) + `APB.API.TRU` (web)
>
> Ejemplo canónico de aplicación de [`TEST_PLAN_STANDARD`](../../../context/apb/standards/TEST_PLAN_STANDARD.md).

---

## 0. Método de unificación y procedencia

Este plan **fusiona sin duplicar** tres visiones del plan de pruebas de TruckCenter, conservando
**absolutamente toda** la información de cada fuente (pruebas **y** contenido narrativo: funcionalidad
detallada, modelo de datos, incidencias históricas, proyectos futuros, documentos de referencia,
checklist y plantilla de ejecución) y anotando, para cada prueba, **quién la propuso** y **de qué origen**
(procedencia múltiple). Fuentes archivadas en [`sources/`](sources/):

| Cód. | Archivo fuente | Herramienta | Origen | Casos |
|---|---|---|---|---|
| **A** | `QA_TRU_TruckCenter_A_rovo-jira.md` | **Rovo** (Atlassian) | Jira (~50 tickets) | 38 |
| **B** | `QA_TRU_TruckCenter_B_rovo-jira-af.md` | **Rovo** | Jira + Análisis Funcional AF v1.1 | 112 |
| **C** | `QA_TRU_TruckCenter_C_copilot-codigo.md` | **GitHub Copilot** | Ingeniería inversa del código | 112 |

**Reconciliación:** B declara en cabecera ser la evolución de A ⇒ **B ⊇ A**. C declara `Fuente base:
ENRIQUECIDO` y reutiliza los 112 IDs de B, añadiendo la clasificación **Tipo**, el estado ejecutable, el
**checklist** y la **plantilla de ejecución**. ⇒ **Unión sin duplicados = 112 casos** (`TRU-T01…T112`),
enriquecidos con Tipo/estructura de C y anotados con procedencia. La numeración de A **no** coincide con la
de B/C (misma etiqueta, distinta prueba) — la unión se hizo **por intención**, no por número; ver
[§7 Mapeo A→unificado](#7-mapeo-aunificado).

**Principio de conservación (norma del framework):** unificar **nunca** elimina información. Todo bloque
presente en cualquiera de las tres fuentes está representado en este documento; lo redundante se funde o se
referencia, pero no se descarta.

**Leyenda de la columna «Procedencia»:**
- Herramientas: **`R`** = Rovo · **`C`** = GitHub Copilot.
- Orígenes: **`J`** = Jira (con ticket cuando consta) · **`AF`** = Documentación / Análisis Funcional · **`Cod`** = Código.
- Ejemplo: `R[J:TRANSTE-1513·AF] · C[Cod]` = propuesta por Rovo desde el ticket Jira TRANSTE-1513 y el AF, validada contra código por Copilot.
- **Multiplicidad:** toda prueba lleva ≥1 herramienta y ≥1 origen; la mayoría llevan varios.

**Columna «Desde»:** fecha en que la prueba quedó definida en el plan (2026-06-30 si venía ya de la visión
A/Jira; 2026-07-01 si se añadió en el enriquecimiento AF de B). **«OK func.»:** funcional que aprobó la
prueba (se rellena en validación; `—` = pendiente). **«Estado»:** `Pendiente` hasta su ejecución (ver el
informe de ejecución en el repo de la app para resultados de ejecución y evidencias).

---

## 1. Descripción general

**TRU** (Truck Center) gestiona el **control de acceso, registro y seguimiento de camiones** en el parking
del Truck Center de la APB. Integra lecturas automáticas de matrículas (LPR) de cámaras **IKUSI** con un
panel web de gestión de entradas, salidas, asignación a terminales, conductores y empresas de transporte.

### 1.1 APIs y endpoints

| API | Función | Endpoint PRE | Endpoint PRO |
|-----|---------|-------------|-------------|
| **APB.API.LGP** | Control de puertas (recepción LPR/IKUSI) | `https://apipre.portdebarcelona.cat/trc/` | `https://api.portdebarcelona.cat/trc/` |
| **APB.API.TRU** | Aplicación web (frontend + backend) | `https://dockspre.portdebarcelona.cat/tru/` | `https://docks.portdebarcelona.cat/tru/` |

> Renombrado abril 2025 (ARQ-2444): `APB.API.TRU.LGP`→`APB.API.LGP`, `APB.API.TRU.TRC`→`APB.API.TRU`.
> Repositorio GitHub: `APB.TRU` (renombrado desde TRU, TRANSTE-1527). Autenticación: **Microsoft EntraID**
> (External ID, migración desde CAS/LDAP en 2025).

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

### 1.3 Integración con ARQ Docks

> TRU se integra en el portal DOCKS siguiendo directrices ARQ.

| Aspecto | Detalle |
|---|---|
| **Pantallas comunes** | Expedientes, eventos, errores, documentos, menú contextual. |
| **WebServices ARQ (7)** | `ARQ_APPFASES` · `ARQ_EVENTOS` · `ARQ_MENSAJES` · `ARQ_ERRORES` · `ARQ_LOGIN_CAS` · `ARQ_LOGIN_TOKEN` · `ARQ_FASES` |
| **Login** | Originalmente CAS/LDAP → migrado a **Microsoft EntraID** (2025). |
| **Multiidioma** | Idioma predeterminado **catalán**, personalizable por usuario en su perfil. |
| **Precondición global** | Si falla una transacción → **ROLLBACK** completo + aviso al usuario, sin reintentos automáticos. |
| **Convención BD** | Aunque las columnas se definan en notación mixta, la implementación es siempre en MAYÚSCULAS. |

### 1.4 Modelo de datos (relación de tablas)

#### 1.4.1 TRUCK_CENTER (tabla principal — expedientes)

| Columna | Tipo | Nulable | Descripción |
|---------|------|---------|-------------|
| `ID` | NUMBER(10) | **PK** | ID del expediente |
| `NOMINTERN` | VARCHAR2(40) | NOT NULL | Identificador único |
| `HORA_ENTRADA` | DATE | NOT NULL | Fecha+hora entrada al parking |
| `HORA_SORTIDA` | DATE | Nullable | Fecha+hora salida del parking |
| `FASE` | VARCHAR2(40) | NOT NULL | Fase expediente. Default: `EN EL PARKING` |
| `MATRICULA_CAMIO` | VARCHAR2(10) | NOT NULL | Matrícula del camión (FK → CAMIONS) |
| `TERMINAL` | NUMBER(10) | Nullable | FK → PERSONES (terminal asignada) |
| `CONDUCTOR` | NUMBER(10) | Nullable | FK → PERSONES (conductor) |
| `EMPRESA_TRANSPORT` | NUMBER(10) | Nullable | FK → PERSONES (empresa transporte) |
| `CONEXIO_ELECTRICITAT` | NUMBER(1) | NOT NULL | 0/1 — conexión eléctrica. Default: 0 |
| `ITV` | NUMBER(1) | NOT NULL | 0/1 — ITV en parking. Default: 0 |
| `MERCADERIES_PERILLOSES` | NUMBER(1) | NOT NULL | 0/1 — mercancías peligrosas. Default: 0 |
| `OBSERVACIONS` | VARCHAR2(4000) | Nullable | Texto libre |
| `APB_CREADOR` | — | Audit | Creador (columna auditoría ARQ) |
| `APB_MODIFICADOR` | — | Audit | Último modificador |
| `APB_CREAT` | — | Audit | Fecha creación |
| `APB_MODIFICAT` | — | Audit | Fecha última modificación |

#### 1.4.2 PERSONES (conductores y empresas)

| Columna | Tipo | Nulable | Descripción |
|---------|------|---------|-------------|
| `ID` | NUMBER(10) | **PK** | ID persona |
| `NOMINTERN` | VARCHAR2(40) | NOT NULL | Identificador único |
| `TIPUS_PERSONA` | VARCHAR2(2) | NOT NULL | **F** = física (conductor), **J** = jurídica (empresa) |
| `NIF` | VARCHAR2(11) | NOT NULL | NIF/CIF |
| `NOM` | VARCHAR2(50) | NOT NULL | Nombre / Razón social |
| `COGNOM1` | VARCHAR2(30) | Nullable | Primer apellido (solo tipo F) |
| `COGNOM2` | VARCHAR2(30) | Nullable | Segundo apellido (solo tipo F) |
| `IDUSUARI_SOSTRAT` | VARCHAR2(6) | Nullable | Código en Sòstrat |
| `TELEFON` | VARCHAR2(30) | Nullable | Teléfono |

#### 1.4.3 CAMIONS (registro de camiones)

| Columna | Tipo | Descripción |
|---------|------|-------------|
| `MATRICULA_CAMIO` | VARCHAR2(10) | **PK** — Matrícula |
| `NOMINTERN` | VARCHAR2(40) | Identificador único. NOT NULL |
| `TIPUS_VEHICLE` | NUMBER(10) | FK → TIPUS_VEHICLE. NOT NULL |

#### 1.4.4 TIPUS_VEHICLE (tabla maestra)

| ID | Descripción |
|----|-------------|
| 1 | Portacontenedores |
| 2 | Portavehículos |
| 3 | Lonas |
| 4 | Cisternas |
| 5 | Bañeras |

> **Nota de ejecución (F5):** en PRE la maestra se observó **multiidioma (CA/ES/EN)**, no un único campo
> `DESCRIPCIO` como indicaba el AF. La visión de código (Copilot) resultó correcta. Ver informe de ejecución.

### 1.5 Máquina de estados (fases del expediente)

```
    ┌──────────────────┐
    ▼                  │  Creación vía LPR (API) o manual (Web)
┌───────────────┐      │
│ EN EL PARKING │──────┘
└──────┬────────┘
       │  Transiciones:
       │   1. Botón "Salir del Parking" (Web) → HORA_SORTIDA = now
       │   2. Lectura LPR salida (acceso=24, carril=91)
       │   3. Alta duplicado confirmado → cierra anterior (HORA_SORTIDA = now − 1s)
       ▼
┌────────────────┐
│ FORA DEL PARKING│  ← Estado final
└────────────────┘
```

**Regla de duplicados (crítica):** al crear (manual o API) con matrícula ya presente sin `HORA_SORTIDA`:
- **Vía Web:** aviso y confirmación → si confirma, cierra anterior (`HORA_SORTIDA = now − 1s`,
  `FASE = FORA DEL PARKING`) y crea nuevo; si cancela, no permite alta.
- **Vía API/LPR:** cierra anterior y crea nuevo automáticamente, sin confirmación del usuario.

### 1.6 Roles EntraID (TRANSTE-1520) y usuario de ejecución

> Matriz de roles necesarios para las pruebas (§9.2). Cada caso de la matriz (§5) declara su **«Rol
> requerido»**. El **usuario concreto** que ejecuta se resuelve por **referencia AKV** o se **proporciona en
> runtime** — **nunca** se escriben credenciales en este documento (`AGENTS.md §3`, `GOVERNANCE.md §5.2`).

| Rol / Permiso | Alcance | Bloques que lo requieren |
|---|---|---|
| `USER_READ_TRUCK_CENTER` | Solo lectura (ver GRID, consultar mantenimiento) | B02, B05, B06, B09 (y lectura en B08) |
| `MANAGE_TRUCK_CENTER` | Gestión completa: alta, baja, modificación, asignar terminal, salir parking, maestros | B03, B04, B07, B10, B12 (y gestión en B08) |
| `USER_TRUCK_CENTER` | Usuario estándar | — |
| `API_CALL_TRU_CONTROL_PUERTAS` | Permite llamar al WS de control de puertas (IKUSI) | B01 |

**Usuario de ejecución:** `AKV://tru-qa-user-{rol}` (por defecto, ejecución autónoma vía `prov-akv-v1.0`) o
login asistido EntraID en runtime (→ `storageState`, no persistido). **Destino de ejecución (§9.1):**
`local` (demo QA-2, login asistido) → `azure-qa` para la ejecución completa (QA-3). B11 es análisis
estático (SonarQube/ZAP): no requiere rol de aplicación.

> Soporte ARQ para creación de AppRegistration en External ID (ARQ-2157). Documento de especificaciones:
> "Cambios en DOCKS para integración con Microsoft EntraID SSO_v1.1".

### 1.7 Integraciones

| Sistema / Servicio | Uso en TRU |
|---|---|
| WS ARQ Docks (7 servicios) | Ver detalle en §1.3 (pantallas comunes, login, auditoría) |
| WS Listar Usuarios Sòstrat | Lupas de conductores/empresas y desplegable de terminales (§2.2.3, §2.2.5) |
| EntraID SSO | Autenticación y roles (§1.6) |
| Cámaras IKUSI | Lectura de matrícula (LPR) para entrada/salida automática (§2.1) |
| Pipelines Jenkins/GitHub | Build y despliegue (§2.6, §5 Bloque B12) |

**Precondición global:** fallo de transacción → **ROLLBACK** + aviso, sin reintentos.

---

## 2. Funcionalidad detallada

> Fusión de A §2 (Rovo/Jira) y B §4 (Rovo/AF). Procedencia global de este apartado: **R[J·AF]**.

### 2.1 API ControlPuertas (APB.API.LGP)

**POST /api/v1/TruckCenter/ControlPuertas** — **Permiso requerido:** `API_CALL_TRU_CONTROL_PUERTAS`

**Parámetros de entrada:**

| Campo | Uso | Descripción |
|-------|-----|-------------|
| `acceso` | ✅ Validado | Puerta del puerto (determina entrada/salida) |
| `carril` | ✅ Validado | Calle de circulación (determina entrada/salida) |
| `fecha` | ✅ Validado | Hora de llegada/salida |
| `lecturasMatricula.matricula` | ✅ Validado | Matrícula del camión |
| `idCamara` | ❌ Ignorado | Cambió de Integer (8 díg.) a Long (17 díg.) — TRANSTE-1522 |
| Resto de campos | ❌ Ignorado | No se validan ni procesan (TRANSTE-1523) |

**Lógica de negocio — determinación entrada/salida:**

| Condición | Resultado |
|---|---|
| `acceso=24 AND carril=90` | **ENTRADA** |
| `acceso=24 AND carril=91` | **SALIDA** |

**Flujos:**

| Flujo | Paso | Acción |
|---|---|---|
| **ENTRADA** | 1 | Buscar en `TRUCK_CENTER` registro con misma matrícula sin `HORA_SORTIDA`. |
| **ENTRADA** | 2 | Si existe → cerrar anterior (`HORA_SORTIDA = now − 1s`, `FASE = FORA DEL PARKING`). |
| **ENTRADA** | 3 | Crear nuevo (`HORA_ENTRADA = fecha_param`, `MATRICULA_CAMIO = matricula_param`, `FASE = EN EL PARKING`, `CONEXIO_ELECTRICITAT = 0`, `ITV = 0`). |
| **SALIDA** | 1 | Buscar registro activo con misma matrícula. |
| **SALIDA** | 2 | Si existe → `HORA_SORTIDA = fecha_param`, `FASE = FORA DEL PARKING`. |

**Casos particulares:**

| Caso | Detalle |
|---|---|
| **Matrícula ausente** (TRANSTE-1513) | Cuando la cámara no detecta matrícula → evento `TRU_CONTROL_PUERTAS_KO` con texto `Control de Acceso OK:Número tarjeta:/Acceso:24/Carril:90/Fecha:29/4/2024 13:14:56/Matricula:NOMATRI`. |
| **Campo idCamara** (TRANSTE-1522) | Cambio de formato 8 (Integer) → 17 (Long) números; aunque no se usa en lógica de negocio, el JSON lo incluye y se ajustó para que el cambio de tamaño no provoque error de parsing. |

### 2.2 Aplicación Web (APB.API.TRU)

#### 2.2.1 GRID Principal

**Columnas por defecto (en este orden):**

| Orden | Columna |
|---|---|
| 1 | Id del Truck Center |
| 2 | Matrícula Camión |
| 3 | Entrada |
| 4 | Salida |
| 5 | Terminal (Nombre) |
| 6 | Conductor Nombre |
| 7 | Conductor Apellido 1 |
| 8 | Conductor Apellido 2 |
| 9 | Empresa Transporte (Razón Social) |

**Columnas añadibles (Selector de Columnas):**

| Campo | Notas |
|-------|-------|
| Fase | Estado del expediente |
| NIF Terminal | NIF de la terminal |
| Id Usuari Terminal | ID Sòstrat terminal |
| NIF Conductor | NIF del conductor |
| Id Usuari Conductor | ID Sòstrat conductor |
| NIF Empresa Transporte | NIF empresa |
| Id Usuari Empresa Transporte | ID Sòstrat empresa |
| Conexión Electricidad | 0/1 |
| ITV | 0/1 |
| Observaciones | Texto libre |
| APB_CREADOR / APB_MODIFICADOR / APB_CREAT / APB_MODIFICAT | Auditoría (TRANSTE-1515), filtrables por lupa |

**Características:**

| Característica | Detalle |
|---|---|
| Ordenación por defecto | Más nuevo a más viejo |
| Exportación Excel | De todos los campos (defecto + añadibles) |
| Botón Refresco | TRANSTE-1511 |
| Acción «Salir del Parking» | Solo con registro seleccionado en fase `EN EL PARKING` → `HORA_SORTIDA = now`, `FASE = FORA DEL PARKING` |
| Filtro por lupa | En todos los campos |

#### 2.2.2 Pantalla de Mantenimiento

| Campo | Tipo | Obligatorio | Editable | Detalle |
|-------|------|-------------|----------|---------|
| ID | Numérico | Auto | Solo lectura | PK expediente |
| Matrícula Camión | Texto(10) | ✅ | Sí | Si existe en CAMIONS → recupera tipo vehículo |
| Fase | Texto | Auto | Solo lectura | `EN EL PARKING` / `FORA DEL PARKING` |
| Tipo de Vehículo | Desplegable | ✅ | Sí | Valores de TIPUS_VEHICLE (5 tipos); auto-recuperado si matrícula existe |
| Hora Entrada | Fecha+Hora | ✅ | Sí | Botón reloj para poner hora actual |
| Hora Salida | Fecha+Hora | No | Sí | Se rellena con "Salir del Parking" |
| Terminal | Desplegable | No | Sí | WS Sòstrat, actividad TU |
| NIF Conductor | Texto(11) | No | Sí | Lupa → WS Listar Usuarios Sòstrat (tipo F) |
| Nombre Conductor | Texto(50) | No | Sí | Recuperado de lupa o manual |
| Apellido 1 Conductor | Texto(30) | No | Sí | Recuperado de lupa o manual |
| Apellido 2 Conductor | Texto(30) | No | Sí | Recuperado de lupa o manual |
| Teléfono Conductor | Texto(30) | No | Sí | Recuperado de lupa o manual |
| NIF Empresa Transporte | Texto(11) | No | Sí | Lupa → WS Listar Usuarios Sòstrat (sin filtro) |
| Empresa Transporte | Texto | No | Solo lectura | Razón social de tabla PERSONES |
| Conexión Electricidad | Checkbox | No | Sí | Default: 0 |
| ITV | Checkbox | No | Sí | Default: 0 |
| Mercancías Peligrosas | Checkbox | No | Sí | Default: 0 |
| Observaciones | Texto(4000) | No | Sí | Texto libre |
| Id Usuario Conductor | Numérico | Auto | Solo lectura | PK en Sòstrat |
| Id Usuario Transporte | Numérico | Auto | Solo lectura | PK en Sòstrat |

**Botón "Salir del Parking":** solo visible en fase `EN EL PARKING`. **Botón Reloj Entrada:** pone
fecha/hora actual como hora de entrada.

#### 2.2.3 Lupas de búsqueda

| Lupa | Fuente | Filtro | Persistencia |
|------|--------|--------|-------------|
| **Conductores** | WS Listar Usuarios Sòstrat | Tipo Persona = **F** | Si no existe en PERSONES → inserta como tipo F |
| **Empresas** | WS Listar Usuarios Sòstrat | Sin filtro de tipo | Si no existe en PERSONES → inserta como tipo J |

Al seleccionar conductor: recupera NIF, nombre, apellidos, teléfono, ID Sòstrat. Al seleccionar empresa:
recupera NIF, razón social, ID Sòstrat. **Bug corregido TRANSTE-1534:** las lupas no filtraban datos.

#### 2.2.4 Tabla Maestra — Tipos de Vehículo

Pantalla CRUD con GRID + Mantenimiento. Campo descripción (obligatorio). 5 valores predefinidos:
Portacontenedores, Portavehículos, Lonas, Cisternas, Bañeras.

#### 2.2.5 Desplegable de Terminales

Solo muestra usuarios con actividad **TU** (no todos). **Bug TRANSTE-1509:** el desplegable cargaba TODOS
los usuarios → bloqueaba la página. **Bug TRANSTE-1510:** error al asignar ciertas terminales (APM,
GRIMALDI…).

#### 2.2.6 Terminales registradas (13)

| # | Terminal | Notas |
|---|----------|-------|
| 1 | PORTCEMENT SA | |
| 2 | TRANSPORTES PORTUARIOS SA | |
| 3 | AUTOTERMINAL SA | |
| 4 | TERMINAL CATALUNYA SA | |
| 5 | BUNGE IBERICA SA | |
| 6 | APM TERMINALS BARCELONA, S.L.U. | Fix TRANSTE-1510 |
| 7 | BALEARIA EUROLINEAS MARTITIMAS SA | |
| 8 | TERMINAL FERRY BARCELONA SRLU | |
| 9 | CARGILL SLU | |
| 10 | AUTORITAT PORTUARIA DE BARCELONA | |
| 11 | GRIMALDI TERMINAL BARCELONA SL | Fix TRANSTE-1510 |
| 12 | BARCELONA CONTAINER DEPT SERVICE SL | |
| 13 | DELTA DEPOT BARCELONA SL | |

#### 2.2.7 Pestaña navegador (TRANSTE-1517)

Cambio del literal "Aplicación de Arquitectura APB" a "Truck Center".

### 2.3 Eventos de auditoría funcional

| Evento | Descripción |
|--------|-------------|
| `TRU_CREACION_TRUCK_CENTER_OK` | Se ha creado el truck center con Id = {XXX} |
| `TRU_CREACION_TRUCK_CENTER_KO` | Error al crear el truck center |
| `TRU_MODIFICACION_TRUCK_CENTER_OK` | Se ha actualizado el truck center con id = {XXX} |
| `TRU_MODIFICACION_TRUCK_CENTER_KO` | Error al actualizar el truck center |
| `TRU_CONTROL_PUERTAS_OK` | Control de Acceso OK: Número tarjeta:{X}/Acceso:{X}/Carril:{X}/Fecha:{X}/Matricula:{X} |
| `TRU_CONTROL_PUERTAS_KO` | Control de acceso fallido (incluye "NOMATRI" si sin matrícula) |
| `TRU_SALIR_PARKING_OK` | Se ha registrado la salida del camión con matrícula {XXX} del truck center con Id = {XXX} |
| `TRU_SALIR_PARKING_KO` | Error al registrar salida |

> Los eventos de negocio de TRU se muestran en la sección de **eventos de dominio propia de TRU**, no en la
> pantalla ARQ genérica (TRANSTE-1524).

### 2.4 Mensajes funcionales

| Pantalla | Motivo | Mensaje |
|----------|--------|---------|
| Gestión Truck Center | Aviso camión duplicado | "Se ha detectado que el camión que quiere dar de alta aún está en el parking. ¿Quiere que se marque la anterior ocurrencia para poder dar de alta el actual?" |

### 2.5 Errores funcionales

| Motivo | Error |
|--------|-------|
| Usuario cancela sacar el camión anterior | "El registro del camión en el parking no se ha hecho" |

### 2.6 Refactorización y calidad (contexto Jira)

- **TRANSTE-1527 (refactor):** mejora y alineamiento de código de APIs, cambio de nomenclatura, repositorio
  TRU → APB.TRU, cambio de tokens para apuntar a app TRU. Valoración: 6h.
- **TRANSTE-1530 (SonarQube):** corrección de vulnerabilidades altas detectadas; refactorización para cobertura.
- **SOSO-2075:** bug en WS de usuarios .NET que devolvía datos duplicados; afecta a Truck Center, P33, P51, Escáner.

---

## 3. Incidencias históricas relevantes

> Unión de A §3 (6 tickets) y B §5 (7 tickets, superset). Procedencia: **R[J·AF]**.

| Ticket | Descripción | Causa raíz | Impacto |
|--------|-------------|------------|---------|
| TRANSTE-1534 | Lupas de usuarios no filtran datos | Bug en componente de filtrado | Imposible buscar conductores/empresas |
| TRANSTE-1513 | Llamadas IKUSI sin matrícula generan error no controlado | Falta manejo del caso "sin matrícula" | Eventos LPR no registrados |
| TRANSTE-1522 | idCamara cambió de 8 a 17 dígitos → error parsing | Integer overflow (Long requerido) | API rechaza llamadas IKUSI válidas |
| TRANSTE-1510 | Error al asignar ciertas terminales (APM, GRIMALDI…) | Bug en asignación de terminal | Terminales no asignables en PRO |
| TRANSTE-1509 | Desplegable Terminal bloquea la página | Carga TODOS los usuarios en lugar de solo actividad TU | Página inutilizable |
| SOSO-2075 | WS usuarios devuelve datos duplicados | Bug en servicio de usuarios .NET | Afecta TRU + P33 + P51 + Escáner |
| TRANSTE-1530 | Vulnerabilidades altas en SonarQube | Código inseguro detectado | Riesgo de seguridad |

---

## 4. Proyectos futuros

> Unión de A §2.11 y B §6. Procedencia: **R[J]**.

| Ticket | Proyecto | Alcance |
|--------|----------|---------|
| MISA-1434 | Smart gates y LPR | Nuevo LPR en salida, módulo de explotación MicroStrategy para facturación |
| MISA-1428 | Replicar modelo a otros parkings | Modelo TRU → parkings TIR, FAR, San Beltrán |
| MISA-1381 | DSS Truck Center | Passos per porta, integración con WS SICAD Rodados para facturación por terminal |
| RM-165 | Migración Cloud | Transformación y migración a Azure de Truck Center |
| MISA-1471 | Migración Cloud Docks | Incluye TRU en la migración global de aplicaciones Docks |

---

## 5. Matriz unificada de pruebas (120 casos)

> `Prio`: Crítica/Alta/Media. `Tipo`: clasificación de la visión formal (C). Estado inicial: `Pendiente`.

### Bloque B01 — API ControlPuertas / Recepción LPR (12)

| ID | Legado | Caso | Tipo | Prio | Rol requerido | Resultado esperado | Procedencia | Desde | OK func. | Estado |
| ---- | -------- | ------ | ------ | ------ | --- | -------------------- | ------------- | ------- | ---------- | -------- |
| TRU-B01-T01 | TRU-T01 | Entrada normal con matrícula | Funcional | Crítica | `API_CALL_TRU_CONTROL_PUERTAS` | Nuevo registro `EN EL PARKING`, elec=0, ITV=0, HORA_ENTRADA=fecha; evento `TRU_CREACION..._OK` | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B01-T02 | TRU-T02 | Salida normal con matrícula | Funcional | Crítica | `API_CALL_TRU_CONTROL_PUERTAS` | Registro activo → `HORA_SORTIDA`=fecha, `FORA DEL PARKING`; evento `TRU_SALIR_PARKING_OK` | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B01-T03 | TRU-T03 | Entrada duplicada — camión aún en parking | Funcional | Crítica | `API_CALL_TRU_CONTROL_PUERTAS` | Cierra anterior (now-1s) + crea nuevo; dos eventos | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B01-T04 | TRU-T04 | Salida sin registro previo | Funcional | Alta | `API_CALL_TRU_CONTROL_PUERTAS` | Sin error, no modifica datos, sin evento KO | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B01-T05 | TRU-T05 | Lectura sin matrícula (NOMATRI) | Funcional | Crítica | `API_CALL_TRU_CONTROL_PUERTAS` | Evento `TRU_CONTROL_PUERTAS_KO` con texto `Matricula:NOMATRI` | R[J:TRANSTE-1513·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B01-T06 | TRU-T06 | idCamara 17 dígitos (nuevo formato) | Integración | Alta | `API_CALL_TRU_CONTROL_PUERTAS` | La API acepta el parámetro sin error de parsing | R[J:TRANSTE-1522·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B01-T07 | TRU-T07 | idCamara 8 dígitos (legacy) | Compatibilidad | Alta | `API_CALL_TRU_CONTROL_PUERTAS` | Compatibilidad con formato antiguo, sin error | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B01-T08 | TRU-T08 | Campos no utilizados con valores extremos | Integración | Media | `API_CALL_TRU_CONTROL_PUERTAS` | Solo se validan los 4 campos usados; resto ignorado | R[J:TRANSTE-1523·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B01-T09 | TRU-T09 | JSON malformado | API | Alta | `API_CALL_TRU_CONTROL_PUERTAS` | Error HTTP 400 controlado (no 500) | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B01-T10 | TRU-T10 | Llamada sin permiso `API_CALL_TRU_CONTROL_PUERTAS` | Seguridad | Crítica | `API_CALL_TRU_CONTROL_PUERTAS` | Rechazo 401/403 | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B01-T11 | TRU-T11 | HORA_SORTIDA anterior = now − 1s exacto | Lógica | Alta | `API_CALL_TRU_CONTROL_PUERTAS` | El cierre del anterior registra salida con diferencia exacta de 1s | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B01-T12 | TRU-T12 | Campos de salida de la API | API | Media | `API_CALL_TRU_CONTROL_PUERTAS` | Respuesta consistente con la lógica de negocio y el contrato | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |

### Bloque B02 — GRID Principal (14)

| ID | Legado | Caso | Tipo | Prio | Rol requerido | Resultado esperado | Procedencia | Desde | OK func. | Estado |
| ---- | -------- | ------ | ------ | ------ | --- | -------------------- | ------------- | ------- | ---------- | -------- |
| TRU-B02-T01 | TRU-T13 | Columnas por defecto visibles | UI | Crítica | `USER_READ_TRUCK_CENTER` | 9 columnas en orden: Id, Matrícula, Entrada, Salida, Terminal, Nombre, Apellido1, Apellido2, Empresa | R[J·AF] · C[Cod] | 2026-06-30 | — | ✅ PASS (2026-07-03) |
| TRU-B02-T02 | TRU-T14 | Ordenación por defecto | UI | Alta | `USER_READ_TRUCK_CENTER` | Registros de más nuevo a más viejo | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03) |
| TRU-B02-T03 | TRU-T15 | Selector de columnas — campos añadibles | UI | Alta | `USER_READ_TRUCK_CENTER` | Aparecen Fase, NIFs, Ids Sòstrat, elec., ITV, Observaciones | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03) |
| TRU-B02-T04 | TRU-T16 | Columnas auditoría en selector | UI | Alta | `USER_READ_TRUCK_CENTER` | APB_CREADOR/MODIFICADOR/CREAT/MODIFICAT disponibles y filtrables | R[J:TRANSTE-1515·AF] · C[Cod] | 2026-06-30 | — | ✅ PASS (2026-07-03) |
| TRU-B02-T05 | TRU-T17 | Filtro por lupa en cada columna | UI | Alta | `USER_READ_TRUCK_CENTER` | Filtrado correcto en todas las columnas visibles | R[J·AF] · C[Cod] | 2026-06-30 | — | ✅ PASS (2026-07-03) |
| TRU-B02-T06 | TRU-T18 | Botón refresco GRID | UI | Alta | `USER_READ_TRUCK_CENTER` | GRID actualizado sin recargar la página completa | R[J:TRANSTE-1511·AF] · C[Cod] | 2026-06-30 | — | ✅ PASS (2026-07-03) |
| TRU-B02-T07 | TRU-T19 | Acción "Salir del Parking" desde GRID | Funcional | Crítica | `USER_READ_TRUCK_CENTER` | HORA_SORTIDA=now, fase final; evento `TRU_SALIR_PARKING_OK` | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03) |
| TRU-B02-T08 | TRU-T20 | "Salir del Parking" sin registro seleccionado | UI | Alta | `USER_READ_TRUCK_CENTER` | Acción no disponible o aviso | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03 II) — desplegable de acciones vacío sin selección |
| TRU-B02-T09 | TRU-T21 | "Salir del Parking" en registro ya FORA | UI | Alta | `USER_READ_TRUCK_CENTER` | Acción no permitida | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03 II) — botón no visible tras cierre |
| TRU-B02-T10 | TRU-T22 | Exportar a Excel — todos los campos | Funcional | Alta | `USER_READ_TRUCK_CENTER` | Excel con 9 defecto + 10 añadibles + 4 auditoría, datos correctos | R[AF] · C[Cod] | 2026-07-01 | — | ⚠️ PASS estructural (2026-07-03) — menú con ambas opciones confirmado; descarga no ejecutada |
| TRU-B02-T11 | TRU-T23 | Exportar a Excel — GRID vacío | Funcional | Media | `USER_READ_TRUCK_CENTER` | Excel generado sin error (cabeceras/vacío) | R[AF] · C[Cod] | 2026-07-01 | — | ⚠️ PASS estructural (2026-07-03 II) — exportación sin error con "Sin datos"; descarga no verificada |
| TRU-B02-T12 | TRU-T24 | Acceso GRID con USER_READ | Permisos | Crítica | `USER_READ_TRUCK_CENTER` | Consulta sí; acción "Salir del Parking" no disponible | R[AF] · C[Cod] | 2026-07-01 | — | Bloqueado por alcance (2026-07-03 II) — requiere segundo usuario con rol USER_READ puro, no disponible en la sesión |
| TRU-B02-T13 | TRU-T25 | Acceso GRID con MANAGE | Permisos | Crítica | `USER_READ_TRUCK_CENTER` | Consulta + acciones de gestión disponibles | R[AF] · C[Cod] | 2026-07-01 | — | Bloqueado por alcance (2026-07-03 II) — mismo motivo que T12 |
| TRU-B02-T14 | TRU-T26 | Pestaña navegador | UI | Media | `USER_READ_TRUCK_CENTER` | Título = "Truck Center" (no "Aplicación de Arquitectura APB") | R[J:TRANSTE-1517·AF] · C[Cod] | 2026-06-30 | — | ✅ PASS (2026-07-03) |

### Bloque B03 — Mantenimiento / Alta (16)

| ID | Legado | Caso | Tipo | Prio | Rol requerido | Resultado esperado | Procedencia | Desde | OK func. | Estado |
| ---- | -------- | ------ | ------ | ------ | --- | -------------------- | ------------- | ------- | ---------- | -------- |
| TRU-B03-T01 | TRU-T27 | Alta mínima (solo obligatorios) | Funcional | Crítica | `MANAGE_TRUCK_CENTER` | Registro `EN EL PARKING`, checkboxes 0; evento creación OK | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03) |
| TRU-B03-T02 | TRU-T28 | Alta completa (todos los campos) | Funcional | Crítica | `MANAGE_TRUCK_CENTER` | Registro con todos los datos; verificar cada columna en BD | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03 II) — registro 1497 con todos los campos rellenados |
| TRU-B03-T03 | TRU-T29 | Alta sin matrícula | Validación | Crítica | `MANAGE_TRUCK_CENTER` | No permite guardar; error de obligatorio | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03) |
| TRU-B03-T04 | TRU-T30 | Alta sin tipo vehículo | Validación | Alta | `MANAGE_TRUCK_CENTER` | Bloquea guardado | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03) |
| TRU-B03-T05 | TRU-T31 | Alta sin hora entrada | Validación | Alta | `MANAGE_TRUCK_CENTER` | Bloquea guardado | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03) |
| TRU-B03-T06 | TRU-T32 | Alta duplicado — usuario CONFIRMA | Regla negocio | Crítica | `MANAGE_TRUCK_CENTER` | Cierra anterior (now-1s) + crea nuevo | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03) |
| TRU-B03-T07 | TRU-T33 | Alta duplicado — usuario CANCELA | Regla negocio | Crítica | `MANAGE_TRUCK_CENTER` | No crea; mensaje "El registro del camión en el parking no se ha hecho" | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03) — no crea registro; el mensaje textual de cancelación no se observó en pantalla |
| TRU-B03-T08 | TRU-T34 | Matrícula existente en CAMIONS | Integración | Alta | `MANAGE_TRUCK_CENTER` | Tipo de vehículo auto-recuperado, editable | R[AF] · C[Cod] | 2026-07-01 | — | ⚠️ Hallazgo H3 (2026-07-03) — no se autocompletó al perder el foco; ver §15 |
| TRU-B03-T09 | TRU-T35 | Matrícula nueva (no en CAMIONS) | Integración | Alta | `MANAGE_TRUCK_CENTER` | Tipo vacío a seleccionar; nueva entrada en CAMIONS al guardar | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03 II) — QATEST01/QATEST02, tipo seleccionable manualmente |
| TRU-B03-T10 | TRU-T36 | Modificar tipo vehículo recuperado | Integración | Alta | `MANAGE_TRUCK_CENTER` | Se actualiza expediente y tabla CAMIONS | R[AF] · C[Cod] | 2026-07-01 | — | ⚠️ No concluyente (2026-07-03 II) — el cambio de selección en el desplegable no persistió al guardar; a repetir |
| TRU-B03-T11 | TRU-T37 | Botón reloj entrada | UI | Media | `MANAGE_TRUCK_CENTER` | Hora entrada = hora actual del sistema | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03) |
| TRU-B03-T12 | TRU-T38 | Checkbox conexión eléctrica | UI | Media | `MANAGE_TRUCK_CENTER` | Valor 1/0 en BD según estado | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03 II) |
| TRU-B03-T13 | TRU-T39 | Checkbox ITV | UI | Media | `MANAGE_TRUCK_CENTER` | Valor 1/0 en BD según estado | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03 II) |
| TRU-B03-T14 | TRU-T40 | Checkbox mercancías peligrosas | UI | Media | `MANAGE_TRUCK_CENTER` | Valor 1/0 en BD (`MERCADERIES_PERILLOSES`) | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B03-T15 | TRU-T41 | Observaciones 4000 caracteres | Validación | Media | `MANAGE_TRUCK_CENTER` | Se guarda completo sin truncar | R[AF] · C[Cod] | 2026-07-01 | — | ⚠️ PASS parcial (2026-07-03 II) — texto corto se guarda correctamente; no se probó el límite exacto de 4000 caracteres |
| TRU-B03-T16 | TRU-T42 | Rol USER_READ no puede crear | Permisos | Crítica | `MANAGE_TRUCK_CENTER` | Botón alta no visible / acción denegada | R[AF] · C[Cod] | 2026-07-01 | — | Bloqueado por alcance (2026-07-03 II) — requiere segundo usuario USER_READ |

### Bloque B04 — Mantenimiento / Modificación y Baja (8)

| ID | Legado | Caso | Tipo | Prio | Rol requerido | Resultado esperado | Procedencia | Desde | OK func. | Estado |
| ---- | -------- | ------ | ------ | ------ | --- | -------------------- | ------------- | ------- | ---------- | -------- |
| TRU-B04-T01 | TRU-T43 | Modificar registro existente | Funcional | Crítica | `MANAGE_TRUCK_CENTER` | Datos actualizados; evento modificación OK | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03) |
| TRU-B04-T02 | TRU-T44 | Campos solo lectura no editables | UI | Alta | `MANAGE_TRUCK_CENTER` | ID, Fase, Empresa (razón social), Ids Sòstrat no editables | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03) |
| TRU-B04-T03 | TRU-T45 | "Salir del Parking" desde mantenimiento | Funcional | Crítica | `MANAGE_TRUCK_CENTER` | HORA_SORTIDA=now, fase final; evento salir OK | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03) |
| TRU-B04-T04 | TRU-T46 | Botón no visible en FORA DEL PARKING | UI | Alta | `MANAGE_TRUCK_CENTER` | Botón oculto para registros cerrados | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03) |
| TRU-B04-T05 | TRU-T47 | Baja de registro | Funcional | Alta | `MANAGE_TRUCK_CENTER` | Registro eliminado; evento correspondiente | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03) |
| TRU-B04-T06 | TRU-T48 | Modificar con USER_READ | Permisos | Crítica | `MANAGE_TRUCK_CENTER` | Modificación denegada; solo consulta | R[AF] · C[Cod] | 2026-07-01 | — | Bloqueado por alcance (2026-07-03 II) — requiere segundo usuario USER_READ |
| TRU-B04-T07 | TRU-T49 | Rollback en error transaccional | Integridad | Crítica | `MANAGE_TRUCK_CENTER` | ROLLBACK completo; sin cambios parciales persistidos | R[AF] · C[Cod] | 2026-07-01 | — | No ejecutable desde navegador (2026-07-03 II) — requiere inyección de fallo en backend/BD |
| TRU-B04-T08 | TRU-T50 | Sin reintento automático tras error | Comportamiento | Alta | `MANAGE_TRUCK_CENTER` | No reintenta; el usuario reejecuta manualmente | R[AF] · C[Cod] | 2026-07-01 | — | No ejecutable desde navegador (2026-07-03 II) — mismo motivo que T07 |

### Bloque B05 — Lupas / Conductores y Empresas (12)

| ID | Legado | Caso | Tipo | Prio | Rol requerido | Resultado esperado | Procedencia | Desde | OK func. | Estado |
| ---- | -------- | ------ | ------ | ------ | --- | -------------------- | ------------- | ------- | ---------- | -------- |
| TRU-B05-T01 | TRU-T51 | Lupa conductores — búsqueda y selección | Integración | Crítica | `USER_READ_TRUCK_CENTER` | Recupera NIF, nombre, apellidos, teléfono, ID Sòstrat (tipo F) | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03) |
| TRU-B05-T02 | TRU-T52 | Lupa conductores — nuevo en PERSONES | Integración | Crítica | `USER_READ_TRUCK_CENTER` | Inserta automáticamente como `TIPUS_PERSONA=F` | R[AF] · C[Cod] | 2026-07-01 | — | ⚠️ No verificable en UI (2026-07-03 II) — la selección funciona (Id Usuario recuperado) pero el alta en BD no es observable sin acceso directo; ver hallazgo H6 |
| TRU-B05-T03 | TRU-T53 | Lupa conductores — ya existente | Integración | Alta | `USER_READ_TRUCK_CENTER` | Recupera de PERSONES, no duplica | R[AF] · C[Cod] | 2026-07-01 | — | ⚠️ No verificable en UI (2026-07-03 II) — mismo motivo que T02 |
| TRU-B05-T04 | TRU-T54 | Lupa conductores — filtrado funciona | UI | Crítica | `USER_READ_TRUCK_CENTER` | Resultados filtrados correctamente | R[J:TRANSTE-1534·AF] · C[Cod] | 2026-06-30 | — | ✅ PASS (2026-07-03) — filtro NIF redujo 188.242→1 |
| TRU-B05-T05 | TRU-T55 | Lupa empresas — búsqueda y selección | Integración | Crítica | `USER_READ_TRUCK_CENTER` | Recupera NIF, razón social, ID Sòstrat (sin filtro tipo) | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03) |
| TRU-B05-T06 | TRU-T56 | Lupa empresas — nueva en PERSONES | Integración | Crítica | `USER_READ_TRUCK_CENTER` | Inserta como `TIPUS_PERSONA=J` | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B05-T07 | TRU-T57 | Lupa empresas — ya existente | Integración | Alta | `USER_READ_TRUCK_CENTER` | Recupera datos, no duplica | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03) |
| TRU-B05-T08 | TRU-T58 | Lupa empresas — filtrado funciona | UI | Crítica | `USER_READ_TRUCK_CENTER` | Resultados filtrados correctamente | R[J:TRANSTE-1534·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B05-T09 | TRU-T59 | WS Sòstrat no disponible | Error handling | Alta | `USER_READ_TRUCK_CENTER` | Error controlado, sin excepción no manejada | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B05-T10 | TRU-T60 | Datos duplicados WS usuarios | Integración | Alta | `USER_READ_TRUCK_CENTER` | Lista sin duplicados | R[J:SOSO-2075·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B05-T11 | TRU-T61 | Escritura manual conductor (sin lupa) | Funcional | Media | `USER_READ_TRUCK_CENTER` | Permite ingreso manual, datos guardados | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03 II) — NIF y nombre manuales guardados en registro 1497 |
| TRU-B05-T12 | TRU-T62 | Escritura manual empresa (sin lupa) | Funcional | Media | `USER_READ_TRUCK_CENTER` | Permite ingreso manual | R[AF] · C[Cod] | 2026-07-01 | — | 🔴 FAIL — Hallazgo H5 (2026-07-03 II): el sistema **rechaza** un NIF de empresa manual no existente en Sòstrat ("Ese nif no se corresponde con ninguna Empresa de Transporte"); no permite el alta libre que describe §2.2.3/§2.2.5 |

### Bloque B06 — Desplegable Terminales (8)

| ID | Legado | Caso | Tipo | Prio | Rol requerido | Resultado esperado | Procedencia | Desde | OK func. | Estado |
| ---- | -------- | ------ | ------ | ------ | --- | -------------------- | ------------- | ------- | ---------- | -------- |
| TRU-B06-T01 | TRU-T63 | Desplegable solo actividad TU | UI | Crítica | `USER_READ_TRUCK_CENTER` | Solo usuarios con actividad TU (no todos) | R[J:TRANSTE-1509·AF] · C[Cod] | 2026-06-30 | — | ⚠️ PASS con matiz (2026-07-03) — 18 terminales en desplegable vs 13 documentadas; ver §15 |
| TRU-B06-T02 | TRU-T64 | Desplegable no bloquea página | Rendimiento | Crítica | `USER_READ_TRUCK_CENTER` | Página responde con fluidez, sin bloqueo | R[J:TRANSTE-1509·AF] · C[Cod] | 2026-06-30 | — | ✅ PASS (2026-07-03) |
| TRU-B06-T03 | TRU-T65 | Asignar PORTCEMENT SA | Funcional | Alta | `USER_READ_TRUCK_CENTER` | Asignación correcta, guardado OK | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B06-T04 | TRU-T66 | Asignar APM TERMINALS | Funcional | Alta | `USER_READ_TRUCK_CENTER` | Asignación correcta | R[J:TRANSTE-1510·AF] · C[Cod] | 2026-06-30 | — | ✅ PASS (2026-07-03 II) — TRANSTE-1510 confirmado corregido |
| TRU-B06-T05 | TRU-T67 | Asignar GRIMALDI | Funcional | Alta | `USER_READ_TRUCK_CENTER` | Asignación correcta | R[J:TRANSTE-1510·AF] · C[Cod] | 2026-06-30 | — | ⚠️ No concluyente (2026-07-03 II) — la selección en el desplegable no se reflejó como cambio guardable ("No se han detectado cambios"); a repetir con más cuidado en la interacción |
| TRU-B06-T06 | TRU-T68 | Asignar AUTOTERMINAL SA | Funcional | Alta | `USER_READ_TRUCK_CENTER` | Asignación correcta | R[J·AF] · C[Cod] | 2026-06-30 | — | ✅ PASS (2026-07-03) |
| TRU-B06-T07 | TRU-T69 | Asignar cada una de las 13 terminales | Funcional | Alta | `USER_READ_TRUCK_CENTER` | Todas asignables sin error | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B06-T08 | TRU-T70 | Desplegable sin servicio Sòstrat | Error handling | Media | `USER_READ_TRUCK_CENTER` | Fallo manejado sin bloquear interfaz | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |

### Bloque B07 — Tabla Maestra / Tipos de Vehículo (6)

| ID | Legado | Caso | Tipo | Prio | Rol requerido | Resultado esperado | Procedencia | Desde | OK func. | Estado |
| ---- | -------- | ------ | ------ | ------ | --- | -------------------- | ------------- | ------- | ---------- | -------- |
| TRU-B07-T01 | TRU-T71 | GRID tipos vehículo — 5 registros iniciales | Datos | Alta | `MANAGE_TRUCK_CENTER` | Portacontenedores, Portavehículos, Lonas, Cisternas, Bañeras | R[AF] · C[Cod] | 2026-07-01 | — | 🔴 FAIL — Hallazgo H2 (2026-07-03): el maestro real tiene 9 tipos (001-011, salta 006), no 5; ver §15 |
| TRU-B07-T02 | TRU-T72 | Alta nuevo tipo vehículo | Funcional | Alta | `MANAGE_TRUCK_CENTER` | Nuevo tipo visible en GRID y desplegable | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03 II) — código 012 creado, multiidioma CA/ES/EN confirmado |
| TRU-B07-T03 | TRU-T73 | Modificar tipo existente | Funcional | Media | `MANAGE_TRUCK_CENTER` | Descripción actualizada | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03 II) |
| TRU-B07-T04 | TRU-T74 | Eliminar tipo sin dependencias | Funcional | Media | `MANAGE_TRUCK_CENTER` | Eliminado sin error | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03 II) — eliminado el tipo de prueba 012 sin dependencias, sin error |
| TRU-B07-T05 | TRU-T75 | Eliminar tipo con dependencias | Integridad | Alta | `MANAGE_TRUCK_CENTER` | Impide eliminación por integridad referencial | R[AF] · C[Cod] | 2026-07-01 | — | 🔴 FAIL — Hallazgo H1 CRÍTICO (2026-07-03): se eliminó "Cisterna" sin bloqueo pese a 4 expedientes dependientes; ver §15 |
| TRU-B07-T06 | TRU-T76 | USER_READ no puede modificar maestro | Permisos | Alta | `MANAGE_TRUCK_CENTER` | Solo consulta permitida | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |

### Bloque B08 — Autenticación y Permisos EntraID (10)

| ID | Legado | Caso | Tipo | Prio | Rol requerido | Resultado esperado | Procedencia | Desde | OK func. | Estado |
| ---- | -------- | ------ | ------ | ------ | --- | -------------------- | ------------- | ------- | ---------- | -------- |
| TRU-B08-T01 | TRU-T77 | Login EntraID exitoso | Autenticación | Crítica | `USER_READ` / `MANAGE` | Acceso según rol asignado | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B08-T02 | TRU-T78 | Rol USER_READ — solo lectura completa | Permisos | Crítica | `USER_READ` / `MANAGE` | Ver GRID + consultar; sin alta/baja/mod/salir | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B08-T03 | TRU-T79 | Rol MANAGE — gestión completa | Permisos | Crítica | `USER_READ` / `MANAGE` | Alta, baja, mod, asignar terminal, salir, maestros | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B08-T04 | TRU-T80 | Rol USER — usuario estándar | Permisos | Alta | `USER_READ` / `MANAGE` | Acceso conforme al perfil estándar | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B08-T05 | TRU-T81 | Sin rol TRU | Autorización | Crítica | `USER_READ` / `MANAGE` | Acceso denegado, sin menú TRU | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B08-T06 | TRU-T82 | Token expirado | Seguridad | Alta | `USER_READ` / `MANAGE` | Redirección a login EntraID | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B08-T07 | TRU-T83 | Idioma predeterminado catalán | Internacionalización | Media | `USER_READ` / `MANAGE` | Interfaz en catalán para usuario sin preferencia | R[AF] · C[Cod] | 2026-07-01 | — | Bloqueado por alcance (2026-07-03 II) — el usuario de la sesión ya tiene preferencia de idioma configurada (Castellano); requiere usuario nuevo sin perfil |
| TRU-B08-T08 | TRU-T84 | Cambio de idioma en perfil | Internacionalización | Media | `USER_READ` / `MANAGE` | Interfaz en idioma seleccionado | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03 II) — cambio a Català aplicado en toda la interfaz (menú, cabecera, etiquetas) |
| TRU-B08-T09 | TRU-T85 | AppRegistration External ID configurada | Configuración | Alta | `USER_READ` / `MANAGE` | AppRegistration TRU correcta en External ID | R[AF·J:ARQ-2157] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B08-T10 | TRU-T86 | Tokens correctos tras renombrado API | Integración | Alta | `USER_READ` / `MANAGE` | Tokens apuntan a la app TRU correcta | R[AF·J:TRANSTE-1527] · C[Cod] | 2026-07-01 | — | Pendiente |

### Bloque B09 — Eventos de Auditoría (8)

| ID | Legado | Caso | Tipo | Prio | Rol requerido | Resultado esperado | Procedencia | Desde | OK func. | Estado |
| ---- | -------- | ------ | ------ | ------ | --- | -------------------- | ------------- | ------- | ---------- | -------- |
| TRU-B09-T01 | TRU-T87 | Evento creación OK | Auditoría | Crítica | `USER_READ_TRUCK_CENTER` | `TRU_CREACION_TRUCK_CENTER_OK` con ID en eventos dominio TRU | R[AF·J:TRANSTE-1524] · C[Cod] | 2026-07-01 | — | Bloqueado (2026-07-03 II) — "Auditoría de procesos" ahora visible en el menú pero sigue devolviendo `Forbidden` con este rol; H4 persiste |
| TRU-B09-T02 | TRU-T88 | Evento creación KO | Auditoría | Alta | `USER_READ_TRUCK_CENTER` | `TRU_CREACION_TRUCK_CENTER_KO` ante error | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B09-T03 | TRU-T89 | Evento modificación OK | Auditoría | Alta | `USER_READ_TRUCK_CENTER` | `TRU_MODIFICACION_TRUCK_CENTER_OK` | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B09-T04 | TRU-T90 | Evento modificación KO | Auditoría | Alta | `USER_READ_TRUCK_CENTER` | `TRU_MODIFICACION_TRUCK_CENTER_KO` | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B09-T05 | TRU-T91 | Evento control puertas OK | Auditoría | Crítica | `USER_READ_TRUCK_CENTER` | `TRU_CONTROL_PUERTAS_OK` con tarjeta/acceso/carril/fecha/matrícula | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B09-T06 | TRU-T92 | Evento control puertas KO | Auditoría | Alta | `USER_READ_TRUCK_CENTER` | `TRU_CONTROL_PUERTAS_KO` con NOMATRI | R[J:TRANSTE-1513·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B09-T07 | TRU-T93 | Evento salir parking OK | Auditoría | Alta | `USER_READ_TRUCK_CENTER` | `TRU_SALIR_PARKING_OK` con matrícula e ID | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B09-T08 | TRU-T94 | Eventos visibles en dominio TRU | Auditoría | Alta | `USER_READ_TRUCK_CENTER` | En sección TRU propia, no en pantalla ARQ genérica | R[J:TRANSTE-1524·AF] · C[Cod] | 2026-06-30 | — | Pendiente |

### Bloque B10 — Integración WS ARQ Docks (6)

| ID | Legado | Caso | Tipo | Prio | Rol requerido | Resultado esperado | Procedencia | Desde | OK func. | Estado |
| ---- | -------- | ------ | ------ | ------ | --- | -------------------- | ------------- | ------- | ---------- | -------- |
| TRU-B10-T01 | TRU-T95 | Expediente Docks creado | Integración | Alta | `MANAGE_TRUCK_CENTER` | Visible en pantalla común de expedientes Docks | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B10-T02 | TRU-T96 | Fases expediente correctas | Integración | Alta | `MANAGE_TRUCK_CENTER` | Solo `EN EL PARKING` → `FORA DEL PARKING` | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B10-T03 | TRU-T97 | Menú contextual funcional | Integración | Media | `MANAGE_TRUCK_CENTER` | Menú contextual Docks operativo | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B10-T04 | TRU-T98 | Pantalla errores Docks | Integración | Media | `MANAGE_TRUCK_CENTER` | Error visible en pantalla común de errores | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B10-T05 | TRU-T99 | Mensajes Docks funcionales | Integración | Alta | `MANAGE_TRUCK_CENTER` | Aviso de duplicado con el mensaje esperado | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B10-T06 | TRU-T100 | WS ARQ todos operativos | Integración | Alta | `MANAGE_TRUCK_CENTER` | APPFASES/EVENTOS/MENSAJES/ERRORES/LOGIN_CAS/LOGIN_TOKEN/FASES OK | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |

### Bloque B11 — Seguridad y Calidad de Código (6)

| ID | Legado | Caso | Tipo | Prio | Rol requerido | Resultado esperado | Procedencia | Desde | OK func. | Estado |
| ---- | -------- | ------ | ------ | ------ | --- | -------------------- | ------------- | ------- | ---------- | -------- |
| TRU-B11-T01 | TRU-T101 | SonarQube sin vulnerabilidades altas | Calidad | Crítica | N/A (análisis estático) | Sin vulnerabilidades altas | R[J:TRANSTE-1530·AF·Cod] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B11-T02 | TRU-T102 | No inyección SQL en lupas | Seguridad | Crítica | N/A (análisis estático) | Input sanitizado, sin efecto en consultas | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B11-T03 | TRU-T103 | No XSS en observaciones | Seguridad | Crítica | N/A (análisis estático) | Contenido malicioso no ejecutado | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B11-T04 | TRU-T104 | No XSS en matrícula | Seguridad | Alta | N/A (análisis estático) | Input no genera ejecución de script | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B11-T05 | TRU-T105 | Validación de largo de campos según modelo | Validación | Alta | N/A (análisis estático) | Rechazo/control de valor fuera de rango, sin error BD | R[AF·Cod] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B11-T06 | TRU-T106 | HTTPS en todos los endpoints | Seguridad | Alta | N/A (análisis estático) | PRE y PRO usan HTTPS exclusivamente | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |

### Bloque B12 — Regresión, Despliegue y E2E (6)

| ID | Legado | Caso | Tipo | Prio | Rol requerido | Resultado esperado | Procedencia | Desde | OK func. | Estado |
| ---- | -------- | ------ | ------ | ------ | --- | -------------------- | ------------- | ------- | ---------- | -------- |
| TRU-B12-T01 | TRU-T107 | Health check API LGP | Despliegue | Crítica | `MANAGE_TRUCK_CENTER` | GET endpoint TRC → 200 OK | R[J·AF] · C[Cod] | 2026-06-30 | — | ✅ PASS (2026-07-03 II) — `https://apipre.portdebarcelona.cat/trc/` responde 200 OK (Swagger UI) |
| TRU-B12-T02 | TRU-T108 | Health check APP TRU | Despliegue | Crítica | `MANAGE_TRUCK_CENTER` | GET endpoint web → 200 OK | R[J·AF] · C[Cod] | 2026-06-30 | — | ✅ PASS (2026-07-03 II) — `https://dockspre.portdebarcelona.cat/tru/` responde 200 OK |
| TRU-B12-T03 | TRU-T109 | Nomenclatura APIs post-renombrado | Despliegue | Alta | `MANAGE_TRUCK_CENTER` | Se observan `APB.API.LGP` y `APB.API.TRU` (no nombres antiguos) | R[J:ARQ-2444·AF] · C[Cod] | 2026-06-30 | — | 🔴 FAIL — Hallazgo H7 (2026-07-03 II): el Swagger del endpoint `/trc/` (que debería ser `APB.API.LGP` tras ARQ-2444) muestra el título **"APB.API.TRU"** — posible resto de nomenclatura antigua sin actualizar |
| TRU-B12-T04 | TRU-T110 | Repositorio APB.TRU | Despliegue | Alta | `MANAGE_TRUCK_CENTER` | Repo y pipelines apuntan al nuevo nombre | R[J:TRANSTE-1527·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B12-T05 | TRU-T111 | E2E: Entrada LPR → GRID → Terminal → Salida LPR | E2E | Crítica | `MANAGE_TRUCK_CENTER` | Registro completo con entrada, terminal, conductor, empresa, salida; todos los eventos | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B12-T06 | TRU-T112 | E2E: Alta manual → Modificar → Salir Parking | E2E | Crítica | `MANAGE_TRUCK_CENTER` | Flujo completo manual; eventos creación + modificación + salida | R[AF] · C[Cod] | 2026-07-01 | — | ✅ PASS (2026-07-03) — ejecutado íntegro sobre registros 1493 y 1494→1495 |

### Bloque B13 — Rendimiento (k6) (4)

> **Añadido en v1.4 (feedback de Débora):** el plan no incluía pruebas de rendimiento como bloque propio —
> solo un caso aislado en B06 (T64, comprobación manual de fluidez). Estos 4 casos son el diseño de carga
> (`prov-k6-v1.0`, `TEST_PLAN_STANDARD §8`); su **ejecución** requiere el destino `azure-qa`
> (`prov-azure-qa-runtime-v1.0`) o `ci-runner` — **nunca desde el portátil contra PRE/PRO** (§9.1).
> Bloque nuevo, append-only (§3.2): no reordena ni renumera los bloques B01–B12.

| ID | Legado | Caso | Tipo | Prio | Rol requerido | Resultado esperado | Procedencia | Desde | OK func. | Estado |
| ---- | -------- | ------ | ------ | ------ | --- | -------------------- | ------------- | ------- | ---------- | -------- |
| TRU-B13-T01 | — | Carga API ControlPuertas (LPR concurrente) | Rendimiento | Crítica | `API_CALL_TRU_CONTROL_PUERTAS` | p95 < 2000 ms, error < 1 % (`prov-k6`, umbral §8) | R[AF] · C[Cod] | 2026-07-03 | — | Pendiente |
| TRU-B13-T02 | — | Carga consulta GRID Principal con filtros | Rendimiento | Alta | `USER_READ_TRUCK_CENTER` | p95 < 2000 ms, error < 1 % con carga concurrente de lectura | R[AF] · C[Cod] | 2026-07-03 | — | Pendiente |
| TRU-B13-T03 | — | Estrés alta manual concurrente (Mantenimiento) | Rendimiento | Alta | `MANAGE_TRUCK_CENTER` | Sin bloqueos ni condiciones de carrera al crear en paralelo (regla de duplicados §1.5) | R[AF] · C[Cod] | 2026-07-03 | — | Pendiente |
| TRU-B13-T04 | — | No-regresión de rendimiento vs. ejecución anterior | Rendimiento | Alta | N/A (comparativa automatizada) | Sin empeoramiento respecto a la baseline (§8); si no hay baseline, ejecutar versión anterior + nueva | R[AF] · C[Cod] | 2026-07-03 | — | Pendiente |

### Bloque B14 — Pruebas Unitarias (xUnit, repo APB.TRU) (4)

> **Añadido en v1.4 (feedback de Débora):** el plan no representaba pruebas unitarias. Requieren acceso al
> **repo de código `APB.TRU`** (xUnit, .NET) — no disponible en una sesión de navegador — por eso quedan
> `Pendiente` con nota de bloqueo, en vez de omitidas en silencio (principio de conservación §3.1: ningún
> tipo de prueba queda fuera del plan, aunque no sea ejecutable hoy). Objetivo de cobertura: **≥ 80 %**
> (`TEST_PLAN_STANDARD`, tabla de tipos de prueba).

| ID | Legado | Caso | Tipo | Prio | Rol requerido | Resultado esperado | Procedencia | Desde | OK func. | Estado |
| ---- | -------- | ------ | ------ | ------ | --- | -------------------- | ------------- | ------- | ---------- | -------- |
| TRU-B14-T01 | — | Determinación ENTRADA/SALIDA por `acceso`/`carril` | Unitaria | Crítica | N/A (requiere repo APB.TRU) | Devuelve ENTRADA/SALIDA según tabla de condiciones (§2.1) | C[Cod] | 2026-07-03 | — | Pendiente (requiere repo APB.TRU) |
| TRU-B14-T02 | — | Regla de duplicados (cierre autom. + alta nueva) | Unitaria | Crítica | N/A (requiere repo APB.TRU) | Cierra registro anterior (`now-1s`) y crea el nuevo, sin solapamiento (§1.5) | C[Cod] | 2026-07-03 | — | Pendiente (requiere repo APB.TRU) |
| TRU-B14-T03 | — | Validación de campos obligatorios de Mantenimiento | Unitaria | Alta | N/A (requiere repo APB.TRU) | Rechaza alta/modificación sin campos obligatorios (§2.2.2) | C[Cod] | 2026-07-03 | — | Pendiente (requiere repo APB.TRU) |
| TRU-B14-T04 | — | Cobertura de módulo TruckCenter ≥ 80 % | Unitaria | Alta | N/A (requiere repo APB.TRU) | Informe xUnit/coverage ≥ 80 % sobre la lógica de negocio del módulo | C[Cod] | 2026-07-03 | — | Pendiente (requiere repo APB.TRU) |

---

## 6. Resumen del plan

| Bloque | Descripción | Casos | Crítica | Alta | Media |
|--------|-------------|-------|---------|------|-------|
| B01 | API ControlPuertas — LPR | 12 | 4 | 5 | 3 |
| B02 | GRID Principal | 14 | 4 | 7 | 3 |
| B03 | Mantenimiento — Alta | 16 | 7 | 5 | 4 |
| B04 | Mantenimiento — Modif./Baja | 8 | 4 | 3 | 1 |
| B05 | Lupas | 12 | 6 | 4 | 2 |
| B06 | Desplegable Terminales | 8 | 2 | 5 | 1 |
| B07 | Tabla Maestra Vehículos | 6 | 0 | 4 | 2 |
| B08 | Autenticación EntraID | 10 | 4 | 4 | 2 |
| B09 | Eventos de Auditoría | 8 | 2 | 6 | 0 |
| B10 | Integración WS ARQ | 6 | 0 | 4 | 2 |
| B11 | Seguridad y Calidad | 6 | 3 | 2 | 1 |
| B12 | Regresión/Despliegue/E2E | 6 | 4 | 2 | 0 |
| B13 | Rendimiento (k6) | 4 | 2 | 2 | 0 |
| B14 | Pruebas Unitarias (xUnit) | 4 | 2 | 2 | 0 |
| **TOTAL** | | **120** | **44** | **55** | **21** |

**Bloques canónicos (§3.2, append-only — nunca se renumeran, un bloque nuevo siempre es el siguiente número):**
`B01`=API ControlPuertas · `B02`=GRID Principal · `B03`=Mantenimiento/Alta · `B04`=Mantenimiento/Modif.-Baja ·
`B05`=Lupas · `B06`=Desplegable Terminales · `B07`=Tabla Maestra Vehículos · `B08`=Autenticación EntraID ·
`B09`=Eventos de Auditoría · `B10`=Integración WS ARQ · `B11`=Seguridad y Calidad · `B12`=Regresión/Despliegue/E2E ·
`B13`=Rendimiento (k6) · `B14`=Pruebas Unitarias (xUnit).

**Procedencia (resumen):** 39 casos con respaldo directo en **Jira** (visión A/Rovo, desde 2026-06-30);
73 añadidos desde el **Análisis Funcional** (visión B/Rovo, desde 2026-07-01); **los 112** validados contra
**código** por GitHub Copilot (visión C); **8 casos nuevos** (B13/B14, desde 2026-07-03) propuestos para
cubrir rendimiento y unitarias, validados contra la lógica de negocio descrita en el propio plan (`Cod`).
0 duplicados.

**Automatización (para Fase de ejecución):** por navegador (Playwright/agéntico) → Bloques 2–10 y E2E
(T111/T112); por API HTTP → Bloque 1; manual/otra herramienta (SonarQube, revisión) → Bloque 11 parcial y
despliegue (T107–T110 vía health-check HTTP); **por k6 en `azure-qa`/`ci-runner`** → Bloque 13 (§9.1, nunca
desde el portátil); **por xUnit en el repo `APB.TRU`** (fuera de esta sesión de navegador) → Bloque 14.

---

## 7. Mapeo A→unificado

Los 38 casos de la visión A (Rovo/Jira, numeración propia `A-T01…A-T38`) se corresponden por **intención**
con los IDs de este plan. Se muestran ambos: el **ID legado** (numeración plana v1.0/v1.1) y el
**ID canónico** (§3.2 `{APP}-B{NN}-T{NN}`, append-only, vigente desde v1.2):

| A (Jira) | Caso A | ID Legado | ID Canónico |
|---|---|---|---|
| A-T01 | Lectura entrada | TRU-T01 | TRU-B01-T01 |
| A-T02 | Lectura salida | TRU-T02 | TRU-B01-T02 |
| A-T03 | Lectura sin matrícula | TRU-T05 | TRU-B01-T05 |
| A-T04 | idCamara 17 díg. | TRU-T06 | TRU-B01-T06 |
| A-T05 | idCamara 8 díg. | TRU-T07 | TRU-B01-T07 |
| A-T06 | Campos no usados | TRU-T08 | TRU-B01-T08 |
| A-T07 | JSON malformado | TRU-T09 | TRU-B01-T09 |
| A-T08 | Visualizar GRID | TRU-T13 | TRU-B02-T01 |
| A-T09 | Columnas auditoría | TRU-T16 | TRU-B02-T04 |
| A-T10 | Filtro lupa auditoría | TRU-T17 | TRU-B02-T05 |
| A-T11 | Botón refresco | TRU-T18 | TRU-B02-T06 |
| A-T12 | Lupa conductores filtra | TRU-T54 | TRU-B05-T04 |
| A-T13 | Lupa empresas filtra | TRU-T58 | TRU-B05-T08 |
| A-T14 | Desplegable TU | TRU-T63 | TRU-B06-T01 |
| A-T15 | Desplegable no bloquea | TRU-T64 | TRU-B06-T02 |
| A-T16 | Asignar PORTCEMENT | TRU-T65 | TRU-B06-T03 |
| A-T17 | Asignar APM | TRU-T66 | TRU-B06-T04 |
| A-T18 | Asignar GRIMALDI | TRU-T67 | TRU-B06-T05 |
| A-T19 | Asignar AUTOTERMINAL | TRU-T68 | TRU-B06-T06 |
| A-T20 | Asignar todas terminales | TRU-T69 | TRU-B06-T07 |
| A-T21 | Login EntraID | TRU-T77 | TRU-B08-T01 |
| A-T22 | Rol USER_READ | TRU-T78 | TRU-B08-T02 |
| A-T23 | Rol MANAGE | TRU-T79 | TRU-B08-T03 |
| A-T24 | Rol USER | TRU-T80 | TRU-B08-T04 |
| A-T25 | Token expirado | TRU-T82 | TRU-B08-T06 |
| A-T26 | Sin rol TRU | TRU-T81 | TRU-B08-T05 |
| A-T27 | Evento entrada | TRU-T91 | TRU-B09-T05 |
| A-T28 | Evento salida | TRU-T93 | TRU-B09-T07 |
| A-T29 | Evento KO sin matrícula | TRU-T92 | TRU-B09-T06 |
| A-T30 | Vulnerab. SonarQube | TRU-T101 | TRU-B11-T01 |
| A-T31 | No inyección SQL | TRU-T102 | TRU-B11-T02 |
| A-T32 | No XSS en campos | TRU-T103/T104 | TRU-B11-T03/T04 |
| A-T33 | Pestaña navegador | TRU-T26 | TRU-B02-T14 |
| A-T34 | WS usuarios sin duplicados | TRU-T60 | TRU-B05-T10 |
| A-T35 | Health check API LGP | TRU-T107 | TRU-B12-T01 |
| A-T36 | Health check APP TRU | TRU-T108 | TRU-B12-T02 |
| A-T37 | Despliegue Jenkins | TRU-T110 (pipelines) | TRU-B12-T04 |
| A-T38 | Nomenclatura APIs | TRU-T109 | TRU-B12-T03 |

> Ningún caso de A queda sin correspondencia; A ⊂ B confirmado. La numeración de A no se conserva en el
> plan unificado (colisiona con la de B/C); esta tabla preserva su trazabilidad completa (legado + canónico).

---

## 8. Criterios de entrada / salida

- **Entrada:** entorno PRE accesible y operativo · datos base cargados · servicios/dependencias disponibles
  (WS Sòstrat, WS ARQ, EntraID) · usuarios y roles configurados.
- **Salida:** todos los casos **Crítica** aprobados o aceptados con riesgo justificado · 0 defectos críticos
  sin resolver · evidencia de ejecución documentada y vinculada (ver §6 del estándar) · sin regresión de
  rendimiento respecto a la ejecución anterior.

---

## 9. Checklist ejecutable

> Preservado de la visión formal C (Copilot). Marcar `[x]` al ejecutar cada caso. IDs canónicos §3.2.

**Bloque B01 — API ControlPuertas:** ☐ TRU-B01-T01 ☐ T02 ☐ T03 ☐ T04 ☐ T05 ☐ T06 ☐ T07 ☐ T08 ☐ T09 ☐ T10 ☐ T11 ☐ T12
**Bloque B02 — GRID Principal:** ☑ TRU-B02-T01 ☑ T02 ☑ T03 ☑ T04 ☑ T05 ☑ T06 ☑ T07 ☑ T08 ☑ T09 ☑ T10 ☑ T11 ☐ T12 (bloq.) ☐ T13 (bloq.) ☑ T14
**Bloque B03 — Mantenimiento/Alta:** ☑ TRU-B03-T01 ☑ T02 ☑ T03 ☑ T04 ☑ T05 ☑ T06 ☑ T07 ☑ T08 (⚠️ H3) ☑ T09 ☒ T10 (no concluyente) ☑ T11 ☑ T12 ☑ T13 ☐ T14 ☑ T15 (parcial) ☐ T16 (bloq.)
**Bloque B04 — Modif./Baja:** ☑ TRU-B04-T01 ☑ T02 ☑ T03 ☑ T04 ☑ T05 ☐ T06 (bloq.) ☐ T07 (no ejecutable) ☐ T08 (no ejecutable)
**Bloque B05 — Lupas:** ☑ TRU-B05-T01 ☒ T02 (no verificable) ☒ T03 (no verificable) ☑ T04 ☑ T05 ☐ T06 ☑ T07 ☐ T08 ☐ T09 ☐ T10 ☑ T11 ☒ T12 (🔴 H5)
**Bloque B06 — Terminales:** ☑ TRU-B06-T01 (⚠️ nota) ☑ T02 ☐ T03 ☑ T04 ☒ T05 (no concluyente) ☑ T06 ☐ T07 ☐ T08
**Bloque B07 — Tabla Maestra:** ☒ TRU-B07-T01 (🔴 H2) ☑ T02 ☑ T03 ☑ T04 ☒ T05 (🔴 H1) ☐ T06 (bloq.)
**Bloque B08 — Autenticación EntraID:** ☑ TRU-B08-T01 (implícito) ☐ T02 ☐ T03 ☐ T04 ☐ T05 ☐ T06 ☐ T07 (bloq.) ☑ T08 ☐ T09 ☐ T10
**Bloque B09 — Eventos Auditoría:** ☐ TRU-B09-T01 ☐ T02 ☐ T03 ☐ T04 ☐ T05 ☐ T06 ☐ T07 ☐ T08 — *bloqueado: menú "Auditoría de procesos" ya visible pero sigue devolviendo Forbidden con el rol usado (2026-07-03 II, H4 persiste)*
**Bloque B10 — WS ARQ Docks:** ☐ TRU-B10-T01 ☐ T02 ☐ T03 ☐ T04 ☐ T05 ☐ T06 — *no ejecutado en esta sesión*
**Bloque B11 — Seguridad/Calidad:** ☐ TRU-B11-T01 ☐ T02 ☐ T03 ☐ T04 ☐ T05 ☐ T06
**Bloque B12 — Regresión/Despliegue/E2E:** ☑ TRU-B12-T01 ☑ T02 ☒ T03 (🔴 H7) ☐ T04 ☐ T05 ☑ T06
**Bloque B13 — Rendimiento (k6):** ☐ TRU-B13-T01 ☐ T02 ☐ T03 ☐ T04
**Bloque B14 — Unitarias (xUnit):** ☐ TRU-B14-T01 ☐ T02 ☐ T03 ☐ T04

> **Leyenda añadida 2026-07-03:** ☑ = ejecutado PASS · ☒ = ejecutado con hallazgo/FAIL/no concluyente · ☐ = pendiente/bloqueado. Detalle completo en [§15](#15-resultados-de-ejecución--sesión-qa-navegador-2026-07-03) y [§16](#16-resultados-de-ejecución--sesión-qa-navegador-2026-07-03-ii).

---

## 10. Plantilla de ejecución

> Preservada de la visión formal C (Copilot). Se rellena en cada corrida.

- **Fecha de ejecución:**
- **Entorno:** (PRE / PRO)
- **Responsable:**
- **Rol utilizado:** (USER_READ / MANAGE / USER)
- **Resultado general:**
- **Observaciones:**
- **Firma:**

---

## 11. Tickets Jira analizados

> Preservado de A §5 / B §9 (~50 tickets).

TRANSTE-1534, TRANSTE-1530, TRANSTE-1527, TRANSTE-1524, TRANSTE-1523, TRANSTE-1522, TRANSTE-1520,
TRANSTE-1517, TRANSTE-1515, TRANSTE-1513, TRANSTE-1511, TRANSTE-1510, TRANSTE-1509, TRANSTE-1507,
TRANSTE-1506, ARQ-2929, ARQ-2926, ARQ-2795, ARQ-2779, ARQ-2447, ARQ-2444, ARQ-2421, ARQ-2346, ARQ-2315,
ARQ-2238, ARQ-2157, ARQ-1621, ARQ-1619, ARQ-1511, ARQ-1507, ARQ-1336, ARQ-1320, ARQ-1317, ARQ-1166,
ARQ-1162, ARQ-1106, ARQ-1105, ARQ-1087, ARQ-1030, ARQ-927, ARQ-924, PVI-2, RM-165, GS-801, MISA-1567,
MISA-1471, MISA-1434, MISA-1428, MISA-1381, MISA-1346, SOSO-2075

---

## 12. Documentos de referencia

> Preservado de B §10.

| Documento | Versión | Fecha | Fuente |
|-----------|---------|-------|--------|
| AF Truck Center | v1.1 | 03/02/2023 (rev. 22/07/2025) | Análisis Funcional oficial — modelo de datos, reglas de negocio, pantallas, eventos |
| AF Truck Center — Modelo de Datos | — | 01/07/2026 | Diagrama Visio de entidades lógicas |
| Cambios en DOCKS para integración con Microsoft EntraID SSO | v1.1 | — | Especificaciones migración autenticación |
| QA_TRU_TruckCenter_A_rovo-jira.md | — | 2026-06-30 | Visión A (Rovo/Jira, 38 casos) — [`sources/`](sources/) |
| QA_TRU_TruckCenter_B_rovo-jira-af.md | — | 2026-07-01 | Visión B (Rovo/Jira+AF, 112 casos) — [`sources/`](sources/) |
| QA_TRU_TruckCenter_C_copilot-codigo.md | 1.0 | 2026-07-01 | Visión C (Copilot/código, formal) — [`sources/`](sources/) |

---

## 13. Histórico de cambios del plan

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| Unificado 1.0 | 2026-07-02 | APB AI Framework (IA) | Unificación sin duplicados de A (Rovo/Jira, 38), B (Rovo/Jira+AF, 112) y C (Copilot/código, 112) → 112 casos con procedencia múltiple, Tipo y mapeo A→unificado. |
| Unificado 1.1 | 2026-07-02 | APB AI Framework (IA) | **Restauración de contenido:** se reincorpora TODA la información narrativa de las tres fuentes que se había perdido en 1.0 — §2 Funcionalidad detallada (API, GRID, Mantenimiento, lupas, terminales, eventos, mensajes, errores), §1.4 Modelo de datos con tipos/nulabilidad, §3 Incidencias históricas relevantes, §4 Proyectos futuros, §9 Checklist ejecutable, §10 Plantilla de ejecución, §11 Tickets Jira, §12 Documentos de referencia. Unificar ya no elimina información. |
| Unificado 1.2 | 2026-07-03 | APB AI Framework (IA) | **Renumeración a ID canónico (§3.2 `TEST_PLAN_STANDARD` v1.2.0):** los 112 casos pasan de numeración plana (`TRU-T01…T112`) a esquema `TRU-B{NN}-T{NN}` (bloque + secuencia, append-only), conservando el **ID legado** en columna propia de la matriz (§5) para no romper la trazabilidad con `INFORME_EJECUCION_112.md`. §7 Mapeo actualizado con ambos IDs. §9 Checklist con IDs canónicos. Resuelve el problema de correlación plan↔informe al crecer el plan (añadir una prueba a un bloque existente ya no exige renumerar las demás). |
| Unificado 1.3 | 2026-07-03 | APB AI Framework (IA) | **Fase I (`TEST_PLAN_STANDARD` v1.3.0):** §1.6 amplía la matriz de roles con «Bloques que lo requieren» + nota de **usuario de ejecución** (AKV/runtime, sin credenciales en fichero) y **destino de ejecución** (§9.1/§9.2); la matriz de casos (§5) incorpora la columna **«Rol requerido»** con el rol EntraID mínimo por bloque. Sin pérdida de contenido (§3.1): solo se añade información. |
| Unificado 1.4 | 2026-07-03 | APB AI Framework (IA) | **Feedback de Débora (legibilidad + cobertura de tipos de prueba):** (a) **nuevos Bloques B13 — Rendimiento (k6, 4 casos)** y **B14 — Pruebas Unitarias (xUnit, 4 casos)**, append-only (§3.2) — el plan no representaba estos tipos, solo un caso aislado de fluidez en B06; total **112 → 120 casos**; §6 Resumen, §9 Checklist e Histórico actualizados. (b) **Reformateo a tabla** de secciones que mezclaban información en prosa con puntos, difíciles de leer: §1.3 Integración con ARQ Docks, §1.7 Integraciones, §2.1 lógica de negocio ENTRADA/SALIDA y casos particulares, §2.2.1 columnas por defecto y características del GRID. Sin pérdida de contenido (§3.1): mismo contenido, presentación tabular. |
| Unificado 1.5 | 2026-07-03 | APB AI Framework (IA, sesión navegador con Débora) | **Primera ejecución real en PRE con el agente de navegación del framework** (`apb-qa-exploratory-nav-v1.0` + `prov-browser-agent-v1.0`, login EntraID asistido): 44 casos con evidencia directa (lectura y escritura) en B02-B07 y B12-T06; **nueva §15 Resultados de ejecución** con 4 hallazgos (H1 crítico — sin integridad referencial al eliminar Tipo de Vehículo; H2 — maestro de tipos desactualizado en AF/plan; H3 — auto-recuperación de tipo no disparada; H4 — pantalla de Auditoría inaccesible con el rol usado); columna **Estado** de la matriz (§5) y checklist (§9) actualizados para los casos ejecutados. Sin pérdida de contenido (§3.1): solo se añade estado y hallazgos, ninguna prueba se elimina. Evidencia (informe + vídeo) en `QA_TruckCenter_evidencias/030726/` (fuera de este repo). |
| Unificado 1.6 | 2026-07-03 (II) | APB AI Framework (IA, sesión navegador con Débora) | **Segunda sesión de ejecución en PRE** (sesión activa reutilizada, sin nuevo login): 17 casos adicionales ejecutados/actualizados en B02, B03, B05, B06, B07, B08 y B12; **nueva §16 Resultados de ejecución** con 3 hallazgos nuevos (H5 — la lupa de empresa rechaza el alta manual de un NIF no existente en Sòstrat, contradice §2.2.3/§2.2.5; H6 — el campo Nombre Conductor se guarda como "." tras seleccionar desde la lupa, mapeo incorrecto; H7 — el Swagger de `/trc/` (APB.API.LGP) muestra el título "APB.API.TRU", nomenclatura post-renombrado inconsistente) y confirmación en vivo de H1/H2 (9 tipos de vehículo reales, código 004 sigue eliminado) y H4 (Auditoría de procesos ahora visible en menú pero sigue Forbidden). Varios casos quedan bloqueados por alcance (requieren segundo usuario/rol) o no ejecutables desde navegador (rollback transaccional, k6, xUnit) — listados explícitamente en checklist (§9) y §16.3. Evidencia en vídeo solo cubre el bloque inicial (B02-B03) por el límite de 50 fotogramas de la herramienta de captura, sin segmentación posterior — pendiente de mejora en próxima sesión. Sin pérdida de contenido (§3.1). |

## 14. Aprobados del plan (por cambio)

| Versión | Cambio | Aprobado por (rol) | Fecha |
|---------|--------|--------------------|-------|
| Unificado 1.0 | Creación del plan unificado | _pendiente — QA Lead / Analista Funcional_ | — |
| Unificado 1.1 | Restauración de contenido íntegro de las fuentes | _pendiente — QA Lead / Analista Funcional_ | — |
| Unificado 1.2 | Renumeración a ID canónico append-only | _pendiente — QA Lead / Analista Funcional_ | — |
| Unificado 1.3 | Roles + usuario de ejecución + destino de ejecución | _pendiente — QA Lead / Analista Funcional_ | — |
| Unificado 1.4 | Bloques B13/B14 (rendimiento/unitarias) + reformateo a tabla | _pendiente — QA Lead / Analista Funcional_ | — |
| Unificado 1.5 | §15 Resultados de ejecución (sesión navegador 2026-07-03) + hallazgos H1-H4 | _pendiente — QA Lead / Analista Funcional / Arquitectura (revisar H1 con prioridad)_ | — |
| Unificado 1.6 | §16 Resultados de ejecución (sesión navegador 2026-07-03 II) + hallazgos H5-H7 | _pendiente — QA Lead / Analista Funcional / Arquitectura (revisar H5 con prioridad — bloquea B05-T12 y el flujo documentado)_ | — |

---

## 15. Resultados de ejecución — Sesión QA navegador (2026-07-03)

> **Borrador generado por IA** (APB AI Framework — `apb-qa-exploratory-nav-v1.0` + `prov-browser-agent-v1.0`,
> sesión Claude en navegador vía extensión Chrome, login asistido por Débora Martín) — pendiente validación
> humana. Añadido en v1.5 (§3.1 principio de conservación: no se elimina información, solo se añade).

### 15.1 Datos de la ejecución

| Campo | Valor |
|---|---|
| Entorno | PRE (`dockspre.portdebarcelona.cat/tru/`) |
| Responsable / rol | Débora Martín — sesión con permisos de gestión completos sobre Truck Center; **sin acceso** a "Auditoría de procesos" (`Forbidden`) |
| Alcance | B02, B03, B04, B05, B06, B07 (ejecución real con escritura); B08/B10/B12 parcial; B01/B09(directo)/B11/B13/B14 fuera de alcance de esta sesión |
| Evidencia | `QA_TruckCenter_evidencias/030726/` (repo local del framework, fuera de este repo de código — ver `INFORME_EJECUCION_030726.md` y GIF de 50 fotogramas de la sesión) |
| Resultado global | 44 casos con evidencia directa; **2 hallazgos críticos** en B07; resto PASS o bloqueado por alcance (no defecto) |

### 15.2 Hallazgos

**🔴 H1 — CRÍTICO — Sin integridad referencial al eliminar Tipo de Vehículo (`TRU-B07-T05`).** Se eliminó el
tipo "Cisterna" (código 004) desde Tablas Maestras sin ningún aviso ni bloqueo, pese a estar referenciado por
al menos 4 expedientes de Truck Center (IDs 1494, 1493, 1491, 1486). Riesgo de referencias huérfanas
(`TIPUS_VEHICLE` apuntando a un maestro inexistente). **Recomendación:** validación de integridad referencial
(FK o check aplicativo) antes de permitir el borrado.

**🟠 H2 — Tabla Maestra desactualizada respecto al AF/plan (`TRU-B07-T01`).** El plan documenta 5 tipos
iniciales (Portacontenedores, Portavehículos, Lonas, Cisternas, Bañeras); el sistema PRE real tiene **9 tipos**
(códigos 001-005, 007-011 — salta el 006, indicio de otro borrado previo sin control, mismo patrón que H1):
Turismo, Moto, Autocaravana/Furgoneta, Servicios (Limpieza, Basuras, Mantenimiento) y Flota APB no estaban
documentados. **Recomendación:** actualizar AF y §1.4.4/§6 de este plan; investigar el hueco del código 006.

**🟡 H3 — Auto-recuperación de Tipo de Vehículo no se disparó al blur (`TRU-B03-T08`/`TRU-T34`).** Al
reutilizar una matrícula ya existente en `CAMIONS`, el campo Tipo de Vehículo no se autocompletó al perder el
foco; hubo que seleccionarlo manualmente. No confirmado si ocurre en otro punto del ciclo (p. ej. al guardar).
No bloqueante — a validar en próxima sesión.

**🔵 H4 — Pantalla "Auditoría de procesos" inaccesible con el rol usado (relacionado con B08/B09).** Recibió
`Forbidden`. Coherente con control de acceso por permiso específico (no es un defecto), pero impide verificar
directamente los eventos `TRU_*` de B09 en esta sesión; se infieren indirectamente por los mensajes de éxito
de UI ("Se ha creado un registro...", "Se ha actualizado el registro...").

### 15.3 Pendiente para próximas sesiones

1. Corregir H1 (prioridad alta — riesgo ya materializado en PRE).
2. Actualizar AF y este plan con los 9 tipos de vehículo reales (H2).
3. Completar B05 (T09-T12), B06 (resto de terminales, T08), B07 (T02-T04, T06 — con cautela tras H1), B08 y
   B09 completos con un segundo usuario/rol (`USER_READ_TRUCK_CENTER` puro y un usuario con permiso de
   Auditoría).
4. B01 vía llamadas HTTP directas; B11/B13 en `azure-qa`/`ci-runner` (§9.1, nunca desde sesión de navegador
   local); B14 requiere acceso al repo `APB.TRU`.

---

## 16. Resultados de ejecución — Sesión QA navegador (2026-07-03, II)

> **Borrador generado por IA** (APB AI Framework — `apb-qa-exploratory-nav-v1.0` + `prov-browser-agent-v1.0`,
> sesión Claude en navegador vía extensión Chrome, sesión EntraID ya activa — sin nuevo login) — pendiente
> validación humana. Añadido en v1.6 (§3.1 principio de conservación: no se elimina información, solo se añade).

### 16.1 Datos de la ejecución

| Campo | Valor |
|---|---|
| Entorno | PRE (`dockspre.portdebarcelona.cat/tru/` + `apipre.portdebarcelona.cat/trc/`) |
| Responsable / rol | Débora Martín — mismo usuario/rol de gestión completo de la sesión 2026-07-03 (I); sin acceso a "Auditoría de procesos" (persiste `Forbidden`) |
| Alcance | Continuación de casos `Pendiente` ejecutables por navegador en B02, B03, B05, B06, B07, B08 y B12; health-check de B12-T01/T02 vía Swagger/URL directa |
| Evidencia | Vídeo (GIF, 50 fotogramas) solo del bloque inicial B02-B03: `QA_TruckCenter_sesion_030726_bloque1.gif` (descargado en el navegador). El resto de la sesión **no quedó grabado** — limitación a corregir en la próxima sesión (segmentar por bloque, `TEST_PLAN_STANDARD §7.2`) |
| Resultado global | 17 casos con evidencia directa adicional; **3 hallazgos nuevos** (H5, H6, H7); 2 casos no concluyentes (a repetir); varios bloqueados por alcance (segundo usuario/rol no disponible) |

### 16.2 Hallazgos nuevos

**🔴 H5 — La lupa/alta manual de Empresa de Transporte rechaza NIF no registrado en Sòstrat (`TRU-B05-T12`).**
Al introducir manualmente un NIF de empresa que no existe en el WS Listar Usuarios Sòstrat (sin usar la lupa),
el sistema muestra el error **"Ese nif no se corresponde con ninguna Empresa de Transporte"** y bloquea el
guardado del campo. Esto contradice §2.2.3 (que documenta que si la empresa no existe en PERSONES se inserta
automáticamente como tipo `J`) y el propio caso de prueba B05-T12, que espera que la escritura manual esté
permitida. **Recomendación:** aclarar con el equipo funcional si la validación estricta es el comportamiento
correcto (y en ese caso corregir §2.2.3/B05-T12 del plan) o si es un defecto que bloquea altas manuales legítimas.

**🟠 H6 — Nombre Conductor se guarda como "." tras seleccionar desde la lupa (`TRU-B05-T01`/`T51`, relacionado con H3).**
Al seleccionar un conductor desde la lupa de búsqueda (WS Listar Usuarios Sòstrat), el `Id Usuario Conductor`
se recupera correctamente, pero los campos Nombre/Apellidos/Teléfono quedaron vacíos en pantalla y, tras
guardar, el campo **Nombre Conductor** persistió con el valor literal **"."** en vez del nombre real o de un
valor vacío. Se observó el mismo patrón "." en Nombre/Terminal de varios registros preexistentes en el GRID,
sugiriendo que no es un caso aislado sino un patrón de mapeo de datos incorrecto entre el WS de Sòstrat y los
campos del formulario para ciertos usuarios. **Recomendación:** revisar el mapeo de campos de la respuesta del
WS Listar Usuarios Sòstrat al formulario de Mantenimiento, especialmente para registros de tipo "CP" (razón
social) devueltos por la búsqueda de conductores.

**🔴 H7 — Nomenclatura de API inconsistente tras el renombrado (`TRU-B12-T03`).** El Swagger del endpoint
`https://apipre.portdebarcelona.cat/trc/` — que según §1.1/ARQ-2444 corresponde a **`APB.API.LGP`** tras el
renombrado de abril 2025 — muestra el título **"APB.API.TRU"** en la propia definición OpenAPI. Puede ser un
resto de la nomenclatura antigua (`APB.API.TRU.LGP`) no actualizado en el proyecto de la API, o una definición
Swagger compartida entre ambas APIs. **Recomendación:** confirmar con el equipo de desarrollo si el título del
Swagger debe actualizarse a `APB.API.LGP` para evitar confusión operativa.

### 16.3 Casos no ejecutados o bloqueados en esta sesión (IDs canónicos)

| Motivo | Casos |
|---|---|
| Bloqueado por alcance — requiere segundo usuario/rol (`USER_READ_TRUCK_CENTER` puro, usuario sin preferencia de idioma, o permiso de Auditoría) | TRU-B02-T12, TRU-B02-T13, TRU-B03-T16, TRU-B04-T06, TRU-B08-T02, TRU-B08-T03, TRU-B08-T04, TRU-B08-T05, TRU-B08-T06, TRU-B08-T07, TRU-B08-T09, TRU-B08-T10, TRU-B07-T06 |
| No ejecutable desde navegador — requiere inyección de fallo en backend/BD | TRU-B04-T07, TRU-B04-T08 |
| Bloqueado — `Forbidden` en "Auditoría de procesos" (H4 persiste) | TRU-B09-T01 a TRU-B09-T08 |
| No ejecutado en esta sesión (sin evidencia nueva) | TRU-B03-T14, TRU-B05-T06, TRU-B05-T08, TRU-B05-T09, TRU-B05-T10, TRU-B06-T03, TRU-B06-T07, TRU-B06-T08, TRU-B10-T01 a TRU-B10-T06, TRU-B11-T01 a TRU-B11-T06, TRU-B12-T04, TRU-B12-T05 |
| No concluyente — a repetir | TRU-B03-T10 (cambio de tipo no persistió), TRU-B06-T05 (asignación GRIMALDI no detectada como cambio) |
| Fuera de alcance de navegador (según plan) | Bloque B13 (k6, `azure-qa`/`ci-runner`), Bloque B14 (xUnit, repo `APB.TRU`) |

### 16.4 Pendiente para próximas sesiones

1. Aclarar y, si procede, corregir H5 (bloquea el alta manual de empresas de transporte).
2. Investigar el mapeo de datos de H6 (campo Nombre "." tras selección por lupa) — parece afectar a varios
   registros históricos, no solo a los creados en esta sesión.
3. Confirmar con desarrollo el título del Swagger de `/trc/` (H7).
4. Repetir TRU-B03-T10 y TRU-B06-T05 con interacción más cuidadosa sobre los desplegables (posible problema
   de automatización, no necesariamente del aplicativo).
5. Conseguir un segundo usuario/rol (`USER_READ_TRUCK_CENTER` puro, usuario con permiso de Auditoría, usuario
   nuevo sin preferencia de idioma) para desbloquear B02-T12/T13, B03-T16, B04-T06, B08-T02 a T07/T09/T10 y B09 completo.
6. Segmentar la grabación de vídeo por bloque desde el inicio de la sesión (start/export/clear en cada límite
   de 50 fotogramas), conforme a `TEST_PLAN_STANDARD §7.2` — en esta sesión solo quedó cubierto el bloque inicial.
7. B10 (integración WS ARQ Docks) sigue sin ejecutar — requiere revisar pantallas comunes de expedientes/errores/mensajes de Docks.

---

*Documento del APB AI Framework. Requiere revisión humana antes de aprobación (draft → candidate).*
