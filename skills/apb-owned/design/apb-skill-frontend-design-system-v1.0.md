---
id: "apb-skill-frontend-design-system-v1.0"
name: "Design System Frontend APB"
description: "Skill de referencia del sistema de diseño frontend APB: tokens de color, tipografía y espaciado (DevExtreme Generic Light + overrides corporativos APB), reglas de uso narrativas y mapeo de componentes DevExtreme jQuery. Consumido por agentes de mockups y generación de código frontend para producir pantallas conformes al estándar visual APB."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "design"
autonomy_level: 1
created_date: "2026-06-25"
review_date: "2026-06-25"
source_commit: "unverified"
verified_date: "unverified"
inputs:
  - "Descripción funcional de la pantalla o sección a generar"
  - "Sistema tipográfico activo (A: Cabin | B: Helvetica Neue/Source Sans Pro) — requerir al usuario si no se especifica"
  - "Perfil del usuario final (operador interno, analista, dirección)"
outputs:
  - "Mockup o código frontend conforme al estándar visual APB"
  - "Uso exclusivo de componentes DevExtreme documentados en component-reference.md"
  - "Tokens de color y espaciado de design-tokens.json, nunca valores inventados"
depends_on:
  - "apb-ops-telemetry-emit-v1.0"
consumed_by:
  - "apb-agent-ux-mockup-v1.0"
  - "apb-sub-dev-devexpress-v1.0"
design_system_repo: "https://github.com/apb-dmartin/APB-DESIGN-SYSTEM"
design_system_submodule: "design-system/"
artifacts:
  tokens: "design-system/tokens/design-tokens.json"
  style_guide: "design-system/style-guide/style-guide.md"
  components: "design-system/components/component-reference.md"
  visual_reference: "design-system/visual-reference/visual-reference.html"
limitations:
  - "Los valores base del tema generic.light de DevExtreme están marcados PENDIENTE_VERIFICACION_ARQUITECTURA en design-tokens.json — no usar como ciertos hasta verificación con CLI DevExtreme."
  - "Existe discrepancia tipográfica sin resolver (Cabin vs Helvetica Neue/Source Sans Pro) — preguntar siempre cuál sistema aplicar si la tarea no lo especifica."
  - "El catálogo de componentes es parcial — cubre los documentados en los PDF de origen APB 2022."
telemetry:
  emit_on: ["invocation", "output_generated", "human_review_requested"]
---

# Design System Frontend APB

## Resumen

Este skill encapsula el **sistema de diseño frontend de la Autoritat Portuària de Barcelona**: la combinación del tema base **DevExtreme Generic Light** (jQuery) con las personalizaciones corporativas APB documentadas en la Guía de Estilos 2022.

Los artefactos de contenido viven en el repo independiente [APB-DESIGN-SYSTEM](https://github.com/apb-dmartin/APB-DESIGN-SYSTEM), integrado en APB-IA-FRAMEWORK como submodule en `design-system/`.

## Uso por el agente

**Orden de lectura obligatorio antes de generar cualquier pantalla:**

1. Leer `design-system/tokens/design-tokens.json` → valores exactos (hex, px, nombres de fuente)
2. Leer `design-system/style-guide/style-guide.md` → cuándo y por qué usar cada token
3. Leer `design-system/components/component-reference.md` → qué componente DevExtreme instanciar

**Nunca:**
- Inventar valores de color, tipografía o espaciado no presentes en `design-tokens.json`
- Usar negro puro (`#000000`) en ningún componente de UI
- Construir un componente a medida que `component-reference.md` ya resuelve con DevExtreme
- Resolver unilateralmente la discrepancia tipográfica — preguntar siempre

## Human review points

1. **Sistema tipográfico:** confirmar con el usuario si la tarea no especifica Cabin (A) o Helvetica Neue/Source Sans Pro (B)
2. **Conformidad visual:** toda pantalla generada debe validarse contra `visual-reference/visual-reference.html` antes de entregarse como definitiva
3. **Nuevos componentes:** si la necesidad funcional requiere un componente no documentado en `component-reference.md`, escalar a Arquitectura APB antes de inventarlo

## Estado de aprobación

**Borrador pendiente de revisión por Arquitectura APB.**

No usar en generación de producción hasta que:
1. Arquitectura APB rellene los valores `PENDIENTE_VERIFICACION_ARQUITECTURA` en `design-tokens.json`
2. Se resuelva la discrepancia tipográfica (`style-guide.md §2.1`)
3. Débora Martín o Arquitectura APB actualice `status` de `draft` a `approved`

> **Validado por:** _______________ (nombre/rol) — Fecha: _______________

## Historial de cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-25 | Arquitectura APB / Claude Code | Creación inicial — sistema de diseño APB v1.0 |

---

> **Generado por IA:** Claude (Anthropic/Claude Code), sesión con Débora Martín — 2026-06-25.
> **Validado por humano:** _pendiente._
