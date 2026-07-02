---
id: "prov-browser-agent-v1.0"
name: "Provider: Agentic Browser"
description: "Proveedor de acción para navegación agéntica/exploratoria en vivo: un agente abre la aplicación, observa la pantalla y el DOM, decide el siguiente paso sin guion fijo, rellena formularios, asevera resultados y captura evidencias. Agnóstico de LLM y de herramienta (Playwright MCP, Claude-in-Chrome o computer-use como implementaciones de referencia)."
version: "1.0.0"
status: "draft"
owner: "QA Gobierno APB <qa-gobierno@portdebarcelona.cat>"
domain: "platform"
provider_type: "action"
access_mode: "read-write"
created_date: "2026-07-02"
review_date: "2026-07-02"
---

# Provider: Agentic Browser

> **Complementa, no sustituye, a [`prov-playwright-v1.0`](prov-playwright-v1.0.md).** Playwright ejecuta
> **guiones fijos reproducibles** (regresión/CI); este provider habilita **navegación exploratoria en vivo**
> (descubrimiento, QA manual asistido). Frontera detallada en `apb-qa-exploratory-nav-v1.0`.
>
> **Agnóstico de LLM y herramienta** (principio #1 del framework / Harness §83): el contrato de capacidades
> es independiente del modelo y de la implementación concreta. Ver §Implementaciones de referencia.

---

## Descripción

Permite que un agente **conduzca un navegador real de forma exploratoria**: abre una URL, "observa" la
pantalla (captura + árbol de accesibilidad/DOM), **decide el siguiente paso en función de lo que ve** (sin
guion predefinido), interactúa (clic, escritura, selección, subida de ficheros), **asevera** condiciones y
**captura evidencias** (screenshots, trazas, vídeo, texto de página).

## Capacidades

- Abrir URL y navegar (ir atrás/adelante, recargar, cambiar de pestaña).
- Observar: captura de pantalla + árbol de accesibilidad + consulta del DOM + texto de página.
- Decidir el siguiente paso a partir del estado observado (bucle percepción→acción).
- Interacción: clic, doble clic, escritura, selección, hover, arrastrar, subir fichero.
- Aserción exploratoria: "¿aparece el elemento X?", "¿el título es Y?", "¿el flujo llegó a Z?".
- Captura de evidencia por paso (screenshot/trace) y consolidación en un paquete.
- Reutilización de sesión autenticada mediante `storage_state` (p. ej. EntraID tras login asistido).

## Configuración

```json
{
  "provider_id": "prov-browser-agent-v1.0",
  "type": "action",
  "endpoint": "local://agentic-browser",
  "implementation": "playwright-mcp | claude-in-chrome | computer-use",
  "auth": "storage_state",
  "browsers": ["chromium", "edge", "firefox", "webkit"],
  "headless": false,
  "evidence": { "screenshots": true, "trace": true, "video": true }
}
```

## Inputs

- `base_url`: URL de entrada de la aplicación.
- `goal`: objetivo en lenguaje natural (p. ej. "verificar que un USER_READ no ve 'Salir del Parking'").
- `storage_state` (opcional): sesión autenticada previamente capturada (evita re-login).
- `constraints` (opcional): límites de exploración (dominios permitidos, acciones prohibidas, timeouts).
- `evidence` (opcional): qué capturar y dónde (`zip` | `jira` | `ambos`).

## Outputs

- `steps`: traza de pasos percepción→decisión→acción.
- `assertions`: resultado de cada aserción (pass/fail + evidencia asociada).
- `evidence_package`: screenshots + trace + vídeo + informe.
- `findings`: hallazgos exploratorios (defectos, comportamientos inesperados).

## Dependencias

- `apb-qa-exploratory-nav-v1.0` (skill consumidora principal — conduce este provider).
- `apb-sub-qa-e2e-v1.0` (subagente E2E).
- `apb-wf-qa-evidence-v1.0` (workflow de evidencias).

## Implementaciones de referencia (no dependencia dura)

| Implementación | Uso típico | Nota |
|---|---|---|
| **Playwright MCP** conducido por el agente | Exploración con capacidad de fijar el guion resultante | Puente natural hacia `prov-playwright` para regresión |
| **Claude-in-Chrome** (extensión) | Conducción de Chrome real ya autenticado (SSO/EntraID) | Útil cuando el login es interactivo |
| **computer-use** | Último recurso (control de escritorio) | Navegadores en tier restringido; preferir los anteriores |

> El componente que consume este provider **no debe** codificar una implementación concreta: selecciona la
> disponible en el runtime. Cambiar de implementación no cambia el contrato.

## Restricciones

- Requiere entorno con navegador instalado.
- **No ejecuta en producción sin sandbox/autorización**; preferente sobre PRE/staging.
- Screenshots/trazas pueden contener datos sensibles → tratar como evidencia controlada (no publicar).
- **Credenciales nunca hardcodeadas**: usar `storage_state` capturado o Azure Key Vault por referencia (`GOVERNANCE.md` §5).
- Autonomy Level 1: la exploración es asistida; el humano valida hallazgos y decide acciones.

## Ejemplo de Uso

```
Invocar: prov-browser-agent-v1.0
Input: { base_url: "https://dockspre.portdebarcelona.cat/tru/", goal: "confirmar que USER_READ no ve la acción 'Salir del Parking'", storage_state: "auth/user_read.json", evidence: "ambos" }
Output: steps[] + assertions[] + evidence_package (zip + adjuntos Jira) + findings[]
```

---
*Registrado en APB AI Framework. Requiere revisión humana antes de aprobación.*
