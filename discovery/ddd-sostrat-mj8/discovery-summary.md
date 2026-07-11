# Discovery Summary — SÒSTRAT (SOSTRAT-Sostrat-MJ8)

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0 / apb-disc-ddd-legacy-v1.0) — pendiente validación humana. No distribuir sin revisión.

**Sistema analizado:** SÒSTRAT — Sistema Central de Gestión de Servicios Portuarios (legacy Java/Struts1/Spring/Oracle)
**Repositorio:** `portdebarcelona/SOSTRAT-Sostrat-MJ8` (copia local sin historial git, analizada en `GitHub-Repos\otros\SOSTRAT-Sostrat-MJ8\`)
**Fuentes analizadas:** código fuente (8 subagentes `apb-sub-ddd-code`/`apb-sub-ddd-spec` en paralelo), estructural/representativo — **no** lectura exhaustiva de los ~13.240 ficheros .java
**Fecha:** 2026-07-11
**Equipo:** Arquitectura APB
**Alcance:** `sostrat/` (app principal), `sostrat-BATCH/`, `sostratWSCXF/`, `sostrat-CARGASINICIALES/`

## Método

Se ha contrastado la hipótesis de partida de `APB_KNOWLEDGE_BASE.md §4.3` (agrupación de módulos por proyecto Jira) contra evidencia real de código: paquetes, clases, tablas, Struts action-mappings, WSDL y jobs batch. La hipótesis Jira queda **confirmada en unos casos, corregida en otros** — ver notas de contradicción por dominio.

---

## 1. Mapa de Dominios de Negocio y Bounded Contexts propuestos

> ⚠️ **CORRECCIÓN 2026-07-11**: los 6 nombres de dominio de esta sección (§1) fueron **inventados** en la primera pasada de este análisis, sin comprobar que `apb-domain-catalog` ya tenía 21 dominios de negocio reales en estado `proposed` (el submodule local estaba desactualizado — ver `catalog-comparison.md` y `session-retro-2026-07-11.md`). Los 21 bounded contexts identificados en esta sección **siguen siendo válidos como evidencia de código**, pero ya **no cuelgan de estos 6 dominios** — se han reparentado a los dominios reales del catálogo. La tabla de mapeo definitiva está en `catalog-comparison.md` §"Recomendación de proceso" y en `pr-instructions.md` §2. En particular: el núcleo financiero (antes "Facturación y Liquidaciones") se separó en dos dominios reales distintos, **Concesiones** (Título+Garantías) y **Facturación** (Liquidación+Facturación) — ver `decomposition-roadmap.md` Fase 4.

### Dominio: Gestión de Escalas y Tráfico Marítimo (`core`) — nombre de trabajo, ver corrección arriba

| Bounded Context | Evidencia | Notas |
|---|---|---|
| **Escalas** (buque/atraque) | `service/escalas/` (67 interfaces `CN_*`), `dataaccess/dto/escalas/Escala.java` (tabla `ESCALA`), `Atracada.java` (tabla `ATRACADA`) | Hub grande y heterogéneo: orquesta también residuos, cruceros, notificaciones EDI. God class `EscalaAction.java` (7.549 líneas). Sub-contexto candidato: gestión documental/EDI (`escalas/dms/`). |
| **Cruceros** | `dataaccess/dto/cruceros/CreuerEscalaAudit.java`, servicio SOAP `CrucerosWSPort` | Ya semi-diferenciado en el código; dependiente de Escalas. |
| **Ferrocarril Portuario** | `service/ferrocarril/` (34 interfaces), tabla implícita vía `EscalaPk` | **Ya parcialmente externalizado**: `swagger/fer/client/api/OpFerroviariaApi.java` consume un microservicio externo de trenes/cámaras — candidato natural a primera extracción (quick win, ya en curso). |

### Dominio: Facturación y Liquidaciones (`core`)

| Bounded Context | Evidencia | Notas |
|---|---|---|
| **Título** (antes hipótesis "CONCB"/Concesiones) | `service/impl/CN_Titol_Impl.java` (1.888 líneas), `service/titolminim/`, `service/documentconcessions/`, `service/plaespecial/` | **Corrige la hipótesis**: el paquete `service/concesiones/` está casi vacío; el dominio real y su ubiquitous language es "Titol" (título de ocupación/actividad portuaria), no "Concesión". |
| **Liquidación** | `service/liquidacion/` (28 clases), `CN_Liquidacion_Impl.java` (2.057 líneas), `CN_LiqLC_Impl.java` (+3.600 líneas) | Actúa como **hub transversal**: 13 clases `*Dependencias_Impl` que escriben en Escalas, Marina, Manifest, Depotsis, Suministros y Título. Escritura cruzada directa detectada (`UPDATE TITOL_MINIM_DADES` desde el servicio de Liquidación). Requiere tratamiento especial en la estrategia de descomposición (no se puede aislar limpiamente sin antes desacoplar sus escrituras cruzadas). |
| **Facturación** (FACT + FACTSTD) | `service/facturas/` (23 clases + ~90 de Facturae/firma XML), `service/factestandar/` con subdominios `rebuts`, `peticiofbd`, `suministros`, `vehiclesAbandonats`, `marinas` | God class `CN_Facturas_Impl.java` (2.111 líneas). Acoplada a Liquidación vía `LiquidacionGenericDependenciasUtil`. |
| **Garantías** (GESGAR) | `service/gestiogaranties/` (`CN_Garantias_Impl.java`, 811 líneas) | **No es agregado independiente**: importa `TitolDades`/`TitolPk` directamente y filtra por `IDTITOL` — es un sub-concepto dependiente de Título, no un bounded context autónomo. |

### Dominio: Mercancías y Aduanas (`core`)

| Bounded Context | Evidencia | Notas |
|---|---|---|
| **Manifiestos** (antes hipótesis "MERC/MERCA/MERCB") | `service/manifiestos/gestion/` — `CN_Manifest_Impl.java` (3.929 líneas), `CN_Partida_Impl.java` (3.338 líneas), `PartidaVersio.java` (tabla `PARTIDA_VERSIO`) | **Corrige la hipótesis**: no existe paquete "merc"; el nombre real es "manifiestos". Las mayores god classes de todo el sistema. |
| **MMPP** (Mercancías Peligrosas) | `service/mmpp/{gestion,hazmat,inspecciones,maestros,edi}`, `MmppAutoritzacio.java` (tabla `MMPP_AUTORITZACIO`), `MmppNotif.java` (tabla `MMPP_NOTIF`) | Contexto sólido y autocontenido, con EDI propio. Confirma hipótesis. |
| **PIF** (control fronterizo/SCPP) | `service/pif/` (`CN_Pif.java`, `CN_AreaPif.java`, `CN_OperacioPif.java`) | Confirma hipótesis, naturaleza regulatoria distinta de MMPP. |
| **DEPOTSIS** | `service/depotsis/`, `struts-config-depotsis.xml` propio | El más aislado del clúster — buen candidato a extracción temprana. |
| **Aduanas / Control de Contenedores** (antes hipótesis "CTA") | `service/aduanas/` (`CN_ConsultaContenedor`, `CN_TrasllatContenidor`, `CN_TransitContenidor`), `service/terminales/` | **Corrige la hipótesis**: "CTA" no existe como paquete propio; la funcionalidad está repartida entre `aduanas` y `terminales`. Requiere consolidación antes de poder extraerse como BC limpio. |
| — dato maestro compartido | `Equipament.java` (tabla `EQUIPAMENT`), físicamente en `mmpp/maestros` pero consumido por Manifiestos, Coarri, Aduanas, Depotsis, Liquidación y Terminales (54 ficheros) | **Anti-patrón transversal**: MMPP es "dueño accidental" de un maestro de contenedores usado por 6 dominios — candidato a contexto de datos maestros compartido (published language) en el modelo objetivo. |

### Dominio: Servicios Auxiliares al Buque (`supporting`)

| Bounded Context | Evidencia | Notas |
|---|---|---|
| **MARPOL / Residuos** (también cubre la hipótesis "MEDI") | `service/marpol/` (114 clases: wasdis, pesatges, contenidor, camio, codisqr) | El más maduro y grande de este clúster — se mantiene como BC propio, no se agrupa con los pequeños. La hipótesis "MEDI" apuntaba en realidad a este mismo dominio. |
| **Servicios Auxiliares al Buque** (agrupación propuesta) | Aguada (`service/aguada/`), Marinas/MARDEP (`service/factestandar/marinas/`), Pesca (`service/gpesca/`) | Los 3 comparten patrón arquitectónico, tamaño pequeño y ausencia de lógica de dominio profunda — cohesión suficiente para agruparlos en un único BC genérico. |
| — | **BUNKER no encontrado en el código** (búsqueda exhaustiva sin resultados) | Contradice la hipótesis Jira — pendiente de confirmar con negocio si vive en otro sistema o si ya no está operativo. |

### Dominio: Transporte Terrestre y Accesos (`supporting`)

| Bounded Context | Evidencia | Notas |
|---|---|---|
| **Transporte Terrestre** (TRANSTE) | `service/transporteterrestre/` — Preavisos, Autorizaciones, RPI, Parquing, Transportistas, Vehículos, Conductores, CODECO/EDI | Segundo módulo más grande tras MARPOL; con sub-bounded-contexts propios (`parquing/`). |
| **PPS** (Pases y Permisos) | `service/pps/` (`CN_Solicituds_Impl.java`, 2.200 líneas), tabla `SOLICITUD` | Sin acoplamiento a Escala — gira en torno a persona/vehículo/tarjeta. God class en la Action (`TarjetasPasesAction.java`, 2.647 líneas). |
| **Mano de Estiba** (MANEST) | `service/manoEstiba/`, ~20 DTOs | **Ya en proceso de extracción**: existe un microservicio externo "MST" referenciado desde `ticketgranting-api-client` — señal de strangler fig ya en marcha para este dominio. |

### Subdominios genéricos / infraestructura (`generic`)

| Componente | Evidencia | Clasificación |
|---|---|---|
| Clavegueram (CLAVEG) | `service/clavegueram/` (6 clases, tabla `CLVG_CONSUMS`) | Generic — facturación de un servicio municipal (alcantarillado), reutilizable/externalizable. |
| Autenticación / SSO | `applicationContext-ldap.xml`, `applicationContext-core-spring-security.xml`, `ticketgranting-api-client/` | La infraestructura de auth real (`org.apb.sostrat.core.*`) **no está en este checkout** — vive en una librería compartida externa. `ticketgranting-api-client` expone ya microservicios de plataforma (USR, GRP, MNU, ADT) que mapean directamente a las APIs DOCKS existentes (`APB.API.USUARIOS`, `APB.API.ROL`, `APB.API.PERMIS`) — **buena noticia**: gran parte de este subdominio ya está resuelto en la arquitectura destino. |
| Notificaciones (SMS/Email) | `sostratWSCXF` → `SmsWSPort`/`SmsWSSecurePort` | Transversal, candidato a mapear directamente sobre `APB.API.SMS`/`APB.API.EMAIL`. |
| Carga Inicial (ETL) | `sostrat-CARGASINICIALES/` | Utilitario de migración AS400→SÒSTRAT, no es un dominio de negocio. Confirma acoplamiento de BBDD compartida entre Título, Manifiestos, MMPP, Facturación y Accesos (todos alimentados desde el mismo proceso). |
| EST (estadísticas) | Sin paquete propio — códigos de clasificación Intrastat/NSTR dispersos en `dataaccess/dto/`, más `CN_EstadistiquesTerminals` como capacidad interna de `terminales` | **Refuta la hipótesis**: no es un dominio autónomo. |
| MILL, INTDBPRO | Sin evidencia en ningún módulo del repositorio | Pendiente confirmar con negocio si pertenecen a otro sistema del inventario APB. |

### Integración / mensajería (cross-cutting, no es un dominio de negocio)

- **sostratWSCXF** (21 servicios SOAP): expone Escalas/Cruceros, MMPP, Notificaciones y Autenticación; integración externa confirmada con la naviera **Grimaldi** (manifiestos) y mensajería **ARTEMIS/JMS** para traslados de contenedores. No se ha encontrado integración directa con GEISER/PORTIC/VTS en este módulo concreto (puede vivir en otro módulo no analizado).
- **sostrat-BATCH** (~85 jobs SpringBatch): circuitos EDI confirmados — COARRI, CODECO, MMPP (notificación/lista de carga), MARPOL (residuos), Manifiestos, Facturación EDI, DUA/VUA (aduanas), Conciliación de terminales. La hipótesis inicial (BERMAN, WASDIS, GEISER/FACE) **no se confirma** en este módulo — WASDIS es un subcircuito de MARPOL, no un job independiente; BERMAN y GEISER/FACE no se encontraron.

---

## 2. Anti-patrones transversales (condicionan la estrategia de descomposición)

1. **BBDD compartida de facto a nivel de código**: paquete único `dataaccess/dto/` con ~3.700 clases de *todos* los dominios sin separación por bounded context — "big ball of mud" en la capa de datos.
2. **Paquete `utility` (146 clases) como cajón de sastre**: mezcla helpers genéricos con subpaquetes de dominio (`utility/marpol`, `utility/clavegueram`, `utility/mmpp`, `utility/edi`) — acoplamiento estructural que atraviesa toda la aplicación.
3. **God classes sistemáticas**: `EscalaAction` (7.549 líneas), `CN_Manifest_Impl` (3.929), `CN_LiqLC_Impl` (+3.600), `TarjetasPasesAction` (2.647), `CN_Solicituds_Impl` (2.200), `CN_Facturas_Impl` (2.111), `CN_Liquidacion_Impl` (2.057), `CN_Titol_Impl` (1.888), `RegistroSuministroAction` (1.882).
4. **Lógica de negocio embebida en Struts Actions** en lugar de en la capa de servicio — patrón repetido en casi todos los dominios.
5. **Dato maestro compartido sin dueño claro**: `Equipament` (contenedor) consumido por 6 dominios distintos.
6. **Escrituras cruzadas de dominio**: Liquidación actualiza tablas de Título directamente.
7. **Jobs batch que cruzan 3 dominios en una sola transacción** (p.ej. `EnvioAutorizacionTransportistasTasklet`).
8. **Carga inicial (ETL) que confirma el acoplamiento de BBDD compartida** entre 5 dominios desde un único proceso.

## 3. Señales positivas (descomposición ya en marcha, orgánicamente)

- **Ferrocarril** ya delega en un microservicio externo (cliente Swagger `OpFerroviariaApi`).
- **Mano de Estiba** ya tiene un microservicio externo referenciado ("MST").
- **Autenticación/SSO** ya vive fuera del monolito (librería `sostrat-core` no incluida en este checkout) y hay evidencia de una API de plataforma (`ticketgranting-api-client`) que mapea a las APIs DOCKS existentes.
- **sostratWSCXF** es, de los 4 módulos, el mejor estructurado (Maven estándar, capa de integración ya aislada del resto del monolito).

## 4. Clasificación estratégica propuesta

| Clasificación | Dominios |
|---|---|
| **Core** | Escalas y Tráfico Marítimo, Facturación y Liquidaciones, Mercancías y Aduanas |
| **Supporting** | Servicios Auxiliares al Buque, Transporte Terrestre y Accesos, Mano de Estiba (en migración) |
| **Generic** | Clavegueram, Notificaciones, Autenticación/SSO (ya externalizado), Carga Inicial/ETL |

*(Garantías, Título y Liquidación se documentan bajo Facturación y Liquidaciones por su fuerte interdependencia; podrían proponerse como bounded contexts separados dentro de ese dominio en la propuesta formal, sujeto a validación humana.)*

## 5. Puntos abiertos para validación humana (checkpoint)

- Confirmar con Arquitectura APB / domain experts si BUNKER, MILL e INTDBPRO son dominios activos fuera de este repositorio o etiquetas Jira obsoletas.
- ~~Decidir si "Título", "Liquidación" y "Facturación" se modelan como 3 bounded contexts separados o como 1 dominio con 3 sub-agregados fuertemente acoplados~~ — **RESUELTO 2026-07-11**: el usuario ha decidido desplegar Título + Liquidación + Facturación + Garantías como **un único servicio** ("núcleo financiero unificado"). Los 4 siguen siendo bounded contexts DDD distintos a nivel de modelo (ver `proposals/bc-titulo-v1.md`, `bc-liquidacion-v1.md`, `bc-facturacion-v1.md`, `bc-garantias-v1.md`), pero se co-despliegan como un monolito modular — un único pipeline/base de datos/ciclo de vida, con separación interna de módulos por bounded context. Ver `decomposition-roadmap.md` Fase 4 y `adr-sostrat-decomposition-strategy.md` actualizados.
- Validar si "Aduanas/Control de Contenedores" (antes CTA) debe consolidarse primero en el propio monolito antes de proponerse como bounded context candidato a extracción.
- Confirmar el dueño de negocio del dato maestro `Equipament` (contenedor) de cara al modelo de datos maestros compartidos.

## 6. Arquitectura de presentación (decidido 2026-07-11)

El usuario ha confirmado el modelo de frontend: **cada uno de los servicios backend extraídos (15 en total, tras unificar el núcleo financiero) tiene su propio frontend independiente** — cuenta como aplicación propia en el catálogo DOCKS, con su propio ciclo de vida y despliegue — **pero todos se integran visualmente en un portal operativo único** de cara al usuario final. Es decir: independencia de despliegue a nivel de arquitectura, unificación solo a nivel de presentación/UX (navegación, shell común, SSO único). Ver `ui-screens-backlog.md` §"Portal Operativo" para el detalle.
