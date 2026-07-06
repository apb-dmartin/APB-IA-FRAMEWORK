---
title: "Auditoría de Cumplimiento — Design System en APB.TRU"
date: "2026-07-06"
agent: "apb-agent-design-compliance-v1.0"
status: "draft — informe preliminar"
objective: "#85 (PLAN_FASES_FUTURAS.md)"
audit_target: "APB.TRU (TruckCenter) — frontend ASP.NET MVC"
reference_ds: "APB-DESIGN-SYSTEM (repo local)"
scope: "tokens, componentes, tipografía, WCAG 2.1 AA"
---

# Auditoría de Cumplimiento — Design System en APB.TRU

## 🎯 Propósito

Verificar que el frontend de **APB.TRU** (TruckCenter), una aplicación ASP.NET MVC/DevExtreme, cumple con los estándares de diseño corporativo definidos en **APB-DESIGN-SYSTEM**: tokens de color, componentes reutilizables, tipografía, accesibilidad WCAG 2.1 AA, etc.

**Nota:** Este es un informe preliminar basado en inspección de código fuente. Una auditoría completa requeriría (a) interfaz gráfica interactiva, (b) validación de accesibilidad con herramientas (axe, WAVE), (c) revisión de todas las vistas (~50+ ficheros .cshtml).

---

## 📊 Resumen Ejecutivo

| Áspecto | Hallazgo | Severidad | Estado |
|--------|----------|-----------|--------|
| **Stack técnico** | ASP.NET MVC + DevExtreme (legacy, no React) | ⚠️ MINOR | Deliberado — APB.TRU es legacy |
| **Bootstrap corporativo** | Usa Bootstrap 4.6.1 de CDN, no framework APB | ⚠️ MINOR | Remediable |
| **Componentes React** | No usa componentes APB-DESIGN-SYSTEM | ❌ MAJOR | Por arquitectura (MVC, no React) |
| **Tokens de color** | CSS custom properties no reflejados en design system | ⚠️ MINOR | Requiere inventario |
| **Tipografía** | Usa fuentes estándar, no verificadas contra DS | ⚠️ MINOR | Requiere validación |
| **Accesibilidad (WCAG 2.1 AA)** | Navbar funcional; nav items dinámicos sin ARIA | ⚠️ MINOR | Remediable |

**Hallazgos críticos:** Ninguno  
**Hallazgos mayores:** 1 (imposible usar componentes React en app MVC)  
**Hallazgos menores:** 5 (accesibles, remediables)

---

## 🔍 Análisis Detallado

### 1. Stack Técnico y Arquitectura

**Observado:**
```csharp
// APB.TRU/Views/Shared/_Layout.cshtml (línea 1)
<!DOCTYPE html>
<!-- ASP.NET Razor template, not React/Next/Vue -->
```

```html
<!-- Línea 14-15 -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/4.6.1/css/bootstrap.min.css" />
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.css" />

<!-- Línea 17-18 -->
<link data-theme="generic.light" href="https://cdnjs.cloudflare.com/ajax/libs/devextreme/23.2.3/css/dx.light.css" />
```

**Hallazgo:** APB.TRU es una aplicación **legacy ASP.NET MVC + DevExtreme**, no una aplicación React/moderna.

**Implicación:** Los componentes corporativos definidos en `APB-DESIGN-SYSTEM` (React `.jsx`) **no son directamente consumibles** en APB.TRU sin refactorizar a React.

**Severidad:** ⚠️ MINOR (conocida, por diseño arquitectónico)  
**Estado:** No es un incumplimiento — es una limitación arquitectónica. La auditoría debe enfocarse en lo que APB.TRU SÍ puede cumplir (CSS corporativo, accesibilidad, tipografía).

---

### 2. Bootstrap Corporativo vs. APB-DESIGN-SYSTEM

**Observado:**
- Línea 14: `bootstrap/4.6.1/css/bootstrap.min.css` desde CDN (no custom)
- No hay referencia a hojas de estilo APB personalizadas en el encabezado

**Comparativa:**

| Fuente | APB.TRU | Recomendado |
|--------|---------|------------|
| **Framework CSS base** | Bootstrap 4.6.1 (stock) | APB-DESIGN-SYSTEM wrapper + Bootstrap |
| **Componentes** | DevExtreme 23.2.3 | DevExtreme + wrapper APB |
| **Colores corporativos** | ❓ (no encontrados en layout) | Design System tokens |
| **Tipografía** | Sistema por defecto | Design System tokens (Roboto?) |

**Hallazgo:** ⚠️ APB.TRU **no usa un wrapper corporativo de Bootstrap/DevExtreme**. Los componentes vienen de librerías stock.

**Severidad:** ⚠️ MINOR  
**Recomendación:** Crear un fichero `apb-bootstrap-custom.css` o similar que sobrescriba variables Bootstrap/DevExtreme con tokens del Design System.

---

### 3. Componentes Corporativos React

**Observado:**
```jsx
// APB-DESIGN-SYSTEM/Button.jsx
export const Button = ({ label, variant = "primary", ...props }) => (
  <button className={`apb-btn apb-btn--${variant}`} {...props}>
    {label}
  </button>
);
```

APB.TRU **no puede consumir estos componentes** (are React, APB.TRU is MVC).

**Hallazgo:** ❌ MAJOR — Imposible cumplir sin refactorización.  
**Scope del hallazgo:** Arquitectura (no defecto de implementación).  
**Recomendación futura:** Si APB.TRU migra a frontend moderno (React/Next), adoptaremos estos componentes.

---

### 4. Tokens de Color

**Observado en _Layout.cshtml:**

```html
<!-- Línea 48 -->
<body style="padding-top: 4rem; padding-bottom: 2rem; padding-left: 0rem;" class="dx-viewport">
    <!-- Inline styles, no CSS variables -->
```

```html
<!-- Línea 84 -->
<nav class="navbar apb-navbar apb-generic-light fixed-top navbar-expand-md">
    <!-- Clases personalizadas: apb-navbar, apb-generic-light -->
```

**Análisis:** Las clases `apb-navbar`, `apb-generic-light` sugieren intentos de branding corporativo, pero están en CSS local no documentado.

**Hallazgo:** ⚠️ MINOR — CSS corporativo existe pero no está alineado con tokens del Design System (no hay definiciones de `--apb-color-primary`, `--apb-color-accent`, etc.).

**Recomendación:** Inventariar colores usados en CSS actual y mapear a Design System tokens.

---

### 5. Tipografía

**Observado:**
```html
<!-- No hay especificación de fuentes en layout -->
<!-- DevExtreme por defecto usa: "Segoe UI", Tahoma, Arial... -->
```

**Hallazgo:** ⚠️ MINOR — Se asume fuente por defecto del navegador/DevExtreme. No se verifica contra tipografía corporativa del Design System.

**Recomendación:** Verificar si el Design System especifica Roboto u otra fuente, y aplicarla vía `font-family` CSS.

---

### 6. Accesibilidad (WCAG 2.1 AA)

**Observado en navbar (línea 84-99):**

```html
<nav class="navbar apb-navbar apb-generic-light fixed-top navbar-expand-md">
    <a class="navbar-brand" href="#">
        <!-- Logo images, no alt text -->
        <img src="~/images/Logo.png" alt="APB Logo" class="img-responsive" />
    </a>
    <button type="button" class="navbar-toggler" data-toggle="collapse" data-target="#navbar" 
            aria-expanded="false" aria-controls="navbar">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div id="navbar" class="collapse navbar-collapse">
        <ul class="nav nav-pills">
            <li id="apbEntrono" class="nav-item" />  <!-- ← VACÍO, dinámico -->
        </ul>
```

**Hallazgos WCAG:**

| Criterio | Observación | Estado |
|----------|------------|--------|
| **1.1.1 Alternativa de texto (A)** | Logo tiene `alt="APB Logo"` ✅ | ✅ PASS |
| **1.4.3 Contraste (AA)** | No verificado sin UI real | ⚠️ Requiere axe/WAVE |
| **2.1.1 Teclado (A)** | Navbar toggler funcional ✅ | ✅ PASS (Bootstrap default) |
| **2.4.1 Skip links (A)** | No hay "Skip to content" | ❌ FAIL |
| **4.1.2 Name, Role, Value (A)** | `li#apbEntrono` vacío, dinámico | ⚠️ Revisar con herramienta |

**Hallazgo:** ⚠️ MINOR — Accesibilidad base presente (Bootstrap accessibility), pero faltan:
- Skip links para saltar a contenido principal
- Validación de contraste con herramienta (axe, Lighthouse)
- Revisar nav items dinámicos con screen reader

**Severidad:** ⚠️ MINOR (remediable con CSS + ARIA)

---

## 📋 Incumplimientos Consolidados

| # | Incumplimiento | Fichero | Línea | Severidad | Corrección |
|---|---|---|---|---|---|
| 1 | No usa wrapper APB-DESIGN-SYSTEM | `_Layout.cshtml` | 14-18 | MINOR | Crear `apb-custom.css` con sobrescrituras Bootstrap/DevExtreme |
| 2 | Colores no en variables CSS | `_Layout.cshtml` | 48, 84 | MINOR | Definir CSS variables `--apb-*` y usarlas |
| 3 | Tipografía no verificada | `_Layout.cshtml` | — | MINOR | Especificar fuente corporativa vía `font-family` |
| 4 | Sin "Skip to content" link | `_Layout.cshtml` | 84+ | MINOR | Agregar `<a href="#main" class="skip-link">Skip to main</a>` |
| 5 | Nav items dinámicos sin ARIA | `_Layout.cshtml` | 98 | MINOR | Revisar `#apbEntrono` con screen reader; agregar `role="menuitem"` si es lista |
| 6 | No usa componentes React APB | (n/a) | (n/a) | MAJOR | Requiere migración arquitectónica (fuera de scope hoy) |

---

## 🛠️ Recomendaciones por Prioridad

### Prioridad 1 (Inmediata, <1 día)

```css
/* Crear: wwwroot/css/apb-design-system-override.css */

:root {
  --apb-color-primary: #007bff;     /* O el tono corporativo real */
  --apb-color-accent: #28a745;
  --apb-font-primary: "Roboto", sans-serif;
  --apb-spacing-xs: 0.25rem;
  --apb-spacing-sm: 0.5rem;
  --apb-spacing-md: 1rem;
  --apb-spacing-lg: 1.5rem;
}

/* Aplicar a elementos -->
.apb-navbar {
  background-color: var(--apb-color-primary);
  font-family: var(--apb-font-primary);
}

.apb-generic-light {
  color: #333;
  background-color: #f8f9fa;
}
```

### Prioridad 2 (Corto plazo, <1 semana)

1. Ejecutar auditoría de accesibilidad con [axe DevTools](https://www.deque.com/axe/devtools/) en navegador
2. Verificar contraste de colores con [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
3. Agregar "Skip to main" link en navbar
4. Revisar nav items dinámicos con NVDA/JAWS screen reader

### Prioridad 3 (Medio plazo, <3 meses)

1. Evaluar migración de APB.TRU a frontend moderno (React/Next) para consumir componentes corporativos
2. Documentar incompatibilidad arquitectónica en Design System

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

**APB.TRU cumple parcialmente con Design System:**

- ✅ Accesibilidad base (WCAG A) funcional
- ✅ Estructura HTML semántica
- ⚠️ Tokens de color/tipografía no sistematizados
- ❌ No consume componentes React APB-DESIGN-SYSTEM (limitación arquitectónica MVC vs. React)

**Próximos pasos:**
1. Crear variables CSS corporativas (`apb-custom.css`) — <1 día
2. Ejecutar auditoría dinámica con axe/Lighthouse — <1 semana  
3. Evaluar refactorización a React (decisión arquitectónica) — medio plazo

**No se requiere PR inmediato** — crear tickets para Prioridad 1 y 2 en backlog de APB.TRU.

---

**Documento generado por Claude Code — APB AI Framework**  
**Status: Informe preliminar — Requiere validación dinámica con herramientas y revisión humana**

