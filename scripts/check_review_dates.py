#!/usr/bin/env python3
"""
check_review_dates.py — Detecta componentes con review_date vencido.

Recorre todos los componentes del repositorio, compara su 'review_date'
con la fecha actual y genera un listado de los que superan el umbral
de días indicado. Usado por la GitHub Action review-reminder.yml.

Uso:
    python scripts/check_review_dates.py --days 180
    python scripts/check_review_dates.py --days 180 --output stale.txt
    python scripts/check_review_dates.py --days 180 --path /ruta/repo
"""

import argparse
import sys
from datetime import date, datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML no instalado. Ejecutar: pip install pyyaml")
    sys.exit(1)

COMPONENT_FOLDERS = [
    "skills/apb-owned",
    "skills/third_party",
    "agents",
    "subagents",
    "workflows",
    "providers",
    "wrappers",
    "adapters",
]


def parse_frontmatter(content: str):
    if not content.startswith("---"):
        return None
    end = content.find("\n---", 3)
    if end == -1:
        return None
    try:
        return yaml.safe_load(content[3:end])
    except yaml.YAMLError:
        return None


def iter_md_files(folder: Path):
    if not folder.exists():
        return
    for f in sorted(folder.rglob("*.md")):
        if ".git" not in f.parts and "_templates" not in f.parts:
            yield f


def main():
    parser = argparse.ArgumentParser(description="Detecta componentes con review_date vencido")
    parser.add_argument("--days", type=int, default=180,
                        help="Umbral en días (default: 180)")
    parser.add_argument("--path", type=str, default=".",
                        help="Ruta al repositorio (default: .)")
    parser.add_argument("--output", type=str, default=None,
                        help="Fichero de salida (default: stdout)")
    args = parser.parse_args()

    repo = Path(args.path).resolve()
    today = date.today()
    stale = []

    for folder_rel in COMPONENT_FOLDERS:
        folder = repo / folder_rel
        for filepath in iter_md_files(folder):
            content = filepath.read_text(encoding="utf-8", errors="replace")
            meta = parse_frontmatter(content)
            if not meta or not isinstance(meta, dict):
                continue
            comp_id = meta.get("id")
            review_raw = meta.get("review_date")
            if not comp_id or not review_raw:
                continue
            try:
                if isinstance(review_raw, date):
                    review_dt = review_raw
                else:
                    review_dt = datetime.strptime(str(review_raw), "%Y-%m-%d").date()
            except ValueError:
                continue
            delta = (today - review_dt).days
            if delta >= args.days:
                rel = str(filepath.relative_to(repo))
                stale.append((delta, comp_id, rel, str(review_raw)))

    stale.sort(reverse=True)

    if not stale:
        output = ""
    else:
        lines = [
            f"## Componentes con `review_date` vencido (≥{args.days} días)\n",
            f"_Generado automáticamente — {today.isoformat()}_\n\n",
            f"| Días vencido | ID | Fichero | review_date |\n",
            f"|---|---|---|---|\n",
        ]
        for delta, comp_id, rel, rv in stale:
            lines.append(f"| {delta} | `{comp_id}` | `{rel}` | {rv} |\n")
        lines.append(f"\n**Total:** {len(stale)} componente(s) con revisión pendiente.\n")
        output = "".join(lines)

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"✅ {len(stale)} componente(s) vencido(s). Resultado en: {args.output}")
    else:
        if output:
            print(output)
        else:
            print(f"✅ Sin componentes vencidos (umbral: {args.days} días).")

    sys.exit(0)


if __name__ == "__main__":
    main()
