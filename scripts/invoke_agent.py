#!/usr/bin/env python3
"""
APB AI Framework — Invocador de Agentes

Lee dinámicamente el frontmatter YAML real de agents/ y workflows/ — no
mantiene catálogos hardcodeados. Esto garantiza que --list y --list-workflows
siempre reflejan el estado real del repositorio, sin riesgo de desincronización
con catalog/CATALOG.md o INDEX.md (que se generan desde la misma fuente vía
scripts/generate_catalog.py).
"""

import argparse
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML no está instalado. Ejecute: pip install pyyaml")
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parent.parent
FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def load_frontmatter(filepath: Path):
    content = filepath.read_text(encoding="utf-8")
    m = FRONTMATTER.match(content)
    if not m:
        return None
    try:
        data = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return None
    return data if isinstance(data, dict) else None


def load_agents():
    agents = {}
    for f in sorted((REPO_ROOT / "agents").glob("*.md")):
        data = load_frontmatter(f)
        if data and data.get("id"):
            agents[data["id"]] = data
    return agents


def load_workflows():
    workflows = {}
    for f in sorted((REPO_ROOT / "workflows").glob("*.md")):
        data = load_frontmatter(f)
        if data and data.get("id"):
            workflows[data["id"]] = data
    return workflows


def list_agents():
    agents = load_agents()
    print(f"\n📋 Agentes disponibles ({len(agents)}):\n")
    for agent_id, agent in agents.items():
        print(f"  {agent_id} — {agent.get('name', '?')}")
        print(f"    Skills: {', '.join(agent.get('skills', []) or ['(ninguna registrada)'])}")
        print(f"    Runtime: {', '.join(agent.get('runtime', []) or ['?'])}")
        print()


def list_workflows():
    workflows = load_workflows()
    print(f"\n🔀 Workflows disponibles ({len(workflows)}):\n")
    for wf_id, wf in workflows.items():
        print(f"  {wf_id} — {wf.get('name', '?')}")
        print(f"    Agentes: {', '.join(wf.get('agents', []) or ['(ninguno registrado)'])}")
        print()


def invoke_agent(agent_id, inputs, runtime="copilot"):
    agents = load_agents()
    if agent_id not in agents:
        print(f"❌ Agente '{agent_id}' no encontrado en agents/.")
        print(f"   Use --list para ver los {len(agents)} agentes disponibles.")
        return 1
    agent = agents[agent_id]
    supported_runtimes = agent.get("runtime", [])
    if runtime not in supported_runtimes:
        print(f"⚠️ Runtime '{runtime}' no soportado por este agente. Soportados: {supported_runtimes}")
        return 1
    print(f"\n🚀 {agent.get('name', '?')} ({agent_id})")
    print(f"   Runtime: {runtime}")
    print(f"   Skills disponibles: {', '.join(agent.get('skills', []))}")
    print(f"   Puntos de validación humana: {agent.get('human_review_points', [])}")
    print(f"   Inputs: {json.dumps(inputs, indent=2, ensure_ascii=False)}")
    print("\n   ⚠️ Este script es un simulador de invocación para pruebas locales.")
    print("   No ejecuta el agente real; consulte el archivo del agente para el prompt completo.")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Invocador de Agentes APB AI Framework")
    parser.add_argument("--list", action="store_true", help="Lista agentes")
    parser.add_argument("--list-workflows", action="store_true", help="Lista workflows")
    parser.add_argument("--agent", type=str, help="ID del agente (debe incluir sufijo -vX.Y)")
    parser.add_argument("--input", type=str, help="JSON de inputs")
    parser.add_argument("--runtime", type=str, default="copilot", choices=["copilot", "claude"])
    args = parser.parse_args()

    if args.list:
        list_agents()
        return 0
    if args.list_workflows:
        list_workflows()
        return 0
    if args.agent:
        inputs = json.loads(args.input) if args.input else {}
        return invoke_agent(args.agent, inputs, args.runtime)
    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
