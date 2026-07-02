# Plan Formal de Pruebas — TRU TruckCenter

## 1. Información general
- Proyecto: TRU TruckCenter
- Alcance funcional: APB.API.LGP + APB.API.TRU
- Versión: 1.0
- Fecha: 2026-07-01
- Responsable QA: Por asignar
- Fuente base: QA_TRU_TruckCenter_ENRIQUECIDO.md

## 2. Objetivo
Validar que el sistema gestione correctamente el control de acceso, el registro y seguimiento de camiones en el parking del Truck Center, garantizando:
- integridad de datos y reglas de negocio,
- correcto funcionamiento de APIs y web,
- cumplimiento de permisos y seguridad,
- trazabilidad de eventos y auditoría,
- estabilidad en despliegue y regresión.

## 3. Alcance
Se incluyen pruebas sobre:
- API ControlPuertas (APB.API.LGP)
- Aplicación web TruckCenter (APB.API.TRU)
- Grid principal
- Mantenimiento de expedientes
- Lupas de conductores y empresas
- Desplegable de terminales
- Tabla maestra de tipos de vehículo
- Autenticación, permisos y EntraID
- Eventos de auditoría
- Integración con servicios ARQ Docks
- Seguridad y calidad de código
- Regresión y despliegue

## 4. Criterios de entrada
- Entorno de pruebas accesible y operativo.
- Datos base cargados.
- Servicios y dependencias disponibles.
- Usuarios y roles configurados.

## 5. Criterios de salida
- Todos los casos críticos aprobados o justificadamente aceptados con riesgo.
- No quedan defectos críticos sin resolver.
- Se documenta evidencia de ejecución y resultados.

## 6. Matriz de pruebas

| ID | Bloque | Caso de prueba | Prioridad | Tipo | Resultado esperado | Estado |
|---|---|---|---|---|---|---|
| TRU-T01 | 1 | Entrada normal con matrícula | Crítica | Funcional | Se crea un nuevo registro en TRUCK_CENTER con fase EN EL PARKING, conexión eléctrica 0, ITV 0 y hora entrada = fecha enviada. | Pendiente |
| TRU-T02 | 1 | Salida normal con matrícula | Crítica | Funcional | Se actualiza el registro activo con HORA_SORTIDA = fecha enviada y fase FORA DEL PARKING. | Pendiente |
| TRU-T03 | 1 | Entrada duplicada — camión aún en parking | Crítica | Funcional | Se cierra el registro anterior y se crea uno nuevo en el parking. | Pendiente |
| TRU-T04 | 1 | Salida sin registro previo | Alta | Funcional | La operación no genera error y no modifica datos. | Pendiente |
| TRU-T05 | 1 | Lectura sin matrícula (NOMATRI) | Crítica | Funcional | Se emite evento TRU_CONTROL_PUERTAS_KO con texto Matricula:NOMATRI. | Pendiente |
| TRU-T06 | 1 | idCamara 17 dígitos | Alta | Integración | La API acepta el parámetro sin error de parsing. | Pendiente |
| TRU-T07 | 1 | idCamara 8 dígitos | Alta | Compatibilidad | La API mantiene compatibilidad con el formato legacy. | Pendiente |
| TRU-T08 | 1 | Campos no utilizados con valores extremos | Media | Integración | Solo se validan los campos usados; el resto se ignora. | Pendiente |
| TRU-T09 | 1 | JSON malformado | Alta | API | Se devuelve error HTTP 400 controlado. | Pendiente |
| TRU-T10 | 1 | Llamada sin permiso API_CALL_TRU_CONTROL_PUERTAS | Crítica | Seguridad | Se rechaza con 401/403. | Pendiente |
| TRU-T11 | 1 | Verificar HORA_SORTIDA exacta anterior = now - 1s | Alta | Lógica | El cierre del registro anterior registra la salida con diferencia exacta de 1 segundo. | Pendiente |
| TRU-T12 | 1 | Campos de salida API | Media | API | La respuesta es consistente con la lógica de negocio y el contrato. | Pendiente |
| TRU-T13 | 2 | Columnas por defecto visibles | Crítica | UI | Se ven 9 columnas en el orden esperado. | Pendiente |
| TRU-T14 | 2 | Ordenación por defecto | Alta | UI | Los registros aparecen de más nuevo a más viejo. | Pendiente |
| TRU-T15 | 2 | Selector de columnas — campos añadibles | Alta | UI | Aparecen todos los campos añadibles esperados. | Pendiente |
| TRU-T16 | 2 | Columnas auditoría en selector | Alta | UI | Se muestran APB_CREADOR, APB_MODIFICADOR, APB_CREAT y APB_MODIFICAT. | Pendiente |
| TRU-T17 | 2 | Filtro por lupa en cada columna | Alta | UI | El filtrado funciona correctamente en todas las columnas visibles. | Pendiente |
| TRU-T18 | 2 | Botón refresco GRID | Alta | UI | El grid se actualiza sin recargar la página completa. | Pendiente |
| TRU-T19 | 2 | Acción Salir del Parking desde GRID | Crítica | Funcional | Actualiza HORA_SORTIDA y fase al estado final. | Pendiente |
| TRU-T20 | 2 | Salir del Parking sin registro seleccionado | Alta | UI | La acción no está disponible o muestra aviso. | Pendiente |
| TRU-T21 | 2 | Salir del Parking en registro ya fuera | Alta | UI | La acción no está permitida. | Pendiente |
| TRU-T22 | 2 | Exportar a Excel — todos los campos | Alta | Funcional | El archivo contiene los campos de la vista con datos correctos. | Pendiente |
| TRU-T23 | 2 | Exportar a Excel — GRID vacío | Media | Funcional | Se genera el archivo sin errores. | Pendiente |
| TRU-T24 | 2 | Acceso GRID con USER_READ | Crítica | Permisos | Puede consultar pero no ejecutar acciones de gestión. | Pendiente |
| TRU-T25 | 2 | Acceso GRID con MANAGE | Crítica | Permisos | Puede consultar y ejecutar acciones de gestión. | Pendiente |
| TRU-T26 | 2 | Pestaña navegador | Media | UI | El título de la pestaña se muestra como Truck Center. | Pendiente |
| TRU-T27 | 3 | Alta mínima | Crítica | Funcional | Se crea el registro con los datos obligatorios y valores por defecto. | Pendiente |
| TRU-T28 | 3 | Alta completa | Crítica | Funcional | Se almacena correctamente toda la información aportada. | Pendiente |
| TRU-T29 | 3 | Alta sin matrícula | Crítica | Validación | El sistema no permite guardar y muestra error. | Pendiente |
| TRU-T30 | 3 | Alta sin tipo vehículo | Alta | Validación | El sistema bloquea el guardado. | Pendiente |
| TRU-T31 | 3 | Alta sin hora entrada | Alta | Validación | El sistema bloquea el guardado. | Pendiente |
| TRU-T32 | 3 | Alta duplicado — usuario confirma | Crítica | Regla negocio | Se cierra el anterior y se crea el nuevo registro. | Pendiente |
| TRU-T33 | 3 | Alta duplicado — usuario cancela | Crítica | Regla negocio | No se crea el nuevo registro y se muestra el mensaje esperado. | Pendiente |
| TRU-T34 | 3 | Matrícula existente en CAMIONS | Alta | Integración | El tipo de vehículo se recupera automáticamente. | Pendiente |
| TRU-T35 | 3 | Matrícula nueva | Alta | Integración | El tipo de vehículo debe seleccionarse manualmente. | Pendiente |
| TRU-T36 | 3 | Modificar tipo vehículo recuperado | Alta | Integración | Se actualiza el expediente y la tabla CAMIONS. | Pendiente |
| TRU-T37 | 3 | Botón reloj entrada | Media | UI | La hora de entrada se rellena con la hora actual. | Pendiente |
| TRU-T38 | 3 | Checkbox conexión eléctrica | Media | UI | El valor se guarda como 1/0 según estado. | Pendiente |
| TRU-T39 | 3 | Checkbox ITV | Media | UI | El valor se guarda como 1/0 según estado. | Pendiente |
| TRU-T40 | 3 | Checkbox mercancías peligrosas | Media | UI | El valor se guarda como 1/0 según estado. | Pendiente |
| TRU-T41 | 3 | Observaciones de 4000 caracteres | Media | Validación | Se guardan sin truncado. | Pendiente |
| TRU-T42 | 3 | Rol USER_READ no puede crear | Crítica | Permisos | No puede crear ni ver la acción de alta. | Pendiente |
| TRU-T43 | 4 | Modificar registro existente | Crítica | Funcional | Se actualizan los campos editables y se registra el evento. | Pendiente |
| TRU-T44 | 4 | Campos solo lectura no editables | Alta | UI | No se permite modificar los campos marcados como solo lectura. | Pendiente |
| TRU-T45 | 4 | Botón Salir del Parking desde mantenimiento | Crítica | Funcional | Se marca la salida y cambia la fase. | Pendiente |
| TRU-T46 | 4 | Botón Salir del Parking no visible en FORA DEL PARKING | Alta | UI | El botón no aparece para registros ya cerrados. | Pendiente |
| TRU-T47 | 4 | Baja de registro | Alta | Funcional | Se elimina correctamente el registro. | Pendiente |
| TRU-T48 | 4 | Modificar con USER_READ | Crítica | Permisos | Se deniega la acción de modificación. | Pendiente |
| TRU-T49 | 4 | Rollback en error transaccional | Crítica | Integridad | No quedan cambios parciales persistidos. | Pendiente |
| TRU-T50 | 4 | Sin reintento automático | Alta | Comportamiento | Tras el error, no se reintenta automáticamente. | Pendiente |
| TRU-T51 | 5 | Lupa conductores — búsqueda y selección | Crítica | Integración | Se recuperan NIF, nombre, apellidos, teléfono e ID. | Pendiente |
| TRU-T52 | 5 | Lupa conductores — conductor nuevo en PERSONES | Crítica | Integración | Se inserta automáticamente como tipo F. | Pendiente |
| TRU-T53 | 5 | Lupa conductores — conductor ya existente | Alta | Integración | No se duplica y se reutilizan los datos. | Pendiente |
| TRU-T54 | 5 | Lupa conductores — filtrado funciona | Crítica | UI | El filtro devuelve resultados correctamente. | Pendiente |
| TRU-T55 | 5 | Lupa empresas — búsqueda y selección | Crítica | Integración | Se recuperan NIF, razón social e ID. | Pendiente |
| TRU-T56 | 5 | Lupa empresas — empresa nueva en PERSONES | Crítica | Integración | Se inserta automáticamente como tipo J. | Pendiente |
| TRU-T57 | 5 | Lupa empresas — empresa ya existente | Alta | Integración | No se duplica y se reutilizan los datos. | Pendiente |
| TRU-T58 | 5 | Lupa empresas — filtrado funciona | Crítica | UI | El filtro devuelve resultados correctamente. | Pendiente |
| TRU-T59 | 5 | WS Sòstrat no disponible | Alta | Error handling | Se muestra un error controlado. | Pendiente |
| TRU-T60 | 5 | Datos duplicados WS usuarios | Alta | Integración | La lista no devuelve duplicados. | Pendiente |
| TRU-T61 | 5 | Escritura manual conductor | Media | Funcional | Se permite el ingreso manual sin lupa. | Pendiente |
| TRU-T62 | 5 | Escritura manual empresa | Media | Funcional | Se permite el ingreso manual sin lupa. | Pendiente |
| TRU-T63 | 6 | Desplegable solo actividad TU | Crítica | UI | Solo aparecen terminales con actividad TU. | Pendiente |
| TRU-T64 | 6 | Desplegable no bloquea página | Crítica | Rendimiento | La página responde sin bloquearse. | Pendiente |
| TRU-T65 | 6 | Asignar PORTCEMENT SA | Alta | Funcional | La terminal se asigna correctamente. | Pendiente |
| TRU-T66 | 6 | Asignar APM TERMINALS | Alta | Funcional | La terminal se asigna correctamente. | Pendiente |
| TRU-T67 | 6 | Asignar GRIMALDI | Alta | Funcional | La terminal se asigna correctamente. | Pendiente |
| TRU-T68 | 6 | Asignar AUTOTERMINAL SA | Alta | Funcional | La terminal se asigna correctamente. | Pendiente |
| TRU-T69 | 6 | Asignar cada una de las 13 terminales | Alta | Funcional | Todas las terminales asignables sin error. | Pendiente |
| TRU-T70 | 6 | Desplegable sin servicio Sòstrat | Media | Error handling | Se maneja el fallo sin bloquear la interfaz. | Pendiente |
| TRU-T71 | 7 | GRID tipos vehículo — 5 registros iniciales | Alta | Datos | Se cargan los 5 registros predefinidos. | Pendiente |
| TRU-T72 | 7 | Alta nuevo tipo vehículo | Alta | Funcional | Se crea correctamente y aparece en el grid y mantenimiento. | Pendiente |
| TRU-T73 | 7 | Modificar tipo existente | Media | Funcional | La descripción se actualiza correctamente. | Pendiente |
| TRU-T74 | 7 | Eliminar tipo sin dependencias | Media | Funcional | Se elimina sin error. | Pendiente |
| TRU-T75 | 7 | Eliminar tipo con dependencias | Alta | Integridad | Se impide la eliminación por integridad referencial. | Pendiente |
| TRU-T76 | 7 | USER_READ no puede modificar maestro | Alta | Permisos | Solo se permite consulta. | Pendiente |
| TRU-T77 | 8 | Login con EntraID exitoso | Crítica | Autenticación | El acceso se concede según rol. | Pendiente |
| TRU-T78 | 8 | Rol USER_READ — solo lectura completa | Crítica | Permisos | Solo consulta, sin acciones de gestión. | Pendiente |
| TRU-T79 | 8 | Rol MANAGE — gestión completa | Crítica | Permisos | Se habilitan alta, baja, modificación, salir parking y maestros. | Pendiente |
| TRU-T80 | 8 | Rol USER — usuario estándar | Alta | Permisos | El acceso cumple el perfil estándar definido. | Pendiente |
| TRU-T81 | 8 | Sin rol TRU | Crítica | Autorización | El usuario no accede a TRU. | Pendiente |
| TRU-T82 | 8 | Token expirado | Alta | Seguridad | El sistema redirige al login. | Pendiente |
| TRU-T83 | 8 | Idioma predeterminado catalán | Media | Internacionalización | La interfaz aparece en catalán. | Pendiente |
| TRU-T84 | 8 | Cambio de idioma en perfil | Media | Internacionalización | La interfaz se adapta al idioma elegido. | Pendiente |
| TRU-T85 | 8 | AppRegistration External ID configurada | Alta | Configuración | La configuración Azure es la esperada. | Pendiente |
| TRU-T86 | 8 | Tokens correctos tras renombrado API | Alta | Integración | Los tokens apuntan correctamente a la app TRU. | Pendiente |
| TRU-T87 | 9 | Evento creación OK | Crítica | Auditoría | Se registra TRU_CREACION_TRUCK_CENTER_OK con el ID del expediente. | Pendiente |
| TRU-T88 | 9 | Evento creación KO | Alta | Auditoría | Se registra TRU_CREACION_TRUCK_CENTER_KO ante error. | Pendiente |
| TRU-T89 | 9 | Evento modificación OK | Alta | Auditoría | Se registra TRU_MODIFICACION_TRUCK_CENTER_OK. | Pendiente |
| TRU-T90 | 9 | Evento modificación KO | Alta | Auditoría | Se registra TRU_MODIFICACION_TRUCK_CENTER_KO. | Pendiente |
| TRU-T91 | 9 | Evento control puertas OK | Crítica | Auditoría | Se registra TRU_CONTROL_PUERTAS_OK con los datos completos. | Pendiente |
| TRU-T92 | 9 | Evento control puertas KO | Alta | Auditoría | Se registra TRU_CONTROL_PUERTAS_KO con NOMATRI. | Pendiente |
| TRU-T93 | 9 | Evento salir parking OK | Alta | Auditoría | Se registra TRU_SALIR_PARKING_OK con matricula e ID. | Pendiente |
| TRU-T94 | 9 | Eventos visibles en dominio TRU | Alta | Auditoría | Los eventos aparecen en la sección TRU, no en la genérica ARQ. | Pendiente |
| TRU-T95 | 10 | Expediente Docks creado | Alta | Integración | El expediente aparece en la pantalla común de expedientes Docks. | Pendiente |
| TRU-T96 | 10 | Fases expediente correctas | Alta | Integración | Solo se observan las fases EN EL PARKING y FORA DEL PARKING. | Pendiente |
| TRU-T97 | 10 | Menú contextual funcional | Media | Integración | El menú contextual funciona correctamente. | Pendiente |
| TRU-T98 | 10 | Pantalla errores Docks | Media | Integración | El error aparece en la pantalla común de errores. | Pendiente |
| TRU-T99 | 10 | Mensajes Docks funcionales | Alta | Integración | El aviso de duplicado se muestra con el mensaje esperado. | Pendiente |
| TRU-T100 | 10 | WS ARQ todos operativos | Alta | Integración | Todos los WS de ARQ responden correctamente. | Pendiente |
| TRU-T101 | 11 | SonarQube sin vulnerabilidades altas | Crítica | Calidad | No se detectan vulnerabilidades altas. | Pendiente |
| TRU-T102 | 11 | No inyección SQL en lupas | Crítica | Seguridad | El input se sanitiza y no afecta a las consultas. | Pendiente |
| TRU-T103 | 11 | No XSS en observaciones | Crítica | Seguridad | El contenido malicioso no se ejecuta. | Pendiente |
| TRU-T104 | 11 | No XSS en matrícula | Alta | Seguridad | El input no genera ejecución de script. | Pendiente |
| TRU-T105 | 11 | Validación largo campos según modelo | Alta | Validación | Se rechaza o controla el valor fuera de rango. | Pendiente |
| TRU-T106 | 11 | HTTPS en todos los endpoints | Alta | Seguridad | PRE y PRO usan HTTPS exclusivamente. | Pendiente |
| TRU-T107 | 12 | Health check API LGP | Crítica | Despliegue | El endpoint responde 200 OK. | Pendiente |
| TRU-T108 | 12 | Health check APP TRU | Crítica | Despliegue | El endpoint web responde 200 OK. | Pendiente |
| TRU-T109 | 12 | Nomenclatura APIs post-renombrado | Alta | Despliegue | Se observan los nombres APB.API.LGP y APB.API.TRU. | Pendiente |
| TRU-T110 | 12 | Repositorio APB.TRU | Alta | Despliegue | El repositorio y pipelines apuntan al nuevo nombre. | Pendiente |
| TRU-T111 | 12 | E2E completo entrada LPR → GRID → terminal → salida | Crítica | E2E | Se completa el flujo con entrada, asignación y salida. | Pendiente |
| TRU-T112 | 12 | E2E completo alta manual → modificar → salir parking | Crítica | E2E | El registro sigue el flujo completo manualmente. | Pendiente |

## 7. Checklist ejecutable

### Bloque 1 — API ControlPuertas — Recepción LPR
- [ ] TRU-T01 — Entrada normal con matrícula
- [ ] TRU-T02 — Salida normal con matrícula
- [ ] TRU-T03 — Entrada duplicada — camión aún en parking
- [ ] TRU-T04 — Salida sin registro previo
- [ ] TRU-T05 — Lectura sin matrícula (NOMATRI)
- [ ] TRU-T06 — idCamara 17 dígitos
- [ ] TRU-T07 — idCamara 8 dígitos
- [ ] TRU-T08 — Campos no utilizados con valores extremos
- [ ] TRU-T09 — JSON malformado
- [ ] TRU-T10 — Llamada sin permiso API_CALL_TRU_CONTROL_PUERTAS
- [ ] TRU-T11 — Verificar HORA_SORTIDA exacta anterior = now - 1s
- [ ] TRU-T12 — Campos de salida API

### Bloque 2 — GRID Principal
- [ ] TRU-T13 — Columnas por defecto visibles
- [ ] TRU-T14 — Ordenación por defecto
- [ ] TRU-T15 — Selector de columnas — campos añadibles
- [ ] TRU-T16 — Columnas auditoría en selector
- [ ] TRU-T17 — Filtro por lupa en cada columna
- [ ] TRU-T18 — Botón refresco GRID
- [ ] TRU-T19 — Acción Salir del Parking desde GRID
- [ ] TRU-T20 — Salir del Parking sin registro seleccionado
- [ ] TRU-T21 — Salir del Parking en registro ya fuera
- [ ] TRU-T22 — Exportar a Excel — todos los campos
- [ ] TRU-T23 — Exportar a Excel — GRID vacío
- [ ] TRU-T24 — Acceso GRID con USER_READ
- [ ] TRU-T25 — Acceso GRID con MANAGE
- [ ] TRU-T26 — Pestaña navegador

### Bloque 3 — Pantalla de Mantenimiento — Alta
- [ ] TRU-T27 — Alta mínima
- [ ] TRU-T28 — Alta completa
- [ ] TRU-T29 — Alta sin matrícula
- [ ] TRU-T30 — Alta sin tipo vehículo
- [ ] TRU-T31 — Alta sin hora entrada
- [ ] TRU-T32 — Alta duplicado — usuario confirma
- [ ] TRU-T33 — Alta duplicado — usuario cancela
- [ ] TRU-T34 — Matrícula existente en CAMIONS
- [ ] TRU-T35 — Matrícula nueva
- [ ] TRU-T36 — Modificar tipo vehículo recuperado
- [ ] TRU-T37 — Botón reloj entrada
- [ ] TRU-T38 — Checkbox conexión eléctrica
- [ ] TRU-T39 — Checkbox ITV
- [ ] TRU-T40 — Checkbox mercancías peligrosas
- [ ] TRU-T41 — Observaciones de 4000 caracteres
- [ ] TRU-T42 — Rol USER_READ no puede crear

### Bloque 4 — Pantalla de Mantenimiento — Modificación y Baja
- [ ] TRU-T43 — Modificar registro existente
- [ ] TRU-T44 — Campos solo lectura no editables
- [ ] TRU-T45 — Botón Salir del Parking desde mantenimiento
- [ ] TRU-T46 — Botón Salir del Parking no visible en FORA DEL PARKING
- [ ] TRU-T47 — Baja de registro
- [ ] TRU-T48 — Modificar con USER_READ
- [ ] TRU-T49 — Rollback en error transaccional
- [ ] TRU-T50 — Sin reintento automático

### Bloque 5 — Lupas — Conductores y Empresas
- [ ] TRU-T51 — Lupa conductores — búsqueda y selección
- [ ] TRU-T52 — Lupa conductores — conductor nuevo en PERSONES
- [ ] TRU-T53 — Lupa conductores — conductor ya existente
- [ ] TRU-T54 — Lupa conductores — filtrado funciona
- [ ] TRU-T55 — Lupa empresas — búsqueda y selección
- [ ] TRU-T56 — Lupa empresas — empresa nueva en PERSONES
- [ ] TRU-T57 — Lupa empresas — empresa ya existente
- [ ] TRU-T58 — Lupa empresas — filtrado funciona
- [ ] TRU-T59 — WS Sòstrat no disponible
- [ ] TRU-T60 — Datos duplicados WS usuarios
- [ ] TRU-T61 — Escritura manual conductor
- [ ] TRU-T62 — Escritura manual empresa

### Bloque 6 — Desplegable Terminales
- [ ] TRU-T63 — Desplegable solo actividad TU
- [ ] TRU-T64 — Desplegable no bloquea página
- [ ] TRU-T65 — Asignar PORTCEMENT SA
- [ ] TRU-T66 — Asignar APM TERMINALS
- [ ] TRU-T67 — Asignar GRIMALDI
- [ ] TRU-T68 — Asignar AUTOTERMINAL SA
- [ ] TRU-T69 — Asignar cada una de las 13 terminales
- [ ] TRU-T70 — Desplegable sin servicio Sòstrat

### Bloque 7 — Tabla Maestra — Tipos de Vehículo
- [ ] TRU-T71 — GRID tipos vehículo — 5 registros iniciales
- [ ] TRU-T72 — Alta nuevo tipo vehículo
- [ ] TRU-T73 — Modificar tipo existente
- [ ] TRU-T74 — Eliminar tipo sin dependencias
- [ ] TRU-T75 — Eliminar tipo con dependencias
- [ ] TRU-T76 — USER_READ no puede modificar maestro

### Bloque 8 — Autenticación y Permisos EntraID
- [ ] TRU-T77 — Login con EntraID exitoso
- [ ] TRU-T78 — Rol USER_READ — solo lectura completa
- [ ] TRU-T79 — Rol MANAGE — gestión completa
- [ ] TRU-T80 — Rol USER — usuario estándar
- [ ] TRU-T81 — Sin rol TRU
- [ ] TRU-T82 — Token expirado
- [ ] TRU-T83 — Idioma predeterminado catalán
- [ ] TRU-T84 — Cambio de idioma en perfil
- [ ] TRU-T85 — AppRegistration External ID configurada
- [ ] TRU-T86 — Tokens correctos tras renombrado API

### Bloque 9 — Eventos de Auditoría
- [ ] TRU-T87 — Evento creación OK
- [ ] TRU-T88 — Evento creación KO
- [ ] TRU-T89 — Evento modificación OK
- [ ] TRU-T90 — Evento modificación KO
- [ ] TRU-T91 — Evento control puertas OK
- [ ] TRU-T92 — Evento control puertas KO
- [ ] TRU-T93 — Evento salir parking OK
- [ ] TRU-T94 — Eventos visibles en dominio TRU

### Bloque 10 — Integración WS ARQ Docks
- [ ] TRU-T95 — Expediente Docks creado
- [ ] TRU-T96 — Fases expediente correctas
- [ ] TRU-T97 — Menú contextual funcional
- [ ] TRU-T98 — Pantalla errores Docks
- [ ] TRU-T99 — Mensajes Docks funcionales
- [ ] TRU-T100 — WS ARQ todos operativos

### Bloque 11 — Seguridad y Calidad de Código
- [ ] TRU-T101 — SonarQube sin vulnerabilidades altas
- [ ] TRU-T102 — No inyección SQL en lupas
- [ ] TRU-T103 — No XSS en observaciones
- [ ] TRU-T104 — No XSS en matrícula
- [ ] TRU-T105 — Validación largo campos según modelo
- [ ] TRU-T106 — HTTPS en todos los endpoints

### Bloque 12 — Regresión, Despliegue y E2E
- [ ] TRU-T107 — Health check API LGP
- [ ] TRU-T108 — Health check APP TRU
- [ ] TRU-T109 — Nomenclatura APIs post-renombrado
- [ ] TRU-T110 — Repositorio APB.TRU
- [ ] TRU-T111 — E2E completo entrada LPR → GRID → terminal → salida
- [ ] TRU-T112 — E2E completo alta manual → modificar → salir parking

## 8. Plantilla de ejecución
- Fecha de ejecución:
- Entorno:
- Responsable:
- Resultado general:
- Observaciones:
- Firma:
