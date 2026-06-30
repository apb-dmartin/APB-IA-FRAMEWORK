#!/usr/bin/env python3
"""
inject_knowledge_context.py
===========================
Inyecta la referencia a prov-apb-knowledge-v1.0 en TODOS los ficheros de
skills (skills/apb-owned/**/*.md) y agents (agents/*.md) que aún no la tienen.

Dos acciones por fichero:
  1. Frontmatter — añade prov-apb-knowledge-v1.0 a `depends_on` si no está.
  2. Sección de contexto — si el fichero tiene sección de system prompt, inyecta
     el bloque APB al inicio del prompt; si no tiene, añade una sección
     "## Contexto Corporativo APB" tras el título H1.

Uso:
  python scripts/inject_knowledge_context.py [--dry-run] [--path <ruta>]

Opciones:
  --dry-run   Muestra qué cambiaría sin escribir nada.
  --path      Limita la ejecución a un directorio o fichero concreto.

El script es idempotente: ejecutarlo dos veces no duplica el bloque.
"""

import argparse
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent

PROVIDER_ID = "prov-apb-knowledge-v1.0"

# Bloque compacto que se inyecta en el system prompt (cuando existe)
PROMPT_BLOCK = """\
## Contexto Corporativo APB
Antes de ejecutar cualquier tarea, carga:
  context/apb/knowledge/APB_KNOWLEDGE_BASE.md  (provider: prov-apb-knowledge-v1.0)

Contiene: negocio portuario (escalas, atraques, tasas, EDI), catálogo de
aplicaciones, integraciones (PORTIC, AGE, AIS, VTS), terminología CA/ES/EN
y mapa de equipos/proyectos Jira.

GUARDRAIL: el legacy (SÒSTRAT/Java/Oracle/CAS/Alfresco) es contexto informacional.
Nunca prescribas tecnologías no aprobadas. Stack aprobado: STANDARD_ARCHITECTURE.md

"""

# Sección independiente para ficheros SIN system prompt
CONTEXT_SECTION = """\
## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

"""

# Patrones que identifican una sección de system prompt
PROMPT_HEADING_RE = re.compile(
    r"^(#{1,3})\s.*(?:Prompt\s+de\s+Sistema|Prompt\s+del\s+Sistema|System\s+Prompt)",
    re.IGNORECASE | re.MULTILINE,
)

# Marcador de idempotencia — si está en el fichero, no tocamos nada
IDEMPOTENCE_MARKER = "prov-apb-knowledge-v1.0"

# ---------------------------------------------------------------------------
# Helpers de frontmatter
# ---------------------------------------------------------------------------

def split_frontmatter(text: str) -> tuple[str, str]:
    """Devuelve (frontmatter_block, body) o ('', text) si no hay frontmatter."""
    if not text.startswith("---"):
        return "", text
    end = text.find("\n---", 3)
    if end == -1:
        return "", text
    fm = text[: end + 4]   # incluye el cierre ---
    body = text[end + 4 :]
    return fm, body


def add_depends_on(frontmatter: str) -> tuple[str, bool]:
    """
    Añade prov-apb-knowledge-v1.0 a la lista depends_on del frontmatter YAML.
    Si depends_on no existe, la crea. Devuelve (nuevo_fm, modificado).
    """
    if IDEMPOTENCE_MARKER in frontmatter:
        return frontmatter, False

    # depends_on ya existe — añadir línea
    depends_re = re.compile(r"^(depends_on:\s*\n(?:  - .+\n)*)", re.MULTILINE)
    m = depends_re.search(frontmatter)
    if m:
        insertion = f'  - "{PROVIDER_ID}"  # Contexto corporativo APB\n'
        new_fm = frontmatter[: m.end()] + insertion + frontmatter[m.end() :]
        return new_fm, True

    # depends_on no existe — insertarlo antes del cierre ---
    close_pos = frontmatter.rfind("\n---")
    if close_pos == -1:
        return frontmatter, False
    new_block = f'\ndepends_on:\n  - "{PROVIDER_ID}"  # Contexto corporativo APB\n'
    new_fm = frontmatter[:close_pos] + new_block + frontmatter[close_pos:]
    return new_fm, True


# ---------------------------------------------------------------------------
# Inyección en el cuerpo
# ---------------------------------------------------------------------------

def inject_in_prompt(body: str) -> tuple[str, bool]:
    """
    Si hay sección de system prompt, inyecta PROMPT_BLOCK justo después del
    primer ``` del bloque de código del prompt. Idempotente.
    """
    if IDEMPOTENCE_MARKER in body:
        return body, False

    m = PROMPT_HEADING_RE.search(body)
    if not m:
        return body, False

    # Buscar el primer ``` después del heading
    fence_pos = body.find("\n```", m.end())
    if fence_pos == -1:
        return body, False

    # Insertar el bloque tras el fence de apertura (salto de línea incluido)
    insert_at = fence_pos + 4  # después de '\n```'
    # Si hay un salto de línea justo después, lo saltamos
    if body[insert_at : insert_at + 1] == "\n":
        insert_at += 1

    new_body = body[:insert_at] + PROMPT_BLOCK + body[insert_at:]
    return new_body, True


def inject_context_section(body: str) -> tuple[str, bool]:
    """
    Para ficheros SIN system prompt, añade la sección CONTEXT_SECTION
    justo después del título H1 (primera línea que empieza con '# ').
    Si no hay H1, lo añade al principio. Idempotente.
    """
    if IDEMPOTENCE_MARKER in body:
        return body, False

    h1_re = re.compile(r"^# .+\n", re.MULTILINE)
    m = h1_re.search(body)
    if m:
        insert_at = m.end()
        # Mantener línea en blanco entre H1 y la sección si ya la hay
        if body[insert_at : insert_at + 1] == "\n":
            insert_at += 1
        new_body = body[:insert_at] + "\n" + CONTEXT_SECTION + body[insert_at:]
    else:
        new_body = CONTEXT_SECTION + body

    return new_body, True


# ---------------------------------------------------------------------------
# Procesamiento por fichero
# ---------------------------------------------------------------------------

def process_file(path: Path, dry_run: bool) -> dict:
    """Procesa un fichero. Devuelve un dict con el resultado."""
    text = path.read_text(encoding="utf-8")
    result = {"path": str(path.relative_to(REPO_ROOT)), "changes": []}

    # Idempotencia global
    if IDEMPOTENCE_MARKER in text:
        result["status"] = "skip"
        return result

    fm, body = split_frontmatter(text)

    new_fm, fm_changed = add_depends_on(fm) if fm else (fm, False)
    if fm_changed:
        result["changes"].append("frontmatter: depends_on añadido")

    # ¿Tiene system prompt?
    has_prompt = bool(PROMPT_HEADING_RE.search(body))
    if has_prompt:
        new_body, body_changed = inject_in_prompt(body)
        if body_changed:
            result["changes"].append("system prompt: bloque APB inyectado")
    else:
        new_body, body_changed = inject_context_section(body)
        if body_changed:
            result["changes"].append("sección Contexto Corporativo APB añadida")

    if not fm_changed and not body_changed:
        result["status"] = "skip"
        return result

    new_text = new_fm + new_body
    result["status"] = "dry_run" if dry_run else "updated"

    if not dry_run:
        path.write_text(new_text, encoding="utf-8")

    return result


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true",
                        help="Muestra cambios sin escribir nada")
    parser.add_argument("--path", type=Path, default=None,
                        help="Limita la ejecución a este directorio o fichero")
    args = parser.parse_args()

    if args.path:
        root = args.path if args.path.is_absolute() else REPO_ROOT / args.path
        if root.is_file():
            targets = [root]
        else:
            targets = list(root.rglob("*.md"))
    else:
        targets = (
            list((REPO_ROOT / "skills" / "apb-owned").rglob("*.md"))
            + list((REPO_ROOT / "agents").glob("*.md"))
        )

    updated, skipped, errors = 0, 0, 0

    for path in sorted(targets):
        try:
            res = process_file(path, args.dry_run)
            if res["status"] in ("updated", "dry_run"):
                tag = "[DRY-RUN]" if args.dry_run else "[OK]"
                print(f"{tag} {res['path']}: {', '.join(res['changes'])}")
                updated += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"[ERROR] {path}: {e}", file=sys.stderr)
            errors += 1

    print(f"\n--- Resumen ---")
    print(f"  Ficheros modificados : {updated}")
    print(f"  Ficheros sin cambios : {skipped}")
    print(f"  Errores              : {errors}")
    if args.dry_run:
        print("\n  (Modo dry-run: no se ha escrito ningún fichero)")


if __name__ == "__main__":
    main()
