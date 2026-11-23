---
id: "prov-axe-core-v1.0"
name: "Provider: axe-core Accessibility Scan (BuiltInTool de Mother)"
description: "Proveedor de acción para auditar accesibilidad WCAG 2.1 de una URL real inyectando axe-core sobre la sesión Playwright ya existente, y devolver las violaciones encontradas por criterio."
version: "1.0.0"
status: "draft"
owner: "QA APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
provider_type: "action"
access_mode: "read-only"
created_date: "2026-11-23"
review_date: "2026-11-23"
depends_on:
  - "prov-playwright-v1.0"  # axe-core corre sobre la misma sesión de navegador, no es un runtime aparte
---

# Provider: axe-core Accessibility Scan (BuiltInTool de Mother)

---

## Descripción

Abre una URL con el mismo motor Playwright (Chromium headless) ya integrado en Mother,
inyecta el script `axe-core` y ejecuta `axe.run()` sobre la página cargada, devolviendo
las violaciones de accesibilidad agrupadas por criterio WCAG 2.1 (nivel, impacto, nodos
afectados). No sustituye una auditoría manual completa (navegación por teclado, lectores
de pantalla) pero cubre el conjunto de reglas automatizables de axe-core, que es lo que
hoy falta por completo en `apb-qa-accessibility-v1.0`.

## Capacidades

| Acción | Descripción | Gate humano |
|--------|-------------|--------------|
| `scan_url` | Carga una URL y devuelve las violaciones axe-core detectadas | No |

## Mecanismo real

**No es un servidor MCP aparte** — reutiliza el mismo paquete `Microsoft.Playwright` que
`PlaywrightSmokeTool` ya usa en Mother. No requiere binario ni proceso adicional: solo
añade la inyección de `axe.min.js` (vendorizado o descargado una vez) y la lectura del
resultado de `axe.run()` vía `page.EvaluateAsync`.

## Configuración

```json
{
  "provider_id": "prov-axe-core-v1.0",
  "type": "action",
  "mechanism": "builtin_tool",
  "builtin_tool_name": "axe-core-scan",
  "permissions": ["read"]
}
```

## Inputs

- `url`: URL http(s) absoluta a auditar.

## Outputs

- `{ violations: [{ id, impact, wcag_tags, description, nodes_count }], url, scanned_at }`

## Dependencias

- `prov-playwright-v1.0` — provee la sesión de navegador sobre la que corre axe-core
- `apb-qa-accessibility-v1.0` (skill que consume el resultado para el informe WCAG)

## Restricciones

- Solo lectura: no interactúa con la página más allá de cargarla y leer el DOM.
- No certifica conformidad WCAG 2.1 AA completa por sí solo — cubre reglas automatizables;
  el informe de la skill debe declarar explícitamente qué queda pendiente de revisión
  manual (navegación por teclado, lectores de pantalla, contraste dinámico).

## Ejemplo de Uso

```
Invocar: prov-axe-core-v1.0
Action: scan_url
Url: "https://localhost:3000/"
→ { violations: [{id: "color-contrast", impact: "serious", wcag_tags: ["wcag2aa","wcag143"],
     description: "...", nodes_count: 3}], url: "...", scanned_at: "2026-11-23T..." }
```

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-11-23 | Claude (Anthropic), a petición de Débora | Creación: `apb-qa-accessibility-v1.0` no tenía ningún mecanismo de ejecución declarado |

---
*Registrado en APB AI Framework.*
