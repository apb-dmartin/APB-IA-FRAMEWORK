# Plan de Fases Futuras — Pendiente de Ejecución

> Este documento acumula tareas anotadas por Debora para sesiones futuras.
> Nada de lo aquí listado se ejecuta hasta que se aborde explícitamente su
> propia sesión.
>
> 📁 **Lo ya ejecutado vive en [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md)** (bitácora).
> Regla de mantenimiento: **antes de cerrar cada sesión**, mover a ese archivo
> los temas que se hayan completado y dejar aquí solo un puntero. Las tablas-índice
> de más abajo (Mapeo a sesiones, Plan de sesiones) se conservan íntegras como
> cuadro de mando del roadmap.

## Mapeo a sesiones planificadas (actualizado durante Sesión 8)

| Punto (#) | Sesión asignada |
|---|---|
| 1 (OpenSpec/SDD) | 8 (parcial — cobertura cap. 5 proyecto.md) |
| 2 (Guía de uso de agentes) | **13** |
| 3 (flujo legacy→SDD) | 8 (parcial — checklist de cobertura) |
| 4 (Sonar + PR automático) | ✅ **Resuelto, Sesión 11** — discovery confirmó que ya existía: `apb-dev-sonar-clean-v1.0`, `apb-dev-pr-doc-v1.0`, `prov-sonar-v1.0`, conectados a `apb-agent-implementer-v1.0`. No se reimplementó. |
| 5 (agente meta-gobernanza) | ✅ **Resuelto, Sesión 10** — `apb-agent-meta-builder-v1.0` creado (dominio `governance`). |
| 6 (plantillas + ofimáticas) | **13** — requiere ejemplos de Debora |
| 7 (mapa agentes↔Jira) | **13** |
| 8 (COSMIC con histórico real) | **13** — requiere datos de Debora |
| 9 (documentar terceros) | **9** |
| 10 (catálogo automático) | ✅ Resuelto, Sesión 3 |
| 11 (DDD + inventario dominios negocio) | ✅ **Unificado con #38 Fase 0** (decisión Debora post-Sesión 9) — mismo artefacto, se resuelve en la sesión de #38, no en 13 |
| 12 (loops de iteración) | **13** |
| 13 (guía UI/UX) | ✅ **Documentos recibidos** (ver bloque nuevo abajo) — tratamiento en **Sesión Frontend** |
| 14 (licencia Understand-Anything) | ✅ **Descartado** — decisión de Debora: no usar `Lum1104/Understand-Anything`. Componente `third-lum1104-knowledge-graph-v1.0.md` eliminado del repo. |
| 15 (soporte incidencias técnicas) | **Sesión 21** |
| 16 (análisis de riesgos validación Ciber/Arq/QA) | **Sesión 12** (parcial) + **Sesión 16** (pendiente). Sesión 12 construyó `apb-gov-ai-risk-gate-v1.0` — evalúa los 6 riesgos *específicos de uso de IA* de `proyecto.md` §3.5. **El alcance completo del punto #16 queda pendiente para Sesión 16:** informe de análisis de riesgos organizativo (incumplimientos de políticas APB, deuda técnica, ENS nivel alto) con procedimiento de excepciones corporativo, para validación por Ciberseguridad y Arquitectura — informe listo para que un humano decida si acepta el incumplimiento y qué plan de mitigación exige. Requiere: esbozo de contenido del informe que facilitará Debora + procedimiento corporativo de excepciones. |
| 17 (auditoría Playwright/apb-ai-skills) | ✅ **Sesión QA — CERRADA** (4 fusiones realizadas, apb-ai-skills deprecado) |
| 18 (comparar funcionalidad GitHub vs. zips previos) | **8** |
| 19 (checklist exhaustivo proyecto.md) | **8** |
| 20 (agente mockups UI para funcionales, añadido hoy) | ✅ **Resuelto, Sesión Frontend** — `apb-agent-ux-mockup-v1.0` creado |
| 21 (agente generación frontend para devs, añadido hoy) | ✅ **Resuelto, Sesión Frontend** — `apb-dev-devexpress-front-v1.0` actualizado + `apb-dev-devexpress-selector-v1.0` nuevo |
| 22 (análisis catálogo de componentes/sistema de diseño, añadido hoy) | **Sesión Design System** — confirmado por Debora (2026-06-24): múltiples equipos usan DevExtreme, componentes corporativos ya se copian entre proyectos. Repo GitHub propio `apb-design-system`; skills/agentes quedan en `APB-IA-FRAMEWORK`. |
| 23 (documentación por audiencias en Word, añadido hoy) | **14** — última sesión del plan |
| 24 (incorporar enfoque andrej-karpathy-skills, añadido hoy) | ✅ **Confirmado: Sesión 10** (decisión Debora post-Sesión 9) — resolver antes/dentro del briefing, no después en 13 |
| 25 (agente de deuda técnica/vulnerabilidades/remediación con Jira, añadido hoy) | ✅ **Confirmado: ampliación de Sesión 11** (decisión Debora post-Sesión 9) — alcance completo: deuda técnica, vulnerabilidades, dependencias obsoletas, rendimiento, incumplimientos de políticas APB |
| 26 (telemetría para KPIs proyecto.md §6, añadido hoy — checklist Sesión 8) | A determinar — relacionado con Sesión 14 |
| 31 (skill conversión universal a Markdown) | ✅ **Confirmado: Sesión 10** (decisión Debora post-Sesión 9), junto con #24 |
| 38 Fase 0 (catálogo de dominios) | ✅ **EJECUTADO (Sesión DDD, 2026-06-30)** — inventario `API_INVENTORY_APIM.md` recibido; 21 dominios de negocio `proposed` en `APB-DOMAIN-CATALOG/domains/`. Incluye #11. Pendiente: aprobación Arquitectura + fronteras de negocio. BCs diferidos a "DDD Fase BC" (requiere código) |
| 33 (skills/agentes de SQL) | **Sesión 21** |
| 34 (validación QA en flujos de despliegue) | **Sesión 21** — aplica a framework y aplicaciones APB; durante construcción del framework no se activa sobre el propio repo, pero se diseña para poder hacerlo. |
| 43 (aplicación retroactiva de política "Generado por IA" + "Validado por humano" a TODO el catálogo) | ✅ **CERRADA (Sesión 23, 2026-06-26)** — ver detalle en punto #43 abajo |

| 77 (orquestación y coreografía de agentes) | **Sesión de Análisis de Orquestación** (nueva, bloqueante: decisión runtime Debora + Plataforma) |

**Nota Sesión 8 (3ª corrección, mismo día):** Debora pidió separar la
Sesión QA (testing: Playwright, `apb-ai-skills`, solape con el framework)
de una **Sesión Frontend** propia e independiente (mockups, generación de
frontend para devs, catálogo de componentes/sistema de diseño). No son la
misma sesión aunque ambas usen la guía de estilo y DevExpress como insumo
común — QA es sobre pruebas, Frontend es sobre construcción de interfaz.

**Nota Sesión 8 (2ª corrección de proceso, mismo día):** Debora señaló un
segundo punto ausente del plan — documentación del framework en Word,
segmentada por audiencia (arquitectos, desarrolladores/analistas, dirección)
— que había sido hablado en sesiones/chats previos pero **nunca llegó a
registrarse en ningún documento del repo** (verificado: no aparece en
`proyecto.md` §7 "Entregables clave", que solo menciona "Guía de uso de
herramientas (Rovo, Copilot, etc.)" como único entregable documental, sin
segmentación por audiencia ni formato). A diferencia de los puntos 11-13,
este no es un caso de "anotado sin fecha" — es un caso de "nunca anotado".
Corregido ahora.

**Nota Sesión 8 — corrección de proceso:** los puntos 2, 6, 7, 8, 11 y 12
estaban marcados como "sin sesión asignada" al cierre de la Sesión 7.
Debora señaló que esto generaba la duda razonable de si de verdad estaban
en el plan. Se corrige asignándoles **Sesión 13** (sesión de cierre de
pendientes históricos), en vez de dejarlos en un cajón sin fecha.

## Sesión QA — ✅ CERRADA · Sesión Frontend — ✅ CERRADA

> ✅ **Ejecutadas** (QA post-Sesión 12; Frontend 2026-06-24). Registro completo
> movido a [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).
> Pendiente derivado que sigue vivo: **#22** (catálogo de componentes /
> design system más allá de la guía en PDF) — ver más abajo.

---

## Bloque añadido (continuación de Sesión 2)

1. **Estandarización Spec Driven Development / OpenSpec Kit**
   Verificar que el framework tiene todo lo necesario para trabajar con SDD
   basado en OpenSpec Kit (`https://github.com/Fission-AI/OpenSpec`).
   Valorar si GitHub Spec Kit aporta algo de valor adicional que incorporar
   o complementar.

2. **Guía de uso de agentes**
   Crear documento guía (`docs/AGENT_USAGE_GUIDE.md` o similar) explicando
   cómo usar los agentes del framework: cuándo invocar cada uno, qué
   esperar como input/output, flujo de aprobación humana asociado.

3. **Flujo/agente de ciclo completo legacy → SDD**
   Identificar si existe ya un flujo o agente que cubra el ciclo completo de
   una aplicación existente (legacy) a través de SDD de principio a fin, o
   si hay que construirlo. Candidatos a revisar: `apb-wf-legacy-onboarding-v1.0`,
   `apb-wf-spec-from-legacy-v1.0`, `apb-agent-modernization-v1.0`.

4. **Corrección de incumplimientos Sonar + PR automático**
   Verificar si el framework tiene lo necesario para: (a) corregir
   incumplimientos detectados por SonarQube/SonarCloud, y (b) preparar un
   Pull Request con esas correcciones. Candidatos a revisar:
   `apb-dev-sonar-clean-v1.0`, `apb-dev-pr-doc-v1.0`, provider `prov-sonar-v1.0`.

5. **(Ya en plan previo, se mantiene)** Agente/subagentes/skills para crear
   agentes/subagentes/skills siguiendo el estándar del framework,
   actualizando catálogo e índice automáticamente.
6. **(Ya en plan previo)** Verificar cobertura de plantillas de todos los
   tipos de componente + plantillas ofimáticas (Debora aportará ejemplos).
7. **(Ya en plan previo)** Mapa de interacción agentes/subagentes ↔ Jira:
   qué agente crea qué ticket y en qué momento (ej. tras OK de backlog,
   tras valoración COSMIC).
8. **(Ya en plan previo)** Entrenar valoración COSMIC con histórico real de
   horas de la organización, para informar conversión puntos↔horas de cara
   a facturación de proveedores por precio/hora.
9. **(Ya en plan previo)** Documentar cómo quedaron estructuradas las
   skills de terceros y el enriquecimiento que aplica APB sobre ellas.
10. **(Ya en plan previo)** Mecanismo de actualización automática del
    catálogo e índice del framework (relacionado con Sesión 3).

## Bloque añadido (2ª ronda, continuación de Sesión 2)

11. **Análisis basados en DDD + inventario global de dominios**
    Asegurar que los análisis del framework (discovery, arquitectura,
    modernización) se basan consistentemente en DDD. Construir un
    inventario global de dominios de negocio APB (distinto de
    `DOMAIN_REGISTRY.md`, que es de dominios *funcionales del framework*,
    no de dominios *de negocio APB*) con gobernanza definida y mecanismo de
    actualización automática — relacionado con el "mecanismo anti-duplicación
    de dominios" ya señalado como gap en `Plan_trabajo_correcciones_GitHub.md`
    punto 4.
12. **Necesidad de definir loops**
    Evaluar si el framework necesita bucles de iteración/retroalimentación
    explícitos (p. ej. reflexión iterativa ya cubierta parcialmente por
    `apb-dev-autocorrect-v1.0`, o loops de validación humana repetida) y
    dónde se formalizarían (¿a nivel de skill, de workflow, de agente?).
13. **Guía de estilo UI/UX como política/contexto corporativo** ✅
    **Documentos recibidos en Sesión 8** (ver "Sesión Frontend" arriba):
    `Guía_Estilos__Port_de_Barcelona__2022__v1.pdf`,
    `GISPEM__Guía_de_estilos.pdf`, `ManualUsuario_WidgetsLayout_v1.pdf`.
    Debe tratarse como política o contexto corporativo (ubicación candidata:
    `context/apb/policies/` o `context/apb/standards/`), y las skills de
    frontend (DevExpress, React/Stitch, frontend-integration) deben
    referenciarla y tenerla en cuenta. Tratamiento completo en Sesión
    Frontend.

## Bloque añadido (cierre de Sesión 7 / apertura Sesión 8)

14. **Verificar licencia de Understand-Anything** ❌ **SIGUE PENDIENTE — no
    resuelto pese a que la Sesión 9 ya cerró.**
    `third-lum1104-knowledge-graph-v1.0` quedó marcado como bloqueante para
    producción por licencia no verificada (ver `CONTINUIDAD_PROYECTO.md`
    §4). Se asignó a Sesión 9 ("resolver al revisar terceros"), pero la
    Sesión 9 cerró sin que este punto concreto se abordara — fue una
    omisión real, detectada en revisión post-Sesión QA. Sigue bloqueante
    para cualquier uso productivo del componente. Requiere acceso directo
    al repo `Lum1104/Understand-Anything` (o su fork
    `Egonex-AI/Understand-Anything`) para verificar el archivo LICENSE.

15. **Soporte a incidencias técnicas generalista**
    Agente/skill que ayude a diagnosticar y resolver incidencias técnicas de
    cualquier tipo (no solo desarrollo) a partir de descripción en lenguaje
    natural, capturas de pantalla/imágenes, o logs. Distinto de
    `apb-agent-sre-v1.0` (RCA formal post-incidente): este es soporte de
    primera línea, más amplio en alcance (no exclusivamente SRE/operación).

16. **Análisis de riesgos para validación de Ciberseguridad/Arquitectura/QA**
    Skill/agente que aplique las políticas corporativas APB y el
    procedimiento de gestión de excepciones/incumplimientos (`proyecto.md`
    §3.5 Gestión de Riesgos, §3.3 Gestión de Excepciones) y genere un informe
    de análisis de riesgos **listo para validación humana** — nunca
    auto-aprobado, el agente no puede aprobar sus propias excepciones
    (principio ya establecido en `proyecto.md` §3.6).

    **Decisión de Debora (Sesión 12, post-Sesión 11):** se construye como
    **skill transversal** (no agente propio, no subagente) — cualquier
    agente del framework la invoca antes de presentar su output a
    validación humana, en cualquiera de las 11 fases de la tabla de Puntos
    de Validación Obligatorios de `proyecto.md` §3.6. Cubre los 6 riesgos
    específicos del uso de IA listados en §3.5 (alucinaciones, información
    desactualizada, incumplimiento de estándares, dependencia excesiva,
    pérdida de conocimiento humano, código inseguro) — **distinto** de
    `apb-sec-risk-analysis-v1.0` (riesgos de seguridad de la información,
    ISO 27005/NIST/MAGERIT, sobre activos técnicos), que no se duplica.

    **Decisión de Debora (Sesión 12, post-Sesión 11):** la fila "Release" se
    resuelve como **"Release Manager / Arquitectura"** en ambos documentos.
    Aplicado en `SYSTEM.md` §6 (era "PMO / Operaciones / Arquitectura",
    corregido). **`proyecto.md` §3.6 no se pudo actualizar** — es un
    documento de proyecto en `/mnt/project/`, de solo lectura para Claude;
    Debora debe actualizar manualmente esa celda de "¿?" a "Release Manager
    / Arquitectura" en su copia del documento, o pedir a Claude que genere
    el texto exacto a copiar si lo prefiere.

17. **Auditoría de skills/agentes de testing Playwright** — ✅ EJECUTADO
    (Sesión QA). Detalle en [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).

18. **Comparación de funcionalidad: GitHub real vs. zip vs. zips de sesiones previas**
    Confirmar que no se ha perdido funcionalidad respecto al repo de GitHub
    (rama paralela, ver nota Sesión 7) ni respecto a zips de sesiones de
    trabajo previas que Debora guardó localmente — Sesión 8.

19. **Checklist exhaustivo de cobertura de `proyecto.md`**
    No limitarse a la tabla de skills de `Plan_trabajo_correcciones_GitHub.md`
    §5.1 (ya parcialmente desactualizada tras Sesión 1.5c) — verificar
    sistemáticamente cobertura de TODO `proyecto.md`: agentes (§4), KPIs
    (§6), entregables clave (§7), no solo skills (§5) — Sesión 8.

## Bloque añadido durante Sesión 8 (Sesión Frontend)

20. **Agente de mockups para perfiles funcionales** — ✅ EJECUTADO (Sesión
    Frontend: `apb-agent-ux-mockup-v1.0`). Detalle en [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).

21. **Agente/skill de generación de frontend para desarrolladores** — ✅
    EJECUTADO (Sesión Frontend: `apb-dev-devexpress-front-v1.0` +
    `apb-dev-devexpress-selector-v1.0`). Detalle en [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).

22. **Catálogo de componentes / sistema de diseño** — ✅ EJECUTADO (Sesión
    Design System, repo `APB-DESIGN-SYSTEM`). Detalle en [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).
    Pendiente derivado vivo: **#53** (prueba e2e Design System).

23. **Documentación del framework por audiencias, en formato Word**
    Generar documentación de `APB-IA-FRAMEWORK` (no de `apb-ai-skills`,
    confirmado por Debora en Sesión 8) segmentada en tres documentos
    distintos, cada uno como entregable Word (.docx):
    - **Arquitectos** que mantienen el framework de IA: cómo está
      estructurado, cómo se extiende, cómo funciona la gobernanza
      (`SCHEMA.md`, `GOVERNANCE.md`, validador, CI), cómo se crean nuevos
      componentes.
    - **Desarrolladores / analistas / perfiles de uso**: cómo invocar
      agentes y skills en el día a día, qué esperar de cada uno, flujo de
      aprobación humana — construye sobre `docs/sdd-getting-started.md`
      (Sesión 7) pero en formato Word y con más profundidad por rol.
    - **Dirección**: documento ejecutivo de alto nivel — qué es el
      framework, qué resuelve, estado de adopción, métricas (conectar con
      `proyecto.md` §3.7 Métricas y Seguimiento), sin detalle técnico.

    Última sesión del plan (Sesión 14) — se beneficia de que todas las
    sesiones anteriores (8-13) ya hayan cerrado gaps de cobertura, para no
    documentar un estado todavía incompleto del framework.

    **Estado 2026-06-27:** borradores Markdown ya disponibles en el repo:
    - `docs/guia-funcional.md` — guía para analistas, desarrolladores y
      jefes de proyecto (cubre: qué hace el framework, cómo empezar, reglas
      de uso, catálogo completo de agentes/workflows/skills, integración con
      las herramientas existentes, limitaciones actuales, ejemplos de uso
      real). Equivale al documento de audiencia "Desarrolladores / analistas".
    - `docs/manual-arquitectura.md` — manual para arquitectos y Tech Leads
      (cubre: mapa técnico de componentes, jerarquía, inventario por capa,
      infraestructura de gobierno/validación, gaps técnicos detectados,
      recomendaciones de infraestructura, componentes futuros recomendados,
      guía de extensibilidad, modelo de gobernanza, deuda técnica del propio
      framework). Equivale al documento de audiencia "Arquitectos".
    Ambos documentos están en estado draft (generados 2026-06-27) y
    **pendientes de validación humana por Arquitectura APB**. La Sesión 14
    los convierte a .docx y añade el documento de Dirección (que aún no
    existe en ningún formato).

24. **Incorporar el enfoque de `multica-ai/andrej-karpathy-skills`** — ✅
    EJECUTADO (Sesión 10/11): `apb-dev-simplicity-first-v1.0` +
    `apb-dev-surgical-changes-v1.0` creadas; principios 1 y 4 tratados como
    transversales. Detalle en [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).

25. **Agente/subagente de análisis de deuda técnica y remediación** — ✅
    EJECUTADO: `apb-agent-tech-debt-v1.0` creado (deuda, vulnerabilidades,
    dependencias, rendimiento, incumplimientos APB → plan priorizado +
    tickets Jira). Detalle en [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).

26. **Mecanismo de telemetría para los KPIs de `proyecto.md` §6**
    (añadido en Sesión 8, durante el checklist exhaustivo). El framework no
    tiene ningún mecanismo documentado para producir los datos que
    alimentarían las 7 dimensiones de KPIs de `proyecto.md` §6
    (Productividad, Calidad, Arquitectura, Uso de IA, Adopción, SDD,
    Automatización, Gestión de Riesgos) — son métricas de uso en
    producción, no componentes que se "construyen" como skill/agente, pero
    sin instrumentación no hay forma de medirlas. Evaluar: ¿campo de
    telemetría en `SCHEMA.md` (ej. `invocation_count`, `human_override_rate`
    por componente), skill de reporting dedicada, o ambos? Relacionado con
    `proyecto.md` §3.7 (Métricas y Seguimiento) y con la Sesión 14
    (documentación ejecutiva para Dirección, que necesitará estos datos
    para tener contenido real, no solo cualitativo). Sesión a determinar.

## Bloque añadido durante Sesión 9 (Debora, mismo día — volumen alto, pendiente de asignación fina de sesión)

> **Nota de proceso:** este bloque agrupa una petición muy densa recibida en
> un único mensaje. Se ha separado en sub-bloques temáticos para mantener
> trazabilidad. Ninguno de estos puntos se ejecuta en Sesión 9 — Sesión 9
> está acotada a §8 de `proyecto.md` (ya en curso). Se proponen sesiones
> candidatas, a confirmar con Debora.

### 27. Repos de terceros adicionales a evaluar (ampliación de §8)

Repos/skills mencionados por Debora para evaluar valor de incorporación,
**no confirmados todavía como §8 oficial** — pendiente de que Debora
confirme si se añaden formalmente a `proyecto.md` §8 o se tratan como lista
paralela. Aparcados para una futura sesión de terceros (¿Sesión 9-bis o
ampliación de Sesión 9?):

- `obra/superpowers` — ya incorporado parcialmente (`third-obra-superpowers-method-v1.0`,
  `third-obra-test-driven-development-v1.0` en Sesión 8); Debora pide
  revisar si falta algo, en concreto **"systematic debugging" de superpowers**
  (mencionado aparte) — verificar si es una skill distinta dentro del mismo
  repo no incorporada aún
- `context7` — gestor de contexto/documentación para LLMs, sin evaluar
- `excalidraw` — herramienta de diagramas; evaluar como posible integración
  para skills de arquitectura/diseño (no como skill en sí, sino posible
  MCP/herramienta)
- `ui ux pro max` — ya evaluado en Sesión 9 actual
  (`nextlevelbuilder/ui-ux-pro-max-skill`, ya incorporado como
  `third-nextlevel-ux-v1.0` en Sesión 8) — confirmar con Debora si se
  refiere a este mismo o a otro recurso
- ✅ **`impecable` — RESUELTO (post-Sesión 9):** `pbakaus/impeccable`
  ("The design language that makes your AI harness better at design").
  Sistema de detección de antipatrones de diseño/UI para harnesses de IA
  (Claude, Cursor, Copilot, Gemini, Codex), con CLI npm, reglas
  deterministas (44 detectores) + crítica vía LLM, hooks de post-edición.
  Verificado por búsqueda directa, repo activo. **DESCARTADO por decisión
  de Debora** — no se incorpora al catálogo.
- ✅ **`caveman` — RESUELTO (post-Sesión 9):** `JuliusBrussee/caveman`
  (~76.3k★ a fecha de verificación, no ~60k como estimó Debora). Skill que
  hace que el agente responda en estilo telegráfico para ahorrar tokens de
  salida — no es una capacidad técnica de desarrollo/arquitectura.
  **DESCARTADO por decisión de Debora** — no se incorpora al catálogo.
- ✅ **`kim barret` — RESUELTO (post-Sesión 9):** `realkimbarrett/*`
  (`avatar-extraction`, `offer-extraction`, `schwartz-awareness-mapper`,
  `mechanism-builder`, `headline-matrix`, `objection-crusher`, etc.) —
  skills de copywriting publicitario de respuesta directa, sin relación
  con el stack técnico de APB. **DESCARTADO por decisión de Debora** — no
  se incorpora al catálogo.
- ✅ **`color expert` — RESUELTO (post-Sesión 9):** `meodai/skill.color-expert`
  — ciencia del color (OKLCH/OKLAB, accesibilidad APCA/WCAG, paletas,
  teoría histórica). Único candidato consistente, conectaba con WCAG 2.1
  AA. **DESCARTADO por decisión de Debora** — no se incorpora al catálogo.
- ✅ **`web scrapper` / `unslot` — RESUELTOS (post-Sesión 9):**
  `D4Vinci/Scrapling` (framework de scraping) y `unslothai/unsloth`
  (~67.2k★, fine-tuning de LLMs locales — confirma que "unslot" era error
  de transcripción de "unsloth"). La skill de scraping del agregador
  `sickn33/antigravity-awesome-skills` (~32k★ del repo contenedor, ya en el
  catálogo APB) también se evaluó y queda descartada como incorporación
  puntual. **DESCARTADOS por decisión de Debora** — ninguno se incorpora
  al catálogo.
- **Cerrados sin identificación (decisión Debora, post-Sesión 9):**
  `pintarlos` y `brand guidelines` se descartan. A diferencia de los 6
  términos anteriores, estos dos **nunca llegaron a identificarse** como
  un repositorio concreto — no se evaluaron y se rechazaron, se cierran
  directamente sin resolución. Si en el futuro Debora recuerda a qué
  repo se refería, no es una reapertura de este punto sino una entrada
  nueva con su propia URL.
- `heygen-com/hyperframes` — sin evaluar, naturaleza a determinar (parece
  herramienta de vídeo/presentación, no típica de desarrollo — verificar
  relevancia real para APB)
- `mcpbuilder` de Anthropic — ya incorporado
  (`third-anthropic-mcp-builder-v1.0`, Sesión 8) — confirmar alcance pedido
- `frontend design` de Anthropic — ya incorporado parcialmente
  (`third-skills-sh-frontend-v1.0` vía skills.sh, Sesión 7/8); verificar si
  Debora se refiere a la misma fuente o a otra variante
- `graphify` — ya incorporado (`third-graphify-visual-v1.0`, Sesión 8)
- `unslot` — sin evaluar, nombre a confirmar (posible error de transcripción
  de "unsloth"? requiere aclaración de Debora)
- `pintarlos`, `impecable`, `caveman` — sin evaluar, nombres no
  identificados como repos conocidos — **requiere que Debora aporte
  URL/organización exacta**, no se puede buscar con garantías solo con el
  nombre
- `kim barret` — sin evaluar, posible referencia a una persona/autora de
  skills — **requiere URL o nombre de repositorio exacto**
- `brand guidelines`, `color expert` — sin evaluar, posible relación con
  Sesión Frontend (guía de estilo APB) más que con Sesión 9 de terceros —
  **requiere URL/fuente exacta**
- `pm skills` — posible solape con el dominio `pm` ya existente en el
  framework (creado en Sesión 1.5) — verificar si Debora se refiere a un
  repo de terceros concreto o al dominio propio
- `matt pocock` — ya incorporado parcialmente
  (`third-mattpocock-grill-prd-issues-v1.0`,
  `third-mattpocock-codebase-architecture-analysis-v1.0`, Sesión 7/8) —
  verificar si Debora pide revisar el resto del monorepo (~21 skills, solo
  2 cubiertas hasta ahora)
- `web scrapper` — sin evaluar, fuente/repo concreto no especificado —
  **requiere URL exacta**

> **Acción inmediata sin esperar a sesión propia:** para los puntos sin URL
> exacta (`pintarlos`, `impecable`, `caveman`, `kim barret`, `brand
> guidelines`, `color expert`, `web scrapper`, `unslot`), Claude no puede
> buscarlos con garantías de precisión por nombre solo — riesgo real de
> identificar el repo equivocado. **Debora debe aportar URL o organización
> de GitHub exacta** en la sesión donde se aborden, igual que se hizo con
> el resto de §8.

### 28. Arquitectura de comunicación entre agentes (pregunta conceptual, no construcción)

Debora pide explicación de cómo se enlazan los agentes entre sí y cómo
comparten información. **Esto es una pregunta a responder con el estado
real del framework, no una construcción nueva** — candidata a responder
en la misma Sesión 9 (o inmediatamente después) revisando `SYSTEM.md`,
`GOVERNANCE.md` y el campo `depends_on`/`consumed_by` de `SCHEMA.md`, en
vez de aparcarla a una sesión futura. Ver respuesta directa al final de
este mensaje.

### 29. Loop engineering — análisis de aplicabilidad

Relacionado con el punto #12 ya existente en este documento (mecanismos de
iteración) y con el punto #24 (Goal-Driven Execution de
andrej-karpathy-skills). Debora pide evaluar explícitamente si el
framework debe incorporar mecanismos de "loop engineering" (iteración
automática hasta criterio de éxito verificable). **No crear contenido
nuevo sin análisis previo** — candidata natural: Sesión 13, donde ya están
los puntos #12 y #24 relacionados. Se recomienda resolver los tres puntos
(#12, #24, #29) en la misma sesión por ser la misma decisión de fondo.

### 30. Integraciones de plataforma Microsoft

Integrar agentes del framework con:
- Microsoft Teams
- Envío de correo (mail)
- SharePoint
- Microsoft Copilot (también preguntado como pregunta de compatibilidad,
  ver punto #34)

Requiere decisión arquitectónica previa: ¿se construye como `provider`
nuevo por servicio (`prov-teams-v1.0`, `prov-sharepoint-v1.0`,
`prov-mail-v1.0`), siguiendo el patrón ya usado para otros providers
(`provider_type: action`, `access_mode`), o como capa de adaptador
(`adapters/`)? Candidata: sesión propia de integraciones, o ampliación de
Sesión 10 (meta-gobernanza) si se decide tratarlo como extensión de
plataforma transversal. **Pendiente de alcance con Debora**: ¿qué casos de
uso concretos? (¿notificación de aprobaciones humanas vía Teams/mail?
¿lectura de documentos desde SharePoint como input de skills?).

### 31. Skill de conversión universal a Markdown — ✅ EJECUTADO

> `apb-plat-doc-to-markdown-v1.0` creada (dominio `platform`): normaliza
> cualquier adjunto ofimático/PDF a Markdown antes de ser consumido por los
> componentes. Detalle en [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).

### 32. Mecanismo automático de actualización de inventario/documentación

Debora pide un mecanismo **automático** que garantice que inventario,
`INDEX.md`, `about`/`README`, y cualquier archivo del repo con referencias
cruzadas, además de la documentación funcional, se mantienen actualizados
sin intervención manual. **Esto ya existe parcialmente**:
`scripts/generate_catalog.py` regenera `CATALOG.md`/`INDEX.md`/
`DOMAIN_REGISTRY.md`, y el CI (`validate.yml`) bloquea PRs si hay drift
(Sesión 6, decisión explícita de Debora: sin auto-commit). **Lo que falta**
y debe analizarse: ¿"documentación funcional" se refiere a algo más amplio
que el catálogo técnico (ej. los documentos Word de Sesión 14, o
descripciones funcionales de negocio)? Si es así, requiere mecanismo nuevo
distinto del validador actual. Sesión candidata: ampliación de Sesión 10 o
de Sesión 14, según se aclare el alcance exacto de "documentación
funcional" con Debora.

### 33. Skills/agentes de SQL

Petición de skill/agente/subagente para: generar queries SQL, revisarlas,
optimizarlas, detectar errores, revisar PRs de SQL, documentar PRs de SQL.
Sin componente equivalente detectado hasta ahora en el framework (dominio
`development` tiene skills genéricas de revisión de código, no
específicas de SQL/Azure SQL). Candidata: dominio `development`, sesión a
determinar — posible ampliación de Sesión 11 (que ya cubre Sonar/calidad de
código) o sesión propia si el volumen de sub-tareas SQL lo justifica.

### 34. Validación QA en flujos de despliegue (incluyendo Markdown)

Los flujos de despliegue (CI/CD vía Jenkins + GitHub Actions, estándar
APB) deben validar cumplimiento de QA antes de desplegar, **incluyendo
despliegues de contenido Markdown** (no solo código). Relacionado con el
CI ya existente (`validate.yml`, Sesión 6) pero ese CI valida el propio
repositorio del framework, no los despliegues de las aplicaciones que el
framework ayuda a construir — **aclarar con Debora** si se refiere a (a)
extender la validación QA del framework a más artefactos, o (b) un
principio para los pipelines de las aplicaciones APB en general (fuera del
propio framework). Sesión candidata: Sesión 11 o Sesión QA, según se
aclare el alcance.

### 35. Documento de uso del framework: Claude web/cliente Windows + compatibilidad Copilot/Rovo

Debora pide:
(a) explicación + documento de cómo usar este framework desde Claude (web
o cliente Windows)
(b) si el framework puede usarse desde Microsoft Copilot o Rovo de
Atlassian, y en caso afirmativo, cómo

**Esto solapa directamente con el punto #2 ya existente** ("Guía de uso de
agentes", asignado a Sesión 13) y con `proyecto.md` §7 ("Guía de uso de
herramientas (Rovo, Copilot, etc.)" ya listada como entregable clave). No
es contenido nuevo de alcance, sino una **priorización**: Debora lo pide
ahora, no en Sesión 13. Requiere decisión: ¿adelantamos este documento a
sesión propia antes de la 13, o se mantiene en el plan original? Nota
técnica importante a verificar antes de prometer nada: el framework está
diseñado primariamente para **Claude y GitHub Copilot** (`runtime: list de
["copilot", "claude"]` en `SCHEMA.md` §3.2); su uso desde Microsoft Copilot
o Rovo dependería de si esas plataformas soportan consumo de
agentes/skills en formato Markdown+YAML estándar de Anthropic Skills o
equivalente — **no confirmado, requiere investigación dedicada antes de
responder con certeza**.

### 36. Agentes de licitación (pendiente de detalle)

Debora anuncia que necesitará 1-2 agentes para crear y revisar
documentación relacionada con una licitación (procedimiento de
contratación pública LCSP), **pero aún no ha dado los detalles**. No se
puede definir alcance, dominio, ni sesión hasta recibir esa información.
Marcado como **pendiente de briefing**, sin sesión asignada todavía.

### 37. Agente de documentación funcional/spec desde histórico (app existente)

Agente que, a partir de documentación existente + histórico de tickets
Jira de una aplicación ya en producción, genere documentación funcional y
especificaciones (spec) de esa aplicación. **Solape parcial detectado**
con `apb-agent-documentation-v1.0` (genera ADRs, Swagger/OpenAPI, manuales)
y `apb-agent-spec-engineer-v1.0` (genera specs, pero parte del output de un
Business Analyst humano, no de reconstrucción desde histórico). Ninguno de
los dos parte de "Jira histórico + docs existentes" como fuente primaria
de reconstrucción retroactiva — éste sería un caso de uso distinto
(reconstrucción/discovery inverso, no especificación hacia delante).
Candidata: nuevo agente o subagente de `apb-agent-spec-engineer-v1.0`,
dominio `discovery` o `pm`. Sesión a determinar.

### 38bis. Unificación confirmada con punto #11 (decisión Debora, post-Sesión 9)

**Decisión de Debora:** el punto #11 ("inventario global de dominios de
negocio APB") y el punto #38 Fase 0 ("catálogo corporativo de dominios" a
partir del listado de APIs que aportará Debora) **son el mismo artefacto**.
No se construyen por separado. Cuando se aborde la sesión de #38 (Fase 0),
se considera resuelto también el punto #11 — no requiere sesión propia
adicional en el bloque de Sesión 13. Actualizar la tabla de mapeo: #11 deja
de estar asignado a Sesión 13 en solitario y pasa a resolverse junto con
#38 Fase 0.

### 38. Agente de descomposición de monolitos a microservicios (DDD + eventos)

Agente que analice un monolito existente y proponga:
- Descomposición en microservicios orientados a dominios (DDD)
- Diseño orientado a eventos, alineado con el **catálogo corporativo de
  dominios**
- Estrategia de migración hacia la arquitectura objetivo
- Creación de tickets Jira
- Documentación funcional y specs asociadas

**Decisión de Debora (Sesión 9, confirmada):** no existe hoy un catálogo
corporativo de dominios en APB. **Debe resolverlo el propio framework de
IA, no asumirse como insumo externo ya disponible.** Mecanismo previsto:
Debora aportará una lista de APIs existentes (sin garantía de que sus
agrupaciones actuales sean dominios correctos) como **borrador de
entrada**; un agente analizará esa lista y propondrá si los dominios
detectados son correctos tal cual, o si conviene unificar o dividir
algunos. Esto reordena el propio agente del punto #38 en dos fases
diferenciadas, no una sola:

1. **Fase 0 — Construcción del catálogo de dominios** (nueva, no estaba
   contemplada originalmente): a partir del listado de APIs que aportará
   Debora, el agente identifica agrupaciones candidatas a dominio/bounded
   context, señala posibles solapamientos, fragmentaciones excesivas, o
   APIs sin dominio claro, y propone una versión depurada del catálogo
   para validación humana (`SYSTEM.md` §6, validación de "Dominios,
   bounded contexts, eventos de negocio" ya exige revisión de
   Arquitecto/Tech Lead — coherente con el framework existente, no
   requiere excepción).
2. **Fase 1 — Descomposición de monolitos** (alcance original del punto
   #38): una vez exista el catálogo de dominios (fruto de la Fase 0, no
   antes), el agente de descomposición lo usa como referencia para
   alinear la propuesta de microservicios/eventos a dominios ya validados,
   en vez de inventar agrupaciones ad-hoc por monolito analizado.

**Implicación de secuenciación:** la Fase 0 debe completarse, al menos en
una primera iteración validada por Arquitectura, antes de que la Fase 1
pueda producir resultados alineados de forma consistente entre distintos
monolitos. Si se analizan varios monolitos sin un catálogo de dominios
común ya estable, cada análisis corre el riesgo de proponer una
taxonomía de dominios distinta e incompatible entre sí.

**Primer input real disponible (2026-06-30):** Azure API Manager en
`https://apipre.portdebarcelona.cat` es la fuente de verdad de las APIs DOCKS
publicadas. Primeras 3 APIs confirmadas: `APB.API.RESPONSIBLE`, `APB.API.ROSS`,
`APB.API.SIG` — función y dominio TBD, pendiente de análisis DDD.
La knowledge base (`APB_KNOWLEDGE_BASE.md §4.4`) ya documenta 42+ APIs ARQ
adicionales — este listado combinado es el punto de partida para Fase 0.
**Restricción explícita de Debora (2026-06-30):** los dominios actuales NO están
bien definidos — el agente de análisis debe proponer la taxonomía correcta, no
asumir que la agrupación actual de la knowledge base es válida. Su misión es
detectar solapamientos, repeticiones, novedades y proponer bounded contexts.

Sigue siendo, en conjunto (Fase 0 + Fase 1), un agente de alcance
considerable que combina: análisis arquitectónico
(`apb-disc-ddd-legacy-v1.0` ya existente como insumo), diseño event-driven
(`apb-arch-event-driven-v1.0`, y las skills de terceros incorporadas en
Sesión 9: `third-sickn33-saga-orchestration-v1.0`,
`third-sickn33-event-store-design-v1.0`,
`third-sickn33-ddd-context-mapping-v1.0` — esta última especialmente
relevante para la Fase 0, dado que cubre exactamente el mapeo de
relaciones entre contextos/dominios), gestión de Jira, y generación de
documentación. Candidato natural a **agente orquestador nuevo** que
consuma varias skills/subagentes existentes en vez de construirse desde
cero. Sesión candidata: sesión propia (volumen alto, ahora mayor por la
Fase 0 añadida) o ampliación de Sesión 13.

### 39. Agente de dashboards/métricas (Power BI, Grafana, Prometheus)

Agente que, a partir de petición en lenguaje natural o de una spec, genere
dashboards y métricas en Power BI, Grafana y Prometheus. Sin componente
equivalente detectado en el framework actual (existe `apb-agent-finops-v1.0`
para costes, pero no para dashboards/observabilidad general). Dominio
candidato: `platform` u `operation`. Sesión a determinar.

### 40. Agente de propuesta y generación de logs para dashboards

Agente complementario al #39: a partir de los dashboards/métricas
definidos, propone qué logs deben incorporarse a las aplicaciones para
alimentarlos, y ayuda a generarlos (instrumentación de logging). Trabajaría
en tándem con el #39. Dominio candidato: `platform` u `operation`, mismo
agente extendido o subagente dedicado — a decidir según volumen real al
construir el #39.

### 41. Análisis: ¿algún agente no debería requerir revisión humana? + orquestación real entre agentes

(Añadido por Debora tras la explicación del punto #28 sobre cómo se
enlazan los agentes hoy.) Dos preguntas relacionadas pero distintas, ambas
pendientes de análisis, no de implementación directa:

1. **¿Hay algún agente candidato a operar sin revisión humana
   obligatoria?** Hoy `SYSTEM.md` §5.1 fija Nivel 1 (revisión humana
   previa obligatoria) como mínimo para análisis, arquitectura, seguridad,
   despliegue y gobierno, y el Nivel por defecto es 1 para todo lo demás.
   Solo "tests automatizados de regresión" puede operar en Nivel 3
   (auditoría periódica, no aprobación previa) si están previamente
   autorizados — y el Nivel 4 nunca se activa sin aprobación explícita de
   Arquitectura y Ciberseguridad. Analizar: ¿qué agentes/skills concretos
   del catálogo actual (217 componentes) son candidatos reales a Nivel 2/3
   sin romper el principio `SYSTEM.md` §2.1 regla 2 ("ningún agente puede
   aprobar sus propios resultados")? Candidatos a evaluar primero: skills
   de solo lectura/diagnóstico (auditoría, detección de drift, generación
   de informes) frente a skills que escriben código o tocan producción.

2. **Mecanismo real de orquestación entre agentes** (más allá del enlace
   declarativo por referencia de ID explicado en el punto #28). Hoy el
   "enlace" es textual (`agents:`, `skills:`, `subagents:` en frontmatter)
   y la información se comparte vía artefactos en Git/Jira entre sesiones
   — no hay paso de mensajes en tiempo real ni un orquestador que encadene
   llamadas automáticamente. Analizar si conviene introducir una capa de
   orquestación real (ej. un `provider` o `adapter` que ejecute la cadena
   `workflow → agent → skill` sin intervención manual entre cada paso,
   dentro de los límites de autonomía ya definidos) y cómo encajaría con
   los `human_checkpoints` obligatorios de cada workflow sin romperlos.

**Relación directa con puntos ya existentes:** este punto es la otra cara
de la moneda del #29 (loop engineering) y del #24 (Goal-Driven Execution) —
los tres tratan, desde ángulos distintos, hasta qué punto el framework
puede/debe reducir la intervención humana sin comprometer
`SYSTEM.md` §2.1. **Recomendación: resolver #24, #28 (ya respondido),
#29 y #41 en la misma sesión** (candidata: Sesión 13), porque son la misma
decisión de fondo vista desde ángulos distintos, y decidirlos por separado
arriesga conclusiones contradictorias entre sí.

---

### 42. Comillas mal cerradas en sección "Dependencias" ✅ **RESUELTO**

> ✅ Corregido (19 archivos, preparación de Sesión 11). Registro completo en
> [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).

---

### 43. Aplicación retroactiva de "Generado por IA" + "Validado por humano" a todo el catálogo

**Decisión de Debora (post-Sesión 11):** la política de identificación explícita —
`SYSTEM.md` §7.2, todo artefacto debe declarar visiblemente que fue generado por IA y qué
humano lo validó — se aplicará a la **totalidad** del catálogo existente (~225 componentes a
fecha de Sesión 11, número crecerá con cada sesión futura), pero como **última fase del
plan**, después de que todas las sesiones de construcción/remediación (8 a 14) hayan
cerrado.

**Razón de la secuenciación:** aplicar esto antes sería trabajo desechable — cada sesión
futura (12, 13, 14, Sesión QA, Sesión Frontend, #38, etc.) sigue creando o modificando
componentes. Aplicar la identificación al final, una sola vez sobre el catálogo ya estable,
evita repetir el trabajo sobre los mismos archivos varias veces.

**Pendiente de definir cuando se aborde esta fase:**
- ¿Quién es "el humano validador" para componentes creados en sesiones donde Debora ya dio
  el OK conversacional (¿se usa su nombre retroactivamente, o queda "pendiente" hasta una
  revisión formal explícita por componente?) — Debora decide el criterio antes de ejecutar.
- Si el propio `apb-agent-meta-builder-v1.0` (Sesión 10) se usa para aplicar esto de forma
  sistemática (candidato natural, ya que su función es generar/mantener componentes
  conforme al esquema), o se hace como tarea de script dedicado.
- Si esta fase también cubre los componentes de terceros (`skills/third_party/`,
  `wrappers/`) o se limita a los `apb-owned`, dado que los de terceros ya tienen su propio
  campo `source_repo`/`source_license` que en cierto modo ya identifica el origen no-APB.

**No bloquea ninguna sesión intermedia** — los componentes que se han creado en Sesiones 10
y 11 (`apb-dev-simplicity-first-v1.0`, `apb-dev-surgical-changes-v1.0`,
`apb-plat-doc-to-markdown-v1.0`, `apb-agent-meta-builder-v1.0`,
`apb-ops-dependency-audit-v1.0`, `apb-ops-perf-bottleneck-v1.0`,
`apb-ops-debt-remediation-plan-v1.0`, `apb-agent-tech-debt-v1.0`) ya tienen el bloque
aplicado individualmente como precedente — la fase #43 es para el resto del catálogo
retroactivamente, de una sola vez.

### 44. Plantilla `context/apb/templates/AGENT.md` desactualizada respecto a `SCHEMA.md`

**Hallazgo detectado durante Sesión 10, nunca registrado formalmente como tarea hasta esta
revisión post-Sesión QA** (Debora detectó que la bitácora y el plan tenían huecos y pidió
verificación exhaustiva). `context/apb/templates/AGENT.md` usa un formato antiguo (metadatos
en blockquote `> **ID:**`) que **ya no es válido** según `SCHEMA.md` §1 — solo YAML
frontmatter es válido para cualquier componente. Los agentes reales del repo (`agents/*.md`)
usan correctamente YAML frontmatter; solo la plantilla de referencia quedó desactualizada,
probablemente de una etapa anterior a la Sesión 0/2 (normalización de frontmatter).

**Riesgo si no se corrige:** cualquier persona o agente que use esa plantilla como base para
crear un agente nuevo (en vez de copiar el formato real observado en `agents/*.md`)
generaría un componente inválido que fallaría el validador. No bloquea nada hoy porque
`apb-agent-meta-builder-v1.0` (Sesión 10) ya fue instruido para seguir el formato real, no la
plantilla — pero la plantilla en sí sigue siendo una trampa para cualquier humano que la use
directamente. **Sesión a determinar** — corrección sencilla (reescribir
`templates/AGENT.md` con YAML frontmatter, replicando la estructura de `templates/SKILL_APB.md`
que sí está correcta), candidata a tarea trivial dentro de cualquier sesión de mantenimiento,
o a resolverse junto con la Sesión 13.

### 45. Carpeta `skills/_spec-driven/` de `apb-ai-skills` — sin decisión, solo mencionada

**Hallazgo de la Sesión QA, documentado como dato pero nunca convertido en tarea con
decisión pendiente** (mismo patrón de hueco que el #44). Al auditar `apb-ai-skills.zip` se
encontró una carpeta `skills/_spec-driven/` con 3 skills (`spec-to-api-contract`,
`spec-to-e2e-flows`, `spec-to-test-plan`) no contabilizadas en la descripción original del
repo ("10 skills APB + 10 externas + agente + 5 subagentes"). Se documentó su existencia en
`CONTINUIDAD_PROYECTO.md` §13.1, pero **nunca se decidió qué hacer con ellas** — a diferencia
de las 10 skills APB, que sí se cruzaron una por una contra el catálogo de
`APB-IA-FRAMEWORK` (resultando en las 4 fusiones de la Sesión QA), estas 3 nunca se evaluaron
individualmente.

**Pregunta pendiente para Debora:** ¿se evalúan estas 3 skills para posible fusión (mismo
tratamiento que las 10 ya cruzadas), o se consideran cubiertas por la decisión general de
deprecar `apb-ai-skills` y no requieren evaluación individual? Sesión a determinar — no
bloquea nada del plan actual, pero queda abierta hasta que Debora decida el criterio.

---

**Resumen de acción inmediata para Debora:** Punto #27 **cerrado en su
totalidad** (post-Sesión 9). De los 8 términos originales: 6 se
identificaron y se descartaron tras evaluación (`impecable`, `caveman`,
`kim barret`, `color expert`, `web scrapper`, `unslot`); 2 se cierran sin
haber llegado a identificarse (`pintarlos`, `brand guidelines`). Ninguno
se incorpora al catálogo. No queda ninguna acción pendiente sobre este
punto.
- Punto #36 (licitación): **pendiente de briefing** de Debora.
- Punto #38 (Fase 0, catálogo de dominios): **pendiente de que Debora
  aporte el listado de APIs** cuando se vaya a abordar esta sesión —
  confirmado que no existe catálogo corporativo previo; lo construirá el
  propio framework a partir de ese listado.
- Punto #35: decidir si se prioriza sobre el orden original del plan
  (estaba en Sesión 13).

> **Nota de proceso (Sesión 9):** Debora confirmó que las dependencias
> abiertas de cada punto (URLs, briefings, listados) se resolverán en el
> momento de abordar la sesión específica correspondiente, no antes. Este
> resumen se mantiene como recordatorio de qué falta por punto, sin
> bloquear el resto del plan.

---

## Plan de sesiones completo — confirmado por Debora (2026-06-24)

> Decisión: a partir de ahora todo componente nuevo que se cree en cualquier sesión
> sigue el protocolo de `apb-agent-meta-builder-v1.0`: discovery previo en
> `CATALOG.md`/`INDEX.md`, YAML frontmatter conforme a `SCHEMA.md`, ejecución de
> `validate_repo.py --strict` y regeneración de catálogo. Claude Code actúa como
> ejecutor del protocolo.

### Sesiones pendientes en orden de ejecución

| Sesión | Tema principal | Puntos del plan | Bloqueante |
|---|---|---|---|
| ~~**Frontend**~~ | ~~Mockups para perfiles funcionales + generación de frontend para devs~~ | ~~#20, #21~~ | ✅ CERRADA |
| ~~**Design System**~~ | ~~Análisis y construcción del sistema de diseño APB sobre DevExtreme: tokens CSS, componentes compuestos corporativos (cabecera, menú, tarjetas de dominio), guía de estilos integrada. Repo GitHub propio `apb-design-system`.~~ | ~~#22~~ | ✅ CERRADA (2026-06-26, v1.3.0) — repo APB-DESIGN-SYSTEM creado. Skills y agentes de diseño en APB-IA-FRAMEWORK; artefactos CSS/JS en repo propio. |
| ~~**15**~~ | ~~Integraciones Microsoft (Teams, mail, SharePoint) + cierre de gaps de otras plataformas IA: Rovo (Forge App skeleton + guía activación) y M365 Copilot (OpenAPI spec + manifest plugin). Claude web y GitHub Copilot VS Code ya funcionan hoy sin desarrollo adicional.~~ | ~~#30, #35, #47~~ | ✅ CERRADA (2026-06-26) — artefactos generados: `openapi/apb-framework-api.yaml`, `openapi/ai-plugin.json`, `forge/manifest.yml` + `forge/src/`, `docs/rovo-getting-started.md`, `docs/HANDOFF_SESION15_INTEGRACIONES.md`. Pendiente de equipo APB (Plataforma + Desarrollo + Admins): ver handoff. |
| ~~**16**~~ | ~~Informe de análisis de riesgos organizativo (ENS alto, políticas APB, deuda técnica, excepciones) para validación Ciberseguridad/Arquitectura~~ | ~~#16 (alcance completo, no el parcial de Sesión 12)~~ | ✅ CERRADA (2026-06-24) — `apb-gov-org-risk-report-v1.0` (v1.2.0) alineado con `PROCEDURE_NONCOMPLIANCE_MANAGEMENT_v1.0` + `PROCEDURE_RISK_EVALUATION`. Análisis multidimensional (ENS, ISO 27001, NIST, OWASP, RGPD, LCSP, WCAG), recomendación explícita APROBAR/DENEGAR/ESCALAR, plan de mitigación, plantilla de informe con firmas. |
| ~~**17**~~ | ~~Observabilidad: dashboards Power BI/Grafana/Prometheus + logging + telemetría de KPIs del framework~~ | ~~#26, #39, #40~~ | ✅ CERRADA — ver punto #46 para pendiente de telemetría en chat |
| **13** | Cierre de pendientes históricos: guía de uso de agentes, plantillas, mapa Jira, COSMIC, loops, autonomía de agentes, plantilla AGENT.md | #2, #6, #7, #8, #12, #29, #41, #44, #48 | ✅ PARCIAL (2026-06-26, 7/10 puntos): #2 ✅ #7 ✅ #12 ✅ #29 ✅ #41 ✅ #44 ✅ #48 ✅. Bloqueados: #6 (ejemplos Word/Excel de Debora), #8 (horas históricas COSMIC), #52 (email Arquitectura). |
| ~~**18**~~ | ~~DDD: catálogo corporativo de dominios (Fase 0) + descomposición de monolitos (Fase 1) + spec desde histórico Jira~~ | ~~#11/#38 Fase 0, #38 Fase 1, #37~~ | ✅ CERRADA (Sesión 18, 2026-06-25) — repo apb-domain-catalog creado (github.com/apb-dmartin/APB-DOMAIN-CATALOG), apb-agent-ddd-v1.0 + 5 subagentes (code/db/doc/spec/interview), submodule integrado en APB-IA-FRAMEWORK. Fase 1 (descomposición monolitos) → pendiente sesión futura. |
| **19** | Terceros pendientes de §8 + evaluación `_spec-driven` de `apb-ai-skills` | #27 (items abiertos), #45 | Items de #27 sin URL requieren que Debora las aporte |
| **20** | Agentes de licitación (LCSP) | #36 | **Pendiente de briefing de Debora** |
| **14** | Documentación Word por audiencias (arquitectos, devs/analistas, dirección) + mecanismo de actualización de documentación funcional | #23, #32 | ⚠️ PARCIAL (2026-06-27): borradores Markdown disponibles (`docs/guia-funcional.md` y `docs/manual-arquitectura.md`). Pendiente: conversión a .docx + documento de Dirección |
| ~~**#43**~~ | ~~Aplicación retroactiva "Generado por IA + Validado por humano" a todo el catálogo~~ | ~~#43~~ | ✅ CERRADA (Sesión 23, 2026-06-26) — 129/129 skills apb-owned marcadas con `## Marcado IA obligatorio (POLICY_AI_USAGE §6)`. Estándar canónico: `context/apb/standards/AI_MARKING_STANDARD.md`. Mecanismos preventivos: check #13 en `validate_repo.py` (ERROR si falta la sección), sección en templates `SKILL_APB.md` y `AGENT.md`, `CLAUDE.md` en raíz del repo. |

| ~~**21**~~ | ~~SQL + soporte de primera línea de incidencias técnicas + QA del propio framework~~ | ~~#15, #33, #34, #50~~ | ✅ CERRADA (2026-06-29, Enriquecimiento D) — `apb-agent-db-v1.0` creado (skills sql-gen/review/fix + subagente sql), `apb-dev-sql-review-v1.0` añadido a implementer. M1-M6 del backlog resueltos: 2 skills orchestration + skill WCAG + agente PM + diferenciación STRIDE/ISO27005 + verificación UTF-8. Total: 5 nuevos componentes + 14 modificaciones. |
| ~~**22 (#47bis)**~~ | ~~Refactorización de taxonomía de carpetas skills/ — consolidar 13 carpetas de un solo archivo en dominios correctos~~ | ~~#47bis~~ | ✅ CERRADA (2026-06-26) — 13 carpetas consolidadas, archivos movidos a dominios correctos, nomenclatura auditada (259 componentes verificados), 1 violación corregida (`apb-skill-` → `apb-design-`), 12 terceros reorganizados en subcarpetas por autor. |
| **22 (#49)** | Propagación automática Design System (decisión distribución: npm / Git submodule / CDN) | #49 | **Requiere decisión de Debora sobre mecanismo de distribución** |
| ~~**Sesión 18 cont. (#54)**~~ | ~~Entrevista portuaria + verificación de dominio + actualización repo dominios~~ | ~~#54~~ | ✅ CERRADA (2026-06-26) — `apb-sub-ddd-interview-v1.0` v1.3.0: (A) Banco A portuario (buques, escalas, consignatario, GISPEM, PORTIC…); (B) Banco B corporativo (RRHH, viajes, contratación LCSP, adm. electrónica, finanzas, jurídico); (C) Fase 1-INT integración entre sistemas (flujo de datos, trigger, frecuencia, fallo, patrón ACL/Published Language/Shared Kernel/event-driven); (D) Fase 1-EVO evolutivos (revisión de lo existente, clasifica en extensión/nuevo BC/deuda técnica/breaking change); Fase 5 verificación APB-DOMAIN-CATALOG; Fase 6 generación artefacto `domain.md`. |
| ~~**Harness**~~ | ~~Harness Engineering agnóstico de LLM: 5 subsistemas, System of Record + ACID, Feature Lists + Pass-State Gating, validación 3 capas, Clean State Handoff. Gobernanza + scaffolding + checks nuevos en `validate_repo.py`~~ | ~~#83~~ | ✅ CERRADA (2026-07-02, sesión combinada con #78) — SYSTEM.md §10 + GOVERNANCE.md §8 + `repo-scaffold/harness-ready/` + check #19 |
| ~~**Estándar Prompting**~~ | ~~Estándar de estructura de prompt para todos los componentes (razonar→plan→ejecutar, objetivo, autocrítica, qué-NO-hacer, ejemplo E/S, separación SISTEMA/USUARIO) + retrofit + check en validador~~ | ~~#78~~ | ✅ CERRADA (2026-07-02, sesión combinada con #83) — `PROMPTING_STANDARD.md` + 6 plantillas + retrofit 244 componentes + check #18 en ERROR |
| **QA-2** | Metodología y plantilla de planes de pruebas (Rovo→Copilot, trazabilidad, histórico, gobernanza, no-regresión rendimiento) + navegación agéntica para pruebas funcionales | #82, #84 | **Bloqueante: ejemplo real + planes preliminares de Debora** |
| **19 (ampliada)** | Terceros #79 (MCP Builder alcance, cybersecurity skills, "Fine Skills") + Obsidian como capa de navegación | #79, #81 | "Fine Skills" requiere URL de Debora |
| **Memoria/Runtime** | Memoria corporativa del framework (contexto/histórico/aprendizaje/persistencia): arquitectura Git+`PROGRESS.md` base + LightRAG/mem0 semántica | #80 | Ligada a decisión de runtime (misma que #77) |

### Decisiones tomadas sobre puntos pendientes (2026-06-24)

- **#34 (validación QA en despliegues):** aplica a todo — framework y aplicaciones APB. De momento, durante la fase de construcción del framework, no se aplica al propio repo; se diseña de forma que pueda activarse también sobre él en el futuro. Se incluye en Sesión 21 junto con #15 y #33.
- **#15 y #33:** sesión propia (Sesión 21), no absorbidos en Sesión 13.
- **#47 (gaps plataformas IA) y #47bis (taxonomía carpetas):** añadidos post-Sesión 17 (2026-06-25) — ver detalle abajo. Asignados a Sesiones 15 y 22 respectivamente.
- **#48 (plantillas de arq + DevExpress):** asignado a Sesión 13 junto con #44.
- **#50 (QA del propio framework):** asignado a Sesión 21 junto con #15, #33, #34.
- **#52 (cambio contacto Arq → mail Jira):** tarea de mantenimiento en Sesión 13, pendiente de que Debora facilite la dirección.

---

### 46. Telemetría automática para usuarios de chat sin commit (pendiente Sesión 17)

**Detectado durante Sesión 17 como gap no resoluble en el alcance de la sesión.**

Los usuarios funcionales que solo interactúan por chat (Claude.ai, GitHub Copilot chat) y nunca hacen commit no están cubiertos por ninguno de los tres mecanismos de telemetría construidos en Sesión 17:
- Mecanismo 1 (Claude Code automático): solo aplica si el runtime es Claude Code.
- Mecanismo 2 (script manual): requiere terminal, inaplicable para usuarios funcionales.
- Mecanismo 3 (GitHub Actions / JSONL): requiere que alguien commitee al repo.

**La cobertura automática para este perfil requiere instrumentar la plataforma de chat**, lo cual está fuera del alcance del framework de Markdown.

**Opciones a evaluar en sesión futura:**
- Proxy de invocación (Azure API Management delante del endpoint de Claude/Copilot) que capture la llamada y emita telemetría antes de pasarla al LLM.
- Wrapper de interfaz que envuelva la sesión de chat y registre eventos de uso.
- Aceptar cobertura parcial y documentarlo en el informe ejecutivo de KPIs.

**Sesión a determinar.** No bloquea ninguna sesión del plan actual — la telemetría de desarrolladores con Claude Code ya es funcional y cubre el caso de uso principal.

---

### 47. Cierre de gaps de uso desde otras plataformas IA (Sesión 15)

**Detectado durante Sesión 17 al anticipar respuesta para pruebas de Debora (2026-06-25).**

El framework tiene adapters para cuatro runtimes, pero con distinto grado de completitud:

| Plataforma | Estado hoy | Gap |
|---|---|---|
| Claude (web / Claude Code) | ✅ Usable hoy | Ninguno — adjuntar .md al chat o usar Claude Code directamente |
| GitHub Copilot (VS Code) | ✅ Usable hoy | `#file:agents/xxx.md` en el chat de Copilot |
| Rovo (Atlassian) | ⚠️ Adapter definido, no desplegable | Falta: Forge App skeleton (manifest + estructura) + `docs/rovo-getting-started.md` |
| M365 Copilot (Teams/Word/Outlook) | ⚠️ Adapter definido, no desplegable | Falta: OpenAPI 3.0 spec de los endpoints APB + manifest `ai-plugin.json` |

**Trabajo concreto para Sesión 15:**

**Rovo:**
- Generar el esqueleto de la Forge App (`forge/manifest.yml` + estructura de carpetas) lista para que el equipo de desarrollo la complete y publique en el tenant Atlassian APB.
- Crear `docs/rovo-getting-started.md` con guía de activación paso a paso.
- Prerrequisito operativo (no de framework): tenant Atlassian con Rovo activado (previsto julio 2026).

**M365 Copilot:**
- Generar la especificación OpenAPI 3.0 (`openapi/apb-framework-api.yaml`) de los endpoints que M365 Copilot consumiría como API Plugin.
- Generar el manifest del plugin (`openapi/ai-plugin.json`).
- Nota explícita: el backend que sirve esos endpoints (Azure APIM o Azure Function) es infraestructura de plataforma, no competencia del framework — el framework entrega la spec, no el backend desplegado.

**Lo que NO se construye en Sesión 15:** backends reales (Forge App desplegada, Azure APIM aprovisionado) — eso es trabajo de plataforma APB.

---

### 47bis. Refactorización de taxonomía de carpetas de skills (Sesión 22)

**Detectado durante Sesión 17 al revisar escalabilidad hacia IT-general y negocio (2026-06-25).**

**Problema actual:** `skills/apb-owned/` mezcla dominios funcionales (`development`, `qa`, `security`) con categorías de capacidad (`api-design`, `code-review`, `event-driven`) y tiene duplicidades aparentes (`architecture` + `architecture-design`, `docs` + `documentation`, `design` + `design-approval`). Con 114 skills APB y crecimiento previsto hacia IT-general y negocio, la inconsistencia escala mal.

**Opción elegida (Debora, 2026-06-25): Opción C — limpiar taxonomía primero, escalar después.**

**Trabajo concreto para Sesión 22:**

1. **Auditoría completa** de las ~114 skills APB: mapear cada carpeta actual a un dominio canónico propuesto.
2. **Propuesta de taxonomía** (8-10 dominios canónicos con criterio claro) — presentar a Debora antes de mover nada. Checkpoint humano obligatorio en este punto.
3. **Ejecución tras aprobación:** mover archivos, actualizar referencias cruzadas en frontmatter (`depends_on`, `consumed_by`, `skills`, `subagents`), actualizar el validador si detecta rutas hardcodeadas.
4. **Validación final:** `validate_repo.py --strict` en verde, 0 drift, 19/19 tests OK.

**Criterio de diseño para la taxonomía:** los dominios deben ser lo suficientemente amplios para absorber skills de IT-general y negocio futuras sin necesidad de restructurar de nuevo. Si el volumen de skills no-dev supera ~30 en algún momento, se evalúa añadir un nivel de área (`software/`, `it-operations/`, `business/`) encima — no antes.

**Bloqueante:** ninguno. Puede ejecutarse en cualquier momento sin depender de insumos externos.

---

## Bloque añadido post-Sesión 18 (2026-06-25)

### 48. Usar plantillas de arquitectura APB como base de nuevos componentes

Las plantillas oficiales de Arquitectura APB (actualmente en `context/apb/templates/`) deben ser el punto de partida de cualquier componente nuevo que se cree en el framework. Relacionado con el punto #44 (plantilla `AGENT.md` desactualizada): la corrección de #44 debe alinear **todas** las plantillas con el formato real de `SCHEMA.md`, incluyendo la referencia a DevExpress como stack frontend estándar APB, que ya figura en las plantillas actuales.

**Acción concreta:** verificar en Sesión 13 (junto con #44) que todas las plantillas (`SKILL_APB.md`, `AGENT.md`, `SUBAGENT.md`, `WORKFLOW.md`, `PROVIDER.md`) incluyen la referencia a DevExtreme/DevExpress como herramienta corporativa estándar en los campos relevantes (p. ej. `tools`, `context`), de forma que cualquier nuevo componente creado desde plantilla ya la tenga referenciada por defecto.

**Sesión asignada:** Sesión 13 (junto con #44).

---

### 49. Sistema de diseño como repo central instanciable por apps APB

El repo `APB-DESIGN-SYSTEM` (creado en Sesión Design System) debe configurarse como **dependencia centralizada** que las aplicaciones APB instancian directamente (npm package, git submodule, o similar), en lugar de que cada proyecto copie los artefactos CSS/JS manualmente. El objetivo es que un cambio en el Design System se propague automáticamente a todas las apps que lo consumen sin intervención manual por proyecto.

**Decisiones pendientes para la sesión que aborde esto:**
- Mecanismo de distribución: npm package privado (Azure Artifacts), git submodule versionado, o CDN corporativo APB.
- Política de versiones semánticas: cuándo un cambio es breaking (major) vs. compatible (minor/patch).
- CI del Design System: añadir job que publique la nueva versión al mecanismo elegido al hacer merge a main.
- Qué apps APB existen ya y cuál es la primera candidata a pilotar la integración.

**Sesión asignada:** pendiente — candidata natural: ampliación de la sesión de Design System o Sesión 22 (refactorización de taxonomía), dado que implica decisiones de infraestructura de distribución. Requiere confirmación de Debora sobre el mecanismo preferido.

---

### 50. Pruebas y QA del propio framework

El framework construye skills y agentes para probar aplicaciones APB, pero no tiene una suite de pruebas propia que valide su propio comportamiento. Gap identificado: las GitHub Actions actuales (`validate.yml`, `telemetry.yml`) validan estructura/sintaxis y drift, pero no comportamiento funcional — no verifican que un agente dado produzca el output esperado para un input conocido.

**Trabajo a definir:**
- Batería de pruebas de integración para los scripts del framework (`validate_repo.py`, `generate_catalog.py`, `emit_telemetry.py`).
- Tests de comportamiento de agentes: given a prompt + skill.md, assert that the agent's response meets defined criteria (formato, campos obligatorios, restricciones de autonomía).
- Considerar si usar el propio `apb-qa-unit-test-gen-v1.0` (fusionado en Sesión QA) para generar estos tests — aplicar el framework a sí mismo.

**Sesión asignada:** pendiente — candidata natural: Sesión 21 (SQL + incidencias técnicas ya incluye #34 de validación QA en despliegues; añadir aquí el QA del propio repo sería coherente). Confirmar con Debora si se prefiere sesión propia.

---

### 51. Prueba real de todos los agentes del catálogo

Más allá de la validación estructural (`validate_repo.py --strict`), verificar que **todos los agentes activos del catálogo funcionan correctamente** cuando se invocan desde Claude con un caso de uso real. Hoy se crean componentes y se valida su sintaxis, pero no hay evidencia registrada de que cada agente haya sido ejercitado con un prompt real y producido output útil.

**Alcance:**
- Para cada agente en `agents/` y `subagents/`: documentar al menos un caso de prueba real (input → output observado → ¿cumple criterios del `purpose` declarado en el frontmatter?).
- Marcar explícitamente los agentes que no se han podido probar por falta de datos/entorno (ej. agentes que requieren Jira real, Rovo activo, o tenant Azure específico).
- Este trabajo alimenta directamente el punto #43 (política "Generado por IA + Validado por humano"): la validación real es la que convierte el campo `human_validated_by` de vacío a un nombre real.

**Sesión asignada:** pendiente — candidata: post-Sesión 13 o como sub-fase de #43 (última fase del plan), ya que tiene sentido probar antes de marcar como validado.

---

### 52. Cambiar contacto de Arquitectura por mail de Jira en toda la documentación

Las referencias a un contacto de arquitectura personal deben sustituirse por la dirección de correo/cola de Jira oficial del equipo de Arquitectura APB, para que las notificaciones y aprobaciones lleguen al canal correcto independientemente de quién esté disponible.

**Acción concreta:** buscar en todo el repo (skills, agentes, documentos, configuración) cualquier mención a un correo personal o nombre directo de contacto de Arquitectura y reemplazarlo por el mail de Jira / cola de equipo que Debora indique.

**Pendiente:** Debora debe facilitar la dirección de Jira / mail del equipo de Arquitectura APB antes de ejecutar este cambio.

**Sesión asignada:** tarea de mantenimiento, sin sesión propia — ejecutar en la primera sesión disponible una vez Debora aporte la dirección. Candidata: Sesión 13 (cierre de pendientes históricos).

---

### 53. Mockup de validación: agente de diseño + verificación de uso del Design System

Una vez el agente `apb-agent-ux-mockup-v1.0` (creado en Sesión Frontend) y el repo `APB-DESIGN-SYSTEM` estén ambos operativos, realizar una prueba de extremo a extremo:

1. Invocar `apb-agent-ux-mockup-v1.0` con un caso de uso real portuario (p. ej. pantalla de gestión de atraques o ficha de buque).
2. Verificar que el mockup generado usa **exclusivamente** componentes del Design System APB (tokens CSS, componentes compuestos de `APB-DESIGN-SYSTEM`), no componentes DevExtreme "en crudo" sin wrapper corporativo.
3. Si el agente usa componentes fuera del Design System, actualizar su `context`/`tools` para restringirlo explícitamente al catálogo de `APB-DESIGN-SYSTEM`.

**Objetivo:** cerrar el ciclo Frontend → Design System: no basta con que el Design System exista, los agentes que generan UI deben referenciarlo activamente.

**Sesión asignada:** pendiente — se puede ejecutar en cuanto `APB-DESIGN-SYSTEM` tenga al menos un componente compuesto publicado. Candidata: ampliación de la sesión que cierre el punto #49, o tarea inline en la sesión de Design System si el tiempo lo permite.

---

### 54. Agente de análisis funcional: entrevista portuaria + verificación de dominio + actualización de repo de dominios

Ampliación del agente `apb-agent-ddd-v1.0` (creado en Sesión 18) o posible agente/subagente complementario que cubra el flujo de análisis funcional desde el inicio:

**Comportamiento deseado:**

1. **Entrevista al funcional:** en lugar de esperar que el funcional describa el problema de forma estructurada, el agente hace preguntas activas específicas del negocio portuario y del dominio que toque (p. ej. si el dominio es "atraques": ¿escala de tiempo?, ¿integración con GISPEM?, ¿tipos de buque involucrados?, ¿permisos de Autoridad Portuaria?). Las preguntas deben estar contextualizadas al vocabulario APB, no ser genéricas.

2. **Verifica si el dominio ya existe:** antes de proponer un dominio nuevo, consulta el repo `APB-DOMAIN-CATALOG` (submodule ya integrado en `APB-IA-FRAMEWORK`) y avisa al funcional si el dominio solicitado ya existe, ya sea exacto o parcialmente — evita proliferación de dominios duplicados o fragmentados.

3. **Actualiza el repo de dominios:** si el dominio es nuevo y se valida, el agente genera el artefacto correspondiente en `APB-DOMAIN-CATALOG` (conforme al schema de ese repo) y propone el commit — con aprobación humana previa obligatoria (nivel de autonomía 1, coherente con `SYSTEM.md` §5.1).

**Relación con componentes existentes:**
- `apb-agent-ddd-v1.0` (Sesión 18): análisis DDD una vez el dominio está identificado — este punto es el paso anterior, el de identificación y validación.
- `apb-sub-ddd-interview-v1.0` (creado en Sesión 18 como subagente de entrevista): verificar si ya cubre parte de este alcance o si el punto #54 lo amplía significativamente.
- `APB-DOMAIN-CATALOG` (repo submodule): es el repositorio de destino para las actualizaciones.

**Pendiente de verificar:** leer el contenido de `apb-sub-ddd-interview-v1.0` para determinar si ya implementa la entrevista portuaria contextualizada (#54.1) o si ese subagente es más genérico. En función de eso, puede ser ampliación del subagente existente o componente nuevo.

**Sesión asignada:** pendiente — candidata natural: sesión de continuación de Sesión 18 (la Fase 1 de descomposición de monolitos ya está marcada como pendiente en esa sesión; este punto podría incluirse en la misma sesión o en la de Sesión 13 si el volumen lo permite). Confirmar con Debora.

---

## Bloque añadido post-Sesión 23 (2026-06-27) — Análisis de enriquecimiento del framework

> Fuente: `discovery/analisis-enriquecimiento-framework.md` (análisis completo: 26 agentes · 23 subagentes · 129 skills · 8 workflows, generado 2026-06-27). El documento fuente completo está en el repo — esta sección extrae las tareas accionables en formato de plan.
> Sesiones candidatas: **Sesión Enriquecimiento A** (rewirings + agentes alta prioridad), **Sesión Enriquecimiento B** (skills nuevas por dominio), **Sesión Enriquecimiento C** (workflows + providers).

> **Estado de ejecución — TODO el bloque #55–#76: ✅ COMPLETADO** (Enriq. A/B/C/D;
> reconciliado 2026-07-02). Enriq. A (rewirings #55 + primeros componentes),
> B/C/D (resto de skills/agentes/subagentes/providers/workflows). El detalle de
> #55 y el registro consolidado de #56–#76 (7 agentes + 8 subagentes + 43 skills +
> 5 providers + 9 workflows verificados en repo) están en
> [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md). Único pendiente real:
> #64 (capacity/portfolio, diferidos por datos) y la decisión sobre #59 incident-l2.

---

### 56–#76 — Enriquecimiento del framework — ✅ EJECUTADO (Enriq. B/C/D, reconciliado 2026-07-02)

> **Reconciliación 2026-07-02:** discovery del repo confirma que **todo el bloque
> de construcción #56–#76 ya está creado y cableado** (se ejecutó en las Sesiones
> Enriquecimiento B/C/D, cerradas en conversación, pero el plan no se había
> reconciliado). Detalle movido a [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).
>
> **Verificado en repo (2026-07-02):**
>
> | Bloque | Propuesto | En repo |
> |---|---|---|
> | Agentes #56–#63 | 8 | ✅ 7 creados (`change-manager`, `problem-manager`, `data-governance`, `accessibility-auditor`, `vendor-manager`, `knowledge-manager`, `api-product-manager`) |
> | Subagentes #65 | 8 | ✅ 8 (`ops-k8s`, `ops-servicebus`, `finops-azure`, `doc-confluence`, `sec-sast`, `qa-performance`, `gov-data`, `ops-entra`) |
> | Skills #66–#72 | 43 | ✅ 43 (operation, security, governance, platform+FinOps, qa, documentation, arch/disc/pm/design) |
> | Providers #73 | 5 | ✅ 5 (`azure-cost`, `confluence`, `entra-id`, `sentinel`, `jira-software`) |
> | Workflows #74 | 9 | ✅ 9 (`change-management`, `problem-management`, `accessibility-audit`, `api-lifecycle`, `data-governance`, `finops-review`, `incident-l2`, `security-patch`, `vendor-procurement`) |
>
> **Pendiente real (no construido, por decisión):**
> - **#59 `apb-agent-incident-l2`** — NO se creó agente dedicado; la capacidad L2
>   se cubre con `apb-agent-incident-support-v1.0` + `apb-agent-sre-v1.0` a través
>   del workflow `apb-wf-incident-l2-v1.0` (+ subagentes k8s/servicebus/oracle).
>   Decisión: mantener así salvo que se quiera separar formalmente.
> - **#64 `apb-agent-capacity-planner`** — diferido: requiere ≥12 meses de datos Azure.
> - **#64 `apb-agent-portfolio-it`** — diferido: requiere datos reales de uso del framework.
> - **#75** (mejoras de calidad por agente) y **#76** (priorización) — aplicados durante Enriq.;
>   los gaps de calidad residuales se rastrean vía el check #18 del validador y §H.


## Revisión integral del framework — 2026-06-29 → ✅ ARCHIVADA

> Auditoría fechada (4 dimensiones + sesiones propuestas + backlog M1–M6, todos
> resueltos) movida a [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).
> Es una fotografía de estado ya superada por la ejecución posterior; los
> pendientes derivados se siguen en las secciones §H/§I de más abajo.

---

## Análisis 360° y reconciliación de estado — 2026-06-29 (post-Enriquecimiento B, revisión exhaustiva)

> ⚠️ Borrador generado por IA (Claude, Anthropic) — pendiente de validación por Arquitectura APB.
> **Commit base:** `bf1c72a` (local). **Método:** lectura completa del repositorio con 3 agentes
> paralelos: plan de fases (1881 líneas íntegras), los 35 agentes, los 33 subagentes, muestra de
> las 175 skills APB, las 51 skills de terceros, los 17 workflows, los 19 providers, scripts y
> docs clave (SYSTEM.md, GOVERNANCE.md, manual-arquitectura.md, SCHEMA.md, templates). Auditoría
> exhaustiva, no parcial.

> **⚠️ Nota de sesión:** Durante la sesión de análisis se aplicó un fix de wiring en
> `apb-agent-incident-support-v1.0.md` (añadidos 7 subagentes que estaban declarando este padre
> pero no estaban listados en él). El resto del wiring y los cambios al validador se realizarán
> en la próxima sesión.

---

### Conformidad estructural real por tipo de componente

| Tipo | Total | Conformes | % | Observación |
|------|-------|-----------|---|-------------|
| Skills APB | 175 | 175 | 100% | ✅ Todas con frontmatter, "Comportamiento", "Marcado IA" |
| Providers | 19 | 19 | 100% | ✅ |
| Wrappers | 7 | 7 | 100% | ✅ |
| Adapters | 4 | 4 | 100% | ✅ |
| Skills terceros | 51 | 51* | 100%* | *`source_commit: "unverified"` en todas — política GOVERNANCE §4.2, exento en CI, pero deuda real de supply-chain |
| Agentes | 35 | Por verificar | — | Requiere ejecutar `validate_repo.py --strict 2>&1 \| grep -i "Marcado IA"` para confirmar si el check produce ERROR o WARNING |
| Subagentes | 33 | Por verificar | — | Ídem para "Prompt de Sistema" |
| Workflows | 17 | Por verificar | — | Ídem para "Manejo de Fallos" |

---

### A. Estado real reconciliado (el plan documentado va por detrás del repo)
> (`validate_repo.py --strict` + grep/conteo sobre frontmatter de huérfanos, estados, autonomía,
> marcado IA, system prompts, duplicados) + lectura íntegra de los documentos meta (`SYSTEM.md`,
> `GOVERNANCE.md`, `docs/manual-arquitectura.md`, este plan completo y
> `analisis-enriquecimiento-framework.md`). No es lectura línea a línea de los 341 archivos: es
> verificación estructural del 100% + muestreo de componentes representativos.

### A. Estado real reconciliado (el plan documentado va por detrás del repo)

| Bloque | Estado documentado | Estado **real verificado** |
|---|---|---|
| Enriquecimiento A (rewirings #55 + sec/gov/ops + 3 agentes + 5 subagentes) | ✅ Completado | ✅ Confirmado |
| Enriquecimiento B (32 skills + 4 agentes + 5 subagentes) | ✅ Componentes creados | ⚠️ **Creados pero NO cableados a sus "Agentes destino"** (los puntos #60–72 sí los especificaban) |
| Enriquecimiento C (5 providers + 9 workflows) | Sin marca | ✅ **Componentes creados** (19 providers, 17 workflows) — ⚠️ faltan mejoras de workflows existentes del #74 |
| Revisión 2026-06-29: 26 agentes sin Marcado IA / 19 subagentes sin prompt / bug validador | 🔴 Pendiente | ✅ **Ya resueltos** (35/35 marcado, 33/33 prompt, validador corregido) |
| Backlog M1–M6 | Mezcla | ✅ Resuelto |
| `README.md` → enlace `CATALOG.md` (raíz) | — | ❌ **Roto**: el catálogo está en `catalog/CATALOG.md`, no en raíz |
| `domain-catalog/domains/` | — | ✅ **POBLADO (2026-06-30)**: 21 dominios de negocio `proposed` (Sesión DDD sobre `API_INVENTORY_APIM.md`) — pendiente aprobación Arquitectura |

> **Conclusión de gobernanza:** falta un mecanismo que reconcilie "plan ↔ repo". Varias cosas marcadas
> como pendientes ya están hechas, y al revés (el wiring de B figura implícito en el plan pero no se ejecutó).

---

### B. Wiring incompleto — 12 inconsistencias confirmadas (revisión agente por agente)

Subagentes que declaran `parent_agent` pero el agente padre NO los lista en `subagents:`. Verificado
leyendo el frontmatter de los 35 agentes y los 33 subagentes:

| Subagente | Padre declarado | Estado en padre |
|-----------|----------------|-----------------|
| `apb-sub-ops-aca-v1.0` | `apb-agent-incident-support-v1.0` | ✅ **FIJADO** (sesión 2026-06-29) |
| `apb-sub-ops-iis-apache-v1.0` | `apb-agent-incident-support-v1.0` | ✅ **FIJADO** (sesión 2026-06-29) |
| `apb-sub-ops-k8s-v1.0` | `apb-agent-incident-support-v1.0` | ✅ **FIJADO** (sesión 2026-06-29) |
| `apb-sub-ops-network-v1.0` | `apb-agent-incident-support-v1.0` | ✅ **FIJADO** (sesión 2026-06-29) |
| `apb-sub-ops-oracle-v1.0` | `apb-agent-incident-support-v1.0` | ✅ **FIJADO** (sesión 2026-06-29) |
| `apb-sub-ops-rancher-v1.0` | `apb-agent-incident-support-v1.0` | ✅ **FIJADO** (sesión 2026-06-29) |
| `apb-sub-ops-servicebus-v1.0` | `apb-agent-incident-support-v1.0` | ✅ **FIJADO** (sesión 2026-06-29) |
| `apb-sub-ops-entra-v1.0` | `apb-agent-security-architect-v1.0` | ⏳ Pendiente próxima sesión |
| `apb-sub-sec-sast-v1.0` | `apb-agent-security-architect-v1.0` | ⏳ Pendiente próxima sesión |
| `apb-sub-qa-performance-v1.0` | `apb-agent-qa-auto-v1.0` | ⏳ Pendiente próxima sesión |
| `apb-sub-finops-azure-v1.0` | `apb-agent-finops-v1.0` | ⏳ Pendiente próxima sesión |
| `apb-sub-gov-data-v1.0` | `apb-agent-data-governance-v1.0` | ⏳ Pendiente próxima sesión |

**Causa raíz:** `validate_agent_subagent_consistency` en el validador verifica solo que el `parent_agent`
referenciado **exista**, no que el agente lo **liste** en `subagents:`. Es validación unidireccional.
**Fix planificado:** función `validate_bidirectional_wiring()` en próxima sesión + test nº 24.

---

### C. Mapeo de skills de Enriq. B pendientes de cablear (por agente destino)

Extraído de los puntos #68–#72 del plan. Las skills existen en el repo pero aún no están en la lista
`skills:` de los agentes que deben usarlas. Pendiente de wiring en próxima sesión:

| Agente destino | Skills a añadir |
|----------------|-----------------|
| `apb-agent-data-governance-v1.0` | `apb-gov-data-classification-v1.0`, `apb-gov-dpia-v1.0` |
| `apb-agent-governance-v1.0` | `apb-gov-data-classification-v1.0`, `apb-gov-ai-model-lifecycle-v1.0`, `apb-gov-tech-radar-v1.0`, `apb-gov-framework-metrics-v1.0`, `apb-gov-framework-audit-v1.0` |
| `apb-agent-compliance-audit-v1.0` | `apb-gov-lcsp-check-v1.0`, `apb-gov-dpia-v1.0` |
| `apb-agent-vendor-manager-v1.0` | `apb-gov-lcsp-check-v1.0`, `apb-gov-vendor-eval-v1.0` |
| `apb-agent-catalog-manager-v1.0` | `apb-gov-framework-metrics-v1.0`, `apb-gov-framework-audit-v1.0` |
| `apb-agent-tech-discovery-v1.0` | `apb-gov-tech-radar-v1.0`, `apb-disc-tech-eval-v1.0`, `apb-disc-poc-guide-v1.0` |
| `apb-agent-finops-v1.0` | `apb-plat-finops-alerting-v1.0`, `apb-plat-finops-chargeback-v1.0`, `apb-plat-finops-reservations-v1.0` |
| `apb-agent-platform-engineer-v1.0` | `apb-plat-k8s-v1.0`, `apb-plat-azure-servicebus-v1.0`, `apb-plat-secret-rotation-v1.0`, `apb-plat-environment-promotion-v1.0` |
| `apb-agent-cloud-architect-v1.0` | `apb-plat-k8s-v1.0`, `apb-plat-azure-servicebus-v1.0` |
| `apb-agent-release-manager-v1.0` | `apb-plat-environment-promotion-v1.0`, `apb-doc-changelog-v1.0`, `apb-doc-release-notes-v1.0` |
| `apb-agent-qa-auto-v1.0` | `apb-qa-performance-v1.0`, `apb-qa-contract-testing-v1.0`, `apb-qa-accessibility-v1.0` |
| `apb-agent-accessibility-auditor-v1.0` | `apb-qa-accessibility-v1.0` |
| `apb-agent-ux-mockup-v1.0` | `apb-qa-accessibility-v1.0`, `apb-design-wcag-patterns-v1.0` |
| `apb-agent-documentation-v1.0` | `apb-doc-changelog-v1.0`, `apb-doc-release-notes-v1.0`, `apb-doc-onboarding-v1.0` |
| `apb-agent-knowledge-manager-v1.0` | `apb-doc-onboarding-v1.0` |
| `apb-agent-sre-v1.0` | `apb-doc-post-mortem-v1.0` |
| `apb-agent-technical-architect-v1.0` | `apb-arch-c4-model-v1.0`, `apb-arch-context-mapping-v1.0` |
| `apb-agent-domain-architect-v1.0` | `apb-arch-context-mapping-v1.0` |
| `apb-agent-api-product-manager-v1.0` | `apb-arch-api-lifecycle-v1.0` |
| `apb-agent-business-analyst-v1.0` | `apb-disc-user-journey-v1.0`, `apb-disc-value-stream-v1.0`, `apb-pm-risk-register-v1.0`, `apb-pm-stakeholder-map-v1.0` |
| `apb-agent-pm-v1.0` | `apb-pm-risk-register-v1.0`, `apb-pm-status-report-v1.0`, `apb-pm-stakeholder-map-v1.0` |

---

### D. Evolución del framework por ámbito (análisis 360°)

#### D.1 Técnico
- **Trayectoria:** prompts sueltos → jerarquía 7 niveles + validador 19 checks + catálogo autogenerado
  + CI bloqueante + 23 tests de dogfooding. Madurez alta en *forma estructural*.
- **Brechas críticas:**
  - Sin **runtime de orquestación real**: workflows son instrucciones manuales. `invoke_agent.py`
    es un esqueleto. Manual-arquitectura §3.1 recomienda **Azure AI Foundry + Semantic Kernel**.
  - Sin **memoria compartida** inter-sesiones: Redis (short-term) + Cosmos DB (state) + Git (long-term).
  - **Wiring unidireccional** en validador: no detecta subagentes/skills huérfanos.
  - **Encoding Windows**: fix ya aplicado en `bf1c72a` (`sys.stdout.reconfigure(encoding="utf-8")`).
  - `README.md` → enlace roto a `CATALOG.md` (raíz no existe; está en `catalog/CATALOG.md`).
- **Mejoras a implementar (próxima sesión):**
  1. `validate_bidirectional_wiring()` en validador con test
  2. Fix enlace README
  3. Verificar si checks de agentes/subagentes/workflows producen ERROR o WARNING en validador actual

#### D.2 Funcional (cobertura de dominios IT)

| Área | Nivel | Gap |
|------|-------|-----|
| SDD / Especificación | ✅ Sólida | — |
| Desarrollo .NET/Django | ✅ Sólida | — |
| Code Review | ✅ Buena | — |
| QA Automatizado | ✅ Buena (caveat) | `qa-performance` no declarado en padre (fix pendiente) |
| Arquitectura / DDD | ✅ Sólida | ✅ Domain Catalog poblado: 21 dominios `proposed` (Sesión DDD 2026-06-30) — pendiente aprobación Arquitectura |
| Seguridad | ✅ Buena | `entra`/`sast` no declarados; sin DAST wrapper propio |
| Gobernanza | ✅ Muy buena | 0 aprobaciones; ningún validador humano nombrado |
| DevOps / Plataforma | 🟡 Media | Wiring de 4 platform skills pendiente |
| Operaciones L1 | ✅ Buena | 7 subagentes ya fijados en incident-support |
| SRE / Observabilidad | ✅ Buena | — |
| FinOps | 🟡 Media | 3 skills + 1 subagente pendientes de cablear |
| Change / Problem Mgmt | 🟡 Media | Agentes existen; skills de wiring pendiente |
| PM / Discovery | 🟡 Limitada | Skills Enriq. B no cableadas a BA/PM/TechDiscovery |
| WCAG / Accesibilidad | 🟡 Nueva | accessibility-auditor nuevo; wiring pendiente |
| LCSP / Licitación | ❌ Pendiente | Bloqueado: briefing de Débora |
| Descomposición monolitos | ❌ Pendiente | Domain Catalog ya poblado (21 dominios `proposed`); falta aprobación + acceso a código SOSTRAT |
| M365 / Teams / SharePoint | ❌ Pendiente | Adapters existen; integración real pendiente |

#### D.3 QA del framework
- **Validación solo estructural** (forma del componente), NO funcional (comportamiento).
- `tests/test_agent_behavior.md` existe como piloto pero no está automatizado.
- Sin tests de regresión de contenido: si una skill cambia instrucción, el validador no lo detecta.
- **Madurez QA propuesta:**
  - Tier 1 (inmediato): check anti-huérfanos automático (test nº 24)
  - Tier 2 (próximas sesiones): Golden Output Tests para 5 skills críticas
  - Tier 3 (mediano plazo): integration tests con LLM mock para agentes

#### D.4 Seguridad
- `apb-sub-sec-sast-v1.0` y `apb-sub-ops-entra-v1.0`: pendientes de **visto bueno de Ciberseguridad** antes de uso.
- 51 skills terceros sin SHA fijado: **deuda de supply-chain** (política temporal deliberada).
- `prov-sentinel-v1.0` y `prov-entra-id-v1.0`: providers presentes sin integración confirmada.
- Gap: sin **DAST wrapper** propio (OWASP ZAP / Trivy) para seguridad ofensiva.

#### D.5 Gobernanza
- GOVERNANCE.md, SYSTEM.md §7.2, estados de componentes: marco bien definido.
- **Brecha crítica: 341/341 en `draft`** (KPI objetivo: <30%). 0 ciclos de aprobación iniciados.
- Ningún componente tiene `validador humano nombrado` → ninguno puede pasar a `approved`.
- Telemetría: scripts `emit_telemetry.py` e `invoke_agent.py` presentes como esqueletos. Los 5 KPIs
  de GOVERNANCE §6 son **imposibles de medir** sin datos reales.
- Plan ↔ repo desincronizado: necesita proceso de reconciliación tras cada sesión.

#### D.6 Mantenimiento futuro
- Sin check anti-huérfanos → cada sesión de enriquecimiento puede añadir deuda silenciosa.
- Sin telemetría real → componentes en desuso no detectables.
- Ciclo revisión semestral (`review_date:` vencido) → sin automatización de avisos.
- Templates actualizadas (29-Jun). Todos los tipos de componentes con plantilla válida.

---

### E. Riesgos de cara a producción

| # | Riesgo | Sev. | Mitigación |
|---|--------|------|-----------|
| R1 | Sin runtime de orquestación: workflows manuales no escalables | 🔴 | Decisión runtime + `prov-orchestration-engine-v1.0` |
| R2 | 5 subagentes no declarados → capacidades invisibles a sus agentes | 🔴 | Wiring en próxima sesión (4 pendientes) |
| R3 | 100% draft: sin ningún componente aprobado formalmente | 🔴 | Primer ciclo aprobación |
| R4 | ~~Domain Catalog vacío → DDD/monolitos bloqueados~~ ✅ MITIGADO: inventario recibido + 21 dominios `proposed` (Sesión DDD 2026-06-30) | 🟢 | Pendiente aprobación Arquitectura + experto de negocio para fronteras |
| R5 | Wiring skills Enriq. B: capacidades funcionales no invocables desde agentes | 🟡 | Mapeo §C, próxima sesión |
| R6 | Sin memoria compartida → contexto perdido inter-sesiones | 🟡 | Redis + Cosmos DB (cuando runtime listo) |
| R7 | Telemetría no instrumentada → KPIs imposibles de medir | 🟡 | Instrumentar `invoke_agent.py` |
| R8 | 51 skills terceros sin SHA fijado | 🟡 | Política temporal; fijar con acceso de red |
| R9 | SAST/Entra sin validación Ciberseguridad | 🟡 | Revisión Ciber antes de uso |
| R10 | Sin DAST wrapper → gap de seguridad ofensiva | 🟡 | OWASP ZAP o Trivy wrapper |
| R11 | Plan ↔ repo desincronizado | 🟡 | Actualizar plan tras cada sesión |
| R12 | README → enlace roto a CATALOG.md | 🟢 | Fix trivial en próxima sesión |

---

### F. Skills / componentes de TERCEROS a evaluar

Para varios gaps conviene **incorporar** en lugar de construir desde cero. Proceso estándar:
licencia + análisis de seguridad + `source_commit` SHA real.

| Gap / necesidad | Tercero candidato | Prioridad | Nota |
|---|---|---|---|
| Runtime de orquestación | **Microsoft Semantic Kernel** / Azure AI Foundry | 🔴 | Ya recomendado en `manual-arquitectura.md §3.1` |
| Telemetría automática | **OpenTelemetry Python** | 🔴 | Para instrumentar `invoke_agent.py` |
| Developer Portal / discoverability | **Backstage** (Spotify) | 🟡 | Catálogo de servicios + componentes APB |
| DAST / seguridad ofensiva | **OWASP ZAP** / Trivy | 🟡 | Gap de cobertura en seguridad |
| Contexto enriquecido para LLM | **`context7`** | 🟡 | Mencionado en #27, **nunca evaluado** |
| Debugging sistemático | **`obra/superpowers` → systematic debugging** | 🟡 | Repo parcialmente incorporado; falta esta skill (#27) |
| Dev / arquitectura TypeScript | **`mattpocock/*` resto del monorepo** | 🟡 | Solo 2 de ~21 incorporadas (#27) |
| Diagramación arquitectura | `excalidraw` (MCP) | 🟢 | Complementaría `apb-arch-c4-model` (#27) |
| Terraform governance | Ampliar `hashicorp` existente | 🟢 | Ya 2 skills; ampliar a modules y workspaces |
| `_spec-driven` skills + terceros abiertos §8 | 3 skills `spec-to-*` de `apb-ai-skills` | 🟢 | Sesión 19 + #45 |

> Acción: **Sesión 19** (terceros), aportando Débora las URLs exactas que falten.

---

### G. Temas futuros planificados — consolidado

| Tema | Punto | Estado / bloqueante |
|---|---|---|
| **Valoración COSMIC con histórico real** | #8 | `apb-disc-cosmic-v1.0` existe; **bloqueado: horas históricas de Débora** |
| Agentes de licitación LCSP | #36/Sesión 20 | **Bloqueado: briefing de Débora** |
| Descomposición de monolitos (Fase 1) | #38 F1 | Catálogo ya poblado (21 dominios `proposed`); bloqueado por aprobación + acceso a código SOSTRAT |
| Spec desde histórico Jira | #37 | Sin sesión asignada |
| Runtime de orquestación real | #41 | **Bloqueado: decisión arquitectónica Débora/Plataforma** |
| Dashboards Power BI/Grafana + logs | #39/#40 | Parcial (Sesión 17); falta agente dedicado |
| Telemetría para usuarios de chat sin commit | #46 | Requiere proxy/wrapper de plataforma |
| Distribución Design System (npm/submodule/CDN) | #49/Sesión 22 | **Bloqueado: decisión de Débora** |
| QA del propio framework + prueba real agentes | #50/#51 | Alimenta paso a `approved` |
| Documentación Word por audiencias + doc Dirección | #23/Sesión 14 | Parcial: borradores MD; falta .docx |
| Plantillas Word/Excel ofimáticas | #6 | Bloqueado: ejemplos de Débora |
| Email Arquitectura → cola Jira | #52 | Bloqueado: dirección de Débora |
| Mockup validación Design System | #53 | Tras #49 |
| Capacity Planner / Portfolio IT | #64 | Diferidos: ≥12 meses de datos reales en Azure |
| Memoria compartida agentes | (nuevo) | Tras decisión runtime |
| Primer ciclo aprobación formal | GOVERNANCE §2 | Requires: aprobadores nombrados por ámbito |

---

### H. Siguientes fases — orden de ejecución recomendado

#### ✅ FASE 0 — Higiene de wiring + validador (COMPLETADA 2026-06-30)

Commit: `d62c6b1`. 24 ficheros, 284 inserciones. Resultado: `--strict` exit 0, 59 warnings exentos.

1. ✅ **Fix README.md**: enlace `CATALOG.md` → `catalog/CATALOG.md` corregido.
2. ✅ **Wiring 5 subagentes huérfanos**: `entra`+`sast` → `security-architect`; `performance` →
   `qa-auto`; `finops-azure` → `finops`; `gov-data` → `data-governance`.
3. ✅ **Wiring skills Enriq. B**: 40 wirings corregidos en 22 agentes (tabla §C + 19 adicionales
   detectados por el nuevo validador).
4. ✅ **`validate_bidirectional_wiring()`** añadida a `scripts/validate_repo.py` + test
   `TestValidateBidirectionalWiring` (2 casos) en `tests/test_validate_repo.py`.
5. ✅ Catálogo regenerado, `--strict` verde, 21/21 tests OK.

> **Regla de cierre de sesión (Débora, 2026-06-30):** al cierre de CADA sesión ejecutar siempre:
> `generate_catalog.py` + `validate_repo.py --strict` + tests + actualizar PLAN_FASES_FUTURAS +
> CONTINUIDAD + HANDOFF + README. Guardado en memoria del agente.

#### ✅ FASE 1 — Mejoras de workflows existentes (COMPLETADA 2026-06-30)

8. ✅ Añadir Change Manager a `sdd-full` y `cloud-migration`.
9. ✅ Añadir Security Architect a `code-review` (PRs con cambios en auth/datos sensibles).
10. ✅ Conectar `incident-l1` → `incident-l2` workflow + campo `escalation:` en frontmatter.
11. ✅ Añadir Problem Manager a `incident-l1` para incidencias recurrentes.
12. ✅ Añadir Tech Debt a `legacy-onboarding`.
13. ✅ Añadir performance y accessibility a `qa-evidence`.

#### ✅ FASE 1B — Corrección de bugs BUG-01 a BUG-08 (COMPLETADA 2026-06-30)

14. ✅ BUG-01: `context/apb/templates/WORKFLOW.md` — blockquote → YAML frontmatter canónico.
15. ✅ BUG-02: `scripts/generate_catalog.py` — regex `\s*+` → `\s*` (8 patrones, Python 3.10).
16. ⏸ BUG-03: `design-system/components/component-reference.md §9` — color sidebar pendiente confirmación equipo diseño.
17. ✅ BUG-04: `adapters/claude/adapter-claude-v1.0.md` — model string `claude-sonnet-4-6`.
18. ✅ BUG-05: `SYSTEM.md §4.2` — añadidos adapters `m365` y `rovo` (los 4 reales del repo).
19. ✅ BUG-06: `.github/workflows/telemetry.yml` — anti-pattern git push → PR automático.
20. ✅ BUG-07: `CONTINUIDAD_PROYECTO.md §8` — 208 → 341 componentes.
21. ✅ BUG-08: `third-lum1104-knowledge-graph-v1.0.md` — stub creado con `status: watchlist` y aviso licencia no verificada.

#### FASE 2 — Sesiones abiertas del plan

14. **Sesión 13** resto: puntos #6 (plantillas Word), #8 (COSMIC—bloqueado), #52 (email Jira).
15. **Sesión 14**: ✅ **documento Dirección creado** (`docs/informe-direccion.md`, 2026-06-30). Pendiente: conversión .docx (requiere decisión runtime + plantilla).
16. **Sesión 19**: terceros adicionales + decisión `_spec-driven` (bloqueado: URLs de Débora).
17. **Sesión 20**: agentes LCSP (bloqueado: briefing de Débora).
18. **Sesión 21**: SQL skills + soporte incidencias generalista (✅ completada 2026-06-29).
19. **Sesión 22**: Design System distribución (bloqueado: decisión de Débora).
20. ✅ **#50/#51**: QA del framework — 20 casos de comportamiento (6 agentes), 5 Golden Output Tests, test Python de cobertura (2026-06-30).

#### FASE 3 — Evolución estratégica (a 1–12 meses)

21. ✅ **Domain Catalog** poblado: 21 dominios de negocio `proposed` en
    `APB-DOMAIN-CATALOG/domains/` (Sesión DDD 2026-06-30, sobre `API_INVENTORY_APIM.md`).
    Pendiente: PR + aprobación de Arquitectura + experto de negocio para fronteras
    (Escalas/Cruceros/Líneas, INS/PIF, MDE/OPS, FER). **Bounded contexts diferidos**
    a sesión "DDD Fase BC" con acceso a código/BBDD.
22. **Runtime de orquestación** (decisión + `prov-orchestration-engine-v1.0` + Semantic Kernel).
23. **Memoria compartida** (`prov-agent-memory-v1.0`: Redis + Cosmos DB + Git).
24. **Telemetría automática**: instrumentar `invoke_agent.py` con OpenTelemetry → dashboard Power BI.
25. **Primer ciclo de aprobación formal**: seleccionar 10 componentes core, asignar aprobadores
    (2 por componente, ámbitos distintos), llevar a `approved`. KPI: <30% en draft.
26. **Fase 1 descomposición monolitos** — Domain Catalog ya poblado (21 dominios
    `proposed`); ahora bloqueado por: aprobación de dominios + acceso al código del
    monolito SOSTRAT (Java/Oracle → DOCKS).

---

### I. Decisiones pendientes por persona/equipo

#### Bloqueos de Débora / Dirección

| Decisión | Desbloquea | Urgencia |
|----------|-----------|---------|
| ~~Listado de APIs/sistemas APB~~ ✅ **RECIBIDO (2026-06-30)** — `API_INVENTORY_APIM.md`; Sesión DDD ejecutada, 21 dominios `proposed` | ~~Domain Catalog, DDD, descomposición monolitos~~ → ahora desbloqueado | 🟢 |
| Decisión runtime orquestación (Azure AI Foundry vs. Anthropic SDK) | Fase 3 §H-22 | 🟡 Mes 1 |
| Mecanismo distribución Design System | Sesión 22 | 🟡 Mes 1 |
| Ejemplos Word/Excel + mapa agentes↔Jira | Sesión 14, punto #6 | 🟡 Mes 1 |
| Horas históricas reales para COSMIC | Calibración `apb-disc-cosmic-v1.0` (#8) | 🟡 Mes 2 |
| Briefing LCSP | Sesión 20 (agentes licitación) | 🟡 Mes 2 |
| Qué componentes aprobar primero + aprobadores por ámbito | Primer ciclo gobernanza | 🟡 Mes 1 |
| Esbozo informe riesgos IA organizativo | Sesión 16 | 🟢 Mes 2-3 |
| URLs de repos de terceros adicionales | Sesión 19 | 🟢 Mes 2-3 |
| Email/cola Jira de Arquitectura | Toda la documentación (#52) | 🟢 |

#### Equipos (tareas técnicas)

| Equipo | Qué validar / hacer | Entregable |
|--------|---------------------|-----------|
| **Arquitectura APB** | Revisar y aprobar (draft→candidate) los 4 agentes y skills arch/disc/governance nuevos; validar wiring §C; decidir destino skills PM; resolver 3 grupos de duplicados; liderar primer ciclo aprobación; decidir runtime con Plataforma | Componentes con `approved_by:` nombrado |
| **Plataforma / Cloud** | Validar skills K8s/AKS, ServiceBus, secret-rotation, environment-promotion y FinOps contra stack Azure real (naming, tiers, subscriptions); activar M365 integrations (HANDOFF_SESION15); co-decidir runtime; implementar Redis+Cosmos cuando runtime decidido | Validación técnica + pipeline parametrizable |
| **Operaciones / SRE** | Validar subagente Entra ID; confirmar umbrales/SLOs reales en skills observabilidad/post-mortem/capacity; preparar runbooks puente mientras no hay orquestación; integrar `emit_telemetry.py` con Azure Monitor | SLOs reales + runbooks operativos |
| **Ciberseguridad** | Revisar y aprobar `apb-sub-sec-sast-v1.0` y `apb-sub-ops-entra-v1.0` antes de uso; validar 51 exenciones `source_commit`; proponer proceso para fijar SHAs; evaluar necesidad de DAST wrapper | Aprobación seguridad documentada |
| **DPO / Protección de datos** | Validar `apb-gov-dpia-v1.0`, `apb-gov-data-classification-v1.0`, `apb-sub-gov-data-v1.0` contra criterio AEPD (RGPD art. 30/35, ENS) | Confirmación encaje normativo |
| **QA** | Definir Golden Output Tests para 5 skills críticas; extender `test_agent_behavior.md` a automatizados; definir umbrales k6 reales para tests de performance | Estrategia test comportamiento |
| **Negocio / PM** | Validar 5 skills PM nuevas (user-journey, value-stream, risk-register, status-report, stakeholder-map); confirmar agente destino (PM vs. BA); confirmar qué perfiles las usarán | Validación utilidad funcional |
| **Gobernanza del catálogo** | Registrar validador humano por componente cuando inicie ciclo aprobación; diseñar proceso draft→candidate→approved; planificar telemetría KPIs; mantener reconciliación plan↔repo | Owner por componente + plan métricas |

---

### J. Verificación end-to-end (al final de CADA sesión — obligatorio)

```bash
# 1. Catálogo actualizado
python scripts/generate_catalog.py

# 2. Validación estricta — criterio canónico: exit 0 (NO el conteo de errores)
PYTHONIOENCODING=utf-8 python scripts/validate_repo.py --strict

# 3. Tests completos
python -m unittest tests.test_validate_repo tests.test_behavior_coverage -v
# → 33/33 (test_validate_repo) + 5/5 (test_behavior_coverage) = 38 total (2026-06-30)

# 4. Verificación de wirings aplicados (ejemplo)
grep -A30 "^subagents:" agents/apb-agent-incident-support-v1.0.md
grep -A5 "^subagents:" agents/apb-agent-security-architect-v1.0.md

# 5. Fix README verificado
grep "CATALOG.md" README.md
# debe mostrar solo "catalog/CATALOG.md", nunca "CATALOG.md" sin prefijo
```

> **Referencia:** `discovery/HANDOFF_TECNICOS.md` contiene el detalle por equipo y las decisiones bloqueantes de Débora/Dirección.


---

## K. Evoluciones propuestas — Análisis 360° (2026-06-29)

> Fuente: `analisis_exhaustivo_framework.md` — análisis multi-perspectiva de los tres repositorios.
> Todo lo que sigue es propuesta IA. Ningún punto es ejecutable sin revisión y aprobación humana.

### K.1 Evoluciones técnicas

| ID | Título | Descripción | Prioridad | Esfuerzo est. |
|----|--------|-------------|-----------|--------------|
| E-T1 | **Motor de orquestación real** | Los workflows están en Markdown pero no se ejecutan automáticamente. Opciones: (A) GitHub Action parametrizable que lee el frontmatter YAML y pausa en `human_checkpoints` vía GitHub Environments — 1-2 días; (B) `orchestrator.py` con log de ejecución — 1 semana; (C) integración con `microsoft/semantic-kernel` — 1 mes+. Recomendada Opción A como primer paso. | Alta | 1-2 días (opción A) |
| E-T2 | **Golden tests para skills críticas** | ~~Para las 5 skills candidadas a aprobación, crear tests estáticos.~~ **✅ COMPLETADO (2026-06-30):** clase `TestGoldenOutputStructure` (5 tests) en `tests/test_validate_repo.py`. Verifica `## Marcado IA obligatorio`, `## ⚠️ Comportamiento ante inputs incompletos` e `id:` en frontmatter para: `apb-arch-api-contract-v1.0`, `apb-qa-accessibility-v1.0`, `apb-dev-code-review-v1.0`, `apb-sec-threat-model-v1.0`, `apb-gov-evidence-v1.0`. | ~~Media~~ | ✅ Cerrado |
| E-T3 | **Notificación de breaking changes en contratos de skills** | ~~Cuando una skill actualiza su versión mayor, `validate_repo.py` debería generar WARNING.~~ **✅ COMPLETADO (2026-06-30):** función `validate_version_drift()` añadida a `scripts/validate_repo.py` + clase `TestVersionDrift` (2 tests) en `tests/test_validate_repo.py`. 33/33 tests OK. | ~~Media~~ | ✅ Cerrado |
| E-T4 | **Capa formal de Capabilities** | Crear la carpeta `capabilities/` declarada en SYSTEM.md §3 con descriptores de capacidades de negocio (Generar Especificaciones, Revisar Código, Diseñar Arquitectura, Gestionar Incidentes...). Completa la jerarquía y facilita la alineación con el negocio. | Baja | 1 semana |
| E-T5 | **Caching de outputs de agentes dentro de un workflow** | Para workflows que procesan el mismo artefacto base, implementar caching por hash de input. Reduce coste de tokens en re-ejecuciones parciales. | Baja | 1-2 semanas |

### K.2 Evoluciones funcionales

| ID | Título | Descripción | Prioridad | Notas |
|----|--------|-------------|-----------|-------|
| E-F1 | **Agente de Change Management / ITIL** | APB opera con ITIL (P1–P4, L1/L2/L3, CAB, RFC, Problem Management). Ningún agente actual gestiona el proceso de cambio formal. `apb-agent-change-manager-v1.0` cubriría: evaluación de impacto de RFC, informe para CAB, tracking de cambios de emergencia, creación de tickets Jira via `prov-atlassian-v1.0`. | Alta | — |
| E-F2 | **Agente de Data Governance / RGPD** | Obligación regulatoria: RAT, bases jurídicas, plazos de conservación, DPIA para tratamientos de alto riesgo. `apb-agent-data-governance-v1.0` que audite el estado de estos requisitos y genere el RAT actualizado. | Alta | No es nice-to-have — es requisito legal |
| E-F3 | **Enriquecimiento FinOps Azure** | 19 providers Azure sin visibilidad de costes de IA. Agente o skill de FinOps que analice Azure Cost Management y proponga optimizaciones. Permite justificar ROI del framework con datos reales. | Media | — |
| E-F4 | **Workflows de licitación / LCSP** | APB sujeto a LCSP. Preparación de pliegos, evaluación de ofertas, gestión de contratos de mantenimiento. Pendiente briefing de Débora. | Media | Bloqueado: briefing de Débora |
| E-F5 | **Agente de Onboarding de Proyectos Legacy** | `apb-agent-legacy-onboarding-v1.0` que automatice el análisis inicial de un proyecto existente (estructura de código, deuda técnica, APIs no documentadas) y genere el primer borrador del `system-spec.md`. | Media | — |

### K.3 Evoluciones de seguridad

| ID | Título | Descripción | Prioridad | Implementación |
|----|--------|-------------|-----------|---------------|
| E-S1 | **SBOM automatizado para terceros** | Los 51 skills de terceros + 7 wrappers deberían generar automáticamente un Software Bill of Materials. Ampliar `generate_catalog.py` para añadir sección SBOM en `CATALOG.md` con `source_repo`, `source_license`, `source_commit`, `verified_date`. | Alta | Extensión de script existente |
| E-S2 | **Supply chain verification en CI** | Step que intente verificar el SHA actual del repo de origen (`git ls-remote`). Si accesible y SHA cambió: WARNING "contenido modificado en origen desde la última revisión". | Media | GitHub Action adicional |
| E-S3 | **Auditoría periódica de dependencias** | GitHub Action semanal con `pip-audit` o `safety check` para wrappers con dependencias Python. Integrar hallazgos como input a `apb-agent-tech-debt-v1.0`. | Media | GitHub Action semanal |

### K.4 Evoluciones de gobernanza

| ID | Título | Descripción | Prioridad | Implementación |
|----|--------|-------------|-----------|---------------|
| E-G1 | **Dashboard de métricas de gobernanza** | Dashboard en Log Analytics o Power BI: % de componentes por estado, tiempo medio de aprobación, skills más invocadas, evolución del reuso (objetivo >50%). Dependiente de telemetría activa. | Alta | Dependiente de telemetría |
| E-G2 | **Ciclo de revisión semestral automatizado** | ~~GitHub Action mensual.~~ **✅ COMPLETADO (2026-06-30):** `scripts/check_review_dates.py` + `.github/workflows/review-reminder.yml` (cron día 1 de cada mes). Abre issue automático con componentes con `review_date` > 180 días. | ~~Media~~ | ✅ Cerrado |
| E-G3 | **Proceso formal de deprecación** | ~~Documentar en GOVERNANCE.md.~~ **✅ COMPLETADO (2026-06-30):** `GOVERNANCE.md §7` — quién propone, quién aprueba, plazos (30 días si consumed_by activo), pasos técnicos, paso a `retired` (90 días). | ~~Media~~ | ✅ Cerrado |

### K.5 Evoluciones de Developer Experience

| ID | Título | Descripción | Prioridad | Esfuerzo est. |
|----|--------|-------------|-----------|--------------|
| E-DX1 | **Guía "Primera skill / Primer agente"** | ~~`docs/getting-started-contributing.md`.~~ **✅ COMPLETADO (2026-06-30):** `docs/getting-started-contributing.md` con 8 secciones: prerrequisitos, discovery, skill paso a paso, agente paso a paso, validador, catálogo, PR checklist, cierre de sesión. | ~~Media~~ | ✅ Cerrado |
| E-DX2 | **Storybook para APB-DESIGN-SYSTEM** | Reemplazar o complementar `visual-reference.html` con Storybook. Cada componente JSX con ejemplos interactivos, documentación de props y tests de accesibilidad automáticos (addon a11y — WCAG 2.1 AA, requisito regulatorio vía RD 1112/2018). | Baja | 2-3 días configuración |

---

## Bloque añadido 2026-06-30 — Orquestación y Coreografía de Agentes

### 77. Orquestación y coreografía de agentes — análisis e implementación

> **Propuesta recibida de Debora (2026-06-30).** Este punto requiere análisis previo antes de
> implementar. Ningún componente se construye hasta que la decisión arquitectónica esté aprobada.

> **Nueva evidencia (Sesión DDD, 2026-06-30):** al ejecutar `apb-agent-ddd-v1.0` para poblar
> APB-DOMAIN-CATALOG no existía motor que invocara el agente programáticamente — se ejecutó su
> protocolo manualmente (lectura del `.md` + aplicación de los pasos). Esto provocó que se
> omitiera el paso explícito del agente "cargar `prov-apb-knowledge-v1.0` antes de ejecutar",
> causando un error de dominio (SOJA mal clasificado, modelo incompleto: 15 dominios en vez de
> 21) que solo se detectó porque Débora lo corrigió manualmente. **Conclusión: la falta de
> runtime de orquestación no es solo un problema de eficiencia — ya ha causado un error de
> calidad real por incumplimiento silencioso de las instrucciones declaradas en el frontmatter
> de un agente.** Refuerza la prioridad de este punto #77.

#### Contexto y propuesta recibida

Debora propone una arquitectura híbrida de dos capas para coordinar los agentes del framework:

1. **Capa de Orquestación (macro)** — workflows de alto nivel con estado, reintentos y ramificaciones.
   Herramientas candidatas: LangGraph, Temporal, Prefect/Dagster.
2. **Capa de Coreografía (micro)** — comunicación inter-agente por eventos (pub/sub).
   Herramientas candidatas: Azure Service Bus (ya en stack APB), CloudEvents + JSON.

Flujo propuesto para "Implementar feature X":

```
PM → Arch → Dev (commit+push) → CI/CD (GitHub Actions vía repository_dispatch)
   ← evento ci.completed ← Service Bus ←─────────────────────────────────────
└─ Si éxito → PR → Review → merge
└─ Si fallo → Dev corrige → nuevo commit (máx 3 reintentos)
```

Patrones adicionales mencionados en la propuesta: Saga Pattern, Event Sourcing, LangGraph con
checkpoint + webhook para reanudar workflows pausados tras eventos CI.

#### Análisis de adecuación al stack APB

**Lo que encaja bien:**

- Azure Service Bus ya está en el stack APB → la coreografía por eventos es coherente. El provider
  `prov-servicebus-v1.0` ya existe; ampliar a orquestación de agentes es extensión natural.
- CloudEvents + JSON ya están en el stack APB → formato de eventos sin coste adicional.
- GitHub Actions ya gestiona CI/CD del framework → `repository_dispatch` para disparar CI desde
  agentes es viable y sin dependencias nuevas.
- El patrón de **autonomy_level 1 con gates humanos** del framework es compatible con Saga Pattern:
  cada compensación puede ser un gate de aprobación humana en vez de un rollback automático.

**Lo que requiere ajuste antes de adoptar:**

- **LangGraph** es Python y de Anthropic/LangChain; el stack APB es .NET + Azure. Viable para el
  framework de IA (ya es Python), pero introduce dependencia nueva. Alternativa nativa Azure:
  **Azure Durable Functions** o **Azure AI Foundry Agents** (ya recomendado en `manual-arquitectura.md §3.1`).
  Hay que decidir cuál antes de implementar. **No adoptar LangGraph sin evaluar las alternativas Azure.**
- **Temporal** es excelente para workflows duraderos pero añade infraestructura separada (servidor
  Temporal) que APB debería operar. **Azure Durable Functions** cubre el mismo caso de uso sin
  infraestructura adicional y ya es parte de Azure. Recomendación: Temporal solo si Azure Durable
  Functions no cubre el caso concreto de APB.
- **Event Sourcing completo** (toda acción es evento inmutable, reconstrucción de estado) es
  potente pero añade complejidad significativa de implementación. Antes de adoptarlo, verificar si
  los logs de GitHub Actions + telemetría JSONL ya existente (`emit_telemetry.py`) cubren el 80%
  del valor con el 20% del coste. El Event Sourcing puro se reserva para decisiones críticas de
  agentes que impacten producción.
- **Power BI (ejecutivo) + Grafana (operativo)** ya están en el plan (#39/#40, Sesión 17 parcial).
  El dashboard de orquestación se construye sobre la misma base, no es una herramienta nueva.

**Restricción no negociable:** todo lo que se construya **debe respetar el guardrail de autonomy_level 1**.
El orquestador no puede auto-aprobar, auto-mergear ni desplegar a producción sin gate humano, aunque
LangGraph o Temporal técnicamente lo permitan. Los `human_checkpoints` declarados en los workflows
son obligatorios también en el motor de ejecución real.

#### Decisiones arquitectónicas previas a implementar (bloqueantes)

| Decisión | Opciones | Quién decide | Urgencia |
|----------|----------|--------------|---------|
| Motor de orquestación macro | (A) Azure Durable Functions + Azure AI Foundry; (B) LangGraph; (C) Temporal | Debora + Plataforma APB | 🔴 Mes 1 |
| Broker de eventos inter-agente | Azure Service Bus (ya en stack, **recomendado**) vs. otra solución | Debora + Plataforma APB | 🟡 Mes 1 |
| Formato de eventos | CloudEvents + JSON (ya en stack, **recomendado**) vs. otro | Arquitectura APB | 🟡 Mes 1 |
| Alcance de Event Sourcing | Solo eventos de agente críticos vs. todo el pipeline vs. ninguno | Debora | 🟡 Mes 2 |
| Almacenamiento de estado de workflow | Redis (short-term) + Cosmos DB (state) — ya en plan §D.1 | Plataforma APB | 🟡 Mes 2 |
| Estrategia de reintentos | Máximo de reintentos + escalado humano (cuántos, quién recibe) | Debora | 🟡 Mes 2 |

#### Trabajo de análisis previo a implementar (Sesión de Análisis de Orquestación)

Antes de construir nada, realizar:

1. **PoC comparativo** de las opciones de orquestación macro sobre un caso de uso real APB
   (candidato: `apb-wf-sdd-full-v1.0` como primer workflow a orquestar):
   - Opción A — GitHub Action parametrizable que lee frontmatter YAML y pausa en `human_checkpoints`
     vía GitHub Environments. Esfuerzo estimado: 1-2 días. Recomendado como primer paso (`E-T1`).
   - Opción B — `orchestrator.py` con log de ejecución local. Esfuerzo: 1 semana.
   - Opción C — Azure Durable Functions (nativo Azure). Esfuerzo: 2-3 semanas.
   - Opción D — LangGraph con checkpoints (solo si C no es viable). Esfuerzo: 2-3 semanas + infra.

2. **Verificar capacidades existentes** antes de construir:
   - `apb-orch-multi-agent-v1.0`, `apb-orch-context-handoff-v1.0`, `apb-orch-human-checkpoint-v1.0`
     (ya creadas en Sesión 21). ¿Qué parte del problema ya resuelven?
   - `invoke_agent.py` (esqueleto existente). ¿Hasta dónde llega?
   - `prov-servicebus-v1.0` (provider existente). ¿Cubre el caso de eventos inter-agente?

3. **Definir los contratos de eventos** antes de implementar la capa de coreografía:
   - Esquema CloudEvent por tipo de evento: `code.generated`, `ci.trigger`, `ci.completed`,
     `pr.review.requested`, `pr.review.completed`, `bug.classified`, etc.
   - Qué campos son obligatorios en `data:` por tipo de evento.
   - Quién es productor y quién es consumidor de cada evento.

#### Componentes a construir (tras decisión arquitectónica)

**Fase de Coreografía (bajo riesgo — Azure Service Bus ya en stack):**

| Componente | Tipo | Descripción |
|------------|------|-------------|
| `apb-orch-event-schema-v1.0` | skill | Esquemas CloudEvents para los eventos del pipeline de desarrollo: `code.*`, `ci.*`, `pr.*`, `bug.*`, `deployment.*` |
| `apb-orch-event-router-v1.0` | skill | Reglas de enrutamiento: qué agente reacciona a qué evento, condiciones de activación, timeout por evento |
| `prov-orchestration-engine-v1.0` | provider | Adaptador al motor de orquestación elegido (Azure Durable Functions / LangGraph). Abstrae el runtime para que skills/agentes no dependan del motor concreto | 
| `apb-sub-orch-ci-bridge-v1.0` | subagente | Puente CI/CD: convierte eventos del framework en `repository_dispatch` de GitHub Actions y procesa `ci.completed` de vuelta al workflow pausado |

**Fase de Orquestación macro (tras PoC):**

| Componente | Tipo | Descripción |
|------------|------|-------------|
| `apb-wf-agent-pipeline-v1.0` | workflow | Workflow de referencia orquestado: PM → Arch → Dev → CI → Review → Deploy, con gates humanos en cada transición de fase |
| `apb-wf-bug-to-fix-v1.0` | workflow | Bug report → Triage → Dev fix → CI → Review → Deploy, con escalado a humano si reintentos fallidos |

**Agente coordinador (fase avanzada — tras orquestación funcionando):**

| Componente | Tipo | Descripción |
|------------|------|-------------|
| `apb-agent-orchestrator-v1.0` | agente | Agente que gestiona el estado global de un workflow activo: pausa en gates humanos, reanuda tras eventos CI, detecta timeouts, escala a humano si se excede el máximo de reintentos. Delega en agentes especializados, no ejecuta lógica de dominio directamente |

**Dashboard de orquestación** (construir sobre base Sesión 17 #39/#40):

- Pipeline de estado de workflows activos en Power BI / DevExpress.
- Stream de eventos CloudEvent con filtros.
- Panel de aprobaciones humanas pendientes (gates activos).

#### Stack recomendado para APB (decisión pendiente de Debora)

| Componente | Tecnología recomendada | Justificación |
|------------|----------------------|---------------|
| Motor orquestación macro | **Azure Durable Functions** (primera opción) / LangGraph (fallback) | Native Azure, sin infraestructura separada, compatible .NET + Python |
| Broker de eventos | **Azure Service Bus** | Ya en stack APB — sin nueva dependencia |
| Formato eventos | **CloudEvents + JSON** | Ya en stack APB |
| Estado de workflow | **Redis** (short-term) + **Cosmos DB** (long-term state) | Ya en plan D.1 |
| Observabilidad | **OpenTelemetry** → Azure Monitor → Power BI / Grafana | Conecta con Sesión 17 (#39/#40) |
| UI de monitoreo | **DevExpress** (JS puro) | Stack frontend APB estándar |

#### Relación con puntos existentes del plan

- **E-T1** (motor de orquestación real, §K.1): este punto #77 es la implementación completa de E-T1.
  E-T1 propone GitHub Action como primer paso; #77 amplía el análisis al ecosistema completo.
- **#41** (orquestación real entre agentes, Sesión 13): #77 es la concreción de ese punto.
- **#29** (loop engineering): los reintentos y loops de iteración forman parte del motor de orquestación.
- **#12** (definición de loops): ídem.
- **#24** (Goal-Driven Execution): el motor de orquestación es el mecanismo que ejecuta los objetivos.
- **Recomendación consolidada de #41**: resolver #12, #24, #29 y #41 en la misma sesión — este punto
  #77 es la sesión donde todo eso converge en decisión + implementación.

#### Sesión asignada

**Sesión de Análisis de Orquestación** (nueva sesión propia, tras Sesión 13).

**Bloqueante:** decisión arquitectónica de Debora + Plataforma APB sobre el motor de orquestación
(Azure Durable Functions vs. LangGraph vs. otro). Sin esa decisión el PoC no puede completarse.

**Secuencia recomendada:**

1. Debora + Plataforma: decidir motor de orquestación (Mes 1).
2. Sesión de Análisis de Orquestación: PoC, contratos de eventos, verificación de capacidades existentes.
3. Construir capa de coreografía (Service Bus + CloudEvents) — bajo riesgo, puede ir en paralelo.
4. Construir `prov-orchestration-engine-v1.0` sobre el motor elegido.
5. Implementar `apb-wf-agent-pipeline-v1.0` como primer workflow orquestado real.
6. `apb-agent-orchestrator-v1.0` — solo tras validar el motor en producción.

---

## Bloque añadido 2026-07-02 (Debora — estándar de prompting, memoria, planes de pruebas, harness)

> Estado: **#78 y #83 ejecutados** (Sesión #78+#83, 2026-07-02 — ver
> [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md)). El resto (#79–#82, #84)
> sigue anotado, no ejecutado, hasta su sesión propia. Se cruzan explícitamente
> con contenido existente para evitar duplicación.

### 78. Estándar de prompting para TODOS los componentes — ✅ EJECUTADO
(Sesión #78+#83, 2026-07-02). Estándar canónico: `context/apb/standards/PROMPTING_STANDARD.md`
(10 ejes + 11 prohibiciones). 6 plantillas actualizadas, retrofit completo de 244 componentes,
check #18 del validador en ERROR. Detalle en [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).

### 79. Terceros a verificar/incorporar: MCP Builder, Fine Skills, Anthropic cybersecurity skills

- **MCP Builder** — **ya incorporado** como `third-anthropic-mcp-builder-v1.0`
  (Sesión 8). Acción: confirmar que el alcance incorporado cubre lo que
  Debora espera (¿construir MCPs propios de APB para providers como
  Teams/SharePoint del #30?), no re-incorporar.
- **"Fine Skills"** — fuente a identificar con precisión (¿`skills.sh`
  "fine skills", fine-tuning de skills, u otra fuente?). **Requiere que
  Debora aporte URL/organización exacta** antes de evaluar (mismo criterio
  que el bloque #27).
- **Anthropic cybersecurity skills** — evaluar el conjunto de skills de
  ciberseguridad de Anthropic para enriquecer el dominio `security` (cruzar
  con `apb-sec-threat-model-v1.0`, `apb-sec-ens-v1.0`,
  `apb-sec-risk-analysis-v1.0` y las skills de terceros ya presentes de
  `mukul975`, `openai/threat-model`, `garrytan/cso-owasp`). Verificar solape
  antes de incorporar.

**Cruce:** bloque #27 (terceros pendientes) y sección M.8. Se añaden como
filas de referencia en M. **Sesión candidata: Sesión 19** (terceros
pendientes de §8).

### 80. Memoria corporativa del framework (contexto + histórico + aprendizaje continuo + persistencia)

Configurar una **memoria propia del framework** que proporcione a los
agentes: (a) **contexto** de proyecto/dominio, (b) **histórico** de
decisiones y sesiones, (c) **aprendizaje continuo** (lecciones, correcciones
recurrentes), con **opción de memoria persistente** entre sesiones.

**Cruces (no duplicar — esto es una DECISIÓN de arquitectura, no un
componente suelto):**
- M.6 ya propone `HKUDS/LightRAG` (`wrap-hkuds-lightrag-v1.0`, definido, sin
  desplegar) y `mem0ai/mem0` (`wrap-mem0-v1.0`, pendiente) como candidatos a
  "memoria corporativa".
- Punto #23 / R6 / la línea 2071 ya prevén **memoria compartida
  inter-sesiones** (`prov-agent-memory-v1.0`: Redis short-term + Cosmos DB
  state + Git long-term), condicionada a la decisión de runtime.
- El modelo de **Harness Engineering (#83)** aporta el mecanismo concreto de
  persistencia versionada: `PROGRESS.md`, principios ACID de estado y
  Bootstrap Contract (ver §2 y §4 de #83). La "memoria persistente en Git"
  del harness y la "memoria episódica" de LightRAG/mem0 son **capas
  complementarias**, no alternativas: Git = durabilidad/auditoría;
  LightRAG/mem0 = recuperación semántica.

**Trabajo del punto:** decidir la arquitectura de memoria (¿Git+PROGRESS.md
como capa base obligatoria + LightRAG/mem0 como capa semántica opcional?),
no reabrir la elección de herramienta desde cero. **Sesión candidata:**
ligada a la decisión de runtime (misma que #77 Orquestación) porque la
memoria compartida depende del motor.

### 81. Obsidian como capa de conocimiento/memoria navegable

Evaluar **Obsidian** (vault Markdown local + grafo de enlaces) como:
- Interfaz humana de navegación sobre la memoria del framework (#80): el
  repo ya es Markdown enlazado, Obsidian lo convierte en grafo navegable sin
  transformación.
- Herramienta de visualización de dependencias entre componentes
  (`depends_on`/`consumed_by` de `SCHEMA.md`) vía backlinks/graph view.

**Cruce:** #80 (memoria) y bloque #27 (Excalidraw/context7 como
herramientas, no como skills). No es un componente del catálogo sino una
**herramienta de apoyo** — documentar como tal en M. Verificar que no
introduce una fuente de verdad paralela (Principio #4: la fuente de verdad
técnica es Git; Obsidian es solo proyección de lectura, como Confluence en
Principio #6). **Sesión candidata: Sesión 19** (junto con #79).

### 82. Metodología y plantilla corporativa de planes de pruebas

Elevar el plan de pruebas de "artefacto que genera una skill" a **proceso
gobernado con plantilla, histórico y trazabilidad**. Requisitos:

**a) Orden de fuentes obligatorio del agente de plan de pruebas:**
   1. **Rovo primero** — analiza los tickets de Jira y sus adjuntos, el
      análisis funcional y la documentación aportada por el usuario.
   2. **GitHub Copilot después** — ingeniería inversa del código para
      completar/contrastar lo funcional.
   (Es decir: lo funcional manda; el código se usa para verificar y
   completar, no como fuente primaria.)

**b) Detección de plan previo:** antes de generar uno nuevo, comprobar si ya
   existía un plan de pruebas. Si existe, **revisar cambios y actualizar
   desde la fecha del plan anterior** (no regenerar desde cero).

**c) Columna de trazabilidad por prueba:** cada caso lleva una columna que
   indica **qué funcional dio el OK** y **desde cuándo** se definió esa
   prueba en el plan.

**d) Secciones nuevas obligatorias del documento de plan:**
   - **Histórico de cambios del plan.**
   - **Aprobados del plan según cambios** (quién aprobó qué versión/cambio).
   - **Enlace bidireccional plan ↔ evidencias** (desde el plan a las
     evidencias de resultados y desde las evidencias al plan).
   - **Evidencias vinculadas a Jira.**

**e) Almacenamiento de resultados:** definir dónde se guardan — propuesta a
   confirmar con Debora: **en el repo de cada aplicación** (no en el repo del
   framework), con las evidencias enlazadas a Jira.

**f) Gobernanza y gestión del cambio** del plan de pruebas: proceso de
   aprobación de cambios, versionado, responsables.

**g) Plantilla de resultados esperados:** partir de **un ejemplo real que
   Debora facilitará** y convertirlo en plantilla. Todos los ejemplos
   incluyen: introducción funcional, integraciones, resumen de arquitectura
   topológica, relación de tablas y Spec — la plantilla debe contemplar
   estas secciones fijas.

**h) Verificación de no-regresión de rendimiento:** comprobar que el
   rendimiento **no empeora** respecto a la ejecución anterior del plan.
   Definir **dónde se consulta el resultado anterior**; y cuando **nunca se
   ejecutó antes**, ejecutar el plan **sobre la versión anterior del código
   y luego sobre la nueva** para obtener la comparativa. (Cruce con
   `prov-k6-v1.0` — carga/rendimiento.)

**i) Planes preliminares existentes:** Debora aportará un conjunto de
   **planes de pruebas preliminares** de ciertas aplicaciones; hay que
   dejarlos disponibles en el repo para el futuro y **actualizarlos con la
   nueva versión del agente**.

**Cruces (no duplicar):** skills `apb-qa-test-plan-v1.0` (marco
LCSP/ENS/RGPD/WCAG, ya tiene tabla de criterios de éxito),
`apb-qa-test-auto-v1.0`, wrapper `third-anthropic-playwright-v1.0`, workflow
`apb-wf-qa-evidence-v1.0`, adapter `adapter-rovo-v1.0`, provider `prov-k6-v1.0`.
Este punto **no crea otra skill de plan de pruebas**: amplía
`apb-qa-test-plan-v1.0` (columnas de trazabilidad, histórico, detección de
plan previo) + define la plantilla de resultados esperados + gobernanza.

**Bloqueantes (aportados por Debora):** el **ejemplo real** para la
plantilla (g) y los **planes preliminares** (i). **Sesión candidata:**
Sesión QA-2 propia (el volumen lo justifica).

### 83. Harness Engineering agnóstico de LLM — ✅ EJECUTADO
(Sesión #78+#83, 2026-07-02). Normativa permanente: `SYSTEM.md §10` (5 subsistemas, ACID,
routing files, WIP=1, Feature Lists) + `GOVERNANCE.md §8` (Pass-State Gating, 3 capas,
Clean State Handoff). Scaffolding en `repo-scaffold/harness-ready/` (AGENTS/PROGRESS/FEATURES/init_check).
Check #19 del validador (Cold-Start Test). Fuera de alcance aquí: OTel §83.7 (→ Sesión 17) y
arquitectura de 3 agentes ejecutable (→ #77). Detalle en [`PLAN_FASES_COMPLETADAS.md`](PLAN_FASES_COMPLETADAS.md).

### 84. Navegación agéntica para pruebas funcionales (gap detectado)

**Origen:** pregunta de Debora (2026-07-02) — "¿el framework puede abrir un
navegador para pruebas funcionales?". Respuesta: **parcial**. Existe
navegación *scripted* (Playwright) a nivel de diseño; **no existe**
navegación *agéntica/exploratoria* en vivo.

Estado actual:
- **Cubierto (diseño, `draft`, sin desplegar):** `prov-playwright-v1.0`
  (abre chromium/firefox/webkit, screenshots, trazas, simula interacciones),
  `third-anthropic-playwright-v1.0`, `apb-sub-qa-e2e-v1.0`,
  `apb-qa-test-auto-v1.0`, `apb-wf-qa-evidence-v1.0` → generan y ejecutan
  **tests Playwright escritos** (guion fijo).
- **Gap:** ningún componente permite que un agente **navegue la UI en vivo y
  de forma exploratoria** (abrir la app, "ver" la pantalla, rellenar
  formularios y decidir el siguiente paso sin guion) — la "agent browser
  skill" que menciona Debora.

**Propuesta:** cubrir el gap combinando **Playwright (pruebas scriptadas
reproducibles)** + una **skill de browser agéntico** para exploración en
vivo (candidatos a evaluar: Playwright MCP conducido por el agente,
computer-use / Claude-in-Chrome como referencia de patrón, siempre bajo el
principio agnóstico de LLM del #83). Definir la frontera: exploratorio para
descubrimiento/QA manual asistido; scriptado para regresión reproducible en
CI. **Sesión candidata:** Sesión QA-2 (junto con #82, comparten insumo de
plan de pruebas y evidencias).

---

## L. Fases de evolución del framework a medio/largo plazo

### Fase 1 — Consolidación (0–6 meses)

**Objetivo:** pasar de "framework diseñado" a "framework operativo".

**Indicadores de éxito:**
- ≥30 componentes en estado `approved`, incluyendo los 5 workflows principales
- APB-DOMAIN-CATALOG con ≥5 dominios core `approved`
- Telemetría activa — al menos un evento por sesión de agente en `APBFrameworkTelemetry_CL`
- Runbooks para `wf-sdd-full`, `wf-code-review`, `wf-qa-evidence`
- Primer agente ejecutado desde Teams vía M365 Copilot adapter por usuario no-Arquitectura
- Métrica "% en draft" < 90%

**Riesgos:**
- Ciclo de aprobación como cuello de botella por falta de tiempo. Mitigación: slots recurrentes de 1h semanal de revisión.
- ✅ APB-DOMAIN-CATALOG **desbloqueado (2026-06-30)**: inventario recibido + entrevista estructurada (`apb-sub-ddd-interview-v1.0`) ejecutada → 21 dominios de negocio `proposed`. Pendiente: aprobación de Arquitectura.

### Fase 2 — Adopción corporativa (6–18 meses)

**Objetivo:** el framework pasa a ser la plataforma de referencia usada por múltiples equipos.

**Indicadores de éxito:**
- Rovo Agents activos y usados por equipos de proyecto (no solo Arquitectura APB)
- Todos los proyectos nuevos arrancan con `wf-sdd-full`
- ≥3 proyectos legacy con análisis DDD documentado y aprobado en APB-DOMAIN-CATALOG
- Motor de orquestación real (E-T1) ejecutando ≥1 workflow por semana
- Agente de Change Management / ITIL operativo (E-F1) integrado con el proceso CAB real
- Agente de Data Governance / RGPD produciendo el RAT trimestralmente (E-F2)
- Dashboard de gobernanza en producción (E-G1)
- Métrica "% en draft" < 50%

**Riesgos:**
- Vibe coding sistémico: equipos generan código sin seguir proceso SDD. Mitigación: formación + validación en PR que exija spec previa (`apb-dev-grill-before-code-v1.0`).
- Proliferación sin gobernanza. Mitigación: `apb-agent-meta-builder-v1.0` requiere discovery previo; todo componente nuevo pasa por el proceso de contribución.

### Fase 3 — Madurez y expansión (18–36 meses)

**Objetivo:** el framework es infraestructura corporativa madura, no un proyecto.

**Indicadores de éxito:**
- 80% de componentes en `approved` o `deprecated` — `draft` es la excepción
- Contribuciones de equipos de proyecto al catálogo sin necesitar a Arquitectura como intermediario
- Agente de FinOps con ahorro medible y documentado (E-F3)
- Integración con sistemas core (GISPEM, Portal Docks, etc.) vía providers específicos
- Ciclo de revisión semestral automatizado sin intervención manual (E-G2)
- Metodología o templates publicados como referencia para otras autoridades portuarias
- Métrica "% de skills con reuso >1 agente" > 50%

**Riesgos transversales:**

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| LLM vendor lock-in | Media | Alto | Mantener los 4 adapters actualizados; no hardcodear behavior de un modelo en los prompts |
| Proliferación descontrolada (>500 en draft) | Alta | Medio | Activar proceso de aprobación cuanto antes; ratio máximo draft/approved |
| ~~APB-DOMAIN-CATALOG vacío en 12 meses~~ ✅ MITIGADO (2026-06-30): 21 dominios `proposed` | Baja | Crítico | Aprobación de Arquitectura + experto de negocio para fronteras |
| Obsolescencia de skills de terceros | Alta | Medio | E-S2 (supply chain verification en CI) + revisión anual |
| Resistencia cultural | Media | Alto | ROI con métricas reales desde telemetría; involucrar equipos en los primeros dominios |
| Cambio de modelo de IA | Alta | Bajo | Los adapters abstraen el modelo; actualizar el model string es tarea de horas |

---

## M. Repositorios de terceros de interés

> Evaluación y decisión de Arquitectura APB obligatoria antes de incorporar cualquier componente.
> No evaluar M.8 hasta que los bloqueos críticos (APB-DOMAIN-CATALOG, ciclo de aprobación) estén resueltos.

### M.1 Orquestación (gap E-T1)

| Repositorio | Licencia | Uso propuesto | Esfuerzo |
|-------------|---------|--------------|---------|
| `microsoft/semantic-kernel` | Apache 2.0 | Motor de orquestación multi-agente con soporte nativo Claude + .NET. Wrapper propuesto: `wrap-semantic-kernel-v1.0`. | 2-4 semanas |
| `langchain-ai/langgraph` | MIT | Orquestación con estado persistente y backtracking. Alternativa ligera si el stack .NET no es requisito. | 1-2 semanas |

### M.2 DDD y gestión de dominios (gap Domain Catalog vacío)

| Repositorio | Licencia | Uso propuesto |
|-------------|---------|--------------|
| `ddd-crew/context-mapping` | Verificar antes de usar | Plantillas para Context Mapping DDD. Compatible con `bounded-context-template.md` del Domain Catalog. |
| Metodología Event Storming | Referencia | Complemento para talleres presenciales. Documentar cómo conecta la salida del taller con `new-domain.sh`. |

### M.3 Seguridad y compliance (gaps E-S1, E-S2, E-S3)

| Repositorio | Licencia | Uso propuesto |
|-------------|---------|--------------|
| `aquasecurity/trivy` | Apache 2.0 | Escáner de vulnerabilidades en código, dependencias y manifiestos IaC. Step de CI: `trivy fs .`. También detecta secretos en código. |
| OWASP DevSecOps Guideline | CC BY-SA 4.0 | Controles aplicables a cada fase del SDLC. Material para enriquecer `apb-sec-threat-model-v1.0` y agentes de seguridad. |

### M.4 Observabilidad (gap telemetría no activa)

| Repositorio | Licencia | Uso propuesto |
|-------------|---------|--------------|
| `open-telemetry/opentelemetry-python` | Apache 2.0 | Estándar de industria para trazas distribuidas. Compatible con `DefaultAzureCredential`. Permite envío simultáneo a Azure Monitor y otros backends (Grafana, Jaeger). |

### M.5 Design System (gaps BUG-03, tipografía, mantenibilidad)

| Repositorio | Licencia | Uso propuesto |
|-------------|---------|--------------|
| `storybookjs/storybook` | MIT | Catálogo de componentes UI con ejemplos interactivos, documentación de props generada automáticamente y tests de accesibilidad (addon a11y — WCAG 2.1 AA, RD 1112/2018). Elimina mantenimiento manual de `visual-reference.html`. |

### M.6 Memoria y conocimiento de agentes

| Repositorio | Licencia | Uso propuesto | Estado en catálogo |
|-------------|---------|--------------|-------------------|
| `HKUDS/LightRAG` | Apache 2.0 | RAG + grafos de conocimiento. Memoria episódica entre sesiones (decisiones de arquitectura, lenguaje ubicuo de dominio). Candidato para "memoria corporativa" del framework. | Wrapper existente: `wrap-hkuds-lightrag-v1.0`. Falta desplegar y conectar. |
| `mem0ai/mem0` | Apache 2.0 | Alternativa más simple a LightRAG. SDK Python con backends PostgreSQL/Redis/Qdrant. Más fácil de operar en Azure. | Wrapper pendiente: `wrap-mem0-v1.0` |
| Obsidian (`obsidianmd`) | Freemium (app propietaria; vault = Markdown abierto) | Capa **humana** de navegación sobre la memoria del framework (#80/#81): grafo de backlinks sobre el repo Markdown ya enlazado; visualización de `depends_on`/`consumed_by`. **Solo proyección de lectura** — no fuente de verdad (Principio #4/#6). | Herramienta de apoyo, no componente de catálogo |

### M.7 Contratación pública LCSP (gap E-F4)

| Recurso | Uso propuesto |
|---------|--------------|
| Plataforma de Contratación del Sector Público (API REST, Ministerio de Hacienda) | Datos públicos de contratos: precios de referencia, pliegos adjudicados, proveedores habituales APB. Integrable como `prov-lcsp-v1.0` una vez recibido el briefing de Débora. |

### M.8 Repositorios pendientes de evaluación profunda

| Repositorio | Posible uso | Prioridad |
|-------------|------------|---------|
| `ComposioHQ/agent-orchestrator` | Alternativa de orquestación de agentes | Media |
| `ruvnet/ruflo` | Framework de agentes ligero | Baja |
| `affaan-m/ecc` | Pendiente de evaluación | Baja |
| `nexu-io/open-design` | Complemento para Design System | Baja |
| `ComposioHQ/awesome-claude-plugins` | Fuente de discovery de MCPs — no incorporar como componente | Referencia |
| `walkinglabs/learn-harness-engineering` | Modelo de Harness Engineering (12 lecciones) — base del punto #83. Insumo de gobernanza + scaffolding + checks de validación, no componente del catálogo | Alta (#83) |
| Anthropic **cybersecurity skills** | Enriquecer dominio `security` (#79). Verificar solape con `apb-sec-*` y terceros ya presentes (`mukul975/*`, `openai/threat-model`, `garrytan/cso-owasp`) antes de incorporar | Media (#79) |
| "Fine Skills" (fuente a identificar) | Pendiente de URL/organización exacta de Debora (#79) | A determinar |
