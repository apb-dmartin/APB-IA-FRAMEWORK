---
id: "apb-dev-autocorrect-v1.0"
name: "Auto-Refinamiento y Autocorrección"
description: "Implementa bucles de auto-refinamiento (Reflexion, Self-Refine) aplicables a código, documentación, diseño y análisis, e incluye un modo dirigido por fallos de test que detecta, diagnostica y propone o aplica correcciones automáticas con umbral de confianza."
version: "1.1.0"
status: "draft"
owner: "QA / Desarrollo APB <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 2
created_date: "2026-06-20"
review_date: "2026-06-22"
depends_on:
  - "apb-dev-implement-v1.0"
  - "apb-qa-test-auto-v1.0"
  - "apb-dev-sonar-clean-v1.0"
---

# Auto-Refinamiento y Autocorrección

> Las secciones 1–6 (reflexión general multi-dominio) incorporan, fusionadas
> y adaptadas, contenidos de la skill de terceros `NeoLabHQ/context-
> engineering-kit` (plugin `reflexion`) bajo licencia MIT. La sección 7
> (autocorrección dirigida por test) es contenido propio de APB. Ver
> sección 8, Procedencia.

## 1. Propósito y Alcance

Mejorar la calidad del output del agente en cualquier dominio (código,
documentación, análisis, diseño) mediante técnicas de reflexión iterativa,
y aplicar correcciones automáticas dirigidas cuando el fallo proviene de un
test (caso de uso operacional concreto y de mayor autonomía).

**Fundamento:** basado en los papers *Self-Refine* y *Reflexion*, que
documentan mejoras de 8–21% en calidad mediante bucles de feedback
iterativos.

## 2. Proceso General de Reflexión

1. **Triage de complejidad** — output simple (< 50 líneas): reflexión ligera
   (1–2 checks); medio (50–200 líneas): reflexión estándar (5–7 checks);
   complejo (> 200 líneas): reflexión profunda (10+ checks).
2. **Identificación** — revisar contra checklist de calidad: corrección,
   completitud, eficiencia, legibilidad, seguridad, tests, documentación,
   consistencia con el proyecto.
3. **Corrección** — priorizar por impacto; corregir issues obvios
   automáticamente; sugerir corrección con explicación para los no obvios;
   verificar que la corrección no introduce nuevos bugs.
4. **Verificación** — re-ejecutar tests si están disponibles, validar
   sintaxis/compilación, confirmar que el output final mejora al inicial.

## 3. Crítica Multi-Perspectiva

Evaluación desde múltiples ángulos especializados, cada uno con un score
0–100 y findings propios:

| Perspectiva | Foco |
|---|---|
| Bugs y edge cases | Input vacío, null pointer, race conditions |
| Seguridad | Inyección, XSS, secrets expuestos, auth bypass |
| Performance | Complejidad algorítmica, memory leaks, N+1, I/O bloqueante |
| Calidad de código | SRP, duplicación, nombres, complejidad ciclomática |
| Contratos y APIs | Consistencia, breaking changes, validación de inputs |
| Consistencia histórica | Patrones del proyecto, regresiones |
| Cobertura de tests | Tests faltantes, edge cases, mocks apropiados |

Proceso de debate: cada perspectiva evalúa independientemente; se comparan
hallazgos y se discuten discrepancias; se llega a consenso o se documenta el
desacuerdo con justificación; score final por promedio ponderado o mínimo
(configurable).

## 4. Checklists de Reflexión por Dominio

**Código:** especificación cumplida · edge cases cubiertos (vacío, null,
overflow, concurrencia) · bugs potenciales · complejidad ciclomática < 10 ·
duplicación extraíble · manejo de errores completo · vulnerabilidades de
seguridad · cobertura de tests (happy path, edge, error).

**Arquitectura:** responsabilidades claras (SRP) · dependencias hacia el
dominio (DIP) · sin acoplamiento circular · interfaces apropiadas (ISP) ·
aggregates con límites claros · sin leakage de infraestructura en el dominio.

**Documentación:** precisión y completitud · ausencia de ambigüedad ·
ejemplos correctos y ejecutables · estructura navegable · sin información
desactualizada o contradictoria.

## 5. Memorización de Insights

Curar lecciones aprendidas para uso futuro, con formato estructurado
(problema, causa raíz, solución, regla de prevención, referencias). Sirve
como base de conocimiento incremental que reduce la recurrencia de errores
ya diagnosticados.

## 6. Anti-patrones de Reflexión

Reflexión superficial (solo sintaxis, sin análisis semántico) · over-
engineering (optimizar sin evidencia de bottleneck) · ignorar constraints
del proyecto · perfeccionismo sin análisis costo-beneficio · generar
findings sin plan de acción · reflexión circular sin progreso (límite
recomendado: 3 iteraciones).

## 7. Modo Dirigido por Test (autocorrección operacional)

### 7.1 Propósito

Detectar fallos en tests automatizados, analizar la causa raíz y proponer o
aplicar correcciones automáticas en el código fuente, reduciendo el ciclo de
feedback entre fallo y corrección.

### 7.2 Trigger

Un test unitario, de integración o E2E falla en CI/CD o en ejecución local.

### 7.3 Input / Output

**Input:** output de ejecución de tests (stack trace, mensaje de error),
código fuente del test y del SUT, historial de cambios recientes (`git
diff`), logs de ejecución, configuración del entorno.

**Output:** diagnóstico de la causa del fallo, propuesta de corrección
(diff), aplicación automática si la confianza es > 90%, reporte de acciones,
alerta si la corrección requiere revisión humana.

### 7.4 Proceso

1. Parsear el stack trace e identificar el tipo de error.
2. Revisar `git diff` reciente para localizar el cambio causante.
3. Examinar SUT y test; identificar discrepancias entre implementación y
   expectativa.
4. Clasificar: error de implementación, error de test (mock desactualizado),
   error de entorno, o flaky test (documentar, no "arreglar" cambiando el test).
5. Generar la corrección propuesta; validar que el test corregido pasa y no
   rompe otros tests.
6. Documentar la corrección y el aprendizaje para evitar recurrencia.

### 7.5 Reglas y Constraints

- Nunca aplicar corrección automática en código de producción sin validación.
- Si la confianza de la corrección es < 90%, requerir revisión humana.
- No modificar tests para que pasen sin entender la causa: puede enmascarar
  bugs reales.
- Mantener registro de todas las autocorrecciones para auditoría.

## 8. Procedencia y Licencia

Las secciones 1–6 están adaptadas del plugin `reflexion` de
`NeoLabHQ/context-engineering-kit`, licencia MIT. Referencias adicionales:
*Self-Refine* (arXiv:2303.17651), *Reflexion* (arXiv:2303.11366),
*Constitutional AI* (Anthropic).

## 9. Dependencias

- `apb-dev-implement-v1.0`
- `apb-qa-test-auto-v1.0`
- `apb-dev-sonar-clean-v1.0`


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Codigo generado** - primera linea del bloque: `// [IA-GEN] Generado por APB AI Framework (apb-dev-autocorrect-v1.0) - pendiente revision humana`
- **Commit** - prefijo `[ai-gen]` en el mensaje + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`
- **PR asociado** - label `ai-generated` en GitHub + footer en descripcion del PR
