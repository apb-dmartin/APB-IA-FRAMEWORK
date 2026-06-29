---
id: "apb-pm-implementation-planning-v1.0"
name: "Planning"
description: "Usar cuando se tiene un spec o requisitos para una tarea multi-paso, antes de tocar\
  \ c\xF3digo. Crea planes de implementaci\xF3n para sistemas orientados a eventos."
version: "1.0.0"
status: "draft"
owner: "PMO APB <arquitectura@portdebarcelona.cat>"
domain: "pm"
autonomy_level: 1
consumed_by:
  - "apb-agent-spec-engineer-v1.0"
  - "apb-agent-pm-v1.0"
created_date: "2026-06-20"
review_date: "2026-06-24"
---

> Procedencia: Adaptado de obra/superpowers (writing-plans) + bmad-method (planning workflows) (licencia MIT). Contenido adaptado y
> generalizado para el APB AI Framework.

# APB Planning: Planes de Implementación Orientados a Eventos

## Visión General

Escribe planes de implementación comprehensivos asumiendo que el ingeniero tiene cero contexto del codebase y gusto cuestionable. Documenta todo lo que necesita saber: qué archivos tocar para cada tarea, código, testing, docs que podría necesitar revisar, cómo probarlo. Dáselo todo como tareas pequeñas. DRY. YAGNI. TDD. Commits frecuentes.

Asume que es un desarrollador competente, pero que casi no sabe de nuestro stack tecnológico o dominio del problema. Asume que no sabe diseñar bien tests.

**Anunciar al inicio:** "Estoy usando el skill apb-planning para crear el plan de implementación."

**Guardar planes en:** `docs/apb/plans/YYYY-MM-DD-<nombre-feature>.md`

## Verificación de Alcance

Si el spec cubre múltiples subsistemas independientes, debería haberse dividido en sub-proyectos durante el brainstorming. Si no fue así, sugerir dividir esto en planes separados — uno por subsistema. Cada plan debería producir software funcional y testeable por sí solo.

## Estructura de Archivos

Antes de definir tareas, mapear qué archivos se crearán o modificarán y qué responsabilidad tiene cada uno. Aquí es donde se toman las decisiones de descomposición.

- Diseñar unidades con límites claros e interfaces bien definidas. Cada archivo debe tener una responsabilidad clara.
- Razonas mejor sobre código que puedes mantener en contexto de una vez, y tus ediciones son más confiables cuando los archivos están enfocados. Prefiere archivos pequeños y enfocados sobre grandes que hacen demasiado.
- Archivos que cambian juntos deben vivir juntos. Dividir por responsabilidad, no por capa técnica.
- En codebases existentes, seguir patrones establecidos. Si el codebase usa archivos grandes, no reestructurar unilateralmente — pero si un archivo que modificas ha crecido demasiado, incluir una división en el plan es razonable.

## Consideraciones de Event-Driven en la Planificación

### Mapeo de Responsabilidades por Tarea

Cada tarea DEBE especificar:

| Elemento | Descripción |
|----------|-------------|
| **Evento(s) involucrados** | Nombre del evento CloudEvents, versión del schema |
| **Topic/Subscription** | Dónde se publica/suscribe en Azure Service Bus |
| **Productor** | Servicio/módulo que emite el evento |
| **Consumidor(es)** | Servicio(s) que procesan el evento |
| **Schema** | Definición JSON del payload, validación |
| **Idempotencia** | Estrategia de detección de duplicados |
| **Ordenamiento** | ¿Requiere session keys? ¿Orden estricto? |
| **Compensación** | Si es saga, definir acción compensatoria |
| **DLQ** | Configuración de dead letter queue |

### Orden de Implementación Recomendado

```
1. Definir schemas CloudEvents (JSON)
2. Configurar topología de Service Bus (topics, subscriptions)
3. Implementar productor de eventos (outbox pattern)
4. Implementar consumidor de eventos (handler + idempotencia)
5. Implementar lógica de negocio
6. Configurar dead letter handling
7. Tests de integración (event publishing/consumption)
8. Tests de saga (compensación)
9. Documentación AsyncAPI
```

## Tamaño Correcto de Tareas

Una tarea es la unidad más pequeña que lleva su propio ciclo de test y vale una revisión de calidad. Al trazar límites de tareas: incluir setup, configuración, scaffolding y pasos de documentación en la tarea cuyo entregable los necesita; dividir solo cuando hay una razón clara para hacerlo.

**Reglas de oro:**
- Una tarea = un comportamiento testeable
- Si una tarea toca más de 3 servicios, dividirla
- Si una tarea requiere cambios en schemas + código + infraestructura, considerar dividir

## Plantilla de Tarea para Event-Driven

```markdown
### Task N: [Nombre de la tarea]

**Evento:** `[namespace].[event-name] v1.0`
**Topic:** `topic-[dominio]`
**Subscription:** `sub-[servicio]-[evento]`

#### Pasos
1. [Paso específico]
2. [Paso específico]
3. ...

#### Archivos a modificar/crear
- `src/[servicio]/events/[event-name].js` — definición del evento
- `src/[servicio]/handlers/[event-name]-handler.js` — consumidor
- `src/[servicio]/producers/[event-name]-producer.js` — productor
- `tests/integration/[event-name].test.js` — tests

#### Verificación
- [ ] Tests pasan: `npm test [pattern]`
- [ ] Evento se publica correctamente
- [ ] Consumidor procesa sin errores
- [ ] DLQ vacía después de procesamiento
- [ ] Schema validado contra CloudEvents spec
```

## Revisión del Plan

Después de escribir el plan completo, despachar un revisor de plan (subagente) usando la plantilla de `plan-document-reviewer-prompt.md` adaptada al contexto APB.

**El revisor verifica:**
- Completitud: TODOs, placeholders, tareas incompletas
- Alineación con spec: el plan cubre los requisitos del spec
- Descomposición de tareas: tareas con límites claros, pasos accionables
- Construibilidad: ¿podría un ingeniero seguir este plan sin atascarse?
- Consideraciones de event-driven: ¿cada tarea define eventos, schemas, topología?


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Codigo generado** - primera linea del bloque: `// [IA-GEN] Generado por APB AI Framework (apb-pm-implementation-planning-v1.0) - pendiente revision humana`
- **Commit** - prefijo `[ai-gen]` en el mensaje + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`
- **PR asociado** - label `ai-generated` en GitHub + footer en descripcion del PR
