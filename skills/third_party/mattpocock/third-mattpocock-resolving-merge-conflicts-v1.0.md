---
id: "third-mattpocock-resolving-merge-conflicts-v1.0"
name: "Skill: Resolving Merge Conflicts (mattpocock/skills)"
description: "Adaptación de la skill resolving-merge-conflicts del repositorio público mattpocock/skills (MIT): resolución guiada de conflictos de merge/rebase en Git preservando la intención de ambos cambios — examinar el estado, entender el porqué de cada lado vía commits/PRs, resolver cada sección conservando ambas intenciones cuando es posible, ejecutar verificaciones y finalizar."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 1
source_repo: "https://github.com/mattpocock/skills"
source_license: "MIT"
source_commit: "272f99b22574f50e4266791c86b9302682970e23"
created_date: "2026-07-04"
review_date: "2026-07-04"
---

# Skill: Resolving Merge Conflicts (mattpocock/skills)

---

## Descripción

Adaptación de la skill `skills/engineering/resolving-merge-conflicts/` del repositorio público
`mattpocock/skills` (MIT). Guía la resolución de un conflicto de merge/rebase **en curso**:

1. Examinar el estado actual del conflicto (`git status`, ficheros afectados).
2. Entender la **intención de cada lado** consultando commits y PRs de origen (no resolver a
   ciegas por el texto).
3. Resolver cada sección de conflicto **preservando ambas intenciones** cuando sea posible.
4. Ejecutar las verificaciones automatizadas del repo (tests/linters).
5. Finalizar con commit o continuación del rebase.

## Nota de gobernanza y encaje APB

- **Gap real:** el catálogo no tenía ninguna skill específica de resolución de conflictos Git;
  las skills de desarrollo cubren revisión/implementación, no la mecánica de merge.
- Complementa el flujo de `apb-dev-pr-doc-v1.0` y a `third-obra-superpowers-method-v1.0`
  (que cubre git-worktrees pero no la resolución de conflictos en sí).
- Aplicable en el paso de integración de `apb-wf-code-review-v1.0` si se decide en sesión futura.

## Human Review

| Fase | Responsable | Tipo de revisión |
|------|-------------|------------------|
| Post-resolución | Desarrollador responsable del merge | Validar que ninguna intención se ha perdido y que las pruebas pasan |

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-04 | Arquitectura APB | Incorporación (Sesión 19, punto #27) — candidata no duplicada del monorepo mattpocock |

---
*Registrado en APB AI Framework. Requiere revisión humana antes de aprobación.*
