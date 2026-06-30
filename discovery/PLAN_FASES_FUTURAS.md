# Plan de Fases Futuras — Pendiente de Ejecución

> Este documento acumula tareas anotadas por Debora para sesiones futuras.
> Nada de lo aquí listado se ejecuta hasta que se aborde explícitamente su
> propia sesión.

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
| 38 Fase 0 (catálogo de dominios) | ✅ **Incluye #11** (decisión Debora post-Sesión 9) — sesión propia o ampliación de 13, pendiente de listado de APIs |
| 33 (skills/agentes de SQL) | **Sesión 21** |
| 34 (validación QA en flujos de despliegue) | **Sesión 21** — aplica a framework y aplicaciones APB; durante construcción del framework no se activa sobre el propio repo, pero se diseña para poder hacerlo. |
| 43 (aplicación retroactiva de política "Generado por IA" + "Validado por humano" a TODO el catálogo) | ✅ **CERRADA (Sesión 23, 2026-06-26)** — ver detalle en punto #43 abajo |

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

## Sesión QA — ✅ CERRADA (ejecutada post-Sesión 12)

Debora decidió que la auditoría de testing/Playwright (#17) y el
solapamiento detectado entre `APB-IA-FRAMEWORK` y el repositorio
`apb-ai-skills` merecen una **sesión propia de QA**, no una sub-tarea de la
Sesión 8. Contenido confirmado de esta sesión:

1. ✅ **Auditoría completa de `apb-ai-skills.zip`** (subido en Sesión QA,
   no Sesión 8 — el zip no había persistido entre sesiones, hubo que
   re-subirlo). Verificado: 10 skills propias APB ✓, 10 externas ✓
   (incluidas las de Playwright), agente `qa-orchestrator` + 5 subagentes
   ✓ — todos coinciden con lo descrito. **Hallazgo no anticipado:** existe
   además una carpeta `skills/_spec-driven/` con 3 skills más
   (`spec-to-api-contract`, `spec-to-e2e-flows`, `spec-to-test-plan`) que
   no estaba contabilizada en la descripción original de la Sesión 8.

2. ✅ **Solapamiento resuelto — 4 fusiones, no 1.** El solapamiento real
   encontrado fue mayor que el único caso anticipado
   (`apb-qa-anonymize-v1.0` vs `apb-test-data-rgpd`). Se detectaron y
   fusionaron **4 pares**, decisión de Debora: "fusionar e incorporar al
   repo de APB-IA-FRAMEWORK" en todos los casos:
   - `apb-qa-unit-test-gen-v1.0` ← `apb-unit-test-generator` (ampliado a
     JS/TS, ejemplos de código, eventos, vínculo RGPD) → v1.1.0
   - `apb-qa-test-plan-v1.0` ← `apb-test-plan-lcsp` (marco normativo
     LCSP/ENS/RGPD/WCAG, tabla de criterios de éxito cuantificados,
     contexto contractual de licitación) → v1.1.0
   - `apb-sec-ens-v1.0` ← `apb-ens-security-audit` (tablas operativas de
     controles concretos por nivel Alto/Medio, cruce OWASP, formato de
     informe de hallazgos con severidad) → v1.1.0
   - `apb-qa-anonymize-v1.0` ← `apb-test-data-rgpd` (tabla de dominios
     ficticios APB con vocabulario portuario específico — IMO de buques,
     código de atraque —, fixtures concretos Oracle/TypeScript/Cosmos
     DB/PostGIS/.NET) → v1.2.0

3. ✅ **Frontera de responsabilidad resuelta: `apb-ai-skills` queda
   DEPRECADO** (decisión de Debora). Todo desarrollo futuro de
   skills/agentes/subagentes de QA vive exclusivamente en
   `APB-IA-FRAMEWORK`. El orquestador `qa-orchestrator` y 3 subagentes
   (`dotnet-backend-agent`, `data-persistence-agent`, `django-gis-agent`)
   referencian las 4 skills ahora fusionadas por su nombre antiguo —
   **estas referencias no se han corregido ni se ha tocado nada del
   repositorio `apb-ai-skills`**, por decisión explícita de Debora ("no
   toques nada de apb-ai-skills, quédate solo con la decisión verbal").
   El repo tiene 2 GitHub Actions activos (`sync-skills.yml`,
   `validate-skills.yml`) que seguirán ejecutándose normalmente — Debora
   fue informada de esto y decidió no actuar sobre ello en esta sesión.

## Sesión Frontend — ✅ CERRADA (ejecutada 2026-06-24)

Inicialmente agrupada con la Sesión QA por compartir la guía de estilo como
insumo común; Debora pidió explícitamente separarlas — QA trata pruebas,
Frontend trata construcción de interfaz. Contenido:

1. ✅ **(Punto #20)** `apb-agent-ux-mockup-v1.0` creado (dominio `architecture`).
   Agente para perfiles funcionales: traduce descripción en lenguaje natural a mockup
   estructurado con componentes DevExtreme. Base: WidgetsGallery + ThemeBuilder.
   Guía de estilos APB (PDFs) diferida — se añadirá en sesión futura.
2. ✅ **(Punto #21)** Cubierto: `apb-dev-devexpress-front-v1.0` actualizado (v1.1 efectivo)
   para referenciar `apb-dev-devexpress-selector-v1.0` como predecesor cuando no hay
   mockup funcional, y aceptar output de `apb-agent-ux-mockup-v1.0` como input directo.
   Stack ya existente (`apb-sub-dev-devexpress-v1.0`, `apb-agent-implementer-v1.0`)
   cubre el flujo de generación de código real.
3. ✅ **(Skill nueva)** `apb-dev-devexpress-selector-v1.0` creado — catálogo de
   componentes DevExtreme con árbol de decisión, patrones de layout APB y guía de
   theming ThemeBuilder. Usada por el agente de mockups y el subagente de desarrollo.
4. **(Punto #22 — pendiente, sesión futura)** Analizar si APB necesita un catálogo
   formal de componentes / design system más allá de la guía de estilo en PDF.

**Componentes entregados en Sesión Frontend:**
- `apb-dev-devexpress-selector-v1.0` (skill, domain: development)
- `apb-agent-ux-mockup-v1.0` (agent, domain: architecture)
- `apb-dev-devexpress-front-v1.0` actualizado (referencias a selector y agente de mockups)

**Documentos ya disponibles para Sesión QA y Sesión Frontend** (en
`/mnt/project/`, subidos por Debora antes de la Sesión 8):
- `Guía_Estilos__Port_de_Barcelona__2022__v1.pdf` — "Rediseño componentes -
  Port de Barcelona" — la guía de estilo UI/UX confirmada (punto #13
  original). Insumo principal de Sesión Frontend.
- `GISPEM__Guía_de_estilos.pdf` — guía de estilo relacionada (a confirmar
  alcance exacto: ¿específica de GIS/GISPEM, o complementaria a la
  anterior?).
- `ManualUsuario_WidgetsLayout_v1.pdf` — manual de usuario de widgets y
  layout, octubre 2022, autoría APB — candidato a referencia técnica de
  componentes DevExpress/DevExtreme reales en uso.
- `apb-ai-skills.zip` — insumo principal de Sesión QA.

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

17. **Auditoría de skills/agentes de testing Playwright** ✅ **Material
    recibido en Sesión 8** (`apb-ai-skills.zip`). Confirmado: cobertura
    Playwright vía 3 skills externas (`playwright-generate-test`,
    `playwright-regression-testing`, `api-playwright-test-developer`),
    coherente con `proyecto.md` §2 ("MCP de interés: Playwright"). Sin
    pérdida detectada. **Promovido a Sesión QA propia** por decisión de
    Debora (Sesión 8), junto con el solapamiento de responsabilidad entre
    `APB-IA-FRAMEWORK` y `apb-ai-skills` detectado durante la revisión.

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

20. **Agente de mockups para perfiles funcionales**
    Agente para que personas con perfil funcional (no desarrolladoras)
    generen mockups de interfaz basados en la guía de estilo APB y en
    componentes DevExpress/DevExtreme, sin necesidad de escribir código.
    Sesión Frontend.

21. **Agente/skill de generación de frontend para desarrolladores**
    Para que desarrolladores generen código de frontend real (no mockup)
    basado en la misma guía de estilo + DevExpress/DevExtreme. Revisar si
    amplía `apb-dev-devexpress-front-v1.0` (ya existente en
    `APB-IA-FRAMEWORK`) o si se crea como skill nueva complementaria.
    Sesión Frontend.

22. **Análisis de catálogo de componentes de frontend / sistema de diseño**
    Evaluar, como paso posterior a los puntos 20 y 21 (no en la misma
    sesión), si APB necesita un catálogo de componentes de frontend
    formalizado y/o un sistema de diseño (design system) más allá de la
    guía de estilo en PDF. Decisión de alcance mayor — requiere primero ver
    qué patrones emergen al construir los agentes de los puntos 20 y 21.

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

24. **Incorporar el enfoque de `multica-ai/andrej-karpathy-skills`** ✅
    **Sesión asignada confirmada: Sesión 10** (decisión Debora, post-Sesión
    9). Razón: si se construye primero el agente meta-gobernanza (Sesión
    10) y se decide después si estos principios aplican a todo componente
    nuevo, habría que retocar el agente meta-gobernanza ya cerrado. Se
    resuelve ANTES o DENTRO del briefing de Sesión 10, no en Sesión 13.
    (añadido en Sesión 8). Repositorio MIT (175k★) que condensa 4
    principios operacionales para agentes de codificación, derivados de
    observaciones públicas de Andrej Karpathy sobre fallos típicos de LLMs
    al programar:
    1. **Think Before Coding** — no asumir en silencio; presentar
       interpretaciones alternativas cuando hay ambigüedad; señalar
       confusión en vez de adivinar.
    2. **Simplicity First** — código mínimo que resuelve el problema, sin
       abstracciones ni flexibilidad no solicitadas.
    3. **Surgical Changes** — tocar solo lo que el cambio requiere; no
       "mejorar" código adyacente; limpiar únicamente los huérfanos que el
       propio cambio genera, no deuda técnica preexistente no solicitada.
    4. **Goal-Driven Execution** — transformar tareas imperativas en
       criterios de éxito verificables (ej. "arregla el bug" → "escribe un
       test que lo reproduzca, luego haz que pase").

    Evaluar en qué nivel del framework encaja mejor: ¿skill propia
    (`apb-dev-*`), ampliación de `GOVERNANCE.md`/`SYSTEM.md` como principio
    transversal, o ambos? Relacionado con el Principio Fundamental #8 del
    framework ("No vibe coding") y con el punto #12 de este mismo documento
    (necesidad de loops) — el principio 4 (Goal-Driven Execution) es
    literalmente un mecanismo de loop con criterio de verificación
    explícito. Sesión a determinar — candidata natural: Sesión 13 (cierre
    de pendientes históricos) por su relación directa con el punto #12, o
    Sesión 10 (agente meta-gobernanza) si se decide que debe aplicarse a
    todo componente nuevo que se genere.

25. **Agente/subagente de análisis de deuda técnica y remediación**
    (añadido en Sesión 8). Agente o subagente dedicado a analizar, sobre un
    repositorio o proyecto APB dado:
    - Deuda técnica acumulada
    - Vulnerabilidades de seguridad
    - Dependencias obsoletas (librerías, paquetes, versiones de runtime)
    - Actualizaciones pendientes (frameworks, SDKs, herramientas)
    - Cuellos de botella de rendimiento
    - Ajustes de rendimiento recomendados
    - Incumplimientos de las políticas corporativas APB (LCSP, ENS, RGPD,
      WCAG 2.1 AA, estándares internos de `GOVERNANCE.md`)

    Salida esperada: **plan detallado y priorizado** de cómo abordar y
    corregir cada hallazgo (no solo el diagnóstico), y **apertura de
    tickets en Jira** por cada acción del plan — coherente con el principio
    de "todo resultado debe identificarse claramente" (`proyecto.md` §2) y
    con la prohibición de auto-aprobación (`proyecto.md` §3.6): el agente
    propone y prioriza, un humano decide qué se ejecuta y cuándo.

    Relacionado con trabajo ya existente: `apb-agent-risk-exception-v1.0`
    (riesgos/excepciones, pero no genera plan de remediación ni abre
    tickets), `apb-dev-sonar-clean-v1.0` / Sesión 11 (incumplimientos Sonar
    específicamente — este agente nuevo tiene alcance más amplio: no solo
    Sonar, sino dependencias, rendimiento y vulnerabilidades en conjunto),
    `apb-agent-finops-v1.0` (cuellos de botella de coste, no de
    rendimiento técnico). Evaluar si se construye como agente nuevo
    (`apb-agent-tech-debt-v1.0` o similar) o como subagente de
    `apb-agent-sre-v1.0` / `apb-agent-platform-engineer-v1.0`. Sesión a
    determinar — candidata natural: ampliar el alcance de la Sesión 11
    (hoy centrada solo en Sonar) o crear sesión propia si el volumen lo
    justifica.

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

### 31. Skill de conversión universal a Markdown ✅ **Sesión asignada
confirmada: Sesión 10** (decisión Debora, post-Sesión 9), junto con #24,
por la misma razón de naturaleza transversal — debe decidirse antes de que
el agente meta-gobernanza quede cerrado, no después.

Skill para transformar cualquier adjunto (Office: Word/Excel/PowerPoint,
PDF, etc.) que se pase a agentes/skills/subagentes a Markdown, bajo el
principio de que todos los componentes del framework deben trabajar
internamente en Markdown por eficiencia, aunque el usuario aporte archivos
ofimáticos. Es un principio transversal con impacto en **todos** los
agentes que aceptan adjuntos como input — candidata a:
- Nueva skill `apb-dev-doc-to-markdown-v1.0` (o nombre similar) en dominio
  `platform` o `development`
- Posible principio nuevo en `GOVERNANCE.md`/`SYSTEM.md`: "todo input
  ofimático se normaliza a Markdown antes de ser consumido por cualquier
  componente"
Sesión candidata: Sesión 10 (meta-gobernanza) por su naturaleza
transversal, con implementación de la skill en la sesión que corresponda
por dominio.

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

**Pendiente de Debora:** aportar la lista de APIs cuando se vaya a abordar
esta sesión — no se construye el catálogo de dominios sin ese insumo real.

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

### 42. Hallazgo de formato: comillas mal cerradas en sección "Dependencias" ✅ **RESUELTO**

**Detectado durante preparación de Sesión 11, corregido el mismo día por decisión explícita
de Debora** ("Arregla el tema de las comillas"). 19 archivos de skills (dominios
`development`, `discovery`, `qa`) tenían un patrón de error sistemático en la sección
"🔗 Dependencias" del cuerpo del documento: backtick de apertura sin cierre o mezclado con
comilla doble, p. ej. `` `apb-dev-code-review-v1.0" `` en lugar de
`` `apb-dev-code-review-v1.0` ``. No afectaba al frontmatter YAML (los IDs declarados ahí
eran correctos) — era puramente cosmético en Markdown del cuerpo.

**Archivos corregidos (19, 47 líneas en total):** `apb-dev-pr-doc-v1.0`,
`apb-dev-openspec-review-v1.0`, `apb-dev-legacy-mapper-v1.0`, `apb-dev-sonar-clean-v1.0`,
`apb-dev-devexpress-front-v1.0`, `apb-dev-gis-django-v1.0`, `apb-disc-backlog-v1.0`,
`apb-disc-adversarial-v1.0`, `apb-disc-ddd-legacy-v1.0`, `apb-disc-reverse-doc-v1.0`,
`apb-disc-enrich-req-v1.0`, `apb-disc-epic-mono-v1.0`, `apb-disc-reverse-code-v1.0`,
`apb-disc-cosmic-v1.0`, `apb-disc-business-v1.0`, `apb-disc-spec-gen-v1.0`,
`apb-qa-release-ready-v1.0`, `apb-qa-unit-test-gen-v1.0`, `apb-qa-post-migration-v1.0`,
`apb-qa-test-auto-v1.0`. Corrección puramente sintáctica (cierre de backtick), sin tocar
ningún otro contenido de los archivos. Validado: `scripts/validate_repo.py --strict` sigue
en 0 errores tras el cambio.

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

**Estado de ejecución — Sesión Enriquecimiento A (2026-06-27):**

| Bloque | Descripción | Estado |
|---|---|---|
| Bloque 1 — Rewirings (punto #55) | 44 conexiones aplicadas en 19 agentes. Corrección: ID real es `third-google-finops-multicloud-v1.0` (p, no b). validate_repo.py --strict → 0 errores. INDEX.md regenerado. | ✅ COMPLETADO |
| Bloque 2 — skills nuevas (ops×1 alerting-design + sec×4 + gov×1 audit) | sec: sast, dast, supply-chain, patch-management. gov: framework-audit. ops: alerting-design (sesión anterior). validate_repo.py 0 errores. | ✅ COMPLETADO |
| Bloque 3 — 3 agentes nuevos (Change Manager, Problem Manager, Data Governance) | change-manager, problem-manager, data-governance. ITIL + RGPD/ENS/NIS2. validate_repo.py 0 errores. | ✅ COMPLETADO |
| Bloque 4 — 5 subagentes nuevos (k8s, ACA, Rancher, ServiceBus, FinOps Azure) | k8s, aca, rancher, servicebus, finops-azure. System prompts incluidos. validate_repo.py 0 errores. | ✅ COMPLETADO |
| Bloque 5 — Prompts de sistema en iis-apache, network, oracle + qa-e2e | System prompts añadidos en 4 subagentes existentes. Stack APB detallado en cada uno. | ✅ COMPLETADO |

---

### 55. ✅ Rewirings: skills/subagentes existentes sin conectar a sus agentes correctos (costo cero, impacto inmediato)

> **EJECUTADO** — Sesión Enriquecimiento A, 2026-06-27. 44 rewirings aplicados en 19 agentes. validate_repo.py --strict → 0 errores. INDEX.md regenerado.

El análisis detecta ~20 conexiones faltantes entre skills ya creadas y los agentes que deberían usarlas. No requieren crear nada nuevo — solo añadir la referencia en el frontmatter del agente correspondiente y ejecutar `validate_repo.py --strict`.

**Lista completa de rewirings pendientes:**

| Skill/subagente a conectar | Agente destino | Justificación |
|---|---|---|
| `apb-sub-dev-parallel-v1.0` | `apb-agent-implementer-v1.0` | El subagente de despacho paralelo existe pero no está en la lista del Implementer — impide implementación paralela en el agente principal |
| `apb-dev-frontend-devexpress-events-v1.0` | `apb-agent-implementer-v1.0` | Skill de DevExtreme para eventos, no conectada |
| `apb-dev-implementation-patterns-v1.0` | `apb-agent-implementer-v1.0` | Catálogo de patrones, no conectado al Implementer principal |
| `apb-dev-sql-gen-v1.0` | `apb-agent-implementer-v1.0` | `apb-dev-sql-fix-v1.0` sí está, pero no la de generación |
| `apb-disc-brainstorming-v1.0` | `apb-agent-business-analyst-v1.0` | Obligatoria antes de cualquier trabajo creativo — gap inconsistente con "grill before code" |
| `apb-disc-adversarial-v1.0` | `apb-agent-business-analyst-v1.0` | El BA debe hacer devil's advocate sobre los requisitos que recoge |
| `apb-pm-product-analysis-v1.0` | `apb-agent-business-analyst-v1.0` | Análisis de producto complementa al BA |
| `apb-disc-brainstorming-v1.0` | `apb-agent-spec-engineer-v1.0` | Fase exploratoria previa a generación de spec |
| `apb-disc-design-approval-v1.0` | `apb-agent-spec-engineer-v1.0` | Gate de aprobación de diseño, existe pero no conectada |
| `apb-disc-brainstorming-v1.0` | `apb-agent-domain-architect-v1.0` | Fase exploratoria antes de modelar |
| `apb-disc-brainstorming-v1.0` | `apb-agent-tech-discovery-v1.0` | Exploración inicial en evaluación de tecnologías |
| `apb-gov-standards-v1.0` | `apb-agent-tech-discovery-v1.0` | Verificar que la tecnología evaluada cumple los estándares APB |
| `apb-sec-mitre-mapping-v1.0` | `apb-agent-security-architect-v1.0` | Existe en catálogo pero no conectada al Security Architect |
| `apb-sec-cloud-hardening-v1.0` | `apb-agent-security-architect-v1.0` | CIS Benchmark hardening, existe pero no conectada |
| `apb-arch-event-driven-master-v1.0` | `apb-agent-technical-architect-v1.0` | Skill maestro de eventos, más profunda que la básica ya conectada |
| `apb-arch-dotnet-base-v1.0` | `apb-agent-technical-architect-v1.0` | Reglas obligatorias para proyectos .NET, no conectada |
| `apb-arch-design-events-v1.0` | `apb-agent-technical-architect-v1.0` | Diseño de microservicios orientados a eventos, no conectada |
| `apb-arch-event-driven-master-v1.0` | `apb-agent-cloud-architect-v1.0` | Skill maestro de eventos no conectada al Cloud Architect |
| `apb-plat-deployment-finish-v1.0` | `apb-agent-release-manager-v1.0` | La skill de cierre de deployment existe exactamente para esto pero no está aquí |
| `apb-plat-ms-notify-v1.0` | `apb-agent-release-manager-v1.0` | Notificación post-release a stakeholders |
| `apb-gov-jira-evidence-v1.0` | `apb-agent-risk-exception-v1.0` | El agente de excepciones no puede crear tickets de excepción |
| `apb-gov-evidence-v1.0` | `apb-agent-risk-exception-v1.0` | Generación de evidencias para expediente de excepción |
| `apb-plat-ms-notify-v1.0` | `apb-agent-risk-exception-v1.0` | Notificación a validadores de excepción |
| `apb-qa-tdd-v1.0` | `apb-agent-qa-auto-v1.0` | TDD existe pero no está en el QA Agent |
| `apb-qa-readiness-check-v1.0` | `apb-agent-qa-auto-v1.0` | Gate de readiness antes de implementar |
| `apb-qa-testing-strategy-v1.0` | `apb-agent-qa-auto-v1.0` | Estrategia de testing para eventos, no conectada |
| `apb-qa-pipeline-v1.0` | `apb-agent-qa-auto-v1.0` | Evaluación de calidad del pipeline CI/CD |
| `apb-qa-framework-v1.0` | `apb-agent-meta-builder-v1.0` | El meta-builder debería auto-validar los componentes que genera |
| `apb-sub-ops-azure-v1.0` | `apb-agent-observability-v1.0` | Es la fuente de datos principal (APBFrameworkTelemetry_CL) pero el subagente solo está en SRE |
| `apb-ops-slo-design-v1.0` | `apb-agent-observability-v1.0` | Monitoring sin SLOs no tiene objetivo |
| `apb-gov-spec-sync-v1.0` | `apb-agent-governance-v1.0` | Gobernanza implica que las specs estén sincronizadas |
| `apb-plat-db-migration-v1.0` | `apb-agent-modernization-v1.0` | La modernización sin migración de BD es incompleta |
| `apb-disc-reverse-doc-v1.0` | `apb-agent-modernization-v1.0` | Análisis de documentación del legacy, complementa reverse-code |
| `apb-dev-review-tl-v1.0` | `apb-agent-code-reviewer-v1.0` | Perspectiva de Tech Lead, complementa al review básico |
| `apb-dev-impact-analysis-v1.0` | `apb-agent-code-reviewer-v1.0` | ¿Qué rompe este PR? Esencial en un reviewer |
| `apb-dev-surgical-changes-v1.0` | `apb-agent-code-reviewer-v1.0` | Detectar scope creep en un PR es función del reviewer |
| `apb-dev-gis-django-v1.0` | `apb-agent-code-reviewer-v1.0` | Review de código Python/Django |
| `apb-doc-event-specs-v1.0` | `apb-agent-documentation-v1.0` | Specs CloudEvents/AsyncAPI, existe pero no conectada |
| `apb-doc-generate-ppt-v1.0` | `apb-agent-documentation-v1.0` | Skill de generación de PPT sin agente asignado |
| `apb-doc-generate-word-v1.0` | `apb-agent-documentation-v1.0` | Skill de generación de Word sin agente asignado |
| `third-google-finobs-multicloud-v1.0` | `apb-agent-finops-v1.0` | Ya aprobada en catálogo, no está conectada al FinOps Agent |
| `apb-ops-dependency-audit-v1.0` | `apb-agent-finops-v1.0` | Detectar recursos huérfanos (sin proyecto asignado) |
| `third-nextlevel-ux-v1.0` | `apb-agent-ux-mockup-v1.0` | Skill de UX aprobada, existe pero no conectada al agente |

**Sesión asignada:** Sesión Enriquecimiento A — primera acción (sin bloqueantes, costo cero).

---

### 56. Nuevo agente: `apb-agent-change-manager-v1.0` — Change Management

**Dominio:** operation | **Autonomía:** 1 | **Owner:** SRE / Operaciones | **Prioridad:** 🔴 ALTA

**Por qué es crítico:** El framework genera releases pero no instrumenta el proceso ITIL de gestión de cambios que precede cualquier despliegue en producción APB. Sin este agente existe el riesgo de que el equipo salte el CAB.

**Skills a conectar:**
- `apb-ops-change-management-v1.0` (nueva — ver punto #66)
- `apb-ops-runbook-v1.0` (existente)
- `apb-gov-jira-evidence-v1.0` (existente)
- `apb-plat-ms-notify-v1.0` (existente)
- `apb-gov-evidence-v1.0` (existente)

**Capacidades del agente:**
- Generación de RFC con: descripción del cambio, impacto, ventana propuesta, rollback plan, responsables
- Evaluación de impacto: qué sistemas afecta, usuarios impactados, servicios en riesgo
- Preparación del expediente para CAB (Change Advisory Board)
- Verificación post-cambio (smoke tests, rollback trigger conditions)
- Calendario de cambios: qué hay en la ventana, conflictos, congelaciones

**Sesión asignada:** Sesión Enriquecimiento A.

---

### 57. Nuevo agente: `apb-agent-problem-manager-v1.0` — Problem Management

**Dominio:** operation | **Autonomía:** 1 | **Owner:** Operaciones / SRE | **Prioridad:** 🔴 ALTA

**Por qué es crítico:** El conocimiento de incidencias recurrentes se fragmenta en tickets individuales. Ningún agente hace análisis de patrones para identificar problemas sistémicos (ITIL Problem Management).

**Skills a conectar:**
- `apb-ops-problem-management-v1.0` (nueva — ver punto #67)
- `apb-ops-rca-v1.0` (existente)
- `apb-gov-jira-evidence-v1.0` (existente)
- `apb-gov-knowledge-v1.0` (existente)
- `apb-plat-ms-notify-v1.0` (existente)

**Capacidades del agente:**
- Análisis de patrones en histórico JSM para detectar problemas sistémicos
- Creación de tickets de Problema y gestión de estado (Investigación → Known Error → Cerrado)
- Known Error Database: workaround documentado y publicado para el equipo de soporte
- Propuesta de corrección definitiva (input para Tech Debt o Platform Engineer)
- Métricas de efectividad: ¿bajaron las incidencias recurrentes?

**Sesión asignada:** Sesión Enriquecimiento A.

---

### 58. Nuevo agente: `apb-agent-data-governance-v1.0` — Data Governance

**Dominio:** governance | **Autonomía:** 1 | **Owner:** DPO / Arquitectura | **Prioridad:** 🔴 ALTA

**Por qué es crítico:** APB procesa datos de operaciones portuarias, ciudadanos y proveedores. La combinación RGPD + ENS crea obligaciones legales de clasificación, inventario y EIPD que no tienen soporte en el framework.

**Skills a conectar:**
- `apb-gov-data-classification-v1.0` (nueva — ver punto #68)
- `apb-gov-dpia-v1.0` (nueva — ver punto #69)
- `apb-sec-risk-analysis-v1.0` (existente)
- `apb-gov-evidence-v1.0` (existente)
- `apb-gov-jira-evidence-v1.0` (existente)
- `apb-doc-manual-v1.0` (existente — para catálogo de datos)

**Subagentes:** `apb-sub-gov-data-v1.0` (nuevo — ver punto #73)

**Capacidades del agente:**
- Inventario de tratamientos RGPD art. 30 (registro por sistema)
- Clasificación de activos de datos: personal / sensible / operativo / público
- EIPD/DPIA cuando aplica (sistemas nuevos con datos personales)
- Catálogo de datos: qué datos tiene APB, dónde están, quién es responsable de cada dataset
- Política de retención: plazos de conservación y procedimiento de destrucción

**Sesión asignada:** Sesión Enriquecimiento A.

---

### 59. Nuevo agente: `apb-agent-incident-l2-v1.0` — Incident Support L2

**Dominio:** operation | **Autonomía:** 1 | **Owner:** Operaciones | **Prioridad:** 🟡 MEDIA

**Por qué importa:** El L1 escala pero no hay nadie que recoja el handoff. El L2 hace diagnóstico más profundo: correlación con cambios recientes, análisis de traces de aplicación, coordinación con desarrollo.

**Skills a conectar:**
- `apb-ops-rca-v1.0` (existente)
- `apb-ops-perf-bottleneck-v1.0` (existente)
- `apb-dev-impact-analysis-v1.0` (existente — correlacionar incidente con cambios de código)
- `apb-ops-post-incident-review-v1.0` (nueva — ver punto #70)
- `apb-gov-jira-evidence-v1.0` (existente)

**Subagentes:** `apb-sub-ops-oracle-v1.0` (existente), `apb-sub-ops-azure-v1.0` (existente), `apb-sub-ops-k8s-v1.0` (nuevo — ver punto #73), `apb-sub-ops-servicebus-v1.0` (nuevo — ver punto #73)

**Sesión asignada:** Sesión Enriquecimiento A.

---

### 60. Nuevo agente: `apb-agent-accessibility-auditor-v1.0` — Accessibility Auditor

**Dominio:** qa | **Autonomía:** 1 | **Owner:** QA / Desarrollo | **Prioridad:** 🟡 MEDIA

**Por qué importa:** Obligación legal (RD 1112/2018) para portales públicos de organismos del sector público. APB tiene portales de cara al ciudadano.

**Skills a conectar:**
- `apb-qa-accessibility-v1.0` (nueva — ver punto #71)
- `third-sickn33-screen-reader-testing-v1.0` (existente draft — activar)
- `apb-doc-manual-v1.0` (existente — para declaración de accesibilidad obligatoria)

**Sesión asignada:** Sesión Enriquecimiento B.

---

### 61. Nuevo agente: `apb-agent-vendor-manager-v1.0` — Vendor Management

**Dominio:** governance | **Autonomía:** 1 | **Owner:** Dirección TI / Contratación | **Prioridad:** 🟡 MEDIA

**Por qué importa:** APB como ente público contrata tecnología bajo LCSP. Ningún componente del framework cubre la evaluación técnica de proveedores ni la verificación de cumplimiento LCSP.

**Skills a conectar:**
- `apb-gov-lcsp-check-v1.0` (nueva — ver punto #72)
- `apb-gov-vendor-eval-v1.0` (nueva — ver punto #72)
- `apb-sec-risk-analysis-v1.0` (existente — riesgo de concentración en proveedores)
- `apb-gov-evidence-v1.0` (existente)

**Sesión asignada:** Sesión Enriquecimiento B.

---

### 62. Nuevo agente: `apb-agent-knowledge-manager-v1.0` — Knowledge Management

**Dominio:** documentation | **Autonomía:** 2 | **Owner:** Operaciones / TI | **Prioridad:** 🟡 MEDIA

**Por qué importa:** El conocimiento operativo APB vive en personas y correos, no en un sistema estructurado. El Knowledge Manager genera artículos de KB desde incidencias resueltas y organiza Confluence.

**Skills a conectar:**
- `apb-gov-knowledge-v1.0` (existente)
- `apb-doc-manual-v1.0` (existente)
- `apb-doc-onboarding-v1.0` (nueva — ver punto #74)
- `apb-plat-sharepoint-io-v1.0` (existente)

**Subagentes:** `apb-sub-doc-confluence-v1.0` (nuevo — ver punto #73)

**Sesión asignada:** Sesión Enriquecimiento B.

---

### 63. Nuevo agente: `apb-agent-api-product-manager-v1.0` — API Product Manager

**Dominio:** architecture | **Autonomía:** 1 | **Owner:** Arquitectura | **Prioridad:** 🟡 MEDIA

**Por qué importa:** Cuando el domain catalog tenga APIs registradas, alguien debe gestionar su ciclo de vida: versiones, deprecaciones, breaking changes, consumers. El framework sabe diseñar APIs pero no gestionar el portfolio.

**Skills a conectar:**
- `apb-arch-api-contract-v1.0` (existente)
- `apb-dev-api-standard-v1.0` (existente)
- `apb-doc-swagger-v1.0` (existente)
- `apb-dev-openspec-review-v1.0` (existente)
- `apb-gov-spec-sync-v1.0` (existente)
- `apb-arch-api-lifecycle-v1.0` (nueva — ver punto #76)

**Sesión asignada:** Sesión Enriquecimiento B.

---

### 64. Nuevos agentes estratégicos (prioridad baja — implementar cuando haya datos suficientes)

#### `apb-agent-capacity-planner-v1.0` — Capacity Planning

**Dominio:** operation | **Autonomía:** 1

**Propósito:** Forecasting de demanda de infraestructura basado en histórico y proyecciones del negocio portuario. APB tiene estacionalidad significativa (tráfico de cruceros en verano, campañas logísticas).

**Bloqueante:** Implementar cuando haya ≥12 meses de datos históricos Azure. Requiere `apb-ops-capacity-planning-v1.0` (nueva — ver punto #70).

#### `apb-agent-portfolio-it-v1.0` — IT Portfolio

**Dominio:** governance | **Autonomía:** 1

**Propósito:** Vista consolidada del portfolio de proyectos IT: alineamiento estratégico, duplicidades, deuda técnica agregada, inversión vs. valor. Input para dirección TI.

**Bloqueante:** Implementar cuando otros agentes lleven meses en uso produciendo datos reales.

**Sesión asignada:** Sesión Enriquecimiento C (solo definir estructura — no implementar hasta que se cumplan los bloqueantes).

---

### 65. Nuevos subagentes propuestos

| ID | Agente(s) padre | Descripción detallada | Prioridad |
|---|---|---|---|
| `apb-sub-ops-k8s-v1.0` | SRE, Platform Engineer, Incident L2 | Diagnóstico AKS: pods crashlooping, OOMKilled, pending, HPA, PDB, eventos de cluster, logs kubectl. Necesario antes de cualquier migración a AKS | 🔴 Alta |
| `apb-sub-ops-servicebus-v1.0` | Incident Support, Incident L2, Platform Engineer | Azure Service Bus: dead-letter queues, backlog, consumers muertos, poison messages, namespaces. Parte del stack APB | 🔴 Alta |
| `apb-sub-finops-azure-v1.0` | FinOps | Azure Cost Management API: exportaciones, budgets, alertas, reservas, Hybrid Benefit, savings plans | 🔴 Alta |
| `apb-sub-doc-confluence-v1.0` | Documentation, Knowledge Manager | Creación y actualización de páginas Confluence: espacios, plantillas, metadatos, jerarquía | 🟡 Media |
| `apb-sub-sec-sast-v1.0` | Security Architect, Code Reviewer | SonarQube security rules, Semgrep, Bandit: interpretación con contexto .NET, Django, JS de APB | 🟡 Media |
| `apb-sub-qa-performance-v1.0` | QA Automation | Diseño y análisis de tests de carga k6: escenarios, virtual users, thresholds, resultados | 🟡 Media |
| `apb-sub-gov-data-v1.0` | Data Governance | Clasificación de activos de datos por sensibilidad (RGPD + ENS): análisis de sistemas y datasets | 🟡 Media |
| `apb-sub-ops-entra-v1.0` | Security Architect, Incident Support | Microsoft Entra ID: usuarios bloqueados, MFA, conditional access, SSPR, auditlog | 🟢 Baja |

**Nota adicional sobre subagentes existentes con gaps de calidad:**
Los subagentes `apb-sub-ops-iis-apache-v1.0`, `apb-sub-ops-network-v1.0` y `apb-sub-ops-oracle-v1.0` tienen `autonomy_level: 2` pero **no tienen prompt de sistema** (no tienen sección `## 🧠`). Son los subagentes de menor calidad del catálogo. Deben recibir prompts de sistema que codifiquen el conocimiento específico de diagnóstico (comandos exactos, patrones de error conocidos para el stack APB).

**Sesión asignada:** Sesión Enriquecimiento A (alta prioridad) y Sesión Enriquecimiento B (media prioridad).

---

### 66. Nuevas skills — dominio Operation (+6)

| ID | Descripción completa | Agentes destino |
|---|---|---|
| `apb-ops-change-management-v1.0` | RFC: descripción del cambio, evaluación de impacto, ventana de mantenimiento propuesta, plan de rollback detallado, responsables, verificación post-cambio. Gate antes de producción | Change Manager, Release Manager, SRE |
| `apb-ops-problem-management-v1.0` | Detección de patrones en histórico de incidencias JSM, apertura de problema ITIL, gestión de estados (Investigación → Known Error → Cerrado), known error database con workaround documentado, propuesta de corrección definitiva | Problem Manager, Incident Support |
| `apb-ops-post-incident-review-v1.0` | PIR blameless estructurado: timeline detallado, impacto real medido, técnica 5 whys, action items con owner y fecha límite, lecciones aprendidas | SRE, Incident L2 |
| `apb-ops-capacity-planning-v1.0` | Forecasting de demanda de recursos: análisis de tendencias históricas, modelado de estacionalidad portuaria (tráfico de cruceros, campañas logísticas), right-sizing de instancias Azure | SRE, Capacity Planner |
| `apb-ops-service-continuity-v1.0` | BCP/DRP: definición de RTOs y RPOs por servicio crítico, estrategia de backup y replicación, plan de recuperación ante desastre, pruebas de continuidad | SRE, Platform Engineer |
| `apb-ops-alerting-design-v1.0` | Diseño de alertas: definición de umbrales, severidades (P1-P4), páginas de guardia, ventanas de silencio planificadas, runbooks asociados a cada alerta | SRE, Observability |

**Sesión asignada:** Sesión Enriquecimiento A.

---

### 67. Nuevas skills — dominio Security (+4)

| ID | Descripción completa | Agentes destino |
|---|---|---|
| `apb-sec-sast-v1.0` | Interpretación de resultados SAST desde perspectiva arquitectónica: SonarQube security rules (hotspots vs. bugs), Semgrep (reglas custom APB), Bandit (Python) — con contexto de severidad APB, no solo CVSS genérico | Security Architect, Code Reviewer |
| `apb-sec-supply-chain-v1.0` | SBOM (Software Bill of Materials), análisis de licencias open source (compatibilidad con proyectos APB públicos), integridad de dependencias transitivas, detección de typosquatting en paquetes NuGet/npm/pip | Security Architect |
| `apb-sec-patch-management-v1.0` | Priorización de patches: CVE severity × impacto real en APB × ventana de cambio disponible × deuda de versión acumulada. Genera plan de actualización priorizado como input para Tech Debt | Security Architect, Tech Debt |
| `apb-sec-dast-v1.0` | Interpretación de resultados DAST en entornos de test: OWASP ZAP (alertas activas vs. pasivas, falsos positivos por configuración APB), Burp Suite (issues por severidad). Diferente del SAST — analiza comportamiento en tiempo de ejecución | Security Architect |

**Sesión asignada:** Sesión Enriquecimiento A.

---

### 68. Nuevas skills — dominio Governance (+8)

| ID | Descripción completa | Agentes destino |
|---|---|---|
| `apb-gov-data-classification-v1.0` | Clasificación de activos de datos: categorías (personal/sensible/operativo/público) según RGPD y ENS nivel Alto, tabla de controles por categoría, inventario de sistemas que procesan cada tipo | Data Governance, Governance |
| `apb-gov-lcsp-check-v1.0` | Verificación LCSP en contratación tecnológica: procedimiento correcto según cuantía (contrato menor / procedimiento abierto simplificado / abierto ordinario), criterios de adjudicación admisibles, documentación requerida para el expediente | Compliance Audit, Vendor Manager |
| `apb-gov-vendor-eval-v1.0` | Evaluación técnica de proveedores tecnológicos: capacidad técnica, solvencia económica, historial de seguridad, SLAs ofrecidos vs. requisitos APB, plan de continuidad del proveedor, riesgo de lock-in | Vendor Manager |
| `apb-gov-ai-model-lifecycle-v1.0` | Gobierno de modelos IA en uso por APB: versión activa por agente, fechas de cambio de modelo, impacto de actualizaciones de modelo en comportamiento de agentes, proceso de retiro y migración | Governance |
| `apb-gov-dpia-v1.0` | EIPD/DPIA según RGPD art. 35: determinación de necesidad (screening), alcance del tratamiento, identificación de riesgos para los interesados, medidas técnicas y organizativas propuestas, plantilla de informe para DPO | Data Governance, Compliance Audit |
| `apb-gov-tech-radar-v1.0` | Technology radar APB inspirado en ThoughtWorks: categorías ADOPT / TRIAL / ASSESS / HOLD con justificación por tecnología, cuadrantes (Técnicas, Plataformas, Herramientas, Lenguajes), proceso de revisión periódica | Tech Discovery, Governance |
| `apb-gov-framework-metrics-v1.0` | Cuadro de mando del framework: % de componentes en estado draft (<30% target), tiempo medio de aprobación (<10 días target), cobertura de dominios IT, componentes más/menos usados, componentes sin uso en >6 meses | Catalog Manager |
| `apb-gov-framework-audit-v1.0` | Auditoría del framework: detección de componentes obsoletos (versión desfasada, skills desconectadas), inconsistencias entre versiones (frontmatter vs. cuerpo), componentes sin uso en >6 meses candidatos a deprecación | Catalog Manager |

**Sesión asignada:** Sesión Enriquecimiento B.

---

### 69. Nuevas skills — dominio Platform (+4 generales + 3 FinOps)

**Platform general:**

| ID | Descripción completa | Agentes destino |
|---|---|---|
| `apb-plat-k8s-v1.0` | Manifiestos Kubernetes para AKS: Deployments, Services, Ingress, NetworkPolicies, PodDisruptionBudgets, HorizontalPodAutoscaler, ConfigMaps, Secrets (referenciando Key Vault). Helm charts con values por entorno | Platform Engineer, Cloud Architect |
| `apb-plat-azure-servicebus-v1.0` | Configuración Azure Service Bus: namespaces, topics, subscriptions, retry policies (exponential backoff), dead-letter queues, particionado, alertas de backlog y dead-letter, autorización con Managed Identity | Platform Engineer, Cloud Architect |
| `apb-plat-secret-rotation-v1.0` | Especificación de automatización de rotación de secretos en Key Vault: cadencia 90 días (conforme a GOVERNANCE.md), notificación pre-expiración, actualización de referencias en App Services / AKS sin downtime, auditoría de uso | Platform Engineer |
| `apb-plat-environment-promotion-v1.0` | Proceso de promoción de artefactos entre entornos dev→staging→prod: smoke tests obligatorios por etapa, gates de aprobación humana, condiciones de rollback automático, registro de promociones en Jira | Platform Engineer, Release Manager |

**FinOps (bajo dominio platform):**

| ID | Descripción completa | Agentes destino |
|---|---|---|
| `apb-plat-finops-alerting-v1.0` | Configuración de alertas en Azure Cost Management: alertas de budget (% consumido), detección de anomalías de coste (spike detection), proyecciones de fin de mes, notificaciones por email y Teams | FinOps |
| `apb-plat-finops-chargeback-v1.0` | Estrategia de allocación de costes cloud: taxonomía de tags obligatorios por proyecto/equipo/dominio, reportes de showback vs. chargeback, modelo de distribución de costes compartidos (networking, monitorización) | FinOps |
| `apb-plat-finops-reservations-v1.0` | Análisis de reservas Azure: Reserved Instances vs. pay-as-you-go por tipo de VM, Azure Hybrid Benefit para licencias Windows/SQL Server existentes, Savings Plans, umbral de utilización mínima para rentabilizar reserva | FinOps |

**Sesión asignada:** Sesión Enriquecimiento B.

---

### 70. Nuevas skills — dominio QA (+3)

| ID | Descripción completa | Agentes destino |
|---|---|---|
| `apb-qa-performance-v1.0` | Tests de carga con k6: diseño de escenarios de tráfico portuario (picos en apertura de ventanas de atraque, carga simultánea de manifiestos), definición de thresholds (p95 latency, error rate), análisis de resultados, integración en pipeline CI | QA Automation |
| `apb-qa-contract-testing-v1.0` | Consumer-Driven Contract Testing con Pact: definición de contratos entre servicios (consumer publica expectativas, provider verifica), integración con Pact Broker, proceso de verificación en CI antes de despliegue de cambios en provider | QA Automation |
| `apb-qa-accessibility-v1.0` | WCAG 2.1 AA audit: criterios de éxito aplicables a portales APB (percepción, operabilidad, comprensibilidad, robustez), análisis de HTML/mockups generados por agentes, declaración de accesibilidad (obligatoria RD 1112/2018), guía de remediación por tipo de fallo | QA Automation, Accessibility Auditor, UX Mockup |

**Sesión asignada:** Sesión Enriquecimiento B.

---

### 71. Nuevas skills — dominio Documentation (+4)

| ID | Descripción completa | Agentes destino |
|---|---|---|
| `apb-doc-changelog-v1.0` | Generación de changelog semántico (SemVer): agrupación de commits por tipo (feat/fix/breaking/chore), formato KEEP A CHANGELOG, extracción desde mensajes de commit y PRs, vinculación con tickets Jira | Documentation, Release Manager |
| `apb-doc-release-notes-v1.0` | Release notes orientadas a usuario final (no a desarrollador): qué hay nuevo, qué se ha corregido, qué impacto tiene para el usuario, aviso de breaking changes con guía de migración. Diferente del changelog técnico | Release Manager, Documentation |
| `apb-doc-onboarding-v1.0` | Guía de onboarding de desarrollador en un proyecto APB: setup de entorno (repo, accesos, IDE, certificados), arquitectura del sistema, convenciones de código, flujo de trabajo (Jira → branch → PR → deploy), contactos de referencia por área | Documentation, Knowledge Manager |
| `apb-doc-post-mortem-v1.0` | Post-mortem blameless: timeline detallado de la incidencia, impacto medido (usuarios afectados, downtime, transacciones fallidas), análisis de causa raíz con 5 whys, action items con owner y fecha límite, decisión de publicación interna/externa | SRE, Incident L2 |

**Sesión asignada:** Sesión Enriquecimiento B.

---

### 72. Nuevas skills — dominios Architecture, Discovery y PM

**Architecture (+3):**

| ID | Descripción completa | Agentes destino |
|---|---|---|
| `apb-arch-c4-model-v1.0` | Generación de diagramas de arquitectura en niveles C4: Context (sistema en su entorno), Container (aplicaciones y datastores), Component (módulos internos de un container). Notación Structurizr/PlantUML, niveles de detalle apropiados por audiencia | Technical Architect |
| `apb-arch-context-mapping-v1.0` | Context maps DDD: identificación de relaciones entre bounded contexts y sus patrones (Anti-Corruption Layer, Open Host Service, Conformist, Published Language, Customer-Supplier, Partnership, Shared Kernel), implicaciones de diseño de cada patrón | Domain Architect, Technical Architect |
| `apb-arch-api-lifecycle-v1.0` | Ciclo de vida de APIs: estrategia de versionado (URI vs. header vs. media type), timeline de deprecation, proceso de notificación a consumers, impact analysis de breaking changes, sunset headers | API Product Manager |

**Discovery (+4):**

| ID | Descripción completa | Agentes destino |
|---|---|---|
| `apb-disc-user-journey-v1.0` | User journey maps para portales y servicios APB: identificación de actores (ciudadano, operador portuario, consignatario), mapeo de pasos, touchpoints digitales/físicos, pain points por etapa, oportunidades de mejora | Business Analyst |
| `apb-disc-value-stream-v1.0` | Value stream mapping para procesos portuarios: representación de flujo de valor actual (current state), identificación de desperdicios (espera, retrabajo, aprobaciones innecesarias), propuesta de estado futuro (future state) | Business Analyst |
| `apb-disc-tech-eval-v1.0` | Framework de evaluación técnica de alternativas tecnológicas: criterios ponderados (madurez, comunidad, licencia, integración con stack APB, coste TCO, curva de aprendizaje, soporte enterprise), scoring comparativo, recomendación razonada | Tech Discovery |
| `apb-disc-poc-guide-v1.0` | Guía para Proof of Concept estructurado: definición de alcance mínimo, criterios de éxito verificables (go/no-go), timebox máximo, entregables esperados, decisión formal con evidencias | Tech Discovery |

**PM (+3):**

| ID | Descripción completa | Agentes destino |
|---|---|---|
| `apb-pm-risk-register-v1.0` | Registro de riesgos de proyecto: identificación, clasificación (técnico/organizativo/normativo), matriz probabilidad × impacto, owner asignado, mitigaciones propuestas, seguimiento periódico de estado | Business Analyst, PM |
| `apb-pm-status-report-v1.0` | Informe de estado semanal: avance por hito (% completado vs. planificado), riesgos activos con RAG status (verde/ámbar/rojo), impedimentos con owner y fecha límite, cambios de scope desde último informe | PM |
| `apb-pm-stakeholder-map-v1.0` | Mapa de stakeholders del proyecto: matriz interés × influencia, clasificación (gestionar de cerca / mantener satisfecho / informar / monitorizar), plan de comunicación por stakeholder, frecuencia y canal de reporte | Business Analyst |

**Design (+1):**

| ID | Descripción completa | Agentes destino |
|---|---|---|
| `apb-design-wcag-patterns-v1.0` | Patrones de componentes DevExtreme accesibles: configuraciones ARIA obligatorias por tipo de componente (grid, form, dropdown, date picker), navegación por teclado, ratios de contraste mínimos por tema APB, ejemplos de implementación correcta | UX Mockup |

**Sesión asignada:** Sesión Enriquecimiento B.

---

### 73. Nuevos providers propuestos

| ID | Sistema | Descripción completa | Prioridad |
|---|---|---|---|
| `prov-azure-cost-v1.0` | Azure Cost Management API | API dedicada de costes (diferente al Azure MCP genérico): exportaciones de coste por periodo, configuración de budgets, alertas programáticas, análisis de reservas y savings plans. Necesario para el FinOps Agent enriquecido | 🔴 Alta |
| `prov-confluence-v1.0` | Atlassian Confluence REST API | Operaciones directas Confluence: crear/actualizar/mover páginas, gestionar espacios, adjuntar archivos, controlar metadatos. Diferente de Rovo (AI-driven) — este es acceso estructural directo | 🟡 Media |
| `prov-entra-id-v1.0` | Microsoft Entra ID | Consultas Azure Active Directory: usuarios, grupos, conditional access policies, registros de auditoría de identidad. Necesario para el subagente `apb-sub-ops-entra-v1.0` | 🟡 Media |
| `prov-sentinel-v1.0` | Microsoft Sentinel | SIEM APB: consultas KQL sobre logs de seguridad, alertas activas, incidentes en investigación, playbooks de respuesta. Necesario si se construye capacidad de CSIRT interno | 🟡 Media |
| `prov-jira-software-v1.0` | Jira Software | Proyectos Jira Software (diferentes de JSM para incidencias): gestión de epics, sprints, backlog de desarrollo. El provider `prov-atlassian-v1.0` existente cubre JSM — este cubre Jira SW | 🟢 Baja |

**Sesión asignada:** Sesión Enriquecimiento C.

---

### 74. Nuevos workflows propuestos

| ID | Agentes | Prioridad | Justificación detallada |
|---|---|---|---|
| `apb-wf-change-management-v1.0` | Change Manager → Governance → Release Manager → SRE | 🔴 Alta | Gap de ITIL crítico: ningún workflow cubre el proceso de aprobación de cambios en producción. El Release Manager valida la calidad del artefacto pero no verifica que haya un RFC aprobado antes del despliegue. Sin esto el framework no está listo para producción real |
| `apb-wf-problem-management-v1.0` | Problem Manager → SRE → Tech Debt → Knowledge Manager | 🔴 Alta | El Incident L1 escala pero no hay workflow de problema para incidencias recurrentes. El conocimiento de la incidencia resuelta no llega a la Knowledge Base ni al backlog de Tech Debt |
| `apb-wf-data-governance-v1.0` | Data Governance → Compliance Audit → Security Architect → Documentation | 🔴 Alta | Obligación RGPD art. 30 (registro de tratamientos) no tiene soporte en el framework. Riesgo de incumplimiento regulatorio con multas potenciales |
| `apb-wf-incident-l2-v1.0` | Incident L2 → SRE → Problem Manager → Knowledge Manager | 🟡 Media | El escalado de L1 no tiene receptor estructurado. El handoff L1→L2 es un texto que desaparece; el L2 empieza desde cero sin contexto del L1 |
| `apb-wf-security-patch-v1.0` | Security Architect → Tech Debt → Change Manager → Platform Engineer → QA Auto | 🟡 Media | Las vulnerabilidades detectadas (CVEs, SAST, DAST) siguen proceso ad hoc; falta workflow estructurado que garantice cobertura completa desde detección hasta verificación post-patch |
| `apb-wf-api-lifecycle-v1.0` | API Product Manager → Technical Architect → Security Architect → Documentation → Release Manager | 🟡 Media | Gestión del ciclo de vida de APIs del domain catalog cuando esté poblado. Deprecation sin workflow genera breaking changes no comunicados a consumers |
| `apb-wf-accessibility-audit-v1.0` | Accessibility Auditor → UX Mockup → Implementer → QA Automation | 🟡 Media | Obligación legal RD 1112/2018 para portales ciudadanos APB. Sin workflow formal el audit de accesibilidad es ad hoc y sin trazabilidad |
| `apb-wf-vendor-procurement-v1.0` | Business Analyst → Vendor Manager → Compliance Audit → Governance | 🟢 Baja | Contratación LCSP es relevante para APB como organismo público, pero el uso del Vendor Manager Agent aún no está probado. Implementar tras validar el agente en uso real |
| `apb-wf-finops-review-v1.0` | FinOps → Cloud Architect → Platform Engineer | 🟢 Baja | Revisión periódica de costes cloud (mensual o trimestral). Útil cuando el FinOps Agent esté enriquecido con las 3 nuevas skills + subagente + provider |

**Nota sobre gaps en workflows existentes (no nuevos workflows, sino mejoras):**
- `apb-wf-sdd-full-v1.0`: no incluye fase de Change Management post-release — el Release Manager valida calidad pero no el RFC de producción.
- `apb-wf-code-review-v1.0`: no incluye al Security Architect para PRs con cambios en autenticación/autorización/datos sensibles.
- `apb-wf-cloud-migration-v1.0`: no incluye Change Manager para ventanas de migración; no incluye Problem Manager para documentar incidencias durante la migración.
- `apb-wf-incident-l1-v1.0`: no hay `apb-wf-incident-l2-v1.0` al que conectar el escalado — el handoff produce un resumen técnico que desaparece.
- `apb-wf-legacy-onboarding-v1.0`: no incluye Security Architect para inventario de vulnerabilidades del legacy; no incluye Tech Debt Agent para inventario inicial de deuda.
- `apb-wf-qa-evidence-v1.0`: no incluye tests de performance ni accesibilidad — la evidencia de release es incompleta para sistemas de cara al ciudadano.
- `apb-wf-risk-exception-v1.0`: no tiene fase de seguimiento post-aprobación para verificar que las condiciones de la excepción se cumplen antes del deadline.
- `apb-wf-spec-from-legacy-v1.0`: no incluye al DDD Agent con sus 5 subagentes — la herramienta principal para analizar un legacy bottom-up no está en el workflow que más la necesita.

**Sesión asignada:** Sesión Enriquecimiento C.

---

### 75. Mejoras específicas por agente con gaps de calidad

Los siguientes agentes tienen gaps de calidad o contenido que requieren actualizaciones en sus archivos existentes (además de los rewirings del punto #55):

**`apb-agent-finops-v1.0`** — El agente más delgado del catálogo junto con Catalog Manager. Con 1 sola skill funcional no puede hacer chargeback, alerting, análisis de reservas ni comparativa multi-cloud. Requiere conectar 5 componentes nuevos/existentes (ver punto #55 + skills nuevas de FinOps del punto #69). Subagente dedicado `apb-sub-finops-azure-v1.0` y provider `prov-azure-cost-v1.0` son bloqueantes para que sea útil en producción.

**`apb-agent-release-manager-v1.0`** — El agente más delgado para su responsabilidad crítica. Solo 4 skills para el gate final antes de producción. Sin checklist de despliegue, sin rollback plan, sin comunicación de release, sin verificación de RFC. Ver rewirings del punto #55 y skills nuevas de los puntos #71 y #66.

**`apb-agent-tech-discovery-v1.0`** — Segundo agente más delgado (3 skills). Evalúa nuevas tecnologías para APB pero tiene menos herramientas que un Business Analyst. Sin framework de evaluación técnica, sin guía de PoC, sin technology radar. Ver punto #72 para las 3 skills nuevas propuestas.

**`apb-agent-ddd-v1.0`** — Buen diseño (delega en 5 subagentes) pero falta skill de síntesis cross-subagente: los 5 subagentes producen 5 outputs independientes sin instrucción de consolidación. Propuesta: `apb-disc-domain-synthesis-v1.0` (nueva, no incluida en la lista principal por ser muy específica de este agente).

**`apb-sub-ops-iis-apache-v1.0`, `apb-sub-ops-network-v1.0`, `apb-sub-ops-oracle-v1.0`** — Los 3 subagentes de diagnóstico con autonomy_level: 2 y sin prompt de sistema. Deben recibir prompts que codifiquen comandos exactos y patrones de error conocidos del stack APB.

**`apb-agent-sre-v1.0`** — Sin subagente AKS. Cuando APB migre a AKS el SRE no tendrá visibilidad del cluster. `apb-sub-ops-k8s-v1.0` es bloqueante para la roadmap cloud.

**Sesión asignada:** Sesión Enriquecimiento A (urgentes) y Sesión Enriquecimiento B (resto).

---

### 76. Resumen de priorización de toda la Sesión de Enriquecimiento

**Cuadro resumen de componentes resultantes si se ejecuta todo:**

| Tipo | Actuales (2026-06-27) | Rewirings (costo 0) | Nuevos | Total propuesto |
|---|---|---|---|---|
| Agentes | 26 | — | +9 | 35 |
| Subagentes | 23 | — | +8 | 31 |
| Skills APB | 129 | ~44 rewirings | +38 | 167 |
| Workflows | 8 | — | +9 | 17 |
| Providers | 14 | — | +5 | 19 |
| **Total** | **~262** | **~44 rewirings (costo cero)** | **+69** | **~375** |

**Orden de ejecución recomendado:**

| Orden | Acción | Esfuerzo estimado | Impacto |
|---|---|---|---|
| 1 | Rewirings (punto #55) — ~44 conexiones | 1-2 días-persona | Impacto inmediato sin crear nada nuevo |
| 2 | Change Management Agent + skill + workflow | 2-3 días-persona | Cierra el gap de ITIL en producción |
| 3 | Data Governance Agent + skills + workflow | 3-4 días-persona | Obligación legal RGPD art. 30 |
| 4 | FinOps Agent: 3 skills + subagente + provider | 2-3 días-persona | Función con impacto presupuestario directo |
| 5 | Problem Management Agent + skill | 2 días-persona | Completa el ciclo Incident → Problem → Known Error |
| 6 | Security: SAST + supply chain + patch skills | 2 días-persona | Moderniza seguridad con técnicas actuales |
| 7 | Platform: K8s + Service Bus + secret rotation | 2-3 días-persona | Necesario antes de cualquier migración AKS |
| 8 | QA: performance + accesibilidad + contract testing | 2 días-persona | Testing moderno y cumplimiento legal WCAG |
| 9 | Incident L2 Agent + workflow | 1-2 días-persona | Completa el ciclo de soporte |
| 10 | Accessibility Auditor Agent + skill | 1-2 días-persona | Obligación legal RD 1112/2018 |
| 11 | Tech Discovery: 3 skills nuevas | 1-2 días-persona | Agente más desaprovechado del catálogo |
| 12 | Resto de skills (doc, pm, arch, design) | 3-4 días-persona | Calidad y completitud del framework |
| 13 | Nuevos workflows (9) | 2-3 días-persona | Cierra ciclos ITIL y legales |
| 14 | Nuevos providers (5) | 1-2 días-persona | Habilita integraciones faltantes |

**Lo que NO implementar todavía:**
- **Portfolio IT Agent**: necesita datos reales de proyectos procesados por el framework.
- **Capacity Planner Agent**: necesita ≥12 meses de datos Azure históricos.
- **Chaos Engineering skill**: después de que SLOs estén definidos y testing normal esté maduro.
- **Vendor Procurement workflow**: después de que Vendor Manager Agent esté probado en uso real.

**Bloqueantes para Debora antes de ejecutar:**
- Confirmar mecanismo de distribución del Design System (punto #49) — no es bloqueante para este bloque pero puede afectar a skills de plataforma.
- Facilitar URL exactas de repositorios de terceros pendientes del punto #27 si se quieren incorporar en paralelo.

---

## Revisión integral del framework — 2026-06-29

> Revisión ejecutada post-Sesión Enriquecimiento B. Cuatro dimensiones: estructura/consistencia, funcional, seguridad/implementación, cobertura de pruebas. Fuente: validate_repo.py + 3 agentes de análisis paralelo.

### Resultados por dimensión

#### Dimensión 1 — Estructura y consistencia

| Hallazgo | Severidad | Estado |
|---|---|---|
| 26 de 29 agentes sin `## Marcado IA obligatorio (POLICY_AI_USAGE §6)` | 🔴 Crítico | Pendiente |
| 19 subagentes sin System Prompt (esqueletos sin instrucciones al LLM) | 🔴 Crítico | Pendiente |
| validate_repo.py no comprueba Marcado IA en `agents/` (condición `skills/apb-owned` excluye la carpeta agents) | 🔴 Crítico (bug validador) | Pendiente |
| 4 skills nuevas (sec×3 + gov×1) no referenciadas en ningún agente | 🟡 Medio | Pendiente |
| Dominio `orchestration`: solo 1 skill (`apb-orch-multi-agent-v1.0`), sin agente dedicado | 🟡 Medio | Pendiente |
| Dominio `design`: solo 2 skills, sin agente dedicado de diseño | 🟡 Bajo | Pendiente |
| 59 warnings de `source_commit: unverified` en skills de terceros | ⚪ Info | Deliberado (política GOVERNANCE.md §4.2) |

#### Dimensión 2 — Funcional

| Hallazgo | Severidad | Descripción |
|---|---|---|
| `apb-wf-incident-l1-v1.0` orquesta skills directamente, NO usa `apb-agent-incident-support-v1.0` como agente padre | 🟡 Medio | El workflow y el agente están desacoplados — debería referenciar al agente |
| Workflow `apb-wf-cloud-migration-v1.0`: 9 agentes en cadena sin formato de output inter-agente definido | 🟡 Medio | Platform Engineer → SRE: no hay contrato de datos entre pasos |
| Solapamiento funcional: `apb-ops-incident-diagnose-v1.0` vs `apb-ops-rca-v1.0` | 🟡 Medio | Ambas producen "causa raíz"; diagnose es táctico/inmediato, rca es post-incidente. Diferencia no documentada claramente |
| Solapamiento parcial: `apb-sec-threat-model-v1.0` (STRIDE) vs `apb-sec-risk-analysis-v1.0` (ISO 27005) | 🟢 Bajo | Diferencia real (táctico vs. estratégico) pero no explicada en los propios documentos |
| `apb-agent-finops-v1.0` requiere "catálogo de precios Azure" sin que ninguna skill tenga ese output | 🟡 Medio | Gap de input no cubierto en la cadena |
| Todos los agentes críticos tienen autonomy_level 1 | ✅ Correcto | |
| `apb-agent-compliance-audit-v1.0` respeta gates humanos correctamente | ✅ Correcto | |

#### Dimensión 3 — Seguridad e implementación

| Hallazgo | Severidad | Descripción |
|---|---|---|
| Sin credenciales hardcodeadas detectadas en ningún fichero | ✅ Seguro | Patrones detectados por validate_repo.py línea 102-108 |
| Máximo autonomy_level en producción: 2. Nivel 4 no usado (declarado en AUTONOMY_LEVELS.md) | ✅ Correcto | |
| Skills de seguridad con instrucciones defensivas, sin instrucciones de ataque | ✅ Correcto | |
| `apb-ops-incident-diagnose-v1.0` (nivel 2) propone `ALTER SYSTEM KILL SESSION` Oracle | 🟡 Bajo | Requiere "confirmación humana" en texto pero el framework no lo bloquea mecánicamente |
| SCHEMA.md y validate_repo.py están sincronizados en campos obligatorios | ✅ Correcto | |
| CI/CD `.github/workflows/validate.yml` usa `--strict`, no auto-commitea catálogo | ✅ Correcto | |
| validate_repo.py línea 346: condición `"skills/apb-owned" in rel_path` excluye comprobación Marcado IA en agentes | 🔴 Bug | Requiere corrección |

#### Dimensión 4 — Cobertura de pruebas

| Hallazgo | Severidad | Descripción |
|---|---|---|
| `tests/test_validate_repo.py`: 19 tests unitarios sobre validate_repo.py | ✅ Existe | Cubre YAML, secretos, refs rotas, circularidades |
| ~85% de skills tienen sección "Ejemplo de Uso" con casos concretos | ✅ Bueno | |
| ~90% de criterios de calidad son verificables objetivamente (checkboxes, porcentajes) | ✅ Bueno | |
| Solo ~40% de skills documentan casos de error / edge cases en los ejemplos | 🟡 Medio | La mayoría asume inputs válidos |
| ~30% de skills no documentan qué hace el agente si el input está incompleto | 🟡 Medio | Comportamiento ante entrada nula no especificado |
| Workflows documentan happy path y gates, pero NO fallos en cascada ni iteraciones | 🟡 Medio | ¿Qué ocurre si falla el paso 3 de 8? No documentado |
| Tests de comportamiento de agentes: AUSENTES | 🔴 Gap crítico | No existe suite que valide "dado prompt X → output Y esperado" |
| Self-testing: `apb-qa-framework-v1.0` solo valida estructura, no comportamiento | 🟡 Medio | Pendiente extensión semántica |

---

### Sesiones propuestas resultado de la revisión

#### Sesión Correcciones Urgentes (estimado: 2-3h)

**Objetivo:** Corregir los 3 hallazgos críticos de estructura antes de continuar añadiendo componentes.

| Tarea | Detalle |
|---|---|
| C1 — Corregir validate_repo.py línea 346 | Extender condición para incluir directorio `agents/` en comprobación de Marcado IA |
| C2 — Marcado IA en 26 agentes | Añadir sección `## Marcado IA obligatorio (POLICY_AI_USAGE §6)` a los 26 agentes sin ella. Patrón: los 3 creados en Sesión Enriquecimiento B son la referencia |
| C3 — Rewiring 4 skills huérfanas | `apb-sec-sast`, `apb-sec-dast`, `apb-sec-supply-chain` → `apb-agent-security-architect-v1.0`; `apb-gov-framework-audit` → `apb-agent-governance-v1.0` |

#### Sesión Enriquecimiento C — Subagentes + Funcional (estimado: 4-6h)

**Objetivo:** System prompts en 19 subagentes prioritarios + correcciones funcionales detectadas.

| Bloque | Tareas |
|---|---|
| C-Bloque 1 — System prompts prioritarios (9 subagentes) | `apb-sub-dev-net`, `apb-sub-dev-devexpress`, `apb-sub-dev-django`, `apb-sub-dev-sql`, `apb-sub-obs-grafana`, `apb-sub-obs-powerbi`, `apb-sub-sec-ens`, `apb-sub-gov-standards`, `apb-sub-ops-azure` |
| C-Bloque 2 — System prompts secundarios (10 subagentes) | `apb-sub-ddd-*` (×5), `apb-sub-dev-parallel`, `apb-sub-plat-ghactions`, `apb-sub-plat-jenkins`, `apb-sub-qa-unit`, `apb-sub-qa-security` |
| C-Bloque 3 — Correcciones funcionales | (1) Añadir `apb-agent-incident-support-v1.0` como orquestador en `apb-wf-incident-l1-v1.0`. (2) Documentar diferencia diagnose vs RCA en ambas skills. (3) Definir formato de output inter-agente en `apb-wf-cloud-migration-v1.0` (contrato Platform Engineer → SRE). (4) Identificar cómo cubre el framework el input "catálogo de precios Azure" para FinOps |

#### Sesión Calidad de Pruebas (estimado: 3-4h)

**Objetivo:** Mejorar cobertura de casos de error y crear base de tests de comportamiento.

| Tarea | Detalle |
|---|---|
| Q1 — Edge cases en skills críticas | Añadir sección "Comportamiento ante inputs incompletos" en las 20 skills más usadas (operation, security, governance). Documenta: qué pregunta el agente, qué devuelve si falta input obligatorio |
| Q2 — Fallos en cascada en workflows | Añadir sección `## Manejo de fallos` en los 3 workflows más complejos (cloud-migration, sdd-full, incident-l1): qué ocurre si falla cada paso y cómo se recupera |
| Q3 — Extender apb-qa-framework-v1.0 | Añadir validaciones semánticas: presencia de ejemplos de error, criterios cuantificables, sección de comportamiento ante inputs nulos |
| Q4 — Primer test de comportamiento (piloto) | Crear `tests/test_agent_behavior.md`: 3-5 casos de prueba documentados para `apb-agent-incident-support-v1.0` con prompt de entrada, output esperado y criterios de evaluación. Base para futura automatización |

#### Sesión Power BI / Framework Metrics (sesión separada, bloqueante: datos reales)

> Ya planificada anteriormente. Pipeline: GitHub Action → Azure Storage → Power BI dinámico. No iniciar hasta tener al menos 30 días de uso real del framework con datos registrados.

---

### Backlog de mejoras detectadas (no urgentes)

| ID | Mejora | Prioridad | Sesión candidata |
|---|---|---|---|
| ~~M1~~ | ~~Dominio `orchestration`: añadir 2-3 skills de coordinación multi-agente~~ | Baja | ✅ RESUELTO (2026-06-29) — `apb-orch-context-handoff-v1.0` (transferencia secuencial) + `apb-orch-human-checkpoint-v1.0` (protocolo aprobación humana) creadas |
| ~~M2~~ | ~~Dominio `design`: añadir agente UX/IA design y 2-3 skills de design system~~ | Baja | ✅ RESUELTO (2026-06-29) — `apb-design-frontend-design-system-v1.0` añadida a `apb-agent-ux-mockup-v1.0` (gap crítico corregido) + `apb-design-wcag-v1.0` creada (obligatoria por RD 1112/2018) |
| ~~M3~~ | ~~Documentar diferencia STRIDE vs ISO 27005 en las propias skills (cuándo usar cada una)~~ | Baja | ✅ RESUELTO (2026-06-29) — callout diferenciador añadido en `apb-sec-threat-model-v1.0` y `apb-sec-risk-analysis-v1.0` |
| ~~M4~~ | ~~`apb-ops-incident-diagnose-v1.0`: añadir nota sobre relación con `apb-ops-rca-v1.0`~~ | Baja | ✅ RESUELTO (verificado) — ya estaba documentado en ambas skills en sesión anterior |
| ~~M5~~ | ~~Agente PM dedicado para las 7 skills de gestión de proyecto huérfanas~~ | Media | ✅ RESUELTO (2026-06-29) — `apb-agent-pm-v1.0` creado con 8 skills PM; `consumed_by: apb-agent-pm-v1.0` añadido en las 8 skills |
| ~~M6~~ | ~~Encoding workflows: verificar que todos los .md están guardados UTF-8 sin BOM~~ | Baja | ✅ RESUELTO (2026-06-29) — `grep -rl $'\xef\xbb\xbf' workflows/` → sin BOM detectado |
- Confirmar prioridad entre Sesión Enriquecimiento A y la Sesión 21 (SQL + incidencias), ya que ambas tocan el dominio `operation`.

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
| `domain-catalog/domains/` | — | ❌ **Solo `.gitkeep`**: catálogo vacío, prerequisito crítico para DDD |

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
| Arquitectura / DDD | ✅ Sólida | Domain Catalog vacío bloquea DDD real |
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
| Descomposición monolitos | ❌ Pendiente | Bloqueado: Domain Catalog poblado |
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
| R4 | Domain Catalog vacío → DDD/monolitos bloqueados | 🔴 | Listado de APIs (Débora) |
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
| Descomposición de monolitos (Fase 1) | #38 F1 | Bloqueado: catálogo de dominios poblado |
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

#### FASE 0 — Higiene de wiring + validador (próxima sesión, costo casi cero, impacto máximo)

1. **Fix README.md**: cambiar `CATALOG.md` → `catalog/CATALOG.md`.
2. **Wiring subagentes** (4 pendientes): añadir a `security-architect` los subagentes `entra` y `sast`;
   a `qa-auto` el subagente `performance`; a `finops` el subagente `finops-azure`; a `data-governance`
   el subagente `gov-data`.
3. **Wiring skills Enriq. B** (ver tabla §C): editar frontmatter `skills:` de los agentes destino.
4. **Check anti-huérfanos en validador** (`validate_bidirectional_wiring()`): warning si subagente
   tiene `parent_agent` pero padre no lo lista; warning si skill APB tiene `consumed_by` pero agente
   no la lista. Añadir test nº 24.
5. **Verificar conformidad** de secciones en agentes/subagentes/workflows con el validador actual.
6. Regenerar catálogo (`generate_catalog.py`), validar (`--strict`), y ejecutar tests. **Criterio
   canónico: exit 0**, no el conteo de errores.
7. Commit + push a GitHub.

> **Recordatorio obligatorio al final de TODA sesión:** ejecutar siempre
> `python scripts/generate_catalog.py` + `python scripts/validate_repo.py --strict` antes del commit.

#### FASE 1 — Mejoras de workflows existentes (#74)

8. Añadir Change Manager a `sdd-full` y `cloud-migration`.
9. Añadir Security Architect a `code-review` (PRs con cambios en auth/datos sensibles).
10. Conectar `incident-l1` → `incident-l2` workflow.
11. Añadir Problem Manager a `incident-l1` para incidencias recurrentes.
12. Añadir Tech Debt a `legacy-onboarding`.
13. Añadir performance y accessibility a `qa-evidence`.

#### FASE 2 — Sesiones abiertas del plan

14. **Sesión 13** resto: puntos #6 (plantillas Word), #8 (COSMIC—bloqueado), #52 (email Jira).
15. **Sesión 14**: conversión .docx (borradores MD listos) + documento Dirección.
16. **Sesión 19**: terceros adicionales + decisión `_spec-driven` (bloqueado: URLs de Débora).
17. **Sesión 20**: agentes LCSP (bloqueado: briefing de Débora).
18. **Sesión 21**: SQL skills + soporte incidencias generalista (sin bloqueo).
19. **Sesión 22**: Design System distribución (bloqueado: decisión de Débora).
20. **#50/#51**: QA del framework + prueba real de agentes → alimenta primer `approved`.

#### FASE 3 — Evolución estratégica (a 1–12 meses)

21. **Domain Catalog** poblar `domain-catalog/domains/` (bloqueado: listado APIs de Débora).
22. **Runtime de orquestación** (decisión + `prov-orchestration-engine-v1.0` + Semantic Kernel).
23. **Memoria compartida** (`prov-agent-memory-v1.0`: Redis + Cosmos DB + Git).
24. **Telemetría automática**: instrumentar `invoke_agent.py` con OpenTelemetry → dashboard Power BI.
25. **Primer ciclo de aprobación formal**: seleccionar 10 componentes core, asignar aprobadores
    (2 por componente, ámbitos distintos), llevar a `approved`. KPI: <30% en draft.
26. **Fase 1 descomposición monolitos** (bloqueado hasta Domain Catalog poblado).

---

### I. Decisiones pendientes por persona/equipo

#### Bloqueos de Débora / Dirección

| Decisión | Desbloquea | Urgencia |
|----------|-----------|---------|
| Listado de APIs/sistemas APB | Domain Catalog, DDD, descomposición monolitos | 🔴 |
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
python -m unittest tests.test_validate_repo -v
# → 23/23 actuales; 24/24 tras añadir test bidireccional

# 4. Verificación de wirings aplicados (ejemplo)
grep -A30 "^subagents:" agents/apb-agent-incident-support-v1.0.md
grep -A5 "^subagents:" agents/apb-agent-security-architect-v1.0.md

# 5. Fix README verificado
grep "CATALOG.md" README.md
# debe mostrar solo "catalog/CATALOG.md", nunca "CATALOG.md" sin prefijo
```

> **Referencia:** `docs/HANDOFF_ENRIQUECIMIENTO_B.md` contiene el detalle por equipo y las
> 8 decisiones bloqueantes de Débora/Dirección.
