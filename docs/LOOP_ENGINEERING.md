# Loop Engineering en el APB AI Framework

> **Audiencia:** Arquitectura APB, equipos que usan agentes en proyectos  
> **Última actualización:** 2026-06-30

---

## ¿Qué es un bucle de iteración?

Un bucle de iteración es un ciclo estructurado en el que el output de un agente se convierte en el input de otro (o del mismo agente en un pase siguiente), con un gate de validación humana entre iteraciones. El bucle continúa hasta que se cumple un criterio de calidad o convergencia.

```
[Input inicial]
      ↓
[Agente A — primera pasada]
      ↓
[Output v1]
      ↓
[Gate humano: ¿cumple criterios?]
   Sí → Siguiente fase
   No → [Agente B o Agente A — iteración 2 con feedback]
      ↓
[Output v2]
      ↓
[Gate humano]
   ...
```

Loop engineering es la disciplina de diseñar, implementar y optimizar estos bucles de forma deliberada: definiendo los criterios de entrada y salida, los agentes participantes, los gates, los mecanismos de feedback y las condiciones de escape. Es la diferencia entre "el agente itera hasta que queda bien" y "el bucle converge en ≤N pasos con criterios medibles".

---

## Tipos de bucle

### 1. Bucle de refinamiento (mismo agente)

El mismo agente recibe su output anterior más el feedback humano y genera una versión mejorada.

**Cuándo usarlo:** Documentos técnicos, especificaciones, ADRs — cuando el resultado es bueno pero necesita ajustes.

**Ejemplo:**
```
apb-agent-spec-engineer → SDD v1
  → Revisión humana → "faltan los criterios de aceptación del módulo X"
apb-agent-spec-engineer → SDD v2 (con los criterios añadidos)
  → Revisión humana → Aprobado
```

**Límite recomendado:** 3 iteraciones. Si en la tercera no converge, revisar el input inicial.

---

### 2. Bucle de revisión cruzada (agentes distintos)

El output de un agente generador es revisado por un agente revisor especializado.

**Cuándo usarlo:** Código (generador → revisor), arquitectura (diseñador → validador de seguridad), documentación (generador → QA).

**Ejemplo:**
```
apb-agent-implementer    → código v1
apb-agent-code-reviewer  → lista de defectos
apb-agent-implementer    → código v2 (defectos corregidos)
apb-agent-code-reviewer  → Aprobado / sin defectos críticos
```

**Criterio de salida:** 0 defectos Críticos y 0 defectos Altos.

---

### 3. Bucle de orquestación (workflow multi-agente)

Un workflow orquesta múltiples agentes en secuencia, con gates humanos entre fases. El bucle se activa cuando una fase no supera su gate.

**Cuándo usarlo:** Flujos de entrega completos (discovery → arquitectura → spec → implementación → QA).

**Referencia:** `workflows/apb-wf-sdd-full-v1.0.md`, `workflows/apb-wf-incident-l1-v1.0.md`

---

### 4. Bucle de validación de framework (QA interno)

```
apb-agent-meta-builder → componente nuevo
apb-qa-framework       → validación esquema + coherencia
  Si errores → meta-builder corrige
  Si OK → PR al repositorio → revisión Arquitectura APB
```

---

## Gates humanos

Todo bucle APB debe tener al menos un gate humano.

| Tipo de gate | Cuándo | Quién aprueba |
|-------------|--------|---------------|
| **Gate de calidad** | Entre iteraciones | Técnico responsable del artefacto |
| **Gate de seguridad** | Antes de merge a main | Security APB (si hay cambios de seguridad) |
| **Gate de producción** | Antes de desplegar | Release Manager + responsable del servicio |
| **Gate de escalado** | En incidencias L1 | Técnico L1 antes de escalar a L2/L3 |

---

## Criterios de convergencia

Un bucle converge cuando se cumple **uno** de estos criterios:

1. **Criterio de calidad:** el output pasa todos los checks del agente revisor sin defectos Críticos/Altos
2. **Criterio de aprobación:** el técnico responsable aprueba explícitamente el output
3. **Criterio de límite:** se alcanza el máximo de iteraciones → escalar a decisión humana

---

## Principios de diseño

### P1 — Todo bucle tiene un criterio de salida medible

Antes de diseñar un bucle, definir:
- **Criterio de éxito:** qué condición exacta termina el bucle (cobertura ≥70%, 0 defectos críticos, aprobación explícita)
- **Criterio de escape:** qué pasa si no converge en N iteraciones (escalado humano, decisión de Arquitectura)
- **Máximo de iteraciones:** ≤3 para bucles de refinamiento, ≤5 para bucles de orquestación

### P2 — El feedback es estructurado, no libre

```yaml
feedback:
  iteration: 2
  defectos_criticos:
    - id: D1
      descripcion: "Falta validación de entrada en el endpoint POST /escales"
      ubicacion: "src/api/escales.controller.ts:45"
  defectos_altos:
    - id: D2
      descripcion: "No se gestiona el caso de escale duplicado"
  aprobado: false
```

### P3 — Los bucles son trazables

Cada iteración queda registrada: número de iteración, timestamp, hash del output (para detectar si el agente regeneró sin cambios reales), feedback aplicado, resultado del gate.

### P4 — Los agentes especializados revisan, no generalizan

En un bucle de revisión cruzada, el agente revisor tiene scope cerrado. No reescribe el artefacto — emite una lista de defectos. El agente generador aplica los defectos en la siguiente iteración.

---

## Patrones de implementación

### Patrón A: Refinamiento simple

```
[Agente generador] → output → [Gate humano] → feedback → [Agente generador] → ...
```

**Uso:** Documentos, especificaciones, ADRs | **Máx. iteraciones:** 3 | **Criterio de salida:** Aprobación humana explícita

---

### Patrón B: Revisión cruzada

```
[Agente generador] → output →
[Agente revisor]   → defectos →
[Gate humano]      → ¿defectos críticos? →
  Sí → [Agente generador] con defectos como input
  No → Aprobado
```

**Uso:** Código, pipelines CI/CD, configuraciones | **Máx. iteraciones:** 3 (críticos) + 2 (altos) | **Criterio:** 0 Críticos, 0 Altos

---

### Patrón C: Ping-pong especializado

```
[Agente A: genera propuesta] →
[Agente B: contra-propuesta o crítica] →
[Agente A: versión refinada con crítica incorporada] →
[Gate humano: decide entre A y B o aprueba A refinado]
```

**Uso:** Decisiones de arquitectura, análisis de riesgo, diseño DDD | **Máx. iteraciones:** 2 rondas (4 outputs)

---

### Patrón D: Validación continua (CI/CD)

```
[Commit] →
[Pipeline CI] →
[apb-qa-pipeline-v1.0] →
  🔴 No apto → Notificación + bloqueo de merge
  🟡 Apto con advertencias → Revisión humana obligatoria
  🟢 Apto → Gate aprobación humana → Deploy
```

**Crítico:** el gate de aprobación humana antes de producción es NO negociable.

---

### Patrón E: Escalado progresivo (incidencias)

```
[Reporte incidencia] →
[apb-agent-incident-support: triaje + diagnóstico] →
[Gate L1: ¿resoluble?] →
  Sí → Runbook → Verificación → Cierre
  No → Escalado L2 → [Gate L2: ¿resoluble?] →
    No → Escalado L3 / Major Incident
```

**Referencia:** `workflows/apb-wf-incident-l1-v1.0.md`

---

## Aplicabilidad en el framework APB

| Área | Patrón | Agentes involucrados |
|------|--------|---------------------|
| Generación de SDD | A (refinamiento) | spec-engineer |
| Revisión de código | B (cruzada) | implementer + code-reviewer |
| Diseño de arquitectura | C (ping-pong) | technical-architect + security-architect |
| Despliegue a producción | D (CI/CD) | qa-auto + release-manager |
| Incidencias técnicas | E (escalado) | incident-support + sre |
| Componentes del framework | B (cruzada) | meta-builder + qa-framework |

---

## Métricas de calidad

| Métrica | Objetivo | Alerta |
|---------|---------|--------|
| Iteraciones hasta convergencia | ≤2 | >3 → revisar input o agente |
| Tasa de defectos críticos en iteración 1 | <20% de reviews | >40% → ajustar prompt o skill |
| Tiempo por iteración (documentos) | <5 min | >15 min → simplificar scope |
| Tasa de escape (no converge) | <5% | >10% → revisar criterio de salida |

---

## Anti-patrones a evitar

| Anti-patrón | Problema | Alternativa |
|-------------|---------|------------|
| Bucle sin gate humano | El error se amplifica en cada iteración | Siempre incluir gate tras cada pasada |
| Más de 3 iteraciones sin convergencia | Input ambiguo o agente inadecuado | Revisar el input o cambiar de agente |
| Aprobar sin leer el output | El gate pierde su función | El técnico debe revisar el diff entre versiones |
| Iterar sobre artefactos en producción | Riesgo de inconsistencia | Iterar siempre en pre-producción |

---

*Documento generado por el APB AI Framework — Sesiones 13 y 30. Requiere revisión humana antes de distribución.*
