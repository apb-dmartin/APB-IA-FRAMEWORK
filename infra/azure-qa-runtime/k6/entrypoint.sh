#!/usr/bin/env sh
# [IA-GEN] Generado por APB AI Framework (prov-azure-qa-runtime-v1.0) — revisar ANTES de aplicar en producción.
#
# Ejecuta el script k6 indicado por K6_SCRIPT_PATH contra TARGET_URL, exportando
# resultados JSON + resumen para el informe (apb-sub-qa-performance-v1.0).
# La imagen base grafana/k6 usa sh, no bash.
set -eu

if [ -z "${K6_SCRIPT_PATH:-}" ]; then
  echo "[qa-runtime/k6] ERROR: falta K6_SCRIPT_PATH — ruta al script k6 a ejecutar" >&2
  exit 1
fi
if [ -z "${TARGET_URL:-}" ]; then
  echo "[qa-runtime/k6] ERROR: falta TARGET_URL — URL base del sistema a probar (solo PRE/QA)" >&2
  exit 1
fi

echo "[qa-runtime/k6] K6_SCRIPT_PATH=${K6_SCRIPT_PATH}"
echo "[qa-runtime/k6] TARGET_URL=${TARGET_URL}"

mkdir -p /output

# VUS/DURATION son opcionales: si el script k6 ya define 'export const options'
# con sus propios 'scenarios', no hace falta forzarlos aquí.
EXTRA_ARGS=""
if [ -n "${VUS:-}" ]; then
  EXTRA_ARGS="${EXTRA_ARGS} --vus ${VUS}"
fi
if [ -n "${DURATION:-}" ]; then
  EXTRA_ARGS="${EXTRA_ARGS} --duration ${DURATION}"
fi

set +e
# shellcheck disable=SC2086
k6 run \
  --env BASE_URL="${TARGET_URL}" \
  --env TOKEN="${AUTH_TOKEN:-}" \
  --out json=/output/results.json \
  --summary-export=/output/summary.json \
  ${EXTRA_ARGS} \
  "${K6_SCRIPT_PATH}"
EXIT_CODE=$?
set -e

echo "[qa-runtime/k6] Ejecución finalizada con código ${EXIT_CODE}. Resultados en /output."
exit "${EXIT_CODE}"
