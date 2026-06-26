# Loop Engineering en el APB AI Framework

> **Audiencia:** Arquitectura APB — para diseño avanzado de flujos multi-agente  
> **Última actualización:** 2026-06-26  
> **Prerrequisito:** Leer `ITERATION_LOOPS.md` antes de este documento

---

## ¿Qué es loop engineering?

Loop engineering es la disciplina de diseñar, implementar y optimizar bucles de agentes IA de forma deliberada: definiendo los criterios de entrada y salida, los agentes participantes, los gates, los mecanismos de feedback y las condiciones de escape. Es la diferencia entre "el agente itera hasta que queda bien" y "el bucle converge en ≤N pasos con criterios medibles".

---

## Principios de diseño de bucles APB

### P1 — Todo bucle tiene un criterio de salida medible

Antes de diseñar un bucle, definir:
- **Criterio de éxito:** qué condición exacta termina el bucle (cobertura ≥70%, 0 defectos críticos, aprobación explícita)
- **Criterio de escape:** qué pasa si no converge en N iteraciones (escalado humano, decisión de Arquitectura)
- **Máximo de iteraciones:** recomendado ≤3 para bucles de refinamiento, ≤5 para bucles de orquestación

### P2 — El feedback es estructurado, no libre

El feedback que entra en cada iteración debe tener formato fijo para que el agente pueda procesarlo de forma consistente:

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

Cada iteración queda registrada:
- Número de iteración y timestamp
- Hash del output (para detectar si el agente regeneró sin cambios reales)
- Feedback aplicado
- Resultado del gate

### P4 — Los agentes especializados revisan, no generalizan

En un bucle de revisión cruzada, el agente revisor tiene un scope cerrado. No reescribe el artefacto — emite una lista de defectos. El agente generador aplica los defectos en la siguiente iteración.

---

## Patrones de bucle

### Patrón A: Refinamiento simple

```
[Agente generador] → output → [Gate humano] → feedback → [Agente generador] → ...
```

**Uso:** Documentos, especificaciones, ADRs  
**Máx. iteraciones:** 3  
**Criterio de salida:** Aprobación humana explícita

---

### Patrón B: Revisión cruzada

```
[Agente generador] → output →
[Agente revisor]   → defectos →
[Gate humano]      → ¿defectos críticos? →
  Sí → [Agente generador] con defectos como input
  No → Aprobado
```

**Uso:** Código, pipelines CI/CD, configuraciones  
**Máx. iteraciones:** 3 (defectos críticos) + 2 (defectos altos)  
**Criterio de salida:** 0 defectos Críticos, 0 defectos Altos

---

### Patrón C: Ping-pong especializado

```
[Agente A: genera propuesta] →
[Agente B: contra-propuesta o crítica] →
[Agente A: versión refinada con crítica incorporada] →
[Gate humano: decide entre A y B o aprueba A refinado]
```

**Uso:** Decisiones de arquitectura, análisis de riesgo, diseño de dominio DDD  
**Máx. iteraciones:** 2 rondas (4 outputs)  
**Criterio de salida:** Gate humano aprueba una de las alternativas

---

### Patrón D: Bucle de validación continua (CI/CD)

```
[Commit] →
[Pipeline CI] →
[apb-qa-pipeline-v1.0: validación] →
  🔴 No apto → Notificación + bloqueo de merge
  🟡 Apto con advertencias → Revisión humana obligatoria
  🟢 Apto → Gate de aprobación humana → Deploy
```

**Uso:** Despliegues a producción  
**Crítico:** El gate de aprobación humana antes de producción es NO negociable

---

### Patrón E: Bucle de incidencia (escalado progresivo)

```
[Reporte incidencia] →
[apb-agent-incident-support: triaje + diagnóstico] →
[Gate L1: ¿resoluble?] →
  Sí → Runbook → Verificación → Cierre
  No → Escalado L2 → [Gate L2: ¿resoluble?] →
    No → Escalado L3 / Major Incident
```

**Uso:** Incidencias técnicas APB  
**Referencia:** `workflows/apb-wf-incident-l1-v1.0.md`

---

## Métricas de calidad de un bucle

| Métrica | Objetivo | Alerta |
|---------|---------|--------|
| Iteraciones hasta convergencia | ≤2 | >3 → revisar input o agente |
| Tasa de defectos críticos en iteración 1 | <20% de reviews | >40% → ajustar prompt o skill |
| Tiempo por iteración (documentos) | <5 min | >15 min → simplificar scope |
| Tasa de escape (no converge) | <5% | >10% → revisar criterio de salida |

---

## Aplicabilidad en el framework APB

| Área | Patrón recomendado | Agentes involucrados |
|------|--------------------|---------------------|
| Generación de SDD | A (refinamiento) | spec-engineer |
| Revisión de código | B (cruzada) | implementer + code-reviewer |
| Diseño de arquitectura | C (ping-pong) | technical-architect + security-architect |
| Despliegue a producción | D (CI/CD) | qa-auto + release-manager |
| Incidencias técnicas | E (escalado) | incident-support + sre |
| Componentes del framework | B (cruzada) | meta-builder + qa-framework |

---

*Documento generado por el APB AI Framework — Sesión 13. Requiere revisión humana antes de distribución.*
