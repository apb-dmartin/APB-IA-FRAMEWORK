---
id: "apb-disc-brainstorming-v1.0"
name: "Brainstorming"
description: "OBLIGATORIO antes de cualquier trabajo creativo en el APB AI Framework. Explora intenci\xF3\
  n del usuario, requisitos y dise\xF1o antes de implementaci\xF3n, con foco en arquitecturas\
  \ orientadas a eventos y microservicios."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "discovery"
autonomy_level: 1
consumed_by:
  - "apb-agent-business-analyst-v1.0"
created_date: "2026-06-20"
review_date: "2026-06-24"
---

> Procedencia: Adaptado de obra/superpowers (brainstorming) + bmad-method (analysis-phase) (licencia MIT).

# APB Brainstorming: De Ideas a Diseños de Eventos

Transforma ideas en diseños completos y especificaciones para sistemas orientados a eventos mediante diálogo colaborativo natural.

## Contexto del APB

Este skill opera dentro del **APB AI Framework** (103 componentes, 18 agentes, 7 workflows). Antes de cualquier implementación, el agente DEBE entender:
- **Stack tecnológico**: Azure Service Bus (broker de eventos), JSON + CloudEvents (schemas), DevExpress con JavaScript puro (UI)
- **Arquitectura**: Microservicios orientados a eventos, eventual consistency, sagas distribuidas
- **Patrones clave**: Outbox pattern, idempotencia, compensating transactions, dead letter handling

## Puerta de Control (HARD-GATE)

<CONTROL>
NO invoques ningún skill de implementación, escribas código, generes scaffolding, ni tomes acción de implementación hasta haber presentado un diseño y el usuario lo haya aprobado. Esto aplica a TODO proyecto sin importar su simplicidad percibida.
</CONTROL>

## Anti-Patrón: "Esto Es Demasiado Simple Para Necesitar Diseño"

Todo proyecto pasa por este proceso. Una lista de tareas, una utilidad de una función, un cambio de configuración — todos. Los proyectos "simples" son donde las suposiciones no examinadas causan más trabajo desperdiciado. El diseño puede ser corto (unas pocas oraciones para proyectos realmente simples), pero DEBES presentarlo y obtener aprobación.

## Checklist del Proceso

Debes crear una tarea para cada ítem y completarlos en orden:

1. **Explorar contexto del proyecto** — revisar archivos, docs, commits recientes, contratos de eventos existentes
2. **Entender topología actual de eventos** — topics, subscriptions, schemas CloudEvents registrados
3. **Hacer preguntas clarificadoras** — una a la vez, entender propósito/restricciones/criterios de éxito
4. **Proponer 2-3 enfoques** — con trade-offs y tu recomendación, considerando:
   - Patrón de comunicación: coreografía vs orquestación de sagas
   - Garantía de entrega: at-least-once vs exactly-once
   - Consistencia: eventual vs fuerte
   - Escalabilidad: particionamiento de streams
5. **Presentar diseño** — en secciones escaladas a su complejidad, obtener aprobación del usuario después de cada sección
6. **Escribir documento de diseño** — guardar en `docs/apb/specs/YYYY-MM-DD-<tema>-design.md` y commitear
7. **Auto-revisión de spec** — verificación rápida inline de placeholders, contradicciones, ambigüedad, alcance
8. **Usuario revisa spec escrito** — pedir al usuario que revise el archivo spec antes de proceder
9. **Transición a implementación** — invocar skill `apb:planning` para crear plan de implementación

## Consideraciones Específicas de Event-Driven

### Preguntas Obligatorias

Para cada feature, DEBES clarificar:

| Aspecto | Preguntas |
|---------|-----------|
| **Eventos** | ¿Qué eventos se emiten? ¿Cuál es el schema CloudEvents? |
| **Productores** | ¿Qué servicios publican? ¿Usan outbox pattern? |
| **Consumidores** | ¿Qué servicios suscriben? ¿Competing consumers o sessions? |
| **Ordenamiento** | ¿Se requiere procesamiento ordenado? ¿Session keys? |
| **Idempotencia** | ¿Cómo se manejan duplicados? ¿Duplicate detection de Service Bus? |
| **Compensación** | ¿Qué pasa si un paso falla? ¿Saga coreografía u orquestación? |
| **DLQ** | ¿Cuál es la estrategia de dead letter? ¿Reintentos con backoff? |
| **Schemas** | ¿JSON + CloudEvents? ¿Versionado de schemas? ¿Backward compatibility? |

### Diagramas Recomendados

Incluir diagramas de:
- Flujo de eventos (event choreography)
- Topología de Service Bus (topics, subscriptions, rules)
- Estados de saga (state machine)
- Secuencia de compensación

## Flujo del Proceso

```
Explorar contexto → Entender topología → Preguntar clarificadoras
         ↓
Proponer enfoques (2-3) → Presentar diseño por secciones
         ↓
Aprobación usuario → Escribir spec → Auto-revisión
         ↓
Revisión usuario → Invocar apb:planning
```


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-disc-brainstorming-v1.0) - pendiente validacion humana. No distribuir sin revision.
