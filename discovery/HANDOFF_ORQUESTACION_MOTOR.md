---
title: "Handoff: Decisión del Motor de Orquestación (#77)"
date: "2026-07-06"
status: "draft"
owner: "Débora Martínez <deboramv@gmail.com>"
related_issue: "#77"
referenced_in: "PLAN_FASES_FUTURAS.md (línea 1509-1703), discovery/CONTINUIDAD_PROYECTO.md"
---

# Handoff: Motor de Orquestación de Agentes (#77)

## 📋 Contexto

El punto #77 del roadmap (`PLAN_FASES_FUTURAS.md`) define la **orquestación real entre agentes** como CRÍTICO. Dos incidentes de calidad documentados ocurrieron por su ausencia (Sesión DDD: dominios incompletos; Sesión QA TruckCenter: pasos de plan/Jira/vídeo omitidos — en ambos casos porque el humano ejecutó manualmente el `.md` del agente en lugar de un motor que fuerce sus pasos declarados).

Esta sesión (2026-07-06) construyó una **PoC de bajo riesgo** que demuestra viabilidad y ejecutabilidad de pausas sincrónicas de aprobación humana en GitHub Actions. El objetivo es informar la decisión definitiva sobre qué motor adoptar para la capa de orquestación macro (multiagente, persistente, distribuido).

---

## 🎯 PoC Entregada

**Archivos nuevos en este commit:**

| Fichero | Propósito |
|---------|-----------|
| `scripts/orchestrate_checkpoint_gate.py` | Genera bloques de pausa estructurados según `apb-orch-human-checkpoint-v1.0.md` |
| `.github/workflows/human-checkpoint-poc.yml` | Workflow que dispara pausas y las registra (GitHub Actions) |
| `scripts/setup_github_environment.py` | Configura Environment + revisores requeridos vía API (portabilidad repo) |
| Este fichero | Especificación de opciones y checklist para decisión |

**Qué demuestra:**

✅ Puntos de aprobación humana declarables en frontmatter (`human_checkpoints: [...]`)  
✅ Protocolo de pausa ejecutable (formato, opciones ✅/🔄/❌, YAML de decisión)  
✅ Sincronización con GitHub (workflow_dispatch + environment con required reviewers)  
✅ Registro de trazabilidad (checkpoint_log YAML, artifacts, timestamps)  
✅ Portabilidad entre repos (scripts parametrizables, no hardcoded)

**Limitaciones de esta PoC (por diseño — es PoC, no solución definitiva):**

- ⚠️ **Scope:** un workflow por vez, no orquestación multiagente simultánea
- ⚠️ **Estado:** pausas registradas en GitHub Artifacts (90 días), no persistencia de BD
- ⚠️ **Eventos:** registra checkpoints, no coreografía por eventos entre agentes
- ⚠️ **Reintentos:** manual (re-disparo del workflow), no backoff/timeout automático
- ⚠️ **Reanudación:** manual (aprobación en GitHub UI), no callback/webhook a backend

---

## 🏗️ Opciones de Motor Definitivo

El motor final debe resolver **coreografía real** entre agentes paralelos/secuenciales con estado distribuido. Tres opciones principales:

### Opción A: Azure Durable Functions

**Vía:** Funciones durables de Azure (serverless, stateful)

| Aspecto | Detalles |
|--------|---------|
| **Ejecuta** | Agentes como Cloud Functions (Python/C#) en Azure |
| **Estado** | Persistente en Azure Table Storage + Event Hub |
| **Pausas** | Nativas: `context.wait_for_input()` → pausa hasta callback/webhook |
| **Reintentos** | Configurables (exponencial, timeout) |
| **Coreografía** | Nativa: Durable Orchestration (C# vía Durable Task Framework) |
| **Integración APB** | Requiere migración de agentes a Cloud Functions; APIs vía APIM |
| **Coste estimado** | Alto (compute + storage) si está siempre activo |
| **Adoptabilidad** | **ALTA**: Plataforma ya usa Azure Stack DOCKS |

**Ejemplo:** Paso 1 (Business Analyst) → await Paso 2 (Spec Engineer) → await Paso 3 (Domain Architect) con checkpoints entre cada uno.

---

### Opción B: LangGraph (Antropic/LangChain)

**Vía:** Grafo de ejecución con estados (framework de orquestación local-first)

| Aspecto | Detalles |
|--------|---------|
| **Ejecuta** | Agentes como nodos en un grafo dirigido (Python puro) |
| **Estado** | En memoria o checkpoint en fichero/Redis (persistencia optional) |
| **Pausas** | Explícitas: `graph.invoke(..., pause_on=["checkpoint_1"])` |
| **Reintentos** | Nodos reutilizables, integración con agent toolkits |
| **Coreografía** | Declarativa: estados + transiciones; ramas condicionales |
| **Integración APB** | Agentes ya en Python/Claude → sin migración; wrapper de LangGraph |
| **Coste estimado** | Bajo (solo compute local/runner GitHub Actions) |
| **Adoptabilidad** | **MEDIA**: Nuevo marco, requiere refactor de orquestación; no serverless puro |

**Ejemplo:** Grafo `sdd_workflow.py` con nodos Business Analyst → Spec Engineer → Domain Architect, aristas condicionales si checkpoint rechaza.

---

### Opción C: Temporal.io (temporal-community/temporal-server)

**Vía:** Workflow engine distribuido (temporal server + workers)

| Aspecto | Detalles |
|--------|---------|
| **Ejecuta** | Agentes como actividades/workflows en Temporal (Python SDK) |
| **Estado** | Persistente en BD (Cassandra/MySQL) + Event Log |
| **Pausas** | Nativas: `workflow.sleep()`, `workflow.wait_for_signal()` |
| **Reintentos** | Avanzados: exponencial, deadletter, circuit breakers |
| **Coreografía** | Workflows declarativos + ramas condicionales + parallelismo |
| **Integración APB** | Requiere temporal-server (self-hosted o Temporal Cloud); workers independientes |
| **Coste estimado** | Medio-Alto (server + infraestructura) |
| **Adoptabilidad** | **BAJA**: Nueva infraestructura; no standard en APB; curva de aprendizaje |

**Ejemplo:** Workflow `SpecDrivenDevelopment` con activities (agentes) coordinadas; pausas en "DP6" gate (Release Manager).

---

## 📊 Matriz Comparativa

| Criterio | Durable Functions | LangGraph | Temporal.io |
|----------|------------------|-----------|------------|
| **Adoptabilidad APB** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **Coste infraestructura** | Alto | Bajo | Medio-Alto |
| **Curva aprendizaje** | Media (Azure) | Baja (Python) | Alta (Temporal) |
| **Persistencia estado** | ✅ Nativa | ⚠️ Manual | ✅ Nativa |
| **Pausas humanas** | ✅ via callbacks | ✅ explícitas | ✅ via signals |
| **Coreografía multiagente** | ✅ | ✅ | ✅✅ (avanzada) |
| **Escala distribuida** | ✅✅ | ⚠️ (local) | ✅✅✅ |
| **Integración actual APB** | ✅ (Azure Stack) | ❌ (no existe) | ❌ (no existe) |

---

## 📋 Contrato de Eventos (Requisito #3, completado en esta sesión)

Independientemente del motor, los agentes y workflows deben emitir eventos en **CloudEvents** para que terceros (CI/CD, métricas, auditoría) puedan subscribirse.

### Dominios de eventos

| Dominio | Ejemplos | Trigger |
|---------|----------|---------|
| `code.*` | `code.agent_output_generated`, `code.review_requested` | Agente completa fase |
| `ci.*` | `ci.workflow_run_completed`, `ci.test_passed` | Pipeline CI/CD |
| `pr.*` | `pr.created`, `pr.approved`, `pr.merged` | Evento de PR en GitHub |
| `bug.*` | `bug.found`, `bug.assigned`, `bug.closed` | Auditoría de hallazgos |
| `deployment.*` | `deployment.started`, `deployment.succeeded`, `deployment.rolled_back` | Release |

### Esquema base (CloudEvents v1.0)

```json
{
  "specversion": "1.0",
  "type": "code.agent_output_generated",
  "source": "https://portdebarcelona.cat/apb/agents/apb-agent-spec-engineer-v1.0",
  "id": "sdd-workflow-2026-07-06T10:30:15Z-001",
  "time": "2026-07-06T10:30:15Z",
  "datacontenttype": "application/json",
  "subject": "workflow/apb-wf-sdd-full-v1.0",
  "data": {
    "workflow_id": "apb-wf-sdd-full-v1.0",
    "agent_id": "apb-agent-spec-engineer-v1.0",
    "checkpoint_index": 2,
    "decision": "approved",
    "artifacts": [
      "system-spec.md",
      "backlog.md"
    ]
  }
}
```

---

## ✅ Checklist: Antes de Decidir

- [ ] **PoC verificada:** `workflow_dispatch` dispara pausa real en GitHub Environment (revisor aprueba/rechaza)
- [ ] **Migración repo personal → oficial:** `setup_github_environment.py --repo portdebarcelona/APB-IA-FRAMEWORK` funciona
- [ ] **Protocolo de checkpoint:** formato exacto de `apb-orch-human-checkpoint-v1.0.md` validado (✅/🔄/❌ opciones)
- [ ] **Registro de trazabilidad:** checkpoint_log YAML persiste en artifacts
- [ ] **Artefactos:** `scripts/orchestrate_checkpoint_gate.py`, `.github/workflows/human-checkpoint-poc.yml`, `setup_github_environment.py` commiteados y listos
- [ ] **Documentación:** este handoff + actualización de `PLAN_FASES_FUTURAS.md` (#77) + entrada en `discovery/CONTINUIDAD_PROYECTO.md`

---

## 🚀 Próximos Pasos

### Si se elige **Durable Functions** (recomendado para APB):

1. **Sesión Plataforma:** Presentar opciones; validar decisión
2. **Fase 1 (Plataforma):** Arquitectura de Durable Functions + contratos de eventos
3. **Fase 2 (Plataforma):** Implementar motor macro + registrador de eventos
4. **Fase 3 (Débora + Plataforma):** Integrar agentes APB-IA-FRAMEWORK con motor (binding)
5. **Fase 4 (Débora):** Validar workflows SDD completo (Sesión 24, 25, ...)

### Si se elige **LangGraph** (bajo coste, rápido):

1. **Sesión Débora:** Crear wrapper de LangGraph sobre agentes existentes
2. **Fase 1:** Refactor PoC → LangGraph grafo (stateful, con checkpoints)
3. **Fase 2:** Persistencia en Redis (optional) para resiliencia
4. **Fase 3:** Integrar con GitHub Actions o ejecutor local
5. **Limitación conocida:** escalabilidad distribuida requiere siguiente fase

### Si se elige **Temporal.io** (máximo control, máxima complejidad):

1. **Sesión Arquitectura:** Evaluación de coste-beneficio (¿merece la pena?)
2. **Fase 1:** Despliegue de temporal-server (auto-hosted o Temporal Cloud)
3. **Fase 2:** Refactor agentes → Temporal activities/workflows
4. **Fase 3:** Workers dedicados + escalado automático
5. **Riesgo:** complejidad operativa; requiere capacitación de equipo

---

## 📞 Decisión Requerida

**Para Débora + Equipo Plataforma:**

Confirma cuál de estas tres rutas tomar:

```
A) Azure Durable Functions ← RECOMENDADO: ya está en stack APB, alto soporte
B) LangGraph ← RÁPIDO: bajo coste, pero escalabilidad limitada inicialmente
C) Temporal.io ← FLEXIBLE: máximo control, pero nueva infraestructura
```

Una vez confirmado, pasamos a:
1. Fase de especificación (contratos, arquitectura)
2. Fase de prototipo (agentes de ejemplo integrados)
3. Fase de integración (workflows SDD completo)

---

## 📎 Apéndices

### A. Checklist de Migración repo personal → oficial APB

| Paso | Repo Personal | Repo Oficial | Automatizado |
|------|---------------|--------------|--------------|
| Clonar código | ✅ | ✅ | `git push` |
| Copiar workflows YAML | ✅ | ✅ | `git push` |
| Crear Environment | ⚠️ Manual UI | ⚠️ Manual UI | `setup_github_environment.py` |
| Añadir revisores | ⚠️ Manual UI | ⚠️ Manual UI | `setup_github_environment.py` |
| Crear secrets/tokens | ⚠️ Manual UI | ⚠️ Manual UI | Manual (sensible) |
| Disparar workflow PoC | ✅ | ✅ | GitHub UI / `gh` CLI |

**Comando único para configurar Environment en repo nuevo:**
```bash
python scripts/setup_github_environment.py \
  --repo portdebarcelona/APB-IA-FRAMEWORK \
  --environment human-checkpoint \
  --reviewers arquitectura-apb-team \
  --token $GITHUB_TOKEN
```

### B. Referencias Técnicas

- GitHub Environments: https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment
- CloudEvents v1.0: https://cloudevents.io/
- Azure Durable Functions: https://learn.microsoft.com/en-us/azure/azure-functions/durable/
- LangGraph: https://python.langchain.com/docs/langgraph
- Temporal.io: https://temporal.io/

---

**Documento generado por Claude Code (APB AI Framework), sesión 2026-07-06.**  
**Status: Draft — Pendiente de confirmación de Débora sobre opción de motor.**

