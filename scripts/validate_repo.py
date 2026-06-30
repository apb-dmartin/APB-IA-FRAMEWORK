#!/usr/bin/env python3
"""
validate_repo.py — Validador del APB AI Framework

Valida estructura, frontmatter YAML, IDs y referencias del repositorio
contra el esquema definido en context/apb/SCHEMA.md.

Uso:
    python scripts/validate_repo.py
    python scripts/validate_repo.py --path /ruta/al/repo
    python scripts/validate_repo.py --strict   # warnings cuentan como error

Salida:
    Código 0: sin errores (puede haber warnings)
    Código 1: errores encontrados
"""

import sys
import re
import argparse
from pathlib import Path
from dataclasses import dataclass, field
from typing import Dict, List, Set, Tuple

try:
    import yaml
except ImportError:
    print("❌ ERROR: PyYAML no está instalado. Ejecute: pip install pyyaml")
    sys.exit(1)

# ──────────────────────────────────────────────────────────────────────────
# CONFIGURACIÓN — derivada de context/apb/SCHEMA.md
# ──────────────────────────────────────────────────────────────────────────

REQUIRED_ROOT_FILES = [
    "README.md", "SYSTEM.md", "GOVERNANCE.md", "CONTRIBUTING.md",
    "LICENSE.md", "INDEX.md", "DOMAIN_REGISTRY.md",
]

REQUIRED_FOLDERS = [
    "providers", "wrappers", "skills", "skills/apb-owned", "skills/third_party",
    "subagents", "agents", "workflows", "context/apb/standards",
    "context/apb/templates", "context/apb/policies", "discovery", "catalog",
    "scripts", "repo-scaffold/sdd-ready", "repo-scaffold/legacy-ready",
    "docs", "examples", "adapters/copilot", "adapters/claude", "tests",
]

# Carpetas que contienen componentes a validar individualmente, mapeadas a su "tipo"
COMPONENT_FOLDERS: Dict[str, str] = {
    "skills/apb-owned": "skill",
    "skills/third_party": "skill",
    "agents": "agent",
    "subagents": "subagent",
    "workflows": "workflow",
    "providers": "provider",
    "wrappers": "wrapper",
    "adapters": "adapter",
}

VALID_STATUSES = {
    "draft", "candidate", "under_review", "approved",
    "deprecated", "retired", "watchlist", "rejected",
}

VALID_AUTONOMY_LEVELS = {0, 1, 2, 3, 4}

# Dominios válidos — debe reflejar DOMAIN_REGISTRY.md
VALID_DOMAINS = {
    "development", "qa", "architecture", "discovery", "platform",
    "security", "governance", "operation", "documentation", "orchestration", "pm",
    "design",
}

ID_PATTERNS = {
    "skill_apb": re.compile(r"^apb-[a-z]+-[a-z0-9-]+-v\d+\.\d+$"),
    "skill_third_party": re.compile(r"^third-[a-z0-9]+-[a-z0-9-]+-v\d+\.\d+$"),
    "agent": re.compile(r"^apb-agent-[a-z0-9-]+-v\d+\.\d+$"),
    "subagent": re.compile(r"^apb-sub-[a-z0-9-]+-v\d+\.\d+$"),
    "workflow": re.compile(r"^apb-wf-[a-z0-9-]+-v\d+\.\d+$"),
    "provider": re.compile(r"^prov-[a-z0-9-]+-v\d+\.\d+$"),
    "wrapper": re.compile(r"^wrap-[a-z0-9-]+-v\d+\.\d+$"),
    "adapter": re.compile(r"^adapter-[a-z0-9-]+-v\d+\.\d+$"),
}

REQUIRED_COMMON_FIELDS = [
    "id", "name", "description", "version", "status",
    "owner", "domain", "created_date", "review_date",
]

REQUIRED_FIELDS_BY_TYPE = {
    "skill": ["autonomy_level"],
    "agent": ["autonomy_level", "skills", "runtime"],
    "subagent": ["parent_agent", "specialty"],
    "workflow": ["autonomy_level", "agents"],
    "provider": ["provider_type", "access_mode"],
    "wrapper": ["wraps", "source_repo", "source_license", "source_commit"],
    "adapter": ["runtime_target"],
}

FRONTMATTER_PATTERN = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

SECRET_PATTERNS = [
    re.compile(r'password\s*=\s*[\'"][^\'"]+[\'"]', re.IGNORECASE),
    re.compile(r'api[_-]?key\s*[:=]\s*[\'"][^\'"]+[\'"]', re.IGNORECASE),
    re.compile(r'secret\s*[:=]\s*[\'"][^\'"]+[\'"]', re.IGNORECASE),
    re.compile(r'token\s*[:=]\s*[\'"][^\'"]+[\'"]', re.IGNORECASE),
    re.compile(r'connection[_-]?string\s*[:=]\s*[\'"][^\'"]+[\'"]', re.IGNORECASE),
]

IP_PATTERN = re.compile(
    r"\b(10\.\d{1,3}\.\d{1,3}\.\d{1,3}|172\.(1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3}|"
    r"192\.168\.\d{1,3}\.\d{1,3})\b"
)

OLD_BRAND_PATTERNS = [
    re.compile(r"@apb\.es"),
    re.compile(r"Islas Baleares"),
    re.compile(r"Administraci[oó]n P[uú]blica de las Islas Baleares"),
]

IGNORED_DIR_NAMES = {"templates", ".git", "node_modules"}


# ──────────────────────────────────────────────────────────────────────────
# CLASES DE DATOS
# ──────────────────────────────────────────────────────────────────────────

@dataclass
class ValidationIssue:
    level: str  # ERROR, WARNING, INFO
    file: str
    message: str
    line: int = 0


@dataclass
class ValidationResult:
    errors: List[ValidationIssue] = field(default_factory=list)
    warnings: List[ValidationIssue] = field(default_factory=list)
    infos: List[ValidationIssue] = field(default_factory=list)

    @property
    def has_errors(self) -> bool:
        return len(self.errors) > 0

    @property
    def has_warnings(self) -> bool:
        return len(self.warnings) > 0

    def add(self, issue: ValidationIssue):
        {"ERROR": self.errors, "WARNING": self.warnings}.get(issue.level, self.infos).append(issue)


# ──────────────────────────────────────────────────────────────────────────
# UTILIDADES
# ──────────────────────────────────────────────────────────────────────────

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


def id_pattern_for(component_type: str, rel_path: str) -> re.Pattern:
    if component_type == "skill":
        return ID_PATTERNS["skill_third_party"] if "third_party" in rel_path else ID_PATTERNS["skill_apb"]
    return ID_PATTERNS[component_type]


# ──────────────────────────────────────────────────────────────────────────
# VALIDACIONES
# ──────────────────────────────────────────────────────────────────────────

def validate_root_files(repo_path: Path, result: ValidationResult):
    for filename in REQUIRED_ROOT_FILES:
        if (repo_path / filename).exists():
            result.add(ValidationIssue("INFO", filename, "Archivo raíz presente"))
        else:
            result.add(ValidationIssue("ERROR", filename, "Archivo raíz obligatorio no encontrado"))


def validate_folder_structure(repo_path: Path, result: ValidationResult):
    for folder in REQUIRED_FOLDERS:
        if (repo_path / folder).exists():
            result.add(ValidationIssue("INFO", folder, "Carpeta presente"))
        else:
            result.add(ValidationIssue("WARNING", folder, f"Carpeta recomendada no encontrada: {folder}/"))


def validate_component_file(
    filepath: Path, repo_path: Path, component_type: str,
    result: ValidationResult, all_ids: Dict[str, str],
):
    rel_path = str(filepath.relative_to(repo_path))
    content = filepath.read_text(encoding="utf-8")
    metadata, found = parse_frontmatter(content)

    if not found:
        result.add(ValidationIssue(
            "ERROR", rel_path,
            "Frontmatter YAML obligatorio ausente o malformado. "
            "Ver context/apb/SCHEMA.md."
        ))
        return

    # 1. Campos comunes obligatorios
    for f in REQUIRED_COMMON_FIELDS:
        if f not in metadata or metadata[f] in (None, ""):
            result.add(ValidationIssue("ERROR", rel_path, f"Campo obligatorio ausente: '{f}'"))

    # 2. Campos específicos por tipo
    for f in REQUIRED_FIELDS_BY_TYPE.get(component_type, []):
        if f not in metadata or metadata[f] in (None, "", []):
            result.add(ValidationIssue(
                "ERROR", rel_path,
                f"Campo obligatorio del tipo '{component_type}' ausente: '{f}'"
            ))

    comp_id = str(metadata.get("id", "")).strip()

    # 3. Formato del ID
    if comp_id:
        pattern = id_pattern_for(component_type, rel_path)
        if not pattern.match(comp_id):
            result.add(ValidationIssue(
                "ERROR", rel_path,
                f"ID con formato no válido: '{comp_id}'. Ver context/apb/SCHEMA.md §4."
            ))

        # 4. ID == nombre de archivo (sin extensión)
        if comp_id != filepath.stem:
            result.add(ValidationIssue(
                "ERROR", rel_path,
                f"El 'id' del frontmatter ('{comp_id}') no coincide con el nombre de archivo "
                f"('{filepath.stem}')."
            ))

        # 5. ID duplicado en todo el repo
        if comp_id in all_ids:
            result.add(ValidationIssue(
                "ERROR", rel_path,
                f"ID duplicado: '{comp_id}' ya declarado en '{all_ids[comp_id]}'."
            ))
        else:
            all_ids[comp_id] = rel_path

    # 6. Estado válido
    status = metadata.get("status", "")
    if status and status not in VALID_STATUSES:
        result.add(ValidationIssue(
            "ERROR", rel_path,
            f"Estado no válido: '{status}'. Permitidos: {', '.join(sorted(VALID_STATUSES))}"
        ))

    # 7. Dominio válido
    domain = metadata.get("domain", "")
    if domain and domain not in VALID_DOMAINS:
        result.add(ValidationIssue(
            "ERROR", rel_path,
            f"Dominio no válido: '{domain}'. Permitidos: {', '.join(sorted(VALID_DOMAINS))}. "
            f"Ver DOMAIN_REGISTRY.md."
        ))

    # 8. Nivel de autonomía válido
    autonomy = metadata.get("autonomy_level")
    if autonomy is not None and autonomy not in VALID_AUTONOMY_LEVELS:
        result.add(ValidationIssue(
            "ERROR", rel_path, f"Nivel de autonomía no válido: {autonomy}. Permitidos: 0-4"
        ))

    # 9. Pin de versión real para wrappers/skills de terceros (nunca "HEAD";
    #    "unverified" es admisible solo junto con verified_date, GOVERNANCE.md §4.2)
    source_commit_val = str(metadata.get("source_commit", "")).strip()
    if source_commit_val.upper() == "HEAD" or source_commit_val.lower() == "main":
        result.add(ValidationIssue(
            "ERROR", rel_path,
            f"source_commit no puede ser '{source_commit_val}'; debe ser un commit/tag fijo "
            f"o 'unverified' + verified_date (GOVERNANCE.md §4.2)."
        ))
    elif source_commit_val.lower() == "unverified":
        if not metadata.get("verified_date"):
            result.add(ValidationIssue(
                "ERROR", rel_path,
                "source_commit='unverified' requiere declarar 'verified_date' (GOVERNANCE.md §4.2)."
            ))
        else:
            result.add(ValidationIssue(
                "WARNING", rel_path,
                f"source_commit pendiente de verificar (revisado manualmente el "
                f"{metadata.get('verified_date')}). Refinar a SHA real cuando haya acceso de red."
            ))

    # 10. Secretos hardcodeados
    for pattern in SECRET_PATTERNS:
        for m in pattern.finditer(content):
            text = m.group(0)
            text_lower = text.lower()
            is_reference_not_secret = (
                "keyvault" in text_lower or "secrets." in text_lower
                or "akv/" in text_lower  # referencia a Azure Key Vault
                or "vault_" in text_lower  # variable de Ansible Vault, no el secreto en sí
                or "{{" in text  # interpolación de variable (Jinja/Ansible), no literal
                or "replace_with" in text_lower or "<your" in text_lower  # placeholder explícito
            )
            if is_reference_not_secret:
                continue
            result.add(ValidationIssue(
                "ERROR", rel_path, f"Posible secreto hardcodeado: '{text[:50]}...'",
                line=content[:m.start()].count("\n") + 1,
            ))

    # 11. IPs internas
    for m in IP_PATTERN.finditer(content):
        result.add(ValidationIssue(
            "WARNING", rel_path, f"Posible IP interna detectada: {m.group(0)}",
            line=content[:m.start()].count("\n") + 1,
        ))

    # 12. Restos de marca antigua
    for pattern in OLD_BRAND_PATTERNS:
        if pattern.search(content):
            result.add(ValidationIssue(
                "ERROR", rel_path, f"Resto de marca/contacto antiguo detectado: '{pattern.pattern}'"
            ))

    # 13. Marcado IA obligatorio (POLICY_AI_USAGE §6)
    #     Todas las skills apb-owned deben incluir la sección de marcado de artefactos.
    #     Los agentes también, ya que orquestan y entregan artefactos.
    #     Ver: context/apb/standards/AI_MARKING_STANDARD.md
    _rp = rel_path.replace("\\", "/")
    _is_apb_skill = component_type == "skill" and "skills/apb-owned" in _rp
    _is_agent = component_type == "agent" and "agents/" in _rp
    if _is_apb_skill or _is_agent:
        if "## Marcado IA obligatorio" not in content:
            result.add(ValidationIssue(
                "ERROR", rel_path,
                "Falta la sección '## Marcado IA obligatorio (POLICY_AI_USAGE §6)'. "
                "Añadir según context/apb/standards/AI_MARKING_STANDARD.md."
            ))

    # 14. Comportamiento ante inputs incompletos (Sesión Calidad de Pruebas)
    #     Todas las skills apb-owned deben documentar qué hace el agente si un input es
    #     nulo, ambiguo o incompleto. Previene que el agente continúe sin datos suficientes.
    if _is_apb_skill:
        if "## ⚠️ Comportamiento ante inputs incompletos" not in content:
            result.add(ValidationIssue(
                "ERROR", rel_path,
                "Falta la sección '## ⚠️ Comportamiento ante inputs incompletos'. "
                "Añadir tabla con comportamiento para cada input obligatorio."
            ))

    # 15. Manejo de fallos en workflows (Sesión Calidad de Pruebas)
    #     Todos los workflows deben documentar qué ocurre si cada fase falla,
    #     si el fallo es bloqueante y quién decide la acción de recuperación.
    _is_workflow = component_type == "workflow" and "workflows/" in _rp
    if _is_workflow:
        if "## \U0001f6a8 Manejo de Fallos" not in content:
            result.add(ValidationIssue(
                "ERROR", rel_path,
                "Falta la sección '## 🚨 Manejo de Fallos'. "
                "Añadir tabla con fallo posible, si es bloqueante y acción para cada fase."
            ))

    # 16. System prompt en subagentes (gap detectado en Sesión Enriquecimiento C1)
    #     Todos los subagentes deben tener un prompt de sistema explícito con stack,
    #     principios de actuación y límites. Sin él el subagente no puede operar.
    _is_subagent = component_type == "subagent" and "subagents/" in _rp
    if _is_subagent:
        if "## \U0001f9e0 Prompt de Sistema" not in content:
            result.add(ValidationIssue(
                "ERROR", rel_path,
                "Falta la sección '## 🧠 Prompt de Sistema'. "
                "Añadir según context/apb/templates/SUBAGENT.md."
            ))

    # 17. Contratos de output inter-agente en workflows complejos (gap C1)
    #     Los workflows con ≥3 agentes deben definir qué entrega cada agente al siguiente.
    if _is_workflow:
        agents_list = metadata.get("agents") or []
        if len(agents_list) >= 3:
            if "## \U0001f4e1 Contratos de Output Inter-Agente" not in content:
                result.add(ValidationIssue(
                    "WARNING", rel_path,
                    f"Workflow con {len(agents_list)} agentes sin sección "
                    "'## 📡 Contratos de Output Inter-Agente'. "
                    "Añadir tabla de contratos entre agentes consecutivos."
                ))

    result.add(ValidationIssue("INFO", rel_path, f"Componente validado: {comp_id or '(sin id)'}"))


def validate_components(repo_path: Path, result: ValidationResult) -> Dict[str, str]:
    all_ids: Dict[str, str] = {}
    for folder, component_type in COMPONENT_FOLDERS.items():
        folder_path = repo_path / folder
        if not folder_path.exists():
            result.add(ValidationIssue("WARNING", folder, "Carpeta no encontrada, se omite"))
            continue
        for filepath in iter_component_files(folder_path):
            validate_component_file(filepath, repo_path, component_type, result, all_ids)
    return all_ids


def validate_references(repo_path: Path, result: ValidationResult, all_ids: Dict[str, str]):
    """Verifica que toda referencia cruzada apunte a un ID que realmente
    existe en el repo. Cubre dos fuentes:
    1. Campos de frontmatter (skills, agents, subagents, depends_on, consumed_by).
    2. Menciones en el cuerpo markdown como `id-con-version` (tablas, listas,
       prosa) — donde históricamente han aparecido más roturas por IDs
       inventados o renombrados sin propagar el cambio.
    """
    reference_fields = ["skills", "subagents", "agents", "depends_on", "consumed_by"]
    body_id_pattern = re.compile(r"`((?:apb|third|prov|wrap|adapter)-[a-z0-9-]+-v\d+\.\d+)`")

    for folder, component_type in COMPONENT_FOLDERS.items():
        folder_path = repo_path / folder
        if not folder_path.exists():
            continue
        for filepath in iter_component_files(folder_path):
            rel_path = str(filepath.relative_to(repo_path))
            content = filepath.read_text(encoding="utf-8")
            metadata, found = parse_frontmatter(content)
            if not found:
                continue

            for field_name in reference_fields:
                refs = metadata.get(field_name)
                if not refs:
                    continue
                if isinstance(refs, str):
                    refs = [refs]
                for ref_id in refs:
                    if ref_id not in all_ids:
                        result.add(ValidationIssue(
                            "ERROR", rel_path,
                            f"Referencia rota en '{field_name}': '{ref_id}' no existe en el repo."
                        ))

            body_match = re.match(r"^---\s*\n.*?\n---\s*\n(.*)$", content, re.DOTALL)
            body = body_match.group(1) if body_match else content
            seen_in_body = set()
            for m in body_id_pattern.finditer(body):
                ref_id = m.group(1)
                if ref_id == metadata.get("id"):
                    continue  # auto-referencia (p.ej. el propio ID en un ejemplo)
                if ref_id not in all_ids and ref_id not in seen_in_body:
                    seen_in_body.add(ref_id)
                    # 18. Si la referencia incluye "(pendiente)" o "(planificado)" en el contexto
                    #     cercano, es un gap documentado intencionalmente — INFO, no WARNING.
                    #     El contexto cercano se busca en los 80 caracteres siguientes al match.
                    match_end = m.end()
                    nearby = body[match_end:match_end + 80]
                    is_documented_gap = "(pendiente)" in nearby or "(planificado)" in nearby
                    if is_documented_gap:
                        result.add(ValidationIssue(
                            "INFO", rel_path,
                            f"Gap documentado: '{ref_id}' marcado como pendiente de crear."
                        ))
                    else:
                        result.add(ValidationIssue(
                            "WARNING", rel_path,
                            f"Posible referencia rota en el cuerpo del documento: '{ref_id}' "
                            f"no existe en el repo. Verificar manualmente (puede ser un gap de "
                            f"catálogo real, no solo un error de escritura)."
                        ))


def validate_agent_subagent_consistency(repo_path: Path, result: ValidationResult, all_ids: Dict[str, str]):
    """Verifica que la relación agente↔subagente sea coherente en ambos
    sentidos: si un agente declara un subagent en su lista 'subagents', ese
    subagent debe declarar el ID (no el nombre) de ese mismo agente en su
    campo 'parent_agent'."""
    agent_to_subagents: Dict[str, str] = {}
    agents_folder = repo_path / "agents"
    if not agents_folder.exists():
        return
    for filepath in iter_component_files(agents_folder):
        metadata, found = parse_frontmatter(filepath.read_text(encoding="utf-8"))
        if not found:
            continue
        agent_id = metadata.get("id")
        for sub_id in (metadata.get("subagents") or []):
            agent_to_subagents[sub_id] = agent_id

    subagents_folder = repo_path / "subagents"
    if not subagents_folder.exists():
        return
    for filepath in iter_component_files(subagents_folder):
        rel_path = str(filepath.relative_to(repo_path))
        metadata, found = parse_frontmatter(filepath.read_text(encoding="utf-8"))
        if not found:
            continue
        sub_id = metadata.get("id")
        declared_parent = str(metadata.get("parent_agent", "")).strip()

        if declared_parent and declared_parent not in all_ids:
            result.add(ValidationIssue(
                "ERROR", rel_path,
                f"'parent_agent' debe ser el ID del agente (p.ej. 'apb-agent-x-v1.0'), "
                f"no un nombre legible: '{declared_parent}'."
            ))
            continue

        expected_parent = agent_to_subagents.get(sub_id)
        if expected_parent and declared_parent != expected_parent:
            result.add(ValidationIssue(
                "ERROR", rel_path,
                f"Inconsistencia agente↔subagente: '{expected_parent}' lista este "
                f"subagent, pero 'parent_agent' aquí es '{declared_parent}'."
            ))


def validate_bidirectional_wiring(repo_path: Path, result: ValidationResult):
    """Verifica el cableado bidireccional entre agentes/subagentes y entre
    agentes/skills APB:
    - Si un subagente declara 'parent_agent: X', el agente X debe listarlo en
      'subagents:'. Si no → WARNING.
    - Si una skill APB declara 'consumed_by: [Y]', el agente Y debe listarla en
      'skills:'. Si no → WARNING.
    Complementa a validate_agent_subagent_consistency (que verifica el sentido
    contrario: agente lista subagente pero subagente no declara padre)."""

    # Construir mapa agente → set de subagentes declarados
    agent_subagents: Dict[str, set] = {}
    agents_folder = repo_path / "agents"
    if agents_folder.exists():
        for fp in iter_component_files(agents_folder):
            meta, found = parse_frontmatter(fp.read_text(encoding="utf-8"))
            if not found:
                continue
            aid = meta.get("id")
            if aid:
                agent_subagents[aid] = set(meta.get("subagents") or [])

    # Construir mapa agente → set de skills declaradas
    agent_skills: Dict[str, set] = {}
    if agents_folder.exists():
        for fp in iter_component_files(agents_folder):
            meta, found = parse_frontmatter(fp.read_text(encoding="utf-8"))
            if not found:
                continue
            aid = meta.get("id")
            if aid:
                agent_skills[aid] = set(meta.get("skills") or [])

    # Check 1: subagente declara parent_agent pero padre no lo lista
    subagents_folder = repo_path / "subagents"
    if subagents_folder.exists():
        for fp in iter_component_files(subagents_folder):
            rel = str(fp.relative_to(repo_path))
            meta, found = parse_frontmatter(fp.read_text(encoding="utf-8"))
            if not found:
                continue
            sub_id = meta.get("id")
            parent = str(meta.get("parent_agent", "")).strip()
            if parent and parent in agent_subagents:
                if sub_id not in agent_subagents[parent]:
                    result.add(ValidationIssue(
                        "WARNING", rel,
                        f"Wiring unidireccional: este subagente declara "
                        f"'parent_agent: {parent}' pero ese agente no lo lista "
                        f"en 'subagents:'. Añadir '{sub_id}' al frontmatter de "
                        f"agents/{parent}.md."
                    ))

    # Check 2: skill APB declara consumed_by pero agente no la lista
    for folder in ["skills/apb-owned"]:
        folder_path = repo_path / folder
        if not folder_path.exists():
            continue
        for fp in iter_component_files(folder_path):
            rel = str(fp.relative_to(repo_path))
            meta, found = parse_frontmatter(fp.read_text(encoding="utf-8"))
            if not found:
                continue
            skill_id = meta.get("id")
            consumed_by = meta.get("consumed_by") or []
            if isinstance(consumed_by, str):
                consumed_by = [consumed_by]
            for agent_id in consumed_by:
                if agent_id in agent_skills and skill_id not in agent_skills[agent_id]:
                    result.add(ValidationIssue(
                        "WARNING", rel,
                        f"Wiring unidireccional: skill declara 'consumed_by: "
                        f"{agent_id}' pero ese agente no la lista en 'skills:'. "
                        f"Añadir '{skill_id}' al frontmatter de "
                        f"agents/{agent_id}.md."
                    ))


def validate_no_circular_dependencies(repo_path: Path, result: ValidationResult):
    """Detecta dependencias circulares directas (A depende de B y B depende
    de A) en el campo 'depends_on' de las skills. 'depends_on' representa
    una relación de prerrequisito de ejecución, por lo que no debe ser
    simétrica; relaciones bidireccionales genuinas (skills complementarias)
    deben documentarse en el cuerpo como 'relacionadas', no como depends_on."""
    depends_map: Dict[str, List[str]] = {}
    for folder in ["skills/apb-owned", "skills/third_party"]:
        folder_path = repo_path / folder
        if not folder_path.exists():
            continue
        for filepath in iter_component_files(folder_path):
            metadata, found = parse_frontmatter(filepath.read_text(encoding="utf-8"))
            if not found:
                continue
            comp_id = metadata.get("id")
            if comp_id:
                depends_map[comp_id] = metadata.get("depends_on") or []

    reported = set()
    for a, deps in depends_map.items():
        for b in deps:
            if a in depends_map.get(b, []) and (b, a) not in reported:
                reported.add((a, b))
                result.add(ValidationIssue(
                    "ERROR", f"{a} / {b}",
                    f"Dependencia circular en 'depends_on': '{a}' y '{b}' se "
                    f"declaran mutuamente como dependencia. Si la relación es "
                    f"complementaria (no de prerrequisito), documentarla en el "
                    f"cuerpo del documento, no en 'depends_on'."
                ))


def validate_catalog(repo_path: Path, result: ValidationResult, all_ids: Dict[str, str]):
    catalog_path = repo_path / "catalog" / "CATALOG.md"
    if not catalog_path.exists():
        result.add(ValidationIssue("WARNING", "catalog/CATALOG.md", "Catálogo no encontrado"))
        return
    content = catalog_path.read_text(encoding="utf-8")
    missing = [cid for cid in all_ids if cid not in content]
    if missing:
        result.add(ValidationIssue(
            "WARNING", "catalog/CATALOG.md",
            f"{len(missing)} IDs existen en el repo pero no aparecen en el catálogo "
            f"(ejecute scripts/generate_catalog.py para regenerarlo)."
        ))
    result.add(ValidationIssue("INFO", "catalog/CATALOG.md", "Catálogo presente"))


# ──────────────────────────────────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────────────────────────────────

def is_policy_exempt_warning(issue: ValidationIssue) -> bool:
    """Warnings que representan una política de gobernanza deliberada
    (GOVERNANCE.md §4.2), no un defecto: 'source_commit: unverified' para
    skills/wrappers de terceros sin acceso de red para verificar el SHA real.
    --strict no debe fallar por estos; cualquier otro warning sí debe
    seguir bloqueando. Decisión de Debora, Sesión 7."""
    return issue.message.startswith("source_commit pendiente de verificar")


def main():
    # En Windows la consola por defecto es cp1252 y rompe al imprimir emojis
    # (📁, ⛔, ✅…). Forzamos UTF-8 en stdout/stderr para que el validador
    # funcione igual en local (Windows) y en CI (Linux). Best-effort: si el
    # stream no soporta reconfigure (p. ej. está redirigido), se ignora.
    for _stream in (sys.stdout, sys.stderr):
        try:
            _stream.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass

    parser = argparse.ArgumentParser(description="Validador del APB AI Framework")
    parser.add_argument("--path", type=str, default=".", help="Ruta al repositorio")
    parser.add_argument(
        "--strict", action="store_true",
        help="Warnings cuentan como error, EXCEPTO 'source_commit: unverified' "
             "(política de gobernanza deliberada, ver GOVERNANCE.md §4.2)."
    )
    args = parser.parse_args()

    repo_path = Path(args.path).resolve()
    if not repo_path.exists():
        print(f"❌ ERROR: la ruta '{repo_path}' no existe.")
        sys.exit(1)

    print("=" * 70)
    print("  APB AI FRAMEWORK — Validador de Repositorio")
    print("=" * 70)
    print(f"📁 Ruta: {repo_path}")
    print(f"🔍 Modo estricto: {'Sí' if args.strict else 'No'}")
    print("-" * 70)

    result = ValidationResult()

    validate_root_files(repo_path, result)
    validate_folder_structure(repo_path, result)
    all_ids = validate_components(repo_path, result)
    validate_references(repo_path, result, all_ids)
    validate_agent_subagent_consistency(repo_path, result, all_ids)
    validate_bidirectional_wiring(repo_path, result)
    validate_no_circular_dependencies(repo_path, result)
    validate_catalog(repo_path, result, all_ids)

    print()
    print("=" * 70)
    print("  RESUMEN DE VALIDACIÓN")
    print("=" * 70)

    if result.warnings:
        print(f"\n⚠️  WARNINGS ({len(result.warnings)}):")
        for issue in result.warnings:
            print(f"   • [{issue.file}] {issue.message}")

    if result.errors:
        print(f"\n❌ ERRORES ({len(result.errors)}):")
        for issue in result.errors:
            line_info = f" (línea {issue.line})" if issue.line > 0 else ""
            print(f"   • [{issue.file}{line_info}] {issue.message}")

    print()
    print("-" * 70)
    print(f"   Total: {len(result.errors)} errores, {len(result.warnings)} warnings, "
          f"{len(result.infos)} infos ({len(all_ids)} componentes con ID detectados)")

    blocking_warnings = [w for w in result.warnings if not is_policy_exempt_warning(w)]
    exempt_count = len(result.warnings) - len(blocking_warnings)
    if exempt_count and args.strict:
        print(f"\nℹ️  {exempt_count} warning(s) de 'source_commit: unverified' excluidos "
              f"del modo estricto (política deliberada, GOVERNANCE.md §4.2).")

    # Destacar por separado los warnings que SÍ hacen fallar el modo estricto.
    # Sin esto, el único warning bloqueante queda enterrado entre decenas de
    # warnings exentos de 'source_commit', y "0 errores" se lee erróneamente
    # como éxito. El criterio canónico de éxito es el exit code / este bloque,
    # NO el conteo de 'errores'.
    if args.strict and blocking_warnings:
        print()
        print("-" * 70)
        print(f"  ⛔ WARNINGS BLOQUEANTES EN MODO ESTRICTO ({len(blocking_warnings)}):")
        print("     (NO exentos — causan el fallo aunque 'errores' sea 0)")
        for issue in blocking_warnings:
            line_info = f" (línea {issue.line})" if issue.line > 0 else ""
            print(f"   • [{issue.file}{line_info}] {issue.message}")

    # 19. Lista consolidada de gaps documentados (pendientes de crear)
    pending_gaps = [i for i in result.infos if i.message.startswith("Gap documentado:")]
    if pending_gaps:
        print()
        print("-" * 70)
        print(f"  📋 PENDIENTES DETECTADOS ({len(pending_gaps)} gaps documentados con '(pendiente)'/'(planificado)'):")
        seen_gaps = set()
        for issue in pending_gaps:
            gap_id = issue.message.replace("Gap documentado: ", "").replace(" marcado como pendiente de crear.", "").strip("'")
            if gap_id not in seen_gaps:
                seen_gaps.add(gap_id)
                print(f"   • {gap_id}  ← referenciado en [{issue.file}]")
        print("  (Crear estos componentes cuando estén disponibles para eliminar los gaps)")

    if result.has_errors or (args.strict and blocking_warnings):
        print("\n❌ VALIDACIÓN FALLIDA.")
        sys.exit(1)
    else:
        print("\n✅ VALIDACIÓN EXITOSA.")
        sys.exit(0)


if __name__ == "__main__":
    main()
