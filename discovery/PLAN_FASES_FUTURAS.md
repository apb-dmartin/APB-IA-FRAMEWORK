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
| 43 (aplicación retroactiva de política "Generado por IA" + "Validado por humano" a TODO el catálogo) | ✅ **Confirmado: ÚLTIMA FASE del plan, posterior a Sesión 14** (decisión Debora, post-Sesión 11) — ver detalle en punto #43 abajo |

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
| **Design System** | Análisis y construcción del sistema de diseño APB sobre DevExtreme: tokens CSS, componentes compuestos corporativos (cabecera, menú, tarjetas de dominio), guía de estilos integrada. **Repo GitHub propio `apb-design-system`** (decisión Debora 2026-06-24). Skills y agentes de diseño permanecen en `APB-IA-FRAMEWORK`; los artefactos CSS/JS desplegables van al repo nuevo. | #22 | Crear repo + integrar guías de estilos PDF cuando se faciliten |
| **15** | Integraciones Microsoft (Teams, mail, SharePoint) + cierre de gaps de otras plataformas IA: Rovo (Forge App skeleton + guía activación) y M365 Copilot (OpenAPI spec + manifest plugin). Claude web y GitHub Copilot VS Code ya funcionan hoy sin desarrollo adicional. | #30, #35, #47 | — |
| **16** | Informe de análisis de riesgos organizativo (ENS alto, políticas APB, deuda técnica, excepciones) para validación Ciberseguridad/Arquitectura | #16 (alcance completo, no el parcial de Sesión 12) | Debora debe facilitar: esbozo del informe de análisis + procedimiento corporativo de excepciones |
| ~~**17**~~ | ~~Observabilidad: dashboards Power BI/Grafana/Prometheus + logging + telemetría de KPIs del framework~~ | ~~#26, #39, #40~~ | ✅ CERRADA — ver punto #46 para pendiente de telemetría en chat |
| **13** | Cierre de pendientes históricos: guía de uso de agentes, plantillas, mapa Jira, COSMIC, loops, autonomía de agentes, plantilla AGENT.md | #2, #6, #7, #8, #12, #29, #41, #44 | #6 y #8 requieren ejemplos/datos de Debora |
| **18** | DDD: catálogo corporativo de dominios (Fase 0) + descomposición de monolitos (Fase 1) + spec desde histórico Jira | #11/#38 Fase 0, #38 Fase 1, #37 | **Debora debe aportar listado de APIs** para Fase 0 |
| **19** | Terceros pendientes de §8 + evaluación `_spec-driven` de `apb-ai-skills` | #27 (items abiertos), #45 | Items de #27 sin URL requieren que Debora las aporte |
| **20** | Agentes de licitación (LCSP) | #36 | **Pendiente de briefing de Debora** |
| **14** | Documentación Word por audiencias (arquitectos, devs/analistas, dirección) + mecanismo de actualización de documentación funcional | #23, #32 | — |
| **#43** | Aplicación retroactiva "Generado por IA + Validado por humano" a todo el catálogo | #43 | **ÚLTIMA FASE — ejecutar después de que todas las sesiones de construcción hayan cerrado** |

| **21** | SQL + soporte de primera línea de incidencias técnicas | #15, #33 | — |
| **22** | Refactorización de taxonomía de carpetas (Opción C): consolidar dominios inconsistentes en taxonomía canónica escalable a IT-general y negocio | #47bis | — |

### Decisiones tomadas sobre puntos pendientes (2026-06-24)

- **#34 (validación QA en despliegues):** aplica a todo — framework y aplicaciones APB. De momento, durante la fase de construcción del framework, no se aplica al propio repo; se diseña de forma que pueda activarse también sobre él en el futuro. Se incluye en Sesión 21 junto con #15 y #33.
- **#15 y #33:** sesión propia (Sesión 21), no absorbidos en Sesión 13.
- **#47 (gaps plataformas IA) y #47bis (taxonomía carpetas):** añadidos post-Sesión 17 (2026-06-25) — ver detalle abajo. Asignados a Sesiones 15 y 22 respectivamente.

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
