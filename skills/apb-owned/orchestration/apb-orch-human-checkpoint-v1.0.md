---
id: "apb-orch-human-checkpoint-v1.0"
name: "Human Checkpoint Protocol"
description: "Protocolo operativo para pausas de aprobación humana en mitad de un workflow. Define el formato del output de pausa, los criterios de reanudación, el comportamiento del agente si el humano rechaza, y cómo documentar la decisión para trazabilidad. Complementa los human_review_points del SCHEMA.md con instrucciones ejecutables."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "orchestration"
autonomy_level: 1
consumed_by:
  - "apb-agent-governance-v1.0"
created_date: "2026-06-29"
review_date: "2026-12-29"
---

# Human Checkpoint Protocol

---

## 🎯 Propósito

Operativizar los `human_review_points` declarados en el frontmatter de cada agente y workflow: definir exactamente qué presenta el agente al llegar a un checkpoint, qué espera del humano, cómo registra la decisión y qué hace si el humano aprueba, rechaza, solicita cambios o no responde.

> Esta skill NO añade checkpoints donde no los hay — los checkpoints los define cada agente/workflow en su frontmatter. Esta skill define cómo comportarse **en** esos checkpoints.

---

## ⚡ Trigger

Invocar esta skill cuando un agente llega a un punto marcado como `human_review_points` en su frontmatter, o cuando un workflow tiene una fase etiquetada como gate de aprobación humana.

---

## 📋 Formato de Output en el Checkpoint

Cuando el agente llega a un checkpoint, produce un bloque de pausa estructurado:

```markdown
---
## ⏸️ CHECKPOINT DE APROBACIÓN HUMANA

**Agente:** <id-agente>
**Checkpoint:** <nombre del human_review_point>
**Workflow (si aplica):** <id-workflow>

### ¿Qué se ha completado hasta aquí?
<resumen del trabajo previo — máximo 5 puntos>

### ¿Qué se necesita revisar?
<descripción precisa de lo que el humano debe evaluar>

### Artefactos para revisión
| Artefacto | Tipo | Ubicación |
|-----------|------|-----------|
| <nombre> | <Markdown / YAML / Ticket> | <ruta o ID> |

### Opciones de respuesta
- ✅ **Aprobar** — el agente continúa al siguiente paso
- 🔄 **Solicitar cambios** — indicar qué debe modificarse antes de continuar
- ❌ **Rechazar** — el agente detiene el workflow y registra la razón

**El agente permanece en pausa hasta recibir respuesta explícita.**
---
```

---

## ⚠️ Comportamiento ante inputs incompletos

| Input | Obligatorio | Si falta |
|-------|------------|----------|
| ID del agente que invoca el checkpoint | ✅ | Bloquea: no se puede registrar trazabilidad sin identificar el agente |
| Nombre del `human_review_point` | ✅ | Bloquea: el checkpoint debe corresponder a uno declarado en el frontmatter |
| Artefactos para revisión | ✅ | Bloquea: sin artefactos el humano no puede revisar nada |
| Workflow (si aplica) | ❌ | Asume: checkpoint individual fuera de workflow formal |
| Contexto previo | ❌ | Asume: el humano puede consultar el historial de la sesión |

---

## 🔄 Comportamiento según la respuesta humana

| Respuesta | Acción del agente |
|-----------|------------------|
| ✅ **Aprobado** | Registra `approved_by`, `approved_at` y continúa al siguiente paso del workflow |
| 🔄 **Cambios solicitados** | Registra los cambios solicitados, los aplica y vuelve al mismo checkpoint para re-revisión |
| ❌ **Rechazado** | Detiene el workflow, registra la razón del rechazo y genera un informe de cierre con las opciones disponibles (reanudar desde un paso anterior, archivar, escalar) |
| ⏰ **Sin respuesta** | El agente no reanuda por su cuenta. Si está configurado con un timeout, envía un recordatorio; si no, permanece en pausa indefinidamente hasta recibir respuesta |

---

## 📋 Registro de la Decisión

Tras la respuesta humana, el agente genera un registro de trazabilidad:

```yaml
checkpoint_log:
  agent: "<id-agente>"
  checkpoint: "<nombre>"
  timestamp_pause: "YYYY-MM-DD HH:MM"
  timestamp_response: "YYYY-MM-DD HH:MM"
  decision: "approved | changes_requested | rejected"
  reviewer: "<nombre/rol del revisor>"
  notes: "<observaciones del revisor, si las hay>"
  artifacts_reviewed:
    - "<artefacto-1>"
    - "<artefacto-2>"
```

Este registro se añade al artefacto principal del workflow para trazabilidad completa.

---

## ⚠️ Restricciones Críticas

- **El agente no continúa sin respuesta explícita.** Ningún timeout o ausencia de respuesta equivale a aprobación.
- **El agente no se auto-aprueba.** Aunque el resultado sea técnicamente correcto, la aprobación humana es obligatoria si está declarada en `human_review_points`.
- **El agente no omite checkpoints** aunque el flujo anterior haya ido sin problemas. Cada checkpoint es independiente.
- Alineado con `SYSTEM.md §2.1` y el principio de autonomy_level 1 del framework.

---

## 📤 Salida Esperada

- Bloque de pausa estructurado (Markdown) presentado al humano
- Registro de decisión (YAML) añadido al artefacto principal tras la respuesta
- En caso de rechazo: informe de cierre con opciones para el humano

---

## 🔗 Dependencias

- `apb-orch-context-handoff-v1.0` — para transferir el contexto al agente receptor tras la aprobación
- `apb-orch-multi-agent-v1.0` — si el checkpoint implica coordinar múltiples agentes en pausa simultánea

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../../context/apb/standards/AI_MARKING_STANDARD.md):

- **Registro de decisión** (YAML):
  `# [IA-GEN] Generado por APB AI Framework (apb-orch-human-checkpoint-v1.0) — pendiente revisión humana`

> **Generado por IA:** Claude (Anthropic/Claude Code), sesión 2026-06-29.
> **Validado por humano:** _pendiente — completar nombre/rol del validador antes de pasar a `candidate`._
