---
id: "std-html-deliverable-v1.0"
name: "Estándar de Entregables en HTML"
version: "1.0.0"
status: "active"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
created_date: "2026-11-22"
review_date: "2027-11-22"
---

# Estándar de Entregables en HTML

## Propósito

Define cómo debe entregarse un documento (informe, análisis de riesgos, plan de mitigación,
especificación, documentación...) cuando su `## 📤 Output Generado` dice «HTML autocontenido»
(ver `apb-plat-deliver-artifact-v1.0`). El portal Mother muestra el contenido tal cual en la
pestaña «Entregables» para que una persona no técnica lo revise y apruebe o rechace cómodamente,
sin necesitar abrir un editor de código ni interpretar Markdown — por eso el HTML debe
renderizarse bien SOLO, sin depender de que Mother lo convierta ni de red/CDN externos.

**Regla general**: si tu `Output Generado` indica HTML, entrega un documento HTML completo y
autocontenido como ÚNICA respuesta — no Markdown, no un resumen seguido del HTML, no los dos
formatos a la vez.

---

## Reglas obligatorias

1. **Documento HTML5 completo y autocontenido.** Empieza literalmente por `<!DOCTYPE html>` y
   contiene `<html>`, `<head>` y `<body>`. Nada antes ni después (sin fences ```html, sin texto
   de acompañamiento) — el portal detecta que es HTML mirando si el contenido empieza por
   `<!doctype html` o `<html`; cualquier otra cosa antes rompe esa detección y se muestra como
   texto plano.
2. **CSS inline en un único `<style>` dentro de `<head>`.** Nunca enlaces a hojas de estilo,
   fuentes o scripts externos (`<link>`, `@import`, CDN) — el visor del portal no tiene acceso a
   red y el documento debe verse igual si se descarga y se abre offline.
3. **Sin JavaScript** salvo que el propio `Output Generado` lo pida explícitamente (p. ej. un
   prototipo interactivo). Un informe/análisis/plan es contenido estático.
4. **Tipografía del sistema, sin librerías de iconos.** `font-family: system-ui, -apple-system,
   "Segoe UI", Roboto, sans-serif;` en `body`. Para estados (Alta/Media/Baja, Aprobado/Pendiente)
   usa texto + color de fondo de la celda/etiqueta, no iconos de una librería externa; un emoji
   Unicode suelto (✅ ⚠️ 🔴) sí está bien, ya lo soporta cualquier navegador sin red.
5. **Imprimible y legible en pantalla.** Ancho de línea cómodo (`max-width: 900px; margin: 0
   auto;` en un contenedor), contraste AA, tablas con `border-collapse: collapse` y celdas con
   padding — quien apruebe o rechace puede imprimirlo o guardarlo como PDF desde el navegador.
6. **Banner de marcado IA visible**, además de los `<meta>` que ya pide
   `apb-plat-deliver-artifact-v1.0` (ver «Metadatos obligatorios» de esa skill): un bloque al
   principio del `<body>`, antes del título, con fondo distintivo y el texto exacto:
   `Generado por IA (APB AI Framework) — pendiente de validación humana`. No eliminable ni
   oculto con `display:none`/`visibility:hidden`.
7. **Estructura semántica**, no una sopa de `<div>`: `<h1>` para el título del documento,
   `<h2>`/`<h3>` para secciones/subsecciones, `<table>` para cualquier matriz o listado tabular
   (scoring de riesgo, hallazgos, plan de acción con fechas/responsables), `<ul>`/`<ol>` para
   listas. Así un lector de pantalla o una extracción posterior a Word/PDF siguen funcionando.
8. **Scoring y severidad con color + texto, nunca solo color.** Una celda "Alta"/"Crítica" lleva
   la palabra Y un color de fondo (p. ej. `background:#fde2e1` para alta, `#fff4cd` para media,
   `#e2f5e6` para baja) — nunca solo el color, por accesibilidad y porque el documento se puede
   imprimir en blanco y negro.
9. **Nada de contenido inventado para rellenar el formato.** Si falta un dato (una fecha, un
   responsable, una métrica), la celda dice literalmente `Pendiente de confirmar` — igual que en
   Markdown, el HTML no es excusa para inventar.

---

## Esqueleto de referencia

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>{Título del documento}</title>
<meta name="generado-por-ia" content="true">
<meta name="agente-origen" content="{agent_id}">
<meta name="estado-revision" content="Pendiente de validación humana">
<meta name="fecha-generacion" content="{fecha ISO}">
<style>
  body { font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; color:#1a1a1a; background:#fff; margin:0; }
  .container { max-width:900px; margin:0 auto; padding:24px; }
  .ai-banner { background:#fff4cd; border:1px solid #e0c35c; border-radius:6px; padding:10px 14px; font-size:0.9rem; margin-bottom:20px; }
  h1 { font-size:1.6rem; } h2 { font-size:1.25rem; margin-top:2rem; } h3 { font-size:1.05rem; }
  table { border-collapse:collapse; width:100%; margin:12px 0; }
  th, td { border:1px solid #d0d0d0; padding:8px 10px; text-align:left; vertical-align:top; }
  th { background:#f3f3f3; }
  .sev-alta, .sev-critica { background:#fde2e1; }
  .sev-media { background:#fff4cd; }
  .sev-baja { background:#e2f5e6; }
  @media print { .ai-banner { -webkit-print-color-adjust:exact; print-color-adjust:exact; } }
</style>
</head>
<body>
<div class="container">
  <div class="ai-banner">⚠️ Generado por IA (APB AI Framework) — pendiente de validación humana</div>
  <h1>{Título del documento}</h1>
  <!-- secciones, tablas de scoring, listas... -->
</div>
</body>
</html>
```

---

## Agentes afectados

Cualquier agente cuyo `## 📤 Output Generado` declare un entregable de la familia «Documento»
en `apb-plat-deliver-artifact-v1.0` (spec, report, risk-report, documentation, plan) y cuyo
`Formato de Salida` referencie este estándar. El prototipo HTML que ya entrega
`apb-agent-ux-mockup-v1.0` (artifact_type `mockup`) es un caso ya resuelto por separado y no
necesita este estándar salvo que quiera adoptarlo por consistencia.

---

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-11-22 | Claude (Anthropic/Claude Code) | Creación — a petición del usuario: los informes de riesgo, planes de mitigación, etc. deben entregarse en HTML navegable en vez de Markdown, para que se puedan aprobar/rechazar cómodamente en el portal. |

---

> **Generado por IA:** Claude (Anthropic/Claude Code).
> **Validado por humano:** _pendiente — completar nombre/rol del validador antes de pasar a `candidate`._
