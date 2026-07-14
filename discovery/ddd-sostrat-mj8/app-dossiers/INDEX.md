# [IA-GEN] Índice consolidado — Dossiers de aplicación final SÒSTRAT

> **Borrador generado por IA** (APB AI Framework — síntesis de apb-disc-spec-gen-v1.0/apb-pm-product-analysis-v1.0/apb-arch-c4-model-v1.0/apb-arch-decompose-v1.0) — pendiente validación humana. No distribuir sin revisión.
>
> Este índice consolida los **24 dossiers** generados en `discovery/ddd-sostrat-mj8/app-dossiers/` (23 apps finales + 1 documento de migración/retirada para Escalas). Cada dossier es un documento autocontenido de 17 secciones (análisis funcional, técnico, modelo de datos, arquitectura, dominio DDD, pantallas, APIs, eventos, diagrama topológico C4, estrategia de convivencia, testing/seguridad, riesgos, estimación, checklist de validación) pensado para que el **equipo funcional valide el alcance** y el **equipo de desarrollo estime e implemente**.
>
> Cada dossier fue generado por un agente independiente con instrucción explícita de **re-verificar contra el código real de `SOSTRAT-Sostrat-MJ8`**, no de copiar sin comprobar los documentos de sesiones anteriores (`proposals/bc-*.md`, `coverage-audit.md`, specs, backlog). Esto produjo un número significativo de correcciones factuales, documentadas app por app en la sección 14 ("Riesgos y gaps de evidencia") de cada dossier y resumidas en §3 de este índice.

## 1. Cómo usar este índice

- **Equipo funcional**: empieza por la columna "Estado" — prioriza validar primero los `PROVISIONAL`/bloqueados (impactan el roadmap) y los que tienen "hallazgo clave" con implicación de alcance.
- **Equipo de desarrollo**: cada dossier enlaza a su `bc-*-v1.md`/`dom-*-v1.md` de origen, a su spec `openapi-*.yaml`/`asyncapi-*.yaml` si existe, y a su épica en `jira-backlog.md`.
- **Arquitectura APB**: la sección 2.2 lista los 3 bloqueantes de decisión que afectan a varias apps a la vez y deben resolverse antes de abrir el PR de catálogo (`pr-instructions.md`).

## 2. Tabla maestra (24 dossiers, agrupados por fase del roadmap)

### Fase 0 — Fundamentos de plataforma

| # | App | Dominio DDD | Estado | Hallazgo clave de esta verificación |
|---|---|---|---|---|
| [01](dossier-01-datos-maestros-equipamiento.md) | Datos Maestros de Equipamiento | `dom-mercancias-v1` (transversal) | DISCOVERED | `matriculaiso` no es la matrícula ISO 6346 real (es un flag S/N); PIF no tiene consumo activo (única referencia comentada); 52 ficheros consumidores reales en 7+ paquetes |

### Fase 1 — Quick wins

| # | App | Dominio DDD | Estado | Hallazgo clave de esta verificación |
|---|---|---|---|---|
| [02](dossier-02-ferrocarril-portuario.md) | Ferrocarril Portuario | `dom-ferrocarril-v1` | DISCOVERED | Candidato recomendado a primera extracción formal del roadmap |
| [03](dossier-03-mano-estiba.md) | Mano de Estiba | `dom-mano-estiba-v1` (propio) | PROVISIONAL | Corrige el alcance funcional asumido por el resto de artefactos de esta app |
| [04](dossier-04-depotsis.md) | Depotsis | `dom-mercancias-v1` | DISCOVERED | Correcciones respecto a `bc-depotsis-v1.md` (ver §7/§12 del dossier) |

### Fase 2 — Dominios supporting de tamaño medio

| # | App | Dominio DDD | Estado | Hallazgo clave de esta verificación |
|---|---|---|---|---|
| [05](dossier-05-pps.md) | PPS (Pases y Permisos) | `dom-acceso-seguridad-fisica-v1` | DISCOVERED | Plantilla de referencia de toda la serie |
| [06](dossier-06-marpol-residuos.md) | MARPOL / Residuos | `dom-medio-ambiente-marpol-v1` | DISCOVERED | Corrige un bloqueante clave (ver §13 del dossier) |
| [07](dossier-07-aguada.md) | Aguada | `dom-suministros-buques-v1` (compartido con Suministro Eléctrico) | 🔴 PROVISIONAL — gap de evidencia sin cerrar | El modelo transaccional real de escritura no existe como código fuente en el checkout auditado |
| [08](dossier-08-marinas-pesca.md) | Marinas y Pesca | `dom-pesca-marinas-v1` | DISCOVERED | Pregunta de modelado abierta: separar Marinas de Pesca en dos dominios |
| [09](dossier-09-transporte-terrestre.md) | Transporte Terrestre | `dom-transporte-terrestre-v1` | DISCOVERED | Rutas reales: 56, no 89 (33 duplicadas con `struts-config.xml` principal); acoplamiento no documentado con PPS y Escalas (CODECO); `OperacioPuntualAction` (4.072 líneas) y `AutorizacionGenericaAction` (3.795) son mayores que `PreavisAction` |

### Fase 3 — Núcleo de Mercancías y Aduanas

| # | App | Dominio DDD | Estado | Hallazgo clave de esta verificación |
|---|---|---|---|---|
| [10](dossier-10-mmpp.md) | MMPP (Mercancías Peligrosas) | `dom-mercancias-peligrosas-v1` | discovered | — |
| [11](dossier-11-pif.md) | PIF (Punto de Inspección Fronteriza) | `dom-inspeccion-control-v1` | DISCOVERED | Decisión de diseño abierta: fusión con SCPP (**resuelta en dossier 19**, ver más abajo) |
| [12](dossier-12-manifiestos.md) | Manifiestos | `dom-mercancias-v1` | DISCOVERED | 63 rutas confirmadas; `CN_Tramo_Impl.java` (4.159 líneas) es la mayor god class del módulo, no citada antes; **153 referencias a Manifiestos desde el motor de reglas de Facturación** — acoplamiento más profundo de la serie hasta ese punto |
| [13](dossier-13-aduanas-contenedores.md) | Aduanas y Control de Contenedores | `dom-mercancias-v1` | DISCOVERED — consolidación interna pendiente | El OpenAPI/AsyncAPI publicado modela `MovimientoContenedor` (DTO sin uso real) en vez de la entidad activa real `TrasllatContenidor`; acoplamiento profundo no documentado con Manifiestos; integración REST moderna sin mapear (`swagger.inspecciones.client`) |

### Fase 4 — Concesiones y Facturación (máximo riesgo, al final)

| # | App | Dominio DDD | Estado | Hallazgo clave de esta verificación |
|---|---|---|---|---|
| [14](dossier-14-concesiones.md) | Concesiones (Título / Garantías) | `dom-concesiones-v1` | PROVISIONAL | Dependiente de EPIC-12 (evento `TituloActualizado` en producción) como prerequisito duro |
| [15](dossier-15-facturacion-liquidaciones.md) | Facturación y Liquidaciones | `dom-facturacion-v1` | PROVISIONAL | El motor de reglas `liquidadormm/` tiene 153 referencias a Manifiestos + 56 a Escalas (acoplamiento más profundo de toda la serie); 2 de 4 hallazgos de `dead-code-register.md` en este módulo son **falsos positivos** (overrides polimórficos activos); god classes hasta 5.413 líneas no documentadas |

### Fase 6 — Bounded contexts descubiertos en la auditoría de cobertura (2026-07-13)

| # | App | Dominio DDD | Estado | Hallazgo clave de esta verificación |
|---|---|---|---|---|
| [16](dossier-16-clavegueram.md) | Clavegueram | `dom-clavegueram-v1` (propio) | PROVISIONAL | Corrige la premisa de "cero acoplamiento": 4 puntos reales de dependencia con Facturación; conflicto de planificación sin resolver entre EPIC-15 y EPIC-13B |
| [17](dossier-17-buques.md) | Buques (Ship Master Data) | `dom-operaciones-maritimas-v1` — **confirmado, no tentativo** | DISCOVERED | Fan-out real de 145/13+ BCs consumidores (4x más de lo documentado); integración externa no documentada (Lloyd's Register); spec OpenAPI cubre solo 14/68 campos reales; recomienda migrarse antes o en paralelo con sus consumidores |
| [18](dossier-18-servicios-auxiliares-cruceros.md) | Servicios Auxiliares de Cruceros | `dom-cruceros-v1` | DISCOVERED | 15 rutas confirmadas pero mapeadas a 8 Actions, no 4; el OpenAPI/events-catalog/ui-screens-backlog modelan campos que no existen en las entidades reales — **requieren regenerarse** |
| [19](dossier-19-inspeccion-scpp.md) | Capacidad e Inspección Fronteriza (SCPP) | `dom-inspeccion-control-v1` | DISCOVERED | **Pregunta de fusión con PIF resuelta con evidencia: SÍ fusionar** — cero uso de `LlocDInspeccio` fuera de PIF/SCPP/Posicionament, comentarios de código confirman ticket compartido PIF-1429; PK inventada en la spec OpenAPI |
| [20](dossier-20-tramites-cliente.md) | Trámites de Cliente | `dom-administracion-electronica-v1` — encaje no verificado hasta este dossier | DISCOVERED | Resuelve que `carpetaclientes` y `documentconcessions` NO son gaps huérfanos (ya cubiertos por Facturación y Concesiones); spec OpenAPI con nombres de campo sistemáticamente incorrectos |
| [21](dossier-21-suministro-electrico-buques.md) | Suministro Eléctrico a Buques (Shore Power) | `dom-suministros-buques-v1` (compartido con Aguada) | DISCOVERED | Integración REST real no documentada con sistema externo de telemetría de conexión eléctrica (posible BEST); a diferencia de Aguada, el modelo de escritura SÍ está confirmado (no hay gap de evidencia) |
| [22](dossier-22-efficiency-network.md) | Efficiency Network (Business Club) | `dom-operaciones-maritimas-v1` — tentativo | 🟡 PROVISIONAL — bloqueante compartido con #23 | `EmpresaBC extends Usuari` (herencia real de clase) — es especialización de Operadores Portuarios, no dominio sin encaje |
| [23](dossier-23-operadores-portuarios.md) | Operadores Portuarios / Terceros (Usuari) | `dom-operaciones-maritimas-v1` — tentativo | 🟡 PROVISIONAL — bloqueante de dominio, resolver este resuelve el de #22 | Fan-out de 369 ficheros (el mayor de toda la serie); entidad no documentada `CompteBancari` (IBAN/BIC, datos SEPA) ausente de la spec OpenAPI y del catálogo de eventos |

### Fuera de fase — Migración/retirada (no es una extracción)

| # | App | Dominio DDD | Estado | Hallazgo clave |
|---|---|---|---|---|
| [00](dossier-00-escalas-migracion-argos.md) | Escalas (Port Call) — SÒSTRAT legacy | `dom-operaciones-maritimas-v1` | 🔴 **NO ES UNA EXTRACCIÓN — ES UNA MIGRACIÓN/RETIRADA**, pendiente de sesión formal con ARGOS/AOM | ARGOS ya consume la escala de SÒSTRAT en producción; requiere separar 81 referencias a Liquidación/Facturación en `EscalaAction.java` antes de cualquier retirada |

> **Nota de numeración**: `dossier-17-buques.md` y `dossier-17-operadores-portuarios.md` compartían por error el mismo número de secuencia en la generación inicial. Se ha renumerado Operadores Portuarios a **`dossier-23`** para eliminar la colisión; no hay pérdida de contenido, solo cambio de nombre de fichero.

## 3. Bloqueantes de decisión pendientes (afectan a varias apps, requieren Arquitectura APB)

1. **`parent_domain` tentativo de Operadores Portuarios (#23) y Efficiency Network (#22)** — comparten el mismo bloqueante (`EmpresaBC extends Usuari`). Resolver el de Operadores Portuarios resuelve automáticamente el de Efficiency Network. Ver `pr-instructions.md §2.3`. Ninguno de los dos se debe enviar al PR de catálogo hasta resolverlo.
2. **Fusión PIF (#11) + SCPP (#19)** — recomendación con evidencia: fusionar en un único bounded context. Pendiente de confirmación funcional/Arquitectura APB. El dossier #19 también señala que **Posicionament** (sin bounded context propio todavía) presenta el mismo patrón de acoplamiento síncrono y debería evaluarse en el mismo movimiento.
3. **Conflicto de planificación Clavegueram (#16)**: `jira-backlog.md` EPIC-15 lo trata como extracción independiente; EPIC-13B lo despliega dentro de Facturación. La evidencia de código (4 puntos de acoplamiento real con Facturación) favorece EPIC-13B, pero es una decisión de producto, no solo técnica.
4. **Gap de evidencia de Aguada (#07)**: el modelo transaccional de escritura no existe en el checkout auditado — es el único dossier de la serie con este nivel de incertidumbre; requiere acceso a un checkout más completo o al equipo IN2 (proveedor) antes de diseñar la migración.

## 4. Correcciones pendientes de propagar a otros documentos de la sesión

Esta verificación app-por-app encontró varios casos de **specs ya publicadas construidas sobre entidades equivocadas, con nombres de campo incorrectos, o con cobertura de campos muy incompleta**. No se han corregido automáticamente (cada dossier solo las reporta) — quedan pendientes de una pasada de corrección explícita:

| Documento afectado | Problema encontrado | Dossier que lo detectó |
|---|---|---|
| `specs/openapi-aduanas-contenedores` / `events-catalog.md` | Modela `MovimientoContenedor` (DTO sin uso real) en vez de `TrasllatContenidor` (entidad activa real) | #13 |
| `specs/openapi-buques.yaml` | Cubre solo 14 de 68 campos reales de `Vaixell`; `bandera` mal tipado como string libre en vez de FK entero; falta endpoint de restauración y sub-recurso de certificados/ISPS | #17 |
| `specs/openapi-servicios-auxiliares-cruceros.yaml`, `events-catalog.md`, `api-surface-by-phase.md`, `ui-screens-backlog.md` | Modelan campos (`numescala`/`anyescala`/`ocupacio`/`moll`) que no existen en `CreuerBus`/`CreuerVigilanciaPunt` (agregado real es por día natural, no por escala) | #18 |
| `specs/openapi-inspeccion-scpp.yaml` | PK inventada (`idinspeccio`); PK real es compuesta (`sptinspeccio`+`anyinspeccio`+`seqinspeccio`) | #19 |
| `specs/openapi-tramites-cliente.yaml` | Nombres de campo sistemáticamente incorrectos (`assumpte`/`idtipustramit`/`idestat`/`datcreacio`/`datlectura` vs. reales `sentittramit`/`idtiptramit`/`idestattramit`/`datacreacio`/`datalectura`) | #20 |
| `specs/openapi-suministro-electrico-buques.yaml`, `events-catalog.md` | No documentan la integración REST externa real de telemetría (`Session/Last7Days`) | #21 |
| `specs/openapi-operadores-portuarios.yaml` | No incluye `CompteBancari` (datos bancarios/SEPA); tipa `eseffnetwork` como boolean cuando es string S/N | #23 |
| `dead-code-register.md` | 2 de los 4 hallazgos de Facturación (`CN_LiquidadorMM_Pasajeros_Impl.java:245` y 2 comentarios "NO SE USA PARA LA L2") son **falsos positivos** — overrides polimórficos activos en producción | #15 |
| `dead-code-register.md` | Nuevos candidatos sin registrar: `decisionMensajeEnviarCUSREP` (Manifiestos), `obtenerConsumosElecFake`/`getConsumosUltimos7Dias` (Suministro Eléctrico), 3 Actions huérfanas (Aduanas/Contenedores) | #12, #21, #13 |
| `coverage-audit.md` | Varias cifras de conteo de rutas corregidas durante esta serie (ver tabla §2 de este índice: Transporte Terrestre 56 no 89; el "63" que tenía asignado a Transporte Terrestre pertenece a Manifiestos) | #09, #12 |

## 5. Próximos pasos sugeridos

1. **Validación funcional**: revisar en orden de prioridad los bloqueantes de §3, empezando por el de Operadores Portuarios/Efficiency Network (afecta a 2 apps) y la fusión PIF/SCPP (afecta al roadmap de Fase 3 y 6).
2. **Corrección de specs**: aplicar la tabla de §4 — son correcciones acotadas (nombres de campo, entidad equivocada, campos faltantes), no rediseños.
3. **Decisión de push**: el trabajo de esta sesión sigue solo en commit local (`c6dd4fe` + posteriores) — pendiente de decidir destino de publicación dado que `apb-dmartin/APB-IA-FRAMEWORK` es un repositorio público con contenido confidencial.
4. **Enriquecimiento del framework**: durante esta serie no se usó un skill dedicado "dossier de aplicación" (no existe todavía en `skills/apb-owned/`) — se sintetizó combinando `apb-disc-spec-gen-v1.0`, `apb-pm-product-analysis-v1.0`, `apb-arch-c4-model-v1.0` y `apb-arch-decompose-v1.0`. Si este formato de dossier resulta útil de forma recurrente, considerar formalizarlo como skill propio.

## 6. Historial de cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-13 | APB AI Framework | Índice inicial, tras completar los 24 dossiers de la serie (00-23) y resolver la colisión de numeración #17 |
