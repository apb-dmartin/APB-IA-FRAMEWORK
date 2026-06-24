---
id: "third-skills-sh-frontend-v1.0"
name: "Skill: Frontend Design (skills.sh)"
description: "Skill especializada en diseño de interfaces frontend modernas, accesibles y responsivas. Incluye generación de wireframes descriptivos, guías de estilo y recomendaciones de componentes."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
source_repo: "https://www.skills.sh/anthropics/skills/frontend-design"
source_license: "Propietaria (uso interno autorizado)"
source_commit: "unverified"
verified_date: "2026-06-23"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Skill: Frontend Design (skills.sh)

---

## Descripción
Skill especializada en diseño de interfaces frontend modernas, accesibles y responsivas. Incluye generación de wireframes descriptivos, guías de estilo y recomendaciones de componentes.

## Capacidades
- Diseño de wireframes textuales detallados
- Recomendación de sistemas de diseño (Material, Fluent, etc.)
- Validación de accesibilidad WCAG 2.1 AA
- Generación de especificaciones de componentes UI

## Inputs
- `user_stories`: historias de usuario
- `brand_guidelines`: guía de marca (opcional)
- `tech_stack`: stack tecnológico objetivo

## Outputs
- `ui_specification.md`
- `component_catalog.md`
- `accessibility_checklist.md`

## Restricciones
- Licencia propietaria: uso restringido a entorno APB
- No genera código ejecutable directamente
- Requiere aprobación de UX/UI humano

## Adaptaciones APB
- Mapeo a componentes DevExpress corporativos
- Integración con `apb-dev-devexpress-front-v1.0`
- Alineación con estándares de diseño APB

## Ejemplo de Uso
```
Invocar: third-skills-sh-frontend-v1.0
Input: { user_stories: [...], tech_stack: "DevExtreme JS" }
Output: ui_specification.md con componentes DevExpress mapeados
```

---
*Adaptado por APB AI Framework. Uso bajo licencia propietaria skills.sh.*
