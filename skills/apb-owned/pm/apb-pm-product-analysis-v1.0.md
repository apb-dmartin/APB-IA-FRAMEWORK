---
id: "apb-pm-product-analysis-v1.0"
name: "Pm Analysis"
description: "An\xE1lisis de producto y requisitos especializado en sistemas orientados a eventos.\
  \ Usar al inicio de un proyecto o feature para definir visi\xF3n, requisitos y casos\
  \ de uso con foco en arquitectura de eventos."
version: "1.0.0"
status: "draft"
owner: "PMO APB <arquitectura@portdebarcelona.cat>"
domain: "pm"
autonomy_level: 1
consumed_by:
  - "apb-agent-spec-engineer-v1.0"
created_date: "2026-06-20"
review_date: "2026-06-24"
---

> Procedencia: Adaptado de bmad-method (bmad-agent-analyst + bmad-product-brief + bmad-prfaq) (licencia MIT). Contenido adaptado y
> generalizado para el APB AI Framework.

# APB PM Analysis: Análisis de Producto Orientado a Eventos

## Visión General

Análisis de producto especializado en sistemas orientados a eventos. Traduce necesidades vagas en especificaciones accionables, manteniendo el foco en cómo los eventos habilitan el flujo de negocio.

**Rol:** Product Manager especializado en arquitecturas de eventos.

## Cuándo Usar

- Inicio de un nuevo proyecto o feature
- Cuando el usuario tiene una idea vaga que necesita cristalizar
- Antes de cualquier diseño técnico
- Cuando se necesita validar suposiciones de negocio
- Para definir el alcance de un MVP orientado a eventos

## El Proceso

### Fase 1: Descubrimiento de Contexto

1. **Entender el dominio del negocio**
   - ¿Qué problema resuelve el producto?
   - ¿Quiénes son los actores (usuarios, sistemas externos)?
   - ¿Cuál es el flujo de valor principal?

2. **Mapear eventos de negocio**
   Identificar eventos del dominio (business events, no técnicos):

   | Evento de Negocio | Actor | Trigger | Resultado |
   |-------------------|-------|---------|-----------|
   | "Cliente realiza pedido" | Cliente | Acción en UI | Orden creada |
   | "Inventario reservado" | Sistema | Orden creada | Stock actualizado |
   | "Pago procesado" | Sistema | Inventario reservado | Orden confirmada |
   | "Envío creado" | Sistema | Pago procesado | Tracking generado |

3. **Identificar bounded contexts**
   - ¿Qué subdominios existen?
   - ¿Cuáles son los contextos delimitados (bounded contexts)?
   - ¿Qué equipos/servicios son responsables de cada contexto?

### Fase 2: Definición de Requisitos

#### Requisitos Funcionales (con perspectiva de eventos)

Para cada evento de negocio, definir:

```markdown
### RF-[N]: [Nombre del requisito]

**Evento de negocio:** [Nombre del evento]
**Contexto:** [Bounded context]

#### Descripción
[Qué debe pasar cuando ocurre el evento]

#### Actores
- **Productor:** [Quién/sistema emite el evento]
- **Consumidores:** [Quiénes/sistemas reaccionan al evento]

#### Flujo de eventos
1. [Evento A] → [Acción 1] → [Evento B]
2. [Evento B] → [Acción 2] → [Evento C]
3. ...

#### Criterios de aceptación
- [ ] Dado [estado], cuando [evento], entonces [resultado]
- [ ] Dado [estado], cuando [evento duplicado], entonces [idempotencia]
- [ ] Dado [estado], cuando [evento falla], entonces [compensación]

#### Métricas de éxito
- [KPI 1]: [Valor objetivo]
- [KPI 2]: [Valor objetivo]
```

#### Requisitos No Funcionales

| Categoría | Requisito | Métrica |
|-----------|-----------|---------|
| **Disponibilidad** | El sistema debe procesar eventos 99.9% del tiempo | Uptime > 99.9% |
| **Latencia** | Eventos procesados en < 5s (p95) | Latencia p95 < 5s |
| **Throughput** | Soportar 1000 eventos/segundo | Throughput > 1000 msg/s |
| **Durabilidad** | Ningún evento perdido | 0 eventos perdidos |
| **Ordenamiento** | Eventos del mismo agregado en orden | Session ordering |
| **Observabilidad** | Trazabilidad de eventos end-to-end | Trace ID en cada evento |

### Fase 3: PRFAQ Challenge (Working Backwards)

Adaptado del método PRFAQ de BMAD, especializado para event-driven:

#### Press Release (6 meses en el futuro)

```markdown
# [Nombre del Producto] — Ahora con Arquitectura de Eventos

## Anuncio
Hoy lanzamos [feature] con procesamiento de eventos en tiempo real,
permitiendo [beneficio principal].

## Beneficios para el Cliente
- [Beneficio 1]: [Cómo los eventos lo habilitan]
- [Beneficio 2]: [Cómo los eventos lo habilitan]
- [Beneficio 3]: [Cómo los eventos lo habilitan]

## Detalles Técnicos
- Procesamiento asíncrono de [N] eventos/segundo
- Tolerancia a fallos con compensación automática
- Visibilidad en tiempo real del estado de cada transacción
```

#### Customer FAQ

```markdown
## Preguntas Frecuentes del Cliente

**Q: ¿Qué pasa si un pago falla después de reservar inventario?**
A: El sistema compensa automáticamente: libera el inventario reservado
   y notifica al cliente. Todo sin intervención manual.

**Q: ¿Puedo ver el estado de mi orden en tiempo real?**
A: Sí. Cada evento del flujo actualiza el estado visible en la UI
   mediante WebSockets alimentados por el stream de eventos.

**Q: ¿El sistema maneja picos de tráfico?**
A: Sí. La arquitectura de eventos permite escalar consumidores
   independientemente según la carga.
```

#### Internal FAQ

```markdown
## Preguntas Frecuentes Internas

**Q: ¿Por qué event-driven y no REST síncrono?**
A: [Justificación técnica y de negocio]

**Q: ¿Cómo manejamos la consistencia eventual?**
A: [Estrategia de consistencia]

**Q: ¿Qué pasa si Service Bus está caído?**
A: [Estrategia de resiliencia]

**Q: ¿Cómo debuggeamos flujos distribuidos?**
A: [Estrategia de observabilidad]
```

### Fase 4: Documento de Producto

Generar `docs/apb/product/product-brief.md`:

```markdown
# Product Brief: [Nombre del Producto]

## Visión
[Una oración que capture la esencia]

## Eventos del Dominio
[Lista de eventos de negocio identificados]

## Bounded Contexts
[Diagrama de contextos delimitados]

## Requisitos Funcionales
[Lista con referencias a RF-[N]]

## Requisitos No Funcionales
[Tabla de métricas]

## Riesgos
| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| [Riesgo 1] | Alta/Media/Baja | Alto/Medio/Bajo | [Estrategia] |

## Métricas de Éxito
[KPIs con valores objetivo]

## Timeline Sugerido
[Fases del proyecto con milestones]
```

## Integración con el Flujo APB

```
[idea vaga] → apb:pm-analysis → [product brief] → apb:brainstorming → [spec técnico]
```


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-pm-product-analysis-v1.0) - pendiente validacion humana. No distribuir sin revision.
