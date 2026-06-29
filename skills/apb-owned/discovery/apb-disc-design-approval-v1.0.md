---
id: "apb-disc-design-approval-v1.0"
name: "Design Approval"
description: "Usar despu\xE9s de presentar un dise\xF1o en apb-brainstorming, antes de proceder\
  \ a apb-planning. Gate de aprobaci\xF3n de dise\xF1o con verificaciones espec\xED\
  ficas de arquitectura de eventos."
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

> Procedencia: Adaptado de obra/superpowers (brainstorming design approval gate) (licencia MIT).

# APB Design Approval: Puerta de Aprobación de Diseño

## Visión General

Antes de que cualquier diseño pase a planificación e implementación, DEBE ser aprobado mediante una revisión estructurada. Este skill actúa como gate de calidad entre el brainstorming y la planificación.

**Principio fundamental:** Diseño aprobado = menos retrabajo en implementación.

## Cuándo Usar

**Obligatorio:**
- Después de completar `apb:brainstorming` y antes de invocar `apb:planning`
- Cuando el usuario aprueba un diseño conceptualmente pero necesita validación técnica
- Antes de cualquier cambio de arquitectura significativo

## El Proceso de Aprobación

### Paso 1: Auto-Revisión del Diseño

Revisar el documento de diseño (`docs/apb/specs/YYYY-MM-DD-<tema>-design.md`) contra esta checklist:

#### Checklist de Event-Driven (Obligatoria)

| # | Verificación | Estado |
|---|-------------|--------|
| 1 | ¿Todos los eventos están definidos con tipo CloudEvents? | ☐ |
| 2 | ¿Cada evento tiene schema JSON documentado? | ☐ |
| 3 | ¿Se identificaron productores y consumidores de cada evento? | ☐ |
| 4 | ¿La topología de Service Bus está definida (topics/subscriptions)? | ☐ |
| 5 | ¿Se consideró idempotencia para todos los consumidores? | ☐ |
| 6 | ¿Se definieron compensaciones para sagas (si aplica)? | ☐ |
| 7 | ¿Se configuró dead letter handling? | ☐ |
| 8 | ¿Los schemas tienen estrategia de versionado? | ☐ |
| 9 | ¿Se consideró ordenamiento (session keys si aplica)? | ☐ |
| 10 | ¿El diseño es backward compatible con eventos existentes? | ☐ |

#### Checklist General de Diseño

| # | Verificación | Estado |
|---|-------------|--------|
| 11 | ¿No hay placeholders ni "TBD" en el diseño? | ☐ |
| 12 | ¿No hay contradicciones internas? | ☐ |
| 13 | ¿Los requisitos son claros (no ambiguos)? | ☐ |
| 14 | ¿El alcance está enfocado (un solo subsistema)? | ☐ |
| 15 | ¿No hay features no solicitadas (YAGNI)? | ☐ |
| 16 | ¿Las interfaces entre componentes están definidas? | ☐ |
| 17 | ¿Se consideraron edge cases? | ☐ |
| 18 | ¿El diseño es construible (no over-engineered)? | ☐ |

### Paso 2: Revisión por Subagente

Despachar revisor de diseño:

```
Subagente (general-purpose):
  description: "Revisar diseño de arquitectura de eventos"
  prompt: |
    Revisa el siguiente diseño de arquitectura orientada a eventos.

    ## Diseño a Revisar
    [Ruta al archivo de diseño]

    ## Verificaciones de Event-Driven
    1. ¿Los eventos siguen CloudEvents 1.0?
    2. ¿Los schemas JSON están completos y validables?
    3. ¿La topología de Service Bus es coherente?
    4. ¿Hay riesgos de inconsistencia eventual no manejados?
    5. ¿Las compensaciones de saga son idempotentes?
    6. ¿La estrategia de DLQ es adecuada?
    7. ¿El versionado de schemas es sostenible?

    ## Verificaciones de Arquitectura
    8. ¿Las fronteras de servicio (bounded contexts) son claras?
    9. ¿Hay acoplamiento innecesario entre servicios?
    10. ¿Se consideró observabilidad (logs, métricas, tracing)?
    11. ¿Hay single points of failure?
    12. ¿La estrategia de escalabilidad es realista?

    ## Formato de Salida
    ## Revisión de Diseño

    **Estado:** Aprobado | Problemas Encontrados | Rechazado

    **Problemas Críticos:**
    - [Descripción] — [Impacto]

    **Problemas Importantes:**
    - [Descripción] — [Impacto]

    **Problemas Menores:**
    - [Descripción]

    **Recomendaciones:**
    - [Sugerencias de mejora]
```

### Paso 3: Aprobación del Usuario

Presentar resultado de la revisión al usuario:

```
Diseño revisado. Resultado: [Aprobado / Problemas Encontrados / Rechazado]

[Resumen de hallazgos]

¿Procedemos con la planificación (apb:planning) o ajustamos el diseño?
```

**Si hay problemas críticos:** Volver a `apb:brainstorming` para corregir.
**Si hay problemas importantes:** Corregir inline, re-revisar.
**Si aprobado:** Invocar `apb:planning`.

## Integración con el Flujo APB

```
apb:brainstorming → [diseño aprobado] → apb:design-approval → [aprobado] → apb:planning
                          ↓ rechazado              ↓ problemas
                    [corregir diseño]         [corregir inline]
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
  > **Borrador generado por IA** (APB AI Framework - apb-disc-design-approval-v1.0) - pendiente validacion humana. No distribuir sin revision.
