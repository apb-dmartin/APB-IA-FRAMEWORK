#!/usr/bin/env bash
# [IA-GEN] Generado por APB AI Framework (prov-azure-qa-runtime-v1.0) — revisar ANTES de aplicar en producción.
#
# Ejecuta la suite Playwright indicada por TEST_SUITE_PATH contra BASE_URL, con
# vídeo real y trazas SIEMPRE activados (TEST_PLAN_STANDARD §7.2 — evidencia
# visual = vídeo, no GIF). Escribe todo a /output para que el job/orquestador lo
# recoja (zip, subida a Jira, etc. — resuelto fuera de este contenedor).
set -euo pipefail

: "${BASE_URL:?Falta BASE_URL — URL base del sistema a probar}"
: "${TEST_SUITE_PATH:?Falta TEST_SUITE_PATH — ruta a la suite/spec Playwright a ejecutar}"

echo "[qa-runtime/playwright] BASE_URL=${BASE_URL}"
echo "[qa-runtime/playwright] TEST_SUITE_PATH=${TEST_SUITE_PATH}"

# storageState (sesión autenticada) es OPCIONAL — si no se aporta, la suite debe
# manejar su propio login o ejecutarse sin autenticación. Nunca se acepta una
# credencial en claro por variable de entorno aquí: solo la ruta a un fichero ya
# materializado (por Managed Identity+AKV en Azure, o aportado localmente).
STORAGE_STATE_ARGS=()
if [[ -n "${STORAGE_STATE_PATH:-}" ]]; then
  if [[ -f "${STORAGE_STATE_PATH}" ]]; then
    echo "[qa-runtime/playwright] Reutilizando storageState: ${STORAGE_STATE_PATH}"
  else
    echo "[qa-runtime/playwright] AVISO: STORAGE_STATE_PATH definido pero el fichero no existe — se ejecuta sin sesión reutilizada." >&2
  fi
fi

mkdir -p /output/traces /output/videos /output/report

set +e
npx playwright test "${TEST_SUITE_PATH}" \
  --reporter=html \
  --output=/output/test-results \
  --trace=on \
  --video=on
EXIT_CODE=$?
set -e

# El reporter HTML ya se genera en /output por --reporter=html (playwright.config
# de la app debe apuntar reportDir a /output/report, ver README.md de esta carpeta).
echo "[qa-runtime/playwright] Ejecución finalizada con código ${EXIT_CODE}. Evidencias en /output."
exit "${EXIT_CODE}"
