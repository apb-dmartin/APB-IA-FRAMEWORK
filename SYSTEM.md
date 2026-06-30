# SYSTEM.md — APB AI Framework

> **Versión:** 1.0.0-draft
> **Estado:** draft
> **Propietario:** Arquitectura APB
> **Fecha revisión:** 2026-06-21

---

## 1. Objetivo General

Definir una plataforma corporativa de conocimiento, capacidades y automatización asistida por Inteligencia Artificial para la **Autoridad Portuaria de Barcelona (APB)**, con las siguientes características:

- **Reutilizable** por distintos LLM y herramientas mediante adaptadores.
- **Compatible** con Spec Driven Development (SDD) y con uso independiente de agentes sobre repositorios legacy.
- **Evolucionable**, con jerarquía de componentes que permite crecimiento progresivo.
- **Gobernada**, con estados, aprobadores humanos y trazabilidad extremo a extremo.
- **Segura**, con gestión centralizada de secretos y validación de cumplimiento.
- **Trazable**, con cadena: Jira → Spec → ADR/API/Event → Código → Tests → Evidencias → Release.

---

## 2. Reglas Globales

### 2.1 Responsabilidad Humana

1. La IA propone, estructura y automatiza; la **responsabilidad final es humana**.
2. **Ningún agente puede aprobar sus propios resultados**.
3. Toda salida relevante debe tener trazabilidad completa.

### 2.2 Estándares Corporativos

4. Los **estándares corporativos APB prevalecen** sobre recomendaciones del modelo de IA.
5. No se permite **vibe coding**: toda generación de código debe partir de spec, plan técnico, issue Jira o hallazgo documentado.
6. Los agentes utilizan siempre la **última versión aprobada** de los estándares disponibles.

### 2.3 Seguridad

7. Los **secretos no se introducen en prompts ni archivos**. Se usan referencias a Azure Key Vault.
8. Modelo **Zero Trust**: privilegios mínimos, human approval obligatorio para acciones de riesgo.
9. Clasificación de riesgo de componentes: **Low, Medium, High, Critical**.

### 2.4 Gestión de Estado

10. El **estado de componentes y artefactos es metadato**. No se mueve un archivo entre carpetas por cambiar de estado.
11. Todo componente nace en estado `draft` y requiere revisión humana para avanzar.

### 2.5 Componentes de Terceros

12. Todo componente externo se gobierna mediante **descriptor**, pin de versión/commit cuando aplique, análisis de licencia y wrapper APB.
13. No se copia ni modifica código de terceros salvo autorización legal expresa.

### 2.6 Fuentes de Verdad

14. La **fuente de verdad técnica es Git**. Confluence es una proyección, no la fuente maestra.
15. La **fuente de verdad funcional es Jira**.
16. Los proyectos guardan sus specs junto al código (`system-spec.md`, `domain-spec.md`).

### 2.7 Workflows

17. Los workflows declaran **permisos** y **nivel de autonomía** en su definición.
18. Todo workflow debe tener puntos de validación humana documentados.

---

## 3. Jerarquía de Componentes

```
┌─────────────────────────────────────────────────────────────┐
│ CAPABILITY                                                    │
│ Capacidad de negocio (ej: "Generar especificaciones")        │
├─────────────────────────────────────────────────────────────┤
│ PROVIDER                                                      │
│ Fuente de conocimiento o acción (ej: GitHub MCP)            │
├─────────────────────────────────────────────────────────────┤
│ WRAPPER                                                       │
│ Adaptación APB sobre componente de terceros                 │
├─────────────────────────────────────────────────────────────┤
│ SKILL                                                         │
│ Unidad reutilizable con inputs/outputs definidos            │
├─────────────────────────────────────────────────────────────┤
│ SUBAGENT                                                      │
│ Especialización de un agente para un contexto concreto      │
├─────────────────────────────────────────────────────────────┤
│ AGENT                                                         │
│ Rol con responsabilidades, skills disponibles y límites     │
├─────────────────────────────────────────────────────────────┤
│ WORKFLOW                                                      │
│ Orquestación de agentes para un objetivo de negocio         │
└─────────────────────────────────────────────────────────────┘
```

### 3.1 Nota sobre el arranque

Para la fase inicial del framework (pilotos controlados):

- **Capability, Provider y Wrapper son opcionales.** Se documentan pero no son obligatorios para operar.
- **Skill, Agent y Workflow son obligatorios.** Constituyen el núcleo operativo.
- A medida que el framework madure, se irá completando la jerarquía completa.

---

## 4. Runtime y Adaptadores

### 4.1 Runtime Inicial: GitHub Copilot

- Modo por defecto: **ReadOnly** para providers de acción.
- Integración nativa con VS Code y Visual Studio.
- Consumo de skills mediante `copilot-instructions.md` o referencia a este repositorio.

### 4.2 Adaptadores Disponibles

| Adaptador | Estado | Descripción |
|-----------|--------|-------------|
| `adapters/copilot/` | draft | Instrucciones y contexto para GitHub Copilot. |
| `adapters/claude/` | draft | Prompts y contexto para Claude (Anthropic). |
| `adapters/m365/` | draft | Integración con Microsoft 365 Copilot. |
| `adapters/rovo/` | draft | Integración con Atlassian Rovo. |

### 4.3 Principio de Agnosticismo

- Un mismo **Agente** debe poder ejecutarse en **ambos runtimes** mediante su adaptador correspondiente.
- Las **Skills** son runtime-agnósticas: definen inputs/outputs en lenguaje natural.
- Los **Adaptadores** traducen el contexto y los prompts al formato específico de cada runtime.

---

## 5. Niveles de Autonomía

| Nivel | Nombre | Descripción | Human Review |
|-------|--------|-------------|--------------|
| 0 | Asistencia | La IA únicamente propone recomendaciones. | Posterior o implícita |
| 1 | Generación asistida | La IA genera artefactos que requieren aprobación humana obligatoria. | **Obligatoria previa** |
| 2 | Ejecución supervisada | La IA puede ejecutar tareas de bajo riesgo con validación posterior. | Posterior obligatoria |
| 3 | Automatización controlada | La IA puede ejecutar actividades previamente autorizadas dentro de límites definidos. | Auditoría periódica |
| 4 | Autorización explícita | La IA puede actualizar Jira/GitHub con aprobación explícita previa. | Explícita por acción |

### 5.1 Reglas de Aplicación

- **Nivel por defecto:** Nivel 1.
- **Análisis, arquitectura, seguridad, despliegue y gobierno:** Mínimo Nivel 1.
- **Documentación y specs:** Puede operar en Nivel 2 con revisión posterior.
- **Tests automatizados de regresión:** Puede operar en Nivel 3 si están previamente autorizados.
- **Ninguna actividad inicia en Nivel 4** sin aprobación explícita de Arquitectura y Ciberseguridad.

---

## 6. Human Review Obligatorio

Los siguientes artefactos requieren validación humana antes de considerarse aprobados:

| Fase | Artefacto | Responsable de Validación |
|------|-----------|---------------------------|
| Descubrimiento | Capacidades de negocio, procesos y alcance | Analista Funcional / Product Owner |
| Análisis | Requisitos, especificaciones, casos de uso, criterios de aceptación | Analista Funcional / Product Owner |
| Diseño DDD | Dominios, bounded contexts, eventos de negocio | Arquitecto / Tech Lead |
| Arquitectura | Arquitectura de solución, APIs, integraciones | Arquitecto |
| Seguridad | Requisitos de seguridad, modelo de amenazas, análisis de riesgos | Arquitectura / Ciberseguridad |
| Backlog | Épicas, historias y planificación propuesta | Analista Funcional / Product Owner |
| Desarrollo | Código generado automáticamente | Desarrollador / Tech Lead |
| Testing | Casos de prueba y resultados de validación | QA / Analista Funcional |
| Plataforma | Infraestructura, pipelines y automatizaciones | Arquitectura / Operaciones |
| Release | Checklist de despliegue y readiness review | Release Manager / Arquitectura |
| Operación | SLO, observabilidad y runbooks | SRE / Operaciones |
| Gobierno | Excepciones, desviaciones e incumplimientos | Arquitectura / Ciberseguridad |

---

## 7. Trazabilidad Extremo a Extremo

La cadena de trazabilidad obligatoria es:

```
Necesidad (Jira)
 ↓
Especificación (system-spec.md, domain-spec.md)
 ↓
ADR / API / Evento (adr/*.md, openapi/*.yaml, asyncapi/*.yaml)
 ↓
Código (src/)
 ↓
Tests (tests/)
 ↓
Evidencias (evidence/)
 ↓
Release (GitHub Release / Jenkins / Azure DevOps)
```

### 7.1 Metadatos de Trazabilidad

Cada artefacto generado por IA debe incluir:

- **Agente** utilizado.
- **Skill** ejecutada.
- **Prompt** utilizado (referencia al catálogo).
- **Usuario** solicitante.
- **Resultado** generado.
- **Validaciones** realizadas.
- **Fecha y versión**.

### 7.2 Identificación Explícita de Generación por IA y Validación Humana

**Política de Debora (Sesión 11, post-Sesión 9), aplicable a todo artefacto que un agente o
skill del framework produzca** — informes, planes, componentes nuevos, documentación,
análisis: el artefacto debe declarar de forma **visible y explícita**, no solo como campo
de metadatos interno:

1. Que fue generado por IA (agente/skill concreto, no una mención genérica de "IA").
2. Qué humano lo validó (nombre o rol), una vez completada la revisión.

Esto va más allá de §7.1: §7.1 exige el registro de metadatos de trazabilidad en el sistema;
esta sección exige que la identificación sea legible directamente en el propio artefacto
entregado, no solo recuperable consultando el catálogo o el sistema de trazabilidad aparte.

Ningún artefacto se considera `approved` (`GOVERNANCE.md` §1) sin que ambos elementos —
identificación de origen IA e identidad del validador humano — estén presentes en el propio
documento o informe entregado.

---

## 8. Gestión de Excepciones

### 8.1 Tipos de Excepción

- Arquitectura
- Seguridad
- Calidad (QA)
- Integración
- Cloud
- Observabilidad
- Automatización
- Desarrollo

### 8.2 Proceso de Excepción

1. **Solicitud:** Descripción de la desviación, justificación, evaluación de riesgos, medidas compensatorias.
2. **Responsable solicitante:** Identificado.
3. **Responsable aprobador:** Según tipo de excepción (Arquitectura, QA, Ciberseguridad).
4. **Fecha de aprobación y caducidad:** Definidas.
5. **Revisión periódica:** Las excepciones aprobadas se revisan periódicamente.

> **Los agentes no pueden aprobar excepciones.** Solo responsables humanos.

---

## 9. Filosofía del Framework

El objetivo no es construir agentes.

El objetivo es construir una **plataforma corporativa** de:

- **Conocimiento** (estándares, políticas, contexto APB).
- **Capacidades** (skills reutilizables, runtime-agnósticas).
- **Automatización** (workflows orquestados, agentes independientes).
- **Gobierno** (estados, trazabilidad, aprobaciones, excepciones).

Los agentes son **una capa más del sistema**, no el sistema en sí.

---

## 10. Referencias

- `GOVERNANCE.md` — Reglas de gobierno, estados y aprobadores.
- `CONTRIBUTING.md` — Guía de contribución y checklist de PR.
- `catalog/CATALOG.md` — Catálogo centralizado de componentes.
- `context/apb/` — Contexto corporativo (estándares, plantillas, políticas).
- `context/apb/SCHEMA.md` — Esquema de metadatos YAML obligatorio para todo componente.
