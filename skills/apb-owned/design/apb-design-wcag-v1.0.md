---
id: "apb-design-wcag-v1.0"
name: "Validación de Accesibilidad WCAG 2.1 AA"
description: "Auditar y validar el cumplimiento de WCAG 2.1 nivel AA en pantallas, componentes y flujos DevExtreme/DevExpress de APB. Obligatorio por RD 1112/2018 para portales y apps de cara al ciudadano. Produce checklist de conformidad, listado de no conformidades con severidad y pasos de remediación, e integración con Playwright para tests automatizados de accesibilidad."
version: "1.0.0"
status: "deprecated"
deprecated_reason: "Consolidado en apb-qa-accessibility-v1.0 (decision Arquitectura APB 2026-06-30)"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "design"
autonomy_level: 1
consumed_by: []
depends_on:
  - "apb-design-frontend-design-system-v1.0"
created_date: "2026-06-29"
review_date: "2026-12-29"
---

# Validación de Accesibilidad WCAG 2.1 AA

---

## 🎯 Propósito

Garantizar que las pantallas, componentes y flujos del stack APB cumplen con **WCAG 2.1 nivel AA**, obligatorio legalmente para portales y aplicaciones de cara al ciudadano en virtud del **RD 1112/2018** (transposición de la Directiva UE 2016/2102).

La skill produce:
1. Checklist de conformidad WCAG 2.1 AA por criterio de éxito
2. Listado de no conformidades con severidad (bloqueante / alta / media)
3. Pasos de remediación concretos por componente DevExtreme/DevExpress
4. Snippets de test Playwright para validación automatizada de los criterios más relevantes

---

## ⚡ Trigger

Invocar esta skill:
- Antes de validar un mockup con el perfil funcional (paso previo a entregar a desarrollo)
- En la revisión de código de cualquier componente de UI de cara al ciudadano
- Como parte del workflow `apb-wf-qa-evidence-v1.0` para la evidencia de release
- Cuando el `apb-wf-accessibility-audit-v1.0` requiere validación técnica de un componente específico

---

## 📋 Criterios de Éxito WCAG 2.1 AA — Checklist

La skill evalúa los 13 principios de los 4 criterios WCAG 2.1 nivel A y AA más relevantes para el stack DevExtreme:

### Perceptible
| Criterio | ID | Nivel | Componentes DevExtreme afectados |
|----------|----|-------|----------------------------------|
| Texto alternativo en imágenes e iconos | 1.1.1 | A | dxButton con iconos, dxList con thumbnails |
| Subtítulos en vídeo (si aplica) | 1.2.2 | AA | dxPopup con contenido multimedia |
| Contraste de color ≥ 4.5:1 (texto normal) | 1.4.3 | AA | Todos — verificar tokens `--apb-color-*` |
| Contraste de color ≥ 3:1 (texto grande) | 1.4.11 | AA | Encabezados, labels de formulario |
| Reflow sin scroll horizontal en 320px | 1.4.10 | AA | dxDataGrid, dxScheduler en móvil |

### Operable
| Criterio | ID | Nivel | Componentes DevExtreme afectados |
|----------|----|-------|----------------------------------|
| Toda funcionalidad operable con teclado | 2.1.1 | A | dxDataGrid (nav flechas), dxDateBox (calendar) |
| Sin trampas de teclado | 2.1.2 | A | dxPopup, dxDrawer, dxOverlay |
| Foco visible en todos los controles | 2.4.7 | AA | Verificar `:focus` en tema Generic Light APB |
| Propósito del enlace comprensible | 2.4.4 | A | dxMenu, dxTreeView, dxBreadcrumb |
| Skip links si hay bloques repetitivos | 2.4.1 | A | Layouts con navegación lateral persistente |

### Comprensible
| Criterio | ID | Nivel | Componentes DevExtreme afectados |
|----------|----|-------|----------------------------------|
| Idioma de la página declarado | 3.1.1 | A | `<html lang="es">` en plantillas APB |
| Etiquetas en todos los campos de formulario | 3.3.2 | A | dxTextBox, dxSelectBox, dxDateBox |
| Mensajes de error descriptivos | 3.3.1 | A | dxValidationSummary, dxValidator |
| Sugerencia de corrección de errores | 3.3.3 | AA | dxForm con validación inline |

### Robusto
| Criterio | ID | Nivel | Componentes DevExtreme afectados |
|----------|----|-------|----------------------------------|
| Nombre, rol y valor accesibles (ARIA) | 4.1.2 | A | Widgets custom, dxList, dxTreeView |
| Mensajes de estado anunciados | 4.1.3 | AA | dxLoadIndicator, notificaciones dinámicas |

---

## ⚠️ Comportamiento ante inputs incompletos

| Input | Obligatorio | Si falta |
|-------|------------|----------|
| Descripción o código del componente a auditar | ✅ | Bloquea: no se puede evaluar sin el componente. Solicitar: "¿Qué pantalla o componente debo auditar?" |
| Tipo de dispositivo objetivo (desktop / móvil / ambos) | ❌ | Asume: ambos. Informa: "Se audita para desktop y móvil (320px mínimo)" |
| Contexto del usuario final (ciudadano / empleado interno) | ❌ | Asume: ciudadano (máxima exigencia WCAG). Informa en el informe |
| Versión DevExtreme en uso | ❌ | Asume: versión actual del Design System APB. Informa si la evaluación depende de la versión |

---

## 🔄 Flujo de Evaluación

```
Componente recibido
    │
    ▼
1. Identificar nivel de obligatoriedad
    │ (¿portal ciudadano? → WCAG AA obligatorio por ley)
    │ (¿app interna? → WCAG AA recomendado, AA para accesibilidad interna)
    ▼
2. Evaluar criterios A y AA por categoría
    │ (perceptible → operable → comprensible → robusto)
    ▼
3. Clasificar no conformidades
    │ Bloqueante: impide uso del componente por usuario con discapacidad
    │ Alta: degrada significativamente la experiencia
    │ Media: corrección recomendada, no bloquea el flujo principal
    ▼
4. Generar pasos de remediación por componente DevExtreme
    │ (atributos ARIA, cambios en tokens CSS, estructura HTML)
    ▼
5. ⚠️ CHECKPOINT HUMANO — revisión del informe por el desarrollador responsable
    ▼
6. Generar snippets Playwright para criterios automatizables
    │ (contraste, foco, roles ARIA, idioma)
```

---

## 📤 Salida Esperada

```markdown
# Informe de Accesibilidad WCAG 2.1 AA — [Nombre del componente]

## Resumen
- Conformes: X de Y criterios evaluados
- No conformidades bloqueantes: N
- No conformidades altas: N
- No conformidades medias: N

## No Conformidades
### [Bloqueante] 2.1.1 — Foco de teclado no llega a X
**Componente:** dxDataGrid column headers
**Problema:** ...
**Remediación:** `tabIndex="0"` + `role="columnheader"` + ...

## Checklist de Conformidad
| Criterio | ID | Estado | Notas |
|----------|----|--------|-------|
| Texto alternativo | 1.1.1 | ✅ | ... |
...

## Tests Playwright Sugeridos
```typescript
// Verificar contraste mínimo
test('contraste 4.5:1 en texto principal', async ({ page }) => { ... });
```
```

---

## 🔗 Dependencias

- `apb-design-frontend-design-system-v1.0` — tokens CSS APB, paleta de colores base
- `third-anthropic-playwright-v1.0` — para generación de tests de accesibilidad automatizados

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../../context/apb/standards/AI_MARKING_STANDARD.md):

- **Informes de accesibilidad** (Markdown):
  > **Borrador generado por IA** (APB AI Framework - apb-design-wcag-v1.0) — pendiente validación humana. La conformidad WCAG legal requiere auditoría manual complementaria.
- **Tests Playwright**:
  `// [IA-GEN] Generado por APB AI Framework (apb-design-wcag-v1.0) — pendiente revisión humana`

> **Generado por IA:** Claude (Anthropic/Claude Code), sesión 2026-06-29.
> **Validado por humano:** _pendiente — completar nombre/rol del validador antes de pasar a `candidate`._
