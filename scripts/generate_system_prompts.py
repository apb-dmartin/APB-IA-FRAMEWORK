#!/usr/bin/env python3
"""
generate_system_prompts.py
==========================
Genera e inyecta una sección "## Prompt de Sistema" en todos los ficheros de
skills (skills/apb-owned/**/*.md) y agents (agents/*.md) que aún no la tienen.

El prompt se construye a partir del contenido existente del fichero:
  - frontmatter: name, id, description, autonomy_level
  - secciones funcionales: Input, Proceso/Capacidades, Output, Restricciones

Uso:
  python scripts/generate_system_prompts.py [--dry-run] [--path <ruta>]

El script es idempotente: si un fichero ya tiene sección de system prompt, se salta.
"""

import argparse
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent

# Headings que indican que ya existe un system prompt → skip
EXISTING_PROMPT_RE = re.compile(
    r"^#{1,3}\s+(?:🤖\s+)?(?:\d+\.\s+)?Prompt\s+(?:de|del)\s+Sistema|System\s+Prompt",
    re.IGNORECASE | re.MULTILINE,
)

# Bloque fijo de contexto APB (igual en todos los prompts)
APB_CONTEXT_BLOCK = """\
## Contexto Corporativo APB
Carga context/apb/knowledge/APB_KNOWLEDGE_BASE.md (provider: prov-apb-knowledge-v1.0)
antes de ejecutar cualquier tarea.

Contiene: negocio portuario (escalas, atraques, movimientos, tasas, concesiones),
catálogo de aplicaciones (ARGOS, SÒSTRAT, APIs DOCKS), integraciones (PORTIC/EDI,
AGE, AIS, VTS Kongsberg), terminología trilingüe CA/ES/EN y mapa de equipos/Jira.

Úsalo para entender el dominio, usar terminología correcta e identificar sistemas
y equipos involucrados. El legacy (SÒSTRAT/Java/Oracle/CAS/Alfresco) es contexto
informacional — nunca prescribas tecnologías fuera del stack aprobado.
Stack aprobado: context/apb/standards/STANDARD_ARCHITECTURE.md"""

# Restricciones estándar APB que van siempre al final
STANDARD_RESTRICTIONS = """\
- Stack DOCKS únicamente: .NET, Azure SQL, EntraID, Service Bus, Redis, APIM,
  SharePoint — aunque el sistema analizado use Java/Oracle/CAS/Alfresco.
- Sin secretos ni credenciales en ningún output.
- Autonomy Level {autonomy_level}: todo output es borrador — requiere aprobación humana.
- Trazabilidad: skill_id/agent_id + usuario + fecha en todo output."""

# Punto de inserción — primero que aparezca
INSERTION_ANCHORS_RE = re.compile(
    r"^##\s+(?:⚠️\s+)?(?:Comportamiento|Historial de Cambios|🔄 Historial|Marcado IA)",
    re.MULTILINE,
)

# ---------------------------------------------------------------------------
# Parseo de frontmatter
# ---------------------------------------------------------------------------

def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text
    end = text.find("\n---", 3)
    if end == -1:
        return "", text
    return text[: end + 4], text[end + 4 :]


def parse_frontmatter_field(fm: str, field: str) -> str:
    """Extrae valor de un campo YAML simple (string o número)."""
    pattern = re.compile(
        rf'^{re.escape(field)}:\s*["\']?([^"\'\n]+)["\']?', re.MULTILINE
    )
    m = pattern.search(fm)
    return m.group(1).strip() if m else ""


def parse_multiline_field(fm: str, field: str) -> str:
    """Extrae valor de un campo YAML con >- o > (bloque multilínea)."""
    # Primero intenta campo simple
    val = parse_frontmatter_field(fm, field)
    if val:
        return val
    # Luego bloque literal/folded
    pattern = re.compile(
        rf'^{re.escape(field)}:\s*[>|]-?\s*\n((?:  .+\n?)+)', re.MULTILINE
    )
    m = pattern.search(fm)
    if m:
        lines = [l.strip() for l in m.group(1).splitlines()]
        return " ".join(lines)
    return ""

# ---------------------------------------------------------------------------
# Extracción de secciones del cuerpo
# ---------------------------------------------------------------------------

def extract_section(body: str, heading_patterns: list[str], max_lines: int = 20) -> str:
    """
    Extrae el contenido de la primera sección H2 que coincida con alguno de los
    heading_patterns. Devuelve hasta max_lines líneas del contenido.
    """
    combined = "|".join(heading_patterns)
    heading_re = re.compile(
        rf"^##\s+(?:[^\w]*)?(?:{combined})", re.IGNORECASE | re.MULTILINE
    )
    m = heading_re.search(body)
    if not m:
        return ""

    # Contenido desde el fin del heading hasta el siguiente H2
    start = m.end()
    next_h2 = re.search(r"^##\s+", body[start:], re.MULTILINE)
    end = start + next_h2.start() if next_h2 else len(body)
    content = body[start:end].strip()

    lines = content.splitlines()[:max_lines]
    return "\n".join(lines)


def clean_section(text: str) -> str:
    """Elimina emojis de encabezados y aplana tablas para el prompt."""
    if not text:
        return "(no especificado)"
    # Quitar líneas de tabla de markdown (---|---) pero mantener contenido
    lines = []
    for line in text.splitlines():
        if re.match(r"^\s*\|[-:| ]+\|\s*$", line):
            continue  # separador de tabla
        lines.append(line)
    result = "\n".join(lines).strip()
    return result if result else "(no especificado)"

# ---------------------------------------------------------------------------
# Generación del prompt
# ---------------------------------------------------------------------------

def is_agent(path: Path) -> bool:
    return "agents" in path.parts and "apb-owned" not in path.parts


def generate_prompt(fm: str, body: str, path: Path) -> str:
    name = parse_multiline_field(fm, "name")
    skill_id = parse_multiline_field(fm, "id")
    description = parse_multiline_field(fm, "description")
    autonomy_level = parse_frontmatter_field(fm, "autonomy_level") or "1"

    if not name:
        name = path.stem
    if not skill_id:
        skill_id = path.stem

    tipo = "agente" if is_agent(path) else "skill"

    # Inputs
    if is_agent(path):
        inputs_raw = extract_section(body, ["Input Esperado", "📥 Input"], 15)
    else:
        inputs_raw = extract_section(body, ["📥 Input", "Input", "Inputs", "3\\. Inputs"], 15)

    # Instrucciones / Capacidades
    if is_agent(path):
        instr_raw = extract_section(
            body, ["🧠 Capacidades", "Capacidades", "Skills Asignadas", "📋 Skills"], 20
        )
        instr_label = "Capacidades y Skills Disponibles"
    else:
        instr_raw = extract_section(
            body, ["🔄 Proceso", "Proceso", "Instrucciones", "Pasos"], 20
        )
        instr_label = "Instrucciones"

    # Outputs
    if is_agent(path):
        output_raw = extract_section(body, ["📤 Output Generado", "Output Generado", "Output"], 10)
    else:
        output_raw = extract_section(body, ["📤 Output", "Output", "Outputs", "4\\. Outputs"], 10)

    # Restricciones específicas
    restr_raw = extract_section(
        body, ["Reglas y Constraints", "🚫 Límites", "Límites y Restricciones", "Restricciones"], 10
    )

    inputs_txt = clean_section(inputs_raw)
    instr_txt = clean_section(instr_raw)
    output_txt = clean_section(output_raw)

    # Restricciones: específicas + estándar
    restr_specific = clean_section(restr_raw)
    std_restr = STANDARD_RESTRICTIONS.replace("{autonomy_level}", autonomy_level)
    if restr_specific and restr_specific != "(no especificado)":
        restr_txt = f"{restr_specific}\n\n{std_restr}"
    else:
        restr_txt = std_restr

    prompt_content = f"""\
Eres el {tipo} "{name}" ({skill_id}) del APB AI Framework,
operando para la Autoritat Portuària de Barcelona (APB).

{APB_CONTEXT_BLOCK}

## Misión
{description if description else "(ver sección Responsabilidad/Propósito)"}

## Inputs Esperados
{inputs_txt}

## {instr_label}
{instr_txt}

## Restricciones
{restr_txt}

## Formato de Salida
{output_txt}"""

    section = f"""\

## Prompt de Sistema

```
{prompt_content}
```

"""
    return section

# ---------------------------------------------------------------------------
# Procesamiento por fichero
# ---------------------------------------------------------------------------

def find_insertion_point(body: str) -> int:
    """
    Devuelve el índice en `body` donde insertar la sección de system prompt.
    Busca el primer anchor válido; si no hay ninguno, devuelve len(body).
    """
    m = INSERTION_ANCHORS_RE.search(body)
    if m:
        return m.start()
    return len(body)


def process_file(path: Path, dry_run: bool) -> dict:
    text = path.read_text(encoding="utf-8")
    result = {"path": str(path.relative_to(REPO_ROOT)), "status": "skip", "error": None}

    # Idempotencia: ya tiene system prompt
    if EXISTING_PROMPT_RE.search(text):
        return result

    fm, body = split_frontmatter(text)
    if not fm:
        result["error"] = "sin frontmatter"
        result["status"] = "error"
        return result

    try:
        prompt_section = generate_prompt(fm, body, path)
    except Exception as e:
        result["error"] = str(e)
        result["status"] = "error"
        return result

    insert_at = find_insertion_point(body)
    new_body = body[:insert_at] + prompt_section + body[insert_at:]
    new_text = fm + new_body

    result["status"] = "dry_run" if dry_run else "updated"
    if not dry_run:
        path.write_text(new_text, encoding="utf-8")

    return result

# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--path", type=Path, default=None)
    args = parser.parse_args()

    if args.path:
        root = args.path if args.path.is_absolute() else REPO_ROOT / args.path
        targets = [root] if root.is_file() else list(root.rglob("*.md"))
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
                print(f"{tag} {res['path']}")
                updated += 1
            elif res["status"] == "error":
                print(f"[ERROR] {res['path']}: {res['error']}", file=sys.stderr)
                errors += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"[ERROR] {path}: {e}", file=sys.stderr)
            errors += 1

    print(f"\n--- Resumen ---")
    print(f"  Ficheros con prompt generado : {updated}")
    print(f"  Ficheros saltados (ya tenían): {skipped}")
    print(f"  Errores                      : {errors}")
    if args.dry_run:
        print("\n  (Modo dry-run: no se ha escrito ningún fichero)")


if __name__ == "__main__":
    main()
