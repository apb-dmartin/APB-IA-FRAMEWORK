---
id: "apb-ops-alerting-design-v1.0"
name: "Diseño de Alertas Operacionales"
description: "Diseña el sistema de alertas para un servicio APB: umbrales de disparo, severidades (P1-P4), rutas de escalado, páginas de guardia, silencias programadas y runbooks asociados. Garantiza que cada alerta tenga un runbook y que no haya alertas sin propietario."
version: "1.0.0"
status: "draft"
owner: "SRE APB <arquitectura@portdebarcelona.cat>"
domain: "operation"
autonomy_level: 1
created_date: "2026-06-29"
review_date: "2026-06-29"
---

# Diseño de Alertas Operacionales

## Propósito
Definir el sistema de alertas operacionales de un servicio: qué se monitoriza, cuándo se dispara una alerta, con qué severidad, quién recibe la notificación y qué debe hacer. El output es un catálogo de alertas listo para implementar en Azure Monitor / Grafana.

## Contexto de Uso
- Definición inicial de alertas al poner un servicio en producción.
- Revisión de alertas tras un post-incident review (PIR).
- Auditoría de alertas existentes: detectar alertas sin runbook, sin owner o con umbrales inadecuados.
- Preparación ante períodos de alta demanda (temporada de cruceros APB).

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `service_name` | Texto | Nombre del servicio o componente | ✅ |
| `slo_definitions` | JSON / Markdown | SLOs definidos: disponibilidad, latencia, error rate | ✅ |
| `existing_alerts` | JSON / Lista | Alertas ya configuradas (para auditoría o revisión) | ❌ |
| `on_call_schedule` | Texto | Horario de guardia: 24x7, L-V 8-20h, etc. | ❌ |
| `escalation_contacts` | Lista | Contactos por nivel: L1 (NOC), L2 (SRE), L3 (arquitectura) | ❌ |

## Flujo de Trabajo

1. **Inventario de señales monitorizables**:
   - Métricas de infraestructura: CPU, memoria, disco, red (de Azure Monitor).
   - Métricas de aplicación: latencia p99, error rate, throughput, saturación de colas.
   - Health checks: endpoints `/health`, `/ready`, `/live`.
   - Logs: patrones de error, excepciones no controladas, timeouts.

2. **Definición de umbrales por SLO**:
   - Derivar umbrales de alerta desde los SLOs: si el SLO de disponibilidad es 99.9%, la alerta debe dispararse antes de alcanzar el burn rate que compromete el SLO.
   - Usar burn rate alerts (modelo SRE Google) cuando hay presupuesto de error definido.
   - Umbrales conservadores para evitar alert fatigue: preferir p90-p95 sobre medias.

3. **Clasificación de severidad**:
   - **P1 — Crítico**: servicio no disponible, impacto en operaciones portuarias o ciudadanos. Respuesta: <15 min.
   - **P2 — Alto**: degradación significativa, SLO en riesgo. Respuesta: <1 hora.
   - **P3 — Medio**: anomalía con tendencia preocupante, sin impacto inmediato. Respuesta: <4 horas.
   - **P4 — Bajo**: informativo, tendencia a observar. Sin respuesta urgente.

4. **Rutas de escalado**:
   - P1/P2: notificación inmediata al on-call + canal Teams `#alerts-criticos`.
   - P3: ticket Jira automático + notificación al equipo responsable.
   - P4: dashboard únicamente (sin notificación activa).
   - Auto-escalado: si P2 sin ACK en 30 min → escalar a L2.

5. **Silencias programadas**:
   - Ventanas de mantenimiento: silenciar alertas P3/P4 durante deploys planificados.
   - Períodos de bajo tráfico nocturno: ajustar umbrales o silenciar alertas no críticas.
   - Eventos estacionales APB: ajuste de umbrales en temporada alta de cruceros.

6. **Runbooks asociados**:
   - Cada alerta P1/P2 debe tener un runbook en Confluence/wiki.
   - Runbook mínimo: síntoma, diagnóstico inmediato (3-5 pasos), mitigación, escalado.
   - Enlace al runbook incluido en el mensaje de la alerta.

7. **⚠️ CHECKPOINT HUMANO**: El catálogo de alertas debe ser validado por el equipo SRE y el propietario del servicio antes de activar en producción.

## Salida Esperada

```markdown
# Catálogo de Alertas — [Servicio]
> Generado: [fecha] | SLO base: [ref] | Revisión requerida por: [fecha]

## Resumen
| Total alertas | P1 | P2 | P3 | P4 | Sin runbook |

## Catálogo de Alertas

| ID | Nombre | Señal | Umbral | Severidad | Canal | Runbook | Owner |
|---|---|---|---|---|---|---|---|
| ALT-001 | Alta tasa de errores | error_rate_5xx | >5% en 5 min | P1 | Teams #alerts-criticos + on-call | [link] | SRE |
| ... |

## Silencias Programadas
| Ventana | Alertas silenciadas | Justificación |

## Gaps Detectados (si modo auditoría)
| Alerta | Problema | Acción recomendada |
```

## Criterios de Calidad
- [ ] Cada alerta P1/P2 tiene runbook asociado con enlace.
- [ ] Cada alerta tiene un owner explícito (equipo o persona).
- [ ] Los umbrales están derivados de los SLOs definidos, no son valores arbitrarios.
- [ ] No hay alertas duplicadas (misma señal, mismo umbral, distintos nombres).
- [ ] Las silencias programadas están documentadas con justificación.
- [ ] El canal de notificación es apropiado para la severidad.

## Stack y Tecnologías
- Monitorización: Azure Monitor, Grafana Alerting, Application Insights
- Notificaciones: Azure Action Groups, Microsoft Teams webhooks
- On-call: PagerDuty (si disponible) o rotación manual documentada
- Runbooks: Confluence APB o GitHub Wiki

## Dependencias
- `apb-ops-slo-design-v1.0` — los SLOs son el input principal para derivar umbrales
- `apb-ops-observability-v1.0` — las señales deben estar instrumentadas antes de alertar
- `apb-ops-runbook-v1.0` — cada alerta P1/P2 requiere un runbook existente

## Ejemplo de Uso

```
Diseña el sistema de alertas para el servicio de reservas de cruceros APB.
El SLO de disponibilidad es 99.9% mensual y el de latencia es p99 < 2 segundos.
Tenemos guardia 24x7 con rotación semanal entre 3 SREs.
Necesito alertas en Azure Monitor exportadas a Teams y un catálogo documentado.
```

## Notas y Advertencias
- **Nivel 1**: El catálogo de alertas requiere validación humana antes de activar en producción.
- Evitar alert fatigue: más de 5 alertas P1/P2 por semana indica que los umbrales son demasiado sensibles.
- Las alertas deben evolucionar con el servicio: revisar tras cada PIR y cada cambio de SLO.
- En temporada alta de cruceros APB, revisar y ajustar umbrales de capacidad preventivamente.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento B, Bloque 2 |

## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-ops-alerting-design-v1.0) - pendiente validacion humana. No distribuir sin revision.
