---
id: "apb-dev-code-review-gate-v1.0"
name: "Code Review"
description: "Usar al completar tareas, implementar features mayores, o antes de mergear para verificar\
  \ que el trabajo cumple requisitos y est\xE1ndares de calidad en sistemas orientados\
  \ a eventos."
version: "1.0.0"
status: "draft"
owner: "Desarrollo APB <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

> Procedencia: Adaptado de obra/superpowers (requesting-code-review + receiving-code-review) (licencia MIT).

# APB Code Review: Revisión de Código Orientado a Eventos

## Visión General

Despacha un revisor subagente para detectar problemas antes de que se propaguen. El revisor recibe contexto cuidadosamente elaborado para evaluación — nunca el historial de tu sesión. Esto mantiene al revisor enfocado en el producto del trabajo, no en tu proceso de pensamiento, y preserva tu propio contexto para trabajo continuo.

**Principio fundamental:** Revisar temprano, revisar a menudo.

## Cuándo Solicitar Revisión

**Obligatorio:**
- Después de cada tarea en desarrollo con subagentes
- Después de completar feature mayor
- Antes de merge a main

**Opcional pero valioso:**
- Cuando estás atascado (perspectiva fresca)
- Antes de refactoring (línea base)
- Después de arreglar bug complejo

## Proceso de Dos Etapas (Two-Stage Review)

### Etapa 1: Revisión de Spec + Calidad de Código (Task-Scoped)

Después de cada tarea completada:

1. Obtener git SHAs:
```bash
BASE_SHA=$(git rev-parse HEAD~1)  # o el SHA de inicio de la tarea
HEAD_SHA=$(git rev-parse HEAD)
```

2. Despachar revisor de tarea (subagente):

```
Subagente (general-purpose):
  description: "Revisar Tarea N (spec + calidad)"
  prompt: |
    Estás revisando la implementación de una tarea: primero si coincide
    con sus requisitos, luego si está bien construida. Esta es una puerta
    de alcance de tarea, no una revisión de merge — una revisión amplia
    de toda la rama ocurre separadamente después de que todas las tareas
    estén completas.

    ## Qué Se Solicitó
    Lee el brief de la tarea: [BRIEF_FILE]

    Restricciones globales del spec/diseño que atan esta tarea:
    [GLOBAL_CONSTRAINTS]

    ## Qué El Implementador Dice Que Construyó
    Lee el reporte del implementador: [REPORT_FILE]

    ## Diff Bajo Revisión
    Base: [BASE_SHA]
    Head: [HEAD_SHA]
    Archivo diff: [DIFF_FILE]

    ## Verificaciones Específicas de Event-Driven

    1. **Schemas CloudEvents:**
       - ¿El evento sigue el spec CloudEvents 1.0?
       - ¿specversion, type, source, id, time están presentes?
       - ¿El schema JSON está validado?

    2. **Contratos de Eventos:**
       - ¿El productor y consumidor acuerdan el schema?
       - ¿Hay versionado de eventos (backward compatibility)?
       - ¿Los campos obligatorios están documentados?

    3. **Idempotencia:**
       - ¿El consumidor maneja duplicados correctamente?
       - ¿Hay mecanismo de deduplicación (idempotency key)?

    4. **Manejo de Errores:**
       - ¿Qué pasa si el procesamiento falla?
       - ¿Hay retry con backoff exponencial?
       - ¿Dead letter queue configurada correctamente?

    5. **Ordenamiento:**
       - ¿Si se requiere orden, se usan session keys?
       - ¿El procesamiento es thread-safe?

    6. **Sagas (si aplica):**
       - ¿Las acciones compensatorias están definidas?
       - ¿Son idempotentes las compensaciones?
       - ¿Hay timeout configurado por paso?

    7. **Tests:**
       - ¿Tests de integración para publish/consume?
       - ¿Tests de idempotencia?
       - ¿Tests de compensación (sagas)?
       - ¿Todos los tests pasan?

    ## No Confíes en el Reporte
    Trata el reporte del implementador como afirmaciones no verificadas.
    Verifica las afirmaciones contra el diff.

    ## Formato de Salida
    ## Revisión de Tarea

    **Estado:** Aprobado | Problemas Encontrados | Bloqueado

    **Problemas Críticos (bloquean):**
    - [Descripción específica] — [por qué importa]

    **Problemas Importantes:**
    - [Descripción específica] — [por qué importa]

    **Problemas Menores:**
    - [Descripción específica]

    **Evaluación:** Lista para continuar | Necesita correcciones
```

### Etapa 2: Revisión Amplia de Rama (Whole-Branch)

Después de que todas las tareas estén completas:

```
Subagente (general-purpose):
  description: "Revisión amplia de rama"
  prompt: |
    Revisa todo el trabajo de esta rama contra el spec original y
    estándares de calidad del codebase.

    ## Verificaciones de Arquitectura de Eventos
    - ¿La topología de Service Bus es correcta?
    - ¿Hay contratos de eventos documentados (AsyncAPI)?
    - ¿Los schemas están versionados?
    - ¿La consistencia eventual está manejada correctamente?
    - ¿Hay observabilidad (logs, métricas, tracing)?
```

## Recibir Revisión de Código

### Patrón de Respuesta

```
CUANDO recibes feedback de revisión:

1. LEER: Feedback completo sin reaccionar
2. ENTENDER: Reformular requisito en tus palabras (o preguntar)
3. VERIFICAR: Chequear contra realidad del codebase
4. EVALUAR: ¿Técnicamente sólido para ESTE codebase?
5. RESPONDER: Reconocimiento técnico o pushback razonado
6. IMPLEMENTAR: Un ítem a la vez, testear cada uno
```

### Respuestas Prohibidas

**NUNCA:**
- "¡Tienes toda la razón!" (violación de instrucciones)
- "¡Buen punto!" / "¡Excelente feedback!" (performático)
- "Voy a implementar eso ahora" (antes de verificación)

**EN LUGAR DE:**
- Reformular el requisito técnico
- Hacer preguntas clarificadoras
- Hacer pushback con razonamiento técnico si está mal
- Simplemente empezar a trabajar (acciones > palabras)

## Manejo de Feedback Específico de Event-Driven

| Tipo de Feedback | Respuesta |
|------------------|-----------|
| "Falta idempotencia" | Verificar mecanismo de deduplicación, implementar si falta |
| "Schema no valida CloudEvents" | Revisar spec 1.0, añadir campos obligatorios |
| "No hay compensación definida" | Definir acciones compensatorias para saga |
| "DLQ no configurada" | Configurar dead letter con retry policy |
| "Falta test de ordenamiento" | Añadir test con session keys |
| "Evento no tiene versión" | Añadir versionado al type (v1, v2) |
