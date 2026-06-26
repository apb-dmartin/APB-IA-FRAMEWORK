---
id: "apb-design-frontend-design-system-v1.0"
name: "Design System Frontend APB"
description: "Skill de referencia del sistema de diseño frontend APB: tokens CSS, componentes React, configuraciones DevExtreme JS y UI kits completos (DevExtreme Generic Light + overrides corporativos APB). Tipografía vigente: Cabin (confirmado jun-2026). Consumido por agentes de mockups y generación de código frontend para producir pantallas conformes al estándar visual APB."
version: "1.1.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "design"
autonomy_level: 1
created_date: "2026-06-25"
review_date: "2026-06-26"
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
  tokens_json: "design-system/tokens/design-tokens.json"
  tokens_css_entry: "design-system/styles.css"
  tokens_colors: "design-system/tokens/colors.css"
  tokens_typography: "design-system/tokens/typography.css"
  tokens_spacing: "design-system/tokens/spacing.css"
  style_guide: "design-system/style-guide/style-guide.md"
  components_reference: "design-system/components/component-reference.md"
  components_react: "design-system/components/"
  components_dx: "design-system/components-dx/apb-dx-config.js"
  components_dx_css: "design-system/components-dx/apb-dx-overrides.css"
  ui_kit: "design-system/ui_kits/aplicaciones-apb/"
  visual_reference: "design-system/visual-reference/visual-reference.html"
  assets: "design-system/assets/"
limitations:
  - "Los valores base del tema generic.light de DevExtreme están marcados PENDIENTE_VERIFICACION_ARQUITECTURA en design-tokens.json — no usar como ciertos hasta verificación con CLI DevExtreme."
  - "El catálogo de componentes React es parcial — cubre los componentes documentados en PDFs de origen APB 2022. Ver 'Pendiente de completar' en component-reference.md."
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
- Inventar valores de color, tipografía o espaciado no presentes en `tokens/design-tokens.json` o `tokens/colors.css`
- Usar negro puro (`#000000`) en ningún componente de UI
- Construir un componente a medida que `component-reference.md` ya resuelve con DevExtreme
- Usar fuentes distintas a Cabin (sistema vigente confirmado jun-2026)

## Human review points

1. **Conformidad visual:** toda pantalla generada debe validarse contra `visual-reference/visual-reference.html` antes de entregarse como definitiva
2. **Nuevos componentes:** si la necesidad funcional requiere un componente no documentado en `component-reference.md`, escalar a Arquitectura APB antes de inventarlo
3. **Valores DevExtreme base:** los campos `PENDIENTE_VERIFICACION_ARQUITECTURA` en `design-tokens.json` no son fiables — usar los tokens CSS de `tokens/colors.css` como fuente de verdad

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
| 1.1.0 | 2026-06-26 | Arquitectura APB / Claude Code | Design System v1.3: +5 cards (accordion, buttons, charts, spinner, brand-footer); ConfirmPopup mejorado (confirmText/Type, cancelar a la izquierda); Danger button 3 modos CSS; token `--apb-sidebar-bg` corregido a `#ffffff` |

---

> **Generado por IA:** Claude (Anthropic/Claude Code), sesión con Débora Martín — 2026-06-25.
> **Validado por humano:** _pendiente._
