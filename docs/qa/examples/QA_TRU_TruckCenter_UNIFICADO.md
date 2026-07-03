# Plan de Pruebas UNIFICADO — TRU TruckCenter (APB.API.LGP + APB.API.TRU)

> **Borrador generado por IA** (APB AI Framework — apb-qa-test-plan-v1.2.0) — pendiente validación humana. No distribuir sin revisión.
>
> **Fecha de unificación:** 2026-07-02 (v1.0) · **v1.2 (2026-07-03):** renumeración a ID canónico §3.2 ·
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

TRU se integra en el portal DOCKS siguiendo directrices ARQ:
- **Pantallas comunes:** expedientes, eventos, errores, documentos, menú contextual.
- **WebServices ARQ (7):** `ARQ_APPFASES`, `ARQ_EVENTOS`, `ARQ_MENSAJES`, `ARQ_ERRORES`, `ARQ_LOGIN_CAS`,
  `ARQ_LOGIN_TOKEN`, `ARQ_FASES`.
- **Login:** originalmente CAS/LDAP → migrado a **Microsoft EntraID** (2025).
- **Multiidioma:** idioma predeterminado **catalán**, personalizable por usuario en su perfil.
- **Precondición global:** si falla una transacción → **ROLLBACK** completo + aviso al usuario, sin
  reintentos automáticos.
- **Convención BD:** aunque las columnas se definan en notación mixta, la implementación es siempre en
  MAYÚSCULAS.

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

### 1.6 Roles EntraID (TRANSTE-1520)

| Rol / Permiso | Alcance |
|---|---|
| `USER_READ_TRUCK_CENTER` | Solo lectura (ver GRID, consultar mantenimiento) |
| `MANAGE_TRUCK_CENTER` | Gestión completa: alta, baja, modificación, asignar terminal, salir parking, maestros |
| `USER_TRUCK_CENTER` | Usuario estándar |
| `API_CALL_TRU_CONTROL_PUERTAS` | Permite llamar al WS de control de puertas (IKUSI) |

> Soporte ARQ para creación de AppRegistration en External ID (ARQ-2157). Documento de especificaciones:
> "Cambios en DOCKS para integración con Microsoft EntraID SSO_v1.1".

### 1.7 Integraciones

WS ARQ Docks (7 servicios) · WS Listar Usuarios Sòstrat (lupas y terminales) · EntraID SSO · cámaras IKUSI ·
pipelines Jenkins/GitHub. Precondición global: fallo de transacción → **ROLLBACK** + aviso, sin reintentos.

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

**Lógica de negocio — determinación entrada/salida:** `acceso=24 AND carril=90` → **ENTRADA** ·
`acceso=24 AND carril=91` → **SALIDA**.

- **Flujo ENTRADA:** (1) buscar en TRUCK_CENTER registro con misma matrícula sin `HORA_SORTIDA`; (2) si
  existe → cerrar anterior (`HORA_SORTIDA = now − 1s`, `FASE = FORA DEL PARKING`); (3) crear nuevo
  (`HORA_ENTRADA = fecha_param`, `MATRICULA_CAMIO = matricula_param`, `FASE = EN EL PARKING`,
  `CONEXIO_ELECTRICITAT = 0`, `ITV = 0`).
- **Flujo SALIDA:** (1) buscar registro activo con misma matrícula; (2) si existe → `HORA_SORTIDA =
  fecha_param`, `FASE = FORA DEL PARKING`.
- **Matrícula ausente (TRANSTE-1513):** cuando la cámara no detecta matrícula → evento
  `TRU_CONTROL_PUERTAS_KO` con texto `Control de Acceso OK:Número tarjeta:/Acceso:24/Carril:90/Fecha:29/4/2024 13:14:56/Matricula:NOMATRI`.
- **Campo idCamara (TRANSTE-1522):** cambio de formato 8 (Integer) → 17 (Long) números; aunque no se usa en
  lógica de negocio, el JSON lo incluye y se ajustó para que el cambio de tamaño no provoque error de parsing.

### 2.2 Aplicación Web (APB.API.TRU)

#### 2.2.1 GRID Principal

**Columnas por defecto (en este orden):** (1) Id del Truck Center · (2) Matrícula Camión · (3) Entrada ·
(4) Salida · (5) Terminal (Nombre) · (6) Conductor Nombre · (7) Conductor Apellido 1 · (8) Conductor
Apellido 2 · (9) Empresa Transporte (Razón Social).

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

**Características:** ordenación por defecto **más nuevo a más viejo** · **Exportación Excel** de todos los
campos (defecto + añadibles) · **Botón Refresco** (TRANSTE-1511) · **Acción "Salir del Parking"** (solo con
registro seleccionado en fase `EN EL PARKING` → `HORA_SORTIDA = now`, `FASE = FORA DEL PARKING`) · todos los
campos con **filtro por lupa**.

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

## 5. Matriz unificada de pruebas (112 casos)

> `Prio`: Crítica/Alta/Media. `Tipo`: clasificación de la visión formal (C). Estado inicial: `Pendiente`.

### Bloque B01 — API ControlPuertas / Recepción LPR (12)

| ID | Legado | Caso | Tipo | Prio | Resultado esperado | Procedencia | Desde | OK func. | Estado |
|----|--------|------|------|------|--------------------|-------------|-------|----------|--------|
| TRU-B01-T01 | TRU-T01 | Entrada normal con matrícula | Funcional | Crítica | Nuevo registro `EN EL PARKING`, elec=0, ITV=0, HORA_ENTRADA=fecha; evento `TRU_CREACION..._OK` | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B01-T02 | TRU-T02 | Salida normal con matrícula | Funcional | Crítica | Registro activo → `HORA_SORTIDA`=fecha, `FORA DEL PARKING`; evento `TRU_SALIR_PARKING_OK` | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B01-T03 | TRU-T03 | Entrada duplicada — camión aún en parking | Funcional | Crítica | Cierra anterior (now-1s) + crea nuevo; dos eventos | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B01-T04 | TRU-T04 | Salida sin registro previo | Funcional | Alta | Sin error, no modifica datos, sin evento KO | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B01-T05 | TRU-T05 | Lectura sin matrícula (NOMATRI) | Funcional | Crítica | Evento `TRU_CONTROL_PUERTAS_KO` con texto `Matricula:NOMATRI` | R[J:TRANSTE-1513·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B01-T06 | TRU-T06 | idCamara 17 dígitos (nuevo formato) | Integración | Alta | La API acepta el parámetro sin error de parsing | R[J:TRANSTE-1522·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B01-T07 | TRU-T07 | idCamara 8 dígitos (legacy) | Compatibilidad | Alta | Compatibilidad con formato antiguo, sin error | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B01-T08 | TRU-T08 | Campos no utilizados con valores extremos | Integración | Media | Solo se validan los 4 campos usados; resto ignorado | R[J:TRANSTE-1523·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B01-T09 | TRU-T09 | JSON malformado | API | Alta | Error HTTP 400 controlado (no 500) | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B01-T10 | TRU-T10 | Llamada sin permiso `API_CALL_TRU_CONTROL_PUERTAS` | Seguridad | Crítica | Rechazo 401/403 | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B01-T11 | TRU-T11 | HORA_SORTIDA anterior = now − 1s exacto | Lógica | Alta | El cierre del anterior registra salida con diferencia exacta de 1s | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B01-T12 | TRU-T12 | Campos de salida de la API | API | Media | Respuesta consistente con la lógica de negocio y el contrato | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |

### Bloque B02 — GRID Principal (14)

| ID | Legado | Caso | Tipo | Prio | Resultado esperado | Procedencia | Desde | OK func. | Estado |
|----|--------|------|------|------|--------------------|-------------|-------|----------|--------|
| TRU-B02-T01 | TRU-T13 | Columnas por defecto visibles | UI | Crítica | 9 columnas en orden: Id, Matrícula, Entrada, Salida, Terminal, Nombre, Apellido1, Apellido2, Empresa | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B02-T02 | TRU-T14 | Ordenación por defecto | UI | Alta | Registros de más nuevo a más viejo | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B02-T03 | TRU-T15 | Selector de columnas — campos añadibles | UI | Alta | Aparecen Fase, NIFs, Ids Sòstrat, elec., ITV, Observaciones | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B02-T04 | TRU-T16 | Columnas auditoría en selector | UI | Alta | APB_CREADOR/MODIFICADOR/CREAT/MODIFICAT disponibles y filtrables | R[J:TRANSTE-1515·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B02-T05 | TRU-T17 | Filtro por lupa en cada columna | UI | Alta | Filtrado correcto en todas las columnas visibles | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B02-T06 | TRU-T18 | Botón refresco GRID | UI | Alta | GRID actualizado sin recargar la página completa | R[J:TRANSTE-1511·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B02-T07 | TRU-T19 | Acción "Salir del Parking" desde GRID | Funcional | Crítica | HORA_SORTIDA=now, fase final; evento `TRU_SALIR_PARKING_OK` | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B02-T08 | TRU-T20 | "Salir del Parking" sin registro seleccionado | UI | Alta | Acción no disponible o aviso | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B02-T09 | TRU-T21 | "Salir del Parking" en registro ya FORA | UI | Alta | Acción no permitida | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B02-T10 | TRU-T22 | Exportar a Excel — todos los campos | Funcional | Alta | Excel con 9 defecto + 10 añadibles + 4 auditoría, datos correctos | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B02-T11 | TRU-T23 | Exportar a Excel — GRID vacío | Funcional | Media | Excel generado sin error (cabeceras/vacío) | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B02-T12 | TRU-T24 | Acceso GRID con USER_READ | Permisos | Crítica | Consulta sí; acción "Salir del Parking" no disponible | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B02-T13 | TRU-T25 | Acceso GRID con MANAGE | Permisos | Crítica | Consulta + acciones de gestión disponibles | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B02-T14 | TRU-T26 | Pestaña navegador | UI | Media | Título = "Truck Center" (no "Aplicación de Arquitectura APB") | R[J:TRANSTE-1517·AF] · C[Cod] | 2026-06-30 | — | Pendiente |

### Bloque B03 — Mantenimiento / Alta (16)

| ID | Legado | Caso | Tipo | Prio | Resultado esperado | Procedencia | Desde | OK func. | Estado |
|----|--------|------|------|------|--------------------|-------------|-------|----------|--------|
| TRU-B03-T01 | TRU-T27 | Alta mínima (solo obligatorios) | Funcional | Crítica | Registro `EN EL PARKING`, checkboxes 0; evento creación OK | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B03-T02 | TRU-T28 | Alta completa (todos los campos) | Funcional | Crítica | Registro con todos los datos; verificar cada columna en BD | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B03-T03 | TRU-T29 | Alta sin matrícula | Validación | Crítica | No permite guardar; error de obligatorio | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B03-T04 | TRU-T30 | Alta sin tipo vehículo | Validación | Alta | Bloquea guardado | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B03-T05 | TRU-T31 | Alta sin hora entrada | Validación | Alta | Bloquea guardado | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B03-T06 | TRU-T32 | Alta duplicado — usuario CONFIRMA | Regla negocio | Crítica | Cierra anterior (now-1s) + crea nuevo | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B03-T07 | TRU-T33 | Alta duplicado — usuario CANCELA | Regla negocio | Crítica | No crea; mensaje "El registro del camión en el parking no se ha hecho" | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B03-T08 | TRU-T34 | Matrícula existente en CAMIONS | Integración | Alta | Tipo de vehículo auto-recuperado, editable | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B03-T09 | TRU-T35 | Matrícula nueva (no en CAMIONS) | Integración | Alta | Tipo vacío a seleccionar; nueva entrada en CAMIONS al guardar | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B03-T10 | TRU-T36 | Modificar tipo vehículo recuperado | Integración | Alta | Se actualiza expediente y tabla CAMIONS | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B03-T11 | TRU-T37 | Botón reloj entrada | UI | Media | Hora entrada = hora actual del sistema | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B03-T12 | TRU-T38 | Checkbox conexión eléctrica | UI | Media | Valor 1/0 en BD según estado | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B03-T13 | TRU-T39 | Checkbox ITV | UI | Media | Valor 1/0 en BD según estado | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B03-T14 | TRU-T40 | Checkbox mercancías peligrosas | UI | Media | Valor 1/0 en BD (`MERCADERIES_PERILLOSES`) | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B03-T15 | TRU-T41 | Observaciones 4000 caracteres | Validación | Media | Se guarda completo sin truncar | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B03-T16 | TRU-T42 | Rol USER_READ no puede crear | Permisos | Crítica | Botón alta no visible / acción denegada | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |

### Bloque B04 — Mantenimiento / Modificación y Baja (8)

| ID | Legado | Caso | Tipo | Prio | Resultado esperado | Procedencia | Desde | OK func. | Estado |
|----|--------|------|------|------|--------------------|-------------|-------|----------|--------|
| TRU-B04-T01 | TRU-T43 | Modificar registro existente | Funcional | Crítica | Datos actualizados; evento modificación OK | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B04-T02 | TRU-T44 | Campos solo lectura no editables | UI | Alta | ID, Fase, Empresa (razón social), Ids Sòstrat no editables | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B04-T03 | TRU-T45 | "Salir del Parking" desde mantenimiento | Funcional | Crítica | HORA_SORTIDA=now, fase final; evento salir OK | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B04-T04 | TRU-T46 | Botón no visible en FORA DEL PARKING | UI | Alta | Botón oculto para registros cerrados | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B04-T05 | TRU-T47 | Baja de registro | Funcional | Alta | Registro eliminado; evento correspondiente | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B04-T06 | TRU-T48 | Modificar con USER_READ | Permisos | Crítica | Modificación denegada; solo consulta | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B04-T07 | TRU-T49 | Rollback en error transaccional | Integridad | Crítica | ROLLBACK completo; sin cambios parciales persistidos | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B04-T08 | TRU-T50 | Sin reintento automático tras error | Comportamiento | Alta | No reintenta; el usuario reejecuta manualmente | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |

### Bloque B05 — Lupas / Conductores y Empresas (12)

| ID | Legado | Caso | Tipo | Prio | Resultado esperado | Procedencia | Desde | OK func. | Estado |
|----|--------|------|------|------|--------------------|-------------|-------|----------|--------|
| TRU-B05-T01 | TRU-T51 | Lupa conductores — búsqueda y selección | Integración | Crítica | Recupera NIF, nombre, apellidos, teléfono, ID Sòstrat (tipo F) | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B05-T02 | TRU-T52 | Lupa conductores — nuevo en PERSONES | Integración | Crítica | Inserta automáticamente como `TIPUS_PERSONA=F` | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B05-T03 | TRU-T53 | Lupa conductores — ya existente | Integración | Alta | Recupera de PERSONES, no duplica | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B05-T04 | TRU-T54 | Lupa conductores — filtrado funciona | UI | Crítica | Resultados filtrados correctamente | R[J:TRANSTE-1534·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B05-T05 | TRU-T55 | Lupa empresas — búsqueda y selección | Integración | Crítica | Recupera NIF, razón social, ID Sòstrat (sin filtro tipo) | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B05-T06 | TRU-T56 | Lupa empresas — nueva en PERSONES | Integración | Crítica | Inserta como `TIPUS_PERSONA=J` | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B05-T07 | TRU-T57 | Lupa empresas — ya existente | Integración | Alta | Recupera datos, no duplica | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B05-T08 | TRU-T58 | Lupa empresas — filtrado funciona | UI | Crítica | Resultados filtrados correctamente | R[J:TRANSTE-1534·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B05-T09 | TRU-T59 | WS Sòstrat no disponible | Error handling | Alta | Error controlado, sin excepción no manejada | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B05-T10 | TRU-T60 | Datos duplicados WS usuarios | Integración | Alta | Lista sin duplicados | R[J:SOSO-2075·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B05-T11 | TRU-T61 | Escritura manual conductor (sin lupa) | Funcional | Media | Permite ingreso manual, datos guardados | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B05-T12 | TRU-T62 | Escritura manual empresa (sin lupa) | Funcional | Media | Permite ingreso manual | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |

### Bloque B06 — Desplegable Terminales (8)

| ID | Legado | Caso | Tipo | Prio | Resultado esperado | Procedencia | Desde | OK func. | Estado |
|----|--------|------|------|------|--------------------|-------------|-------|----------|--------|
| TRU-B06-T01 | TRU-T63 | Desplegable solo actividad TU | UI | Crítica | Solo usuarios con actividad TU (no todos) | R[J:TRANSTE-1509·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B06-T02 | TRU-T64 | Desplegable no bloquea página | Rendimiento | Crítica | Página responde con fluidez, sin bloqueo | R[J:TRANSTE-1509·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B06-T03 | TRU-T65 | Asignar PORTCEMENT SA | Funcional | Alta | Asignación correcta, guardado OK | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B06-T04 | TRU-T66 | Asignar APM TERMINALS | Funcional | Alta | Asignación correcta | R[J:TRANSTE-1510·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B06-T05 | TRU-T67 | Asignar GRIMALDI | Funcional | Alta | Asignación correcta | R[J:TRANSTE-1510·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B06-T06 | TRU-T68 | Asignar AUTOTERMINAL SA | Funcional | Alta | Asignación correcta | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B06-T07 | TRU-T69 | Asignar cada una de las 13 terminales | Funcional | Alta | Todas asignables sin error | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B06-T08 | TRU-T70 | Desplegable sin servicio Sòstrat | Error handling | Media | Fallo manejado sin bloquear interfaz | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |

### Bloque B07 — Tabla Maestra / Tipos de Vehículo (6)

| ID | Legado | Caso | Tipo | Prio | Resultado esperado | Procedencia | Desde | OK func. | Estado |
|----|--------|------|------|------|--------------------|-------------|-------|----------|--------|
| TRU-B07-T01 | TRU-T71 | GRID tipos vehículo — 5 registros iniciales | Datos | Alta | Portacontenedores, Portavehículos, Lonas, Cisternas, Bañeras | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B07-T02 | TRU-T72 | Alta nuevo tipo vehículo | Funcional | Alta | Nuevo tipo visible en GRID y desplegable | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B07-T03 | TRU-T73 | Modificar tipo existente | Funcional | Media | Descripción actualizada | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B07-T04 | TRU-T74 | Eliminar tipo sin dependencias | Funcional | Media | Eliminado sin error | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B07-T05 | TRU-T75 | Eliminar tipo con dependencias | Integridad | Alta | Impide eliminación por integridad referencial | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B07-T06 | TRU-T76 | USER_READ no puede modificar maestro | Permisos | Alta | Solo consulta permitida | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |

### Bloque B08 — Autenticación y Permisos EntraID (10)

| ID | Legado | Caso | Tipo | Prio | Resultado esperado | Procedencia | Desde | OK func. | Estado |
|----|--------|------|------|------|--------------------|-------------|-------|----------|--------|
| TRU-B08-T01 | TRU-T77 | Login EntraID exitoso | Autenticación | Crítica | Acceso según rol asignado | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B08-T02 | TRU-T78 | Rol USER_READ — solo lectura completa | Permisos | Crítica | Ver GRID + consultar; sin alta/baja/mod/salir | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B08-T03 | TRU-T79 | Rol MANAGE — gestión completa | Permisos | Crítica | Alta, baja, mod, asignar terminal, salir, maestros | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B08-T04 | TRU-T80 | Rol USER — usuario estándar | Permisos | Alta | Acceso conforme al perfil estándar | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B08-T05 | TRU-T81 | Sin rol TRU | Autorización | Crítica | Acceso denegado, sin menú TRU | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B08-T06 | TRU-T82 | Token expirado | Seguridad | Alta | Redirección a login EntraID | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B08-T07 | TRU-T83 | Idioma predeterminado catalán | Internacionalización | Media | Interfaz en catalán para usuario sin preferencia | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B08-T08 | TRU-T84 | Cambio de idioma en perfil | Internacionalización | Media | Interfaz en idioma seleccionado | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B08-T09 | TRU-T85 | AppRegistration External ID configurada | Configuración | Alta | AppRegistration TRU correcta en External ID | R[AF·J:ARQ-2157] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B08-T10 | TRU-T86 | Tokens correctos tras renombrado API | Integración | Alta | Tokens apuntan a la app TRU correcta | R[AF·J:TRANSTE-1527] · C[Cod] | 2026-07-01 | — | Pendiente |

### Bloque B09 — Eventos de Auditoría (8)

| ID | Legado | Caso | Tipo | Prio | Resultado esperado | Procedencia | Desde | OK func. | Estado |
|----|--------|------|------|------|--------------------|-------------|-------|----------|--------|
| TRU-B09-T01 | TRU-T87 | Evento creación OK | Auditoría | Crítica | `TRU_CREACION_TRUCK_CENTER_OK` con ID en eventos dominio TRU | R[AF·J:TRANSTE-1524] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B09-T02 | TRU-T88 | Evento creación KO | Auditoría | Alta | `TRU_CREACION_TRUCK_CENTER_KO` ante error | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B09-T03 | TRU-T89 | Evento modificación OK | Auditoría | Alta | `TRU_MODIFICACION_TRUCK_CENTER_OK` | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B09-T04 | TRU-T90 | Evento modificación KO | Auditoría | Alta | `TRU_MODIFICACION_TRUCK_CENTER_KO` | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B09-T05 | TRU-T91 | Evento control puertas OK | Auditoría | Crítica | `TRU_CONTROL_PUERTAS_OK` con tarjeta/acceso/carril/fecha/matrícula | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B09-T06 | TRU-T92 | Evento control puertas KO | Auditoría | Alta | `TRU_CONTROL_PUERTAS_KO` con NOMATRI | R[J:TRANSTE-1513·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B09-T07 | TRU-T93 | Evento salir parking OK | Auditoría | Alta | `TRU_SALIR_PARKING_OK` con matrícula e ID | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B09-T08 | TRU-T94 | Eventos visibles en dominio TRU | Auditoría | Alta | En sección TRU propia, no en pantalla ARQ genérica | R[J:TRANSTE-1524·AF] · C[Cod] | 2026-06-30 | — | Pendiente |

### Bloque B10 — Integración WS ARQ Docks (6)

| ID | Legado | Caso | Tipo | Prio | Resultado esperado | Procedencia | Desde | OK func. | Estado |
|----|--------|------|------|------|--------------------|-------------|-------|----------|--------|
| TRU-B10-T01 | TRU-T95 | Expediente Docks creado | Integración | Alta | Visible en pantalla común de expedientes Docks | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B10-T02 | TRU-T96 | Fases expediente correctas | Integración | Alta | Solo `EN EL PARKING` → `FORA DEL PARKING` | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B10-T03 | TRU-T97 | Menú contextual funcional | Integración | Media | Menú contextual Docks operativo | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B10-T04 | TRU-T98 | Pantalla errores Docks | Integración | Media | Error visible en pantalla común de errores | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B10-T05 | TRU-T99 | Mensajes Docks funcionales | Integración | Alta | Aviso de duplicado con el mensaje esperado | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B10-T06 | TRU-T100 | WS ARQ todos operativos | Integración | Alta | APPFASES/EVENTOS/MENSAJES/ERRORES/LOGIN_CAS/LOGIN_TOKEN/FASES OK | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |

### Bloque B11 — Seguridad y Calidad de Código (6)

| ID | Legado | Caso | Tipo | Prio | Resultado esperado | Procedencia | Desde | OK func. | Estado |
|----|--------|------|------|------|--------------------|-------------|-------|----------|--------|
| TRU-B11-T01 | TRU-T101 | SonarQube sin vulnerabilidades altas | Calidad | Crítica | Sin vulnerabilidades altas | R[J:TRANSTE-1530·AF·Cod] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B11-T02 | TRU-T102 | No inyección SQL en lupas | Seguridad | Crítica | Input sanitizado, sin efecto en consultas | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B11-T03 | TRU-T103 | No XSS en observaciones | Seguridad | Crítica | Contenido malicioso no ejecutado | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B11-T04 | TRU-T104 | No XSS en matrícula | Seguridad | Alta | Input no genera ejecución de script | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B11-T05 | TRU-T105 | Validación de largo de campos según modelo | Validación | Alta | Rechazo/control de valor fuera de rango, sin error BD | R[AF·Cod] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B11-T06 | TRU-T106 | HTTPS en todos los endpoints | Seguridad | Alta | PRE y PRO usan HTTPS exclusivamente | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |

### Bloque B12 — Regresión, Despliegue y E2E (6)

| ID | Legado | Caso | Tipo | Prio | Resultado esperado | Procedencia | Desde | OK func. | Estado |
|----|--------|------|------|------|--------------------|-------------|-------|----------|--------|
| TRU-B12-T01 | TRU-T107 | Health check API LGP | Despliegue | Crítica | GET endpoint TRC → 200 OK | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B12-T02 | TRU-T108 | Health check APP TRU | Despliegue | Crítica | GET endpoint web → 200 OK | R[J·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B12-T03 | TRU-T109 | Nomenclatura APIs post-renombrado | Despliegue | Alta | Se observan `APB.API.LGP` y `APB.API.TRU` (no nombres antiguos) | R[J:ARQ-2444·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B12-T04 | TRU-T110 | Repositorio APB.TRU | Despliegue | Alta | Repo y pipelines apuntan al nuevo nombre | R[J:TRANSTE-1527·AF] · C[Cod] | 2026-06-30 | — | Pendiente |
| TRU-B12-T05 | TRU-T111 | E2E: Entrada LPR → GRID → Terminal → Salida LPR | E2E | Crítica | Registro completo con entrada, terminal, conductor, empresa, salida; todos los eventos | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |
| TRU-B12-T06 | TRU-T112 | E2E: Alta manual → Modificar → Salir Parking | E2E | Crítica | Flujo completo manual; eventos creación + modificación + salida | R[AF] · C[Cod] | 2026-07-01 | — | Pendiente |

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
| **TOTAL** | | **112** | **40** | **51** | **21** |

**Bloques canónicos (§3.2, append-only — nunca se renumeran, un bloque nuevo siempre es B13, B14…):**
`B01`=API ControlPuertas · `B02`=GRID Principal · `B03`=Mantenimiento/Alta · `B04`=Mantenimiento/Modif.-Baja ·
`B05`=Lupas · `B06`=Desplegable Terminales · `B07`=Tabla Maestra Vehículos · `B08`=Autenticación EntraID ·
`B09`=Eventos de Auditoría · `B10`=Integración WS ARQ · `B11`=Seguridad y Calidad · `B12`=Regresión/Despliegue/E2E.

**Procedencia (resumen):** 39 casos con respaldo directo en **Jira** (visión A/Rovo, desde 2026-06-30);
73 añadidos desde el **Análisis Funcional** (visión B/Rovo, desde 2026-07-01); **los 112** validados contra
**código** por GitHub Copilot (visión C). 0 duplicados.

**Automatización (para Fase de ejecución):** por navegador (Playwright/agéntico) → Bloques 2–10 y E2E
(T111/T112); por API HTTP → Bloque 1; manual/otra herramienta (SonarQube, revisión) → Bloque 11 parcial y
despliegue (T107–T110 vía health-check HTTP).

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
**Bloque B02 — GRID Principal:** ☐ TRU-B02-T01 ☐ T02 ☐ T03 ☐ T04 ☐ T05 ☐ T06 ☐ T07 ☐ T08 ☐ T09 ☐ T10 ☐ T11 ☐ T12 ☐ T13 ☐ T14
**Bloque B03 — Mantenimiento/Alta:** ☐ TRU-B03-T01 ☐ T02 ☐ T03 ☐ T04 ☐ T05 ☐ T06 ☐ T07 ☐ T08 ☐ T09 ☐ T10 ☐ T11 ☐ T12 ☐ T13 ☐ T14 ☐ T15 ☐ T16
**Bloque B04 — Modif./Baja:** ☐ TRU-B04-T01 ☐ T02 ☐ T03 ☐ T04 ☐ T05 ☐ T06 ☐ T07 ☐ T08
**Bloque B05 — Lupas:** ☐ TRU-B05-T01 ☐ T02 ☐ T03 ☐ T04 ☐ T05 ☐ T06 ☐ T07 ☐ T08 ☐ T09 ☐ T10 ☐ T11 ☐ T12
**Bloque B06 — Terminales:** ☐ TRU-B06-T01 ☐ T02 ☐ T03 ☐ T04 ☐ T05 ☐ T06 ☐ T07 ☐ T08
**Bloque B07 — Tabla Maestra:** ☐ TRU-B07-T01 ☐ T02 ☐ T03 ☐ T04 ☐ T05 ☐ T06
**Bloque B08 — Autenticación EntraID:** ☐ TRU-B08-T01 ☐ T02 ☐ T03 ☐ T04 ☐ T05 ☐ T06 ☐ T07 ☐ T08 ☐ T09 ☐ T10
**Bloque B09 — Eventos Auditoría:** ☐ TRU-B09-T01 ☐ T02 ☐ T03 ☐ T04 ☐ T05 ☐ T06 ☐ T07 ☐ T08
**Bloque B10 — WS ARQ Docks:** ☐ TRU-B10-T01 ☐ T02 ☐ T03 ☐ T04 ☐ T05 ☐ T06
**Bloque B11 — Seguridad/Calidad:** ☐ TRU-B11-T01 ☐ T02 ☐ T03 ☐ T04 ☐ T05 ☐ T06
**Bloque B12 — Regresión/Despliegue/E2E:** ☐ TRU-B12-T01 ☐ T02 ☐ T03 ☐ T04 ☐ T05 ☐ T06

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

## 14. Aprobados del plan (por cambio)

| Versión | Cambio | Aprobado por (rol) | Fecha |
|---------|--------|--------------------|-------|
| Unificado 1.0 | Creación del plan unificado | _pendiente — QA Lead / Analista Funcional_ | — |
| Unificado 1.1 | Restauración de contenido íntegro de las fuentes | _pendiente — QA Lead / Analista Funcional_ | — |
| Unificado 1.2 | Renumeración a ID canónico append-only | _pendiente — QA Lead / Analista Funcional_ | — |

---

*Documento del APB AI Framework. Requiere revisión humana antes de aprobación (draft → candidate).*
