# Informe de Análisis de Riesgos — ARQ-3684

> **Ejemplo real de output** de la skill `apb-gov-org-risk-report-v1.0`
> (agente `apb-agent-compliance-audit-v1.0`), generado a partir del ticket
> Jira real [ARQ-3684](https://portdebarcelona.atlassian.net/browse/ARQ-3684)
> como prueba de validación solicitada por Débora (2026-07-06). Sigue la
> plantilla corporativa exacta de
> [`PROCEDURE_RISK_EVALUATION.md §8`](../../context/apb/policies/quality/PROCEDURE_RISK_EVALUATION.md)
> — no se ha inventado una plantilla nueva.
>
> **v2 (2026-07-06):** revisado tras aportar Débora el contexto real que
> faltaba en la v1 — la integración es con Alfresco, y Ciberseguridad ha
> confirmado que afecta a 5 servidores con Apache Tomcat 7.0.x, en End of
> Life desde el 31/3/2021 (deuda técnica sin soporte ni parches del
> fabricante desde hace más de 5 años). Esto cambia sustancialmente el
> análisis: ya no hay un dato pendiente que condicione la decisión — hay un
> segundo riesgo, más grave que el original, que había quedado sin
> registrar.
>
> **v3 (2026-07-06):** Débora detectó que la v2, pese a citar
> `PROCEDURE_NONCOMPLIANCE_MANAGEMENT_v1.0` en la cabecera, no aplicó
> realmente su contenido — solo lo nombraba. Causa raíz corregida en la
> skill (`apb-gov-org-risk-report-v1.0` v1.4.0) y en `validate_repo.py`
> (check #27): el procedimiento se nombraba en prosa sin ruta literal ni
> instrucción de carga, a diferencia de `PROCEDURE_RISK_EVALUATION`, que sí
> tenía un paso "Aplica" explícito — por eso este último se aplicó a fondo
> (tabla de riesgos, dimensiones C/I/D/T) y el primero no. Esta versión
> corrige también la atribución de agente (el informe original se atribuyó
> a `apb-agent-risk-exception-v1.0`, que no tiene asignada esta skill) y
> añade las 4 secciones que el procedimiento exige y la v2 omitió: ticket
> maestro JSM (§8.7), justificación de negocio de la excepción (§9.1),
> flujo exacto de 3 aprobaciones (§9.3) y tabla de plazos de resolución
> (§10). El análisis de riesgos R1/R2/R3 y el plan de mitigación de la v2
> no cambian de fondo — se mantienen porque ya eran correctos.
>
> **Generado por IA:** Claude (Anthropic), 2026-07-06. Recomendación de
> soporte, no vinculante — la decisión final y las firmas son siempre
> humanas (POLICY_AI_USAGE §6, PROCEDURE_NONCOMPLIANCE_MANAGEMENT_v1.0).

---

## Identificación

- **Objeto:** Evaluación del riesgo derivado del incumplimiento de política de arquitectura y estándares tecnológicos (uso de llamadas SOAP), y del riesgo de seguridad de la infraestructura legacy a la que ese incumplimiento conecta
- **Sistema/Activo:** APB.API.FIL (`git@github.com:portdebarcelona/ApbApi.git`, rama `origin/develop`, build 8) — integra con **Alfresco** vía SOAP (capa SOA legacy, `APB_KNOWLEDGE_BASE.md §5.5`, en migración progresiva a REST/SharePoint vía `APB.API.FLC`)
- **Infraestructura afectada (aportado por Ciberseguridad):** 5 servidores con Apache Tomcat 7.0.x
- **Responsable del sistema:** [Completar — equipo de desarrollo asignado a APB.API.FIL]
- **Responsable de la infraestructura Alfresco/Tomcat:** [Completar — Ciberseguridad/Sistemas ya tiene conocimiento de este hallazgo según lo aportado]
- **Ticket técnico de origen (Jira Software):** [ARQ-3684](https://portdebarcelona.atlassian.net/browse/ARQ-3684)
- **Ticket maestro (Jira Service Management):** ⚠️ **Pendiente de confirmar** — ver §"Aplicación del procedimiento de incumplimientos", punto 1. No asumido ni inventado.
- **Fecha:** 2026-07-06 (detección original del incumplimiento SOAP: 2026-02-13T10:56:00+0000; End of Life de Tomcat 7.0.x: 31/3/2021)
- **Analista:** Claude (Anthropic) — soporte de IA, agente `apb-agent-compliance-audit-v1.0` (orquesta la skill `apb-gov-org-risk-report-v1.0`)
- **Origen del incumplimiento (R1):** detección automática, SonarQube Quality Gate, entorno TST
- **Origen del riesgo de infraestructura (R2):** comunicado por Ciberseguridad (no detectado por el escaneo Nessus mensual documentado en este análisis — a confirmar si ya está en el Registro de Vulnerabilidades en SharePoint)
- **Ticket origen R1:** [ARQ-3684](https://portdebarcelona.atlassian.net/browse/ARQ-3684)
- **Control incumplido (R1):** `ARC-VALIDATION-SOAP` — Validación de llamadas SOAP
- **Política aplicada (R1):** `POL-ARC-001` — Arquitectura y estándares tecnológicos
- **Procedimiento aplicado (R2):** `POLICY_VULNERABILITY_MANAGEMENT_v1.1`
- **Severidad declarada (SonarQube, R1):** CRITICAL
- **Archivo (R1):** `APB.API.FIL:src/APB.API.FIL/Program.cs`
- **Enlaces de origen:** [SonarQube](http://gisplanolpre.port.apb.es:9001/project/issues?id=APB.API.FIL&issues=339acf83-5a9a-46bc-a309-b8c1ad8b1b4a) · [Jenkins build 8](https://serveispre.portdebarcelona.cat/jenkins/job/ARQ/job/TST/job/ARQ/job/APBAPI-ApisArquitectura/job/APB.API.FIL/8/)

---

## Resumen ejecutivo

El análisis automático de calidad (SonarQube) ha detectado, en el entorno de pruebas (TST) de APB.API.FIL, uso de llamadas SOAP en el fichero de arranque del servicio (`Program.cs`), incumpliendo `STANDARD_ARCHITECTURE.md` ("REST homologado, NO SOAP/WSDL") y `STANDARD_QA.md` ("NO SOAP/WebServices") bajo el control `ARC-VALIDATION-SOAP`.

Débora ha confirmado el contexto que la v1 de este informe dejaba como dato pendiente: la llamada SOAP integra con **Alfresco**, sistema legacy ya documentado en migración progresiva a REST (`APB_KNOWLEDGE_BASE.md §5.5`). Esto por sí solo movería la valoración hacia "Media-Alta en legacy si existe plan de retirada" en vez de "Alta" (criterio de `PROCEDURE_RISK_EVALUATION.md §4.3`).

Pero Ciberseguridad ha aportado un dato que **cambia la naturaleza del análisis**: la infraestructura que sirve esa integración Alfresco corre sobre **Apache Tomcat 7.0.x en 5 servidores**, cuyo End of Life del fabricante fue el **31/3/2021** — es decir, **más de 5 años sin parches de seguridad ni soporte del fabricante**. Esto no es deuda arquitectónica (como el uso de SOAP); es una **vulnerabilidad de infraestructura sin solución de fabricante disponible**, que `POLICY_VULNERABILITY_MANAGEMENT_v1.1 §4.3` trata como un caso cualitativamente distinto: no se puede "aplicar un parche", solo contener el riesgo y decidir formalmente qué hacer con él (migrar, aislar o aceptar el riesgo a nivel de dirección).

**El riesgo real no es aprobar o denegar una excepción de arquitectura aislada — es que aprobar sin condiciones un nuevo acoplamiento de código (APB.API.FIL) a una plataforma ya crítica por obsolescencia de 5 años prolonga y profundiza la dependencia de ese riesgo no resuelto**, en un momento en que el sistema está en desarrollo activo (build 8, TST) y por tanto es el punto de menor coste para intervenir — antes de que llegue a PRE/PRO.

Adicionalmente, este informe **no puede darse por completo hasta resolver dos huecos de procedimiento** (ver siguiente sección): confirmar el ticket maestro JSM y obtener la justificación de negocio de la excepción. Sin ambos, `PROCEDURE_NONCOMPLIANCE_MANAGEMENT_v1.0` impide considerar el incumplimiento formalmente registrado/evaluable.

---

## Aplicación del procedimiento de gestión de incumplimientos (`PROCEDURE_NONCOMPLIANCE_MANAGEMENT_v1.0`)

> Sección añadida en v3. `PROCEDURE_NONCOMPLIANCE_MANAGEMENT_v1.0`
> (`context/apb/policies/compliance/PROCEDURE_NONCOMPLIANCE_MANAGEMENT_v1.0.md`)
> exige estos 4 puntos explícitamente — ninguno estaba en la v2.

### 1. Ticket maestro (§8.7)

`ARQ-3684` es, por su formato y proyecto (`ARQ` — Arquitectura .NET), un **ticket técnico de Jira Software**. El procedimiento es explícito: *"el ticket técnico no sustituye el registro del incumplimiento"* y *"en ningún caso se considerará resuelto un incumplimiento únicamente por el cierre de un ticket técnico en herramientas de desarrollo"* (§8.7).

⚠️ **Pendiente de confirmar — pregunta bloqueante, no se asume:** ¿existe un ticket en Jira Service Management (JSM), tipo "Incumplimiento" o "Solicitud de Excepción", vinculado a `ARQ-3684`? Este informe no tiene acceso a JSM para verificarlo directamente.

- Si **existe**: ese ticket JSM es el registro oficial; este informe debe adjuntarse a él y el seguimiento del incumplimiento debe hacerse ahí, no en `ARQ-3684`.
- Si **no existe**: debe crearse antes de que este incumplimiento pueda considerarse formalmente registrado, conforme a §7 y §8.7.

### 2. Justificación de negocio de la excepción (§9.1, §9.5)

El procedimiento es explícito: *"no se evaluará ninguna solicitud de excepción que no esté debidamente documentada"* (§9.1), y la evaluación de negocio debe responder *"¿qué impacto tendría para el negocio no conceder la excepción?"* (§9.5).

⚠️ **Pendiente de confirmar — pregunta bloqueante, no se asume:** ¿cuál es el impacto operativo de **no** conceder la excepción a R1 (p. ej.: bloqueo del desarrollo de APB.API.FIL, coste/plazo de reescribir la integración sin SOAP, dependencia de una fecha de entrega comprometida)? Este dato no consta en el ticket `ARQ-3684` ni ha sido aportado en esta sesión — debe solicitarse al Responsable del Servicio antes de que la solicitud de excepción (Track B, condiciones más abajo) pueda evaluarse formalmente.

### 3. Flujo de aprobación — 3 niveles exactos (§9.3)

El procedimiento exige 3 aprobaciones obligatorias, no una tabla de firmas genérica. Aplicado a este caso (`POL-ARC-001`, matriz de responsables §3.1: "Arquitectura tecnológica → responsable técnico principal Sistemas, validador adicional Ciberseguridad/Arquitectura"):

| Tipo de aprobación | Rol en este caso | Función |
|---|---|---|
| Aprobación de negocio | Jefe de Departamento solicitante (responsable de APB.API.FIL) | Valida la necesidad operativa (una vez completado el punto 2) y asume el compromiso de corrección |
| Evaluación técnica 1 | Responsable de la política `POL-ARC-001` (Sistemas/Arquitectura) | Evalúa el impacto técnico y la viabilidad de aislar la llamada SOAP (Track B) |
| Evaluación técnica 2 | Ciberseguridad o Arquitectura, aprobado por CISO o CTO — *`POL-ARC-001` tiene un único responsable técnico principal, por lo que §9.3 exige que la segunda validación la haga Ciberseguridad/Arquitectura con aprobación de CISO/CTO* | Evalúa el riesgo tecnológico global y la coherencia con el marco de políticas IT |
| **Evaluación adicional obligatoria (CISO)** | Ciberseguridad (CISO) | **Obligatoria por R2** (impacto en seguridad de la información, §9.3 tercer párrafo) — no es opcional dado el hallazgo de Tomcat 7.0.x EOL |

Ninguna de las 4 puede omitirse ni aprobarse unilateralmente por el equipo solicitante (§9.3, último párrafo).

### 4. Plazos de resolución y de excepción (§10)

| Riesgo | Criticidad (`PROCEDURE_NONCOMPLIANCE_MANAGEMENT_v1.0 §10`) | Plazo de corrección recomendado | Duración máxima de excepción |
|---|---|---|---|
| R1 — SOAP no homologado | Alto (Media-Alta, ver tabla de riesgos) | ≤ 30 días naturales | Hasta 90 días, con plan de remediación (Track B) |
| R2 — Tomcat 7.0.x EOL | Crítico | Corrección/contención inmediata, ≤ 7 días naturales | Excepcionalmente hasta 30 días, solo con medidas compensatorias activas (Track A) |

Estos plazos son el criterio corporativo general (§10); no sustituyen, sino que complementan, los plazos ya fijados en el Plan de mitigación más abajo desde `POLICY_VULNERABILITY_MANAGEMENT_v1.1` para R2 (más estricta y más específica para infraestructura EOL — prevalece la más restrictiva).

---

## Análisis de riesgos

| ID | Riesgo | Dimensión más afectada | Impacto | Probabilidad | Riesgo inherente | Riesgo residual (sin controles compensatorios confirmados) |
|---|---|---|---|---|---|---|
| R1 | Uso de SOAP/WebService no homologado (integración confirmada con Alfresco, legacy en migración) | Mantenibilidad / Trazabilidad (T) | Medio | Alta | Media-Alta | Media-Alta |
| R2 | Apache Tomcat 7.0.x End of Life (31/3/2021) en 5 servidores — sin parches de seguridad del fabricante desde hace >5 años | Confidencialidad / Integridad / Disponibilidad (C/I/D) | **Crítico** | Alta (exposición prolongada, superficie de ataque conocida y sin mitigar) | **Crítico** | **Crítico** (sin controles compensatorios confirmados en el ticket) |
| R3 (transversal) | Acumulación de riesgo: nuevo código (APB.API.FIL) profundiza el acoplamiento a una plataforma ya clasificada como Crítica por obsolescencia | Gobernanza / Riesgo agregado | — | — | Se suma a R2, no se valora de forma independiente | Aumenta el radio de impacto de R2 si se aprueba sin aislamiento |

R2 tiene un nivel de riesgo muy superior a R1 y es, en la práctica, el que debería gobernar la decisión final — un incumplimiento de arquitectura (R1) no debería aprobarse "gratis" cuando profundiza la dependencia de una infraestructura ya crítica (R2) que aún no tiene plan de remediación confirmado en este ticket.

---

## Evaluación de riesgos

### R1 — Riesgo por uso de SOAP/WebService no homologado (§4.3 `PROCEDURE_RISK_EVALUATION.md`)

**Descripción del riesgo (formato corporativo):** *Existe riesgo de aumento de deuda técnica y pérdida de observabilidad uniforme debido al uso de llamadas SOAP no homologadas para integrar con Alfresco, afectando a la mantenibilidad y sostenibilidad tecnológica de APB.API.FIL.*

**Argumentación:**
- `STANDARD_ARCHITECTURE.md §APIs` exige "REST homologado (NO SOAP/WSDL)" — requisito documentado, no preferencia.
- Con el contexto ya confirmado (integración con Alfresco, sistema legacy con migración a REST ya en marcha vía `APB.API.FLC`), este caso corresponde al supuesto **"Media-Alta en legacy si existe plan de retirada y aislamiento"** de `PROCEDURE_RISK_EVALUATION.md §4.3` — más favorable que "Alta" (que aplicaría a un sistema nuevo naciendo fuera de estándar sin justificación legacy).
- Condición no verificada en el ticket: si existe o no un adaptador que aísle la llamada SOAP del resto del dominio de APB.API.FIL. Sin esa confirmación, el riesgo residual no puede reducirse por debajo del inherente.

**Impacto (C/I/D/T):** Trazabilidad/Mantenibilidad Medio (dimensión máxima). **Probabilidad:** Alta (el código ya existe en build 8). **Riesgo inherente y residual:** Media-Alta.

**Tratamiento propuesto:** Mitigar (aislar), no Evitar (la dependencia con Alfresco es real mientras dure la migración), no Aceptar sin condiciones.

---

### R2 — Riesgo por infraestructura en End of Life sin soporte del fabricante (Apache Tomcat 7.0.x, 5 servidores)

**Marco aplicado:** `POLICY_VULNERABILITY_MANAGEMENT_v1.1 §4.2` (categorización) y `§4.3` ("Gestión de vulnerabilidades sin solución disponible"), `PROCEDURE_RISK_EVALUATION.md §3` (criterios de aceptación: *"Riesgo Crítico: no aceptable; requiere remediación inmediata o decisión de dirección"*).

**Descripción del riesgo (formato corporativo):** *Existe riesgo de compromiso de confidencialidad, integridad y disponibilidad debido a la ejecución de Apache Tomcat 7.0.x sin soporte ni parches del fabricante desde el 31/3/2021, afectando a 5 servidores que sirven la integración Alfresco de la que depende APB.API.FIL.*

**Por qué es un riesgo distinto y más grave que R1 (argumentación):**
- Un incumplimiento de arquitectura (R1) tiene remediación disponible (reescribir a REST, aislar con adaptador). Una plataforma en End of Life **no tiene parches disponibles por definición** — cualquier vulnerabilidad descubierta en Tomcat 7.0.x desde 2021 hasta hoy queda sin corrección posible del fabricante. `POLICY_VULNERABILITY_MANAGEMENT_v1.1 §4.3` reconoce explícitamente este escenario y lo trata aparte del ciclo normal de parcheo: *"Implementar medidas de contención... Elevar a OTS y RSI si es necesario escalar al Comité de Seguridad y Riesgos... transferir al Comité de Riesgos para aceptación formal del riesgo residual."*
- **5 años de exposición acumulada** (2021→2026) implica que vulnerabilidades públicas conocidas de Tomcat 7.0.x (CVE de esa rama, EOL desde hace años) muy probablemente ya están documentadas en fuentes públicas (NIST NVD, CCN-CERT) sin que exista parche oficial — es decir, el riesgo no es hipotético, es acumulado y conocido por la comunidad de seguridad.
- Afecta a **5 servidores**, no a uno — el radio de impacto de cualquier explotación es multiplicado.
- Este riesgo **no es nuevo por este ticket** — ya existía antes de ARQ-3684. Lo que sí introduce este ticket es una **razón adicional para no ampliar la dependencia** de código nuevo sobre esa plataforma sin, como mínimo, confirmar que ya está siendo tratado.

**Impacto (C/I/D):** Crítico — un Tomcat sin parches de 5+ años puede tener vulnerabilidades de ejecución remota de código conocidas y sin mitigar. **Probabilidad:** Alta — no requiere un atacante sofisticado; son vulnerabilidades públicas de una versión obsoleta. **Riesgo inherente:** Crítico. **Riesgo residual:** Crítico, salvo que existan controles compensatorios no reflejados en este ticket (segmentación de red, WAF, ausencia de exposición a Internet, monitorización reforzada).

**Tratamiento (ISO 27001):** Mitigar de forma inmediata (contención) + Migrar/Evitar a medio plazo (no es aceptable dejarlo como "riesgo aceptado" indefinido, per criterio de Riesgo Crítico del propio procedimiento). **Este riesgo, si no está ya en el Registro de Vulnerabilidades, debe registrarse y escalarse independientemente de la resolución de R1.**

---

## Plan de mitigación (acciones, responsables, plazos, criterios de cierre)

> Exigido por el propio alcance de `apb-gov-org-risk-report-v1.0`
> ("outputs: plan de mitigación concreto: acciones, responsables, plazos y
> criterios de cierre") — ausente en la v1 de este informe, corregido aquí.

### Track A — R2, infraestructura crítica (prioridad máxima, no depende de la decisión sobre R1)

| # | Acción | Responsable propuesto | Plazo recomendado | Criterio de cierre |
|---|---|---|---|---|
| A1 | Verificar si Tomcat 7.0.x / los 5 servidores ya constan en el Registro de Vulnerabilidades (SharePoint) de `POLICY_VULNERABILITY_MANAGEMENT_v1.1`. Si no constan, darlos de alta como Crítico | OTS / RSI | Inmediato (≤ 5 días naturales — plazo de resolución para Crítico, `POLICY_VULNERABILITY_MANAGEMENT_v1.1 §4.4`, aplicado aquí al registro y evaluación, no a la migración completa) | Entrada registrada con nivel Crítico y responsable asignado |
| A2 | Medidas de contención inmediatas: restringir exposición de red de los 5 servidores (firewall/segmentación), reforzar monitorización/alertado, verificar que no están expuestos a Internet sin control adicional (WAF/IPS) | Administradores de sistemas y red | ≤ 5-7 días naturales | Controles de contención verificados y documentados en el registro |
| A3 | Escalar formalmente a Comité de Seguridad y Riesgos para decisión de aceptación de riesgo residual o mandato de migración/decomiso, conforme a `POLICY_VULNERABILITY_MANAGEMENT_v1.1 §4.3` | RSI | ≤ 30 días naturales | Acta/decisión formal del Comité registrada |
| A4 | Plan de migración/decomiso de la plataforma Tomcat 7.0.x (actualización de versión soportada o migración de Alfresco a la infraestructura destino de la migración ya en marcha) | Responsable de Sistemas + Arquitectura | A definir por el Comité de Seguridad y Riesgos en A3 — recomendado alinear con la migración Alfresco→SharePoint/`APB.API.FLC` ya documentada, no crear un proyecto paralelo | Plataforma migrada o decomisada; cierre formal del riesgo |

### Track B — R1, arquitectura (condicionado a que A1-A3 estén en marcha)

| # | Acción | Responsable propuesto | Plazo recomendado | Criterio de cierre |
|---|---|---|---|---|
| B1 | Confirmar si la llamada SOAP en `Program.cs` ya está aislada tras un adaptador/anti-corruption layer. Si no lo está, implementarlo antes de promocionar a PRE | Equipo de desarrollo APB.API.FIL | Antes de la promoción a PRE (bloqueante) | Adaptador implementado; el resto del dominio de APB.API.FIL no referencia tipos/contratos SOAP directamente |
| B2 | No promocionar APB.API.FIL a PRE/PRO hasta que Track A (A1-A2 como mínimo) esté confirmado | Responsable del Servicio + Arquitectura | Bloqueante de la promoción | Confirmación explícita de A1-A2 antes del paso a PRE |
| B3 | Vincular la fecha de retirada de esta dependencia SOAP a la fecha de decisión de A4 (no fijar una fecha de arquitectura independiente de la decisión de infraestructura) | Arquitectura | Tras cierre de A3 | Fecha de retirada única y consistente entre R1 y R2 |

---

## Observaciones de auditoría

1. **Riesgo transversal de acumulación (§6.2 `PROCEDURE_RISK_EVALUATION.md`; principio de no acumulación de excepciones, §9.9 `PROCEDURE_NONCOMPLIANCE_MANAGEMENT_v1.0`):** aprobar R1 sin resolver o al menos contener R2 no es una excepción aislada — es ampliar la superficie de un riesgo ya Crítico. Aquí no son dos excepciones sobre el mismo ticket, pero sí dos riesgos acoplados sobre la misma cadena de dependencia (APB.API.FIL → Alfresco → Tomcat 7.0.x EOL).
2. **Punto positivo de gobernanza:** el control `ARC-VALIDATION-SOAP` ha funcionado según diseño — detección en TST, antes de PRE/PRO. Esto da margen real para actuar sin coste de rollback en producción.
3. **Verificar duplicidad:** si Ciberseguridad ya tiene un hallazgo abierto sobre estos 5 servidores (mencionado como comunicación informal — "Según nos comentó Ciberseguridad"), debe confirmarse si ya existe entrada en el Registro de Vulnerabilidades antes de crear una nueva (A1), para no duplicar el seguimiento.
4. Esta evaluación no sustituye un escaneo Nessus ni un análisis CVSS formal de R2 — la clasificación de Crítico aquí es una valoración cualitativa de soporte, consistente con los criterios documentados de `POLICY_VULNERABILITY_MANAGEMENT_v1.1`, pero la clasificación CVSS formal la determina la OTS.
5. **(Añadido v3)** Este informe tiene dos huecos de procedimiento sin resolver (ticket maestro JSM, justificación de negocio) — ver §"Aplicación del procedimiento de gestión de incumplimientos". La decisión final no debería tomarse sin cerrarlos, conforme a §9.1 del procedimiento.

---

## Decisión

**Resultado:** ⚠️ **NO AUTORIZAR la excepción de R1 sin condiciones — condicionar la aprobación al arranque verificable de Track A (R2) y, con carácter previo, a resolver los dos huecos de procedimiento del punto anterior (ticket JSM, justificación de negocio).**

**Justificación:** El riesgo que gobierna esta decisión no es el incumplimiento de arquitectura en sí (R1, Media-Alta, con remediación disponible y precedente legacy documentado), sino la infraestructura Crítica de la que depende (R2). Aprobar R1 sin exigir contención de R2 significaría autorizar que código nuevo, en desarrollo activo, profundice una dependencia sobre una plataforma sin soporte del fabricante desde hace más de 5 años — exactamente el tipo de riesgo que el procedimiento corporativo clasifica como "no aceptable; requiere remediación inmediata o decisión de dirección" (`PROCEDURE_RISK_EVALUATION.md §3`). Adicionalmente, `PROCEDURE_NONCOMPLIANCE_MANAGEMENT_v1.0 §9.1` impide evaluar formalmente una solicitud de excepción sin justificación de negocio documentada.

**Condiciones para autorizar R1 (APROBAR CON CONDICIONES, no aprobación libre):**
- Confirmar el ticket maestro JSM (§"Aplicación del procedimiento", punto 1) y aportar la justificación de negocio (punto 2) — bloqueante antes de cualquier firma.
- Track A (A1-A2, ver Plan de mitigación) confirmado en marcha — registro y contención de R2 — antes de continuar el desarrollo de la integración.
- Track B (B1) — aislamiento de la llamada SOAP tras adaptador — implementado antes de promoción a PRE.
- No promoción a PRE/PRO (B2) hasta ambas condiciones verificadas.
- Fecha de retirada de la dependencia SOAP vinculada a la decisión del Comité de Seguridad y Riesgos sobre R2 (B3), no fijada de forma independiente.
- Firmas conforme al flujo de 3+1 aprobaciones del punto 3 (§9.3), incluida la evaluación del CISO por impacto en seguridad de R2.

**Si estas condiciones no se cumplen:** la recomendación es **DENEGAR** — no por el mérito aislado de R1, sino porque no es razonable evaluar una excepción de arquitectura ignorando que profundiza un riesgo de infraestructura ya clasificado como Crítico, y porque el procedimiento corporativo no permite evaluar una excepción sin justificación de negocio ni ticket maestro confirmado.

---

## Aprobación

| Rol | Nombre | Firma | Fecha |
|---|---|---|---|
| Aprobación de negocio — Jefe de Departamento solicitante | [Completar] | | |
| Evaluación técnica 1 — Responsable de `POL-ARC-001` (Sistemas/Arquitectura) | [Completar] | | |
| Evaluación técnica 2 — Ciberseguridad/Arquitectura, aprobado por CISO o CTO | [Completar] | | |
| Evaluación adicional obligatoria — CISO (por impacto en seguridad de R2) | [Completar] | | |

---

*Este informe es una recomendación de soporte generada por IA (Claude, Anthropic). No sustituye el criterio profesional humano ni constituye una decisión de excepción válida sin las firmas anteriores. La clasificación de R2 como Crítico es una valoración cualitativa de apoyo — la calificación CVSS formal corresponde a la Oficina Técnica de Seguridad (OTS).*
