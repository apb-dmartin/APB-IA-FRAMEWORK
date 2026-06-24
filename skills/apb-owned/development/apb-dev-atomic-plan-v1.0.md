---
id: "apb-dev-atomic-plan-v1.0"
name: "Atomic Plan"
description: "Descompone cualquier trabajo de desarrollo en unidades atomicas (maximo 2-4 horas) con entregables verificables, eliminando la ambiguedad del 'esta en progreso'."
version: "1.0.0"
status: "draft"
owner: "Desarrollo APB <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

> Inspirado en: skills.sh/superpowers-method (atomic tasks) (licencia MIT).

# Atomic Plan

## Purpose
Descompone cualquier trabajo de desarrollo en unidades atomicas (maximo 2-4 horas) con entregables verificables, eliminando la ambiguedad del "esta en progreso".

## Trigger
- Despues de completar apb-dev-grill-before-code-v1.0
- Cuando una tarea estimada supera 4 horas
- Cuando el progreso es dificil de reportar

## Input
- Requerimiento clarificado (output del grill)
- Estimacion inicial en horas
- Dependencias tecnicas identificadas

## Output
- Lista de tasks atomicas (<=4h cada una)
- Criterio de done explicito por task
- Orden de ejecucion con dependencias
- Checkpoint de validacion cada 2 tasks

## Procedure

### Step 1: Descomposicion Horizontal
Dividir el trabajo en fases independientes:
- Investigacion/Spike
- Diseno/Contrato
- Implementacion
- Verificacion
- Integracion

### Step 2: Descomposicion Vertical
Dentro de cada fase, crear tasks atomicas:
- Regla: Si no puedes describir el "done" en una oracion, sigue dividiendo
- Regla: Si una task depende de otra no completada, es una sub-task
- Regla: Maximo 4 horas de trabajo concentrado

### Step 3: Definicion de Done
Cada task debe tener:
- [ ] Entregable tangible (codigo, doc, test, decision)
- [ ] Criterio de verificacion objetivo
- [ ] Estado binario: done / not done (no "casi done")

### Step 4: Checkpoint
Cada 2 tasks completadas:
- Revisar si el plan original sigue valido
- Ajustar tasks pendientes si hay aprendizaje nuevo
- Documentar desviaciones

## Rules
- Una task "en progreso" mas de 4h sin done = planificacion fallida
- No adelantar tasks futuras si la actual no esta done
- El "done" debe ser verificable por alguien mas sin explicacion adicional
- Si una task se completa en <30 min, considerar merge con la siguiente

## Examples

### Example 1: API Endpoint
Input: "Crear endpoint POST /api/v2/orders con validacion"
Plan Atomico:
1. [0.5h] Spike: revisar contrato actual de v1 -> Done: lista de campos a mantener/eliminar
2. [1h] Disenar DTO y validadores (FluentValidation) -> Done: clase + tests unitarios pasan
3. [2h] Implementar handler CQRS -> Done: handler compila, tests pasan
4. [1h] Agregar endpoint a controller + swagger -> Done: swagger muestra endpoint, 200/400 testeado
5. [1h] Integracion: test e2e con base de datos -> Done: test e2e pasa en pipeline

Checkpoint despues de task 2: El DTO cubre todos los casos de v1? Si -> continuar. No -> ajustar 3-5.

### Example 2: Refactor Legacy
Input: "Extraer logica de pricing del monolito"
Plan Atomico:
1. [2h] Identificar todos los call sites de pricing -> Done: lista con archivo:linea
2. [2h] Crear interfaz + implementacion mock -> Done: tests existentes pasan con mock
3. [3h] Migrar logica a nuevo servicio -> Done: nuevo servicio con tests, 100% cover
4. [2h] Wire up: inyectar nuevo servicio, eliminar viejo -> Done: tests de integracion pasan

## Integration
- Precedido por: apb-dev-grill-before-code-v1.0
- Seguido por: apb-dev-verify-before-done-v1.0
- Usa: third-obra-superpowers-method-v1.0 (wrapper con estructura APB)

## Tags
#atomic #planning #task-breakdown #development #sprint
