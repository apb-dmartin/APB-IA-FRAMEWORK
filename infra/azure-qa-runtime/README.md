# Azure QA Runtime — Contenedores Playwright + k6

> **Borrador generado por IA** (APB AI Framework — `prov-azure-qa-runtime-v1.0`) — pendiente de
> validación humana. No aplicar a producción sin revisión de Plataforma/Ciberseguridad.

Implementación de referencia de [`providers/prov-azure-qa-runtime-v1.0.md`](../../providers/prov-azure-qa-runtime-v1.0.md):
dos imágenes Docker que permiten ejecutar pruebas funcionales (Playwright, scriptadas)
y de rendimiento (k6) **sin instalar nada en el puesto de quien las lanza**. Resuelven
directamente dos bloqueantes documentados en `discovery/HANDOFF_TECNICOS.md`:

- **QA3-2** — el vídeo de evidencia real depende hoy de que Playwright MCP esté cargado
  en la sesión local de quien ejecuta.
- **`TEST_PLAN_STANDARD` §8.1** — la carga k6 real nunca debe lanzarse desde un portátil
  contra un entorno compartido (PRE/PRO).

**Estado real de este directorio (léase antes de nada):** los contenedores están
**listos para build/run en local**. El **despliegue a Azure Container Apps queda
pendiente de confirmación de Débora** — no está desplegado todavía, no asumir fecha.

---

## Estructura

```
infra/azure-qa-runtime/
├── playwright/
│   ├── Dockerfile        # runner Playwright — regresión scriptada
│   ├── entrypoint.sh
│   └── .dockerignore
└── k6/
    ├── Dockerfile         # runner k6 — rendimiento
    ├── entrypoint.sh
    └── .dockerignore
```

- **Playwright** es para **regresión scriptada** (`apb-qa-test-auto-v1.0` +
  `prov-playwright-v1.0`), no para `apb-qa-exploratory-nav-v1.0` (navegación EN VIVO,
  inherentemente interactiva — no aplica a un job efímero sin persona).
- **k6** es para el bloque de rendimiento (`apb-qa-performance-v1.0` +
  `apb-sub-qa-performance-v1.0`), p. ej. el bloque B13 del plan unificado de TruckCenter.

---

## Ruta 1 — Uso inmediato en localhost (disponible ya)

Sin Managed Identity ni AKV: las variables se pasan a mano o desde un `.env` local
(**nunca commiteado** — ya cubierto por `.dockerignore`).

### Playwright

```bash
# Build — PLAYWRIGHT_VERSION debe coincidir con "@playwright/test" del package.json
# de la app a testear (docs/qa/EJECUCION_LOCAL.md)
docker build \
  --build-arg PLAYWRIGHT_VERSION=1.48.0 \
  -t apb-qa-playwright-runtime:local \
  infra/azure-qa-runtime/playwright

# Run — monta la suite de tests de la app y una carpeta de salida local
docker run --rm \
  -e BASE_URL="https://staging.gispem.apb.es" \
  -e TEST_SUITE_PATH="/tests/e2e" \
  -v "$(pwd)/ruta/a/tests-app:/tests:ro" \
  -v "$(pwd)/output:/output" \
  apb-qa-playwright-runtime:local
```

### k6

```bash
# Build — K6_VERSION real y verificada (>= 0.50, docs/qa/EJECUCION_LOCAL.md)
docker build \
  --build-arg K6_VERSION=0.54.0 \
  -t apb-qa-k6-runtime:local \
  infra/azure-qa-runtime/k6

# Run — monta el script k6 generado por apb-qa-performance-v1.0
docker run --rm \
  -e TARGET_URL="https://staging.gispem.apb.es" \
  -e K6_SCRIPT_PATH="/scripts/load-test.js" \
  -v "$(pwd)/ruta/a/script-k6:/scripts:ro" \
  -v "$(pwd)/output:/output" \
  apb-qa-k6-runtime:local
```

Evidencias (vídeo/trazas/informe HTML de Playwright, `results.json`/`summary.json`
de k6) quedan en `./output` en el host.

---

## Ruta 2 — Despliegue a Azure Container Apps (pendiente — no ejecutar todavía)

Cuando Débora confirme que el entorno Container Apps está listo para recibir estas
imágenes, quedan estos pasos (**Plataforma, no Claude**):

1. **Build + push a ACR** (Azure Container Registry) — mismas imágenes, con
   `PLAYWRIGHT_VERSION`/`K6_VERSION` fijados a los valores reales acordados.
2. **Crear el Container Apps Job** (uno por imagen, o un job parametrizable que
   seleccione cuál correr) referenciando la imagen en ACR — ver
   `providers/prov-azure-qa-runtime-v1.0.md` para el contrato de configuración
   (`endpoint`, `identity`, `network_scope`, `evidence`).
3. **Asignar Managed Identity** al job, con permiso de lectura sobre el Key Vault
   (`prov-akv-v1.0`) — el job resuelve `AUTH_STORAGE_STATE_SECRET_REF`/`AUTH_TOKEN_SECRET_REF`
   vía esa identidad, nunca con claves estáticas.
4. **Poblar el secreto real en AKV** — comparte bloqueante con `HANDOFF_TECNICOS.md` QA2-1.
5. **Acotar la red** del job a los entornos PRE/QA autorizados (nunca acceso directo
   a producción sin autorización explícita).
6. **Verificar el flujo end-to-end** con una ejecución de prueba antes de usarlo en
   una sesión QA real.

Este README se actualizará cuando Débora confirme que el despliegue está operativo.

---

## Seguridad — reglas que NO cambian entre local y Azure

- Ningún secreto/credencial se hornea en la imagen ni se escribe en este repo
  (`GOVERNANCE.md §5.2`, `prov-akv-v1.0`).
- Las pruebas de rendimiento reales (no `smoke`) nunca se lanzan contra producción
  sin autorización explícita.
- Todo output de estos contenedores es evidencia — tratarla como material controlado,
  no publicarla sin revisión (puede contener datos de sesión/capturas sensibles).
