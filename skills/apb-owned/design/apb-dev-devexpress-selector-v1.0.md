---
id: "apb-dev-devexpress-selector-v1.0"
name: "DevExtreme Component Selector"
description: "Guía de selección de componentes DevExtreme/DevExpress para aplicaciones APB: qué widget usar según el caso de uso, patrones de layout, y referencia de theming con ThemeBuilder. Usada tanto por perfiles funcionales (vía agente de mockups) como por desarrolladores antes de implementar."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "design"
autonomy_level: 1
inputs:
  - "Descripción funcional de la pantalla o sección a construir"
  - "Tipo de dato principal (lista, formulario, gráfico, mixto)"
  - "Perfil del usuario final (operador interno, analista, dirección)"
outputs:
  - "Selección de componentes DevExtreme justificada"
  - "Patrón de layout recomendado"
  - "Referencia de theming aplicable"
consumed_by:
  - "apb-agent-ux-mockup-v1.0"
  - "apb-sub-dev-devexpress-v1.0"
depends_on: []
created_date: "2026-06-24"
review_date: "2026-06-24"
---

# DevExtreme Component Selector

## Propósito

Antes de escribir código o describir un mockup, elegir el componente DevExtreme correcto
para cada caso de uso. Esta skill evita el error más frecuente: usar un DataGrid cuando
basta un List, o un Chart cuando un conjunto de KPI cards es suficiente.

Referencia oficial de componentes: https://js.devexpress.com/jQuery/Demos/WidgetsGallery/
Referencia de theming: https://devexpress.github.io/ThemeBuilder/master/generic/light

---

## Árbol de decisión por tipo de necesidad

### 1. Mostrar colecciones de datos

| Necesidad | Componente | Cuándo NO usarlo |
|---|---|---|
| Lista tabular con filtros, sort, export | `dxDataGrid` | Si hay < 20 registros sin interacción |
| Árbol jerárquico (expedientes, departamentos) | `dxTreeList` | Si la jerarquía tiene > 4 niveles (preferir TreeView) |
| Lista simple de elementos seleccionables | `dxList` | Si necesitas columnas — usa DataGrid |
| Árbol navegable sin datos tabulares | `dxTreeView` | Si necesitas columnas — usa TreeList |
| Tarjetas/fichas de elementos | `dxTileView` | Si hay más de 50 elementos (rendimiento) |
| Tabla de solo lectura con formato rico | `dxDataGrid` con `allowEditing: false` | — |

**Regla DataGrid APB:** virtual scrolling por defecto para > 100 filas; paginación server-side para > 1.000 filas.

### 2. Capturar datos (formularios)

| Necesidad | Componente | Notas APB |
|---|---|---|
| Formulario complejo multi-campo | `dxForm` | Agrupar campos con `colCount` y `itemType: "group"` |
| Campo de texto libre | `dxTextBox` / `dxTextArea` | TextArea si > 1 línea esperada |
| Selección de valor único de lista corta (< 20 items) | `dxSelectBox` | Con `searchEnabled: true` si > 10 items |
| Selección múltiple | `dxTagBox` | |
| Fecha / Hora | `dxDateBox` | Siempre con `displayFormat` explícito (dd/MM/yyyy) |
| Rango de fechas | Dos `dxDateBox` | No existe componente nativo de rango — patrón estándar APB |
| Número | `dxNumberBox` | Con `format` para importes (€) o cantidades |
| Booleano visible | `dxCheckBox` | `dxSwitch` solo para configuraciones on/off explícitas |
| Búsqueda con autocompletado de entidad | `dxAutocomplete` o `dxSelectBox` con `dataSource` remoto | |
| Upload de archivos | `dxFileUploader` | Validar extensiones y tamaño en `onValueChanged` |

**Regla formularios APB:** validación client-side obligatoria con `validationRules`; nunca confiar solo en server-side para feedback de usuario.

### 3. Visualizar métricas y datos analíticos

| Necesidad | Componente | Cuándo usarlo |
|---|---|---|
| Evolución temporal (líneas, barras) | `dxChart` | Series por categoría, datos con eje temporal |
| Distribución (circular) | `dxPieChart` | Máximo 6 segmentos; si hay más, agrupar como "Otros" |
| KPIs individuales con número grande | HTML + CSS (no DevExtreme) | Un número + etiqueta no necesita un componente chart |
| Gauge / velocímetro | `dxCircularGauge` / `dxLinearGauge` | Solo para valores con rango definido (SLA, ocupación) |
| Mapa de calor / pivot | `dxPivotGrid` | Análisis multidimensional; no para informes simples |
| Sparkline en celda de grid | `dxSparkline` dentro de cellTemplate | |

**Anti-patrón frecuente:** dxChart con una sola serie de un solo punto → usar un número con etiqueta en HTML.

### 4. Navegación y estructura de página

| Necesidad | Componente | Notas APB |
|---|---|---|
| Pestañas de sección en misma página | `dxTabPanel` | Máximo 6 pestañas visibles sin scroll |
| Menú lateral de navegación | `dxDrawer` + `dxList` | Patrón estándar de aplicaciones APB |
| Acordeón de secciones colapsables | `dxAccordion` | Para formularios largos o secciones opcionales |
| Breadcrumb | HTML semántico (`<nav>`) | No existe componente nativo — implementar con `<ol>` |
| Wizard / paso a paso | `dxForm` con `screenByScreenValidation` o pestañas | |
| Popup / modal de detalle | `dxPopup` | Evitar popups dentro de popups |
| Panel lateral de detalle | `dxDrawer` con `openedStateMode: "overlap"` | |

### 5. Acciones y controles

| Necesidad | Componente |
|---|---|
| Botón primario de acción | `dxButton` con `type: "default"` |
| Botón secundario / cancelar | `dxButton` con `type: "normal"` |
| Botón peligroso (eliminar) | `dxButton` con `type: "danger"` |
| Menú contextual de acciones | `dxContextMenu` o columna de `buttons` en DataGrid |
| Barra de herramientas | `dxToolbar` |
| Notificación / toast | `dxToast` con `type: "success"/"error"/"warning"/"info"` |
| Confirmación destructiva | `DevExpress.ui.dialog.confirm()` |
| Loading / spinner | `dxLoadPanel` o `dxLoadIndicator` |

---

## Patrones de layout estándar APB

### Layout maestro-detalle
```
[dxDataGrid — listado]          [dxForm o panel — detalle del elemento seleccionado]
     50% ancho                          50% ancho
```
Implementación: `dxSplitter` o dos columnas CSS con `dxDataGrid.onSelectionChanged` → rellenar el form.

### Layout de dashboard operativo
```
[Fila de KPIs — 4 valores en HTML cards]
[dxChart — evolución temporal]    [dxDataGrid — alertas o últimos eventos]
        60% ancho                          40% ancho
```

### Layout de formulario de alta
```
[dxForm — campos agrupados, colCount: 2]
[dxToolbar — botones Guardar / Cancelar alineados a la derecha]
```

### Layout de búsqueda + resultados
```
[dxForm — filtros (colCount: 3 o 4)]   [dxButton — Buscar]
[dxDataGrid — resultados, ocupa 100%]
```

---

## Theming APB con DevExtreme ThemeBuilder

Tema base corporativo: **Generic Light** (https://devexpress.github.io/ThemeBuilder/master/generic/light)

Variables CSS clave a personalizar para APB:

```css
/* Color primario APB — azul corporativo */
--base-accent: #005A9E;          /* botones dxButton type:default, badges, foco */

/* Tipografía */
--base-font-family: "Segoe UI", Arial, sans-serif;
--base-font-size: 14px;

/* Grid */
--datagrid-row-alternation-color: #F5F8FC;   /* filas alternas */
--datagrid-header-color: #E8EEF5;            /* cabeceras */

/* Bordes */
--base-border-color: #D0D9E4;
--base-border-radius: 4px;
```

Para generar el archivo CSS compilado del tema: usar ThemeBuilder CLI (`devextreme-themebuilder`) o la UI web exportando como `.css`.

**Regla APB:** no sobreescribir estilos de DevExtreme con CSS ad-hoc en archivos de componente — toda personalización de tema va en el archivo de tema compilado o en variables CSS del proyecto.

---

## Checklist de selección

Antes de proponer un componente, verificar:
- [ ] ¿Existe un componente DevExtreme nativo para esta necesidad? (consultar WidgetsGallery)
- [ ] ¿El volumen de datos requiere paginación server-side o virtual scrolling?
- [ ] ¿El usuario final es operador interno, analista o dirección? (condiciona la densidad de información)
- [ ] ¿La pantalla debe ser funcional en tablet/móvil? (ajustar `colCount` y ocultar columnas secundarias)
- [ ] ¿Hay acciones destructivas? → confirmar siempre con `dialog.confirm()`

---

> **Generado por IA:** Claude (Anthropic/Claude Code), Sesión Frontend del plan APB-IA-FRAMEWORK.
> **Validado por humano:** _pendiente — completar nombre/rol del validador antes de pasar a `candidate`._


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-dev-devexpress-selector-v1.0) - pendiente validacion humana. No distribuir sin revision.
