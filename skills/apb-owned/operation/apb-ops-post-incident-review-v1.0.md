---
id: "apb-ops-post-incident-review-v1.0"
name: "Post-Incident Review (PIR) Blameless"
description: "Genera el Post-Incident Review (PIR) blameless tras una incidencia significativa: timeline reconstruido, impacto real medido, análisis 5-Why, action items con owner y fecha límite. Cultura de aprendizaje sin culpa."
version: "1.0.0"
status: "draft"
owner: "SRE / Operaciones APB <arquitectura@portdebarcelona.cat>"
domain: "operation"
autonomy_level: 1
created_date: "2026-06-27"
review_date: "2026-06-27"
---

# Post-Incident Review (PIR) Blameless

## Propósito
Generar el Post-Incident Review (PIR) estructurado y blameless tras una incidencia significativa. El PIR reconstruye el timeline, mide el impacto real, identifica la causa raíz mediante 5-Why, y define action items accionables con owner y fecha límite para prevenir recurrencia.

## Contexto de Uso
- Tras cualquier incidencia de severidad P1 o P2.
- Incidencias P3 con patrón recurrente detectado por Problem Management.
- Revisión periódica de incidencias cerradas (sesión mensual de calidad de servicio).

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `incident_id` | String | ID del ticket de incidencia en JSM | ✅ |
| `incident_summary` | Texto | Descripción de lo que ocurrió | ✅ |
| `timeline_events` | Lista | Eventos cronológicos con timestamps | ✅ |
| `affected_users` | Número | Usuarios o servicios impactados | ✅ |
| `downtime_minutes` | Número | Minutos de servicio degradado o no disponible | ✅ |
| `responders` | Lista | Personas que participaron en la respuesta | ✅ |
| `contributing_factors` | Lista | Factores identificados durante la respuesta | ❌ |
| `existing_rca` | Texto | RCA previo si ya se realizó | ❌ |

## Flujo de Trabajo

1. **Recopilación de contexto**: Consolidar toda la información de la incidencia: ticket JSM, logs, alertas, comunicaciones de Teams/email durante el incidente.

2. **Reconstrucción del timeline**: Ordenar cronológicamente todos los eventos relevantes:
   - Cuándo empezó la degradación real (no cuándo se detectó).
   - Cuándo se recibió la primera alerta.
   - Cuándo se identificó la causa.
   - Cuándo se aplicó la mitigación.
   - Cuándo se restableció el servicio completamente.

3. **Medición del impacto real**:
   - Tiempo total de indisponibilidad / degradación.
   - Usuarios/servicios afectados (con datos reales, no estimaciones).
   - Impacto en SLOs: ¿se consumió error budget?
   - Impacto económico o reputacional si aplica.

4. **Análisis blameless de causa raíz (5-Why)**:
   - Partir del síntoma observable.
   - Preguntar "¿Por qué?" cinco veces hasta llegar a la causa sistémica.
   - Identificar factores contribuyentes (no solo la causa directa).
   - **Principio blameless**: las personas actúan según el contexto y las herramientas disponibles. El PIR busca mejorar sistemas, no culpar individuos.

5. **Identificación de factores contribuyentes**: Clasificar por categoría:
   - Código / Defecto
   - Configuración / Infraestructura
   - Proceso / Procedimiento
   - Monitorización / Alertas
   - Documentación / Runbooks
   - Capacidad / Escalado

6. **Definición de action items**: Para cada causa raíz o factor contribuyente:
   - Acción concreta y verificable.
   - Owner (persona, no equipo genérico).
   - Fecha límite.
   - Prioridad: CRÍTICO / ALTO / MEDIO.
   - Ticket Jira de seguimiento.

7. **⚠️ CHECKPOINT HUMANO**: El responsable del servicio valida el PIR antes de publicarlo. Los action items requieren compromiso explícito de los owners.

8. **Publicación y seguimiento**: Publicar en Confluence. Revisar estado de action items en la siguiente reunión de operaciones (≤2 semanas).

## Salida Esperada

```markdown
# Post-Incident Review — [Nombre del Incidente]
> INC-[número] | Severidad: [P1/P2/P3] | Fecha: [fecha]
> **Blameless**: Este documento busca aprendizaje sistémico, no responsabilidad individual.

## Resumen Ejecutivo
| Métrica | Valor |
|---|---|
| Duración total | [X horas Y minutos] |
| Tiempo detección | [X minutos desde inicio] |
| Usuarios afectados | [número] |
| Impacto en SLO | [X% de error budget consumido] |

## Timeline Reconstruido
| Timestamp | Evento | Actor |

## Causa Raíz (5-Why)
- **Síntoma:** [observable]
- **¿Por qué 1?** → [causa 1]
- **¿Por qué 2?** → [causa 2]
- **¿Por qué 3?** → [causa 3]
- **¿Por qué 4?** → [causa 4]
- **¿Por qué 5?** → **[causa raíz sistémica]**

## Factores Contribuyentes
| Factor | Categoría | Descripción |

## Lo que fue bien
## Lo que no fue bien

## Action Items
| # | Acción | Owner | Fecha límite | Prioridad | Ticket |
```

## Criterios de Calidad
- [ ] El timeline incluye el tiempo real de inicio de la degradación (no solo la detección).
- [ ] El análisis 5-Why llega a una causa sistémica, no se queda en causa directa.
- [ ] Todos los action items tienen owner nominal (persona), fecha límite y ticket de seguimiento.
- [ ] El documento no menciona nombres en tono de culpa.
- [ ] El impacto en SLOs está cuantificado.

## Stack y Tecnologías
- Proceso: Google SRE Book (Postmortem Culture), ITIL v4
- Registro: Jira Service Management + Confluence
- Análisis: `apb-ops-rca-v1.0` (complementario)

## Dependencias
- `apb-ops-rca-v1.0` — análisis de causa raíz
- `apb-gov-knowledge-v1.0` — publicación en base de conocimiento
- `apb-gov-jira-evidence-v1.0` — creación de action items en Jira

## Ejemplo de Uso

```
Genera el PIR de la incidencia INC-2024-0847 (caída del portal ciudadano APB,
sábado 15 junio, 14:00-17:30, ~2.400 usuarios afectados). El equipo identificó
que una migración de BD ejecutada a las 13:45 dejó una constraint rota.
Responders: equipo de guardia (Ana, Carlos) y DBA (Miguel).
```

## Notas y Advertencias
- **Nivel 1**: El agente estructura y redacta; los owners de action items son personas reales que deben comprometerse.
- El PIR debe completarse en ≤5 días hábiles tras el incidente mientras la memoria está fresca.
- La cultura blameless no elimina la responsabilidad de mejorar; elimina la culpa como fin en sí misma.
- Para incidencias de seguridad, coordinr con Security Architect antes de publicar detalles técnicos.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-27 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento A, Bloque 2 |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-ops-post-incident-review-v1.0) - pendiente validacion humana. No distribuir sin revision.
