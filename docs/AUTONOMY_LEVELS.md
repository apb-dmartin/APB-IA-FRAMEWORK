# Niveles de Autonomía en el APB AI Framework

> **Audiencia:** Arquitectura APB, equipos que diseñan o usan agentes  
> **Última actualización:** 2026-06-26

---

## Definición

El `autonomy_level` es un campo obligatorio en todos los componentes del framework (agents, skills, subagents, workflows). Define cuánto puede actuar el componente sin intervención humana explícita. El nivel no es una característica del modelo IA — es una decisión de gobernanza que establece en qué puntos el técnico APB debe aprobar, confirmar o supervisar.

---

## Escala de autonomía APB (0–4)

### Nivel 0 — Informativo

El componente solo genera información. No propone ni ejecuta ninguna acción.

**Comportamiento:**
- Analiza, resume, responde preguntas
- No emite recomendaciones de acción
- No genera tickets, runbooks ni código ejecutable

**Uso APB:** Consultas de catálogo, búsquedas en base de conocimiento, dashboards de estado.

**Ejemplo:** Un componente que responde "¿Qué agentes tengo disponibles?" listando el catálogo.

---

### Nivel 1 — Propone, espera confirmación

El componente propone una acción concreta pero no la ejecuta hasta recibir aprobación explícita del técnico para **cada acción individual**.

**Comportamiento:**
- Genera propuesta detallada (runbook, ticket, configuración)
- Se detiene y espera: "¿Confirmas esta acción?"
- No continúa hasta recibir "sí" explícito

**Uso APB:** Escalados de incidencia, cambios de configuración, acciones sobre sistemas de producción, decisiones de arquitectura.

**Ejemplo:** `apb-ops-incident-escalate-v1.0` propone el escalado pero el técnico L1 debe confirmar antes de ejecutarlo.

**Agentes APB en nivel 1:** business-analyst, code-reviewer, security-architect, compliance-audit, risk-exception, governance, release-manager, catalog-manager.

---

### Nivel 2 — Ejecuta bajo riesgo, para en gates

El componente ejecuta autónomamente las acciones de riesgo Bajo. Se detiene en los gates declarados en `human_review_points` para acciones de riesgo Medio o Alto.

**Comportamiento:**
- Ejecuta el flujo nominal sin pedir confirmación en cada paso
- En gates de riesgo Medio: muestra el plan y espera aprobación antes de continuar
- En acciones de riesgo Alto: siempre requiere confirmación explícita
- Registra todas las acciones tomadas

**Uso APB:** La mayoría de agentes de desarrollo, arquitectura, QA y operación en contexto no-producción.

**Ejemplo:** `apb-agent-incident-support-v1.0` hace el triaje y diagnóstico autónomamente, pero para antes de ejecutar cualquier paso del runbook (gate humano obligatorio).

**Agentes APB en nivel 2:** spec-engineer, technical-architect, cloud-architect, domain-architect, ddd, implementer, qa-auto, documentation, platform-engineer, observability, sre, incident-support, tech-discovery, tech-debt, modernization, ux-mockup, finops, meta-builder.

---

### Nivel 3 — Alta autonomía, gates solo en críticos

El componente actúa de forma autónoma en casi todo su dominio. Solo se detiene ante acciones con consecuencias irreversibles o impacto en producción.

**Comportamiento:**
- Ejecuta el flujo completo incluyendo acciones de riesgo Medio
- Gate solo para: acciones irreversibles, cambios en producción, escalados P1
- Documenta todas las decisiones tomadas

**Uso APB:** Componentes de automatización avanzada en entornos controlados (pre-producción, pipelines CI/CD con guardarraíles técnicos).

**Nota:** En APB, el nivel 3 se reserva para casos muy específicos con runbooks completamente definidos y reversibles.

---

### Nivel 4 — Totalmente autónomo

El componente actúa sin intervención humana en ningún punto.

**Uso APB:** **No utilizado.** El APB AI Framework no despliega componentes de nivel 4. El riesgo operacional y de cumplimiento de Port de Barcelona requiere siempre supervisión humana en el ciclo de vida del software.

---

## Matriz de riesgo × autonomía

| Riesgo de la acción | Nivel 0 | Nivel 1 | Nivel 2 | Nivel 3 |
|--------------------|---------|---------|---------|---------|
| **Bajo** (lectura, análisis) | ✅ Autónomo | ✅ Autónomo | ✅ Autónomo | ✅ Autónomo |
| **Medio** (propuesta, pre-prod) | ❌ No aplica | ⏸ Confirma | ⏸ Gate | ✅ Autónomo |
| **Alto** (producción, irreversible) | ❌ No aplica | ⏸ Confirma | ⏸ Gate obligatorio | ⏸ Gate obligatorio |
| **Crítico** (P1, datos, seguridad) | ❌ No aplica | ⏸ Confirma | ⏸ Gate obligatorio | ⏸ Gate obligatorio |

> ✅ Autónomo = ejecuta sin preguntar  
> ⏸ Gate = se detiene y espera aprobación humana explícita  
> ❌ No aplica = el componente no genera este tipo de acciones

---

## Orquestación real entre agentes

El framework APB declara las relaciones entre agentes en el frontmatter (campos `skills`, `subagents`, `workflows`). La orquestación efectiva funciona así:

### Orquestación directa (agente → skill)

Un agente invoca una skill dentro de su contexto. El nivel de autonomía del agente determina si la skill se ejecuta automáticamente o con gate.

```
apb-agent-incident-support (nivel 2)
  → apb-ops-incident-triage-v1.0  (ejecución automática — riesgo Bajo)
  → apb-ops-incident-diagnose-v1.0 (ejecución automática — riesgo Bajo)
  → apb-ops-incident-escalate-v1.0 (gate obligatorio — riesgo Medio/Alto)
```

### Delegación a subagente (agente → subagente)

Cuando el diagnóstico requiere especialización, el agente delega al subagente correspondiente. El subagente opera con su propio nivel de autonomía dentro del scope delegado.

```
apb-agent-incident-support
  → detecta componente Oracle
  → delega en apb-sub-ops-oracle-v1.0
  → subagente genera runbook Oracle específico
  → control vuelve al agente principal para el gate humano
```

### Orquestación por workflow (agente → workflow → agentes)

Los workflows coordinan múltiples agentes con gates entre fases.

```
apb-wf-incident-l1-v1.0
  Paso 1: apb-ops-incident-triage-v1.0
  Paso 2: apb-ops-incident-diagnose-v1.0 (+ subagente especializado)
  Paso 3: ⚠️ GATE HUMANO — obligatorio
  Paso 4: apb-ops-incident-escalate-v1.0 O resolución L1
  ...
```

---

## Cómo elegir el nivel de autonomía al diseñar un nuevo componente

1. **¿El componente puede causar cambios en producción?** → Máximo nivel 2, con gate obligatorio antes de cualquier acción en producción.
2. **¿Las acciones son reversibles?** → Si no lo son, el gate es obligatorio independientemente del nivel.
3. **¿El dominio tiene regulación (LCSP, RGPD, seguridad)?** → Nivel 1 para todas las acciones que generen compromisos.
4. **¿Es un flujo de información o análisis puro?** → Nivel 2 es suficiente.
5. **¿Es el primer componente de un nuevo dominio?** → Empezar en nivel 1 hasta validar el comportamiento en producción.

---

*Documento generado por el APB AI Framework — Sesión 13. Requiere revisión humana antes de distribución.*
