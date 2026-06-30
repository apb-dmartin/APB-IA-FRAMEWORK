---
id: "apb-disc-poc-guide-v1.0"
name: "Guía Estructurada de PoC (Prueba de Concepto)"
description: "Diseña una Prueba de Concepto (PoC) estructurada para validar una tecnología, arquitectura o enfoque en APB. Define el scope, los criterios de éxito, el plan de trabajo, los riesgos y el proceso de go/no-go con criterios cuantificados. Evita PoCs que se convierten en proyectos sin fin o que validan lo que ya se quería validar."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "discovery"
autonomy_level: 1
created_date: "2026-06-29"
review_date: "2026-12-29"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# Guía Estructurada de PoC (Prueba de Concepto)


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Propósito
Estructurar el diseño y ejecución de Pruebas de Concepto (PoC) en APB de forma que sean una herramienta de aprendizaje real y no una demostración de lo que ya se quería hacer. Define el scope mínimo para validar las hipótesis críticas, los criterios de éxito cuantificados (go/no-go), el plan de trabajo acotado en tiempo, y el proceso de decisión. Una buena PoC responde preguntas concretas en el tiempo mínimo necesario.

## Contexto de Uso
- Evaluación de una nueva tecnología o arquitectura antes de comprometerse con ella.
- Validación de un enfoque de integración entre dos sistemas APB.
- Demostración a dirección de la viabilidad técnica de un proyecto antes de su aprobación.
- Test de rendimiento de una solución bajo carga realista APB antes de adoptarla.
- Validación de una hipótesis de negocio que requiere un prototipo técnico.

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `poc_goal` | Texto | Objetivo de la PoC: qué hipótesis se quiere validar | ✅ |
| `technology_or_approach` | Texto | Tecnología, arquitectura o enfoque que se va a probar | ✅ |
| `time_budget_days` | Número | Días de trabajo disponibles para la PoC | ✅ |
| `success_criteria` | Lista | Criterios de éxito cuantificados (go criteria) | ❌ |
| `team_size` | Número | Número de personas disponibles para la PoC | ❌ |
| `constraints` | Lista | Restricciones: presupuesto, infraestructura disponible, accesos | ❌ |

## Principios de una PoC Efectiva APB

1. **Tiempo acotado**: máximo 4 semanas. Si necesita más, no es una PoC, es un piloto.
2. **Hipótesis explícita**: "Creemos que X puede hacer Y con rendimiento Z. La PoC lo confirma o refuta."
3. **Criterios de éxito antes de empezar**: si se definen después, se manipulan para validar lo que ya se quería.
4. **Scope mínimo**: solo lo necesario para validar la hipótesis crítica. No se busca el producto final.
5. **Código desechable**: el código de una PoC no va a producción. Si la PoC es un go, se rediseña.
6. **Decisión formal de go/no-go**: con participación de los responsables técnicos y de negocio.

## Estructura de la PoC

### Fase 1 — Diseño (día 1-2)
- [ ] Definir la hipótesis central con precisión.
- [ ] Definir los criterios de éxito (go) y fracaso (no-go) cuantificados.
- [ ] Diseñar el scope mínimo: qué hay que construir para validar la hipótesis.
- [ ] Identificar los riesgos principales de la PoC.
- [ ] Definir el plan de trabajo por días.

### Fase 2 — Ejecución (días 3-N)
- [ ] Construir el mínimo necesario para la validación.
- [ ] Documentar hallazgos y problemas encontrados durante la ejecución.
- [ ] No añadir funcionalidad no planificada — si aparece algo relevante, anotarlo para después.
- [ ] Checkpoint intermedio (a mitad del tiempo): ¿vamos bien? ¿es necesario ajustar el scope?

### Fase 3 — Evaluación y decisión (últimos 2 días)
- [ ] Medir los resultados contra los criterios de éxito.
- [ ] Documentar los hallazgos inesperados (tanto positivos como negativos).
- [ ] Reunión de go/no-go con los stakeholders relevantes.
- [ ] Documentar la decisión y los próximos pasos.

## Criterios de Éxito — Ejemplos APB

| Hipótesis | Criterio go | Criterio no-go |
|---|---|---|
| "Azure Container Apps puede reemplazar AKS para servicios pequeños" | Latencia p95 < 200ms bajo 50 RPS, coste < 30% del AKS actual | Latencia p95 > 500ms O coste similar al AKS |
| "LLM puede clasificar automáticamente documentación de escalas" | Precisión > 85% en dataset de prueba de 100 documentos | Precisión < 70% O tiempo de procesamiento > 5 seg/doc |
| "Pact contract testing puede reemplazar tests de integración de GISPEM" | Tests corren en < 2 min, detectan 100% de los breaking changes del dataset de prueba | Tests tardan > 5 min O falsan negativos en > 2% de casos |

## Salida Esperada

```markdown
# Plan de PoC — [Tecnología/Enfoque] — [Fecha]
> ⚠️ Borrador generado por IA (APB AI Framework - apb-disc-poc-guide-v1.0) — validar scope y criterios con el responsable técnico antes de empezar.

## Hipótesis a Validar
"Creemos que [tecnología/enfoque] puede [hacer algo concreto] con [rendimiento/calidad esperada]."

## Criterios de Éxito (go/no-go)
| Criterio | Valor go | Valor no-go | Cómo se mide |
|---|---|---|---|

## Scope de la PoC
**Incluye:**
- [Lo mínimo necesario para validar la hipótesis]

**Excluye explícitamente:**
- [Lo que no se va a construir en esta PoC]

## Plan de Trabajo
| Día | Actividad | Responsable | Entregable |
|---|---|---|---|

## Riesgos
| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|

## Decisión go/no-go
Fecha: [Fecha]
Participantes: [Lista]
```

## Criterios de Calidad
- [ ] La hipótesis está formulada de forma falsable (puede ser refutada por la evidencia).
- [ ] Los criterios de éxito están definidos antes de empezar la PoC.
- [ ] El scope excluye explícitamente qué NO se va a hacer.
- [ ] Hay un checkpoint intermedio planificado.
- [ ] La decisión go/no-go tiene participantes identificados y fecha fijada.

## Dependencias
- `apb-disc-tech-eval-v1.0` — la evaluación técnica puede desembocar en una PoC para el finalista
- `apb-gov-tech-radar-v1.0` — una PoC exitosa puede promover la tecnología al anillo "Probar" del radar

## Ejemplo de Uso

```
Diseña la PoC para evaluar si podemos usar Semantic Kernel (.NET) como framework de orquestación
de agentes IA en APB, en lugar de construir nuestra propia capa de orquestación.
Tiempo disponible: 10 días de trabajo.
Equipo: 1 arquitecto + 1 desarrollador.
```


## Prompt de Sistema

```
Eres el skill "Guía Estructurada de PoC (Prueba de Concepto)" (apb-disc-poc-guide-v1.0) del APB AI Framework,
operando para la Autoritat Portuària de Barcelona (APB).

## Contexto Corporativo APB
Carga context/apb/knowledge/APB_KNOWLEDGE_BASE.md (provider: prov-apb-knowledge-v1.0)
antes de ejecutar cualquier tarea.

Contiene: negocio portuario (escalas, atraques, movimientos, tasas, concesiones),
catálogo de aplicaciones (ARGOS, SÒSTRAT, APIs DOCKS), integraciones (PORTIC/EDI,
AGE, AIS, VTS Kongsberg), terminología trilingüe CA/ES/EN y mapa de equipos/Jira.

Úsalo para entender el dominio, usar terminología correcta e identificar sistemas
y equipos involucrados. El legacy (SÒSTRAT/Java/Oracle/CAS/Alfresco) es contexto
informacional — nunca prescribas tecnologías fuera del stack aprobado.
Stack aprobado: context/apb/standards/STANDARD_ARCHITECTURE.md

## Misión
Diseña una Prueba de Concepto (PoC) estructurada para validar una tecnología, arquitectura o enfoque en APB. Define el scope, los criterios de éxito, el plan de trabajo, los riesgos y el proceso de go/no-go con criterios cuantificados. Evita PoCs que se convierten en proyectos sin fin o que validan lo que ya se quería validar.

## Inputs Esperados
(no especificado)

## Instrucciones
(no especificado)

## Restricciones
- Stack DOCKS únicamente: .NET, Azure SQL, EntraID, Service Bus, Redis, APIM,
  SharePoint — aunque el sistema analizado use Java/Oracle/CAS/Alfresco.
- Sin secretos ni credenciales en ningún output.
- Autonomy Level 1: todo output es borrador — requiere aprobación humana.
- Trazabilidad: skill_id/agent_id + usuario + fecha en todo output.

## Formato de Salida
(no especificado)
```

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento B |

## ⚠️ Comportamiento ante inputs incompletos

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `poc_goal` | Pregunta: "¿Qué hipótesis quiere validar la PoC? ¿Qué pregunta debe responder?" | Sí |
| `technology_or_approach` | Pregunta: "¿Qué tecnología o enfoque se va a probar en la PoC?" | Sí |
| `time_budget_days` | Pregunta: "¿Cuántos días de trabajo hay disponibles para la PoC?" | Sí |
| `success_criteria` | Genera criterios de éxito razonables basados en el objetivo declarado; marca claramente que deben ser validados | No |
| `team_size` | Asume 1-2 personas e indica la asunción | No |
| `constraints` | Asume stack e infraestructura estándar APB | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** — callout inmediatamente tras el título H1:
  > ⚠️ Borrador generado por IA (APB AI Framework - apb-disc-poc-guide-v1.0) — validar scope y criterios con el responsable técnico antes de empezar.
