---
id: "prov-apb-knowledge-base-v1.0"
name: "APB Knowledge Base — Contexto Corporativo"
description: >
  Base de conocimiento consolidada de la Autoritat Portuària de Barcelona.
  Proporciona a los agentes IA el contexto de negocio, funcional y tecnológico
  (incluyendo sistemas legacy) necesario para dar respuestas de calidad.
  NO modifica los estándares DOCKS ni las políticas tecnológicas aprobadas:
  el legacy se documenta como contexto, nunca como patrón a seguir en desarrollos nuevos.
version: "1.0.0"
status: "approved"
owner: "Debora Martin <deboramv@gmail.com>"
domain: "knowledge"
provider_type: "knowledge"
access_mode: "read-only"
created_date: "2026-06-30"
review_date: "2026-06-30"
sources:
  - "APB_Knowledge_Base_IA.md (v1.0)"
  - "APB_Knowledge_Base_IA_v2.md (v2.0)"
  - "APB_Knowledge_Base_IA_v3.md (v3.0)"
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
Es el concepto central del negocio portuario.

**Identificadores:**

| Campo | Descripción |
|-------|-------------|
| YearPortCall | Año de la escala |
| NumPortCall | Número secuencial de escala |
| IdSubPort | Subpuerto (generalmente "B" = Barcelona) |
| Aspecto | R = Real, S = Solicitado |

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

### 2.4. Concesiones y Ocupaciones

Las **concesiones** son títulos que otorgan derecho de uso de terreno portuario.

| Campo | Descripción |
|-------|-------------|
| IDTITOL | Identificador del título |
| Tipo | Concesión, Autorización, Licencia, Evento |
| Ocupació | Parcela con perímetro georreferenciado |
| Zona portuaria / zona de valor | Clasificación del espacio |
| Vigencia / caducidad / renovación | Fechas de validez del título |

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

- **Manifiestos**: declaración de carga del buque (0811 = descarga, 0812 = carga).
- **Declaraciones sumarias (CUSCAR)**: información anticipada para Aduana.
- **Mercancías Peligrosas (MMPP/ADR/IMO)**: gestión especial con requisitos de seguridad.
- **SCPP**: Servicio de Control y Posicionamiento de Contenedores para inspección aduanera.
- **PIF**: Punto de Inspección Fronterizo (control sanitario).
- **Gate-in / Gate-out**: entrada/salida de contenedores de terminal (mensajes CODECO).

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

### 3.4. Convención de Grupos de Permisos

Formato: `GRP_{ENTORNO}_{APP}_{ROL}`
Ejemplo: `GRP_PRO_ARG_TWO` (Producción, ARGOS, Tower Operator)

### 3.5. Entornos

| Entorno | Uso |
|---------|-----|
| DEV / DES | Desarrollo |
| PRE | Preproducción / pruebas |
| PRO | Producción |

### 3.6. Migración EntraID

- AuthScheme: `TGT` → `EntraIdOrTGT` → `EntraID`
- Permisos: roles en App Registration de Entra ID.
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
| PIF | SCPP — posicionamiento contenedores inspección aduanera |
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

**Procesos batch especiales (SpringBatch):** ~80 tareas. Circuitos principales: BERMAN, WASDIS, COARRI/CODECO, GEISER/FACE, Notifica, TarifasResidus, Conciliación terrestre.

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
| Aplicaciones DOCKS (Cloud) | Microsoft Entra ID + grupos APIM |
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
| Conocimiento (B/L) | Bill of Lading — documento de embarque |
| DUA | Documento Único Administrativo (aduanas) |
| Gate-in / Gate-out | Entrada/salida de contenedores de terminal |
| Contenedor | Unidad estándar de transporte (TEU = 20 pies, FEU = 40 pies) |
| Precinto | Sello de seguridad en contenedores |
| SCPP | Servicio de Control y Posicionamiento de Contenedores |
| PIF | Puesto de Inspección Fronteriza |
| Preavis | Aviso previo de transporte terrestre |
| ISPS | International Ship and Port Facility Security Code |
| Liquidació | Cálculo de la tasa portuaria aplicable |
| Baremo | Tabla de precios aplicable (BE1 = fijo, BE2 = variable) |
| Sujeto pasivo | Quién paga la tasa (consignatario o terminal) |
| Concesión | Derecho de uso de espacio portuario |
| Garantia | Aval financiero asociado a una concesión |
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
| App Registration | Registro de aplicación en Microsoft Entra ID |
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

---

*Documento generado el 2026-06-30. Fuentes: APB_Knowledge_Base_IA.md (v1.0), APB_Knowledge_Base_IA_v2.md (v2.0), APB_Knowledge_Base_IA_v3.md (v3.0) — 150 proyectos Jira, 520+ repos GitHub org:portdebarcelona, Confluence APLIS, tickets 2023-2026.*
