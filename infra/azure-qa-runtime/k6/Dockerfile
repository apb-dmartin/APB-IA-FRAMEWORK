# [IA-GEN] Generado por APB AI Framework (prov-azure-qa-runtime-v1.0) — revisar ANTES de aplicar en producción.
#
# Imagen de ejecución efímera para pruebas de rendimiento k6, sin instalar nada
# localmente. Implementa providers/prov-azure-qa-runtime-v1.0.md ("tools_preinstalled":
# k6) y cierra la verificación pre-vuelo de context/apb/standards/TEST_PLAN_STANDARD.md
# §8.1: la carga real (no smoke) nunca se lanza desde un portátil individual contra
# un entorno compartido — este contenedor es el destino `ci-runner`/`azure-qa`.
#
# Consumidor de referencia: skills/apb-owned/qa/apb-qa-performance-v1.0.md +
# subagents/apb-sub-qa-performance-v1.0.md.
#
# IMPORTANTE — K6_VERSION: fijar a una versión real verificada (>= 0.50 según
# docs/qa/EJECUCION_LOCAL.md) antes de construir; no se asume "latest" para evitar
# drift silencioso entre ejecuciones.
ARG K6_VERSION
FROM grafana/k6:${K6_VERSION}

# La imagen oficial grafana/k6 ya corre como usuario non-root (UID 1000, "k6") —
# no se cambia aquí para no romper permisos ya configurados por la imagen base.

WORKDIR /scripts

# El/los script(s) k6 (generados por apb-qa-performance-v1.0) se copian o montan
# en build/run time — este Dockerfile es un runner genérico, no incluye scripts propios.
COPY --chown=k6:k6 entrypoint.sh /entrypoint.sh

USER root
RUN chmod +x /entrypoint.sh && mkdir -p /output && chown k6:k6 /output
USER k6

# Variables resueltas por entorno (nunca hardcodeadas — GOVERNANCE.md §5.2):
#   K6_SCRIPT_PATH     ruta al script k6 a ejecutar (dentro de /scripts)
#   TARGET_URL         URL base del sistema a probar (solo PRE/QA, nunca prod sin autorización)
#   VUS, DURATION      parámetros de carga (opcional — el propio script puede definir 'scenarios')
#   AUTH_TOKEN_SECRET_REF   referencia AKV://<secret> resuelta antes de llegar aquí (nunca en claro)
ENTRYPOINT ["/entrypoint.sh"]
