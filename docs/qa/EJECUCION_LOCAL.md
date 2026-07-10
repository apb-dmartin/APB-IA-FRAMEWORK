# Ejecución local de pruebas (Playwright + k6)

> **Borrador generado por IA** (APB AI Framework) — pendiente de validación humana. No distribuir sin revisión.
>
> Guía para el **destino de ejecución `local`** de [`TEST_PLAN_STANDARD §9.1/§9.3`](../../context/apb/standards/TEST_PLAN_STANDARD.md):
> cómo preparar tu PC para lanzar las pruebas funcionales (Playwright) y de rendimiento (k6). Si prefieres
> **no instalar nada**, usa el destino `azure-qa` (`prov-azure-qa-runtime-v1.0`) o un `ci-runner` — esta guía
> es solo para ejecución en tu máquina.

La skill [`apb-qa-test-plan-v1.0`](../../skills/apb-owned/qa/apb-qa-test-plan-v1.0.md) **detecta si falta
tooling y te guía** por estos pasos; también puedes seguirlos manualmente.

---

## 0. Regla de oro sobre credenciales

- **Nunca** escribas usuario, contraseña, token ni un `storageState` con secretos en el repositorio
  (`AGENTS.md §3`, `GOVERNANCE.md §5.2`).
- El usuario de ejecución se resuelve por **referencia Azure Key Vault** (`AKV://<secret>`) o se introduce
  en un **login asistido** en runtime. El `storageState` resultante se guarda **fuera** de control de
  versiones (p. ej. en `.gitignore`).
- **La carga k6 no se lanza desde el portátil** contra infraestructura compartida (PRE/PRO): eso va a
  `ci-runner` o `azure-qa`. En local, k6 solo para pruebas de humo o contra un entorno propio.

---

## 1. Requisitos previos

| Herramienta | Para qué | Versión mínima |
|---|---|---|
| Node.js LTS | Playwright (E2E/funcional/API) | ≥ 18 |
| Playwright | Navegadores + runner de pruebas | última |
| k6 | Rendimiento (solo humo en local) | ≥ 0.50 |
| Navegador | Chrome / Edge ya suelen estar instalados | — |

---

## 2. Windows (PowerShell) — recomendado en APB

> APB usa Windows como entorno principal. Usa `winget` (incluido en Windows 11).

### 2.1 Node.js

```powershell
winget install OpenJS.NodeJS.LTS
# Cierra y reabre la terminal para refrescar el PATH
node --version   # debe mostrar v18+ 
npm --version
```

### 2.2 Playwright (en el repo de la aplicación, no en el del framework)

```powershell
cd C:\ruta\al\repo-de-la-app
npm init -y                      # solo si no hay package.json
npm install -D @playwright/test
npx playwright install           # descarga Chromium/Firefox/WebKit
npx playwright --version
```

### 2.3 k6 (opcional, solo humo en local)

```powershell
winget install k6.k6
# alternativa: choco install k6
k6 version
```

---

## 3. macOS / Linux (bash)

```bash
# Node vía nvm (recomendado)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
nvm install --lts && node --version

# Playwright (en el repo de la app)
npm install -D @playwright/test
npx playwright install

# k6
brew install k6           # macOS
# Linux: ver instrucciones oficiales de k6 para tu distro
```

---

## 4. Autenticación EntraID (login asistido → storageState)

Muchas apps APB usan EntraID/SSO. En lugar de hardcodear credenciales:

1. Lanza un login asistido una vez (tú completas usuario/rol de prueba + MFA).
2. Guarda la sesión autenticada en un `storageState.json` **fuera** del control de versiones.
3. Reutilízalo en las corridas (Playwright: `use: { storageState: 'auth/storageState.json' }`).

```powershell
# Ejemplo: capturar sesión con Playwright (headed) y guardarla
npx playwright open --save-storage=auth/storageState.json https://dockspre.portdebarcelona.cat/tru/
```

> Añade `auth/` a `.gitignore`. El `storageState` con cookies de sesión es **secreto**.

---

## 5. Verificación rápida

```powershell
node --version && npm --version
npx playwright --version
k6 version            # si instalaste k6
```

Si los tres responden, tu máquina está lista para el destino `local`. Si algo falla, la skill te indicará
el paso concreto que falta.

---

## 5.1 Nota (2026-07-10): preferir Docker si el proxy corporativo bloquea la instalación nativa

En un PC dentro de la red APB, `npx playwright install` puede fallar con
`DEPTH_ZERO_SELF_SIGNED_CERT` porque el proxy corporativo intercepta el TLS de la descarga directa
del CDN de Playwright. Docker Desktop sí atraviesa ese proxy sin problema (usa los registries
oficiales, no el CDN de descarga de navegadores de Playwright). Si te pasa esto, en vez de pelear
con `NODE_EXTRA_CA_CERTS`/`--use-system-ca`, usa directamente las imágenes ya construidas en
`infra/azure-qa-runtime/` (`playwright/` y `k6/`, ver su `README.md`) — es exactamente lo que
`QA3-2` (`discovery/HANDOFF_TECNICOS.md`) resuelve: cero dependencia del puesto de trabajo. El k6
CLI nativo (`winget install GrafanaLabs.k6` — el ID correcto en winget, no `k6.k6`) sí suele
instalar sin problema si lo prefieres para chequeos rápidos, pero para consistencia con el resto del
framework se recomienda usar también la imagen Docker de k6.

## 6. Cuándo NO usar local

| Situación | Destino recomendado |
|---|---|
| Regresión automática por cada PR | `ci-runner` (GitHub Actions / Azure DevOps) |
| Carga/estrés k6 contra PRE/PRO | `azure-qa` (`prov-azure-qa-runtime-v1.0`) o `ci-runner` |
| "No quiero instalar nada" | `azure-qa` — job efímero con todo pre-instalado |
| Ejecución completa (funcional + rendimiento + seguridad) | `azure-qa` |

---

*Documento del APB AI Framework. Requiere revisión humana antes de aprobación.*
