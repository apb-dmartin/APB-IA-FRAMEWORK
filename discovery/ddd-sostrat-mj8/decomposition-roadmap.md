# Roadmap de Descomposición — SÒSTRAT → DOCKS

> **Borrador generado por IA** (APB AI Framework - apb-arch-decompose-v1.0) — pendiente validación humana. No distribuir sin revisión.

**Base:** `discovery-summary.md` (confirmado por checkpoint humano, 2026-07-11).
**Arquitectura destino:** stack DOCKS (.NET, Azure SQL, EntraID, Service Bus, APIM, SharePoint, Docker/Container Apps, .NET Aspire). El legacy Java/Struts/Oracle/CAS es solo contexto, nunca prescripción.
**Principio rector:** ninguna migración "big bang". Descomposición incremental por strangler fig, con anti-corruption layer (ACL) en cada extracción y BBDD compartida solo como estado transitorio y documentado.

## 1. Matriz de acoplamiento (cualitativa)

> No se ha tenido acceso a SonarQube/NDepend ni a un grafo de dependencias real — esta matriz se basa en imports cruzados, tablas compartidas y escrituras cruzadas observadas por los 8 subagentes de evidencia. **Limitación explícita**: debe confirmarse con un análisis estático automatizado (SonarQube) antes de comprometer fechas de roadmap.

| Contexto | Acoplamiento entrante (quién depende de él) | Acoplamiento saliente (de quién depende) | Nivel |
|---|---|---|---|
| Escalas | Cruceros, Ferrocarril, MARPOL, Aguada (todos referencian `EscalaPk`) | — | **Alto** (hub, muchos downstream) |
| Liquidación | — | Título, Facturación, Escalas, Marinas, Manifiestos, Depotsis, Suministros (13 clases `*Dependencias_Impl`) + escritura directa en `TITOL_MINIM_DADES` | **Muy alto** (hub bidireccional, escrituras cruzadas) |
| Título | Garantías, Liquidación | — | Alto (entrante) |
| Equipament (dato maestro, dueño accidental: MMPP) | Manifiestos, Coarri, Aduanas, Depotsis, Liquidación, Terminales (54 ficheros) | — | **Muy alto** (dato maestro sin contexto propio) |
| Manifiestos | MMPP (`PartidaMmpp` vive en el paquete de manifiestos) | Equipament | Medio-alto |
| Ferrocarril | — | Escalas (`EscalaPk`) | **Bajo** (1 dependencia, ya con ACL parcial vía swagger) |
| Mano de Estiba | — | ninguna detectada | **Bajo** (ya en extracción externa) |
| DEPOTSIS | — | Equipament (lectura) | **Bajo** |
| PPS | — | ninguna detectada (sin acoplamiento a Escala) | **Bajo** |
| MARPOL | — | Escalas (`EscalaPk`) | Medio (grande pero solo 1 dependencia externa) |
| Servicios Auxiliares al Buque (Aguada/Marinas/Pesca) | — | Escalas (solo Aguada) | Bajo-medio |
| Transporte Terrestre | — | ninguna detectada hacia otros dominios de negocio (sí hacia EDI/CBOX) | Medio (tamaño, no acoplamiento) |

**Anti-patrón estructural que afecta a TODOS los contextos**: paquete plano `dataaccess/dto` (~3.700 clases) y `utility` (146 clases con subpaquetes de dominio) — esto no es acoplamiento punto a punto sino ausencia de fronteras físicas en el código. Cualquier extracción requiere primero "recortar" las clases DTO propias de cada bounded context de ese paquete compartido.

## 2. Selección de primeros candidatos de extracción

Criterio: alto valor / bajo acoplamiento / bajo riesgo / momentum ya existente.

1. **Ferrocarril Portuario** — ya tiene un cliente Swagger externo (`OpFerroviariaApi`) consumiendo parte de la funcionalidad; acoplamiento mínimo (solo `EscalaPk`); equipo ya familiarizado con el patrón de extracción. **Quick win #1.**
2. **Mano de Estiba** — ya existe un microservicio externo referenciado ("MST" vía `ticketgranting-api-client`); sin acoplamiento detectado a otros dominios de negocio. **Quick win #2.**
3. **DEPOTSIS** — struts-config propio, el más aislado del clúster de Mercancías; único acoplamiento es lectura del futuro servicio de datos maestros de Equipamiento.

## 3. Estrategia de desacoplamiento por fase

### Fase 0 — Fundamentos transversales (prerequisito, no extrae nada todavía)

- **Anti-corruption layer / fachada API** sobre APIM sobre los endpoints SOAP existentes de `sostratWSCXF` (ya es el módulo mejor aislado — buen punto de apoyo).
- **Servicio de datos maestros de Equipamiento (contenedores)**: extraer `Equipament` de MMPP como contexto de datos maestros compartido (patrón *published language*), consumido por Manifiestos, Coarri, Aduanas, Depotsis, Liquidación y Terminales vía API en lugar de acceso directo a tabla.
- **Consolidación interna de "Aduanas/Control de Contenedores"**: unificar la lógica hoy repartida entre `aduanas` y `terminales` antes de poder extraerla como bounded context limpio.
- **Réplica de lectura Oracle → Azure SQL (CDC)** para los primeros servicios extraídos, evitando reescritura de todo el modelo de datos de golpe.
- **EntraID en paralelo a CAS**: dado que la infraestructura de auth ya vive fuera del monolito (`sostrat-core` externo) y existe `ticketgranting-api-client` (USR/GRP/MNU/ADT), evaluar si puede mapearse directamente sobre `APB.API.USUARIOS`/`APB.API.ROL`/`APB.API.PERMIS` ya existentes en DOCKS — este subdominio genérico podría requerir mucho menos esfuerzo del habitual.
- **Notificaciones (SMS/Email)**: sustitución casi directa de `SmsWSPort` por `APB.API.SMS`/`APB.API.EMAIL` — sin lógica de dominio propia, bajo riesgo, puede hacerse en paralelo a la Fase 0.

### Fase 1 — Quick wins (bajo acoplamiento, bajo riesgo)

- Extraer **Ferrocarril Portuario** a microservicio .NET en Container Apps. ACL: traducir `EscalaPk` legacy al identificador de escala del nuevo modelo objetivo.
- Extraer **Mano de Estiba**, formalizando el servicio "MST" ya iniciado como microservicio DOCKS completo.
- Extraer **DEPOTSIS**, consumiendo el servicio de datos maestros de Equipamiento de la Fase 0.
- Migrar **Notificaciones** a `APB.API.SMS`/`APB.API.EMAIL`.

### Fase 2 — Dominios supporting de tamaño medio

- **PPS** (Pases y Permisos) — sin acoplamiento a Escala, extracción relativamente limpia.
- **MARPOL/Residuos** — grande pero autocontenido (solo depende de Escala); extraer con ACL hacia Escalas.
- **Servicios Auxiliares al Buque** (Aguada + Marinas + Pesca) como un único microservicio agrupado — evita el sobrecoste operativo (N pipelines/monitores) de 3 servicios diminutos.
- **Transporte Terrestre** — requiere primero descomponer internamente su sub-contexto `parquing/` antes de extraer el conjunto.

### Fase 3 — Núcleo de Mercancías y Aduanas (alto valor, acoplamiento medio-alto)

- Refactor interno (strangler fig *dentro* del monolito) de las god classes `CN_Manifest_Impl` (3.929 líneas) y `CN_Partida_Impl` (3.338 líneas) en `Manifiestos` antes de exponerlo como servicio — extraer sin este paso arrastraría la complejidad interna al nuevo microservicio.
- Extraer **MMPP** y **PIF** apoyándose en el servicio de datos maestros de Equipamiento ya disponible (Fase 0).
- Extraer **Manifiestos** ya refactorizado.
- Extraer **Aduanas/Control de Contenedores** (ya consolidado en Fase 0).

### Fase 4 — Concesiones y Facturación (máximo riesgo, se aborda al final)

- Es el clúster más acoplado del sistema (Liquidación escribe directamente en tablas de Título; Facturación comparte utilidades base con Liquidación).
- **Paso previo obligatorio, ahora aún más crítico**: sustituir las escrituras cruzadas directas por eventos de dominio (`TituloActualizado`, `LiquidacionGenerada` vía Service Bus) antes de cualquier extracción física. Al separarse en dos servicios distintos (ver decisión abajo), esto deja de ser una mejora arquitectónica opcional y pasa a ser un **requisito duro**: sin este desacoplamiento, Título y Liquidación no pueden vivir en bases de datos/despliegues distintos sin romper la consistencia transaccional actual.
- **DECISIÓN CONFIRMADA (2026-07-11, revisada tras reparentar contra el catálogo real de dominios de APB)**: Título y Garantías se despliegan como el servicio **Concesiones** (mapea a `dom-concesiones-v1`, ya existente en `apb-domain-catalog` — CONCB/GESGAR). Liquidación y Facturación se despliegan como el servicio **Facturación y Liquidaciones** (mapea a `dom-facturacion-v1`, ya existente, de alcance todo el puerto — T0-T5, P33, REB, ODP, no solo SÒSTRAT). **Se revierte la decisión anterior de unificar los 4 en un único servicio** — el catálogo de dominios de negocio de APB ya trataba Concesiones y Facturación como capacidades distintas antes de este análisis, con dueños y ciclos de vida propios; forzar un servicio único habría contradicho ese modelo ya validado por Arquitectura APB.
- Garantías se extrae junto con Título en el servicio Concesiones, dado que no tiene identidad de agregado propia (depende de `IDTITOL`).
- Con esta decisión, el total de servicios backend nuevos del roadmap es **16** (14 de siempre + Concesiones + Facturación y Liquidaciones como servicios separados) — ver recuento completo en `ui-screens-backlog.md`.
- **Secuenciación interna de la Fase 4**: extraer primero Concesiones (menor acoplamiento saliente — solo Garantías depende de Título) y, solo cuando el evento `TituloActualizado` esté maduro y consumido en producción, extraer Facturación y Liquidaciones (que consume ese evento en lugar de escribir directamente en las tablas de Título).

### Fase 5 — Escalas: NO es una extracción, es una migración/retirada hacia ARGOS (revisado 2026-07-11)

> **Cambio de naturaleza confirmado por evidencia de código, pendiente de validación final con el equipo de ARGOS (AOM) antes de ejecutar**: esta fase deja de ser "extraer Escalas como microservicio DOCKS nuevo" y pasa a ser "migrar la maestría del dato de escala desde SÒSTRAT hacia ARGOS, que ya es su consumidor operativo en producción".

- **Evidencia**: `dom-operaciones-maritimas-v1` (ya existente en `apb-domain-catalog`) es operado por ARGOS, con el microservicio `APB.API.TES` (`MS_PORTCALL`) ya en producción. Su código real (`APB.API.TES/src/Consumer/Dto/PortCallCreatedDto.cs`) tiene un DTO con `Origin = SOSTRAT` por defecto y campos idénticos al modelo de SÒSTRAT (`IdSubPort`, `YearPortCall`, `NumPortCall`, `Aspecte` — terminología catalana literal de la tabla `ESCALA_ASPECTE`). El consumer `TesPortCallCreatedConsumer.cs` procesa el evento real `MSG0004 PortcallUpdated` (dirección confirmada: **SÒSTRAT → TES**), y `TesBerthUpdatedConsumer.cs` hace lo mismo con atraques (`MSG0017 BerthUpdated`). Es decir: **ARGOS ya recibe y aplica en su propio modelo los datos de escala/atraque que SÒSTRAT sigue escribiendo hoy** — no son dos sistemas complementarios, es la misma capacidad de negocio en transición.
- **Matiz importante**: no todo lo que hoy vive en `service/escalas/` de SÒSTRAT es "Operaciones Marítimas". La god class `EscalaAction.java` mezcla la escala en sí con lógica de liquidación/facturación (81 referencias a `Liquidacion`/`Facturacio` encontradas en el fichero) y con residuos MARPOL (`CN_EnvioMarpolEscala.java`) — la propuesta `bc-escalas-v1.md` afirmaba una separación limpia ("no incluye facturación ni liquidación") que **no coincide con el código real**; corregir esa nota antes de usarla como base de diseño.
- **Acción revisada para esta fase**:
  1. Separar primero la lógica de liquidación/facturación entrelazada en `EscalaAction.java` hacia el servicio de Facturación y Liquidaciones (Fase 4) — no puede migrarse a ARGOS junto con la escala, porque ARGOS no es un sistema de facturación.
  2. Diseñar la migración de maestría del dato de escala/atraque hacia `APB.API.TES`/`APB.API.TBE` (invertir o retirar progresivamente el flujo `SOSTRAT→TES` una vez ARGOS pueda escribir su propio dato), en vez de construir un tercer sistema.
  3. Cruceros (hoy `bc-cruceros-v1`, ya reparentado a `dom-cruceros-v1`) y Ferrocarril, MARPOL y Aguada mantienen sus ACL ya diseñados en fases previas, pero apuntando a ARGOS/TES como destino final en vez de a un hipotético servicio "Escalas" nuevo.
  4. **Escalar explícitamente este hallazgo al equipo de ARGOS (AOM: Alberto Ponseti, Jose Joaquin Mena — ver `APB_KNOWLEDGE_BASE.md`) antes de tocar código** — esto no se ejecuta solo con el equipo de SÒSTRAT.
- **Impacto en el recuento de aplicaciones**: al dejar de ser una extracción a servicio nuevo, el total de aplicaciones backend del roadmap baja de 16 a **15** (ver `ui-screens-backlog.md`).

## 4. Diseño de datos

- Oracle compartido es el bloqueador estructural principal. Estrategia: **CDC (Change Data Capture) desde Oracle hacia Azure SQL** para cada servicio extraído, manteniendo Oracle como fuente de verdad durante la transición de cada dominio, con corte de escritura (cutover) al final de cada fase — nunca antes.
- BBDD compartida se acepta **solo como estado transitorio** por dominio, con fecha de fin de fase documentada en el ADR correspondiente.
- El dato maestro de Equipamiento se modela desde el principio como servicio propio para evitar que cada extracción posterior tenga que resolver su propia copia.

## 5. Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Matriz de acoplamiento es cualitativa, no confirmada por herramienta automatizada | Ejecutar SonarQube (o equivalente) sobre `sostrat/` antes de comprometer fechas de Fase 2 en adelante |
| SÒSTRAT es sistema 24x7 crítico (criticidad "Muy Alta" en KB) | Ninguna fase implica apagar funcionalidad existente; ACL + strangler fig en todas las extracciones |
| Núcleo financiero (Fase 4) tiene escrituras cruzadas de dominio | No extraer sin sustituir antes las escrituras directas por eventos de dominio |
| Coste operativo de N microservicios pequeños | Fase 2 agrupa explícitamente Aguada+Marinas+Pesca en un único servicio en vez de 3 |
| Dato maestro Equipamiento sin dueño de negocio confirmado | Punto abierto en discovery-summary.md §5 — bloquea el diseño final del servicio de datos maestros hasta validación |

## 6. Estimación de esfuerzo por fase (orden de magnitud, pendiente de validar con los equipos)

| Fase | Alcance | Esfuerzo relativo |
|---|---|---|
| Fase 0 | Fundamentos (ACL, datos maestros, CDC, auth) | Alto (una vez, habilita todo lo demás) |
| Fase 1 | Ferrocarril, Mano de Estiba, Depotsis, Notificaciones | Bajo — quick wins |
| Fase 2 | PPS, MARPOL, Servicios Auxiliares, Transporte Terrestre | Medio |
| Fase 3 | Manifiestos (+ refactor interno), MMPP, PIF, Aduanas | Alto |
| Fase 4 | Título, Liquidación, Facturación, Garantías | Muy alto — mayor riesgo del roadmap |
| Fase 5 | Escalas | Alto (hub central, pero contratos ya maduros) |

**Métrica de éxito por fase**: time-to-deploy del microservicio extraído &lt; 15 minutos (criterio estándar de `apb-arch-decompose-v1.0`); cero incidentes de disponibilidad en el monolito durante y después de cada extracción.
