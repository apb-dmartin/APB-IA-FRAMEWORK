#!/usr/bin/env python3
"""
generate_catalog.py — Generador automático de catálogo, índice y registro
de dominios del APB AI Framework.

Lee el frontmatter YAML real de todos los componentes y regenera:
  - catalog/CATALOG.md
  - INDEX.md (sección de resumen y listados)
  - DOMAIN_REGISTRY.md (tabla de dominios con conteos reales)

Uso:
    python scripts/generate_catalog.py
    python scripts/generate_catalog.py --path /ruta/al/repo
    python scripts/generate_catalog.py --check   # no escribe, solo indica si hay drift (exit 1 si sí)

Este script es la única forma soportada de actualizar estos 3 documentos.
No editar sus secciones generadas a mano — los cambios se sobrescriben en
la siguiente ejecución.
"""

import sys
import argparse
import re
from pathlib import Path
from collections import defaultdict
from datetime import date

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML no está instalado. Ejecute: pip install pyyaml")
    sys.exit(1)

COMPONENT_FOLDERS = {
    "skills/apb-owned": "skill_apb",
    "skills/third_party": "skill_third",
    "agents": "agent",
    "subagents": "subagent",
    "workflows": "workflow",
    "providers": "provider",
    "wrappers": "wrapper",
    "adapters": "adapter",
}

DOMAIN_COLORS = {
    "development": "🔵", "qa": "🟢", "architecture": "🟣", "discovery": "🟡",
    "platform": "🟠", "security": "🔴", "governance": "⚫", "operation": "🔵",
    "documentation": "⚪", "orchestration": "🟤", "pm": "🟢", "design": "🎨",
}

FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
IGNORED_DIRS = {"templates", ".git", "node_modules"}


def load_component(filepath: Path, repo_path: Path):
    content = filepath.read_text(encoding="utf-8")
    m = FRONTMATTER.match(content)
    if not m:
        return None
    try:
        data = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return None
    if not isinstance(data, dict):
        return None
    data["_rel_path"] = str(filepath.relative_to(repo_path))
    return data


def collect_all(repo_path: Path):
    components = defaultdict(list)
    for folder, kind in COMPONENT_FOLDERS.items():
        folder_path = repo_path / folder
        if not folder_path.exists():
            continue
        for filepath in sorted(folder_path.rglob("*.md")):
            if any(part in IGNORED_DIRS for part in filepath.parts):
                continue
            data = load_component(filepath, repo_path)
            if data:
                components[kind].append(data)
    return components


def generate_catalog_md(components, repo_path: Path):
    today = date.today().isoformat()
    total = sum(len(v) for v in components.values())

    lines = [
        "# APB AI Framework — Component Catalog",
        "",
        "> Generado automáticamente por `scripts/generate_catalog.py`.",
        "> No editar a mano — los cambios se perderán en la siguiente ejecución.",
        "> Para añadir o modificar un componente, edite su archivo y vuelva a ejecutar el script.",
        "",
        "## Overview",
        f"- **Total Components**: {total}",
        f"- **Last Generated**: {today}",
        "",
        "## Component Breakdown",
        "",
    ]

    skill_apb = sorted(components["skill_apb"], key=lambda d: (d.get("domain", ""), d.get("id", "")))
    skill_third = sorted(components["skill_third"], key=lambda d: d.get("id", ""))

    lines.append(f"### Skills APB-Owned ({len(skill_apb)} total)")
    lines.append("")
    lines.append("| ID | Dominio | Estado | Archivo |")
    lines.append("|---|---|---|---|")
    for d in skill_apb:
        lines.append(f"| `{d.get('id','?')}` | {d.get('domain','?')} | {d.get('status','?')} | `{d['_rel_path']}` |")
    lines.append("")

    lines.append(f"### Skills de Terceros ({len(skill_third)} total)")
    lines.append("")
    lines.append("| ID | Fuente | Licencia | Estado | Archivo |")
    lines.append("|---|---|---|---|---|")
    for d in skill_third:
        source = d.get("source_repo", "?")
        lines.append(f"| `{d.get('id','?')}` | {source} | {d.get('source_license','?')} | {d.get('status','?')} | `{d['_rel_path']}` |")
    lines.append("")

    type_titles = {
        "agent": "Agentes", "subagent": "Subagentes", "workflow": "Workflows",
        "provider": "Providers", "wrapper": "Wrappers", "adapter": "Adapters",
    }
    for kind, title in type_titles.items():
        items = sorted(components[kind], key=lambda d: d.get("id", ""))
        lines.append(f"### {title} ({len(items)} total)")
        lines.append("")
        lines.append("| ID | Nombre | Estado | Archivo |")
        lines.append("|---|---|---|---|")
        for d in items:
            lines.append(f"| `{d.get('id','?')}` | {d.get('name','?')} | {d.get('status','?')} | `{d['_rel_path']}` |")
        lines.append("")

    return "\n".join(lines) + "\n"


def compute_domain_counts(components):
    domain_counts = defaultdict(int)
    for d in components["skill_apb"]:
        domain_counts[d.get("domain", "unknown")] += 1
    return domain_counts


def generate_domain_registry_table(domain_counts):
    domain_names = {
        "development": "Development", "qa": "Quality Assurance",
        "architecture": "Architecture", "discovery": "Discovery",
        "platform": "Platform", "security": "Security",
        "governance": "Governance", "operation": "Operation",
        "documentation": "Documentation", "orchestration": "Orchestration",
        "pm": "Project Management", "design": "Design & UX",
    }
    short_ids = {
        "development": "dev", "qa": "qa", "architecture": "arch", "discovery": "disc",
        "platform": "plat", "security": "sec", "governance": "gov", "operation": "ops",
        "documentation": "doc", "orchestration": "orch", "pm": "pm", "design": "design",
    }
    lines = ["| ID | Nombre | Skills | Color |", "|----|--------|--------|-------|"]
    for domain in domain_names:
        count = domain_counts.get(domain, 0)
        short = short_ids[domain]
        color = DOMAIN_COLORS.get(domain, "⚪")
        lines.append(f"| `{short}` | {domain_names[domain]} | {count} | {color} |")
    return "\n".join(lines)


def update_domain_registry(repo_path: Path, components, write: bool):
    path = repo_path / "DOMAIN_REGISTRY.md"
    content = path.read_text(encoding="utf-8")
    domain_counts = compute_domain_counts(components)
    new_table = generate_domain_registry_table(domain_counts)

    pattern = re.compile(r"\| ID \| Nombre \| Skills \| Color \|\n\|----\|--------\|--------\|-------\|\n(?:\|.*\n)+")
    if not pattern.search(content):
        return False, "No se encontró la tabla de dominios en DOMAIN_REGISTRY.md"
    new_content = pattern.sub(new_table + "\n", content, count=1)
    changed = new_content != content
    if write and changed:
        path.write_text(new_content, encoding="utf-8", newline="\n")
    return changed, None


def update_index_md(repo_path: Path, components, write: bool):
    path = repo_path / "INDEX.md"
    content = path.read_text(encoding="utf-8")
    today = date.today().isoformat()

    counts = {
        "Skills APB": len(components["skill_apb"]),
        "Skills terceros": len(components["skill_third"]),
        "Agentes": len(components["agent"]),
        "Subagentes": len(components["subagent"]),
        "Workflows": len(components["workflow"]),
        "Providers": len(components["provider"]),
        "Wrappers": len(components["wrapper"]),
        "Adaptadores": len(components["adapter"]),
    }
    total = sum(counts.values())

    summary_lines = ["| Métrica | Valor |", "|---------|-------|"]
    for k, v in counts.items():
        summary_lines.append(f"| {k} | {v} / {v} |")
    summary_lines.append(f"| **Total** | **{total}** |")
    new_summary = "\n".join(summary_lines)

    pattern = re.compile(r"\| Métrica \| Valor \|\n\|---------\|-------\|\n(?:\|.*\n)+")
    if not pattern.search(content):
        return False, "No se encontró la tabla de resumen en INDEX.md"
    new_content = pattern.sub(new_summary + "\n", content, count=1)

    date_pattern = re.compile(r"(> \*\*Fecha de actualización:\*\* )\S+")
    new_content = date_pattern.sub(rf"\g<1>{today}", new_content)

    domain_counts = compute_domain_counts(components)
    domain_table_lines = ["| Dominio | Cantidad | Patrón ID |", "|---------|----------|-----------|"]
    short_ids = {
        "development": "dev", "qa": "qa", "architecture": "arch", "discovery": "disc",
        "platform": "plat", "security": "sec", "governance": "gov", "operation": "ops",
        "documentation": "doc", "orchestration": "orch", "pm": "pm", "design": "design",
    }
    for domain, count in sorted(domain_counts.items(), key=lambda x: -x[1]):
        short = short_ids.get(domain, domain[:4])
        domain_table_lines.append(f"| {domain} | {count} | `apb-{short}-*` |")
    new_domain_table = "\n".join(domain_table_lines)

    skills_section_pattern = re.compile(
        r"## ✅ Skills APB por Dominio \(\d+\)\n\n\| Dominio \| Cantidad \| Patrón ID \|\n\|---------\|----------\|-----------\|\n(?:\|.*\n)+"
    )
    total_skills_apb = len(components["skill_apb"])
    new_section_header = f"## ✅ Skills APB por Dominio ({total_skills_apb})\n\n"
    if skills_section_pattern.search(new_content):
        new_content = skills_section_pattern.sub(new_section_header + new_domain_table + "\n", new_content, count=1)

    agent_ids = sorted(d.get("id", "").rsplit("-v", 1)[0] for d in components["agent"])
    agents_pattern = re.compile(r"## ✅ Agentes \(\d+\)\n\n`[^\n]+`\n")
    new_agents_line = f"## ✅ Agentes ({len(agent_ids)})\n\n" + ", ".join(f"`{a}`" for a in agent_ids) + "\n"
    if agents_pattern.search(new_content):
        new_content = agents_pattern.sub(new_agents_line, new_content, count=1)

    workflow_ids = sorted(d.get("id", "") for d in components["workflow"])
    workflows_pattern = re.compile(r"## ✅ Workflows \(\d+\)\n\n`[^\n]+`\n")
    new_workflows_line = f"## ✅ Workflows ({len(workflow_ids)})\n\n" + ", ".join(f"`{w}`" for w in workflow_ids) + "\n"
    if workflows_pattern.search(new_content):
        new_content = workflows_pattern.sub(new_workflows_line, new_content, count=1)

    # Actualizar comentarios de conteo dentro del árbol ASCII de estructura
    tree_replacements = [
        (re.compile(r"(agents/\s*+# )\d+( agentes)"), rf"\g<1>{len(components['agent'])}\g<2>"),
        (re.compile(r"(subagents/\s*+# )\d+( subagentes)"), rf"\g<1>{len(components['subagent'])}\g<2>"),
        (re.compile(r"(workflows/\s*+# )\d+( workflows)"), rf"\g<1>{len(components['workflow'])}\g<2>"),
        (re.compile(r"(apb-owned/\s*+# )\d+( skills)"), rf"\g<1>{len(components['skill_apb'])}\g<2>"),
        (re.compile(r"(third[-_]party/\s*+# )\d+( skills)"), rf"\g<1>{len(components['skill_third'])}\g<2>"),
        (re.compile(r"(providers/\s*+# )\d+( providers)"), rf"\g<1>{len(components['provider'])}\g<2>"),
        (re.compile(r"(wrappers/\s*+# )\d+( wrappers)"), rf"\g<1>{len(components['wrapper'])}\g<2>"),
        (re.compile(r"(adapters/\s*+# )\d+( adaptadores)"), rf"\g<1>{len(components['adapter'])}\g<2>"),
    ]
    for pattern, repl in tree_replacements:
        new_content = pattern.sub(repl, new_content)

    changed = new_content != content
    if write and changed:
        path.write_text(new_content, encoding="utf-8", newline="\n")
    return changed, None


def main():
    parser = argparse.ArgumentParser(description="Generador de catálogo del APB AI Framework")
    parser.add_argument("--path", type=str, default=".", help="Ruta al repositorio")
    parser.add_argument("--check", action="store_true", help="No escribir; salir con error si hay drift")
    args = parser.parse_args()

    repo_path = Path(args.path).resolve()
    components = collect_all(repo_path)
    total = sum(len(v) for v in components.values())
    print(f"Componentes escaneados: {total}")
    for kind, items in components.items():
        print(f"  {kind}: {len(items)}")

    write = not args.check

    new_catalog = generate_catalog_md(components, repo_path)
    catalog_path = repo_path / "catalog" / "CATALOG.md"
    old_catalog = catalog_path.read_text(encoding="utf-8") if catalog_path.exists() else ""
    catalog_changed = new_catalog != old_catalog
    if write:
        catalog_path.write_text(new_catalog, encoding="utf-8", newline="\n")

    index_changed, index_err = update_index_md(repo_path, components, write)
    domain_changed, domain_err = update_domain_registry(repo_path, components, write)

    print()
    print(f"catalog/CATALOG.md: {'actualizado' if catalog_changed else 'sin cambios'}")
    print(f"INDEX.md: {'actualizado' if index_changed else 'sin cambios'}" + (f" ({index_err})" if index_err else ""))
    print(f"DOMAIN_REGISTRY.md: {'actualizado' if domain_changed else 'sin cambios'}" + (f" ({domain_err})" if domain_err else ""))

    if args.check and (catalog_changed or index_changed or domain_changed):
        print("\nDRIFT DETECTADO: ejecute sin --check para regenerar.")
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
