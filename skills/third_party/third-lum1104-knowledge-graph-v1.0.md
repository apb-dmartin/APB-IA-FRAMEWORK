---
id: "third-lum1104-knowledge-graph-v1.0"
name: "Skill: Codebase Knowledge Graph (Understand-Anything)"
description: "Construcción de un grafo de conocimiento navegable de una base de código (archivos, funciones, clases, dependencias) para análisis de impacto y onboarding. Adaptado del repositorio público Lum1104/Understand-Anything."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 0
source_repo: "https://github.com/Lum1104/Understand-Anything"
source_license: "unverified — sin archivo LICENSE confirmado en el repo de origen; revisar antes de adopción en producción"
source_commit: "unverified"
verified_date: "2026-06-24"
created_date: "2026-06-24"
review_date: "2026-06-24"
---

# Skill: Codebase Knowledge Graph (Understand-Anything)

---

## Descripción
Adaptación de la skill de construcción de grafos de conocimiento del
repositorio público `Lum1104/Understand-Anything` (también distribuido bajo
`Egonex-AI/Understand-Anything`). Analiza un repositorio mediante un pipeline
multi-agente, extrayendo cada archivo, función, clase y dependencia, y genera
un grafo de conocimiento navegable que permite consultar relaciones, evaluar
el impacto de un cambio antes de aplicarlo, y generar guías de onboarding.

> ⚠️ **Atención específica — licencia no verificada.** A diferencia de otras
> skills de terceros del catálogo, no se ha podido confirmar la licencia del
> repositorio de origen (al menos una fuente externa indica ausencia de
> archivo `LICENSE`). **No usar en flujos de producción ni redistribuir hasta
> verificar formalmente los términos de licencia con acceso directo al
> repositorio.** Adicionalmente, existen señales externas mixtas sobre el
> origen exacto del tráfico/popularidad del repositorio (posible inflación de
> métricas reportada por fuentes de terceros); esto no afecta la validez
> técnica del patrón pero refuerza la necesidad de revisión de licencia antes
> de cualquier adopción real.

> **Nota de gobernanza:** este descriptor cubre un gap de catálogo
> identificado en la Sesión 7. Citado desde `apb-dev-impact-analysis-v1.0`
> antes de existir como componente formal.

## Capacidades
- Análisis estructural de codebase vía pipeline multi-agente
- Grafo de conocimiento de archivos, funciones, clases y dependencias
- Análisis de impacto de cambios antes de commitear (`diff` de impacto)
- Extracción de dominio de negocio (flujos, pasos) además de estructura técnica
- Actualización incremental del grafo (solo archivos modificados)

## Inputs
- `repository_path`: ruta o referencia al repositorio a analizar
- `change_scope`: cambios propuestos o en curso (para análisis de impacto)

## Outputs
- `knowledge_graph`: grafo de conocimiento del código (formato JSON)
- `impact_analysis`: componentes afectados por un cambio propuesto
- `onboarding_guide`: guía generada para nuevos miembros del equipo

## Restricciones
- **Licencia sin verificar** — ver advertencia superior; bloqueante para uso
  en producción hasta resolución
- Pipeline multi-agente con coste computacional no trivial en repositorios
  grandes; evaluar coste antes de habilitar actualización automática en cada
  commit
- No sustituye el `DOMAIN_REGISTRY.md` del framework como fuente de verdad de
  dominios de negocio APB; es una herramienta de apoyo al análisis, no de
  gobernanza

## Adaptaciones APB
- Relacionado con `apb-dev-impact-analysis-v1.0` para evaluación de alcance de
  cambios antes de implementar
- El grafo generado no debe contener datos sensibles ni secretos: aplicar la
  misma restricción que sobre cualquier artefacto versionado en Git

## Ejemplo de Uso
```
Invocar: third-lum1104-knowledge-graph-v1.0
Input: { repository_path: "apb-facturacion-escalas", change_scope: "PR-current" }
Output: Grafo de conocimiento + componentes afectados por el cambio propuesto
```

---
*Adaptado por APB AI Framework. Licencia de origen pendiente de verificación —
no redistribuir ni usar en producción hasta confirmarla.*
