#!/usr/bin/env python3
"""
enforce_autonomy_limits.py — Gap B3 de enforcement de autonomía (SYSTEM.md §5.1).

Salvaguarda DOCUMENTAL, no de runtime: este repo son metadatos/documentación,
no ejecuta el código de los agentes. Este script recorre el cuerpo Markdown de
cada agent/subagent y avisa (WARNING, no ERROR — no forma parte de
`validate_repo.py --strict`) si el propio documento describe, en un ejemplo de
uso o instrucción, una acción de la tabla de "Límites Hardcoded por Nivel"
(SYSTEM.md §5.1) sin matización humana cercana ("aprobación", "checkpoint
humano", "human_review"), dado el autonomy_level que declara.

No sustituye el enforcement real de runtime — eso es responsabilidad del
futuro APB Agents MCP Server (ver discovery/PLAN_MCP_SERVER_APB.md, bloqueado
hoy por MCP-1). Es, en cambio, una comprobación de coherencia: ¿el agente se
documenta a sí mismo haciendo algo que su propio nivel prohíbe?

Uso:
    python scripts/enforce_autonomy_limits.py [--repo-path RUTA]
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List

sys.path.insert(0, str(Path(__file__).parent))
from validate_repo import parse_frontmatter, iter_component_files, FRONTMATTER_PATTERN  # noqa: E402

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# patrón: nivel mínimo de autonomía por debajo del cual está prohibido
# describir la acción sin matización humana cercana. Un valor de 5 significa
# "nunca permitido, ni en Nivel 4".
FORBIDDEN_PATTERNS_BY_MIN_LEVEL: Dict[str, int] = {
    r"push\s+.*--force.*\bmain\b": 5,
    r"git push --force": 4,
    r"despliegu?e?\s+a\s+producci[oó]n": 4,
    r"eliminar?\s+(recursos?|base[s]?\s+de\s+datos|storage)\s+de\s+producci[oó]n": 4,
    r"modificar\s+(IAM|permisos|roles?\s+de\s+acceso)": 4,
    r"aprobar\s+su\s+propio\s+pull\s+request": 5,
}

NEARBY_MITIGATION_PATTERN = re.compile(
    r"aprobaci[oó]n|checkpoint humano|human_review|revisi[oó]n humana",
    re.IGNORECASE,
)

CONTEXT_WINDOW_CHARS = 150


def extract_body(content: str) -> str:
    """Devuelve el cuerpo Markdown tras el frontmatter (o el contenido
    completo si no hay frontmatter detectable)."""
    match = FRONTMATTER_PATTERN.match(content)
    if not match:
        return content
    return content[match.end():]


def check_component(filepath: Path, repo_path: Path) -> List[str]:
    content = filepath.read_text(encoding="utf-8")
    metadata, found = parse_frontmatter(content)
    if not found:
        return []

    level = metadata.get("autonomy_level")
    if not isinstance(level, int):
        return []

    body = extract_body(content)
    rel_path = str(filepath.relative_to(repo_path))
    findings = []

    for pattern, min_level_required in FORBIDDEN_PATTERNS_BY_MIN_LEVEL.items():
        for match in re.finditer(pattern, body, re.IGNORECASE):
            window_start = max(0, match.start() - CONTEXT_WINDOW_CHARS)
            nearby = body[window_start: match.end() + CONTEXT_WINDOW_CHARS]
            if NEARBY_MITIGATION_PATTERN.search(nearby):
                continue
            if level < min_level_required:
                findings.append(
                    f"{rel_path}: menciona '{match.group()}' sin matización humana "
                    f"cercana, pero autonomy_level={level} (< {min_level_required} "
                    f"requerido por SYSTEM.md §5.1)."
                )

    return findings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-path", default=".", help="Ruta raíz del repositorio")
    args = parser.parse_args()

    repo_path = Path(args.repo_path).resolve()
    all_findings: List[str] = []

    for folder in ("agents", "subagents"):
        folder_path = repo_path / folder
        if not folder_path.exists():
            continue
        for filepath in iter_component_files(folder_path):
            all_findings.extend(check_component(filepath, repo_path))

    print("=" * 70)
    print("  Enforcement documental de límites de autonomía (SYSTEM.md §5.1)")
    print("=" * 70)

    if not all_findings:
        print("\n✅ Sin hallazgos — ningún agente/subagente describe una acción "
              "prohibida para su nivel sin matización humana cercana.")
        return 0

    print(f"\n⚠️  {len(all_findings)} hallazgo(s) (WARNING — no bloqueante):\n")
    for finding in all_findings:
        print(f"   • {finding}")

    print("\nNota: esto es una salvaguarda documental, no enforcement de "
          "runtime. Revisar manualmente cada hallazgo — puede ser un falso "
          "positivo de un match textual sin contexto suficiente.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
