"""
scripts/_frontmatter.py — parseo y escaneo compartido de frontmatter YAML de
componentes del framework (skills, agents, subagents, workflows, providers,
wrappers, adapters).

Módulo interno (prefijo '_'): no es un CLI, lo importan validate_repo.py,
analyze_autonomy_landscape.py y generate_catalog.py para evitar tener tres
implementaciones divergentes del mismo parseo (ver
discovery/ESTRATEGIA_OPTIMIZACION_TOKENS_2026-07-06.md, Estrategia 1).
"""

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional, Tuple

try:
    import yaml
except ImportError:
    yaml = None  # los callers ya comprueban/exigen PyYAML antes de usar este módulo

FRONTMATTER_PATTERN = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
IGNORED_DIR_NAMES = {"templates", ".git", "node_modules"}


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


def iter_component_files(folder_path: Path):
    """Itera .md de un árbol, ignorando carpetas de templates/.git."""
    for filepath in sorted(folder_path.rglob("*.md")):
        if any(part in IGNORED_DIR_NAMES for part in filepath.parts):
            continue
        yield filepath


@dataclass(frozen=True)
class ComponentRecord:
    """Un componente ya leído y parseado una única vez.

    `metadata` es compartido entre todas las funciones que reciben el mismo
    escaneo — nunca mutarlo (p. ej. no inyectar claves nuevas dentro de él;
    construir un dict nuevo si hace falta añadir algo como '_rel_path')."""
    path: Path
    rel_path: str          # str(path.relative_to(repo_path)) — separador nativo
                            # del SO, igual que el rel_path usado históricamente
                            # en ValidationIssue.file (backslash en Windows).
    folder: str             # clave de component_folders que contiene este fichero
    component_type: Optional[str]
    content: str
    metadata: Dict
    found: bool


def scan_components(
    repo_path: Path,
    component_folders: Dict[str, Optional[str]],
) -> Dict[str, ComponentRecord]:
    """Recorre cada carpeta de component_folders UNA sola vez: carpetas en el
    orden de inserción del dict, ficheros con sorted() dentro de cada una —
    mismo orden que el recorrido disperso que sustituye. Lee y parsea cada
    fichero una única vez. Devuelve un dict keyed por rel_path (con el mismo
    formato de separador que devolvía cada validate_* antes de este cambio).
    """
    scanned: Dict[str, ComponentRecord] = {}
    for folder, component_type in component_folders.items():
        folder_path = repo_path / folder
        if not folder_path.exists():
            continue
        for filepath in iter_component_files(folder_path):
            rel_path = str(filepath.relative_to(repo_path))
            content = filepath.read_text(encoding="utf-8")
            metadata, found = parse_frontmatter(content)
            scanned[rel_path] = ComponentRecord(
                path=filepath,
                rel_path=rel_path,
                folder=folder,
                component_type=component_type,
                content=content,
                metadata=metadata,
                found=found,
            )
    return scanned
