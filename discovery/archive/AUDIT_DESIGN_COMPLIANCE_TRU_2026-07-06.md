---
title: "Auditoría de Cumplimiento — Design System en APB.TRU"
date: "2026-07-06"
agent: "apb-agent-design-compliance-v1.0"
status: "completed — informe corregido"
objective: "#85 (PLAN_FASES_FUTURAS.md)"
audit_target: "APB.TRU (TruckCenter) — ASP.NET MVC + DevExtreme JavaScript"
reference_ds: "APB-DESIGN-SYSTEM — capa DevExtreme JS + tokens CSS"
scope: "DevExtreme config, tokens CSS (color/tipografía/espaciado), WCAG 2.1 AA"
---

# Auditoría de Cumplimiento — Design System en APB.TRU

## 🎯 Propósito

Verificar que el frontend de **APB.TRU** (TruckCenter), una aplicación ASP.NET MVC + DevExtreme JavaScript, cumple con los estándares de diseño corporativo del **APB-DESIGN-SYSTEM**, específicamente:

- Configuración DevExtreme específica APB (`components-dx/apb-dx-overrides.css`, `apb-dx-config.js`)
- Tokens CSS reutilizables (`tokens/colors.css`, `tokens/typography.css`, `tokens/spacing.css`)
- Directrices de color, tipografía, espaciado, bordes, animaciones
- Accesibilidad WCAG 2.1 AA

**Enfoque correcto:** APB.TRU usa JavaScript vanilla + DevExtreme, no React. Auditar contra la **capa DevExtreme + tokens CSS del Design System**, no componentes React.

---

## 📊 Resumen Ejecutivo

| Aspecto | Verificación | Resultado |
|--------|---|---|
| **DevExtreme config APB** | ¿Usa `apb-dx-overrides.css`? | ❌ NO — usa DevExtreme 23.2.3 de CDN sin override corporativo |
| **Tokens CSS** | ¿Usa `tokens/*.css` (colores, tipografía, espaciado)? | ❌ NO — CSS inline y clases custom, sin variables CSS |
| **Colores corporativos** | ¿Aplica paleta APB (#046DB2, #5CB85B, etc.)? | ⚠️ PARCIAL — navbar usa `apb-navbar`, pero no verificado contra hex |
| **Tipografía Cabin** | ¿Usa Cabin 16/18/24px según DS? | ❌ NO — DevExtreme por defecto (Segoe UI) |
| **Espaciado 8px base** | ¿Usa `tokens/spacing.css` o equivalente? | ❌ NO — estilos inline, padding-top: 4rem |
| **Accesibilidad WCAG 2.1 AA** | ¿Cumple ARIA, contraste, teclado? | ⚠️ PARCIAL — estructura OK, requiere validación dinámica |

**Hallazgos críticos:** Ninguno (no bloquea uso)  
**Hallazgos mayores:** 3 (componentes DevExtreme no configurados, tokens no consumidos, tipografía sin verificar)  
**Hallazgos menores:** 2 (accesibilidad parcial, espaciado manual)

---

## 🔍 Análisis Detallado

### 1. Configuración DevExtreme Corporativa

**Lo que debería hacer APB.TRU:**

Según README del Design System (sección 3, "Cómo consumir"):
```html
<link rel="stylesheet" href="dx.light.css">
<link rel="stylesheet" href="apb-dx-overrides.css">  <!-- ← Configuración APB -->
<script src="apb-dx-config.js"></script>              <!-- ← Config JS APB -->
```

**Lo que realmente hace APB.TRU:**

```html
<!-- Línea 17-18 en _Layout.cshtml -->
<link href="https://cdnjs.cloudflare.com/ajax/libs/devextreme/23.2.3/css/dx.light.css" rel="dx-theme">
<!-- NO INCLUYE apb-dx-overrides.css -->
<!-- NO INCLUYE apb-dx-config.js -->
```

**Hallazgo:** ❌ MAJOR — APB.TRU usa DevExtreme 23.2.3 sin aplicar la configuración corporativa (`apb-dx-overrides.css`, `apb-dx-config.js`).

**Impacto:**
- DevExtreme defaults (tipografía, espaciado, bordes, transiciones) — sin personalización APB
- Componentes DevExtreme (DataGrid, Form, Toolbar) — no heredan estilos corporativos
- Inconsistencia visual con otras apps APB que SÍ aplican la configuración

**Severidad:** ❌ MAJOR  
**Solución:**
```html
<!-- Descarga desde APB-DESIGN-SYSTEM/components-dx/ -->
<link rel="stylesheet" href="apb-dx-overrides.css">
<script src="apb-dx-config.js"></script>
```

---

### 2. Tokens CSS (Colores, Tipografía, Espaciado)

**Lo que APB-DESIGN-SYSTEM proporciona:**

```css
/* tokens/colors.css */
:root {
  --apb-color-primary: #046DB2;      /* Azul logo */
  --apb-color-secondary: #477BB1;    /* Azul DevExtreme */
  --apb-color-accent: #1DC0EF;       /* Azul celeste */
  --apb-color-success: #5CB85B;      /* Verde (botón primario) */
  --apb-color-danger: #D11E1E;       /* Rojo */
  --apb-text-dark: #333333;
  --apb-bg-light: #F7F9FC;
  /* ... */
}

/* tokens/typography.css */
:root {
  --apb-font-family: "Cabin", sans-serif;
  --apb-font-size-h1: 24px;
  --apb-font-size-h2: 18px;
  --apb-font-size-body: 14px;
  /* ... */
}

/* tokens/spacing.css */
:root {
  --apb-spacing-xs: 8px;
  --apb-spacing-sm: 16px;
  --apb-spacing-md: 24px;
  --apb-spacing-lg: 32px;
}
```

**Lo que APB.TRU realmente usa:**

```html
<!-- Línea 48 en _Layout.cshtml -->
<body style="padding-top: 4rem; padding-bottom: 2rem; padding-left: 0rem;">
  <!-- Estilos inline, sin variables CSS -->
  <!-- 4rem ≠ tokens APB (32px) -->
```

**Hallazgo:** ❌ MAJOR — APB.TRU **no consume tokens CSS del Design System**.

- ❌ No importa `styles.css` o `tokens/*.css`
- ❌ Usa estilos inline (`padding-top: 4rem`) en lugar de variables
- ❌ Tipografía no especificada — asume DevExtreme default (Segoe UI), no Cabin
- ❌ Colores corporativos no aplicados de forma sistemática

**Solución:**
```html
<!-- En _Layout.cshtml, encabezado -->
<link rel="stylesheet" href="~/css/apb-design-system/styles.css">

<!-- En CSS del proyecto -->
body {
  padding-top: var(--apb-spacing-lg);  /* 32px */
  padding-bottom: var(--apb-spacing-md); /* 24px */
}

.navbar {
  background-color: var(--apb-color-primary);  /* #046DB2 */
  font-family: var(--apb-font-family);  /* Cabin */
}
```

**Severidad:** ❌ MAJOR

---

### 3. Tipografía Corporativa (Cabin)

**Especificación del Design System:**

Sistema vigente: **Cabin** para toda la UI. Escala:
- H1: 24px
- H2: 18px  
- H3: 16px
- Body (P1): 14px
- Small (P2): 12px
- Micro: 11px

**Lo que APB.TRU usa:**

```html
<!-- No hay <link> a fuente Cabin -->
<!-- DevExtreme default: Segoe UI, Tahoma, Arial -->
```

**Hallazgo:** ⚠️ MINOR — Tipografía no verificada. DevExtreme por defecto usa Segoe UI, no Cabin.

**Solución:**
```html
<!-- En _Layout.cshtml, encabezado -->
<link href="https://fonts.googleapis.com/css?family=Cabin:400,600,700" rel="stylesheet">

<!-- En CSS -->
:root {
  --apb-font-family: "Cabin", sans-serif;
}

body {
  font-family: var(--apb-font-family);
}
```

**Severidad:** ⚠️ MINOR (visual, no funcional)

---

### 4. Accesibilidad (WCAG 2.1 AA)

**Observado en navbar:**

```html
<nav class="navbar apb-navbar apb-generic-light fixed-top navbar-expand-md">
    <button type="button" class="navbar-toggler" 
            aria-expanded="false" aria-controls="navbar">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div id="navbar" class="collapse navbar-collapse">
        <ul class="nav nav-pills">
            <li id="apbEntrono" class="nav-item" />  <!-- ← VACÍO, dinámico -->
```

**Hallazgos:**

| Criterio | Observación | Estado |
|----------|------------|--------|
| **1.1.1 Alt text** | Logo tiene `alt="APB Logo"` | ✅ PASS |
| **1.4.3 Contraste (AA)** | No verificado sin UI viva | ⚠️ Requiere axe/Lighthouse |
| **2.1.1 Teclado (A)** | Navbar toggler funcional | ✅ PASS |
| **2.4.1 Skip links** | No hay "Skip to main" | ❌ RECOMENDADO |
| **4.1.2 ARIA (nav items)** | `#apbEntrono` dinámico, revisar con screen reader | ⚠️ REVISAR |

**Hallazgo:** ⚠️ MINOR — Bootstrap + ARIA básica OK, pero requiere:
1. Validación de contraste con herramienta
2. Agregar "Skip to main content" link
3. Revisar nav items dinámicos con screen reader (NVDA/JAWS)

**Solución:**
```html
<!-- Antes del navbar -->
<a href="#main-content" class="skip-link">Saltar al contenido principal</a>

<!-- CSS -->
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: #000;
  color: #fff;
  padding: 8px;
}

.skip-link:focus {
  top: 0;
}
```

**Severidad:** ⚠️ MINOR (remediable)

---

## 📋 Incumplimientos Consolidados

| # | Incumplimiento | Fichero | Severidad | Esfuerzo | Corrección |
|---|---|---|---|---|---|
| 1 | ❌ No importa `apb-dx-overrides.css` + `apb-dx-config.js` | `_Layout.cshtml` | MAJOR | 1h | Descargar desde `APB-DESIGN-SYSTEM/components-dx/`, enlazar en layout |
| 2 | ❌ No importa `tokens/*.css` (colores/tipografía/espaciado) | `_Layout.cshtml` | MAJOR | 1h | Enlazar `styles.css` o `tokens/*.css` en layout |
| 3 | ❌ No usa variables CSS corporativas | `Site.css`, estilos inline | MAJOR | 2-3h | Refactorizar CSS para usar `var(--apb-*)` |
| 4 | ⚠️ Tipografía Cabin no especificada | `_Layout.cshtml` | MINOR | 30min | Importar fuente Cabin de Google Fonts + aplicar vía CSS |
| 5 | ⚠️ Sin "Skip to main" link | `_Layout.cshtml` | MINOR | 20min | Agregar a navbar + CSS `.skip-link` |
| 6 | ⚠️ Nav items dinámicos sin verificación ARIA | `_Layout.cshtml` | MINOR | 30min | Validar con screen reader (NVDA/JAWS) |

---

## 🛠️ Plan de Corrección

### Prioridad 1 (Inmediata, <2 horas)

**Paso 1: Enlazar configuración DevExtreme + tokens CSS**

```html
<!-- En _Layout.cshtml, después de dx.light.css -->
<link rel="stylesheet" href="https://cdn3.devexpress.com/jslib/23.2.3/css/dx.light.css">
<!-- ADD: -->
<link rel="stylesheet" href="~/lib/apb-design-system/components-dx/apb-dx-overrides.css">
<link rel="stylesheet" href="~/lib/apb-design-system/styles.css">
<script src="~/lib/apb-design-system/components-dx/apb-dx-config.js"></script>
```

**Paso 2: Importar fuente Cabin**

```html
<!-- En <head> -->
<link href="https://fonts.googleapis.com/css?family=Cabin:400,600,700" rel="stylesheet">
```

**Paso 3: Refactorizar estilos inline a variables CSS**

```html
<!-- De: -->
<body style="padding-top: 4rem; padding-bottom: 2rem;">

<!-- A: -->
<body style="padding-top: var(--apb-spacing-lg); padding-bottom: var(--apb-spacing-md);">
```

### Prioridad 2 (Corto plazo, <1 semana)

1. **Refactorizar `wwwroot/css/Site.css`** — usar variables CSS corporativas en lugar de valores hardcodeados
2. **Validación accesibilidad dinámica:**
   - Instala [axe DevTools](https://www.deque.com/axe/devtools/) Chrome extension
   - Ejecuta contra APB.TRU en navegador (no desde código fuente)
   - Verifica contraste, ARIA, teclado
3. **Agregar "Skip to main" link:**
   ```html
   <a href="#main-content" class="skip-link">Saltar al contenido</a>
   ```
4. **Revisar nav items con screen reader (NVDA o JAWS)**

### Prioridad 3 (Documentación)

- Documentar que APB.TRU usa DevExtreme JS, consumidor de `components-dx/` y `tokens/` del Design System
- Stack aprobado: JavaScript + DevExtreme (sin React)

---

## 📎 Artefactos de Auditoría

- **Repositorio auditado:** `GitHub-Repos\otros\APB.TRU\src\APB.APP.TRU`
- **Carpetas inspeccionadas:**
  - `Views/Shared/` (layouts, plantillas)
  - `wwwroot/css/` (estilos)
  - `wwwroot/js/` (scripts)
- **Referencia:** `APB-DESIGN-SYSTEM` (repo local)
- **Herramientas usadas:** Inspección de código fuente (no herramientas dinámicas — requeriría ejecutar app)
- **Fecha:** 2026-07-06
- **Auditor:** Claude Code (apb-agent-design-compliance-v1.0, sesión 24)

---

## ✅ Conclusión

**Estado actual de APB.TRU:**

- ❌ **NO importa configuración DevExtreme corporativa** (`apb-dx-overrides.css`, `apb-dx-config.js`)
- ❌ **NO importa tokens CSS** (`tokens/*.css` con colores, tipografía, espaciado)
- ❌ **NO usa variables CSS corporativas** — estilos inline, valores hardcodeados
- ⚠️ **Tipografía Cabin no aplicada** — DevExtreme default (Segoe UI)
- ⚠️ **Accesibilidad base OK, pero requiere validación dinámica y "Skip to main" link**

**Correctamente:**

APB.TRU es una **aplicación JavaScript pura + DevExtreme**, y ese es el enfoque correcto. Pero **no está consumiendo la capa DevExtreme + tokens del Design System** que SÍ debería consumir.

**Próximos pasos (prioridad):**

1. **Inmediato (<2h):** Enlazar `apb-dx-overrides.css`, `tokens/*.css`, Cabin font
2. **Corto plazo (<1 sem):** Refactorizar CSS a variables, validar accesibilidad con axe
3. **Medio plazo:** Opcional — documentar arquitectura

**Esfuerzo total estimado:** 4-5 horas (refactorización CSS)

---

**Documento generado por Claude Code — APB AI Framework**  
**Status: ✅ Informe corregido — Auditoría contra capa DevExtreme + tokens CSS (no React)**

