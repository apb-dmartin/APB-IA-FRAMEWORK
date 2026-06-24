---
id: "third-graphify-visual-v1.0"
name: "Skill: Visual Knowledge Graph (Graphify)"
description: "Generación de grafos de conocimiento visuales a partir de documentación, código y especificaciones. Visualización interactiva de relaciones entre componentes."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
source_repo: "https://graphify.net/"
source_license: "Propietaria (evaluación)"
source_commit: "unverified"
verified_date: "2026-06-23"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Skill: Visual Knowledge Graph (Graphify)

---

## Descripción
Generación de grafos de conocimiento visuales a partir de documentación, código y especificaciones. Visualización interactiva de relaciones entre componentes.

## Capacidades
- Extracción de entidades y relaciones desde texto
- Generación de grafos de conocimiento
- Visualización interactiva (HTML/SVG)
- Exportación a formatos estándar (GraphML, GEXF)

## Inputs
- `documents`: lista de documentos fuente
- `entity_types`: tipos de entidades a extraer
- `relation_types`: tipos de relaciones a extraer

## Outputs
- `knowledge_graph.html`
- `knowledge_graph.graphml`
- `entity_report.md`

## Restricciones
- Licencia propietaria en evaluación
- No autorizado para datos clasificados
- Uso limitado a proyectos piloto

## Adaptaciones APB
- Integración con `apb-disc-ddd-legacy-v1.0`
- Mapeo a dominios DDD identificados
- Workflow `apb-wf-legacy-onboarding-v1.0`

## Ejemplo de Uso
```
Invocar: third-graphify-visual-v1.0
Input: { documents: ["spec.md", "adr.md"], entity_types: ["Service", "Domain"] }
Output: knowledge_graph.html con dominios y servicios mapeados
```

---
*Adaptado por APB AI Framework. Uso bajo licencia propietaria Graphify (evaluación).*