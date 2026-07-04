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

# Nivel del check #18 (Estándar de Prompting). "WARNING" solo durante un
# retrofit en curso; el estado permanente es "ERROR" (anti-repetición:
# ningún componente puede existir sin el bloque canónico).
# Retrofit de 244 componentes completado 2026-07-02 → ERROR.
PROMPTING_STANDARD_LEVEL = "ERROR"

# Headings canónicos exigidos por PROMPTING_STANDARD.md §3 (literales, no
# traducir ni renombrar). El primero es la sección contenedora.
PROMPTING_SECTION = "## \U0001f9ed Estándar de Prompting"
PROMPTING_REQUIRED_HEADINGS = [
    "### Objetivo",
    "### Proceso (razonar → plan → aceptación → ejecutar)",
    "### Qué NO hacer",
    "### Ejemplo entrada → salida",
    "### Formato de respuesta",
    "### Separación SISTEMA / USUARIO",
]


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

    # 18. Estándar de Prompting (PROMPTING_STANDARD v1.0, punto #78)
    #     Skills apb-owned, agentes y subagentes deben incluir el bloque canónico
    #     completo (sección 🧭 + 6 headings). Ver context/apb/standards/PROMPTING_STANDARD.md §3.
    if _is_apb_skill or _is_agent or _is_subagent:
        if PROMPTING_SECTION not in content:
            result.add(ValidationIssue(
                PROMPTING_STANDARD_LEVEL, rel_path,
                "Falta la sección '## 🧭 Estándar de Prompting (PROMPTING_STANDARD v1.0)'. "
                "Añadir el bloque canónico según context/apb/standards/PROMPTING_STANDARD.md §3."
            ))
        else:
            missing_headings = [h for h in PROMPTING_REQUIRED_HEADINGS if h not in content]
            if missing_headings:
                result.add(ValidationIssue(
                    PROMPTING_STANDARD_LEVEL, rel_path,
                    "Bloque 'Estándar de Prompting' incompleto — faltan headings canónicos: "
                    + ", ".join(f"'{h}'" for h in missing_headings)
                    + ". No traducir ni renombrar (PROMPTING_STANDARD.md §3)."
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


def validate_no_deprecated_wiring(repo_path: Path, result: ValidationResult):
    """Check #25 (Sesión 19, 2026-07-04, anti-repetición): ningún componente
    activo puede declarar en su wiring de frontmatter ('skills', 'subagents',
    'agents', 'depends_on') un componente con status 'deprecated' o 'retired'.
    Origen: al crear apb-agent-design-compliance-v1.0 se estuvo a punto de
    cablear apb-design-wcag-v1.0 (deprecada, consolidada en
    apb-qa-accessibility-v1.0) sin que nada lo detectara; el mismo defecto ya
    existía en apb-agent-accessibility-auditor-v1.0 (corregido esa sesión).
    Los componentes que están ellos mismos deprecated/retired quedan exentos
    (su wiring es histórico). 'consumed_by' no se comprueba: que una skill
    deprecada conserve la lista de sus antiguos consumidores es inocuo."""
    wiring_fields = ["skills", "subagents", "agents", "depends_on"]

    # Mapa id → status de todos los componentes
    id_status: Dict[str, str] = {}
    for folder in COMPONENT_FOLDERS:
        folder_path = repo_path / folder
        if not folder_path.exists():
            continue
        for fp in iter_component_files(folder_path):
            meta, found = parse_frontmatter(fp.read_text(encoding="utf-8"))
            if found and meta.get("id"):
                id_status[meta["id"]] = str(meta.get("status", "")).strip().lower()

    for folder in COMPONENT_FOLDERS:
        folder_path = repo_path / folder
        if not folder_path.exists():
            continue
        for fp in iter_component_files(folder_path):
            rel_path = str(fp.relative_to(repo_path))
            meta, found = parse_frontmatter(fp.read_text(encoding="utf-8"))
            if not found:
                continue
            own_status = str(meta.get("status", "")).strip().lower()
            if own_status in ("deprecated", "retired"):
                continue  # wiring histórico de un componente ya retirado
            for field_name in wiring_fields:
                refs = meta.get(field_name) or []
                if isinstance(refs, str):
                    refs = [refs]
                for ref_id in refs:
                    ref_status = id_status.get(ref_id)
                    if ref_status in ("deprecated", "retired"):
                        result.add(ValidationIssue(
                            "ERROR", rel_path,
                            f"Wiring a componente {ref_status} en '{field_name}': "
                            f"'{ref_id}'. Sustituir por su reemplazo (ver "
                            f"'deprecated_reason' de ese componente) — check #25."
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


def validate_version_drift(repo_path: Path, result: ValidationResult, all_ids: Dict[str, str]):
    """Check E-T3: si un agente referencia una skill cuya major version es
    inferior a la última disponible en el repo, emite WARNING para que el
    equipo actualice la referencia o ancle explícitamente la versión antigua.

    Ejemplo: agente usa 'apb-foo-v1.0' pero el repo tiene 'apb-foo-v2.0'
    → WARNING. Ignorado si la skill referenciada no existe en all_ids (ya lo
    detecta validate_references como ERROR de referencia rota)."""

    _v_pattern = re.compile(r"^(.+)-v(\d+)\.\d+$")

    # Mapa base_name → major version más alta disponible en el repo
    base_to_max_major: Dict[str, int] = {}
    for comp_id in all_ids:
        m = _v_pattern.match(comp_id)
        if m:
            base, major_str = m.group(1), m.group(2)
            major = int(major_str)
            if major > base_to_max_major.get(base, 0):
                base_to_max_major[base] = major

    agents_folder = repo_path / "agents"
    if not agents_folder.exists():
        return

    for fp in iter_component_files(agents_folder):
        rel = str(fp.relative_to(repo_path))
        meta, found = parse_frontmatter(fp.read_text(encoding="utf-8"))
        if not found:
            continue
        for skill_ref in (meta.get("skills") or []):
            m = _v_pattern.match(skill_ref)
            if not m:
                continue
            base, ref_major = m.group(1), int(m.group(2))
            max_major = base_to_max_major.get(base, ref_major)
            if ref_major < max_major:
                result.add(ValidationIssue(
                    "WARNING", rel,
                    f"Version drift en skill '{skill_ref}': el repo tiene "
                    f"'{base}-v{max_major}.x'. Actualizar la referencia o "
                    f"documentar explícitamente por qué se ancla en v{ref_major}."
                ))


def validate_harness_cold_start(repo_path: Path, result: ValidationResult):
    """19. Cold-Start Test + infraestructura del harness (SYSTEM.md §10, punto #83).

    El repo es el System of Record: debe responder por sí solo las 5 preguntas
    cold-start y contener el scaffolding del harness. Mensajes 'bolígrafo rojo':
    indican qué falta y dónde reponerlo (GOVERNANCE.md §8.2)."""
    # Las 5 preguntas cold-start → archivo que las responde
    cold_start_map = {
        "¿Qué es el sistema?": "README.md",
        "¿Cómo está organizado?": "INDEX.md",
        "¿Cómo se ejecuta?": "SYSTEM.md",
        "¿Cómo se verifica?": "scripts/validate_repo.py",
        "¿Dónde estamos ahora?": "discovery/CONTINUIDAD_PROYECTO.md",
    }
    for question, rel in cold_start_map.items():
        path = repo_path / rel
        if not path.exists() or path.stat().st_size == 0:
            result.add(ValidationIssue(
                "ERROR", rel,
                f"Cold-Start Test roto: falta o está vacío el archivo que responde "
                f"'{question}'. Reponer {rel} (SYSTEM.md §10.2)."
            ))

    # Secciones de gobernanza del harness
    system_md = repo_path / "SYSTEM.md"
    if system_md.exists() and "## 10. Harness Engineering" not in system_md.read_text(encoding="utf-8"):
        result.add(ValidationIssue(
            "ERROR", "SYSTEM.md",
            "Falta la sección '## 10. Harness Engineering'. Restaurarla (punto #83, sesión 2026-07-02)."
        ))
    gov_md = repo_path / "GOVERNANCE.md"
    if gov_md.exists() and "## 8. Disciplina operacional del harness" not in gov_md.read_text(encoding="utf-8"):
        result.add(ValidationIssue(
            "ERROR", "GOVERNANCE.md",
            "Falta la sección '## 8. Disciplina operacional del harness'. Restaurarla (punto #83)."
        ))

    # Scaffolding harness-ready completo
    for rel in ("repo-scaffold/harness-ready/AGENTS.md",
                "repo-scaffold/harness-ready/PROGRESS.md",
                "repo-scaffold/harness-ready/FEATURES.md",
                "repo-scaffold/harness-ready/init_check.py"):
        if not (repo_path / rel).exists():
            result.add(ValidationIssue(
                "ERROR", rel,
                f"Scaffold del harness incompleto: falta {rel}. "
                "Restaurarlo desde el historial git (SYSTEM.md §10)."
            ))

    result.add(ValidationIssue("INFO", "SYSTEM.md", "Harness / Cold-Start verificado"))


def validate_test_plan_methodology(repo_path: Path, result: ValidationResult):
    """20. Metodología de planes de pruebas (punto #82, sesión QA-2 2026-07-02).

    Toda skill apb-owned de plan de pruebas (id contiene 'test-plan') debe
    referenciar el estándar corporativo TEST_PLAN_STANDARD, para que la
    metodología (orden de fuentes, procedencia múltiple, secciones obligatorias,
    gobernanza, no-regresión) no derive en silencio. Mensaje 'bolígrafo rojo'."""
    standard_rel = "context/apb/standards/TEST_PLAN_STANDARD.md"
    standard_path = repo_path / standard_rel

    qa_folder = repo_path / "skills" / "apb-owned" / "qa"
    if not qa_folder.exists():
        return
    referencing = []
    for fp in iter_component_files(qa_folder):
        meta, found = parse_frontmatter(fp.read_text(encoding="utf-8"))
        if not found:
            continue
        cid = str(meta.get("id", ""))
        if "test-plan" not in cid:
            continue
        referencing.append(cid)
        body = fp.read_text(encoding="utf-8")
        if "TEST_PLAN_STANDARD" not in body:
            result.add(ValidationIssue(
                "ERROR", str(fp.relative_to(repo_path)),
                "Skill de plan de pruebas sin referencia a 'TEST_PLAN_STANDARD'. "
                f"Añadir el enlace al estándar ({standard_rel}) en el cuerpo (punto #82)."
            ))

    # Si hay skills que lo referencian, el estándar debe existir
    if referencing and not standard_path.exists():
        result.add(ValidationIssue(
            "ERROR", standard_rel,
            "Falta el estándar TEST_PLAN_STANDARD.md referenciado por las skills de "
            "plan de pruebas. Restaurarlo (punto #82, sesión QA-2)."
        ))
    result.add(ValidationIssue("INFO", standard_rel, "Metodología de planes de pruebas verificada"))


def validate_unified_plan_conservation(repo_path: Path, result: ValidationResult):
    """21. Conservación íntegra al unificar planes de pruebas (TEST_PLAN_STANDARD §3.1).

    Anti-repetición del error 2026-07-02: unificar debe conservar TODO el contenido
    de las fuentes (pruebas Y narrativa), no resumir. Se verifica sobre el ejemplo
    canónico QA_TRU_TruckCenter_UNIFICADO.md que:
      (a) referencia cada fuente archivada en docs/qa/examples/sources/, y
      (b) contiene los encabezados narrativos obligatorios que las fuentes aportan.
    La pérdida silenciosa de un bloque es un defecto bloqueante → ERROR 'bolígrafo rojo'."""
    examples_dir = repo_path / "docs" / "qa" / "examples"
    unified = examples_dir / "QA_TRU_TruckCenter_UNIFICADO.md"
    sources_dir = examples_dir / "sources"
    if not unified.exists():
        return  # sin ejemplo canónico no hay nada que verificar
    unified_rel = str(unified.relative_to(repo_path))
    body = unified.read_text(encoding="utf-8")

    # (a) cada fuente archivada debe estar referenciada por su nombre en el unificado
    if sources_dir.exists():
        for src in sorted(sources_dir.glob("*.md")):
            if src.name not in body:
                result.add(ValidationIssue(
                    "ERROR", unified_rel,
                    f"El plan unificado no referencia la fuente archivada '{src.name}'. "
                    "Unificar debe conservar la trazabilidad de todas las fuentes "
                    "(TEST_PLAN_STANDARD §3.1 — conservación íntegra)."
                ))

    # (b) encabezados narrativos obligatorios (pérdida silenciosa = defecto bloqueante)
    required_sections = [
        "Incidencias históricas",
        "Proyectos futuros",
        "Modelo de datos",
        "Funcionalidad detallada",
        "Documentos de referencia",
    ]
    lowered = body.lower()
    for section in required_sections:
        if section.lower() not in lowered:
            result.add(ValidationIssue(
                "ERROR", unified_rel,
                f"El plan unificado ha perdido la sección '{section}'. Unificar NUNCA "
                "elimina información (TEST_PLAN_STANDARD §3.1). Reincorpórela desde las fuentes."
            ))

    # (c) esquema de ID canónico {APP}-B{NN}-T{NN} (TEST_PLAN_STANDARD §3.2, anti-repetición 2026-07-03)
    canonical_ids = re.findall(r"\bTRU-B\d{2}-T\d{2}\b", body)
    if not canonical_ids:
        result.add(ValidationIssue(
            "ERROR", unified_rel,
            "El plan unificado no usa el esquema de ID canónico 'TRU-B{NN}-T{NN}' "
            "(TEST_PLAN_STANDARD §3.2). No derivar de vuelta a numeración plana sin bloque."
        ))

    result.add(ValidationIssue("INFO", unified_rel, "Conservación íntegra del plan unificado verificada"))


def validate_agnostic_root_routing(repo_path: Path, result: ValidationResult):
    """22. Routing raíz agnóstico de LLM y herramienta (SYSTEM.md §4.3, §10.1).

    Anti-deriva (sesión 2026-07-03, feedback de Debora: 'nuestro framework debe
    ser agnóstico al LLM y la herramienta'): AGENTS.md es la fuente única de
    reglas permanentes. Las vistas por runtime (CLAUDE.md, .github/copilot-
    instructions.md) deben existir y ser ficheros DELGADOS que remitan a
    AGENTS.md, nunca reglas duplicadas de forma independiente. Si AGENTS.md
    falta, o una vista no lo referencia, el punto de entrada de esa herramienta
    puede divergir en silencio de la fuente única — ERROR 'bolígrafo rojo'."""
    agents_path = repo_path / "AGENTS.md"
    if not agents_path.exists() or agents_path.stat().st_size == 0:
        result.add(ValidationIssue(
            "ERROR", "AGENTS.md",
            "Falta el routing file raíz agnóstico AGENTS.md (SYSTEM.md §10.1, §4.3). "
            "Sin él, cada herramienta (Claude Code, GitHub Copilot...) puede acabar "
            "con sus propias reglas divergentes."
        ))
        return  # sin AGENTS.md no hay fuente contra la que comparar las vistas

    runtime_views = {
        "CLAUDE.md": repo_path / "CLAUDE.md",
        ".github/copilot-instructions.md": repo_path / ".github" / "copilot-instructions.md",
    }
    for rel, path in runtime_views.items():
        if not path.exists() or path.stat().st_size == 0:
            result.add(ValidationIssue(
                "ERROR", rel,
                f"Falta el punto de entrada '{rel}' para su herramienta, o está vacío. "
                "Debe existir como fichero delgado que remita a AGENTS.md (SYSTEM.md §10.1)."
            ))
            continue
        if "AGENTS.md" not in path.read_text(encoding="utf-8"):
            result.add(ValidationIssue(
                "ERROR", rel,
                f"'{rel}' no referencia AGENTS.md. Las vistas por runtime deben derivar "
                "de la fuente única de reglas, nunca duplicarlas de forma independiente "
                "(SYSTEM.md §10.1, riesgo de deriva silenciosa entre herramientas)."
            ))

    result.add(ValidationIssue("INFO", "AGENTS.md", "Routing raíz agnóstico de LLM/herramienta verificado"))


def validate_execution_and_approval_methodology(repo_path: Path, result: ValidationResult):
    """23. Roles + usuario de ejecución + destino + aprobación del informe
    (TEST_PLAN_STANDARD v1.3.0, Fase I, 2026-07-03).

    Anti-deriva: las secciones obligatorias de la Fase I no deben perderse en
    silencio ni de la plantilla, ni del estándar, ni del ejemplo canónico:
      - Estándar: «Roles de usuario y usuario de ejecución», «Aprobación del
        informe», «Destino de ejecución».
      - Plantilla: columna «Rol requerido», «Acta de aprobación», «Usuario de
        ejecución».
      - Ejemplo canónico: columna «Rol requerido» en la matriz de casos.
    Si falta alguno → ERROR 'bolígrafo rojo'."""
    standard = repo_path / "context" / "apb" / "standards" / "TEST_PLAN_STANDARD.md"
    template = repo_path / "context" / "apb" / "templates" / "TEST_PLAN.md"
    unified = repo_path / "docs" / "qa" / "examples" / "QA_TRU_TruckCenter_UNIFICADO.md"

    checks = [
        (standard, [
            "Roles de usuario y usuario de ejecución",
            "Aprobación del informe",
            "Destino de ejecución",
        ]),
        (template, [
            "Rol requerido",
            "Acta de aprobación",
            "Usuario de ejecución",
        ]),
        (unified, [
            "Rol requerido",
        ]),
    ]
    for path, needles in checks:
        if not path.exists():
            continue  # su ausencia la cubren otros checks (#82/#21)
        rel = str(path.relative_to(repo_path))
        body = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle not in body:
                result.add(ValidationIssue(
                    "ERROR", rel,
                    f"Falta el elemento obligatorio de Fase I '{needle}' "
                    f"(TEST_PLAN_STANDARD v1.3.0 §6.2/§9.1/§9.2). No debe derivar en silencio."
                ))
    result.add(ValidationIssue("INFO", "context/apb/standards/TEST_PLAN_STANDARD.md",
                               "Metodología de roles/ejecución/aprobación (Fase I) verificada"))


def validate_execution_report_evidence_methodology(repo_path: Path, result: ValidationResult):
    """24. Informe de ejecución: entrega dual + casos no ejecutados + evidencia vídeo
    (TEST_PLAN_STANDARD v1.4.0 §5.15/§7.1/§7.2, 2026-07-03).

    Anti-repetición del error 2026-07-03: se generó un informe de ejecución de QA
    (TruckCenter) solo en '.md' (sin '.html' corporativo), sin listar por ID los
    casos NO ejecutados (solo un recuento agregado), y con un GIF presentado como
    evidencia de sesión completa sin verificar su cobertura real (tope de
    fotogramas de la herramienta de captura). El informe en sí vive en el repo de
    cada aplicación (fuera de este repo, TEST_PLAN_STANDARD §7), así que este
    check no puede inspeccionar informes concretos de apps — verifica que las
    fuentes normativas del framework (estándar + skill de navegación exploratoria)
    no pierdan en silencio estas tres obligaciones, que es lo que falló esta vez."""
    standard = repo_path / "context" / "apb" / "standards" / "TEST_PLAN_STANDARD.md"
    exploratory_skill = repo_path / "skills" / "apb-owned" / "qa" / "apb-qa-exploratory-nav-v1.0.md"

    checks = [
        (standard, [
            "Casos NO ejecutados",
            "vídeo real",
            "Nunca solo",
        ]),
        (exploratory_skill, [
            "Casos NO ejecutados",
            "HTML",
        ]),
    ]
    for path, needles in checks:
        if not path.exists():
            continue  # su ausencia la cubren otros checks (#82/#20)
        rel = str(path.relative_to(repo_path))
        body = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle not in body:
                result.add(ValidationIssue(
                    "ERROR", rel,
                    f"Falta el elemento obligatorio de evidencia de ejecución '{needle}' "
                    f"(TEST_PLAN_STANDARD v1.4.0 §5.15/§7.1/§7.2). No debe derivar en silencio "
                    "— un informe sin esto vuelve a ser incompleto como el del 2026-07-03."
                ))
    result.add(ValidationIssue("INFO", "context/apb/standards/TEST_PLAN_STANDARD.md",
                               "Metodología de evidencia de informes de ejecución (entrega dual, "
                               "casos no ejecutados, vídeo) verificada"))


# IDs de componente citados como entregables en el plan (mismo prefijo que el
# resto de referencias del repo). Requiere versión (-vX.Y) para no confundir con
# menciones de familias/repos externos sin versión (p.ej. 'apb-ai-skills').
PLAN_DELIVERABLE_ID_RE = re.compile(
    r"`((?:apb|third|prov|wrap|adapter)-[a-z0-9-]+-v\d+\.\d+)`"
)
# Marcadores que, cerca del ID, indican que el plan lo declara explícitamente
# NO entregado (gap documentado o decisión de no crearlo) — no es un desfase.
PLAN_NEGATION_MARKERS = (
    "(pendiente)", "(planificado)", "diferido", "no se creó", "no se cre",
    "sin crear", "no existe", "hipotétic",
)


def validate_plan_deliverables_exist(repo_path: Path, result: ValidationResult, all_ids: Dict[str, str]):
    """26. Reconciliación plan↔repo (2026-07-04, anti-repetición).

    Origen: auditoría de desfase 2026-07-04 (discovery/AUDITORIA_DESFASE_PLAN_REPO.md)
    + riesgo R11 ya declarado en el propio plan ('Plan ↔ repo desincronizado') +
    precedente real #56–#76 (el plan afirmaba entregables que hubo que reconciliar
    a mano). El desfase que este check evita es 'DRIFT-repo': una sesión marcada
    CERRADA que declara un componente que NO existe en el repo.

    Alcance conservador para no generar falsos positivos: solo filas de tabla
    (empiezan por '|') de discovery/PLAN_FASES_FUTURAS.md que contienen 'CERRADA',
    y solo los IDs de componente con versión citados en ellas (entre backticks).
    Se excluyen los IDs con un marcador de negación cercano (gap documentado o
    decisión de no crear). Si un ID así declarado no existe en el repo → ERROR
    'bolígrafo rojo': corrige el plan o crea el componente."""
    plan_path = repo_path / "discovery" / "PLAN_FASES_FUTURAS.md"
    if not plan_path.exists():
        return
    rel = str(plan_path.relative_to(repo_path))
    seen: Set[str] = set()
    for lineno, line in enumerate(plan_path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.lstrip().startswith("|") or "CERRADA" not in line:
            continue
        for m in PLAN_DELIVERABLE_ID_RE.finditer(line):
            comp_id = m.group(1)
            nearby = line[max(0, m.start() - 40): m.end() + 40].lower()
            if any(neg in nearby for neg in PLAN_NEGATION_MARKERS):
                continue
            if comp_id in all_ids or comp_id in seen:
                continue
            seen.add(comp_id)
            result.add(ValidationIssue(
                "ERROR", rel,
                f"Desfase plan↔repo (check #26): una sesión marcada CERRADA declara el "
                f"entregable '{comp_id}' pero ese componente no existe en el repo. "
                f"Corrige la afirmación del plan o crea el componente (ver "
                f"discovery/AUDITORIA_DESFASE_PLAN_REPO.md).",
                line=lineno,
            ))
    result.add(ValidationIssue("INFO", rel, "Reconciliación plan↔repo (entregables CERRADA) verificada"))


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
    validate_no_deprecated_wiring(repo_path, result)
    validate_agent_subagent_consistency(repo_path, result, all_ids)
    validate_bidirectional_wiring(repo_path, result)
    validate_version_drift(repo_path, result, all_ids)
    validate_no_circular_dependencies(repo_path, result)
    validate_harness_cold_start(repo_path, result)
    validate_test_plan_methodology(repo_path, result)
    validate_unified_plan_conservation(repo_path, result)
    validate_agnostic_root_routing(repo_path, result)
    validate_execution_and_approval_methodology(repo_path, result)
    validate_execution_report_evidence_methodology(repo_path, result)
    validate_plan_deliverables_exist(repo_path, result, all_ids)
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
