#!/usr/bin/env python3
"""
orchestrate_checkpoint_gate.py — PoC de orquestación con puntos de aprobación humana

Lee el frontmatter de un workflow, extrae los human_checkpoints, y genera
el bloque de pausa estructurado definido en apb-orch-human-checkpoint-v1.0.md.

Uso:
    python scripts/orchestrate_checkpoint_gate.py --workflow apb-wf-sdd-full-v1.0
    python scripts/orchestrate_checkpoint_gate.py --workflow apb-wf-sdd-full-v1.0 --checkpoint 1

Salida:
    Bloque Markdown + YAML de decisión (destinado a ser output de un job de GitHub Actions).
"""

import sys
import re
import argparse
from pathlib import Path
from typing import Dict, Tuple, List

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML no esta instalado. Ejecute: pip install pyyaml")
    sys.exit(1)

# Forzar UTF-8 en Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parent.parent
FRONTMATTER_PATTERN = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(content: str) -> Tuple[Dict, bool]:
    """Extrae y parsea el frontmatter YAML real. Devuelve (metadata, found)."""
    match = FRONTMATTER_PATTERN.match(content)
    if not match:
        return {}, False
    try:
        data = yaml.safe_load(match.group(1))
        if not isinstance(data, dict):
            return {}, False
        return data, True
    except yaml.YAMLError:
        return {}, False


def load_workflow(workflow_id: str) -> Tuple[Dict, str, bool]:
    """
    Carga un workflow por ID y devuelve (metadata, content, found).
    Busca en workflows/{workflow_id}.md
    """
    workflow_path = REPO_ROOT / "workflows" / f"{workflow_id}.md"
    if not workflow_path.exists():
        return {}, "", False

    content = workflow_path.read_text(encoding="utf-8")
    metadata, found = parse_frontmatter(content)
    return metadata, content, found


def generate_checkpoint_block(
    workflow_id: str,
    checkpoint_name: str,
    checkpoint_index: int,
    agents_list: List[str] = None
) -> str:
    """
    Genera el bloque de pausa estructurado según apb-orch-human-checkpoint-v1.0.md.

    Args:
        workflow_id: ID del workflow (ej. "apb-wf-sdd-full-v1.0")
        checkpoint_name: Nombre del checkpoint (ej. "Validación humana antes de cada fase crítica del workflow")
        checkpoint_index: Índice del checkpoint en la lista (1-indexed para presentación)
        agents_list: Lista de agentes del workflow (opcional, para contexto)

    Returns:
        Bloque Markdown formateado.
    """

    # Resumen del trabajo previo — adaptado al contexto del workflow
    work_completed = f"""
- Fase previa completada según agentes anteriores del workflow
- Artefactos intermedios generados y validados
- Contexto de negocio/técnico/seguridad integrado
- Cambios solicitados en checkpoints previos (si aplica) ya aplicados
"""

    # Descripción de lo que se necesita revisar
    review_scope = f"""
**Checkpoint #{checkpoint_index}:** {checkpoint_name}

El workflow `{workflow_id}` requiere validación humana antes de continuar:
- Revisar los artefactos principales generados hasta aquí
- Confirmar que el scope y la dirección técnica son correctos
- Identificar cualquier riesgo o dependencia no contemplada
- Aprobar la continuación al siguiente agente, o solicitar cambios
"""

    # Tabla de artefactos (placeholder — en uso real vendrá de outputs del workflow)
    artifacts_table = """| Artefacto | Tipo | Ubicación |
|-----------|------|-----------|
| Workflow output | Markdown | `_checkpoint_artifacts/{workflow_id}_output.md` |
| Decision log | YAML | `_checkpoint_artifacts/{workflow_id}_decision.yaml` |"""

    block = f"""---
## ⏸️ CHECKPOINT DE APROBACIÓN HUMANA

**Workflow:** {workflow_id}
**Checkpoint:** {checkpoint_name}
**Índice:** {checkpoint_index}

### ¿Qué se ha completado hasta aquí?
{work_completed.strip()}

### ¿Qué se necesita revisar?
{review_scope.strip()}

### Artefactos para revisión
{artifacts_table}

### Opciones de respuesta

- ✅ **Aprobar** — el workflow continúa al siguiente agente
- 🔄 **Solicitar cambios** — indicar qué debe revisarse/corregirse antes de continuar
- ❌ **Rechazar** — el workflow se detiene y se registra el motivo

**El workflow permanece en pausa hasta recibir respuesta explícita.**

---
"""
    return block


def generate_decision_log_yaml(
    workflow_id: str,
    checkpoint_name: str,
    checkpoint_index: int
) -> str:
    """
    Genera la estructura YAML para registrar la decisión del humano.

    Se usará como template — el revisor lo completará con su decisión.
    """

    log = f"""# [IA-GEN] Registro de decisión — Generado por APB AI Framework (apb-orch-human-checkpoint-v1.0)
# Pendiente de validación humana

checkpoint_log:
  workflow: "{workflow_id}"
  checkpoint: "{checkpoint_name}"
  checkpoint_index: {checkpoint_index}
  timestamp_pause: "{{ ISO 8601 — completar }}"
  timestamp_response: "{{ ISO 8601 — completar }}"
  decision: "{{ approved | changes_requested | rejected }}"
  reviewer: "{{ nombre/rol del revisor }}"
  notes: "{{ observaciones (si aplica) }}"
  artifacts_reviewed:
    - "{{ artefacto-1 }}"
    - "{{ artefacto-2 }}"
"""
    return log


def main():
    parser = argparse.ArgumentParser(
        description="PoC de orquestación con checkpoints de aprobación humana"
    )
    parser.add_argument(
        "--workflow",
        type=str,
        required=True,
        help="ID del workflow (ej. apb-wf-sdd-full-v1.0)"
    )
    parser.add_argument(
        "--checkpoint",
        type=int,
        default=1,
        help="Índice del checkpoint a generar (default: 1). Si no se especifica, genera todos."
    )
    parser.add_argument(
        "--output",
        type=str,
        choices=["checkpoint", "decision-log", "both"],
        default="both",
        help="Qué generar: solo checkpoint, solo decision-log, o ambos (default: both)"
    )

    args = parser.parse_args()

    # Cargar workflow
    metadata, content, found = load_workflow(args.workflow)
    if not found:
        print(f"❌ ERROR: Workflow '{args.workflow}' no encontrado en workflows/", file=sys.stderr)
        return 1

    # Extraer human_checkpoints del frontmatter
    human_checkpoints = metadata.get("human_checkpoints", [])
    if not human_checkpoints:
        print(f"⚠️ AVISO: Workflow '{args.workflow}' no declara human_checkpoints en frontmatter")
        return 1

    # Extraer agents para contexto
    agents = metadata.get("agents", [])

    print(f"📋 Workflow: {args.workflow}")
    print(f"✓ Human checkpoints encontrados: {len(human_checkpoints)}")
    print(f"✓ Agentes: {len(agents)}")
    print()

    # Generar checkpoints
    if args.checkpoint > 0:
        # Generar un checkpoint específico
        if args.checkpoint > len(human_checkpoints):
            print(
                f"❌ ERROR: Checkpoint #{args.checkpoint} no existe. "
                f"El workflow tiene {len(human_checkpoints)} checkpoint(s)",
                file=sys.stderr
            )
            return 1

        checkpoint_name = human_checkpoints[args.checkpoint - 1]

        if args.output in ["checkpoint", "both"]:
            block = generate_checkpoint_block(
                args.workflow,
                checkpoint_name,
                args.checkpoint,
                agents
            )
            print(block)

        if args.output in ["decision-log", "both"]:
            log = generate_decision_log_yaml(
                args.workflow,
                checkpoint_name,
                args.checkpoint
            )
            print(log)
    else:
        # Generar todos los checkpoints
        for idx, checkpoint_name in enumerate(human_checkpoints, start=1):
            block = generate_checkpoint_block(
                args.workflow,
                checkpoint_name,
                idx,
                agents
            )
            print(block)
            if args.output in ["decision-log", "both"]:
                log = generate_decision_log_yaml(args.workflow, checkpoint_name, idx)
                print(log)

    return 0


if __name__ == "__main__":
    sys.exit(main())
