---
id: "prov-playwright-v1.0"
name: "Provider: Playwright MCP"
description: "Proveedor de acción para automatización de pruebas E2E con Playwright. Permite ejecutar tests, capturar screenshots y generar trazas de ejecución."
version: "1.2.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
provider_type: "action"
access_mode: "read-write"
created_date: "2026-06-20"
review_date: "2026-07-03"
verified_date: "2026-07-10"
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

**Verificada (2026-07-03):** registrada a nivel de proyecto en `.mcp.json` (raíz del repo, versionado en
git), usando el servidor oficial [`@playwright/mcp`](https://github.com/microsoft/playwright-mcp):

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest", "--caps", "devtools", "--output-dir", "qa-evidence/output"]
    }
  }
}
```

Al estar en `.mcp.json` del repo, está disponible para cualquier sesión de Claude Code que se abra sobre
`APB-IA-FRAMEWORK` sin reconfiguración adicional (norma de activación de providers MCP del framework:
proyecto + doc, no solo sesión de usuario). **Tras cambiar `.mcp.json` hay que reabrir la sesión de Claude
Code** para que el nuevo argumento del servidor se cargue (no hay hot-reload de configuración MCP).

### Grabación de vídeo real — verificado end-to-end (2026-07-10)

Corrige la suposición de `TEST_PLAN_STANDARD §7.2` (previa a esta fecha): la grabación de vídeo **no** es
un flag de arranque tipo `video:'on'`, son dos tools MCP (`browser_start_video` / `browser_stop_video`)
que hay que invocar explícitamente. Requisitos reales, verificados uno a uno con un servidor de prueba
aislado (no bastaba con leer el README del paquete, que documenta más tools de las que expone por
defecto):

1. **`--caps devtools`** en los args del servidor (arriba) — sin esto, `browser_start_video` /
   `browser_stop_video` / `browser_video_chapter` / `browser_start_tracing` ni existen como tools; están
   implementadas en `playwright-core` pero con `capability: "devtools"`, no en el set por defecto.
2. **Binario `ffmpeg` instalado**: `npx playwright install ffmpeg` (no lo instala `playwright install
   chromium`). Sin él, `browser_start_video` falla con `Executable doesn't exist at
   .../ms-playwright/ffmpeg-*/ffmpeg-win64.exe` — el error es claro pero fácil de pasar por alto.
3. **El parámetro `filename` de `browser_start_video` se resuelve relativo al directorio de trabajo del
   proceso del servidor MCP (la raíz del repo), NO relativo a `--output-dir`** — a diferencia de
   snapshots/consola, que sí respetan `--output-dir`. Para no dejar `.webm` sueltos en la raíz del repo,
   pasar siempre una ruta explícita dentro de `qa-evidence/`, p. ej.
   `filename: "qa-evidence/videos/{APP}/{bloque}.webm"` (carpeta cubierta por `.gitignore`).

**Uso real para segmentar evidencia por bloque** (resuelve la exigencia de `TEST_PLAN_STANDARD §7.2` de
segmentar por bloque en vez de una grabación continua que puede truncarse):
```
browser_start_video({ filename: "qa-evidence/videos/TRU/B02.webm" })
... navegación/interacciones del bloque B02 ...
browser_stop_video()
browser_start_video({ filename: "qa-evidence/videos/TRU/B03.webm" })
... bloque B03 ...
browser_stop_video()
```
Verificado con un servidor de prueba aislado (puerto local temporal, sesión MCP HTTP manual): el `.webm`
resultante es un contenedor WebM/EBML válido (cabecera `1A 45 DF A3`), no un fichero vacío ni un enlace
roto.

**Contrato conceptual del provider** (agnóstico de la config anterior — otros runtimes/adaptadores pueden
resolver el mismo contrato con su propio mecanismo de conexión MCP):
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
