---
id: "apb-api-inventory-apim-v1.0"
name: "Inventario de APIs publicadas en Azure API Manager"
description: >-
  Listado completo de aplicaciones DOCKS y sus APIs publicadas en el APIM de APB
  (entorno pre: https://apipre.portdebarcelona.cat). Incluye organización por
  equipo. Fuente de verdad para la Sesión de Análisis de Dominios (#38 Fase 0).
  Los agrupamientos son hipótesis de trabajo — NO son dominios DDD validados.
type: "reference"
source: "Azure API Manager APB + lista de aplicaciones DOCKS (Debora Martin, 2026-06-30)"
last_updated: "2026-06-30"
status: "draft — pendiente análisis DDD"
---

# Inventario de APIs y Aplicaciones DOCKS

> ⚠️ Borrador generado por IA — pendiente de validación por Arquitectura APB.
>
> **Propósito:** este fichero es el **input** para la Sesión de Análisis de Dominios
> (#38 Fase 0). Los agrupamientos son hipótesis inferidas. **NO son dominios DDD validados.**
>
> **Restricción (Debora Martin, 2026-06-30):** los dominios actuales NO están bien
> definidos. Este inventario puede tener solapamientos, repeticiones y novedades.
> El agente de análisis DDD debe detectarlos y proponer la estructura correcta.

---

## 1. Organización por equipo

La estructura de equipos refleja la organización actual — **puede no coincidir con
los dominios DDD correctos**, especialmente en el caso del equipo SOSTRAT, cuyo nombre
replica el sistema legacy pero gestiona APIs DOCKS nuevas.

| Equipo | Descripción | APIs en APIM | Observación DDD |
|--------|-------------|-------------|-----------------|
| **ARQUITECTURA** | Arquitectura DOCKS — servicios horizontales | 36 | Probable dominio Platform (transversal) |
| **SOSTRAT** | APIs relacionadas con el negocio APB | 66 | ⚠️ Nombre de equipo = sistema legacy, pero son APIs DOCKS nuevas. El mayor grupo — muy probable que contenga múltiples bounded contexts mezclados |
| **ADMIN-ELECTRONICA** | Administración Electrónica | 6 | Dominio candidato: Gestión Administrativa / Contratación |
| **INDUSTRIAL** | APIs del ámbito industrial e IoT | 6 | Dominio candidato: Infraestructura Portuaria / IoT |
| **OSMA** | APIs relacionadas con aplicaciones corporativas | 4 | Dominio candidato: Corporativo / RRHH |
| **PLANOLS** | APIs GIS | 0 | Sin APIs en APIM aún — el sistema GIS existe pero no ha publicado APIs |

> **Señal de alerta para DDD:** SOSTRAT con 66 APIs es el doble del segundo grupo más
> grande. Alta probabilidad de que contenga al menos 3–5 bounded contexts distintos
> que están agrupados por herencia organizativa del legacy, no por cohesión de dominio.

---

## 2. Inventario completo de aplicaciones DOCKS y sus APIs

### 2.1 Plataforma y Servicios Horizontales (equipo: ARQUITECTURA)

| Código | Nombre completo | APIs | Función principal |
|--------|----------------|------|-------------------|
| `APBAPI-ApisArquitectura` | APIs de Arquitectura DOCKS | 25 | Servicios base del framework: APPS, AUDIT, AVI, CALENDAR, COUNTRIES, CRYPTO, DOCUMENTS, EMAIL, ENTRADASMENU, EVENT, EVENTTIPUS, FIL, FLC, GRIDCONFIG, ITEM, JERARQUIAS, LANGUAGE, LOG, MENU, NOTIFICATION, PARAM, PERMIS, ROL, USUARIOS, FASES |
| `FLC-FileCloud` | FileCloud | 1 | `APB.API.FLC` — Publicación y gestión de ficheros en SharePoint/cloud |
| `GPS-ExponerDatosDocksPlanol` | Exponer Datos DOCKS en Plano | 1 | `APB.API.GPS` — Consume mensajes `APB.MSG.PSR` de PAD para el plano del puerto |
| `LGC-LogClave` | Log Clave | 1 | `APB.API.LOG` (?) — Logging centralizado clave |
| `GNA-GestionNotificacionesAdviser` | Gestión Notificaciones Adviser | 2 | `APB.API.GNA`, `APB.API.GNS` — Notificaciones vía Adviser |
| `NTA-Notifica` | Notifica | 1 | `APB.API.NTA` — Sistema de notificación (¿diferente de GNA?) |

### 2.2 Operaciones Marítimas — Escalas y Atraques

> **Punto crítico para DDD:** `ESC-Escalas` tiene 4 APIs propias, y además existe
> todo el ecosistema ARGOS (TES, TBE, TMO, etc.) que también gestiona escalas.
> Puede ser que ESC sea el módulo de gestión de escalas de cruceros (CRE) u otro
> sistema paralelo. **Requiere clarificación urgente antes de modelar el dominio.**

| Código | Nombre completo | APIs | Función principal |
|--------|----------------|------|-------------------|
| `ESC-Escalas` | Escalas | 4 | APIs de escalas (¿ARGOS microservicios? ¿CRE? ¿independiente?) |
| `CRE-Cruceros` | Cruceros | 2 | `APB.API.CRE`, `APB.API.CRL` — Gestión de reservas de atraque y planificación de escalas de cruceros |

### 2.3 Gestión de Mercancías y Contenedores

| Código | Nombre completo | APIs | Función principal |
|--------|----------------|------|-------------------|
| `CTA-Contenedores_OLD` | Contenedores (OLD) | 1 | ⚠️ Versión antigua — probablemente `APB.API.CTS` (integración SÒSTRAT). Candidato a deprecar |

> **Nota:** el ecosistema CTA completo (CTA, CTD, CTL, CTP, CTS, CTU, CTA.USC — 7 APIs)
> probablemente pertenece al equipo SOSTRAT y no aparece con nombre propio en la lista
> de aplicaciones. `CTA-Contenedores_OLD` con 1 API es el sistema anterior.

### 2.4 Transporte Terrestre y Ferroviario

| Código | Nombre completo | APIs | Función principal |
|--------|----------------|------|-------------------|
| `FER-GestionDeFerrocarriles` | Gestión de Ferrocarriles | 1 | `APB.API.FER` — Gestión de ferrocarriles portuarios (audiencia `/sos/` — posible integración con emergencias o SOStrat) |
| `TRU-TruckCenter` | Truck Center | 1 | `APB.API.LGP` (audiencia `/tru/`) — Centro de gestión de camiones |
| `PVI-PuertasVirtuales` | Puertas Virtuales | 2 | `APB.API.PVI`, `APB.API.PVD` — Control acceso vehículos en coordinación con PORTIC |

### 2.5 Vehículos (Seguimiento y Daños)

| Código | Nombre completo | APIs | Función principal |
|--------|----------------|------|-------------------|
| `EQV-Vehiculos` | Seguimiento de Vehículos | 5 | `APB.API.EQD`, `APB.API.EQI`, `APB.API.EQL`, `APB.API.EQS`, `APB.API.EQV` — Expedientes de daños, desperfectos e incidencias de vehículos |

### 2.6 Inspección

| Código | Nombre completo | APIs | Función principal |
|--------|----------------|------|-------------------|
| `INS-Escaner` | Escáner | 4 | `APB.API.INS.IPC`, `APB.API.INS.IPR`, `APB.API.INS.SCD`, `APB.API.INS.SOS` — Escaneo de camiones/contenedores |
| `PIF-PuntoInspeccionFisica` | Punto de Inspección Física | 1 | `APB.API.CPR` — Inspección física de mercancías |

> **Posible solapamiento:** INS (escáner de camiones/contenedores) y PIF (inspección
> física) pueden ser el mismo bounded context o contextos adyacentes. A analizar.

### 2.7 Líneas Regulares

| Código | Nombre completo | APIs | Función principal |
|--------|----------------|------|-------------------|
| `LRG-LineasRegulares` | Líneas Regulares | 4 | `APB.API.LRD`, `APB.API.LRG`, `APB.API.LRL`, `APB.API.LRT` — Gestión de líneas navieras regulares (ferry, ro-ro, líneas de contenedor fijas) |

### 2.8 Energía y Suministros

| Código | Nombre completo | APIs | Función principal |
|--------|----------------|------|-------------------|
| `MDE-MuelleDeEnergia` | Muelle de la Energía | 3 | `APB.API.MAD`, `APB.API.MPC`, `APB.API.MSH` — Operaciones con productos inflamables/energéticos |
| `OPS-GestionSuministroElectricidad` | Gestión Suministro Electricidad | 1 | `APB.API.OPS` — Lecturas, consumos, liquidaciones y facturación de electricidad OPS a buques atracados |

> **Relación a aclarar:** OPS (electricidad a buques) y MDE (energéticos/inflamables)
> pueden ser el mismo dominio energético o contextos separados.

### 2.9 Emergencias y Seguridad Industrial

| Código | Nombre completo | APIs | Función principal |
|--------|----------------|------|-------------------|
| `PEM-GestionEmergencias` | Gestión de Emergencias | 4 | `APB.API.BKO`, `APB.API.EME`, `APB.API.MES`, `APB.API.PEL` — Gestión activa de emergencias (sistema que reemplazó GISPEM) |
| `HEM-HistoricoEmergencias` | Histórico de Emergencias | 1 | `APB.API.HEM` — Acceso de solo lectura al histórico de GISPEM (sistema legacy) |

### 2.10 Autorizaciones y Accesos

| Código | Nombre completo | APIs | Función principal |
|--------|----------------|------|-------------------|
| `AUT-Autorizaciones` | Autorizaciones | 1 | `APB.API.AUT` — Gestión y registro de autorizaciones de permisos de acceso por puertas de tránsito/acceso dentro del Puerto de Barcelona |

> **Diferencia clave con PERMIS:** AUT gestiona autorizaciones físicas de acceso al
> recinto portuario (puertas, tránsito). PERMIS gestiona permisos de aplicación DOCKS
> (quién puede hacer qué en cada app). Son bounded contexts distintos.

### 2.11 Facturación y Pagos

| Código | Nombre completo | APIs | Función principal |
|--------|----------------|------|-------------------|
| `P33-TransportesEspeciales` | Transportes Especiales | 2 | `APB.API.L33`, `APB.API.P33` — Facturación módulo 33 (transportes especiales) |
| `P51-GestionPagosT0` | Gestión Pagos T0 | 3 | `APB.API.P51.CNS`, `APB.API.P51.EXP`, `APB.API.P51.L51` — Gestión de pagos en T0 (¿ventanilla única de pagos?) |
| `REB-Recibos` | Recibos | 1 | `APB.API.REB` — Gestión de recibos |
| `RCF-ReclamacionFacturas` | Reclamación de Facturas | 2 | `APB.API.RCF.REC`, `APB.API.RCF.SOS` — Reclamación y gestión de facturas |

> **Dominio candidato: Facturación/Finanzas Portuarias** — P33, P51, REB, RCF son 4
> aplicaciones que probablemente comparten el mismo bounded context de facturación
> y cobro de tasas portuarias, hoy separadas en 4 aplicaciones distintas.

### 2.12 Firma Electrónica y Flujos Documentales

| Código | Nombre completo | APIs | Función principal |
|--------|----------------|------|-------------------|
| `FEL-FirmaElectronica` | Firma Electrónica | 1 | `APB.API.FirmaElectronica` (audiencia `/fel/`) — Firma electrónica interna APB |
| `SIG-SignatureIntegracionViafirma` | Signature Integración Viafirma | 1 | `APB.API.SIG` — Integración con Viafirma (plataforma externa de firma electrónica) |
| `FLU-CircuitosFirmas` | Circuitos de Firmas | 1 | `APB.API.FIL` (?) — Circuitos/flujos de firma |
| `FLU-Flujos` | Flujos | 1 | Flujos de trabajo / aprobaciones |

> **Posible solapamiento:** FEL (firma interna APB) y SIG (Viafirma externo) parecen
> complementarios, no duplicados. FLU puede ser la capa de orquestación de flujos que
> usa ambas firmas. A confirmar si son 1 o 3 bounded contexts.

### 2.13 Administración Electrónica (equipo: ADMIN-ELECTRONICA)

| Código | Nombre completo | APIs | Función principal |
|--------|----------------|------|-------------------|
| `AGE-PortaFirmas` | AGE / Portafirmas | 1 | `APB.API.AGE` (v1,v2,v3) — Integración con Administración General del Estado (Portafirmas, GEISER) |
| `GEISER` | GEISER | 1 | `APB.API.GEI` — Integración GEISER (Plataforma de Gestión de Expedientes del Estado) |
| `PAD-ProcedimientoAdministrativo` | Procedimiento Administrativo | 2 | `APB.API.PSR`, `APB.API.PAL` — Gestión integral de obras, servicios y suministros contratados (LCSP) |

### 2.14 Integración con AEAT (equipo: INDUSTRIAL o OSMA)

| Código | Nombre completo | APIs | Función principal |
|--------|----------------|------|-------------------|
| `MPT-AEATService` | AEATService | 1 | `APB.API.AEATService` — Integración con AEAT (Agencia Estatal Administración Tributaria) |

### 2.15 Aplicaciones Corporativas (equipo: OSMA)

| Código | Nombre completo | APIs | Función principal |
|--------|----------------|------|-------------------|
| `MPS-MutuaPrevisionSocial` | Mutua Previsión Social | 1 | Integración con Mutua de Previsión Social |
| `GPC` | (desconocido) | 1 | `APB.API.GPC` — función desconocida |
| `ROSS` | (desconocido) | 1 | `APB.API.ROSS` — función desconocida |

---

## 3. APIs aún sin aplicación identificada

Las siguientes APIs aparecen en el APIM pero no tienen aplicación asignada en la lista:

| API | Pista de audiencia | Hipótesis |
|-----|--------------------|-----------|
| `APB.API.DGS` | portdebarcelona.cat | Desconocida — ¿DGS = Diagnóstico/Gestión de Sistemas? |
| `APB.API.ESF` | /esf/ | Desconocida |
| `APB.API.ESM` | /esm/ | Desconocida |
| `APB.API.FLO` | portdebarcelona.cat | Desconocida — ¿Flotilla? ¿Flujos Old? |
| `APB.API.IPB` | /ipb/ | Desconocida |
| `APB.API.MPA` | /mpa/ | Desconocida |
| `APB.API.MST` | /mst/ | Desconocida — ¿Maestros? |
| `APB.API.MIGRACION` | portdebarcelona.cat | Migraciones de datos (posiblemente herramienta temporal) |
| `APB.API.RESPONSIBLE` | portdebarcelona.cat | Desconocida |
| `APB.API.ITEM` | portdebarcelona.cat | Desconocida — ¿Ítems de catálogo/maestros? |
| `APB.API.PARAM` | portdebarcelona.cat | Parámetros de configuración (puede ser ARQ/Platform) |
| `APB.API.GPC` | portdebarcelona.cat | Aplicación GPC — función desconocida |

---

## 4. Preguntas DDD abiertas (input para la Sesión de Análisis)

### 4.1 Posibles solapamientos a investigar

| Posible solapamiento | APIs involucradas | Pregunta clave |
|---------------------|------------------|----------------|
| Escalas duplicadas | `ESC-Escalas` (4 APIs) vs. ARGOS `TES/TBE/TMO` | ¿ESC es el nuevo ecosistema DOCKS que reemplaza a ARGOS para escalas, o son contextos complementarios? |
| Cruceros vs. Escalas generales | `CRE` (2 APIs) vs. `ESC` (4 APIs) | ¿CRE gestiona solo cruceros y ESC gestiona todas las escalas, o se solapan? |
| Inspección duplicada | `INS-Escaner` (4 APIs) vs. `PIF-PuntoInspeccionFisica` (1 API) | ¿Son el mismo dominio (inspección de mercancías) con dos canales diferentes, o bounded contexts distintos? |
| Firma electrónica fragmentada | `FEL` (1) + `SIG-Viafirma` (1) + `FLU-CircuitosFirmas` (1) + `FLU-Flujos` (1) | ¿Son 1 dominio "Firma y Aprobaciones" o 4 contextos distintos? |
| Facturación fragmentada | `P33` + `P51` + `REB` + `RCF` | ¿Pertenecen al mismo dominio "Facturación Portuaria" o tienen reglas de negocio suficientemente distintas para ser BCs separados? |
| Energía portuaria | `MDE-MuelleDeEnergia` (3) vs. `OPS-SuministroElectricidad` (1) | ¿Mismo dominio energético o contextos separados (sólidos/líquidos vs. electricidad)? |
| Notificaciones múltiples | `GNA-NotificacionesAdviser` (2) + `NTA-Notifica` (1) + `NOTIFICATION` (ARQ) | ¿3 sistemas de notificación distintos o 1 dominio fragmentado? |
| Accesos y autorizaciones | `AUT-Autorizaciones` (físico) vs. `PERMIS/ROL/USUARIOS` (DOCKS) | Diferencia real confirmada, pero ¿comparten algún aggregate? |

### 4.2 Preguntas sobre el equipo SOSTRAT

El equipo SOSTRAT gestiona 66 APIs pero su nombre replica el sistema legacy (SÒSTRAT Java/Oracle).
Esto genera riesgo de que la organización de APIs refleje la estructura del legacy en vez de
los dominios de negocio correctos.

**Preguntas para la entrevista DDD:**
- ¿Cuáles de las 66 APIs de SOSTRAT pertenecen a dominios que ya tienen su propia aplicación
  DOCKS (p.ej. CTA gestiona contenedores pero CTS está en SOSTRAT)?
- ¿El equipo SOSTRAT tiene previsto crear aplicaciones propias por dominio (como CTA, CRE, EQV)
  o mantener el modelo de un único equipo que gestiona todo el negocio APB?
- ¿ESC-Escalas (4 APIs) pertenece al equipo SOSTRAT? Si es así, ¿es el reemplazante DOCKS
  del módulo de escalas de SÒSTRAT?

### 4.3 APIs sin función conocida (requieren entrevista)

`ROSS`, `GPC`, `DGS`, `ESF`, `ESM`, `FLO`, `IPB`, `MPA`, `MST`, `RESPONSIBLE`

---

## 5. Mapa candidato de dominios DDD (hipótesis de trabajo)

> ⚠️ **Esto es una hipótesis de trabajo, NO una propuesta validada.**
> El agente `apb-agent-ddd-v1.0` y el equipo de Arquitectura APB son quienes validan.

| Dominio candidato | Aplicaciones incluidas | Equipo actual | Confianza |
|-------------------|----------------------|---------------|-----------|
| **Platform / ARQ** | APBAPI-ApisArquitectura, FLC, LGC, GNA, NTA | ARQUITECTURA | Alta |
| **Operaciones Marítimas** | ESC-Escalas, CRE-Cruceros (+ ARGOS) | SOSTRAT | Media — solapamiento ESC/CRE/ARGOS por aclarar |
| **Gestión de Contenedores** | CTA (completo) | SOSTRAT | Alta |
| **Líneas Regulares** | LRG | SOSTRAT | Alta |
| **Vehículos y Transporte Terrestre** | EQV, TRU, PVI, FER | SOSTRAT | Media — FER puede ser dominio propio |
| **Inspección de Mercancías** | INS-Escaner, PIF | SOSTRAT | Media — posible fusión |
| **Acceso al Recinto** | AUT | SOSTRAT | Alta |
| **Emergencias y Seguridad Industrial** | PEM, HEM | SOSTRAT / INDUSTRIAL | Alta |
| **Energía Portuaria** | MDE, OPS | INDUSTRIAL | Media — posible fusión |
| **Facturación y Tasas** | P33, P51, REB, RCF | SOSTRAT | Media — posible fusión en 1 BC |
| **Firma y Aprobaciones** | FEL, SIG, FLU-CircuitosFirmas, FLU-Flujos | ARQUITECTURA / ADMIN | Baja — muy fragmentado |
| **Administración Electrónica** | PAD, AGE, GEISER | ADMIN-ELECTRONICA | Alta |
| **Integración con AEAT** | MPT-AEATService | INDUSTRIAL | Alta |
| **Corporativo / RRHH** | MPS, OSMA apps | OSMA | Media |
| **GIS / Plano del Puerto** | GPS (datos para plano) + PLANOLS (sin APIs) | ARQUITECTURA / PLANOLS | Baja — solo 1 API hoy |
| **Sin clasificar** | ROSS, GPC, DGS, ESF, ESM, FLO, IPB, MPA, MST, RESPONSIBLE | Varios | Nula |

---

## Historial de cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-30 | APB AI Framework | Inventario inicial desde APIM pre (3 APIs) |
| 1.1.0 | 2026-06-30 | APB AI Framework + Debora Martin | Inventario completo: lista de aplicaciones DOCKS + organización por equipos. ~100 APIs, 36 aplicaciones, 6 equipos |
