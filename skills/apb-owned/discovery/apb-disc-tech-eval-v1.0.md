---
id: "apb-disc-tech-eval-v1.0"
name: "Evaluación Técnica de Alternativas Tecnológicas"
description: "Evalúa y compara alternativas tecnológicas para una decisión de arquitectura en APB. Genera una matriz de decisión con criterios ponderados, analiza el fit con el stack APB, los riesgos de adopción y el coste total de propiedad (TCO), y produce una recomendación razonada con los trade-offs explícitos."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "discovery"
autonomy_level: 1
created_date: "2026-06-29"
review_date: "2026-12-29"
---

# Evaluación Técnica de Alternativas Tecnológicas

## Propósito
Proporcionar una metodología estructurada para evaluar y comparar alternativas tecnológicas en decisiones de arquitectura APB (framework, base de datos, servicio cloud, herramienta de CI/CD, proveedor de IA...). Genera una matriz de decisión con criterios ponderados adaptados al contexto APB, analiza cada alternativa y produce una recomendación razonada con los trade-offs explícitos. El objetivo es que la decisión sea reproducible, documentada y revisable.

## Contexto de Uso
- Selección de una nueva tecnología para un proyecto: base de datos, framework, ORM, message broker.
- Evaluación de si actualizar la versión mayor de una dependencia crítica o migrar a una alternativa.
- Decisión de build vs. buy: ¿construir internamente o adoptar un SaaS?
- Justificación de una decisión técnica para el Comité de Arquitectura APB (ADR — Architecture Decision Record).
- Revisión de una decisión tecnológica tomada hace años: ¿sigue siendo válida?

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `decision_title` | Texto | Qué se está decidiendo (ej. "Selección de ORM para GISPEM v2") | ✅ |
| `alternatives` | Lista | Alternativas a evaluar (mínimo 2, máximo 5) | ✅ |
| `requirements` | Lista | Requisitos funcionales y no funcionales que debe cumplir la solución | ✅ |
| `context` | Texto | Contexto de la decisión: proyecto, stack actual, restricciones | ❌ |
| `weights` | JSON | Pesos de los criterios de evaluación (si el equipo tiene preferencias) | ❌ |

## Criterios de Evaluación APB por Defecto

| Criterio | Peso por defecto | Descripción |
|---|---|---|
| Compatibilidad con stack APB | 25% | ¿Encaja con .NET 8, Azure, Python, DevExtreme? |
| Madurez y estabilidad | 20% | Años en producción, adopción en industria, versiones LTS |
| Seguridad y cumplimiento | 20% | CVEs conocidos, certificaciones, conformidad ENS/RGPD |
| Coste total de propiedad | 15% | Licencia + mantenimiento + formación + coste de migración |
| Curva de aprendizaje | 10% | Tiempo para que el equipo APB sea productivo |
| Comunidad y soporte | 10% | Documentación, ecosistema, opciones de soporte comercial |

## Flujo de Trabajo

1. **Definir el problema y las restricciones** (no buscar la solución óptima global, sino la óptima para APB):
   - ¿Qué problema resuelve? ¿Por qué la solución actual no sirve?
   - Restricciones no negociables: presupuesto, timeline, skills del equipo, compatibilidad Azure.

2. **Definir los criterios y pesos** (usar los por defecto o adaptar):
   - Si hay criterios adicionales específicos del caso, añadirlos y ajustar pesos.
   - Los pesos deben sumar 100%.

3. **Evaluar cada alternativa** (escala 1-5 en cada criterio):
   - 1: No cumple en absoluto
   - 3: Cumple parcialmente con limitaciones
   - 5: Cumple plenamente

4. **Calcular puntuación ponderada**:
   ```
   Puntuación total = Σ (puntuación_criterio × peso_criterio)
   ```

5. **Análisis de riesgos por alternativa**:
   - ¿Qué riesgo representa adoptar esta tecnología para APB?
   - ¿Hay riesgo de lock-in? ¿Hay alternativa de salida?
   - ¿El equipo tiene skills o necesita formación?

6. **Recomendación razonada** con trade-offs explícitos:
   - No solo decir "A es mejor que B" — explicar en qué escenarios B podría ser mejor.
   - Indicar las condiciones bajo las que la recomendación podría cambiar.

7. **ADR (Architecture Decision Record)**:
   - Formato Y-Statements o MADR para documentar la decisión.

## Salida Esperada

```markdown
# Evaluación Técnica — [Decisión] — [Fecha]
> ⚠️ Borrador generado por IA (APB AI Framework - apb-disc-tech-eval-v1.0) — validar con el equipo técnico y presentar al Comité de Arquitectura APB.

## Contexto
[Por qué se toma esta decisión ahora]

## Alternativas Evaluadas
| Criterio | Peso | [Alternativa A] | [Alternativa B] | [Alternativa C] |
|---|---|---|---|---|
| Compatibilidad stack APB | 25% | 5 (1.25) | 4 (1.00) | 3 (0.75) |
| Madurez y estabilidad | 20% | | | |
| Seguridad y cumplimiento | 20% | | | |
| Coste TCO | 15% | | | |
| Curva de aprendizaje | 10% | | | |
| Comunidad y soporte | 10% | | | |
| **TOTAL** | 100% | | | |

## Análisis de Riesgos por Alternativa
[...]

## Recomendación
**[Alternativa X]** — justificación en 3-5 frases con trade-offs explícitos.

## Trade-offs de la decisión
- ✅ Ventaja principal de la alternativa elegida
- ⚠️ Principal riesgo o limitación
- ❌ Qué sacrificamos al no elegir [alternativa B]
```

## Criterios de Calidad
- [ ] Se evalúan al menos 2 alternativas reales (no "alternativa A vs. no hacer nada").
- [ ] Los pesos de los criterios suman 100%.
- [ ] La recomendación incluye los trade-offs explícitos (qué se gana y qué se sacrifica).
- [ ] Se documenta el contexto que hace válida la recomendación (si el contexto cambia, puede cambiar la recomendación).

## Dependencias
- `apb-gov-tech-radar-v1.0` — la evaluación puede resultar en una nueva entrada en el radar tecnológico
- `apb-gov-vendor-eval-v1.0` — si la tecnología viene de un proveedor, la evaluación del proveedor complementa la técnica

## Ejemplo de Uso

```
Evalúa las alternativas de base de datos para el nuevo módulo de analytics de APB.
Alternativas: Azure Synapse Analytics, PostgreSQL con extensiones analíticas, ClickHouse.
Requisitos: consultas analíticas sobre datos históricos de 5 años de escalas marítimas, integración con Azure, coste razonable.
```

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento B |

## ⚠️ Comportamiento ante inputs incompletos

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `decision_title` | Pregunta: "¿Qué decisión técnica estás tomando?" | Sí |
| `alternatives` | Pregunta: "¿Qué alternativas quieres comparar? (mínimo 2)" | Sí |
| `requirements` | Pregunta: "¿Qué requisitos debe cumplir la solución?" | Sí |
| `context` | Asume stack estándar APB (.NET, Azure, Python) e indica la asunción | No |
| `weights` | Usa los pesos por defecto APB e indica los valores usados | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** — callout inmediatamente tras el título H1:
  > ⚠️ Borrador generado por IA (APB AI Framework - apb-disc-tech-eval-v1.0) — validar con el equipo técnico y presentar al Comité de Arquitectura APB.
