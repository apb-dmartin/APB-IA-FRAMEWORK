---
id: "third-anthropic-document-skills-v1.0"
name: "Anthropic Document Skills (docx/pptx/xlsx/pdf)"
description: "Skills oficiales de Anthropic para creación y edición de documentos Word, PowerPoint, Excel y PDF, usadas internamente para la generación de documentos en Claude. Source-available, no open source."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "documentation"
autonomy_level: 1
source_repo: "https://github.com/anthropics/skills"
source_license: "Source-available (no open source) — ver THIRD_PARTY_NOTICES.md del repositorio de origen"
source_commit: "unverified"
verified_date: "2026-06-23"
created_date: "2026-06-23"
review_date: "2026-06-23"
---

# Anthropic Document Skills (docx/pptx/xlsx/pdf)

## 1. Propósito

Skills oficiales mantenidas por Anthropic para la creación, edición y
análisis de documentos en formatos ofimáticos: Word (`docx`), PowerPoint
(`pptx`), Excel (`xlsx`) y PDF (`pdf`). Son las mismas skills que dan
soporte a la generación de documentos en Claude.ai y Claude Code.

## 2. Alcance

- `docx` — creación, edición y extracción de texto en Word; soporta
  tracked changes, comentarios, preservación de formato.
- `pptx` — creación, edición y análisis de presentaciones PowerPoint;
  layouts, plantillas, gráficos, generación automática de diapositivas.
- `xlsx` — creación, edición y análisis de Excel; fórmulas, formato,
  análisis de datos, visualización.
- `pdf` — extracción de texto/tablas, fusión/división, creación,
  relleno de formularios, cifrado/descifrado.

## 3. Licencia y disclaimer

**Importante:** a diferencia de la mayoría de skills de
`anthropics/skills` (Apache 2.0), las skills de documentos son
**source-available, no open source** — se comparten como referencia para
patrones avanzados de manejo de archivos binarios, pero con restricciones
de uso distintas. Antes de adaptar contenido literal de estas skills,
verificar `THIRD_PARTY_NOTICES.md` del repositorio de origen.

## 4. Uso en el framework APB

Empleadas como referencia/wrapper para:
- `apb-doc-generate-ppt-v1.0` (generación de presentaciones con diseño APB)
- `apb-doc-generate-word-v1.0` (generación de documentos Word con estilos APB)

## 5. Procedencia

`https://github.com/anthropics/skills` (subcarpetas `skills/docx`,
`skills/pptx`, `skills/xlsx`, `skills/pdf`). `source_commit` pendiente de
verificación con acceso de red completo (ver GOVERNANCE.md §4.2).
