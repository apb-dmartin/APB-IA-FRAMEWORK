# QA — TRU-TruckCenter (APB.API.LGP + APB.API.TRU)

> **Generado automáticamente** como Ingeniero QA · Fecha: 2026-06-30
> **Fuentes:** ~50 tickets Jira (TRANSTE, ARQ, MISA, GS, RM, PVI, SOSO, LNVB)

---

## 1. Descripción General

**TRU** (Truck Center) es una aplicación del ecosistema DOCKS (.NET) que gestiona el **control de acceso y registro de camiones** en el Truck Center de la Autoridad Portuaria de Barcelona. Integra lecturas de matrículas (LPR) de cámaras IKUSI con un panel de gestión de entradas/salidas y asignación a terminales.

### 1.1 APIs

| API | Función | Endpoint PRE | Endpoint PRO |
|-----|---------|-------------|-------------|
| **APB.API.LGP** | API de control de puertas (recepción datos LPR/IKUSI) | `https://apipre.portdebarcelona.cat/trc/` | `https://api.portdebarcelona.cat/trc/` |
| **APB.API.TRU** | Aplicación web Truck Center (frontend + backend) | `https://dockspre.portdebarcelona.cat/tru/` | `https://docks.portdebarcelona.cat/tru/` |

**Nota:** Renombrado en abril 2025 (ARQ-2444): `APB.API.TRU.LGP` → `APB.API.LGP` y `APB.API.TRU.TRC` → `APB.API.TRU`

### 1.2 Arquitectura

```
Cámaras LPR IKUSI
    │
    │ JSON (acceso, carril, fecha, matricula)
    ▼
┌──────────────────────────┐
│  APB.API.LGP (.NET)       │  ← API Control de Puertas
│  POST /api/v1/TruckCenter │
│        /ControlPuertas     │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│  Oracle (TRUCK_CENTER)    │  ← Tabla principal
└──────────────────────────┘
           ▲
           │
┌──────────┴───────────────┐
│  APB.API.TRU (.NET)       │  ← Aplicación Web
│  Frontend MVC             │
│  GRID principal           │
│  Lupas: Conductores,      │
│         Empresas           │
│  Desplegable: Terminales   │
│  Acciones: Asignar        │
│            terminal,       │
│            Refrescar       │
└──────────────────────────┘
           │
           ▼
    Usuarios DOCKS
    (EntraID desde 2025)
```

### 1.3 Repositorio GitHub

Renombrado de TRU a `APB.TRU` (TRANSTE-1527)

---

## 2. Funcionalidad Detallada

### 2.1 API ControlPuertas (APB.API.LGP)

**POST /api/v1/TruckCenter/ControlPuertas**

Recibe JSON de cámaras IKUSI con datos de lectura de matrículas:

**Campos utilizados (validados):**
- `acceso` — Tipo de acceso (entrada/salida)
- `carril` — Número de carril
- `fecha` — Fecha/hora de lectura
- `lecturasMatricula.matricula` — Matrícula del camión

**Campos no utilizados (se ignoran, sin validación):**
- `idCamara` — Cambió de Integer (8 dígitos) a Long (17 dígitos) (TRANSTE-1522)
- Resto de campos del JSON

**Eventos generados:**
- `TRU_CONTROL_PUERTAS_OK` — Procesado correctamente
- `TRU_CONTROL_PUERTAS_KO` — Sin matrícula: texto incluye "Matricula:**NOMATRI**" (TRANSTE-1513)

### 2.2 Gestión de Matrículas sin Lectura (TRANSTE-1513)

Cuando la cámara no detecta matrícula:
- Se genera evento controlado `TRU_CONTROL_PUERTAS_KO`
- Texto: `Control de Acceso OK:Número tarjeta:/Acceso:24/Carril:90/Fecha:29/4/2024 13:14:56/Matricula:NOMATRI`

### 2.3 Campo idCamara (TRANSTE-1522)

- Cambio de formato: 8 números (Integer) → 17 números (Long)
- Aunque no se usa en lógica de negocio, el JSON lo incluye
- Se modificó para que el cambio de tamaño no provoque error de parsing

### 2.4 Aplicación Web (APB.API.TRU)

#### GRID Principal
- Muestra registros de Truck Center (entradas/salidas)
- Columnas de auditoría añadidas al Selector de Columnas (TRANSTE-1515):
  - `APB_CREADOR`, `APB_MODIFICADOR`, `APB_CREAT`, `APB_MODIFICAT`
  - Todas con filtro por lupa
- **Botón de Refresco** en GRID (TRANSTE-1511)

#### Lupas
- **Lupa Conductores** — Búsqueda de conductores
- **Lupa Empresas** — Búsqueda de empresas
- **Bug TRANSTE-1534:** Las lupas no filtraban datos → Corregido

#### Desplegable de Terminales
- Solo muestra usuarios con actividad **TU**
- **Bug TRANSTE-1509:** Desplegable cargaba TODOS los usuarios → página bloqueada
- **Bug TRANSTE-1510:** Error al asignar ciertas terminales (PORTCEMENT, APM TERMINALS, GRIMALDI, etc.)

### 2.5 Terminales Registradas

| Terminal |
|----------|
| PORTCEMENT SA |
| TRANSPORTES PORTUARIOS SA |
| AUTOTERMINAL SA |
| TERMINAL CATALUNYA SA |
| BUNGE IBERICA SA |
| APM TERMINALS BARCELONA, S.L.U. |
| BALEARIA EUROLINEAS MARTITIMAS SA |
| TERMINAL FERRY BARCELONA SRLU |
| CARGILL SLU |
| AUTORITAT PORTUARIA DE BARCELONA |
| GRIMALDI TERMINAL BARCELONA SL |
| BARCELONA CONTAINER DEPT SERVICE SL |
| DELTA DEPOT BARCELONA SL |

### 2.6 Autenticación EntraID (TRANSTE-1520)

Migración de autenticación CAS/LDAP a **Microsoft EntraID** (External ID):
- **Roles definidos:**
  - `USER_READ_TRUCK_CENTER` — Solo lectura
  - `MANAGE_TRUCK_CENTER` — Gestión completa
  - `USER_TRUCK_CENTER` — Usuario estándar
- Soporte ARQ para creación de AppRegistration en External ID (ARQ-2157)
- Documento de especificaciones: "Cambios en DOCKS para integración con Microsoft EntraID SSO_v1.1"

### 2.7 Refactorización (TRANSTE-1527)

- Mejora y alineamiento de código de APIs
- Cambio de nomenclatura de API
- Cambio de repositorio: TRU → APB.TRU
- Cambio de tokens para apuntar a app TRU
- Valoración: 6h

### 2.8 Vulnerabilidades SonarQube (TRANSTE-1530)

Corrección de vulnerabilidades altas detectadas por SonarQube. Refactorización para cobertura.

### 2.9 Pestaña Navegador (TRANSTE-1517)

Cambio literal de "Aplicación de Arquitectura APB" a "Truck Center".

### 2.10 Eventos de Dominio (TRANSTE-1524)

Mover eventos de negocio de TRU de la pantalla ARQ a eventos de dominio propios.

### 2.11 Proyectos Futuros

- **MISA-1434:** Truck Center, smart gates y LPR — nuevo LPR en salida, módulo de explotación MicroStrategy para facturación
- **MISA-1428:** Replicar modelo Truck Center a parkings TIR, FAR y San Beltrán
- **MISA-1381:** DSS Truck Center — passos per porta, integración con WS SICAD Rodados para facturación por terminal
- **RM-165:** Transformación y migración Cloud de Truck Center
- **MISA-1471:** Migración Cloud aplicaciones Docks (incluye TRU)

### 2.12 Datos Duplicados WS Usuarios (SOSO-2075)

Bug en WS de usuarios .NET que devolvía datos duplicados, afectaba a Truck Center, P33, P51, Escáner.

---

## 3. Incidencias Históricas Relevantes

| Ticket | Descripción | Causa Raíz | Impacto |
|--------|-------------|------------|---------|
| TRANSTE-1534 | Lupas de usuarios no filtran | Bug en filtrado | Usuarios no pueden buscar conductores/empresas |
| TRANSTE-1513 | Llamadas IKUSI sin matrícula dan error no controlado | Falta manejo de caso "sin matrícula" | Eventos no registrados |
| TRANSTE-1522 | idCamara cambió de 8 a 17 dígitos, error parsing | Integer overflow | API rechaza llamadas IKUSI |
| TRANSTE-1510 | Error al asignar terminales en PRO | Bug en asignación | Terminales no asignables |
| TRANSTE-1509 | Desplegable Terminal bloquea página | Carga todos los usuarios en lugar de solo actividad TU | Página inutilizable |
| SOSO-2075 | WS usuarios devuelve datos duplicados | Bug en servicio usuarios .NET | Afecta Truck Center y otras apps |

---

## 4. Plan de Pruebas

### Bloque 1: API ControlPuertas (LGP)

| ID | Caso | Entrada | Resultado Esperado |
|----|------|---------|-------------------|
| TRU-T01 | Lectura entrada con matrícula | JSON: acceso=entrada, carril=1, fecha, matricula=1234ABC | Registro creado en TRUCK_CENTER, evento OK |
| TRU-T02 | Lectura salida con matrícula | JSON: acceso=salida, carril=2, fecha, matricula=1234ABC | Registro actualizado, evento OK |
| TRU-T03 | Lectura sin matrícula | JSON: matricula ausente o vacía | Evento `TRU_CONTROL_PUERTAS_KO` con texto "NOMATRI" |
| TRU-T04 | idCamara 17 dígitos | JSON con idCamara de 17 números | Sin error de parsing (fix TRANSTE-1522) |
| TRU-T05 | idCamara 8 dígitos (legacy) | JSON con idCamara de 8 números | Sin error, retrocompatible |
| TRU-T06 | Campos no utilizados con valores extremos | JSON con campos extra largos/inusuales | Solo se validan los 4 campos usados (fix TRANSTE-1523) |
| TRU-T07 | JSON malformado | JSON inválido | Error 400 controlado |

### Bloque 2: Aplicación Web — GRID

| ID | Caso | Entrada | Resultado Esperado |
|----|------|---------|-------------------|
| TRU-T08 | Visualizar GRID principal | Acceso a Truck Center | Registros mostrados con datos correctos |
| TRU-T09 | Columnas auditoría en Selector | Abrir Selector de Columnas | APB_CREADOR, APB_MODIFICADOR, APB_CREAT, APB_MODIFICAT disponibles |
| TRU-T10 | Filtro por lupa en columnas auditoría | Filtrar por APB_CREADOR | Filtrado correcto |
| TRU-T11 | Botón Refresco | Clic botón refresco | GRID actualizado sin recargar página |

### Bloque 3: Lupas y Desplegables

| ID | Caso | Entrada | Resultado Esperado |
|----|------|---------|-------------------|
| TRU-T12 | Lupa Conductores filtra | Buscar texto en lupa | Resultados filtrados correctamente (fix TRANSTE-1534) |
| TRU-T13 | Lupa Empresas filtra | Buscar empresa | Resultados filtrados correctamente (fix TRANSTE-1534) |
| TRU-T14 | Desplegable Terminal solo actividad TU | Clic en desplegable Terminal | Solo 18 usuarios con actividad TU (no todos) |
| TRU-T15 | Desplegable no bloquea página | Clic en desplegable con muchos usuarios | Página responde fluidamente (fix TRANSTE-1509) |

### Bloque 4: Asignación de Terminales

| ID | Caso | Entrada | Resultado Esperado |
|----|------|---------|-------------------|
| TRU-T16 | Asignar PORTCEMENT SA | Seleccionar terminal | Asignación correcta |
| TRU-T17 | Asignar APM TERMINALS | Seleccionar terminal | Asignación correcta (fix TRANSTE-1510) |
| TRU-T18 | Asignar GRIMALDI | Seleccionar terminal | Asignación correcta (fix TRANSTE-1510) |
| TRU-T19 | Asignar AUTOTERMINAL SA | Seleccionar terminal | Asignación correcta (fix TRANSTE-1510) |
| TRU-T20 | Asignar todas las terminales registradas | Cada una de las 13 terminales | Todas asignables sin error |

### Bloque 5: Autenticación EntraID

| ID | Caso | Entrada | Resultado Esperado |
|----|------|---------|-------------------|
| TRU-T21 | Login con EntraID | Credenciales EntraID válidas | Acceso concedido según rol |
| TRU-T22 | Rol USER_READ_TRUCK_CENTER | Login usuario solo lectura | Puede ver GRID, NO puede modificar |
| TRU-T23 | Rol MANAGE_TRUCK_CENTER | Login gestor | Puede ver y gestionar registros |
| TRU-T24 | Rol USER_TRUCK_CENTER | Login usuario estándar | Acceso según permisos definidos |
| TRU-T25 | Token expirado | Sesión caducada | Redirección a login |
| TRU-T26 | Usuario sin rol TRU | Login usuario sin roles | Acceso denegado |

### Bloque 6: Eventos de Negocio

| ID | Caso | Entrada | Resultado Esperado |
|----|------|---------|-------------------|
| TRU-T27 | Evento entrada registrado | Lectura LPR entrada | Evento en pantalla de eventos de dominio TRU (no ARQ) |
| TRU-T28 | Evento salida registrado | Lectura LPR salida | Evento registrado correctamente |
| TRU-T29 | Evento KO sin matrícula | Lectura sin matrícula | Evento `TRU_CONTROL_PUERTAS_KO` visible en eventos de dominio |

### Bloque 7: Seguridad y Calidad de Código

| ID | Caso | Entrada | Resultado Esperado |
|----|------|---------|-------------------|
| TRU-T30 | Vulnerabilidades SonarQube | Escaneo SonarQube | Sin vulnerabilidades altas (fix TRANSTE-1530) |
| TRU-T31 | No inyección SQL en lupas | Intentar SQL injection en búsqueda | Input sanitizado |
| TRU-T32 | No XSS en campos | Intentar script en campos texto | Input sanitizado |

### Bloque 8: UI y Navegador

| ID | Caso | Entrada | Resultado Esperado |
|----|------|---------|-------------------|
| TRU-T33 | Pestaña navegador | Acceso a cualquier pantalla TRU | Título = "Truck Center" (no "Aplicación de Arquitectura APB") |
| TRU-T34 | WS usuarios sin duplicados | Cargar desplegable/lupas | Datos sin duplicados (fix SOSO-2075) |

### Bloque 9: Regresión y Despliegue

| ID | Caso | Entrada | Resultado Esperado |
|----|------|---------|-------------------|
| TRU-T35 | Health check API LGP | GET endpoint TRC | 200 OK |
| TRU-T36 | Health check APP TRU | GET endpoint TRU web | 200 OK |
| TRU-T37 | Despliegue Jenkins | Pipeline CI/CD | Build y deploy exitoso |
| TRU-T38 | Nomenclatura APIs correcta | Verificar nombres en IIS/Jenkins | APB.API.LGP y APB.API.TRU (no nombres antiguos) |

---

## 5. Tickets Jira Analizados

TRANSTE-1534, TRANSTE-1530, TRANSTE-1527, TRANSTE-1524, TRANSTE-1523, TRANSTE-1522, TRANSTE-1520, TRANSTE-1517, TRANSTE-1515, TRANSTE-1513, TRANSTE-1511, TRANSTE-1510, TRANSTE-1509, TRANSTE-1507, TRANSTE-1506, ARQ-2929, ARQ-2926, ARQ-2795, ARQ-2779, ARQ-2447, ARQ-2444, ARQ-2421, ARQ-2346, ARQ-2315, ARQ-2238, ARQ-2157, ARQ-1621, ARQ-1619, ARQ-1511, ARQ-1507, ARQ-1336, ARQ-1320, ARQ-1317, ARQ-1166, ARQ-1162, ARQ-1106, ARQ-1105, ARQ-1087, ARQ-1030, ARQ-927, ARQ-924, PVI-2, RM-165, GS-801, MISA-1567, MISA-1471, MISA-1434, MISA-1428, MISA-1381, MISA-1346, SOSO-2075
