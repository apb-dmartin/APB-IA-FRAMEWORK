#!/usr/bin/env python3
# [IA-GEN] Generado por APB AI Framework (scaffold harness-ready) — pendiente revisión humana
"""
init_check.py — Fase de inicialización dedicada del harness (SYSTEM.md §10.4).

Plantilla PORTABLE y agnóstica de LLM/herramienta: Python estándar, sin
dependencias externas. Copiar al repo destino y adaptar los comandos.

Verifica ANTES de que el agente trabaje:
  1. El entorno es ejecutable (intérprete/toolchain disponible).
  2. El framework de pruebas funciona (smoke test).
  3. Los archivos del harness existen (AGENTS.md, PROGRESS.md, FEATURES.md).

Salida: código 0 si todo OK (el agente puede empezar); 1 si algo falla,
con mensaje "bolígrafo rojo" (GOVERNANCE.md §8.2) indicando cómo corregirlo.
"""

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent

# ── Adaptar al repo destino ────────────────────────────────────────────────
HARNESS_FILES = ["AGENTS.md", "PROGRESS.md", "FEATURES.md"]
ENV_CHECK_CMD = [sys.executable, "--version"]          # p. ej. ["dotnet", "--info"]
TEST_SMOKE_CMD = [sys.executable, "-m", "unittest", "discover", "-s", "tests"]
# ───────────────────────────────────────────────────────────────────────────


def fail(msg: str) -> None:
    print(f"[INIT-FAIL] {msg}")
    sys.exit(1)


def main() -> None:
    for name in HARNESS_FILES:
        if not (REPO_ROOT / name).exists():
            fail(f"Falta {name} en la raíz. Copiarlo desde repo-scaffold/harness-ready/ y completarlo.")

    try:
        subprocess.run(ENV_CHECK_CMD, check=True, capture_output=True)
    except (OSError, subprocess.CalledProcessError) as exc:
        fail(f"Entorno no ejecutable ({' '.join(ENV_CHECK_CMD)}): {exc}. Revisar instalación/PATH.")

    result = subprocess.run(TEST_SMOKE_CMD, capture_output=True, text=True)
    if result.returncode != 0:
        tail = (result.stderr or result.stdout).strip().splitlines()[-5:]
        fail("El framework de pruebas no funciona. Últimas líneas:\n  " + "\n  ".join(tail))

    print("[INIT-OK] Entorno verificado: harness completo, entorno ejecutable, pruebas operativas.")
    print("[INIT-OK] Leer PROGRESS.md (Contrato de Bootstrap) antes de empezar. WIP=1.")


if __name__ == "__main__":
    main()
