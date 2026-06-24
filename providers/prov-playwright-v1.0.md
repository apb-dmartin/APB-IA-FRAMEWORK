---
id: "prov-playwright-v1.0"
name: "Provider: Playwright MCP"
description: "Proveedor de acción para automatización de pruebas E2E con Playwright. Permite ejecutar tests, capturar screenshots y generar trazas de ejecución."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
provider_type: "action"
access_mode: "read-write"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Provider: Playwright MCP

---

## Descripción
Proveedor de acción para automatización de pruebas E2E con Playwright. Permite ejecutar tests, capturar screenshots y generar trazas de ejecución.

## Capacidades
- Ejecución de tests Playwright
- Captura de screenshots y videos
- Generación de trazas de ejecución
- Inspección de elementos DOM
- Simulación de interacciones de usuario

## Configuración
```json
{
  "provider_id": "prov-playwright-v1.0",
  "type": "action",
  "endpoint": "local://playwright",
  "auth": "none",
  "browsers": ["chromium", "firefox", "webkit"],
  "headless": true,
  "rate_limit": "unlimited"
}
```

## Inputs
- `test_path`: ruta a los tests
- `browser`: navegador a usar
- `base_url`: URL base de la aplicación
- `options`: opciones adicionales de ejecución

## Outputs
- `test_results`: resultados de los tests
- `screenshots`: capturas de pantalla
- `trace`: traza de ejecución
- `report`: informe HTML

## Dependencias
- `apb-sub-qa-e2e-v1.0` (consumidor principal)
- `apb-qa-test-auto-v1.0` (skill)
- `apb-wf-qa-evidence-v1.0` (workflow)

## Restricciones
- Requiere entorno con navegadores instalados
- No ejecuta en producción sin sandbox
- Screenshots pueden contener datos sensibles

## Ejemplo de Uso
```
Invocar: prov-playwright-v1.0
Input: { test_path: "tests/e2e/login.spec.ts", browser: "chromium", base_url: "https://app.apb.es" }
Output: test_results.json + screenshots + trace.zip
```

---
*Registrado en APB AI Framework.*
