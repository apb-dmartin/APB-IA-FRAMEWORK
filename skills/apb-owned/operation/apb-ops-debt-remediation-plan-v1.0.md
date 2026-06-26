---
id: "apb-ops-debt-remediation-plan-v1.0"
name: "Plan de Remediación de Deuda Técnica"
description: "Consolida los hallazgos de auditoría de deuda técnica, vulnerabilidades, dependencias y rendimiento en un plan único priorizado, lo presenta para aprobación humana, y crea los tickets Jira correspondientes únicamente tras OK explícito."
version: "1.0.0"
status: "draft"
owner: "Gobierno TI APB <arquitectura@portdebarcelona.cat>"
domain: "operation"
autonomy_level: 2
created_date: "2026-06-24"
review_date: "2026-06-24"
---

> Autonomy Level 2 (Ejecución supervisada): esta skill SÍ ejecuta una acción con efecto real
> (creación de tickets Jira), pero únicamente después de mostrar la propuesta completa al
> humano y recibir su confirmación explícita. Nunca crea tickets antes de ese punto de
> control. Decisión de Debora (Sesión 11, post-Sesión 9).

# Plan de Remediación de Deuda Técnica

---

## 🎯 Propósito

Toma los hallazgos generados por `apb-ops-dependency-audit-v1.0`,
`apb-ops-perf-bottleneck-v1.0`, y opcionalmente `apb-dev-sonar-clean-v1.0` /
`apb-agent-risk-exception-v1.0`, los consolida en un único plan priorizado, lo presenta al
humano para revisión, y solo tras recibir confirmación explícita ("OK", "aprobado", o
equivalente inequívoco) crea los tickets Jira correspondientes vía
`apb-gov-jira-evidence-v1.0` / `prov-atlassian-v1.0`.

---

## ⚡ Trigger

Tras completar una auditoría de `apb-agent-tech-debt-v1.0` (dependencias + rendimiento +
incumplimientos de política), cuando hay hallazgos que requieren acción y se necesita
convertirlos en trabajo planificado y trazable.

---

## 📥 Input

- Hallazgos de `apb-ops-dependency-audit-v1.0` (dependencias/vulnerabilidades)
- Hallazgos de `apb-ops-perf-bottleneck-v1.0` (rendimiento)
- Hallazgos de incumplimiento de políticas APB (`apb-gov-policy-check-v1.0`, si aplica)
- Proyecto Jira destino y convenciones de issue type del equipo

---

## 📤 Output

- Plan de remediación priorizado, mostrado al humano antes de cualquier acción
- Confirmación humana registrada (quién aprobó, cuándo, qué versión del plan)
- Tickets Jira creados (solo tras confirmación) — uno por acción del plan, vinculados a un
  épica/ticket padre de remediación de deuda técnica

---

## 🔄 Proceso

### Fase 1: Consolidación
1. Recopilar todos los hallazgos de las skills de diagnóstico de la sesión de auditoría.
2. Eliminar duplicados (ej. una misma dependencia obsoleta detectada por dos análisis).
3. Priorizar: Critical (vulnerabilidades con CVE activo) → High (rendimiento con SLO
   incumplido) → Medium (obsolescencia sin CVE, incumplimiento de política no crítico) →
   Low (mejoras menores).

### Fase 2: Presentación para Aprobación (PUNTO DE CONTROL OBLIGATORIO)
4. Mostrar el plan completo al humano: cada acción con severidad, esfuerzo estimado, y
   ticket Jira propuesto (título, descripción, issue type, proyecto).
5. **Esperar confirmación explícita.** No se procede a la Fase 3 sin un "OK" / "aprobado" /
   equivalente inequívoco del humano. Si el humano pide cambios, se ajusta el plan y se
   vuelve a presentar — nunca se asume aprobación parcial o implícita.
6. Si el humano no responde o la respuesta es ambigua, la skill NO crea ningún ticket y
   pregunta de nuevo explícitamente.

### Fase 3: Ejecución (solo tras OK)
7. Invocar `apb-gov-jira-evidence-v1.0` para crear cada ticket del plan aprobado, vinculado
   a un ticket padre de tipo Epic o Task "Remediación de deuda técnica — [fecha]".
8. Registrar en el output final: lista de tickets creados con sus claves Jira reales.

---

## 📋 Reglas y Constraints

- **Ningún ticket se crea sin el punto de control de la Fase 2 cumplido.** Esta es la regla
  no negociable de esta skill — si se omite, es un defecto de la skill, no una optimización.
- Si el plan cambia entre la presentación y la aprobación (ej. nuevo hallazgo detectado),
  se re-presenta el plan actualizado; no se mezcla aprobación de una versión anterior con
  ejecución de una versión nueva.
- El agente nunca se auto-aprueba ni interpreta silencio como aprobación.

---

## 🛠 Stack Tecnológico Relevante

- Jira Cloud / Data Center vía `prov-atlassian-v1.0`
- Markdown para la presentación del plan antes de la conversión a tickets

---

## 💡 Ejemplos de Uso

**Ejemplo — Plan con aprobación:**
> Plan presentado: 3 acciones (1 Critical: CVE en Newtonsoft.Json; 1 High: query N+1 en
> VesselController; 1 Medium: .NET 6 EOL).
> Humano: "OK, créalos."
> Resultado: 3 tickets creados en proyecto APB, vinculados a épica padre "Remediación deuda
> técnica — 2026-06-24". Output devuelve las 3 claves Jira reales.

**Ejemplo — Plan rechazado parcialmente:**
> Plan presentado: 3 acciones.
> Humano: "La de .NET 6 todavía no, lo demás sí."
> Resultado: skill re-presenta plan con solo 2 acciones, espera nueva confirmación antes de
> crear esos 2 tickets. La acción de .NET 6 queda registrada como diferida, no descartada.

---

## 🔗 Dependencias

- `apb-ops-dependency-audit-v1.0` — fuente de hallazgos de dependencias
- `apb-ops-perf-bottleneck-v1.0` — fuente de hallazgos de rendimiento
- `apb-gov-jira-evidence-v1.0` — ejecución real de creación de tickets (no se reimplementa
  aquí, se reutiliza)
- `prov-atlassian-v1.0` — conectividad con Jira (transitiva, vía la skill anterior)
- Consumida por: `apb-agent-tech-debt-v1.0`

---

## 📝 Notas

- Nivel 2: única skill de esta familia con efecto real fuera del framework (creación de
  tickets), y por eso es la única con el punto de control humano explícito documentado como
  regla no negociable.
- No reemplaza el juicio del Comité de Gobierno para deuda crítica que requiera presupuesto
  o re-priorización de roadmap — eso se eleva por canales normales de PM, esta skill solo
  traduce hallazgos técnicos en tickets ejecutables.

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*

> **Generado por IA:** Claude (Anthropic), Sesión 11 del plan de remediación APB-IA-FRAMEWORK.
> **Validado por humano:** _pendiente — completar nombre/rol del validador antes de pasar a `candidate`._


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Label Jira**: `ia-generado` - campo Labels del ticket
- **Footer en descripcion del ticket**: `Generado por IA (APB AI Framework - apb-ops-debt-remediation-plan-v1.0). Requiere validacion humana antes de ejecutar.`
