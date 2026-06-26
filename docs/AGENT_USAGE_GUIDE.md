# Guía de uso de agentes APB AI Framework

> **Audiencia:** Equipos técnicos APB — analistas, desarrolladores, arquitectos, operaciones  
> **Última actualización:** 2026-06-26  
> **Versión del framework:** 259 componentes, 26 agentes

---

## ¿Qué es un agente APB?

Un agente APB es una unidad de IA especializada en un rol concreto del ciclo de vida del software (análisis, arquitectura, desarrollo, operaciones, etc.). Cada agente:

- Tiene un **conjunto fijo de skills** que puede invocar
- Opera con un **nivel de autonomía declarado** (0–4) que determina cuándo necesita aprobación humana
- Genera **artefactos concretos** (documentos, tickets Jira, código, runbooks)
- Está disponible en **Claude web, GitHub Copilot, Rovo (Atlassian) y M365 Copilot**

---

## Catálogo de agentes disponibles

| Agente | Rol | Dominio | Autonomía | Runtime |
|--------|-----|---------|-----------|---------|
| `apb-agent-business-analyst-v1.0` | Análisis funcional y descubrimiento de negocio | discovery | 1 | claude, copilot |
| `apb-agent-spec-engineer-v1.0` | Ingeniería de especificaciones (SDD, PRD, ADR) | development | 2 | claude, copilot |
| `apb-agent-technical-architect-v1.0` | Diseño de arquitectura técnica | architecture | 2 | claude, copilot |
| `apb-agent-cloud-architect-v1.0` | Arquitectura cloud Azure | architecture | 2 | claude, copilot |
| `apb-agent-domain-architect-v1.0` | Diseño DDD y bounded contexts | architecture | 2 | claude, copilot |
| `apb-agent-ddd-v1.0` | Domain-Driven Design end-to-end | architecture | 2 | claude, copilot |
| `apb-agent-implementer-v1.0` | Implementación de código guiada por spec | development | 2 | claude, copilot |
| `apb-agent-code-reviewer-v1.0` | Revisión de código y pull requests | development | 1 | claude, copilot |
| `apb-agent-qa-auto-v1.0` | QA automatizado y validación de pipelines | qa | 2 | claude, copilot |
| `apb-agent-documentation-v1.0` | Generación de documentación técnica | documentation | 2 | claude, copilot |
| `apb-agent-security-architect-v1.0` | Análisis y diseño de seguridad | security | 1 | claude, copilot |
| `apb-agent-compliance-audit-v1.0` | Auditoría de cumplimiento normativo | governance | 1 | claude, copilot |
| `apb-agent-risk-exception-v1.0` | Gestión de riesgos y excepciones | governance | 1 | claude, copilot |
| `apb-agent-governance-v1.0` | Gobernanza del framework APB | governance | 1 | claude, copilot |
| `apb-agent-platform-engineer-v1.0` | Ingeniería de plataforma y DevOps | platform | 2 | claude, copilot |
| `apb-agent-release-manager-v1.0` | Gestión de releases y despliegues | platform | 1 | claude, copilot |
| `apb-agent-observability-v1.0` | Observabilidad y monitorización | operation | 2 | claude, copilot |
| `apb-agent-sre-v1.0` | Site Reliability Engineering | operation | 2 | claude, copilot |
| `apb-agent-incident-support-v1.0` | Soporte a incidencias técnicas L1 | operation | 2 | claude, copilot |
| `apb-agent-tech-discovery-v1.0` | Descubrimiento técnico de sistemas existentes | discovery | 2 | claude, copilot |
| `apb-agent-tech-debt-v1.0` | Análisis y gestión de deuda técnica | development | 2 | claude, copilot |
| `apb-agent-modernization-v1.0` | Modernización de aplicaciones legacy | architecture | 2 | claude, copilot |
| `apb-agent-ux-mockup-v1.0` | Generación de mockups y diseño UX | design | 2 | claude |
| `apb-agent-finops-v1.0` | Optimización de costes cloud (FinOps) | platform | 2 | claude, copilot |
| `apb-agent-meta-builder-v1.0` | Construcción de componentes del propio framework | orchestration | 2 | claude |
| `apb-agent-catalog-manager-v1.0` | Gestión del catálogo de componentes APB | governance | 1 | claude |

---

## Cómo invocar un agente

### En Claude web (claude.ai)

```
Actúa como el agente APB [nombre del agente].
Contexto: [descripción de lo que necesitas]
[Pega aquí el input relevante: requisitos, logs, código, etc.]
```

**Ejemplo:**
```
Actúa como el agente APB apb-agent-business-analyst-v1.0.
Contexto: Necesito analizar el proceso de gestión de escales del Port.
Input: [descripción del proceso actual]
```

### En GitHub Copilot Chat

```
@copilot /apb [id-del-agente] [descripción del task]
```

### En Rovo (Atlassian) — disponible julio 2026

Desde el chat de Jira o Confluence, invocar directamente por nombre:
```
APB Business Analyst: analiza los requisitos del ticket PROJ-123
```

### En M365 Copilot

Desde Teams o Word, activar el plugin APB AI Framework y seleccionar el agente del menú.

---

## Flujo de trabajo típico por fase del proyecto

```
1. DISCOVERY
   └── apb-agent-business-analyst-v1.0
       └── apb-agent-tech-discovery-v1.0 (si hay sistema existente)

2. ARQUITECTURA
   └── apb-agent-technical-architect-v1.0
       ├── apb-agent-cloud-architect-v1.0 (componentes Azure)
       ├── apb-agent-domain-architect-v1.0 (DDD)
       └── apb-agent-security-architect-v1.0 (revisión de seguridad)

3. ESPECIFICACIÓN
   └── apb-agent-spec-engineer-v1.0
       └── apb-agent-documentation-v1.0 (documentación derivada)

4. IMPLEMENTACIÓN
   └── apb-agent-implementer-v1.0
       └── apb-agent-code-reviewer-v1.0 (gate antes de merge)

5. CALIDAD
   └── apb-agent-qa-auto-v1.0
       └── apb-agent-compliance-audit-v1.0 (antes de producción)

6. OPERACIÓN
   └── apb-agent-incident-support-v1.0
       ├── apb-agent-sre-v1.0
       └── apb-agent-observability-v1.0
```

---

## Niveles de autonomía — qué esperar

| Nivel | Comportamiento | Requiere aprobación |
|-------|---------------|---------------------|
| **0** | Solo informa, no propone acciones | No aplica |
| **1** | Propone, pero espera confirmación antes de cada acción | Sí — cada acción |
| **2** | Ejecuta acciones de bajo riesgo; para en gates de riesgo medio/alto | En gates declarados |
| **3** | Ejecuta la mayoría de acciones de forma autónoma | Solo acciones críticas |
| **4** | Totalmente autónomo dentro de su dominio | No (no usado en APB) |

> **APB no usa autonomía 4.** El nivel máximo en producción es 3, y solo para agentes de operación con runbooks muy acotados. La mayoría de agentes APB operan en nivel 1–2.

---

## Regla fundamental: `human_review_required`

Todos los agentes APB incluyen en su respuesta el campo `human_review_required`. Cuando es `true`:

- **No ejecutar** la acción propuesta sin revisión humana previa
- El agente habrá indicado el motivo (riesgo Alto, acción irreversible, impacto en producción)
- El técnico responsable debe aprobar explícitamente antes de continuar

---

## Preguntas frecuentes

**¿Puedo usar varios agentes a la vez?**  
Sí. Los workflows del framework orquestan múltiples agentes. También puedes encadenarlos manualmente pasando el output de uno como input del siguiente.

**¿El agente tiene acceso a mis sistemas?**  
No directamente. Los agentes proponen acciones, comandos y configuraciones. La ejecución siempre la realiza el técnico APB.

**¿Qué hago si el agente da una respuesta incorrecta?**  
Proporciona más contexto o corrige el input. Si el error es sistemático, abre un ticket en el repositorio APB-IA-FRAMEWORK para revisar la skill correspondiente.

**¿Cómo sé qué skills usa un agente?**  
Consulta el fichero del agente en `agents/apb-agent-{nombre}-v1.0.md` — el campo `skills` lista todas las skills que puede invocar.

---

*Guía generada por el APB AI Framework — Sesión 13. Requiere revisión humana antes de distribución.*
