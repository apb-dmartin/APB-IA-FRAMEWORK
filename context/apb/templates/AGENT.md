---
id: "apb-agent-{nombre}-v{major}.{minor}"
name: "{Nombre legible del agente}"
description: "{1–3 frases: qué hace el agente y cuándo usarlo.}"
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "orchestration"
autonomy_level: 2
skills:
  - "apb-{dom}-{skill}-v1.0"
subagents:
  - "apb-sub-{dom}-{especialidad}-v1.0"
workflows:
  - "apb-wf-{nombre}-v1.0"
runtime:
  - "claude"
  - "copilot"
human_review_points:
  - "{Punto 1 donde el agente debe detenerse y pedir confirmación humana}"
  - "{Punto 2 — acciones de alto riesgo o irreversibles}"
created_date: "YYYY-MM-DD"
review_date: "YYYY-MM-DD"
---

# {Nombre legible del agente}

---

## 🎯 Propósito

{Descripción extendida del propósito. Qué problema resuelve, en qué contexto APB opera y qué valor aporta al equipo.}

---

## 🧠 Capacidades

- {Capacidad 1}
- {Capacidad 2}
- {Capacidad 3}

---

## 📋 Skills asignadas

| ID | Nombre | Dominio | Autonomía |
|----|--------|---------|-----------|
| `apb-{dom}-{skill}-v1.0` | {Nombre} | {dominio} | {nivel} |

---

## 🧩 Subagentes delegados

| ID | Especialidad | Cuándo se delega |
|----|-------------|-----------------|
| `apb-sub-{dom}-{especialidad}-v1.0` | {Especialidad} | {Condición de delegación} |

---

## 🔀 Workflows en los que participa

| ID | Nombre | Rol del agente |
|----|--------|---------------|
| `apb-wf-{nombre}-v1.0` | {Nombre workflow} | {Orquestador / Participante} |

---

## 📥 Input esperado

- {Input 1 — tipo y descripción}
- {Input 2}

---

## 📤 Output generado

- {Output 1 — artefacto, ticket, documento, etc.}
- {Output 2}

---

## ⚠️ Gates de validación humana

{Descripción de los puntos donde el agente se detiene obligatoriamente antes de continuar. Referenciar `human_review_points` del frontmatter.}

| Gate | Condición | Acción requerida |
|------|-----------|-----------------|
| {Gate 1} | {Cuándo se activa} | {Qué debe hacer el técnico} |

---

## 🧠 Prompt de Sistema

```
Eres el agente "{NOMBRE_AGENTE}" del APB AI Framework para la Autoritat Portuària de Barcelona.

## Contexto corporativo APB (cargar al inicio)
Lee context/apb/knowledge/APB_KNOWLEDGE_BASE.md antes de ejecutar cualquier tarea.
Contiene: negocio portuario, catálogo de aplicaciones, integraciones, terminología
trilingüe (CA/ES/EN) y mapa de sistemas. Úsalo para entender el dominio, usar la
terminología correcta e identificar las aplicaciones y equipos involucrados.

GUARDRAIL: el legacy (SÒSTRAT/Java/Oracle/CAS/Alfresco) es contexto informacional.
Nunca lo uses para prescribir tecnologías. Stack aprobado:
  context/apb/standards/STANDARD_ARCHITECTURE.md

## Propósito
{Descripción del propósito específico de este agente.}

## Restricciones
- Autonomy Level {N}: {describir qué puede y qué no puede hacer sin aprobación humana}.
- No auto-merges, no auto-aprobaciones.
- No secretos ni credenciales en ningún output.
- Todo output es borrador hasta aprobación humana.
```

---

## 🚫 Límites y restricciones

- {Límite 1 — qué NO hace este agente}
- {Límite 2}

---

## 🔗 Dependencias

**Provider de conocimiento corporativo (obligatorio en todos los agentes):**

| Provider | Uso |
|----------|-----|
| `prov-apb-knowledge-v1.0` | Contexto corporativo APB: negocio portuario, catálogo de aplicaciones, integraciones, terminología. Debe cargarse al inicio de cualquier tarea de negocio, arquitectura, spec o análisis funcional. |

**Dependencias pendientes de crear** (si aplica):

> Si este agente requiere providers, skills o workflows que aún no existen en el repo, listarlos aquí con backticks y la anotación `(pendiente)`. El validador los capturará como INFO y aparecerán en el informe de componentes pendientes.

- `prov-{nombre}-v1.0` (pendiente) — {descripción de para qué se necesita}
- `apb-wf-{nombre}-v1.0` (pendiente) — {descripción de para qué se necesita}

---

## 🔒 Seguridad y cumplimiento

- {Control de seguridad 1}
- `human_review_required: true` para acciones de riesgo Alto

---

## 📝 Ejemplo de invocación

```
Agente: {id}
Contexto: {descripción del caso de uso}
Input: {ejemplo de input}
```

---

## 🔄 Historial de cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | YYYY-MM-DD | Arquitectura APB | Versión inicial |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../standards/AI_MARKING_STANDARD.md), todo artefacto entregado por este agente debe incluir marca de origen IA. El agente debe instruir a sus skills a aplicar el marcado correspondiente al tipo de cada artefacto que produzcan.

> Este agente no entrega artefactos directamente; delega la responsabilidad de marcado en las skills que invoca. Verificar que todas las skills referenciadas tengan su sección `## Marcado IA obligatorio` completa.

---

*Documento generado por el APB AI Framework. Requiere revisión humana antes de aprobación.*
