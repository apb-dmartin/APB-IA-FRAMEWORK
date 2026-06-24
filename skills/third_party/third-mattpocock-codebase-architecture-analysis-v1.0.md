---
id: "third-mattpocock-codebase-architecture-analysis-v1.0"
name: "Skill: Codebase Architecture Analysis (mattpocock/skills)"
description: "Escaneo de una base de código en busca de oportunidades de mejora arquitectónica, presentadas como informe visual, con sesión de profundización (grilling) sobre la oportunidad elegida. Adaptado del repositorio público mattpocock/skills."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 0
source_repo: "https://github.com/mattpocock/skills"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-24"
created_date: "2026-06-24"
review_date: "2026-06-24"
---

# Skill: Codebase Architecture Analysis (mattpocock/skills)

---

## Descripción
Adaptación de la skill `improve-codebase-architecture` del repositorio público
`mattpocock/skills` (MIT, Matt Pocock). Escanea una base de código en busca de
oportunidades de mejora estructural, las presenta como informe visual (HTML) y
permite profundizar mediante una sesión de grilling sobre la oportunidad
seleccionada antes de planificar el cambio.

> **Nota de gobernanza:** este descriptor cubre un gap de catálogo identificado
> en la Sesión 7. Citado desde `apb-dev-impact-analysis-v1.0` antes de existir
> como componente formal.

## Capacidades
- Escaneo estructural de una base de código existente
- Identificación de "puntos de profundización" (deepening opportunities):
  zonas con alto acoplamiento, complejidad o deuda técnica
- Informe visual navegable de hallazgos
- Sesión de grilling dirigida sobre el hallazgo elegido, antes de planificar
  la refactorización

## Inputs
- `repository_path`: ruta o referencia al repositorio a analizar
- `scope`: alcance del análisis (módulo, dominio, repositorio completo)

## Outputs
- `architecture_report`: informe visual HTML de hallazgos
- `prioritized_opportunities`: oportunidades de mejora priorizadas
- `refactor_focus`: oportunidad seleccionada para profundización tras grilling

## Restricciones
- Es una herramienta de **diagnóstico**, no de refactorización automática: no
  modifica código por sí misma
- El repositorio de origen asume convenciones de stack TypeScript/Node; en APB
  se usa como patrón de análisis aplicable a .NET, Django y DevExtreme, no como
  herramienta literal de análisis estático de TypeScript

## Adaptaciones APB
- Relacionado con `apb-dev-impact-analysis-v1.0` para evaluar si el cambio
  propuesto compensa el esfuerzo (Grill Before Code → Impact Analysis →
  Codebase Architecture Analysis)
- Los hallazgos relevantes para deuda técnica se enlazan con la política
  corporativa de cumplimiento Sonar (`apb-dev-sonar-clean-v1.0`)

## Ejemplo de Uso
```
Invocar: third-mattpocock-codebase-architecture-analysis-v1.0
Input: { repository_path: "apb-facturacion-escalas", scope: "full" }
Output: Informe visual de oportunidades de mejora arquitectónica priorizadas
```

---
*Adaptado por APB AI Framework. Licencia MIT original respetada.*
