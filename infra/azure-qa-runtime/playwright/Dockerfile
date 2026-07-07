# [IA-GEN] Generado por APB AI Framework (prov-azure-qa-runtime-v1.0) — revisar ANTES de aplicar en producción.
#
# Imagen de ejecución efímera para pruebas Playwright scriptadas (regresión) contra
# PRE/QA, sin que el usuario ni el runner instalen nada localmente. Implementa el
# contrato de providers/prov-azure-qa-runtime-v1.0.md ("tools_preinstalled": playwright.
#
# Consumidor de referencia: skills/apb-owned/qa/apb-qa-test-auto-v1.0.md (regresión
# scriptada). NO usar para apb-qa-exploratory-nav-v1.0 (navegación EN VIVO/interactiva
# — no tiene sentido en un job efímero sin persona).
#
# IMPORTANTE — PLAYWRIGHT_VERSION: no se fija un valor por defecto real aquí a
# propósito. Debe coincidir con la versión de "@playwright/test" del package.json
# del REPO DE LA APLICACIÓN a testear (docs/qa/EJECUCION_LOCAL.md: Playwright vive
# en el repo de la app, no en este framework) — un desfase de versión entre esta
# imagen y los tests reales puede producir falsos negativos/positivos.
ARG PLAYWRIGHT_VERSION
FROM mcr.microsoft.com/playwright:v${PLAYWRIGHT_VERSION}-noble

# Usuario non-root (UID > 10000), conforme a skills/apb-owned/platform/apb-plat-docker-v1.0.md
RUN groupadd --gid 10001 qaruntime \
    && useradd --uid 10001 --gid qaruntime --shell /bin/bash --create-home qaruntime

WORKDIR /tests

# El código de tests (specs Playwright) se monta o se copia en build time desde el
# repo de la app — este Dockerfile NO incluye tests propios, es un runner genérico.
# package.json/playwright.config.* del repo de la app deben copiarse en el mismo
# contexto de build (ver README.md de esta carpeta).
COPY --chown=qaruntime:qaruntime entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Directorio de salida de evidencias (vídeo/trazas/informes) — se monta como volumen
# en local o como storage compartido en Azure Container Apps Job.
RUN mkdir -p /output && chown qaruntime:qaruntime /output

USER qaruntime

# Variables resueltas SIEMPRE por entorno (Managed Identity/AKV en Azure, o .env
# local sin commitear) — NUNCA hardcodeadas aquí (GOVERNANCE.md §5.2, prov-akv-v1.0):
#   BASE_URL                    URL del sistema a probar (preferente PRE/staging)
#   TEST_SUITE_PATH             ruta a la carpeta/spec Playwright a ejecutar
#   AUTH_STORAGE_STATE_SECRET_REF   referencia AKV://<secret> al storageState de sesión
#                                (resuelta por Managed Identity antes de llegar aquí;
#                                 el contenedor recibe la ruta ya materializada, no el secreto)
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
