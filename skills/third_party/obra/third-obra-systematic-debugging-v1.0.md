---
id: "third-obra-systematic-debugging-v1.0"
name: "Skill: Systematic Debugging (obra)"
description: "Adaptación de la skill standalone systematic-debugging de obra/superpowers (MIT): metodología disciplinada de 4 fases (investigación de causa raíz → análisis de patrones → hipótesis y prueba → implementación) que exige encontrar la causa raíz antes de proponer cualquier fix. Aplicable a bugs, fallos de test, comportamiento inesperado, problemas de rendimiento y de integración."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 1
source_repo: "https://github.com/obra/superpowers"
source_license: "MIT"
source_commit: "84620bd48380b1cac66b9b25180987116e2ce2fe"
created_date: "2026-07-04"
review_date: "2026-07-04"
---

# Skill: Systematic Debugging (obra)

---

## Descripción

Adaptación de la skill **standalone** `skills/systematic-debugging/` del repositorio público
`obra/superpowers` (MIT). Principio central: *"encuentra SIEMPRE la causa raíz antes de intentar
un fix; arreglar el síntoma es un fracaso"*. Las 4 fases:

1. **Investigación de causa raíz** — leer el error con atención, reproducir de forma
   consistente, revisar cambios recientes, recoger evidencia en las fronteras de componentes,
   trazar el flujo de datos hacia atrás.
2. **Análisis de patrones** — localizar ejemplos que sí funcionan, comparar contra
   referencias, identificar diferencias, entender dependencias.
3. **Hipótesis y prueba** — formular una hipótesis concreta, probar mínimamente con una sola
   variable cada vez, verificar el resultado antes de continuar.
4. **Implementación** — crear un test que falle, aplicar un único fix dirigido, verificar.

**Señal de alarma:** si se han intentado 3+ fixes y cada uno revela nuevos problemas, detenerse
— es un problema arquitectónico que requiere discusión, no más parches.

## Nota de gobernanza — relación con componentes existentes (no duplica)

- **`third-obra-superpowers-method-v1.0`** ya lista "systematic-debugging" como una de sus 9
  skills, pero a nivel de *método integrado* (brainstorm→plan→implement→…). Este descriptor
  aísla la skill de **depuración** para invocarla sola, sin arrastrar todo el método —
  cubriendo el caso de uso concreto que Débora pidió evaluar (Sesión 19, bloque #27). Ambos
  apuntan al mismo repo/commit; no hay contenido duplicado, sí distinto grano de uso.
- Complementa a las skills APB de desarrollo (`apb-dev-code-review-v1.0`,
  `apb-dev-autocorrect-v1.0`) aportando el rigor de causa-raíz previo al fix.

## Human Review

| Fase | Responsable | Tipo de revisión |
|------|-------------|------------------|
| Post-diagnóstico | Tech Lead | Validación de que el fix ataca la causa raíz, no el síntoma |

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-04 | Arquitectura APB | Incorporación (Sesión 19, punto #27) — skill standalone, distinta del method wrapper |

---
*Registrado en APB AI Framework. Requiere revisión humana antes de aprobación.*
