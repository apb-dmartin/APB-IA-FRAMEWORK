#!/usr/bin/env python3
"""
generate_test_plan_html.py — Genera la versión HTML de un plan de pruebas /
informe de ejecución Markdown conforme a TEST_PLAN_STANDARD (§7.1: entrega
dual Markdown + HTML).

Produce un HTML autocontenido y portable:
  - Cabecera azul corporativa APB (--azul-corporativo #046DB2) + logo.
  - Menú de navegación lateral (ancla a cada sección ## y a cada bloque "### Bloque …").
  - Acordeón nativo (<details>/<summary>, sin DevExpress ni CDN) para cada
    "### Bloque …" — el primero se muestra abierto.
  - Los assets de logo se copian junto al HTML de salida (carpeta assets/).

Sin dependencias externas (no usa CDN, no requiere `pip install markdown`):
implementa un conversor Markdown→HTML mínimo para el subconjunto de sintaxis
usado en los documentos de TEST_PLAN_STANDARD (encabezados ATX, párrafos,
citas '>', tablas con pipes, bloques de código ```, negrita/código en línea,
listas, enlaces, líneas horizontales).

Uso:
    python scripts/generate_test_plan_html.py docs/qa/examples/QA_TRU_TruckCenter_UNIFICADO.md
    python scripts/generate_test_plan_html.py <plan.md> -o <salida.html>
"""

import argparse
import html
import re
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LOGO_SRC = REPO_ROOT / "design-system" / "assets" / "logo-horizontal-blanco.png"

AZUL_CORPORATIVO = "#046DB2"
AZUL_HOVER = "#035A95"

BLOCK_HEADING_RE = re.compile(r"^Bloque\b", re.IGNORECASE)


def slugify(text: str) -> str:
    text = re.sub(r"[`*_]", "", text)
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"[\s_]+", "-", text).strip("-")
    return text or "seccion"


def md_inline(text: str) -> str:
    """Convierte inline markdown (negrita, código, enlaces) a HTML, escapando el resto."""
    out = []
    i = 0
    n = len(text)
    while i < n:
        if text[i] == "`":
            j = text.find("`", i + 1)
            if j != -1:
                out.append(f"<code>{html.escape(text[i + 1:j])}</code>")
                i = j + 1
                continue
        if text[i:i + 2] == "**":
            j = text.find("**", i + 2)
            if j != -1:
                out.append(f"<strong>{md_inline(text[i + 2:j])}</strong>")
                i = j + 2
                continue
        if text[i] == "[":
            m = re.match(r"\[([^\]]*)\]\(([^)]*)\)", text[i:])
            if m:
                out.append(f'<a href="{html.escape(m.group(2))}">{html.escape(m.group(1))}</a>')
                i += m.end()
                continue
        out.append(html.escape(text[i]))
        i += 1
    return "".join(out)


# Estados de decisión/ejecución → badge de color (acta de aprobación §6.2, columna Estado).
STATUS_CLASS = {
    "aprobado": "ok",
    "pass": "ok",
    "ok": "ok",
    "rechazado": "ko",
    "fail": "ko",
    "con reservas": "warn",
    "aprobado-con-reservas": "warn",
    "pendiente": "pend",
    "pendiente-aprobación": "pend",
    "pendiente-aprobacion": "pend",
}


def cell_html(c: str) -> str:
    """HTML de una celda de datos; envuelve los estados conocidos en un badge de color."""
    key = c.strip().lower().strip("`")
    inner = md_inline(c)
    cls = STATUS_CLASS.get(key)
    if cls:
        return f'<span class="badge badge-{cls}">{inner}</span>'
    return inner


def render_table(lines):
    header = [c.strip() for c in lines[0].strip().strip("|").split("|")]
    rows = [
        [c.strip() for c in line.strip().strip("|").split("|")]
        for line in lines[2:]
    ]
    out = ['<div class="table-wrap"><table>', "<thead><tr>"]
    for h in header:
        out.append(f"<th>{md_inline(h)}</th>")
    out.append("</tr></thead><tbody>")
    for row in rows:
        out.append("<tr>")
        for c in row:
            out.append(f"<td>{cell_html(c)}</td>")
        out.append("</tr>")
    out.append("</tbody></table></div>")
    return "\n".join(out)


def render_body(lines):
    """Renderiza un bloque de líneas markdown (sin encabezados) a HTML."""
    html_parts = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            i += 1
            continue
        if stripped.startswith("```"):
            j = i + 1
            code_lines = []
            while j < n and not lines[j].strip().startswith("```"):
                code_lines.append(lines[j])
                j += 1
            html_parts.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>")
            i = j + 1
            continue
        if re.match(r"^-{3,}\s*$", stripped):
            html_parts.append("<hr>")
            i += 1
            continue
        if stripped.startswith("|") and i + 1 < n and re.match(r"^\|?[\s:|-]+\|?$", lines[i + 1].strip()):
            j = i
            table_lines = []
            while j < n and lines[j].strip().startswith("|"):
                table_lines.append(lines[j])
                j += 1
            html_parts.append(render_table(table_lines))
            i = j
            continue
        if stripped.startswith(">"):
            j = i
            quote_lines = []
            while j < n and lines[j].strip().startswith(">"):
                quote_lines.append(re.sub(r"^\s*>\s?", "", lines[j]))
                j += 1
            inner = render_body(quote_lines)
            html_parts.append(f"<blockquote>{inner}</blockquote>")
            i = j
            continue
        if re.match(r"^[-*]\s+", stripped):
            j = i
            items = []
            while j < n and re.match(r"^[-*]\s+", lines[j].strip()):
                items.append(re.sub(r"^[-*]\s+", "", lines[j].strip()))
                j += 1
            html_parts.append(
                "<ul>" + "".join(f"<li>{md_inline(it)}</li>" for it in items) + "</ul>"
            )
            i = j
            continue
        if re.match(r"^\d+\.\s+", stripped):
            j = i
            items = []
            while j < n and re.match(r"^\d+\.\s+", lines[j].strip()):
                items.append(re.sub(r"^\d+\.\s+", "", lines[j].strip()))
                j += 1
            html_parts.append(
                "<ol>" + "".join(f"<li>{md_inline(it)}</li>" for it in items) + "</ol>"
            )
            i = j
            continue
        # párrafo: agrupa líneas consecutivas no vacías
        j = i
        para_lines = []
        while j < n and lines[j].strip() and not lines[j].strip().startswith(("|", ">", "```", "#")):
            para_lines.append(lines[j].strip())
            j += 1
        if para_lines:
            html_parts.append(f"<p>{md_inline(' '.join(para_lines))}</p>")
            i = j
        else:
            i += 1
    return "\n".join(html_parts)


class Node:
    def __init__(self, level, title, anchor):
        self.level = level
        self.title = title
        self.anchor = anchor
        self.body_lines = []
        self.children = []
        self.is_block = level == 3 and bool(BLOCK_HEADING_RE.match(title))


def parse_markdown(text: str):
    lines = text.splitlines()
    root = Node(1, "root", "root")
    stack = [root]
    doc_title = None
    for line in lines:
        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            if level == 1 and doc_title is None:
                doc_title = title
                continue
            anchor = slugify(title)
            node = Node(level, title, anchor)
            while stack and stack[-1].level >= level:
                stack.pop()
            stack[-1].children.append(node)
            stack.append(node)
        else:
            if stack[-1] is root:
                root.body_lines.append(line)
            else:
                stack[-1].body_lines.append(line)
    return doc_title or "Documento", root


def render_node(node: Node, first_block_flag: list) -> str:
    body_html = render_body(node.body_lines)
    children_html = "".join(render_node(c, first_block_flag) for c in node.children)
    if node.is_block:
        open_attr = ""
        if not first_block_flag[0]:
            open_attr = " open"
            first_block_flag[0] = True
        return (
            f'<details class="block" id="{node.anchor}"{open_attr}>'
            f"<summary>{md_inline(node.title)}</summary>"
            f'<div class="block-body">{body_html}{children_html}</div>'
            f"</details>"
        )
    tag = {1: "h1", 2: "h2", 3: "h3", 4: "h4"}.get(node.level, "h4")
    heading = f'<{tag} id="{node.anchor}">{md_inline(node.title)}</{tag}>' if node.level > 1 else ""
    return f"{heading}{body_html}{children_html}"


def build_nav(root: Node) -> str:
    items = []
    for section in root.children:
        if section.level != 2:
            continue
        sub_items = [c for c in section.children if c.is_block]
        sub_html = ""
        if sub_items:
            sub_html = "<ul>" + "".join(
                f'<li><a href="#{b.anchor}">{html.escape(b.title)}</a></li>' for b in sub_items
            ) + "</ul>"
        items.append(
            f'<li><a href="#{section.anchor}">{html.escape(section.title)}</a>{sub_html}</li>'
        )
    return "<ul>" + "".join(items) + "</ul>"


def generate_html(md_path: Path, out_path: Path):
    text = md_path.read_text(encoding="utf-8")
    doc_title, root = parse_markdown(text)

    nav_html = build_nav(root)
    first_block_flag = [False]
    body_html = "".join(render_node(c, first_block_flag) for c in root.children)
    intro_html = render_body(root.body_lines)

    out_dir = out_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    assets_dir = out_dir / "assets"
    assets_dir.mkdir(exist_ok=True)
    logo_rel = "assets/logo-horizontal-blanco.png"
    if LOGO_SRC.exists():
        shutil.copy(LOGO_SRC, assets_dir / LOGO_SRC.name)

    css = f"""
    :root {{
      --azul-corporativo: {AZUL_CORPORATIVO};
      --azul-corporativo-hover: {AZUL_HOVER};
      --gris-oscuro-texto: #3C495A;
      --gris-medio: #7A8DA4;
      --gris-claro: #D5DBE5;
      --gris-muy-claro: #E3E9F4;
      --gris-fondo: #F7F9FC;
      --blanco: #FFFFFF;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0; font-family: Calibri, "Segoe UI", Arial, sans-serif;
      color: var(--gris-oscuro-texto); background: var(--gris-fondo);
    }}
    header.apb-header {{
      background: var(--azul-corporativo); color: #fff; padding: 12px 24px;
      display: flex; align-items: center; gap: 16px; position: sticky; top: 0; z-index: 10;
    }}
    header.apb-header img {{ height: 32px; }}
    header.apb-header h1 {{ font-size: 16px; margin: 0; font-weight: 600; }}
    .layout {{ display: flex; min-height: 100vh; }}
    nav.sidebar {{
      width: 280px; min-width: 280px; background: #fff; border-right: 1px solid var(--gris-claro);
      padding: 16px; overflow-y: auto; max-height: calc(100vh - 56px); position: sticky; top: 56px;
      align-self: flex-start;
    }}
    nav.sidebar > ul {{ list-style: none; margin: 0; padding: 0; }}
    nav.sidebar ul ul {{ list-style: none; margin: 2px 0 8px 12px; padding: 0; }}
    nav.sidebar li {{ margin: 4px 0; font-size: 13px; }}
    nav.sidebar a {{ color: var(--gris-oscuro-texto); text-decoration: none; }}
    nav.sidebar a:hover {{ color: var(--azul-corporativo); text-decoration: underline; }}
    main {{ flex: 1; padding: 24px 32px; max-width: 1100px; }}
    h1, h2, h3, h4 {{ color: var(--gris-oscuro-texto); }}
    h2 {{ border-bottom: 2px solid var(--azul-corporativo); padding-bottom: 6px; margin-top: 36px; }}
    h3 {{ margin-top: 24px; }}
    details.block {{
      background: #fff; border: 1px solid var(--gris-claro); border-radius: 6px;
      margin: 12px 0; padding: 0;
    }}
    details.block > summary {{
      cursor: pointer; padding: 10px 16px; font-weight: 600; color: #fff;
      background: var(--azul-corporativo); border-radius: 6px 6px 0 0; list-style: none;
    }}
    details.block[open] > summary {{ border-radius: 6px 6px 0 0; }}
    details.block > summary::-webkit-details-marker {{ display: none; }}
    details.block > summary::before {{ content: "▸ "; }}
    details.block[open] > summary::before {{ content: "▾ "; }}
    .block-body {{ padding: 12px 16px; }}
    .table-wrap {{ overflow-x: auto; margin: 12px 0; }}
    table {{ border-collapse: collapse; width: 100%; font-size: 13px; }}
    th, td {{ border: 1px solid var(--gris-claro); padding: 6px 10px; text-align: left; vertical-align: top; }}
    th {{ background: var(--gris-muy-claro); color: var(--gris-oscuro-texto); }}
    tr:nth-child(even) td {{ background: #FAFBFD; }}
    blockquote {{
      border-left: 4px solid var(--azul-corporativo); background: var(--gris-muy-claro);
      margin: 12px 0; padding: 8px 16px; color: var(--gris-medio); font-size: 13px;
    }}
    .badge {{ display: inline-block; padding: 1px 8px; border-radius: 10px; font-size: 12px; font-weight: 600; white-space: nowrap; }}
    .badge-ok {{ background: #DCF3E4; color: #1B7A3D; }}
    .badge-ko {{ background: #FBE0E0; color: #B12A2A; }}
    .badge-warn {{ background: #FCEFD3; color: #8A6100; }}
    .badge-pend {{ background: var(--gris-muy-claro); color: var(--gris-oscuro-texto); }}
    code {{ background: var(--gris-muy-claro); padding: 1px 5px; border-radius: 3px; font-size: 12px; }}
    pre {{ background: #2b2b2b; color: #eee; padding: 12px; border-radius: 6px; overflow-x: auto; }}
    pre code {{ background: transparent; color: inherit; }}
    footer.apb-footer {{
      text-align: center; font-size: 11px; color: var(--gris-medio); padding: 24px;
    }}
    """

    logo_img = f'<img src="{logo_rel}" alt="Port de Barcelona">' if LOGO_SRC.exists() else ""

    html_doc = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="Generado_Por_IA" content="Si">
<title>{html.escape(doc_title)}</title>
<style>{css}</style>
</head>
<body>
<header class="apb-header">
  {logo_img}
  <h1>{html.escape(doc_title)}</h1>
</header>
<div class="layout">
  <nav class="sidebar">{nav_html}</nav>
  <main>
    <div class="intro">{intro_html}</div>
    {body_html}
  </main>
</div>
<footer class="apb-footer">
  Generado por IA (APB AI Framework) — pendiente de validación humana. No distribuir sin revisión.
</footer>
</body>
</html>
"""
    out_path.write_text(html_doc, encoding="utf-8")
    return out_path


def main():
    parser = argparse.ArgumentParser(description="Genera el HTML de un plan/informe de pruebas APB")
    parser.add_argument("input", type=Path, help="Fichero Markdown de origen")
    parser.add_argument("-o", "--output", type=Path, default=None, help="Fichero HTML de salida")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"ERROR: no existe {args.input}")
        sys.exit(1)

    out_path = args.output or args.input.with_suffix(".html")
    result = generate_html(args.input, out_path)
    print(f"HTML generado: {result}")


if __name__ == "__main__":
    main()
