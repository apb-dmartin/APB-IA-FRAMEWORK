# Bucles de Iteración en el APB AI Framework

> **Audiencia:** Arquitectura APB, equipos que usan agentes en proyectos  
> **Última actualización:** 2026-06-26

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

---

## Tipos de bucle en el framework

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

El agente `apb-agent-meta-builder-v1.0` genera componentes del framework que son validados por `apb-qa-framework-v1.0` antes de incorporarse al catálogo.

```
apb-agent-meta-builder → componente nuevo
apb-qa-framework       → validación esquema + coherencia
  Si errores → meta-builder corrige
  Si OK → PR al repositorio → revisión Arquitectura APB
```

---

## Gates humanos en bucles

Todo bucle APB debe tener al menos un gate humano. Los gates son:

| Tipo de gate | Cuándo | Quién aprueba |
|-------------|--------|---------------|
| **Gate de calidad** | Entre iteraciones | Técnico responsable del artefacto |
| **Gate de seguridad** | Antes de merger a main | Security APB (si hay cambios de seguridad) |
| **Gate de producción** | Antes de desplegar | Release Manager + responsable del servicio |
| **Gate de escalado** | En incidencias L1 | Técnico L1 antes de escalar a L2/L3 |

---

## Criterios de convergencia

Un bucle converge cuando se cumple **uno** de estos criterios:

1. **Criterio de calidad:** el output pasa todos los checks del agente revisor sin defectos Críticos/Altos
2. **Criterio de aprobación:** el técnico responsable aprueba explícitamente el output
3. **Criterio de límite:** se alcanza el número máximo de iteraciones → escalar a decisión humana

---

## Anti-patrones a evitar

| Anti-patrón | Problema | Alternativa |
|-------------|---------|------------|
| Bucle sin gate humano | El error se amplifica en cada iteración | Siempre incluir gate tras cada pasada |
| Más de 3 iteraciones sin convergencia | El input es ambiguo o el agente inadecuado | Revisar el input o cambiar de agente |
| Aprobar sin leer el output | El gate pierde su función | El técnico debe revisar el diff entre versiones |
| Iterar sobre artefactos en producción | Riesgo de inconsistencia | Iterar siempre en entorno de pre-producción |

---

*Documento generado por el APB AI Framework — Sesión 13. Requiere revisión humana antes de distribución.*
