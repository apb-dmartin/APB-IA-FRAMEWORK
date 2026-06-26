---
id: "third-nextlevel-ux-v1.0"
name: "Skill: UI/UX Pro Max (NextLevelBuilder)"
description: "Skill avanzada de diseño UX/UI con generación de prototipos descriptivos, análisis heurístico y recomendaciones de mejora de usabilidad."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
source_repo: "https://github.com/nextlevelbuilder/ui-ux-pro-max-skill"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Skill: UI/UX Pro Max (NextLevelBuilder)

---

## Descripción
Skill avanzada de diseño UX/UI con generación de prototipos descriptivos, análisis heurístico y recomendaciones de mejora de usabilidad.

## Capacidades
- Análisis heurístico de interfaces existentes
- Generación de prototipos descriptivos detallados
- Evaluación de usabilidad con métricas
- Recomendaciones de accesibilidad avanzada

## Inputs
- `existing_ui`: descripción o captura de UI existente
- `user_personas`: perfiles de usuario
- `business_goals`: objetivos de negocio

## Outputs
- `ux_analysis.md`
- `prototype_description.md`
- `usability_scorecard.md`

## Restricciones
- No genera código de implementación
- Requiere validación con usuarios reales
- Accesibilidad validada según EN 301 549

## Adaptaciones APB
- Integración con `apb-dev-devexpress-front-v1.0`
- Alineación con estándares de diseño APB
- Workflow `apb-wf-sdd-full-v1.0`

## Ejemplo de Uso
```
Invocar: third-nextlevel-ux-v1.0
Input: { existing_ui: "...", user_personas: [...], goals: [...] }
Output: ux_analysis.md con puntuaciones y recomendaciones
```

---
*Adaptado por APB AI Framework. Licencia MIT original respetada.*
