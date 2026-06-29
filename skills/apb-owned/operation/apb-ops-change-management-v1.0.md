---
id: "apb-ops-change-management-v1.0"
name: "Gestión de Cambios ITIL"
description: "Instrumenta el proceso ITIL de gestión de cambios para despliegues en producción: generación de RFC, evaluación de impacto, preparación del expediente para CAB, verificación post-cambio y calendario de ventanas. Gate obligatorio antes de cualquier cambio en producción APB."
version: "1.0.0"
status: "draft"
owner: "SRE / Operaciones APB <arquitectura@portdebarcelona.cat>"
domain: "operation"
autonomy_level: 1
created_date: "2026-06-27"
review_date: "2026-06-27"
---

# Gestión de Cambios ITIL

## Propósito
Instrumentar el proceso ITIL de gestión de cambios antes de cualquier despliegue en producción APB. Genera el RFC (Request for Change), evalúa el impacto, prepara el expediente para el CAB (Change Advisory Board) y verifica que el cambio se completó correctamente.

## Contexto de Uso
- Gate obligatorio antes de despliegues en producción.
- Verificación de que existe RFC aprobado antes de ejecutar un release.
- Preparación del expediente para revisión por el CAB.
- Seguimiento post-cambio y cierre del RFC.

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `change_description` | Texto | Descripción del cambio propuesto | ✅ |
| `affected_systems` | Lista | Sistemas y servicios afectados | ✅ |
| `change_type` | Enum | `standard`, `normal`, `emergency` | ✅ |
| `proposed_window` | Fecha/hora | Ventana de cambio propuesta (inicio y fin) | ✅ |
| `rollback_plan` | Texto | Plan de rollback si el cambio falla | ✅ |
| `requester` | Texto | Nombre y equipo del solicitante | ✅ |
| `jira_reference` | String | Ticket Jira relacionado (si existe) | ❌ |
| `risk_assessment` | Texto | Evaluación de riesgo previa (si existe) | ❌ |

## Flujo de Trabajo

1. **Clasificación del cambio**: Determinar tipo:
   - **Standard**: cambios pre-aprobados de bajo riesgo (despliegues rutinarios con checklist).
   - **Normal**: requiere evaluación y aprobación del CAB.
   - **Emergency**: bypass parcial de proceso, con justificación y revisión post-hoc obligatoria.

2. **Generación del RFC**: Producir documento estructurado con:
   - Descripción del cambio y justificación.
   - Sistemas impactados (producción, staging, integrados).
   - Usuarios y servicios en riesgo durante la ventana.
   - Plan de implementación paso a paso.
   - Plan de rollback con criterios de activación.
   - Responsables: implementador, aprobador, validador post-cambio.

3. **Evaluación de impacto**:
   - ¿Qué servicios quedan en degradación o inactivos durante el cambio?
   - ¿Hay dependencias que pueden verse afectadas?
   - ¿Hay cambios en curso que puedan entrar en conflicto?
   - Nivel de riesgo: ALTO / MEDIO / BAJO.

4. **Verificación de calendario**: Comprobar que la ventana propuesta:
   - No coincide con períodos de congelación de cambios.
   - No solapa con otros cambios programados en los mismos sistemas.
   - Respeta horarios preferentes (fuera de horario crítico para cambios normales).

5. **Preparación del expediente CAB**: Consolidar en formato estándar APB para presentación al comité.

6. **⚠️ CHECKPOINT HUMANO**: El RFC no se ejecuta sin aprobación explícita del responsable de cambios o CAB.

7. **Verificación post-cambio**: Tras el despliegue, verificar:
   - Smoke tests superados.
   - Métricas de servicio estables (error rate, latencia).
   - Rollback no activado.
   - Notificación de cierre a stakeholders.

8. **Cierre del RFC**: Registrar resultado (Exitoso / Fallido / Rollback activado) y lecciones aprendidas.

## Salida Esperada

```markdown
# RFC — [Nombre del Cambio]
> RFC-[número] | Tipo: [standard/normal/emergency] | Riesgo: [ALTO/MEDIO/BAJO]
> Solicitante: [nombre] | Ventana: [inicio] → [fin] | Estado: PENDIENTE APROBACIÓN

## 1. Descripción del Cambio
## 2. Justificación
## 3. Sistemas Afectados
| Sistema | Impacto | Degradación durante cambio |
## 4. Plan de Implementación
| Paso | Acción | Responsable | Duración estimada |
## 5. Plan de Rollback
| Criterio de activación | Acción de rollback | Responsable |
## 6. Verificación Post-Cambio
| Check | Herramienta / Fuente | Umbral de éxito |
## 7. Aprobaciones Requeridas
## 8. Resultado (completar tras el cambio)
```

## Criterios de Calidad
- [ ] El RFC tiene clasificación de tipo y nivel de riesgo documentados.
- [ ] El plan de rollback especifica criterios de activación claros (no ambiguos).
- [ ] Los smoke tests de verificación post-cambio están definidos antes de la ventana.
- [ ] La ventana propuesta respeta el calendario de congelaciones APB.
- [ ] El RFC está aprobado por el responsable de cambios antes de la ejecución.

## Stack y Tecnologías
- Proceso: ITIL v4 Change Management
- Registro: Jira Service Management (JSM) — tickets de tipo Change
- Notificación: apb-plat-ms-notify-v1.0 (Teams)
- Evidencia: apb-gov-evidence-v1.0, apb-gov-jira-evidence-v1.0

## Dependencias
- `apb-ops-runbook-v1.0` — para el plan de implementación paso a paso
- `apb-gov-jira-evidence-v1.0` — para crear el ticket de cambio en JSM
- `apb-gov-evidence-v1.0` — para evidencia del cierre
- `apb-plat-ms-notify-v1.0` — para notificación a stakeholders

## Ejemplo de Uso

```
Necesito abrir un RFC para el despliegue del servicio APB-EXP-API v2.1 en producción:
- Cambio: actualización de endpoints REST con breaking change en /api/v1/expedientes
- Sistemas afectados: APB-EXP-API, portal ciudadano, integración SAP
- Ventana propuesta: sábado 5 julio 2026, 02:00-04:00
- Tipo: normal (requiere aprobación CAB)
- Rollback: revertar al tag v2.0 en el registry y desplegar con pipeline de rollback
```

## Notas y Advertencias
- **Nivel 1**: El agente genera el RFC y la documentación; no despliega ni ejecuta cambios directamente.
- Los cambios de emergencia deben tener justificación explícita y revisión post-hoc en <24h.
- La congelación de cambios en APB se activa en períodos críticos de operación portuaria.
- El CAB debe revisar todos los cambios de tipo `normal` y `emergency` con riesgo ALTO.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-27 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento A, Bloque 2 |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-ops-change-management-v1.0) - pendiente validacion humana. No distribuir sin revision.
