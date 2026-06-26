---
id: "apb-ops-telemetry-emit-v1.0"
name: "Telemetría de Invocación de Componentes"
description: "Define la convención de emisión de telemetría para todos los componentes del framework. Cada agente o skill que la invoca incluye un bloque TELEMETRY_BLOCK en su output; el runtime (Claude Code) o el script emit_telemetry.py lo envían automáticamente a Azure Monitor vía prov-azure-monitor-v1.0."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "operation"
autonomy_level: 2
inputs:
  - component_id
  - component_type
  - outcome
  - human_approved
outputs:
  - telemetry_block_json
  - emit_command
consumed_by:
  - apb-agent-observability-v1.0
depends_on:
  - prov-azure-monitor-v1.0
created_date: "2026-06-25"
review_date: "2026-06-25"
---

# Telemetría de Invocación de Componentes

## Propósito

Skill transversal que estandariza cómo cualquier componente del framework (agente, skill, subagente, workflow) registra su invocación en Azure Monitor. El objetivo es producir los datos que alimentan los KPIs de `proyecto.md` §6 y los dashboards de `apb-agent-observability-v1.0`.

**Runtime-agnóstica por diseño:** la skill produce siempre el bloque de datos; el mecanismo de envío varía según el contexto de ejecución (ver sección "Mecanismos de Envío").

## Cuándo Usar Esta Skill

Al final de cada invocación de un agente, skill o workflow, **antes** de presentar el output final al usuario. No se emite telemetría si la invocación fue interrumpida antes de producir cualquier resultado.

## Entradas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `component_id` | string | ID exacto del componente invocado (ej. `apb-agent-tech-debt-v1.0`) | ✅ |
| `component_type` | enum | `skill`, `agent`, `subagent`, `workflow` | ✅ |
| `component_domain` | string | Dominio del componente (ej. `operation`) | ✅ |
| `outcome` | enum | `success`, `human_override`, `cancelled`, `error` | ✅ |
| `human_approved` | boolean | ¿El output pasó revisión humana explícita antes de aplicarse? | ✅ |
| `runtime` | enum | `claude-code`, `copilot`, `unknown` | ✅ |
| `user_profile` | enum | `developer`, `functional`, `admin` | ✅ |
| `duration_seconds` | int | Tiempo aproximado de la invocación en segundos | ❌ |
| `artifact_type` | string | Tipo de artefacto generado (ej. `dashboard-spec`, `word-doc`, `code-pr`) | ❌ |
| `notes` | string | Contexto adicional libre | ❌ |

## Salida: TELEMETRY_BLOCK

Al final del output del componente, incluir el siguiente bloque en texto plano (no en código de markdown oculto):

```
---
📊 TELEMETRY_BLOCK
{
  "TimeGenerated": "<ISO-8601-timestamp>",
  "component_id": "<component_id>",
  "component_type": "<component_type>",
  "component_domain": "<component_domain>",
  "invocation_id": "<uuid-v4-generado>",
  "runtime": "<runtime>",
  "user_profile": "<user_profile>",
  "outcome": "<outcome>",
  "human_approved": <true|false>,
  "duration_seconds": <int-o-null>,
  "artifact_type": "<tipo-o-null>",
  "notes": "<texto-o-null>"
}
Para enviar: python3 scripts/emit_telemetry.py --stdin
---
```

## Mecanismos de Envío

### Mecanismo 1 — Automático (Claude Code)

Claude Code puede ejecutar el script directamente tras producir el bloque:

```bash
echo '<json-del-bloque>' | python3 scripts/emit_telemetry.py --stdin
```

El agente incluye esta instrucción en su output y Claude Code la ejecuta como parte de la sesión. No requiere acción del usuario.

### Mecanismo 2 — Script manual (desarrolladores)

Si el desarrollador prefiere enviarlo manualmente o si el envío automático falla:

```bash
python3 scripts/emit_telemetry.py --event '{"component_id": "...", ...}'
# o bien
python3 scripts/emit_telemetry.py --file telemetry/events.jsonl
```

### Mecanismo 3 — GitHub Actions (fallback scheduled)

El workflow `.github/workflows/telemetry.yml` reintenta nightly cualquier evento en `telemetry/events.jsonl` marcado como `sent: false`. Aplica a flujos que commitean artefactos al repositorio.

### Cobertura Pendiente ⚠️

> **PENDIENTE (registrado en `discovery/PLAN_FASES_FUTURAS.md` punto #46):**
> Los usuarios funcionales que solo interactúan por chat y nunca hacen commit no están cubiertos por ninguno de los tres mecanismos anteriores. La cobertura automática para este perfil requiere instrumentar la plataforma de chat (Claude.ai, Copilot chat), que está fuera del alcance del framework. Solución futura: proxy/wrapper de invocación o integración con Azure API Management.

## Convención para Nuevos Componentes

Todo componente nuevo creado en el framework **debe** referenciar esta skill en su frontmatter (`depends_on`) y producir el TELEMETRY_BLOCK al final de su output. Regla recogida en `GOVERNANCE.md` §3.1.

Los ~226 componentes existentes antes de la Sesión 17 recibirán esta referencia retroactivamente en la Fase #43 (última fase del plan, tras el cierre de todas las sesiones de construcción).

## Criterios de Calidad

- [ ] El `invocation_id` es un UUID v4 único por invocación (nunca reutilizar).
- [ ] El `TimeGenerated` es el timestamp del momento de emisión, no de inicio de la invocación.
- [ ] El campo `human_approved` refleja si hubo checkpoint humano real, no una aprobación implícita.
- [ ] El bloque TELEMETRY_BLOCK es texto plano visible en el output, no un comentario oculto.
- [ ] Si el envío a Azure Monitor falla, el evento se escribe en `telemetry/events.jsonl` para reintento.

## Ejemplo de Output

```
[... output principal del componente ...]

---
📊 TELEMETRY_BLOCK
{
  "TimeGenerated": "2026-06-25T10:30:00Z",
  "component_id": "apb-agent-observability-v1.0",
  "component_type": "agent",
  "component_domain": "operation",
  "invocation_id": "a3f9c2d1-7b4e-4f8a-9c0d-e1f2a3b4c5d6",
  "runtime": "claude-code",
  "user_profile": "developer",
  "outcome": "success",
  "human_approved": false,
  "duration_seconds": 185,
  "artifact_type": "dashboard-spec",
  "notes": null
}
Para enviar: python3 scripts/emit_telemetry.py --stdin
---
```

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-25 | Arquitectura APB / Claude Code | Creación inicial — Sesión 17 |

---

> **Generado por IA:** Claude (Anthropic/Claude Code), Sesión 17 — Observabilidad, 2026-06-25.
> **Validado por humano:** _pendiente — completar nombre/rol del validador antes de pasar a `candidate`._


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Codigo generado** - primera linea del bloque: `// [IA-GEN] Generado por APB AI Framework (apb-ops-telemetry-emit-v1.0) - pendiente revision humana`
- **Commit** - prefijo `[ai-gen]` en el mensaje + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`
- **PR asociado** - label `ai-generated` en GitHub + footer en descripcion del PR
