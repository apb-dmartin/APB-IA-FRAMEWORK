---
id: "prov-apb-knowledge-base-v1.0"
name: "APB Knowledge Base — Contexto Corporativo"
description: >
  Base de conocimiento consolidada de la Autoritat Portuària de Barcelona.
  Proporciona a los agentes IA el contexto de negocio, funcional y tecnológico
  (incluyendo sistemas legacy) necesario para dar respuestas de calidad.
  NO modifica los estándares DOCKS ni las políticas tecnológicas aprobadas:
  el legacy se documenta como contexto, nunca como patrón a seguir en desarrollos nuevos.
version: "1.3.0"
status: "approved"
owner: "Debora Martin <deboramv@gmail.com>"
domain: "knowledge"
provider_type: "knowledge"
access_mode: "read-only"
created_date: "2026-06-30"
review_date: "2026-07-15"
sources:
  - "APB_Knowledge_Base_IA.md (v1.0)"
  - "APB_Knowledge_Base_IA_v2.md (v2.0)"
  - "APB_Knowledge_Base_IA_v3.md (v3.0)"
  - "discovery/ddd-sostrat-mj8/ (v1.1.0, 2026-07-15) — descomposición DDD de SÒSTRAT: 24 dossiers de aplicación verificados contra código real, auditoría de 9 consumidores externos, cierre de cobertura de código (coverage-audit.md), análisis de arquitectura de eventos para EDI/Ventanilla Única"
  - "Documento 'Roles de Aplicación DOCKS en Entra ID' (Débora Martin, 2026-07-15) — modelo de roles/grupos de autorización DOCKS, PLAN_FASES_FUTURAS.md #104"
---

# APB Knowledge Base — Contexto Corporativo

> ⚠️ Borrador generado por IA — revisado y aprobado por Debora Martin (Tech&Ops, APB). Fuentes: 150 proyectos Jira, 520+ repositorios GitHub org:portdebarcelona, Confluence APLIS, tickets 2023-2026.

---

## ⚠️ Guardrail para agentes IA

> **Este documento es contexto, no prescripción tecnológica.**
>
> Los sistemas legacy documentados aquí (Java/Struts/Oracle/CAS/Alfresco/Tomcat) existen
> en producción y los agentes deben conocerlos para entender tickets, integraciones y
> dominios funcionales. Sin embargo, **ningún agente puede recomendar ni generar artefactos
> que usen tecnologías no aprobadas** solo porque existan en el legacy.
>
> Estándar autoritativo: `context/apb/standards/STANDARD_ARCHITECTURE.md`
> Stack aprobado para nuevos desarrollos: ver §3 (Arquitectura DOCKS).

---

## 1. Visión General de la Organización

La **Autoritat Portuària de Barcelona (APB)** es el organismo público responsable de la
gestión, administración y explotación del Port de Barcelona, uno de los principales puertos
del Mediterráneo. Entidad de derecho público con personalidad jurídica propia, dependiente
del Ministerio de Transportes, dentro del sistema de Puertos del Estado.

### 1.1. Misión

- Gestionar la infraestructura portuaria (muelles, terminales, accesos).
- Regular y coordinar las operaciones marítimas, terrestres y ferroviarias.
- Facilitar el comercio internacional y la logística.
- Garantizar la seguridad portuaria (policía portuaria, control de accesos, emergencias).
- Administrar concesiones, autorizaciones y facturación de servicios portuarios.

### 1.2. Actores del Ecosistema Portuario

| Actor | Rol |
|-------|-----|
| Consignatario | Representante del armador; gestiona la escala del buque |
| Armador / Naviera | Propietario o explotador del buque |
| Terminal | Empresa concesionaria que opera muelles (BEST, TCB, Grimaldi, DECAL…) |
| Práctico (Pilot) | Piloto que guía al buque en maniobras portuarias |
| Remolcador (Tug) | Embarcación de asistencia en maniobras |
| Amarrador (Linesman) | Personal que amarra/desamarra el buque al muelle |
| Estibador (Stevedore) | Empresa de manipulación de carga |
| Aduana | Control aduanero de mercancías |
| PORTIC | Plataforma EDI de la comunidad portuaria de Barcelona |
| Policía Portuaria | Seguridad, control de accesos, vigilancia |
| Capitanía Marítima | Autoridad estatal sobre el tráfico marítimo |
| Operador de Atraque (Berth Operator) | Gestiona y autoriza los atraques |
| Empresa MARPOL | Recogida de residuos de buques (ECOIMSA, Otto Schwandt, ECOMARPOL…) |
| PdE (Puertos del Estado) | Organismo estatal que supervisa las autoridades portuarias |
| AGE | Administración General del Estado (GEISER, Notifica, FACe) |

### 1.3. Departamento de Sistemas de Información (SSI)

- **OSMA (Oficina de Soporte y Mantenimiento de Aplicaciones)**: gestión de contratos, mantenimientos y coordinación de proveedores.
- **Tech&Ops**: Arquitectura, Operaciones, QA, SRE, DevOps. Responsable: Debora Martin (CTO).
- **Ciberseguridad (CIBER)**: OTS (Oficina Técnica de Seguridad), SOC 24x7, ENS/ISO 27001.
- **HelpDesk / SAU**: soporte al usuario (Jira Service Management, proyecto APBPIT).

### 1.4. Entorno Lingüístico (trilingüe)

| Lengua | Uso |
|--------|-----|
| **Catalán (CA)** | Nombres internos, documentación SÒSTRAT, menús de sistemas legacy |
| **Castellano (ES)** | Documentación técnica formal, contratos, comunicaciones oficiales |
| **Inglés (EN)** | APIs, microservicios ARGOS, estándares marítimos internacionales (EDI, IMO) |

---

## 2. Negocio Portuario — Conceptos Clave

### 2.1. La Escala (Port Call)

Una **escala** es la visita completa de un buque al puerto, desde el preaviso hasta la salida.
Es el concepto central del negocio portuario — **todos** los demás procesos de negocio de SÒSTRAT
(residuos, agua, mercancías peligrosas, transporte terrestre, ferrocarril, cruceros, servicios
auxiliares) se cuelgan de una escala concreta vía su clave compuesta.

**Identificadores reales (grounded en `Escala.java`, tabla `ESCALA`):**

| Campo | Descripción |
|-------|-------------|
| `idsubport` | Subpuerto (generalmente `"B"` = Barcelona) — 1ª parte de la PK compuesta |
| `anyescala` | Año de la escala — 2ª parte de la PK |
| `numescala` | Número secuencial de escala — 3ª parte de la PK |
| `EscalaAspecte` | Tabla separada (~90 campos técnicos de buque por versión de la escala) — no un simple flag R/S, es una entidad propia con su propio historial de versiones |
| YearPortCall / NumPortCall / IdSubPort | Nombres del DTO equivalente en ARGOS (`PortCallCreatedDto.cs`) — mismo concepto de negocio, terminología catalana (`ESCALA`/`ASPECTE`) heredada literalmente en el nombre del campo `Aspecte` |

**Ciclo de vida:**

```
Preaviso (BERMAN F11) → Autorizada → Confirmada → Iniciada → [Fondeada] → Atracada → Operativa → Finalizada → Cancelada
```

**Estados de escala (ARGOS/DOCKS):** `REQ` → `CONF` → `INIT` → `FIN` / `CAN`

**Fechas clave:**

| Sigla | Significado |
|-------|-------------|
| ETA | Estimated Time of Arrival |
| ATA | Actual Time of Arrival |
| ETD | Estimated Time of Departure |
| ATD | Actual Time of Departure |

**Hallazgos funcionales importantes (descomposición DDD 2026-07)**:
- **La facturación está entrelazada con la gestión de la escala, no separada**: `EscalaAction.java` (7.549 líneas, la god class más grande de todo SÒSTRAT) tiene ~73-81 referencias directas a `Liquidacio`/`Facturacio` — dar de alta o modificar una escala dispara lógica de facturación en el mismo flujo. Cualquier análisis que asuma "Escalas no calcula tasas" está equivocado para el legacy actual (aunque sí es la separación correcta para el destino DOCKS).
- **ARGOS (`APB.API.TES`, microservicio `MS_PORTCALL`) ya es hoy la maestría operativa real de la escala** — SÒSTRAT sigue escribiendo `ESCALA`/`ATRACADA` y emitiendo los eventos `MSG0004`/`MSG0017`, pero migrar Escalas no es "construir un servicio nuevo": es decidir cómo se retira SÒSTRAT como fuente de verdad y se traspasa esa responsabilidad a ARGOS, que ya la ejerce.
- **`APB.API.LRT`** (ecosistema de Líneas Regulares) también **escribe** directamente en `ESCALA` — hay hoy un tercer escritor real (SÒSTRAT, ARGOS futuro, LRT), no dos.
- **Sistemas satélite de la escala, poco conocidos fuera del código**: `SistemaPantallas` (pantallas informativas de escala/atraque) e `InformationPortcdmWS` (notificación PortCDM — Port Collaborative Decision Making) viven ambos en `service/escalas`, no en un módulo separado.

### 2.2. El Atraque (Berth)

Asigna un buque a un punto de amarre en un muelle.

| Campo | Descripción |
|-------|-------------|
| BerthCode | Código de muelle (ej. "32A", "32B", "34B") |
| StateAdministrative | P (Pending) → S (Solicited) → AUTH → INI → FIN |
| StartModule / EndModule | Segmento del muelle ocupado |
| BerthingSide | Costado: babor (ABM), estribor |
| ArrivalDraft / DepartureDraft | Calados de llegada/salida |
| Stevedoring | Empresa estibadora asignada |

**Estados de atracamiento (ARGOS):** Solicitado → Confirmado → INI → FI

### 2.3. Movimientos Marítimos

**Tipos de movimiento:**

| Tipo | Descripción |
|------|-------------|
| D | Mar → Fondeig (entrada al fondeo) |
| E | Fondeig → Atraque (del fondeo al muelle) |
| F | Atraque → Fondeig (del muelle al fondeo) |
| G | Fondeig → Mar (salida al mar) |

**Estados de movimiento (ARGOS):** `Pending` → `Approvable` → `Approved` → `Coordinated` → `Initiated` → `Finished`

**Milestones (Fites) de movimiento:**
- ARRIVAL NOTICE
- PORT TRAFFIC COMMUNICATION (2MN / 4MN)
- ANCHORAGE CLEARANCE
- HEAVE UP & CALL / 1H CALL
- READY SHIFTING / ANCHOR UP
- ENTRY CLEARANCE / MANOEUVRING CLEARANCE
- BUOY CHECKPOINT
- 20MIN DEPARTURE / READY TO SAIL
- SHIP ANCHORED CALL

### 2.4. Título, Ocupaciones y Garantías (lo que el negocio llama "Concesiones")

> **Corrección de nomenclatura (dossier-14-concesiones.md)**: el concepto real en el modelo de datos y el código es **Título** (`Titol`, tabla `TITOL`), no "Concesión" — "Concesión" es un tipo posible de título entre varios (Concesión, Autorización, Ocupación, Licencia, Evento), la hipótesis inicial de nombrar todo el módulo "Concesiones" sobregeneraliza un caso particular.

El **Título** otorga derecho de uso de terreno/actividad portuaria. Un título puede tener **ocupaciones** (`TitolOcupacio`, uso de dominio público — parcela con perímetro) y/o **actividades** (`TitolActivitat`, actividad portuaria autorizada), no son excluyentes.

| Campo | Descripción |
|-------|-------------|
| `idsubport`+`idtitol` | PK compuesta real del título |
| `idestattitol` | Estado del título — catálogo real (`TITOL_ESTAT`) confirmado en código, pero sus valores concretos (más allá del nombre del campo) no estaban confirmados en el checkout auditado |
| `idtitolprecedent` | Referencia autoreferencial — un título puede suceder a otro (renovación) |
| Ocupació | Parcela con perímetro georreferenciado, asociada a `TitolOcupacio` |
| Zona portuaria / zona de valor | Clasificación del espacio |
| Vigencia / caducidad / renovación | Fechas de validez del título |

**Garantía** (`Garantia`, tabla `GARANTIA`) es un aval financiero **siempre asociado a un título** (`IDTITOL`) — no tiene identidad de agregado propia, se modela como sub-recurso de Título, no como colección independiente. Incluye evidencias documentales (`GarantiaEvidencia`) y auditoría de cambios (`GarantiaAudit`).

**Hallazgo estructural importante**: en el código legacy, `Liquidación` **escribe directamente** sobre `TITOL_MINIM_DADES` al eliminar una liquidación (`CN_Liquidacion_Impl.java:434`, `UPDATE TITOL_MINIM_DADES SET PORTLIQUIDACIO=NULL...`) — es el ejemplo de acoplamiento por escritura cruzada más citado de toda la descomposición DDD, y la razón por la que el evento `TituloActualizado` se considera "fundacional" para poder separar Concesiones y Facturación en dos servicios con bases de datos propias.

### 2.5. Tasas y Tarifas Portuarias

| Tasa / Tarifa | Descripción |
|---------------|-------------|
| T0 / T1 | Tasa de buque (por acceso y estancia) |
| T2 | Tasa de pasaje |
| T3 | Tasa de mercancía |
| T4 | Tasa de pesca |
| T5 | Tasa de ocupación de dominio público |
| L1 | Tarifa por atraque |
| L3 | Tarifa por operaciones de carga/descarga |
| L6 | Liquidación de concesiones |
| L7 | Tarifa fija MARPOL (recogida de residuos) |
| P11000 | Tarifa electricidad (Shore Power/OPS): BE1 (fijo) + BE2 (variable) |
| Bonificaciones | Descuentos comerciales (3W1, 3W4 = intermodalidad ferroviaria) |

**Tipos de liquidación:** L0 / L1 / L6 / L7

### 2.6. Operativa de Mercancías

- **Manifiesto** (`Manifest`, tabla `MANIFEST`): declaración de carga del buque, con líneas de detalle llamadas **Partida** (`PartidaVersio`, versionada) — cada partida es una línea de mercancía concreta dentro del manifiesto, con su propia clasificación arancelaria (`numonu`/`classemmpp` cuando aplica). Tipos reales de declaración: `0811` (descarga), `0812` (carga).
- **COARRI**: mensaje EDIFACT que informa de operaciones reales de terminal (carga/descarga física de un contenedor). En SÒSTRAT sirve para **conciliar** lo que el terminal reporta contra lo que dice el manifiesto — de ahí que su tabla de negocio real sea `CONCILIACION_MANIFIESTO`, no una entidad propia. Existe también un **COARRI ferroviario** (mensaje `RAIL20`) para movimientos de contenedores por tren, con la misma función de conciliación pero en el dominio de Ferrocarril.
- **CODECO** (gate-in/gate-out): mensaje de entrada/salida de un contenedor de una terminal. En SÒSTRAT alimenta el módulo de **Transporte Terrestre** (preavisos/autorizaciones de camión) — no es una entidad de mercancía en sí, es el evento que dispara la autorización de acceso físico del transportista.
- **Declaraciones sumarias (CUSCAR)** y familia (`CUSREP`/`CUSRES`/`CUSRP2`): información anticipada para Aduana sobre la carga de un manifiesto, mismo motor batch que IFCSUM.
- **Mercancías Peligrosas (MMPP/ADR/IMO)**: dos procesos de negocio distintos, no uno solo — **notificación** a las autoridades (circuito EDI `IFTDGN`, con respuesta APERAK) y **autorización** de manipulación/inspección (circuito EDI `HAZMAT`, alimenta el listado de carga). El modelo de datos (`MmppNotif`) duplica literalmente el bloque de datos de transporte para "entrada" y "salida" — 61 campos totales, la mitad simétricos.
- **SCPP** (Servicio de Control y Posicionamiento de Contenedores): gestiona la **capacidad** del recinto de inspección (lugares, turnos, calendario de capacidad ya comprometida) y el **resultado** formal de cada inspección concreta. No confundir con PIF.
- **PIF** (Punto de Inspección Fronteriza): gestiona la **operación real** de un camión/contenedor concreto en el finger de muelle — 6 estados confirmados en código (`CR`=creada, `AP`=aprobada, `PF`=?, `FI`=finalizada, `AN`=anulada, `AF`=?; nombres completos de `PF`/`AF` no confirmados con evidencia adicional). PIF y SCPP están tan acoplados síncronamente en el código real (validación de turno de SCPP dentro de la transacción de alta de una operación PIF) que la recomendación de la descomposición DDD es desplegarlos como **un único servicio con dos agregados**, no como dos microservicios separados.
- **Posicionamiento**: capacidad de negocio real (no solo un detalle técnico) que asigna la posición física de un camión/contenedor en el recinto PIF, con su propio circuito EDI y su propia máquina de incidencias (`Incidencia`/`IncidenciaEQ`) — acoplada síncronamente tanto a PIF como a SCPP, pero sin bounded context propio identificado todavía en el catálogo.
- **Depotsis** (T6): depósito de mercancía en muelle libre — una **solicitud** de depósito versionada (no editable in-place: cada cambio crea una nueva versión numerada), que agrupa una o varias **operaciones** de desconsolidación de mercancía.

**Tipos de transporte ant/post:** ZZ1 = marítimo, ZZ2 = terrestre (camión), ZZ5 = tránsito marítimo, ZZ6 = ferrocarril.

### 2.7. Ferrocarril Portuario

- **Escala ferroviaria**: paso de un tren por el puerto.
- **Terminales ferroviarias**: de recepción/expedición (gestionada por APB) y de carga/descarga (terminales).
- **COARRI ferroviario (RAIL20)**: mensaje de movimiento de contenedores por ferrocarril.
- **Ordre de Transport (OT)**: orden de transporte ferroviario.
- **Efficiency Network**: marca de calidad de servicios portuarios.

### 2.8. Seguridad y Accesos

- **Pases y Permisos (PPS)**: control de acceso de personas y vehículos.
- **Permisos de obra**: autorizaciones para trabajos dentro del recinto.
- **Acreditaciones**: registros biométricos (huellas digitales) para acceso.
- **ISPS**: Código Internacional de Seguridad para Buques e Instalaciones Portuarias.
- **PFSO/POPF**: Port Facility Security Officer / Oficial de Protecció de la Instal·lació Portuària.

### 2.9. Infraestructura Portuaria

**Muelles principales:** Drassanes, Adossat, Sant Bertran, Álvarez de la Campa, Princep d'Espanya, Inflamables, Moll de l'Energia (supermolls 32A-32H, 34B), Barcelona (WTC), Ponent.

**Terminales de contenedores:** BEST (Barcelona Europe South Terminal), TCB (Terminal de Contenidors de Barcelona).

**Terminales de cruceros:** A, B, C, D, E.

**Terminal ferroviaria:** Terminal Ferroviària C (recepción/expedición).

**ZAL:** Zona de Actividades Logísticas (ZAL-BCN y ZAL-PRAT).

### 2.10. Muelle de la Energía (Moll de l'Energia)

Área específica para operaciones con productos inflamables y energéticos. Aplicación propia (MDE) separada de ARGOS con roles específicos:
- Operador de Atraques (`MANAGE_BERTH_SUPERVISOR`)
- Consignatario (`MANAGE_CONSIGNEE`)
- Terminal (`MANAGE_TERMINAL`)

Funcionalidades específicas: Bunkering, Shore Power (OPS), Anexo I Terminal y Consignatario, Informe de fecha fin operaciones, Facturación electricidad (DSS_DWH).

### 2.11. Servicios al Buque (residuos, agua, electricidad, alcantarillado)

Cuatro servicios distintos que un buque puede contratar durante su escala, cada uno con su propio ciclo de vida y tarifa — no son variantes de lo mismo:

- **MARPOL (recogida de residuos)**: gestiona el ciclo completo desde la solicitud hasta el pago de una recogida de residuos de buque. **7 estados de negocio confirmados en código** (`ResidusEscala.idestat`): `1`=Recibido, `2`=Anulado, `3`=No pagado, `4`=Confirmado, `5`=Enviado, `6`=Pagado, `7`=Reclamado (la semántica de qué transiciones son válidas entre ellos no está confirmada, solo los nombres). Tiene su **propio tarifario** (`TARIFAS_RESIDUS`, por rango y tipo de residuo), **distinto y adicional** a la bonificación de la tasa L7 que se calcula del lado de Facturación según el tipo de residuo entregado — MARPOL y Facturación comparten el "hecho de negocio" (tipo de residuo) pero no el cálculo. Circuito EDI: WASDIS, con respuesta APERAK propia.
- **Aguada**: suministro de agua potable al buque. Bloqueado documentalmente — el DTO fuente real (`SaSolicitud`) no existe en el checkout auditado, requiere recuperarlo del proveedor (IN2).
- **Shore Power / OPS** (Suministro Eléctrico): suministro eléctrico a un buque atracado, con lecturas de consumo real. Tarifa `P11000` (BE1 fijo + BE2 variable). Existe un puente de solo lectura hacia un Data Warehouse externo (`APB.API.OPS`, tabla `OPS_B_SESSIONS` en `DSS_DWH`) que replica estas sesiones — decisión pendiente de si el nuevo servicio lo alimenta o se retira.
- **Clavegueram (alcantarillado)**: liquidación de consumos de alcantarillado de empresas adheridas al puerto — el bounded context más pequeño de toda la serie (3 rutas), pero con acoplamiento real de código hacia Facturación (tarifa fija `L6-50-10`, motor `CN_LiquidadorBase_Impl` compartido con Aguada/Depotsis/Suministros).

### 2.12. Terceros / Operadores Portuarios y Efficiency Network

El maestro de terceros de SÒSTRAT es `Usuari` (tabla `USUARI`, 118 campos confirmados) — cubre consignatarios, armadores, agentes de aduanas, transitarios y cualquier operador económico con relación comercial con APB. Es un dato maestro consumido por **al menos 30 módulos distintos** (fan-out real confirmado — más que el propio maestro de buques), pese a que la documentación previa solo citaba 3 consumidores.

Incluye datos bancarios (`CompteBancari`, mandato SEPA — dato financiero sensible, sujeto a PSD2), circuitos EDI propios (`UsuariCircuitEDI`) y presencia web (`nomweb`/`urlweb`/`logoweb`).

**Efficiency Network** ("Business Club") es un programa de certificaciones de sostenibilidad para empresas adheridas — funcionalmente parece un programa aparte, pero en código `EmpresaBC extends Usuari` (herencia real de clase): toda empresa adherida al programa **es**, estructuralmente, un Operador Portuario con datos adicionales. El campo `Usuari.eseffnetwork` (String `"S"`/`"N"`, no booleano) marca la adhesión desde el propio maestro de terceros.

### 2.13. Transporte Terrestre

Gestiona los preavisos y autorizaciones de camiones que acceden al recinto portuario para recoger/entregar mercancía, más un sub-dominio de **parquing** (plazas de aparcamiento con tarifa propia) con paquete Java diferenciado. Alimentado por los circuitos EDI CODECO (gate-in/gate-out) y COPINO (recogida/entrega, con respuesta APERAK). Tiene acoplamiento de código real (no solo documental) hacia PPS (`CN_Targetas`) y Escalas (`AlineacioDades`).

---

## 3. Arquitectura Corporativa: DOCKS (Stack Aprobado para Nuevos Desarrollos)

> **Este apartado define el stack canónico.** Los agentes deben recomendar EXCLUSIVAMENTE
> tecnologías de esta sección para cualquier nuevo desarrollo, independientemente de lo
> que exista en sistemas legacy.

### 3.1. Stack Tecnológico Aprobado

| Capa | Tecnología | Notas |
|------|------------|-------|
| Backend | .NET Core / .NET 10 | Migración en curso a .NET 10 |
| Frontend | JavaScript + DevExpress/DevExtreme | |
| BBDD nuevas apps | Azure SQL | |
| Autenticación | Microsoft Entra ID | Migración en curso desde LDAP/CAS/TGT |
| Mensajería | Azure Service Bus (topics/subscriptions) | |
| Caché | Redis (Azure) | |
| API Gateway | Azure API Management (APIM) | |
| Almacenamiento | Azure Blob Storage + SharePoint Online | Migración desde Alfresco |
| Gestor documental | SharePoint Online / APB.API.FLC | Alfresco = legacy, NO usar en nuevos |
| CI/CD | Jenkins (shared library) + GitHub Actions | |
| SAST / QA | SonarQube + Dependabot | |
| IaC | Terraform (Azure) | |
| CaC | AWX / Ansible | |
| Orquestación | .NET Aspire (HST hosts) | |
| Mapping | Mapperly | Sustituto de AutoMapper |
| JSON | System.Text.Json | No usar Newtonsoft.Json en nuevos |
| Contenedores | Docker / Azure Container Apps | |
| Observabilidad | Monitorización de Servicios | |

**Autenticación aprobada:** `EntraID` (esquema `EntraID` o `EntraIdOrTGT` en migración).
**NO usar en nuevos proyectos:** CAS, TGT, LDAP, Alfresco, Oracle, Java/Spring/Struts.

### 3.2. Convención de Nombres de Repositorios GitHub

| Patrón | Tipo | Ejemplo |
|--------|------|---------|
| `APB.API.XXX` | Microservicio API backend | APB.API.TES, APB.API.TBE, APB.API.AIS |
| `APB.APP.XXX` | Aplicación frontend/web | APB.APP.ARG (ARGOS), APB.APP.INS |
| `APB.HST.XXX` | Host Aspire orquestador | APB.HST.PAD, APB.HST.EQV, APB.HST.REB |
| `APB.MSG.XXX` | Librería de mensajes (contratos) | APB.MSG.EME, APB.MSG.GEI, APB.MSG.PSR |
| `APB.LIB.XXX` | Librería compartida | APB.LIB.ARG |
| `PLANOL-*` | Aplicaciones GIS/Plano | PLANOL-koop, PLANOL-QGIS-Resources |
| `SOSTRAT-*` | Módulos Java SÒSTRAT (legacy) | SOSTRAT-Sostrat-MJ8 |

### 3.3. Pipeline CI/CD Obligatorio

```
Checkout → Restore → Build → Unit Test → APB Validations
→ Sonar Scanner → Quality Gate → Deploy → Healthcheck → Notification
```

**Políticas QA obligatorias:**

| Métrica | Umbral |
|---------|--------|
| Blocker Issues | 0 |
| Coverage (new code) | ≥ 60% |
| Maintainability | ≥ B |
| Reliability | ≥ C |
| Security | ≥ C |

### 3.4. Modelo de Roles y Permisos (Entra ID)

**Transición del modelo de autorización** (migración CAS/LDAP → Entra ID):

| OnPremises | Entra ID |
|------------|----------|
| Permisos asignados a roles de aplicación | Roles definidos por aplicación, comprobados en el token emitido por Entra ID |
| Roles asignados directamente a usuarios | Roles asignados a **grupos**; los usuarios se incorporan a los grupos |

Es decir: `Permisos (OnPrem) → Roles (Entra ID)` y `Roles (OnPrem) → Grupos de
usuarios (Entra ID)`. La autorización se resuelve comprobando los roles
contenidos en el token, no consultando permisos individuales por usuario.

**Convención de nombre de grupo** (el grupo es quien porta el rol, no lo
sustituye — ver más abajo la convención de nombre de *rol*):
Formato: `GRP_{ENTORNO}_{APP}_{ROL}`
Ejemplo: `GRP_PRO_ARG_TWO` (Producción, ARGOS, Tower Operator)

**Catálogo de roles por defecto:**

| Rol nuevo | Rol/permiso anterior | Propósito | Alcance |
|-----------|----------------------|-----------|---------|
| `APPLICATION_AUDIT` | Rol `APPLICATION_AUDITOR` / permiso `ACCESS_AUDITOR` | Acceso de solo lectura a toda la aplicación para auditorías internas, revisiones de cumplimiento | Todas las operaciones de consulta (GET) |
| `FRAMEWORK_ADMINISTRATOR` | Rol `FRAMEWORK_ADMINISTRADOR` | Administradores del framework DOCKS | Acceso total — administración del framework, configuración global, soporte avanzado de plataforma |
| `APPLICATION_CLIENT` | — | Aplicación que se autentica sin identidad de usuario (Cl@ve, Application-to-Application, procesos automáticos). Ej.: E33, EPS | No representa una persona física; flujo de credenciales de aplicación |
| `APPLICATION_USER_EXT` | — | Persona física externa que accede a APIs/aplicaciones del Puerto. Ej.: P33, EQV, CTA | Asociado a identidad personal; control de acceso de terceros |
| `APPLICATION_CLIENT_EXT` | — | Aplicación externa que consume APIs del Puerto sin usuario detrás. Ej.: API CTA | Autenticación por credenciales de aplicación; no asociado a usuario físico |
| `APPLICATION_USER` (opcional) | Rol `APPLICATION_USUARI` / permiso `ACCESS_USUARI` | Funcionalidades operativas de un usuario estándar | Normalizado al inglés para estandarización y soporte |
| `APPLICATION_ADMINISTRATOR` (opcional) | Rol `APPLICATION_ADMINISTRADOR` / permiso `ACCESS_ADMINISTRADOR` | Administración completa de la aplicación | Acceso administrativo total de la app |

> ⚠️ **Pendiente de decisión**: el rol "Gestor de la aplicación" (permiso
> anterior `ACCESS_GESTOR`) no tiene definición final aprobada — queda por
> decidir si se fusiona con `APPLICATION_ADMINISTRATOR` o se mantiene como
> rol independiente. No usar como referencia hasta que se cierre esa decisión.

**Roles propios de aplicación**: además de los roles estándar, cada
aplicación puede mantener roles personalizados de negocio propios (ej.
`VIA_SGOIRI`), que se conservan durante la migración y siguen asignándose
como App Roles de Entra ID.

**Autorización API-to-API**: el modelo legacy de permisos `API_CALL_*` para
conceder acceso entre aplicaciones desaparece en Entra ID. Se sustituye por
App Registrations + permisos de aplicación + App Roles asignados entre APIs.
Ejemplo:
```
API_BKO_DEV
 └── APPLICATION_ADMINISTRATOR
      └── API_EME_DEV
API_BKO_DEV
 └── APPLICATION_ADMINISTRATOR
      └── API_MES_DEV
```
La comunicación API-to-API se basa en roles de aplicación, no en permisos
específicos `API_CALL_*`.

**Convención de nomenclatura de roles** (distinta de la convención de nombre
de grupo anterior — el rol se define a nivel de aplicación en Entra ID; el
grupo es el vehículo por el que se asigna a usuarios): MAYÚSCULAS,
separación mediante `_`, inglés, sin acentos ni caracteres especiales. Ej.
válidos: `APPLICATION_AUDIT`, `APPLICATION_USER`, `APPLICATION_ADMINISTRATOR`,
`FRAMEWORK_ADMINISTRATOR`, `APPLICATION_CLIENT`, `APPLICATION_CLIENT_EXT`,
`APPLICATION_USER_EXT`.

### 3.5. Entornos

| Entorno | Uso |
|---------|-----|
| DEV / DES | Desarrollo |
| PRE | Preproducción / pruebas |
| PRO | Producción |

### 3.6. Migración EntraID

- AuthScheme: `TGT` → `EntraIdOrTGT` → `EntraID`
- Permisos: roles en App Registration de Entra ID. La asignación real es
  Rol → Grupo → Usuario (nunca Rol → Usuario directo) — ver catálogo completo
  de roles y modelo de grupos en §3.4.
- SCIM para provisioning automático.
- SSO con GitHub Enterprise.

---

## 4. Catálogo de Aplicaciones

### 4.1. ARGOS — Torre de Control / Operaciones Marítimas

**Jira:** AOM | **GitHub:** APB.APP.ARG, APB.API.ARG
**Equipo:** Alberto Ponseti (PO), Jose Joaquin Mena, Cristian Monzon, Adrian Rodriguez, Carlos Jorge, Christian Torreblanca, Ignasi Fandos (QA Lead), Suilen Hernandez (QA)
**Proveedor:** ICONUS / AMBAR | **Criticidad:** Muy Alta

Aplicación de **gestión de operaciones marítimas en tiempo real**. Arquitectura de microservicios DOCKS:

| Microservicio | API | Función |
|---------------|-----|---------|
| MS_PORTCALL (TES) | APB.API.TES | Gestión de escalas |
| MS_BERTH (TBE) | APB.API.TBE | Gestión de atraques |
| MS_MOVEMENT (TMO) | APB.API.TMO | Gestión de movimientos |
| MS_CALL (TCA) | APB.API.TCA | Gestión de trucadas/llamadas |
| MS_SHIP | APB.API.SHP | Datos de buques, exenciones práctico |
| MS_SERVICE | APB.API.SRV | Servicios portuarios (práctico, remolque, amarre) |
| MS_MILESTONE | APB.API.MIL | Hitos operativos |
| MS_ADMINISTRATION | APB.API.ADM | Notificaciones administrativas |
| MS_VTMOS (VTM) | APB.API.VTM | Integración con VTS (Kongsberg) |
| MS_GEOLOCATION (TGE) | APB.API.TGE | Geolocalización de buques |

**Mensajería entre microservicios:**

| Mensaje | Topic | Emisor | Suscriptores |
|---------|-------|--------|--------------|
| MSG0001 | PositionUpdated | TGE | — |
| MSG0004 | PortcallUpdated | SOSTRAT→TES | TBE, TMO |
| MSG0005 | MilestoneUpdated | TCA, TBE, SRV | MS_MILESTONE |
| MSG0010 | VTMMilestone | VTM | TCA |
| MSG0011 | ShipEvent | TBE | MS_SHIP |
| MSG0017 | BerthUpdated | SOSTRAT→TBE | — |
| MSG0018 | CallUpdated | TCA | TES, TMO |
| MSG0019 | PortcallStateChanged | TES | — |
| NOT0001 | AdministrationUpdated | Varios | MS_ADMIN |
| NOT0002 | BerthNotification | TBE | MS_ADMIN |

**Roles ARGOS:** `MANAGE_TOWER_OPERATOR`, `MANAGE_TOWER_SUPERVISOR`, `MANAGE_TOWER_VTM`, `MANAGE_TOWER_VTS`, `APPLICATION_ADMINISTRATOR`, `APPLICATION_AUDIT`, `FRAMEWORK_ADMINISTRATOR`

**Pantallas principales:** PNT0001 (Lista PortCalls), PNT0016 (Movimientos activos), PNT0030 (Board Kanban), PNT0031 (Planificación atraques), PNT0032 (Line-up / Mapa distancias), PNT0039 (Mapa distancias entre vaixells), ExtendedShip (info VTS Kongsberg).

### 4.2. MDE — Moll de l'Energia

**Jira:** AOM (etiqueta MOLL_ENERGIA) | Ecosistema: mismo que ARGOS
**Equipo:** Alberto Ponseti (PO), Jose Joaquin Mena, Suilen Hernandez (QA)

Ver §2.10 para detalle funcional.

### 4.3. SÒSTRAT — Sistema Central de Gestión de Servicios Portuarios *(Legacy)*

> ⚠️ **Legacy.** Stack Java no aprobado para nuevos desarrollos. Los agentes deben conocer
> SÒSTRAT para entender integraciones, tickets y dominios funcionales, pero NO deben
> recomendar su stack (Java/Struts/Oracle/CAS) para ningún nuevo artefacto.
>
> **Fuente de verdad detallada**: `discovery/ddd-sostrat-mj8/` contiene la descomposición DDD
> completa de SÒSTRAT (24 dossiers de aplicación, uno por bounded context, cada uno
> verificado campo a campo contra el código real — no solo generado). Empezar por
> `discovery/ddd-sostrat-mj8/app-dossiers/INDEX.md` y `INFORME_EJECUTIVO.md` antes de
> analizar cualquier módulo de SÒSTRAT en profundidad — evita repetir análisis ya hecho.

**Jira:** SOSO, SOSI, ESCA, ESCADOS, ESCAIIB, FACT, FACTSTD, CONCB, FER, MARPOL, MERC, MERCA, MERCB, MMPP, PIF, PESCA, PPS, TRANSTE, AIGUADA, CTA, MANEST, MEDI, TERC, EST, TREDI, COARRI, WASDIS, PAXLST, DEPOTSIS, MVM, INTDBPRO, MILL, CLAVEG, SOSGIS, BUNKER, MARDEP
**GitHub:** SOSTRAT-Sostrat-MJ8, SOSTRAT-Sostrat-JEE
**Proveedor:** IN2 (ICONUS para .NET) | **Criticidad:** Muy Alta
**Equipo:** Xavier Estebanell, Toni Estrada, Elisabeth Fernandez, Juan Manuel Miguel, Enrique Salinas, Daniel Padron, Raul Tamurejo, Jon Oyarzabal, Miguel Lostal, Victor Portillo, Pere Martinez, Luis Rivas, Eduardo Guadalupe

**Stack legacy (solo contextual):** Java SE, Spring 5.2.6, Struts 1.3.10, Tiles, Apache ANT 1.9.16, JPA, SpringBatch 4.2.2, CXF 2.6.1, Oracle DB, CAS/Apereo, Tomcat (cluster activo-pasivo).

**Módulos funcionales:**

| Proyecto Jira | Función |
|---------------|---------|
| ESCA / ESCADOS / ESCAIIB | Gestión de escalas (datos buque, atraque, operaciones) |
| FACT / FACTSTD | Facturación de tasas portuarias |
| CONCB | Concesiones (títulos, ocupaciones, liquidaciones L6) |
| GESGAR | Gestión de Garantías |
| FER | Ferrocarril portuario |
| MARPOL | Servicios MARPOL (recogida residuos buques) |
| MERC / MERCA / MERCB | Mercancías (manifiestos EDI, liquidación T2/T3) |
| MMPP | Mercancías Peligrosas (autorizaciones, notificaciones) |
| PIF | Puesto de Inspección Fronteriza — operación real de camión/contenedor en el finger de muelle (agregado `OperacioPif`). Candidato confirmado a fusión con SCPP (capacidad/turnos/resultado de inspección, agregado `LlocDInspeccio`/`Inspeccio`) por acoplamiento síncrono transaccional real — ver `dossier-11-pif.md`/`dossier-19-inspeccion-scpp.md`. Ambos comparten además acoplamiento síncrono con **Posicionament** (`CN_Posicionament_Impl.java`, posicionamiento físico de contenedores), capacidad de negocio real identificada sin bounded context propio todavía (`PLAN_FASES_FUTURAS.md #102`) |
| TRANSTE | Transporte terrestre (preavisos, autorizaciones) |
| PPS | Pases y Permisos de acceso |
| PESCA | Actividad pesquera |
| EST | Estadísticas portuarias |
| AIGUADA | Servicio agua potable a buques |
| CTA | Control de Contenedores |
| BUNKER | Bunkering (suministro combustible) |
| MARDEP | Marinas Deportivas |
| DEPOTSIS | Depósito en muelle libre T6 |
| MANEST | Mans d'Estiba (control estibadores) |
| MEDI | Medio Ambiente |

**⚠️ Consumidores externos reales de la base de datos de SÒSTRAT (hallazgo 2026-07-14)**: al menos **9 aplicaciones .NET ya en producción** (`APB.API.CPR`, `APB.API.IPB`, `APB.API.CTS`/`APB.APP.CTA`, `APB.API.AUT`, `APB.API.REB`/`apb.p51`, `APB.API.LRT`, `APB.API.OPS`, ecosistema `APB.API.CRE`/`APB.APP.CRE`/`APB.API.VXL`/`APB.API.SLC`) leen o **escriben directamente** sobre tablas Oracle de SÒSTRAT sin pasar por ningún API/evento formal — 3 de ellas con escritura directa confirmada. Ningún análisis de dominio/bounded context de SÒSTRAT debe darse por completo sin comprobar este universo de aplicaciones externas primero (ver `discovery/ddd-sostrat-mj8/EXTERNAL_CONSUMERS_AUDIT.md` para el detalle completo por app/tabla). Esta es precisamente la razón por la que `apb-agent-ddd-v1.0` incorporó una Fase 0 de rastreo de consumidores externos (ver §11).

**Tablas clave de SÒSTRAT (solo para entender integraciones):**

| Tabla | Descripción |
|-------|-------------|
| ESCALA | Escalas marítimas |
| ESCALA_ASPECTE | Versiones/aspectos de la escala |
| ATRACADA | Atraques |
| LIQUIDACIO / LIQUIDACIO_LINIA | Liquidaciones y líneas |
| MMPP_AUTORITZACIO / MMPP_NOTIF | Mercancías peligrosas |
| RESIDUS_ESCALA | Residuos por escala |
| PROFERCONT | Operaciones ferroviarias de contenedores |
| PARTIDA_VERSIO | Versiones de partidas de manifiestos |
| EQUIPAMENT | Contenedores / equipos |
| OPS_B_SESSIONS (DSS_DWH) | Sesiones de Shore Power (facturación electricidad) |

**Procesos batch especiales (SpringBatch):** **90 jobs confirmados** por recuento exacto sobre 67 ficheros `sostrat-batch-*.xml` (auditoría 2026-07-14, `coverage-audit.md §8.3` — corrige la estimación previa de "~80"). Circuitos principales: BERMAN, WASDIS, COARRI, CODECO, COPINO, HAZMAT/IFTDGN (MMPP), IFCSUM/CUSCAR (Manifiestos), PAXLST, TarifasResidus (MARPOL), Conciliación de terminales, **VUA/SAPL** (Ventanilla Única Aduanera **española/AEAT**, el job más frecuente del sistema, cada 1 minuto) y **DMS** (Declaración Marítima de Sanidad — este es el circuito real de la **EMSWe europea**, no VUA). Ver §5.1 para el detalle de arquitectura EDI y la corrección VUA≠EMSWe.

### 4.4. APIs del Framework ARQ (DOCKS)

42+ APIs identificadas. Principales:

| API | GitHub | Función |
|-----|--------|---------|
| APB.API.APPS | portdebarcelona/APB.API.APPS | Catálogo de aplicaciones |
| APB.API.PERMIS | portdebarcelona/APB.API.PERMIS | Permisos |
| APB.API.ROL | portdebarcelona/APB.API.ROL | Roles |
| APB.API.USUARIOS | portdebarcelona/APB.API.USUARIOS | Usuarios |
| APB.API.AUDIT | portdebarcelona/APB.API.AUDIT | Auditoría |
| APB.API.DOCUMENTS (DCM) | portdebarcelona/APB.API.DOCUMENTS | Documentos |
| APB.API.FLC | portdebarcelona/APB.API.FLC.FileCloud | Ficheros SharePoint |
| APB.API.EMAIL | portdebarcelona/APB.API.EMAIL | Email corporativo |
| APB.API.SMS | portdebarcelona/APB.API.SMS | SMS (v2 en desarrollo) |
| APB.API.CALENDAR | portdebarcelona/APB.API.CALENDAR | Calendario |
| APB.API.LANGUAGE | portdebarcelona/APB.API.LANGUAGE | Multiidioma |
| APB.API.GRIDCONFIG | portdebarcelona/APB.API.GRIDCONFIG | Configuración grids |
| APB.API.NOTIFICACION | portdebarcelona/APB.API.NOTIFICACION | Notificaciones (SOAP legacy) |
| APB.API.AVI | portdebarcelona/APB.API.AVI | Avisos |
| APB.API.AIS | portdebarcelona/APB.API.AIS | Publicador mensajes AIS |
| APB.API.ARG | portdebarcelona/APB.API.ARG | ARGOS (nuevo, ene 2026) |
| APB.API.PVI | portdebarcelona/APB.API.PVI | Puertas Virtuales (jun 2026) |
| APB.API.CTS | portdebarcelona/APB.API.CTS | Contenedores (integración SOSTRAT) |
| APB.API.EME | portdebarcelona/APB.API.EME | Emergencias |
| APB.API.ORD | portdebarcelona/APB.API.ORD | Órdenes de Pago |
| APB.API.ZONES | portdebarcelona/APB.API.ZONES | Zonas |
| APB.API.EMP | portdebarcelona/APB.API.EMP | Empleados |
| APB.API.RESPONSIBLE | portdebarcelona/APB.API.RESPONSIBLE | _(función pendiente de confirmar — dominio TBD)_ |
| APB.API.ROSS | portdebarcelona/APB.API.ROSS | _(función pendiente de confirmar — dominio TBD)_ |
| APB.API.SIG | portdebarcelona/APB.API.SIG | _(posible: Firmas/Signatures — dominio TBD)_ |

> **Nota (2026-06-30):** Esta tabla documenta un subconjunto representativo. El **inventario completo** de APIs publicadas en Azure API Manager (`https://apipre.portdebarcelona.cat`) está en [`API_INVENTORY_APIM.md`](API_INVENTORY_APIM.md) — ~100 APIs estructuradas por ecosistema inferido con preguntas DDD abiertas. Los ecosistemas identificados ahí son **hipótesis de trabajo**, no dominios validados — el análisis DDD (#38 Fase 0) es quien definirá los bounded contexts correctos. **La agrupación actual puede no ser correcta.**

**Mejoras en curso ARQ:** actualización apibase 10.0.2, migrar AutoMapper→Mapperly, quitar Newtonsoft.Json, migrar auth EntraID, mover JenkinsFile a /deploy, cambiar .sln→.slnx.

### 4.5. Otras Aplicaciones DOCKS (.NET)

| App | Jira | GitHub | Función |
|-----|------|--------|---------|
| VIA (Viajes) | OSPROG | APB.VIA | Viajes empleados, cheques gourmet |
| ODP (Órdenes de Pago) | — | APB.API.ORD | Órdenes de pago (app piloto Cloud) |
| P33 | FACTSTD | APB.APP.E33 | Facturación estándar módulo 33 |
| REB (Recibos) | FACTSTD | APB.HST.REB | Gestión de recibos |
| EQV (Seguimiento Vehículos) | PIF | APB.HST.EQV, APB.API.EQL | Seguimiento daños carga/descarga |
| PEM / SISPEM | SISPEM | APB.API.EME, APB.MSG.EME | Emergencias / seguridad industrial |
| PVI (Puertas Virtuales) | PVI | APB.API.PVI | Control acceso vehículos (PORTIC) |
| INS (Escáner) | — | APB.APP.INS | Escaneo camiones/contenedores |
| GSM (SMS) | ARQ | APB.APP.GSM | Gestión SMS corporativo |
| CNF (Configuración) | ARQ | ConfigurationApp | Administración portal DOCKS |

### 4.6. Administración Electrónica

**Equipo:** Manuel Martinez, Cristian Rubio, Juan Carlos Baca
**GitHub:** contractacioweb, APB.HST.PAD, APB.MSG.PSR, APB.MSG.GEI

| App | Función |
|-----|---------|
| PAE | Plataforma Administración Electrónica |
| Contratación | Expedientes de contratación pública |
| Portafirmas (PTF) | Firma electrónica (integración AGE) |
| GEISER | Registro electrónico (integración AGE) |
| Notifica | Notificaciones electrónicas (AGE) |
| FACe | Facturación electrónica |
| PLACSP | Plataforma de Contratación del Sector Público |

### 4.7. GIS / Plano del Puerto

| App | Jira | GitHub | Función |
|-----|------|--------|---------|
| PlanolPort | PPP, POT, PLAN, PED | PLANOL-* (20+ repos) | Plano integral del puerto |
| GISPEM | GISPEM, SWPEM | PLANOL-GISPEM-desktop | Seguridad industrial / emergencias |
| GIS-Batimetria | GISBAT | — | Batimetrías |
| GIS Atracs | SWATR | — | GIS de atraques |
| GIS Concessions | SWCONC | — | GIS de concesiones |
| Koop | — | PLANOL-koop | Servidor ArcGIS Features |
| BIM/IFC | — | PLANOL-BIM-IFC-Catalog | Catálogo BIM/IFC del puerto |
| Geofotos | — | PLANOL-django_geofotos_app | App Django geofotos |
| Port 3D | — | PLANOL-W2PY-port3d | Visualización 3D |
| Geoposicionament Vaixells | — | PLANOL-geoposicionament-vaixells-video-frontend | Vue geoloc. buques + video |

### 4.8. Aplicaciones de Gestión de Identidades (2025–2026)

**Jira:** ARQ (Fases 1–5) | **GitHub:** APB.API.USUARIOS

Sistema centralizado: altas/bajas de usuarios internos, colaboradores externos, funcionales y técnicos; catálogo técnico de aplicaciones (IAppCatalogProvider); integración Entra ID + LDAP + GPCN; notificaciones a RRLL, Servicios Médicos, PRL; trazabilidad completa.

### 4.9. Aplicaciones Corporativas y de Terceros

| App | Función | Tipo |
|-----|---------|------|
| Salesforce CRM | CRM comercial y marketing | SaaS |
| SAGE XRT | Tesorería (migrando a SaaS Cloud) | Producto/SaaS |
| Etempo / MEDTRA | Control fichajes, medicina trabajo | Producto |
| Rosmiman (GISCSV) | GMAO — gestión activos e infraestructuras | Producto |
| Vinfopol | Gestión policía portuaria (sustituye GesCity) | Producto Cloud |
| Intranet (Liferay) | Portal empleados (migración a SaaS 2027) | Legacy/SaaS |
| Portal Web | Web pública (Drupal / portdebarcelona.cat) | CMS |
| OpenData / CKAN | Plataforma datos abiertos | Open Source |
| EMSWe | European Maritime Single Window | Integración EU |
| Brand Center | Gestión de marca corporativa | — |
| Control Presupuestario | VB6 legacy | Legacy |
| Alfresco | Gestor documental *(en migración a SharePoint)* | Legacy |
| DSS / MicroStrategy | Business Intelligence | Producto |

---

## 5. Integraciones

### 5.1. PORTIC / EDI

Plataforma de intercambio electrónico de la comunidad portuaria de Barcelona. Hub EDI entre consignatarios, terminales, Aduana y APB.

**Mensajes EDIFACT:**

| Mensaje | Función |
|---------|---------|
| BERMAN F11 | Preaviso de escala (solicitud) |
| BERMAN F21/F33 | Modificación de escala |
| APERAB / APERAK | Respuesta de aceptación/rechazo |
| WASDIS (WD1041/1042) | Declaración de residuos MARPOL |
| COARRI (RAIL20) | Informe carga/descarga terminal / ferrocarril |
| CODECO | Gate-in / Gate-out contenedores |
| COPRAR | Lista de carga ferrocarril |
| PAXLST | Lista de pasajeros |
| CUSCAR | Declaración sumaria de aduanas |
| IFCSUM | Manifiestos de carga |

**Segmentos EDI clave:** UNB (cabecera intercambio), UNH (cabecera mensaje), BGM (tipo documento), DTM (fechas), RFF (referencias), LOC (ubicación), TDT (detalles transporte), NAD (nombres/direcciones), MEA (medidas: calado, peso), FTX (texto libre / ISPS).

**Arquitectura real del "gateway EDI" en SÒSTRAT (analizada 2026-07-15, ver `discovery/ddd-sostrat-mj8/edi-event-architecture-analysis.md`)**: no es un único gateway — coexisten 3 arquitecturas bajo el mismo nombre:
1. **Cola genérica `MISSATGE_EDI` + adaptador por dominio** (COARRI, CODECO, COPINO, WASDIS, HAZMAT, IFTDGN, IFCSUM/CUSCAR, PAXLST, BERMAN, Facturas). El transporte físico con Portic (`sendMessageOracle`, WSDL `ApbEdiWS.wsdl`/`PortICWS.wsdl`) y el modelo de auditoría (`MissatgeEdi`, `TipusMissatgeEdi` — tabla real de ruteo circuito→sentido, `CircuitEdi`, `ProcesEdi`, `ErrorEdi`) sí son genuinamente compartidos; el parsing de negocio y la generación de APERAK están duplicados por dominio (7 implementaciones distintas, sin clase base común).
2. **Intercambio de ficheros XML ad-hoc**: **VUA/SAPL** (Ventanilla Única Aduanera **española**, AEAT — 4 XSD reales de la AEAT, batch cada 1 min) y **DMS** (Declaración Marítima de Sanidad — **este es el circuito real de la EMSWe europea**, formulario FAL). Ninguno de los dos usa `MISSATGE_EDI`.
3. **Consulta SOAP síncrona bajo demanda** (parte de CODECO en transporte terrestre, vía `PortICWS`).

**⚠️ Corrección importante de terminología**: VUA/SAPL (implementado en `service/pif/impl/sapl`) **no es** la Ventanilla Única Europea pese al nombre — es la aduana **nacional** española (AEAT). El circuito que sí implementa la *European Maritime Single Window environment* (EMSWe, Directiva UE 2019/1239) es **DMS**. No confundir ambos al hablar con negocio o al diseñar el bounded context correspondiente.

### 5.2. Administración General del Estado (AGE)

| Sistema | Función |
|---------|---------|
| GEISER | Registro electrónico de entrada/salida |
| Notifica | Notificaciones electrónicas a ciudadanos/empresas |
| FACe | Factura electrónica |
| Portafirmas AGE | Firma electrónica de documentos oficiales |

Integración actual: SpringBoot (SÒSTRAT) → API .NET REST → SOAP GEISER/Portafirmas.

### 5.3. AIS (Automatic Identification System)

- Datos de posición de buques en tiempo real.
- Integración con Port of Antwerp-Bruges (formato RAW, endpoint REST).
- API publicadora: APB.API.AIS → Azure Service Bus → MS_GEOLOCATION (TGE).

### 5.4. VTS Kongsberg

- Sistema VTS (Vessel Traffic Service) — proveedor Kongsberg.
- Milestones de tipo CallEvent y Waypoints.
- Pantalla ExtendedShip en ARGOS para información adicional del movimiento.
- Integración: APB.API.VTM (MS_VTMOS).

### 5.5. Alfresco (Capa SOA — Legacy en Migración)

Servicios SOAP para integración con Alfresco. En migración progresiva a API REST de SharePoint/APB.API.FLC.

Servicios actuales: createFolder, deleteFolder, moveDocument, existElement, setDocumentMetadata, setDocumentURN, createFolderURN, validateURN, getThumbnail.

Aplicaciones que usan Alfresco (en migración): Rosmiman, Contratación, SÒSTRAT, Sede Electrónica, Web, Intranet.

### 5.6. Shore Power / OPS

- Suministro eléctrico a buques atracados en Moll de l'Energia.
- Datos de consumo: tabla `OPS_B_SESSIONS` en BBDD `DSS_DWH`.
- Facturación de electricidad integrada en SÒSTRAT (tarifas P11000 BE1/BE2).

---

## 6. Estrategia GoToCloud

Migración progresiva OnPremise → Azure Cloud. **Principio: Cloud First** para toda nueva iniciativa.

### 6.1. Roadmap

| Tipo de aplicación | Estrategia |
|--------------------|------------|
| Desarrollo propio DOCKS | Containerización (Docker/Container Apps) + Azure SQL |
| Producto de mercado | Migración a versión SaaS cuando esté disponible |
| Legacy | Análisis caso a caso: lift-and-shift, refactor, o amortización |

### 6.2. Proyectos de Migración en Curso

| Proyecto | Estado |
|----------|--------|
| DOCKS a Azure Container Apps | En progreso |
| Gestor Documental: Alfresco → SharePoint Online | En progreso |
| Auth: CAS/LDAP → Microsoft Entra ID | En progreso |
| BBDD: Oracle → Azure SQL | En progreso (progresivo) |
| APIM (ApiManager) — Fase 2 | En implementación |
| IaC/CaC: Terraform + AWX/Ansible | Operativo |
| Intranet (Liferay) → SaaS | Planificado 2027 |
| SAGE XRT → Sage Cloud | En progreso |
| VTMOS / GMV | Pendiente (contactar proveedores) |
| NAS → Azure Storage (~50TB) | Planificado |

### 6.3. Migraciones de Documentos

| Origen | Destino | Estado |
|--------|---------|--------|
| Alfresco → Contratación | SharePoint | Completada |
| Alfresco → P33 | Azure Storage | Completada |
| Alfresco → ODP | Azure | Completada |
| Alfresco → SÒSTRAT | SharePoint | Pendiente |
| Alfresco → Báscula | Azure Storage | Pendiente |

Herramienta: GestorDocMigrationTool (portdebarcelona/GestorDocMigrationTool).

### 6.4. Gobernanza Cloud

- **Nomenclatura de recursos Azure**: estandarizada (MISA-1509).
- **Etiquetas y Azure Policy**: gobernanza de costes y cumplimiento.
- **FinOps**: políticas de retención, archivado, disponibilidad.
- **Entornos PRE**: disponibles solo en horario laboral (optimización costes).

---

## 7. Seguridad y Cumplimiento

### 7.1. Marcos Normativos

| Marco | Aplicación |
|-------|------------|
| ENS | Obligatorio para administración pública española |
| ISO 27001 | En proceso de certificación/mantenimiento |
| RGPD / LOPD | Protección de datos personales |
| ISPS | Seguridad buques e instalaciones portuarias |

### 7.2. Herramientas de Seguridad

| Herramienta | Uso |
|-------------|-----|
| SonarQube | Análisis estático (SAST) obligatorio en pipeline |
| Dependabot | Análisis de dependencias (GitHub) |
| GitHub Security | Code scanning, secret scanning, dependency scanning |
| Nessus | Escáner de vulnerabilidades (DMZ y servidores) |
| APIM | Control de acceso, rate limiting, auditoría de APIs |
| FortiSandbox | En proceso de baja |

### 7.3. Control de Accesos por Sistema

| Sistema | Mecanismo |
|---------|-----------|
| Aplicaciones DOCKS (Cloud) | Microsoft Entra ID + grupos APIM — catálogo de roles y modelo de grupos en §3.4 |
| SÒSTRAT (legacy) | CAS (Apereo) + LDAP + Active Directory |
| Alfresco (legacy) | CAS + Kerberos + LDAP |
| Acceso físico al puerto | KABA + DormaKaba + huellas digitales (biometría) |

---

## 8. Modelo de Contratación

**Estructura:** Acuerdo Marco (AM) → Contrato Basado (CB) → Concreción

### 8.1. Proveedores Principales

| Proveedor | Ámbito |
|-----------|--------|
| ICONUS | ARGOS/MDE, desarrollo .NET DOCKS, CAS (legacy) |
| IN2 | SÒSTRAT (Java), Alfresco |
| CiSGA / T-Systems | Soporte al usuario, helpdesk, infraestructura |
| Ambar | ARGOS microservicios, GIS |
| Schneider | PSIM / CCTV / VMS |
| GMV | Geoespacial, ayudas a la navegación |
| PORTIC | Plataforma EDI |
| Inetum | JSM / ITSM, consultoría QA |
| Izertis | JSM / ITSM |
| Sage | Tesorería (XRT) |

---

## 9. Herramientas y Plataformas

| Herramienta | Uso |
|-------------|-----|
| Jira Software | Gestión de proyectos y tickets (150 proyectos) |
| Jira Service Management | Portal ITSM (APBPIT) |
| Confluence | Documentación técnica y funcional (espacios APLIS, Arquitectura) |
| GitHub Enterprise | Código fuente (520+ repos org:portdebarcelona) |
| GitHub Copilot | Asistencia IA para desarrollo |
| Jenkins | CI/CD (shared libraries) |
| SonarQube | Análisis estático de código |
| Azure (DevOps, Container Apps, SQL, Service Bus, APIM, Key Vault, Storage…) | Infraestructura cloud |
| Atlassian Rovo | IA corporativa Atlassian |
| Microsoft 365 | Colaboración (Teams, SharePoint, Outlook) |
| Salesforce | CRM |
| Terraform | IaC para Azure |
| AWX / Ansible | CaC |
| Nessus | Escáner de vulnerabilidades |
| MicroStrategy | Business Intelligence |
| GeoServer | Servidor de mapas OGC (WMS/WFS) |
| CKAN | Plataforma de datos abiertos |
| Psi Probe | Monitorización Apache Tomcat (legacy) |
| KeePass | Gestión de contraseñas |

---

## 10. Tabla de Relación: Jira / Aplicación / Equipo / GitHub

| Clave Jira | Aplicación | Equipo/Personas | Repos GitHub |
|------------|-----------|-----------------|--------------|
| AOM | ARGOS / MDE | Alberto Ponseti, Jose J. Mena, Cristian Monzon, Adrian Rodriguez, Ignasi Fandos (QA), Suilen Hernandez (QA) | APB.APP.ARG, APB.API.TES, APB.API.TBE, APB.API.TMO, APB.API.TCA, APB.API.TGE, APB.API.AIS, APB.LIB.ARG, APB.API.ARG |
| ARQ | Arquitectura .NET / DOCKS | Alina Suros, Manuel Villalonga, Vanessa Jimenez, Veronica Cartagena, Gemma Garrigosa, Sergi Gil, Andrew Ursel | Apb_ARQ_Templates, ArqApp, ArqApiBase, APB.API.*, ConfigurationApp, APB.APP.GSM |
| SOSO/ESCA/FACT… | SÒSTRAT | Xavier Estebanell, Toni Estrada, Elisabeth Fernandez, Juan Manuel Miguel, Enrique Salinas, Daniel Padron, Raul Tamurejo, Jon Oyarzabal, Miguel Lostal, Victor Portillo, Pere Martinez, Luis Rivas, Eduardo Guadalupe | SOSTRAT-Sostrat-MJ8, SOSTRAT-Sostrat-JEE |
| AE | Admin. Electrónica | Manuel Martinez, Cristian Rubio, Juan Carlos Baca | contractacioweb, APB.HST.PAD, APB.MSG.PSR, APB.MSG.GEI |
| OPS | Operaciones IT | Albert Prats, Israel Perez, Ivan Perez, Sergi Fernandez, Pol Ponsico, Diego Rodriguez | CICD_PipeLine_APB, terraform-*, PipeLineDevSecOpsOthers |
| CIBER | Ciberseguridad | Albert Prats, Alina Suros | — |
| TECH | Tech&Ops | Debora Martin (CTO) | — |
| MISA | Control de Proyectos | Alina Suros, Alain Pica | — |
| OSPROG | OSMA Programación | Eva Soto, Victoriano Almeida, Wafae Afkir, Carlos Maestra, Enrique Puga, Wail El Achiri | APB.VIA |
| SISPEM | Emergencias | Maria Soledad Flores, Wafae Afkir | APB.API.EME, APB.MSG.EME |
| PVI | Puertas Virtuales | Maria Soledad Flores, Eduardo Guadalupe | APB.API.PVI |
| PPP/POT/PLAN/PED | PlanolPort | — | PLANOL-* |
| SALESFORCE/OTC/CRM | CRM | — | — |
| BI | Business Intelligence | — | — |
| RM / TO2025 | Roadmap Tech&Ops | Debora Martin | — |

---

## 11. Estrategia de IA Corporativa

- **Marco de IA corporativa**: gobernanza, políticas, uso responsable (POLICY_AI_USAGE).
- **Spec-Driven Development (SDD)**: integración de IA en el SDLC con GitHub Copilot.
- **Valoración COSMIC asistida por IA**: generación de estimaciones funcionales (CFP).
- **Generación de especificaciones (OpenAPI)**: agentes para borrador de specs en Markdown/Word.
- **Integración con Atlassian Rovo**: IA sobre datos Confluence/Jira.
- **Análisis de seguridad obligatorio**: todo skill/agente de terceros requiere revisión antes de incorporarse en GitHub corporativo.
- **Política de privacidad**: no usar código APB para entrenamiento de modelos externos.

---

## 12. Diccionario de Términos

### 12.1. Negocio Portuario

| Término | Definición |
|---------|-----------|
| Escala (PortCall) | Visita de un buque al puerto, desde la solicitud hasta la salida |
| Atraque (Berth) | Asignación de un puesto de amarre a un buque |
| Abarloado | Buque amarrado a otro buque (no directamente al muelle) |
| Fondeo / Fondeadero | Zona de anclaje donde el buque espera antes de atracar |
| Moll / Muelle | Estructura de atraque |
| Mòdul | Segmento de un muelle; unidad de medida de ocupación |
| Superzona / Supermoll | Agrupación de muelles (ej: Moll d'Energia = 32A-32H, 34B) |
| Práctico (Pilot) | Piloto que guía el buque en aguas portuarias |
| Practicaje | Servicio de asistencia al buque por un práctico |
| Exempció de pràctic | Exención del servicio de practicaje para capitanes acreditados |
| Remolcador (Tug) | Embarcación de asistencia en maniobras |
| Amarrador (Linesman) | Operario que gestiona las amarras del buque |
| Consignatari | Representante del armador en puerto |
| Armador / Naviera | Propietario o explotador del buque |
| Estibador (Stevedore) | Empresa que carga/descarga mercancías |
| Calat (Draft) | Profundidad del casco bajo la línea de flotación |
| Eslora (LOA) | Longitud total del buque |
| Manga (Beam) | Ancho máximo del buque |
| GT (Gross Tonnage) | Arqueo bruto del buque |
| IMO | Número identificativo internacional del buque |
| MMSI | Maritime Mobile Service Identity |
| Call Sign | Señal de llamada del buque |
| NMI | Navegación Marítima Internacional (determina aplicación IVA) |
| ETA / ATA / ETD / ATD | Estimated/Actual Time of Arrival/Departure |
| Trucada / Llamada (Call) | Comunicación operativa buque/VTS/torre de control |
| 1H Call | Llamada una hora antes de la maniobra |
| 4MN / 2MN | Millas náuticas antes de la boya de entrada |
| Buoy Checkpoint | Punto de control en la boya |
| Milestone (Fita) | Hito operativo en el proceso de una escala |
| Coordinació | Estado donde todos los servicios de un movimiento están coordinados |
| MARPOL | Convenio internacional de prevención de contaminación marítima |
| MARPOL I | Residuos oleosos (hidrocarburos) |
| MARPOL V | Desechos sólidos (basura) |
| WASDIS | Waste Discharge Notification — declaración de residuos |
| Bunkering | Suministro de combustible al buque |
| Shore Power (OPS) | Suministro eléctrico al buque desde tierra |
| Aguada / Aiguada | Suministro de agua potable al buque |
| Manifest / Manifiest | Declaración de carga del buque |
| Partida | Línea de mercancía concreta dentro de un manifiesto, con su propia clasificación arancelaria (versionada — `PartidaVersio`) |
| Conocimiento (B/L) | Bill of Lading — documento de embarque |
| DUA | Documento Único Administrativo (aduanas) |
| Gate-in / Gate-out | Entrada/salida de contenedores de terminal |
| COARRI | Mensaje EDIFACT de operaciones reales de terminal (carga/descarga) — en SÒSTRAT se usa para **conciliar** contra el manifiesto, no como entidad de negocio propia. Existe también un COARRI ferroviario (`RAIL20`), ver §12.2 |
| CODECO | Mensaje EDIFACT de entrada/salida de contenedor de terminal (gate-in/gate-out) — alimenta las autorizaciones de Transporte Terrestre |
| COPINO | Mensaje EDIFACT de recogida/entrega de mercancía y vacíos — circuito bidireccional con respuesta APERAK, dominio de Transporte Terrestre |
| HAZMAT | Circuito EDI de autorización/inspección de mercancías peligrosas (alimenta el listado de carga MMPP) |
| IFTDGN | Circuito EDI de notificación de mercancías peligrosas a las autoridades (con respuesta APERAK), distinto de HAZMAT |
| IFCSUM | Mensaje EDIFACT de manifiesto resumen de carga (familia CUSCAR/CUSREP/CUSRES/CUSRP2) |
| APERAK | Mensaje EDIFACT de acuse/confirmación de aplicación — en SÒSTRAT hay **7 implementaciones distintas**, una por circuito de negocio (WASDIS, MMPP, Facturas, Posicionamiento, Preavisos, PAXLST...), sin código base compartido |
| Contenedor | Unidad estándar de transporte (TEU = 20 pies, FEU = 40 pies) |
| Precinto | Sello de seguridad en contenedores |
| Depotsis | Depósito de mercancía en muelle libre (terminal T6) — solicitud versionada + operaciones de desconsolidación asociadas |
| Título (Titol) | Documento que otorga derecho de uso de terreno/actividad portuaria — término correcto en el modelo real; "Concesión" es solo uno de sus tipos posibles (junto a Autorización, Ocupación, Licencia, Evento), no un sinónimo exacto |
| Operador Portuario | Maestro de terceros con relación comercial con APB (consignatarios, armadores, agentes de aduanas, transitarios) — entidad real `Usuari`, 118 campos, consumida por 30+ módulos |
| Efficiency Network | Programa de certificaciones de sostenibilidad ("Business Club") — estructuralmente una especialización del maestro de Operadores Portuarios (`EmpresaBC extends Usuari`), no un programa aislado |
| SCPP | Servicio de Control y Posicionamiento de Contenedores — capacidad/turnos/resultado de inspección (`LlocDInspeccio`/`Inspeccio`), candidato a fusión con PIF |
| PIF | Puesto de Inspección Fronteriza — operación real de camión/contenedor (`OperacioPif`), distinto de SCPP aunque acoplado |
| Posicionament | Posicionamiento físico de un camión/contenedor en el recinto PIF — capacidad de negocio real identificada en SÒSTRAT sin bounded context propuesto todavía (`CN_Posicionament_Impl.java`) |
| VUA / SAPL | Ventanilla Única Aduanera **española** (AEAT) — coordinación de alta/baja/notificación de entrada-salida de contenedores para aduana. **No es la EMSWe europea** pese al nombre similar |
| DMS | Declaración Marítima de Sanidad (Maritime Declaration of Health) — este es el circuito real que implementa la **EMSWe** europea (formulario FAL) |
| MissatgeEdi / TipusMissatgeEdi | Modelo genérico de mensajería EDI de SÒSTRAT — cabecera de mensaje y tabla real de ruteo circuito→sentido, compartidos por la mayoría de circuitos EDIFACT (no por VUA ni DMS) |
| Preavis | Aviso previo de transporte terrestre |
| ISPS | International Ship and Port Facility Security Code |
| Liquidació | Cálculo de la tasa portuaria aplicable |
| Baremo | Tabla de precios aplicable (BE1 = fijo, BE2 = variable) |
| Sujeto pasivo | Quién paga la tasa (consignatario o terminal) |
| Concesión | Derecho de uso de espacio portuario — en el modelo real es un **tipo de Título** (ver `Título` más arriba), no un sinónimo genérico |
| Garantia | Aval financiero asociado a un título — sin identidad de agregado propia, siempre referencia a `IDTITOL` |
| ADR | Acuerdo Europeo sobre Transporte de Mercancías Peligrosas |

### 12.2. Ferrocarril

| Término | Definición |
|---------|-----------|
| Escala ferroviaria | Paso de un tren por el puerto |
| COARRI ferroviario | Mensaje de movimiento de contenedores por ferrocarril (RAIL20) |
| Terminal ferroviaria | Punto de carga/descarga ferroviaria |
| Ordre de Transport (OT) | Orden de transporte ferroviario |
| Efficiency Network | Marca de calidad de servicios portuarios |

### 12.3. Tecnología (Stack Aprobado)

| Término | Definición |
|---------|-----------|
| DOCKS | Framework corporativo de desarrollo de aplicaciones APB |
| Portal DOCKS | Portal web unificado que aloja las aplicaciones DOCKS |
| APIBASE / ArqApiBase | Plantilla base para APIs .NET del framework |
| ARQBASE / ArqBase | Plantilla base para aplicaciones .NET |
| App Registration | Registro de aplicación en Microsoft Entra ID — ahí se definen los App Roles de la aplicación |
| App Role | Rol de aplicación definido en Entra ID (ej. `APPLICATION_USER`, `APPLICATION_ADMINISTRATOR`) y asignado a grupos, no a usuarios directamente. Catálogo completo en §3.4 |
| EntraID | Microsoft Entra ID (antiguo Azure AD) — estándar de autenticación |
| Service Bus | Azure Service Bus — mensajería asíncrona entre microservicios |
| Topic / Subscription | Patrón publicación/suscripción en Service Bus |
| Redis | Caché distribuida (Azure) |
| APIM | Azure API Management — gateway centralizado de APIs |
| Aspire Host (HST) | Orquestador .NET Aspire para microservicios |
| MSG | Librería de contratos de mensajes (APB.MSG.*) |
| Mapperly | Librería de mapping (sustituto de AutoMapper) |
| FLC (FileCloud) | API de gestión de ficheros en cloud (SharePoint) |
| Pipeline | Flujo automatizado CI/CD (Jenkins + GitHub Actions) |
| Quality Gate | Umbral de calidad SonarQube que debe superar el código |
| Shared Library | Biblioteca Jenkins compartida para pipelines |
| IaC | Infrastructure as Code (Terraform) |
| CaC | Configuration as Code (AWX/Ansible) |
| DevExpress / DevExtreme | Framework UI utilizado en frontend DOCKS |
| CMDB | Configuration Management Database |
| FinOps | Financial Operations — gestión de costes cloud |

### 12.4. Tecnología Legacy (Solo Contextual)

| Término | Definición |
|---------|-----------|
| CAS | Central Authentication Service (Apereo) — SSO para SÒSTRAT. NO usar en nuevos |
| TGT | Ticket Granting Ticket — autenticación legacy. NO usar en nuevos |
| Alfresco | Gestor documental open-source. En migración a SharePoint. NO usar en nuevos |
| SpringBatch | Framework para procesos batch Java (SÒSTRAT). NO usar en nuevos |
| Psi Probe | Monitor open-source para Apache Tomcat (SÒSTRAT) |
| J2EP | Proxy reverso Java para Cross-Domain (GIS legacy) |
| GeoServer | Servidor de mapas OGC — usado en GIS. Stack GIS no DOCKS |

### 12.5. GIS y Cartografía

| Término | Definición |
|---------|-----------|
| GeoServer | Servidor de mapas OGC (WMS/WFS) |
| SLD | Styled Layer Descriptor — estilos para capas GIS |
| Koop | Servidor para servicios ArcGIS Features desde datos no-Esri |
| BIM/IFC | Building Information Modeling / Industry Foundation Classes |
| Batimetria | Medición de profundidades del fondo marino |

### 12.6. Administración Electrónica

| Término | Definición |
|---------|-----------|
| PAE | Plataforma de Administración Electrónica |
| GEISER | Registro electrónico de la AGE |
| Notifica | Servicio de notificaciones electrónicas (AGE) |
| FACe | Punto General de Entrada de Facturas Electrónicas |
| Portafirmas | Sistema de firma electrónica (AGE) |
| PLACSP | Plataforma de Contratación del Sector Público |
| Expediente | Unidad administrativa de contratación |
| AGE | Administración General del Estado |
| CSV | Código Seguro de Verificación de documentos firmados |
| SIA | Sistema de Información Administrativa (código identificador AGE) |

### 12.7. Seguridad y Cumplimiento

| Término | Definición |
|---------|-----------|
| ENS | Esquema Nacional de Seguridad |
| ISO 27001 | Estándar de seguridad de la información |
| RGPD / LOPD | Reglamento General de Protección de Datos |
| ISPS | Código Internacional de Seguridad para Buques e Instalaciones Portuarias |
| OTS | Oficina Técnica de Seguridad |
| SOC | Security Operations Center (vigilancia 24x7) |
| PFSP | Port Facility Security Plan |
| SAST | Static Application Security Testing |
| Branch Protection | Reglas de protección de ramas en GitHub |
| PSIM | Physical Security Information Management |
| VMS | Video Management System |
| LPR | License Plate Recognition (lectores matrículas) |

### 12.8. Contratación

| Término | Definición |
|---------|-----------|
| AM | Acuerdo Marco (contrato paraguas plurianual) |
| CB | Contrato Basado (derivado del AM) |
| Concreción | Encargo específico dentro de un AM/CB |
| PAC | Pla Anual de Contractació |
| MISA | Control de Projectes MISA (proyecto Jira transversal) |
| OSMA | Oficina de Soporte y Mantenimiento de Aplicaciones |
| COSMIC / CFP | Common Software Measurement International Consortium / Function Points |

---

## 13. Mapa de los 150 Proyectos Jira por Dominio

### Operaciones Marítimas
`AOM, PMSTORRECONTROL`

### SÒSTRAT (Gestión de Servicios Portuarios)
`SOSO, SOSI, SOS, SOSOT, SOSGIS, SOSBRAN, SOSTRAT, OTS, ESCA, ESCADOS, ESCAIIB, FACT, FACTSTD, CONCB, GESGAR, FER, MARPOL, MERC, MERCA, MERCB, MMPP, PIF, MVM, PESCA, PPS, TRANSTE, AIGUADA, CTA, MANEST, MEDI, TERC, EST, TREDI, COARRI, WASDIS, PAXLST, DEPOTSIS, BUNKER, MARDEP, CLAVEG, MILL, INTDBPRO`

### Arquitectura y Desarrollo
`ARQ, MISA, TECH`

### Operaciones IT / Infraestructura
`OPS, CIBER, AT, CMEX, GRC, GSBD, GSALC, GS`

### Administración Electrónica
`AE, PAE, APBDIGITAL`

### GIS / Plano
`GGIS, GIS, GISBAT, GISESCALES, GISIAA, GISMAP, GISMETEO, GISPA, GISPEM, GISPEMDOTZE, GISPEMMMMPP, GISPLAT, GISWEB, GISWINF, GISCSV, SWATR, SWCONC, SWCORE, SWFME, SWGIP, SWPARK, SWPEM, SWPLAN, PEMWEB, PPP, POT, PLAN, PED, SISPEM`

### Aplicaciones Corporativas
`OSPROG, LNVB, PJ, BRAND, CP, CONTMAT, CRM, SALESFORCE, OTC, EDIFIC, FIN, BI, BPM, FND, GDOC, GESDOC, GTT, INT, NPW, WEB, WEB2, ERES, ER, GESPOL, PAQSOFT, SELLIGENT, SMART, SMSZED, SOJA, PVI, RPA`

### Portal ITSM
`APBPIT`

### EMSWe
`EM, EK`

### Roadmap
`RM, TO2025`

### Proyectos de Prueba/Descubrimiento
`ATPD, GTGH, MI, MPDD, PE, PRB, PRUEB, PMDS, PMDSA, SJ, SOSTEST, TD5, TST, TEST, TESTDOS, TESTGD`

---

## 14. Reglas de Comportamiento para Agentes IA

Estas reglas complementan y nunca reemplazan las del framework (`STANDARD_ARCHITECTURE.md`, `POLICY_ARCHITECTURE_BASE.md`).

1. **Priorizar reutilización** sobre desarrollo nuevo — usar framework DOCKS y APIs existentes.
2. **Stack aprobado únicamente** — no recomendar ni generar artefactos en Java, Struts, Oracle, CAS, Alfresco o tecnologías no aprobadas, aunque existan en legacy.
3. **EntraID es el estándar de autenticación** — no sugerir CAS/TGT/LDAP en ningún nuevo componente.
4. **SharePoint/Azure es el estándar de almacenamiento** — no sugerir Alfresco para nuevos desarrollos.
5. **Considerar impacto operativo** — ARGOS y SÒSTRAT son sistemas 24x7 críticos; cualquier cambio requiere análisis de impacto.
6. **Trazabilidad y auditoría** en todos los procesos.
7. **Cumplimiento normativo** — ENS, ISO 27001, RGPD en toda recomendación.
8. **Respetar modelo de contratación pública** — AM → CB → Concreción.
9. **Nomenclatura de repos** — respetar el patrón `APB.API/APP/HST/MSG/LIB.XXX`.
10. **Pipeline obligatorio** — checkout → build → test → sonar → deploy → healthcheck.
11. **Contexto trilingüe** — adaptar al idioma del usuario; respetar nombres catalanes/ingleses de sistemas.
12. **Sin secretos** — no generar ni sugerir tokens, passwords ni credenciales en ningún artefacto.
13. **Legacy es contexto, no prescripción** — el conocimiento de SÒSTRAT, Alfresco y sistemas legacy sirve para entender el negocio e integraciones, nunca para copiar su patrón tecnológico.
14. **Mantenimiento continuo obligatorio** — todo análisis de aplicación/dominio (DDD, arquitectura, testing, threat-model...) que descubra terminología de negocio nueva, corrija un hecho ya documentado aquí, o identifique un sistema/integración no listado, debe proponer la actualización correspondiente de este documento como parte del cierre de esa sesión — no dejarlo solo en el fichero de análisis de origen (`discovery/`). Ver `agents/apb-agent-ddd-v1.0.md` Fase 3 para el paso concreto en el caso DDD.

---

## Historial de Versiones

| Versión | Fecha | Cambio |
|---------|-------|--------|
| 1.0.0 | 2026-06-30 | Creación — consolidación de APB_Knowledge_Base_IA.md v1-v3 (150 proyectos Jira, 520+ repos GitHub, Confluence APLIS, tickets 2023-2026) |
| 1.1.0 | 2026-07-15 | Enriquecida con hallazgos de la descomposición DDD de SÒSTRAT (`discovery/ddd-sostrat-mj8/`, 24 dossiers + auditorías): distinción real PIF vs. SCPP y su candidatura a fusión; hallazgo `Posicionament` sin bounded context; recuento exacto de 90 jobs batch (corrige "~80"); arquitectura real de la mensajería EDI (modelo `MissatgeEdi`/`TipusMissatgeEdi` compartido, parsing de negocio repartido); corrección terminológica VUA (AEAT, nacional) vs. DMS (circuito real de la EMSWe europea); 9 aplicaciones externas con dependencia directa no documentada sobre datos de SÒSTRAT. Añadida regla de mantenimiento continuo (§14.14). |
| 1.2.0 | 2026-07-15 | Segunda pasada, a petición explícita del usuario ("me refería a actualizar conocimiento funcional de negocio, nomenclaturas... qué es una escala, un COARRI, etc."): enriquece el conocimiento **funcional** (no solo arquitectura) de §2 con hallazgos reales de código — Escala (facturación entrelazada, EscalaAspecte, 3 escritores reales), Título/Garantía (corrige "Concesión" como término genérico erróneo), Mercancías (definiciones grounded de COARRI/CODECO/WASDIS/HAZMAT/IFTDGN/Depotsis/PIF-SCPP), nuevas §2.11-2.13 (Servicios al Buque, Operadores Portuarios/Efficiency Network, Transporte Terrestre). Añade ~20 términos nuevos al diccionario §12.1 (Partida, COARRI, CODECO, COPINO, HAZMAT, IFTDGN, IFCSUM, APERAK, Depotsis, Título, Operador Portuario) y corrige 2 entradas existentes (Concesión, Garantia). |
| 1.3.0 | 2026-07-15 | Incorpora el modelo de roles/permisos DOCKS en Entra ID facilitado por Débora (cierre de `PLAN_FASES_FUTURAS.md` #104 / `HANDOFF_TECNICOS.md` DC12): §3.4 pasa de la mera convención de nombre de grupo a documentar la transición CAS/LDAP→EntraID (Permisos→Roles, Roles→Grupos), el catálogo de 7 roles estándar (`APPLICATION_AUDIT`, `FRAMEWORK_ADMINISTRATOR`, `APPLICATION_CLIENT[_EXT]`, `APPLICATION_USER[_EXT]`, `APPLICATION_ADMINISTRATOR`), el rol "Gestor" marcado como pendiente de decisión, el fin de `API_CALL_*` en favor de App Roles entre APIs, y la convención de nomenclatura de roles. Referencias cruzadas añadidas en §3.6, §7.3 y §12.3 (nuevo término App Role). |

---

*Documento generado el 2026-06-30, actualizado el 2026-07-15. Fuentes: APB_Knowledge_Base_IA.md (v1.0), APB_Knowledge_Base_IA_v2.md (v2.0), APB_Knowledge_Base_IA_v3.md (v3.0) — 150 proyectos Jira, 520+ repos GitHub org:portdebarcelona, Confluence APLIS, tickets 2023-2026 — y `discovery/ddd-sostrat-mj8/` (descomposición DDD de SÒSTRAT, Sesión 30, 2026-07-11 a 2026-07-15).*
