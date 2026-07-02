# QA — TRU-TruckCenter (APB.API.LGP + APB.API.TRU) — VERSIÓN ENRIQUECIDA

> **Generado como Ingeniero QA** · Fecha: 2026-07-01  
> **Fuentes primarias:**  
> - AF Truck Center v1.1 (03/02/2023, rev. 22/07/2025) — Análisis Funcional oficial  
> - ~50 tickets Jira (TRANSTE, ARQ, MISA, GS, RM, PVI, SOSO, LNVB)  
> - Adjuntos de tickets Jira (capturas, specs EntraID, SonarQube)  
> **Versión anterior:** QA_TRU_TruckCenter.md (38 casos) → **Esta versión: 112 casos de prueba**

---

## 1. Descripción General

**TRU** (Truck Center) es una aplicación del ecosistema **DOCKS (.NET)** que gestiona el **control de acceso, registro y seguimiento de camiones** en el parking del Truck Center de la Autoridad Portuaria de Barcelona. Integra lecturas automáticas de matrículas (LPR) desde cámaras IKUSI con un panel web de gestión de entradas, salidas, asignación a terminales, conductores y empresas de transporte.

### 1.1 APIs

| API | Función | Endpoint PRE | Endpoint PRO |
|-----|---------|-------------|-------------|
| **APB.API.LGP** | API Control de Puertas (recepción datos LPR/IKUSI) | `https://apipre.portdebarcelona.cat/trc/` | `https://api.portdebarcelona.cat/trc/` |
| **APB.API.TRU** | Aplicación web Truck Center (frontend + backend) | `https://dockspre.portdebarcelona.cat/tru/` | `https://docks.portdebarcelona.cat/tru/` |

> **Renombrado abril 2025 (ARQ-2444):** `APB.API.TRU.LGP` → `APB.API.LGP` · `APB.API.TRU.TRC` → `APB.API.TRU`  
> **Repositorio GitHub:** `APB.TRU` (renombrado desde TRU, TRANSTE-1527)

### 1.2 Arquitectura

```
Cámaras LPR IKUSI (Controlacceso)
    │
    │ JSON {acceso, carril, fecha, lecturasMatricula}
    │
    │ REGLA ENTRADA/SALIDA:
    │   acceso=24, carril=90 → ENTRADA
    │   acceso=24, carril=91 → SALIDA
    ▼
┌──────────────────────────────┐
│  APB.API.LGP (.NET)          │  ← API Control de Puertas
│  POST /api/v1/TruckCenter    │
│       /ControlPuertas         │
│  Permiso: API_CALL_TRU_      │
│           CONTROL_PUERTAS     │
└──────────┬───────────────────┘
           │ Lógica duplicados:
           │  Si matrícula existe sin HORA_SORTIDA
           │  → Cierra anterior (hora-1s) + Alta nueva
           ▼
┌──────────────────────────────┐
│  Oracle DB                    │
│  ┌─────────────────────────┐ │
│  │ TRUCK_CENTER (12 cols)  │ │  ← Tabla principal expedientes
│  │ PERSONES (9 cols)       │ │  ← Conductores (F) y Empresas (J)
│  │ CAMIONS (3 cols)        │ │  ← Registro camiones + tipo vehículo
│  │ TIPUS_VEHICLE (3 cols)  │ │  ← Tabla maestra tipos
│  └─────────────────────────┘ │
└──────────────────────────────┘
           ▲
           │
┌──────────┴───────────────────┐
│  APB.API.TRU (.NET)           │  ← Aplicación Web DOCKS
│  ┌─────────────────────────┐ │
│  │ GRID Principal          │ │  ← 9 cols defecto + 10 añadibles
│  │ Mantenimiento           │ │  ← Alta/Baja/Modificación expedientes
│  │ Lupas (Conductores F,   │ │  ← WS Listar Usuarios Sòstrat
│  │        Empresas J)      │ │
│  │ Desplegable Terminales  │ │  ← Sòstrat actividad TU
│  │ Tabla Maestra Vehículos │ │  ← CRUD Tipos Vehículo
│  │ Acción "Salir Parking"  │ │
│  │ Exportación Excel       │ │
│  └─────────────────────────┘ │
│  Auth: EntraID (ext. 2025)   │
│  Idioma: Multiidioma (CA)    │
└──────────────────────────────┘
           │
           ▼
    WS ARQ Docks:
    ARQ_APPFASES, ARQ_EVENTOS, ARQ_MENSAJES,
    ARQ_ERRORES, ARQ_LOGIN_CAS, ARQ_LOGIN_TOKEN, ARQ_FASES
```

### 1.3 Integración con ARQ Docks

TRU se integra en el portal DOCKS siguiendo directrices ARQ:
- Pantallas comunes: **expedientes, eventos, errores, documentos, menú contextual**
- WebServices ARQ: APPFASES, EVENTOS, MENSAJES, ERRORES, LOGIN_CAS, LOGIN_TOKEN, FASES
- Login: originalmente CAS/LDAP → migrado a **Microsoft EntraID** (2025)
- **Multiidioma**: idioma predeterminado **catalán**, personalizable por usuario en perfil
- **Precondición global**: si falla transacción → ROLLBACK + aviso al usuario, sin reintentos automáticos

---

## 2. Modelo de Datos

### 2.1 TRUCK_CENTER (Tabla principal — expedientes)

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

### 2.2 PERSONES (Conductores y Empresas)

| Columna | Tipo | Nulable | Descripción |
|---------|------|---------|-------------|
| `ID` | NUMBER(10) | **PK** | ID persona |
| `NOMINTERN` | VARCHAR2(40) | NOT NULL | Identificador único |
| `TIPUS_PERSONA` | VARCHAR2(2) | NOT NULL | **F** = persona física (conductor), **J** = jurídica (empresa) |
| `NIF` | VARCHAR2(11) | NOT NULL | NIF/CIF |
| `NOM` | VARCHAR2(50) | NOT NULL | Nombre / Razón social |
| `COGNOM1` | VARCHAR2(30) | Nullable | Primer apellido (solo tipo F) |
| `COGNOM2` | VARCHAR2(30) | Nullable | Segundo apellido (solo tipo F) |
| `IDUSUARI_SOSTRAT` | VARCHAR2(6) | Nullable | Código en Sòstrat |
| `TELEFON` | VARCHAR2(30) | Nullable | Teléfono |

### 2.3 CAMIONS (Registro de camiones)

| Columna | Tipo | Descripción |
|---------|------|-------------|
| `MATRICULA_CAMIO` | VARCHAR2(10) | **PK** — Matrícula |
| `NOMINTERN` | VARCHAR2(40) | Identificador único. NOT NULL |
| `TIPUS_VEHICLE` | NUMBER(10) | FK → TIPUS_VEHICLE. NOT NULL |

### 2.4 TIPUS_VEHICLE (Tabla maestra)

| ID | Descripción |
|----|-------------|
| 1 | Portacontenedores |
| 2 | Portavehículos |
| 3 | Lonas |
| 4 | Cisternas |
| 5 | Bañeras |

---

## 3. Máquina de Estados (Fases del Expediente)

```
    ┌──────────────────┐
    │                  │
    ▼                  │
┌──────────────┐       │  Creación vía LPR (API) o manual (Web)
│ EN EL PARKING │──────┘
└──────┬───────┘
       │
       │ Acciones que provocan transición:
       │  1. Botón "Salir del Parking" (Web)
       │  2. Lectura LPR salida (acceso=24, carril=91)
       │  3. Alta duplicado confirmado → cierra anterior (hora_sortida = now - 1s)
       ▼
┌────────────────┐
│ FORA DEL PARKING│  ← Estado final
└────────────────┘
```

**Regla de duplicados (crítica):**  
Al crear registro (manual o API), si existe otro con **misma matrícula** sin `HORA_SORTIDA`:
- **Vía Web:** Aviso al usuario → Si confirma: cierra anterior (`HORA_SORTIDA = now - 1s`, fase = `FORA DEL PARKING`) y crea nuevo → Si cancela: no permite alta
- **Vía API (LPR):** Automáticamente cierra anterior y crea nuevo (sin confirmación usuario)

---

## 4. Funcionalidad Detallada

### 4.1 API ControlPuertas (APB.API.LGP)

**POST /api/v1/TruckCenter/ControlPuertas**  
**Permiso requerido:** `API_CALL_TRU_CONTROL_PUERTAS`

#### Parámetros de entrada

| Campo | Uso | Descripción |
|-------|-----|-------------|
| `acceso` | ✅ Validado | Puerta del puerto (determina entrada/salida) |
| `carril` | ✅ Validado | Calle de circulación (determina entrada/salida) |
| `fecha` | ✅ Validado | Hora de llegada/salida |
| `lecturasMatricula.matricula` | ✅ Validado | Matrícula del camión |
| `idCamara` | ❌ Ignorado | Cambió de Integer (8 dígitos) a Long (17 dígitos) — TRANSTE-1522 |
| Resto campos | ❌ Ignorado | No se validan ni procesan |

#### Lógica de negocio

**Determinación entrada/salida:**
- `acceso=24 AND carril=90` → **ENTRADA**
- `acceso=24 AND carril=91` → **SALIDA**

**Flujo ENTRADA:**
1. Buscar en TRUCK_CENTER registro con misma matrícula sin `HORA_SORTIDA`
2. Si existe → Cerrar anterior: `HORA_SORTIDA = now - 1 segundo`, `FASE = FORA DEL PARKING`
3. Crear nuevo registro: `HORA_ENTRADA = fecha_param`, `MATRICULA_CAMIO = matricula_param`, `FASE = EN EL PARKING`, `CONEXIO_ELECTRICITAT = 0`, `ITV = 0`

**Flujo SALIDA:**
1. Buscar en TRUCK_CENTER registro con misma matrícula sin `HORA_SORTIDA`
2. Si existe → `HORA_SORTIDA = fecha_param`, `FASE = FORA DEL PARKING`

**Manejo matrícula ausente (TRANSTE-1513):**
- Cuando cámara no detecta matrícula → evento `TRU_CONTROL_PUERTAS_KO`
- Texto: `Control de Acceso OK:…/Matricula:NOMATRI`

### 4.2 Aplicación Web (APB.API.TRU)

#### 4.2.1 GRID Principal

**Columnas por defecto** (en este orden):

| # | Campo |
|---|-------|
| 1 | Id del Truck Center |
| 2 | Matrícula Camión |
| 3 | Entrada |
| 4 | Salida |
| 5 | Terminal (Nombre) |
| 6 | Conductor Nombre |
| 7 | Conductor Apellido 1 |
| 8 | Conductor Apellido 2 |
| 9 | Empresa Transporte (Razón Social) |

**Columnas añadibles** (Selector de Columnas):

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
| APB_CREADOR | Auditoría (TRANSTE-1515) |
| APB_MODIFICADOR | Auditoría (TRANSTE-1515) |
| APB_CREAT | Auditoría (TRANSTE-1515) |
| APB_MODIFICAT | Auditoría (TRANSTE-1515) |

**Características:**
- Ordenación por defecto: **más nuevo a más viejo**
- **Exportación Excel** de todos los campos (defecto + añadibles)
- **Botón Refresco** (TRANSTE-1511)
- **Acción "Salir del Parking"**: solo con registro seleccionado en fase `EN EL PARKING` → informa `HORA_SORTIDA = now`, cambia fase a `FORA DEL PARKING`
- Todos los campos con **filtro por lupa**

#### 4.2.2 Pantalla de Mantenimiento

| Campo | Tipo | Obligatorio | Editable | Detalle |
|-------|------|-------------|----------|---------|
| ID | Numérico | Auto | Solo lectura | PK expediente |
| Matrícula Camión | Texto(10) | ✅ | Sí | Si existe en CAMIONS → recupera tipo vehículo |
| Fase | Texto | Auto | Solo lectura | `EN EL PARKING` / `FORA DEL PARKING` |
| Tipo de Vehículo | Desplegable | ✅ | Sí | Valores de TIPUS_VEHICLE (5 tipos). Auto-recuperado de CAMIONS si matrícula existe |
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

**Botón "Salir del Parking":** Solo visible en fase `EN EL PARKING` → `HORA_SORTIDA = now`, `FASE = FORA DEL PARKING`  
**Botón Reloj Entrada:** Pone fecha/hora actual como hora de entrada

#### 4.2.3 Lupas de Búsqueda

| Lupa | Fuente | Filtro | Persistencia |
|------|--------|--------|-------------|
| **Conductores** | WS Listar Usuarios Sòstrat | Tipo Persona = **F** | Si no existe en PERSONES → inserta como tipo F |
| **Empresas** | WS Listar Usuarios Sòstrat | Sin filtro tipo | Si no existe en PERSONES → inserta como tipo J |

Al seleccionar conductor: recupera NIF, nombre, apellidos, teléfono, ID Sòstrat.  
Al seleccionar empresa: recupera NIF, razón social, ID Sòstrat.

#### 4.2.4 Tabla Maestra — Tipos de Vehículo

Pantalla CRUD con GRID + Mantenimiento:
- Campo DESCRIPCIO (texto, obligatorio)
- 5 valores predefinidos: Portacontenedores, Portavehículos, Lonas, Cisternas, Bañeras

#### 4.2.5 Terminales Registradas

| Terminal | Notas |
|----------|-------|
| PORTCEMENT SA | |
| TRANSPORTES PORTUARIOS SA | |
| AUTOTERMINAL SA | |
| TERMINAL CATALUNYA SA | |
| BUNGE IBERICA SA | |
| APM TERMINALS BARCELONA, S.L.U. | Fix TRANSTE-1510 |
| BALEARIA EUROLINEAS MARTITIMAS SA | |
| TERMINAL FERRY BARCELONA SRLU | |
| CARGILL SLU | |
| AUTORITAT PORTUARIA DE BARCELONA | |
| GRIMALDI TERMINAL BARCELONA SL | Fix TRANSTE-1510 |
| BARCELONA CONTAINER DEPT SERVICE SL | |
| DELTA DEPOT BARCELONA SL | |

### 4.3 Eventos de Auditoría Funcional

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

### 4.4 Mensajes Funcionales

| Pantalla | Motivo | Mensaje |
|----------|--------|---------|
| Gestión Truck Center | Aviso camión duplicado | "Se ha detectado que el camión que quiere dar de alta aún está en el parking. ¿Quiere que se marque la anterior ocurrencia para poder dar de alta el actual?" |

### 4.5 Errores Funcionales

| Motivo | Error |
|--------|-------|
| Usuario cancela sacar camión anterior | "El registro del camión en el parking no se ha hecho" |

### 4.6 Autenticación y Roles (EntraID — TRANSTE-1520)

| Rol | Permisos |
|-----|----------|
| `USER_READ_TRUCK_CENTER` | Solo lectura (ver GRID, consultar mantenimiento) |
| `MANAGE_TRUCK_CENTER` | Alta, baja, modificación, asignar terminal, salir parking |
| `USER_TRUCK_CENTER` | Usuario estándar |
| `API_CALL_TRU_CONTROL_PUERTAS` | Permite llamar al WS Control de Puertas (IKUSI) |

### 4.7 Precondiciones Técnicas

- **Rollback**: si falla cualquier transacción → ROLLBACK completo + aviso usuario. Sin reintentos automáticos
- **Columnas BD**: aunque se definan en mixta, implementación siempre en MAYÚSCULAS
- **Multiidioma**: predeterminado catalán, personalizable por usuario

---

## 5. Incidencias Históricas Relevantes (Jira)

| Ticket | Descripción | Causa Raíz | Impacto |
|--------|-------------|------------|---------|
| TRANSTE-1534 | Lupas de usuarios no filtran datos | Bug en componente filtrado | Imposible buscar conductores/empresas |
| TRANSTE-1513 | Llamadas IKUSI sin matrícula generan error no controlado | Falta manejo caso "sin matrícula" | Eventos LPR no registrados |
| TRANSTE-1522 | idCamara cambió de 8 a 17 dígitos → error parsing | Integer overflow (Long requerido) | API rechaza llamadas IKUSI válidas |
| TRANSTE-1510 | Error al asignar ciertas terminales (APM, GRIMALDI...) | Bug en asignación terminal | Terminales no asignables en PRO |
| TRANSTE-1509 | Desplegable Terminal bloquea página | Carga TODOS los usuarios en lugar de solo actividad TU | Página inutilizable |
| SOSO-2075 | WS usuarios devuelve datos duplicados | Bug en servicio usuarios .NET | Afecta TRU + P33 + P51 + Escáner |
| TRANSTE-1530 | Vulnerabilidades altas SonarQube | Código inseguro detectado | Riesgo seguridad |

---

## 6. Proyectos Futuros

| Ticket | Proyecto | Alcance |
|--------|----------|---------|
| MISA-1434 | Smart gates y LPR | Nuevo LPR en salida, módulo MicroStrategy para facturación |
| MISA-1428 | Replicar a otros parkings | Modelo TRU → parkings TIR, FAR, San Beltrán |
| MISA-1381 | DSS Truck Center | Passos per porta, integración WS SICAD Rodados para facturación por terminal |
| RM-165 | Migración Cloud | Transformación y migración a Azure |
| MISA-1471 | Migración Cloud Docks | Incluye TRU en migración global Docks |

---

## 7. Plan de Pruebas

### Bloque 1: API ControlPuertas — Recepción LPR (12 casos)

| ID | Caso | Precondición | Entrada | Resultado Esperado | Prioridad |
|----|------|-------------|---------|-------------------|-----------|
| TRU-T01 | Entrada normal con matrícula | Matrícula no existe en parking | JSON: acceso=24, carril=90, fecha, matricula=1234ABC | Nuevo registro en TRUCK_CENTER: FASE=`EN EL PARKING`, CONEXIO_ELECTRICITAT=0, ITV=0, HORA_ENTRADA=fecha_param. Evento `TRU_CREACION_TRUCK_CENTER_OK` | **Crítica** |
| TRU-T02 | Salida normal con matrícula | Registro existente `EN EL PARKING` para 1234ABC | JSON: acceso=24, carril=91, fecha, matricula=1234ABC | `HORA_SORTIDA = fecha_param`, `FASE = FORA DEL PARKING`. Evento `TRU_SALIR_PARKING_OK` | **Crítica** |
| TRU-T03 | Entrada duplicada — camión aún en parking | Registro existente `EN EL PARKING` para 1234ABC | JSON: acceso=24, carril=90, matricula=1234ABC | Anterior cerrado (HORA_SORTIDA=now-1s, FASE=FORA DEL PARKING) + Nuevo creado EN EL PARKING. Dos eventos generados | **Crítica** |
| TRU-T04 | Salida sin registro previo | No existe registro activo para matrícula | JSON: acceso=24, carril=91, matricula=9999ZZZ | Sin error (no encuentra registro, no hace nada). No genera evento KO | **Alta** |
| TRU-T05 | Lectura sin matrícula (NOMATRI) | Cámara no detecta matrícula | JSON: matricula ausente o vacía | Evento `TRU_CONTROL_PUERTAS_KO` con texto "Matricula:NOMATRI" | **Crítica** |
| TRU-T06 | idCamara 17 dígitos (nuevo formato) | — | JSON con idCamara de 17 números | Sin error de parsing (fix TRANSTE-1522) | **Alta** |
| TRU-T07 | idCamara 8 dígitos (formato legacy) | — | JSON con idCamara de 8 números | Sin error, retrocompatible | **Alta** |
| TRU-T08 | Campos no utilizados con valores extremos | — | JSON con campos extra largos/inusuales en campos ignorados | Solo se validan los 4 campos usados, resto ignorado (TRANSTE-1523) | **Media** |
| TRU-T09 | JSON malformado | — | JSON inválido/truncado | Error HTTP 400 controlado, no excepción 500 | **Alta** |
| TRU-T10 | Llamada sin permiso API_CALL_TRU_CONTROL_PUERTAS | Token sin permiso | JSON válido | Error 401/403 — acceso denegado | **Crítica** |
| TRU-T11 | Verificar HORA_SORTIDA exacta anterior = now - 1 segundo | Duplicado entrada | Dos entradas consecutivas misma matrícula | HORA_SORTIDA del primer registro = HORA_ENTRADA del segundo - 1 segundo exacto | **Alta** |
| TRU-T12 | Campos de salida API | — | Llamada válida | Respuesta contiene status correcto o error (según AF: "ninguno o el error") | **Media** |

### Bloque 2: GRID Principal (14 casos)

| ID | Caso | Precondición | Entrada | Resultado Esperado | Prioridad |
|----|------|-------------|---------|-------------------|-----------|
| TRU-T13 | Columnas por defecto visibles | Acceso con permisos | Abrir Truck Center | 9 columnas visibles en orden: Id, Matrícula, Entrada, Salida, Terminal, Nombre, Apellido1, Apellido2, Empresa | **Crítica** |
| TRU-T14 | Ordenación por defecto | Múltiples registros | Abrir GRID | Registros ordenados de más nuevo a más viejo | **Alta** |
| TRU-T15 | Selector de Columnas — campos añadibles | — | Abrir Selector | Disponibles: Fase, NIF Terminal, Id Usuari Terminal, NIF Conductor, Id Usuari Conductor, NIF Empresa, Id Usuari Empresa, Conexión Electricidad, ITV, Observaciones | **Alta** |
| TRU-T16 | Columnas auditoría en Selector | — | Abrir Selector | APB_CREADOR, APB_MODIFICADOR, APB_CREAT, APB_MODIFICAT disponibles y filtrables por lupa (TRANSTE-1515) | **Alta** |
| TRU-T17 | Filtro por lupa en cada columna | Columna visible | Usar lupa para filtrar | Filtrado correcto en TODAS las columnas (defecto + añadibles) | **Alta** |
| TRU-T18 | Botón Refresco GRID | Datos actualizados en BD | Clic botón refresco | GRID actualizado sin recargar página completa (TRANSTE-1511) | **Alta** |
| TRU-T19 | Acción "Salir del Parking" desde GRID | Registro seleccionado en fase `EN EL PARKING` | Ejecutar acción | HORA_SORTIDA=now, FASE=FORA DEL PARKING. Evento `TRU_SALIR_PARKING_OK` | **Crítica** |
| TRU-T20 | "Salir del Parking" — registro no seleccionado | Ningún registro seleccionado | Intentar acción | Acción no disponible o mensaje de error | **Alta** |
| TRU-T21 | "Salir del Parking" — registro ya FORA DEL PARKING | Registro en fase `FORA DEL PARKING` | Intentar acción | Acción no visible/no permitida | **Alta** |
| TRU-T22 | Exportar a Excel — todos los campos | Registros en GRID | Exportar | Excel contiene TODOS los campos (9 defecto + 10 añadibles + 4 auditoría) con datos correctos | **Alta** |
| TRU-T23 | Exportar a Excel — GRID vacío | Sin registros | Exportar | Excel generado vacío o con cabeceras, sin error | **Media** |
| TRU-T24 | Acceso GRID con USER_READ | Login USER_READ_TRUCK_CENTER | Abrir GRID | Puede ver datos. Acción "Salir del Parking" NO disponible | **Crítica** |
| TRU-T25 | Acceso GRID con MANAGE | Login MANAGE_TRUCK_CENTER | Abrir GRID | Puede ver datos + acciones de gestión disponibles | **Crítica** |
| TRU-T26 | Pestaña navegador | Acceso a cualquier pantalla | Ver título pestaña | Muestra "Truck Center" (no "Aplicación de Arquitectura APB" — TRANSTE-1517) | **Media** |

### Bloque 3: Pantalla de Mantenimiento — Alta (16 casos)

| ID | Caso | Precondición | Entrada | Resultado Esperado | Prioridad |
|----|------|-------------|---------|-------------------|-----------|
| TRU-T27 | Alta mínima (solo obligatorios) | Rol MANAGE | Matrícula + Tipo Vehículo + Hora Entrada | Registro creado, FASE=EN EL PARKING, checkboxes a 0. Evento `TRU_CREACION_TRUCK_CENTER_OK` | **Crítica** |
| TRU-T28 | Alta completa (todos los campos) | Rol MANAGE | Todos los campos rellenos | Registro creado con todos los datos. Verificar cada columna en BD | **Crítica** |
| TRU-T29 | Alta sin matrícula | Rol MANAGE | Matrícula vacía | Validación: campo obligatorio, no permite guardar | **Crítica** |
| TRU-T30 | Alta sin tipo vehículo | Rol MANAGE | Tipo vehículo sin seleccionar | Validación: campo obligatorio, no permite guardar | **Alta** |
| TRU-T31 | Alta sin hora entrada | Rol MANAGE | Hora entrada vacía | Validación: campo obligatorio, no permite guardar | **Alta** |
| TRU-T32 | Alta duplicado — usuario CONFIRMA | Existe registro activo misma matrícula | Alta con matrícula duplicada → Sí | Mensaje aviso. Anterior: HORA_SORTIDA=now-1s, FASE=FORA DEL PARKING. Nuevo creado | **Crítica** |
| TRU-T33 | Alta duplicado — usuario CANCELA | Existe registro activo misma matrícula | Alta con matrícula duplicada → No | Mensaje "El registro del camión en el parking no se ha hecho". No se crea registro | **Crítica** |
| TRU-T34 | Matrícula existente en CAMIONS | Matrícula con tipo vehículo ya registrado | Introducir matrícula existente | Tipo de Vehículo auto-recuperado de CAMIONS, editable | **Alta** |
| TRU-T35 | Matrícula nueva (no existe en CAMIONS) | Primera vez de esta matrícula | Introducir matrícula nueva | Tipo Vehículo vacío, usuario debe seleccionar. Nueva entrada en CAMIONS al guardar | **Alta** |
| TRU-T36 | Modificar tipo vehículo recuperado | Matrícula existente con tipo recuperado | Cambiar desplegable tipo vehículo | Se actualiza tanto en expediente como en tabla CAMIONS | **Alta** |
| TRU-T37 | Botón Reloj Entrada | — | Clic botón reloj | Hora entrada = fecha/hora actual del sistema | **Media** |
| TRU-T38 | Checkbox Conexión Electricidad | — | Marcar checkbox | Valor 1 en BD, desmarcado = 0 | **Media** |
| TRU-T39 | Checkbox ITV | — | Marcar checkbox | Valor 1 en BD, desmarcado = 0 | **Media** |
| TRU-T40 | Checkbox Mercancías Peligrosas | — | Marcar checkbox | Valor 1 en BD (MERCADERIES_PERILLOSES), desmarcado = 0 | **Media** |
| TRU-T41 | Observaciones — texto largo (4000 chars) | — | Introducir 4000 caracteres | Se guarda completo sin truncar | **Media** |
| TRU-T42 | Rol USER_READ no puede crear | Login USER_READ | Intentar alta | Botón alta no visible o acción denegada | **Crítica** |

### Bloque 4: Pantalla de Mantenimiento — Modificación y Baja (8 casos)

| ID | Caso | Precondición | Entrada | Resultado Esperado | Prioridad |
|----|------|-------------|---------|-------------------|-----------|
| TRU-T43 | Modificar registro existente | Rol MANAGE, registro EN EL PARKING | Cambiar terminal, observaciones | Datos actualizados. Evento `TRU_MODIFICACION_TRUCK_CENTER_OK` | **Crítica** |
| TRU-T44 | Campos solo lectura no editables | Registro existente | Intentar editar ID, Fase, Empresa Transporte (razón social), Id Usuario Conductor/Transporte | Campos no editables | **Alta** |
| TRU-T45 | Botón "Salir del Parking" desde mantenimiento | Registro EN EL PARKING | Clic botón | HORA_SORTIDA=now, FASE=FORA DEL PARKING. Evento `TRU_SALIR_PARKING_OK` | **Crítica** |
| TRU-T46 | Botón "Salir del Parking" no visible en FORA DEL PARKING | Registro FORA DEL PARKING | Abrir mantenimiento | Botón no visible | **Alta** |
| TRU-T47 | Baja de registro | Rol MANAGE | Eliminar registro | Registro eliminado, evento correspondiente | **Alta** |
| TRU-T48 | Modificar con USER_READ | Login USER_READ | Intentar modificar | Solo consulta, modificación denegada | **Crítica** |
| TRU-T49 | Rollback en error transaccional | Error de BD durante guardado | Guardar con error forzado | ROLLBACK completo, aviso usuario, datos no persistidos parcialmente | **Crítica** |
| TRU-T50 | Sin reintento automático tras error | Error previo | Verificar comportamiento post-error | No hay reintento automático; usuario debe volver a ejecutar | **Alta** |

### Bloque 5: Lupas — Conductores y Empresas (12 casos)

| ID | Caso | Precondición | Entrada | Resultado Esperado | Prioridad |
|----|------|-------------|---------|-------------------|-----------|
| TRU-T51 | Lupa conductores — búsqueda y selección | WS Sòstrat disponible | Buscar por nombre | Lista de personas tipo F. Seleccionar → recupera NIF, nombre, apellidos, teléfono, ID Sòstrat | **Crítica** |
| TRU-T52 | Lupa conductores — conductor nuevo en PERSONES | Conductor no existe en tabla PERSONES | Seleccionar conductor | Se inserta automáticamente en PERSONES como TIPUS_PERSONA=F con datos de Sòstrat | **Crítica** |
| TRU-T53 | Lupa conductores — conductor ya existente en PERSONES | Conductor ya en PERSONES | Seleccionar conductor | Se recuperan datos de PERSONES, no se duplica | **Alta** |
| TRU-T54 | Lupa conductores — filtrado funciona | — | Escribir texto filtro | Resultados filtrados correctamente (fix TRANSTE-1534) | **Crítica** |
| TRU-T55 | Lupa empresas — búsqueda y selección | WS Sòstrat disponible | Buscar empresa | Lista sin filtro de tipo. Seleccionar → recupera NIF, razón social, ID Sòstrat | **Crítica** |
| TRU-T56 | Lupa empresas — empresa nueva en PERSONES | Empresa no existe en PERSONES | Seleccionar empresa | Se inserta en PERSONES como TIPUS_PERSONA=J | **Crítica** |
| TRU-T57 | Lupa empresas — empresa ya existente | Empresa ya en PERSONES | Seleccionar empresa | Se recuperan datos, no se duplica | **Alta** |
| TRU-T58 | Lupa empresas — filtrado funciona | — | Escribir texto filtro | Resultados filtrados correctamente (fix TRANSTE-1534) | **Crítica** |
| TRU-T59 | WS Sòstrat no disponible | Servicio caído | Abrir lupa | Mensaje error controlado, no excepción no manejada | **Alta** |
| TRU-T60 | Datos duplicados WS usuarios | — | Cargar lupa | Sin duplicados en resultados (fix SOSO-2075) | **Alta** |
| TRU-T61 | Escritura manual conductor (sin lupa) | — | Escribir NIF, nombre, apellidos manualmente | Se permite sin usar lupa, datos guardados correctamente | **Media** |
| TRU-T62 | Escritura manual empresa (sin lupa) | — | Escribir NIF empresa manualmente | Se permite | **Media** |

### Bloque 6: Desplegable Terminales (8 casos)

| ID | Caso | Precondición | Entrada | Resultado Esperado | Prioridad |
|----|------|-------------|---------|-------------------|-----------|
| TRU-T63 | Desplegable solo actividad TU | WS Sòstrat disponible | Clic desplegable Terminal | Solo muestra usuarios con actividad TU (no todos) | **Crítica** |
| TRU-T64 | Desplegable no bloquea página | Muchos usuarios en Sòstrat | Clic desplegable | Página responde fluidamente, sin bloqueo (fix TRANSTE-1509) | **Crítica** |
| TRU-T65 | Asignar PORTCEMENT SA | — | Seleccionar terminal | Asignación correcta, guardado OK | **Alta** |
| TRU-T66 | Asignar APM TERMINALS | — | Seleccionar terminal | Asignación correcta (fix TRANSTE-1510) | **Alta** |
| TRU-T67 | Asignar GRIMALDI | — | Seleccionar terminal | Asignación correcta (fix TRANSTE-1510) | **Alta** |
| TRU-T68 | Asignar AUTOTERMINAL SA | — | Seleccionar terminal | Asignación correcta (fix TRANSTE-1510) | **Alta** |
| TRU-T69 | Asignar cada una de las 13 terminales | — | Iterar 13 terminales | Todas asignables sin error | **Alta** |
| TRU-T70 | Desplegable sin servicio Sòstrat | Servicio caído | Clic desplegable | Error controlado, no bloqueo | **Media** |

### Bloque 7: Tabla Maestra — Tipos de Vehículo (6 casos)

| ID | Caso | Precondición | Entrada | Resultado Esperado | Prioridad |
|----|------|-------------|---------|-------------------|-----------|
| TRU-T71 | GRID tipos vehículo — 5 registros iniciales | — | Abrir tabla maestra | Portacontenedores, Portavehículos, Lonas, Cisternas, Bañeras | **Alta** |
| TRU-T72 | Alta nuevo tipo vehículo | Rol MANAGE | Crear tipo "Frigoríficos" | Nuevo tipo creado, visible en GRID y en desplegable Mantenimiento | **Alta** |
| TRU-T73 | Modificar tipo existente | Rol MANAGE | Cambiar descripción | Descripción actualizada | **Media** |
| TRU-T74 | Eliminar tipo sin dependencias | Rol MANAGE, tipo sin camiones asociados | Eliminar tipo | Eliminado correctamente | **Media** |
| TRU-T75 | Eliminar tipo con dependencias | Tipo con camiones asociados en CAMIONS | Intentar eliminar | Error controlado: no se permite eliminar por integridad referencial | **Alta** |
| TRU-T76 | USER_READ no puede modificar maestro | Login USER_READ | Intentar CRUD | Solo consulta permitida | **Alta** |

### Bloque 8: Autenticación y Permisos EntraID (10 casos)

| ID | Caso | Precondición | Entrada | Resultado Esperado | Prioridad |
|----|------|-------------|---------|-------------------|-----------|
| TRU-T77 | Login con EntraID exitoso | Credenciales válidas | Login | Acceso concedido según rol asignado | **Crítica** |
| TRU-T78 | Rol USER_READ — solo lectura completa | Login USER_READ_TRUCK_CENTER | Navegar toda la app | Ver GRID + consultar mantenimiento. NO alta/baja/modificación/salir parking | **Crítica** |
| TRU-T79 | Rol MANAGE — gestión completa | Login MANAGE_TRUCK_CENTER | Navegar toda la app | Alta, baja, modificación, asignar terminal, salir parking, gestionar maestros | **Crítica** |
| TRU-T80 | Rol USER — usuario estándar | Login USER_TRUCK_CENTER | Navegar | Acceso según permisos definidos para este nivel | **Alta** |
| TRU-T81 | Sin rol TRU | Login usuario sin ningún rol TRU | Acceder a TRU | Acceso denegado, sin ver menú TRU | **Crítica** |
| TRU-T82 | Token expirado | Sesión caducada | Navegar | Redirección a login EntraID | **Alta** |
| TRU-T83 | Idioma predeterminado catalán | Nuevo usuario sin preferencia | Acceder | Interfaz en catalán | **Media** |
| TRU-T84 | Cambio de idioma en perfil | Usuario con preferencia ES/EN | Acceder | Interfaz en idioma seleccionado | **Media** |
| TRU-T85 | AppRegistration External ID configurada | — | Verificar config Azure | AppRegistration TRU correcta en External ID (ARQ-2157) | **Alta** |
| TRU-T86 | Tokens correctos tras renombrado API | APIs renombradas (ARQ-2444) | Login + llamadas API | Tokens apuntan a app TRU correcta (TRANSTE-1527) | **Alta** |

### Bloque 9: Eventos de Auditoría (8 casos)

| ID | Caso | Precondición | Entrada | Resultado Esperado | Prioridad |
|----|------|-------------|---------|-------------------|-----------|
| TRU-T87 | Evento creación OK | Alta exitosa | Crear registro | `TRU_CREACION_TRUCK_CENTER_OK` con ID en pantalla de eventos TRU (no ARQ — TRANSTE-1524) | **Crítica** |
| TRU-T88 | Evento creación KO | Error en alta | Forzar error | `TRU_CREACION_TRUCK_CENTER_KO` registrado | **Alta** |
| TRU-T89 | Evento modificación OK | Modificación exitosa | Modificar registro | `TRU_MODIFICACION_TRUCK_CENTER_OK` con ID | **Alta** |
| TRU-T90 | Evento modificación KO | Error en modificación | Forzar error | `TRU_MODIFICACION_TRUCK_CENTER_KO` registrado | **Alta** |
| TRU-T91 | Evento control puertas OK | Entrada/salida LPR | Llamada API válida | `TRU_CONTROL_PUERTAS_OK` con datos completos: tarjeta/acceso/carril/fecha/matrícula | **Crítica** |
| TRU-T92 | Evento control puertas KO | Sin matrícula | Llamada sin matrícula | `TRU_CONTROL_PUERTAS_KO` con "NOMATRI" | **Alta** |
| TRU-T93 | Evento salir parking OK | Salida exitosa | Botón salir parking | `TRU_SALIR_PARKING_OK` con matrícula e ID | **Alta** |
| TRU-T94 | Eventos visibles en dominio TRU | — | Abrir pantalla eventos | Eventos en sección TRU propia, no en pantalla ARQ genérica (TRANSTE-1524) | **Alta** |

### Bloque 10: Integración WS ARQ Docks (6 casos)

| ID | Caso | Precondición | Entrada | Resultado Esperado | Prioridad |
|----|------|-------------|---------|-------------------|-----------|
| TRU-T95 | Expediente Docks creado | Alta registro TRU | Crear registro | Expediente visible en pantalla común de expedientes Docks | **Alta** |
| TRU-T96 | Fases expediente correctas | Expediente existente | Verificar fases | Solo 2 fases: EN EL PARKING → FORA DEL PARKING | **Alta** |
| TRU-T97 | Menú contextual funcional | — | Clic derecho en registro | Menú contextual Docks operativo | **Media** |
| TRU-T98 | Pantalla errores Docks | Error funcional | Provocar error | Error visible en pantalla común de errores | **Media** |
| TRU-T99 | Mensajes Docks funcionales | Duplicado matrícula | Alta duplicado | Mensaje aviso correcto vía framework Docks | **Alta** |
| TRU-T100 | WS ARQ todos operativos | — | Verificar 7 WS | ARQ_APPFASES, EVENTOS, MENSAJES, ERRORES, LOGIN_CAS, LOGIN_TOKEN, FASES responden OK | **Alta** |

### Bloque 11: Seguridad y Calidad de Código (6 casos)

| ID | Caso | Precondición | Entrada | Resultado Esperado | Prioridad |
|----|------|-------------|---------|-------------------|-----------|
| TRU-T101 | SonarQube sin vulnerabilidades altas | Escaneo SonarQube | Analizar código | Sin vulnerabilidades altas (fix TRANSTE-1530) | **Crítica** |
| TRU-T102 | No inyección SQL en lupas | — | SQL injection en búsqueda conductores/empresas | Input sanitizado, sin efecto | **Crítica** |
| TRU-T103 | No XSS en observaciones | — | Script en campo observaciones | Input sanitizado, script no ejecutado | **Crítica** |
| TRU-T104 | No XSS en matrícula | — | Script en campo matrícula | Input sanitizado | **Alta** |
| TRU-T105 | Validación largo campos según modelo datos | — | Matrícula > 10 chars, Observaciones > 4000 chars, NIF > 11 chars | Validación o truncamiento controlado, sin error BD | **Alta** |
| TRU-T106 | HTTPS en todos los endpoints | — | Verificar TLS | PRE y PRO usan HTTPS exclusivamente | **Alta** |

### Bloque 12: Regresión, Despliegue y E2E (6 casos)

| ID | Caso | Precondición | Entrada | Resultado Esperado | Prioridad |
|----|------|-------------|---------|-------------------|-----------|
| TRU-T107 | Health check API LGP | API desplegada | GET endpoint TRC | 200 OK | **Crítica** |
| TRU-T108 | Health check APP TRU | App desplegada | GET endpoint TRU web | 200 OK | **Crítica** |
| TRU-T109 | Nomenclatura APIs post-renombrado | Deploy completado | Verificar IIS/Jenkins/pipelines | APB.API.LGP y APB.API.TRU (no nombres antiguos TRU.LGP / TRU.TRC) | **Alta** |
| TRU-T110 | Repositorio APB.TRU | GitHub | Verificar repo | Nombre correcto APB.TRU, pipelines apuntan al nuevo repo | **Alta** |
| TRU-T111 | E2E completo: Entrada LPR → GRID → Asignar Terminal → Salida LPR | Todo operativo | 1. IKUSI envía entrada 2. Verificar GRID 3. Asignar terminal + conductor 4. IKUSI envía salida | Registro completo con entrada, terminal, conductor, empresa, salida. Todos los eventos generados | **Crítica** |
| TRU-T112 | E2E completo: Alta manual → Modificar → Salir Parking | Todo operativo | 1. Alta manual 2. Asignar datos 3. Botón Salir Parking | Registro con flujo completo manual. Eventos creación + modificación + salida | **Crítica** |

---

## 8. Resumen del Plan de Pruebas

| Bloque | Descripción | Casos | Crítica | Alta | Media |
|--------|-------------|-------|---------|------|-------|
| 1 | API ControlPuertas — Recepción LPR | 12 | 4 | 5 | 3 |
| 2 | GRID Principal | 14 | 4 | 7 | 3 |
| 3 | Mantenimiento — Alta | 16 | 7 | 5 | 4 |
| 4 | Mantenimiento — Modificación y Baja | 8 | 4 | 3 | 1 |
| 5 | Lupas — Conductores y Empresas | 12 | 6 | 4 | 2 |
| 6 | Desplegable Terminales | 8 | 2 | 5 | 1 |
| 7 | Tabla Maestra — Tipos de Vehículo | 6 | 0 | 4 | 2 |
| 8 | Autenticación y Permisos EntraID | 10 | 4 | 4 | 2 |
| 9 | Eventos de Auditoría | 8 | 2 | 6 | 0 |
| 10 | Integración WS ARQ Docks | 6 | 0 | 4 | 2 |
| 11 | Seguridad y Calidad de Código | 6 | 3 | 2 | 1 |
| 12 | Regresión, Despliegue y E2E | 6 | 4 | 2 | 0 |
| **TOTAL** | | **112** | **40** | **51** | **21** |

---

## 9. Tickets Jira Analizados

TRANSTE-1534, TRANSTE-1530, TRANSTE-1527, TRANSTE-1524, TRANSTE-1523, TRANSTE-1522, TRANSTE-1520, TRANSTE-1517, TRANSTE-1515, TRANSTE-1513, TRANSTE-1511, TRANSTE-1510, TRANSTE-1509, TRANSTE-1507, TRANSTE-1506, ARQ-2929, ARQ-2926, ARQ-2795, ARQ-2779, ARQ-2447, ARQ-2444, ARQ-2421, ARQ-2346, ARQ-2315, ARQ-2238, ARQ-2157, ARQ-1621, ARQ-1619, ARQ-1511, ARQ-1507, ARQ-1336, ARQ-1320, ARQ-1317, ARQ-1166, ARQ-1162, ARQ-1106, ARQ-1105, ARQ-1087, ARQ-1030, ARQ-927, ARQ-924, PVI-2, RM-165, GS-801, MISA-1567, MISA-1471, MISA-1434, MISA-1428, MISA-1381, MISA-1346, SOSO-2075

---

## 10. Documentos de Referencia

| Documento | Versión | Fecha | Fuente |
|-----------|---------|-------|--------|
| AF Truck Center | v1.1 | 03/02/2023 (rev. 22/07/2025) | Análisis Funcional oficial — incluye modelo de datos, reglas de negocio, pantallas, eventos |
| AF Truck Center - Modelo de Datos | — | 01/07/2026 | Diagrama Visio entidades lógicas |
| Cambios en DOCKS para integración con Microsoft EntraID SSO | v1.1 | — | Especificaciones migración autenticación |
