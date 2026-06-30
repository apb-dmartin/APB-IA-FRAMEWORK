#!/usr/bin/env python3
"""
test_validate_repo.py — Tests de dogfooding para scripts/validate_repo.py

No valida el repositorio real: construye fixtures sintéticos mínimos en un
directorio temporal y comprueba que las funciones públicas del validador
detectan (o no detectan, según el caso) exactamente lo que deberían.

Objetivo (Sesión 7, tarea 7.1): que el propio framework de validación esté
sujeto a la misma disciplina de pruebas que exige a las skills y agentes
generados ("dogfooding").

Uso:
    python3 -m pytest tests/test_validate_repo.py -v
    python3 tests/test_validate_repo.py            # ejecución directa, sin pytest
"""

import sys
import tempfile
import textwrap
import shutil
import unittest
from pathlib import Path

# Permite importar scripts/validate_repo.py sin instalar el paquete
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import validate_repo as vr  # noqa: E402


VALID_SKILL_FRONTMATTER = """---
id: "apb-test-fixture-v1.0"
name: "Fixture de Test"
description: "Skill de prueba usada solo por la suite de tests del validador."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 1
inputs:
  - "input_ficticio"
outputs:
  - "output_ficticio"
created_date: "2026-06-24"
review_date: "2026-06-24"
---

# Fixture de Test
Cuerpo mínimo de prueba.
"""


class TestParseFrontmatter(unittest.TestCase):
    """Sesión 0: el parser debe basarse en pyyaml real, no en regex frágil."""

    def test_parses_valid_yaml_frontmatter(self):
        metadata, found = vr.parse_frontmatter(VALID_SKILL_FRONTMATTER)
        self.assertTrue(found)
        self.assertEqual(metadata["id"], "apb-test-fixture-v1.0")
        self.assertEqual(metadata["autonomy_level"], 1)

    def test_missing_frontmatter_is_reported_as_not_found(self):
        metadata, found = vr.parse_frontmatter("# Sin frontmatter\nSolo texto.\n")
        self.assertFalse(found)
        self.assertEqual(metadata, {})

    def test_malformed_yaml_is_reported_as_not_found(self):
        broken = "---\nid: \"sin cierre de comillas\n---\nCuerpo\n"
        metadata, found = vr.parse_frontmatter(broken)
        self.assertFalse(found)

    def test_frontmatter_that_is_not_a_mapping_is_rejected(self):
        # Un YAML válido pero que no es un dict (p.ej. una lista) no es un
        # frontmatter válido y debe tratarse igual que "no encontrado".
        not_a_dict = "---\n- item1\n- item2\n---\nCuerpo\n"
        metadata, found = vr.parse_frontmatter(not_a_dict)
        self.assertFalse(found)


class TestSecretAndBrandPatterns(unittest.TestCase):
    """Sesión 0/1: detección de secretos embebidos y marca corporativa
    incorrecta ('Islas Baleares' / dominios antiguos)."""

    def test_secret_patterns_detect_common_leak_shapes(self):
        samples_that_should_match = [
            'password = "Sup3rSecreto!"',
            'api_key: "abc123def456"',
            "secret = 'shh-dont-tell'",
            'connection_string: "Server=tcp:...;Password=x;"',
        ]
        for sample in samples_that_should_match:
            with self.subTest(sample=sample):
                matched = any(p.search(sample) for p in vr.SECRET_PATTERNS)
                self.assertTrue(matched, f"Debería detectar secreto en: {sample}")

    def test_secret_patterns_do_not_match_safe_references(self):
        safe_samples = [
            "Referencia a secretos mediante Azure Key Vault (`prov-akv-v1.0`)",
            "secret_reference: AKV://db-connection-string",
        ]
        for sample in safe_samples:
            with self.subTest(sample=sample):
                matched = any(p.search(sample) for p in vr.SECRET_PATTERNS)
                self.assertFalse(
                    matched, f"No debería marcar como secreto una referencia simbólica: {sample}"
                )

    def test_old_brand_patterns_detect_baleares_reference(self):
        sample = "Esta APB-E corresponde a la Administración Pública de las Islas Baleares"
        matched = any(p.search(sample) for p in vr.OLD_BRAND_PATTERNS)
        self.assertTrue(matched)

    def test_old_brand_patterns_do_not_flag_corrected_text(self):
        sample = "Autoridad Portuaria de Barcelona (APB), referencia APB-EXP-001"
        matched = any(p.search(sample) for p in vr.OLD_BRAND_PATTERNS)
        self.assertFalse(matched)

    def test_ip_pattern_detects_private_ranges(self):
        for ip in ["10.0.0.1", "172.16.5.4", "192.168.1.100"]:
            with self.subTest(ip=ip):
                self.assertIsNotNone(vr.IP_PATTERN.search(f"host: {ip}"))

    def test_ip_pattern_ignores_public_looking_ips(self):
        # 8.8.8.8 no es un rango privado de los que el validador vigila
        self.assertIsNone(vr.IP_PATTERN.search("host: 8.8.8.8"))


class TestIterComponentFiles(unittest.TestCase):
    """El iterador debe ignorar carpetas de plantillas/.git/node_modules."""

    def setUp(self):
        self.tmp_dir = Path(tempfile.mkdtemp(prefix="apb_validator_test_"))

    def tearDown(self):
        shutil.rmtree(self.tmp_dir, ignore_errors=True)

    def test_ignores_template_and_git_dirs(self):
        (self.tmp_dir / "real").mkdir()
        (self.tmp_dir / "real" / "a.md").write_text(VALID_SKILL_FRONTMATTER, encoding="utf-8")
        (self.tmp_dir / "templates").mkdir()
        (self.tmp_dir / "templates" / "ignored.md").write_text(VALID_SKILL_FRONTMATTER, encoding="utf-8")
        (self.tmp_dir / ".git").mkdir()
        (self.tmp_dir / ".git" / "also_ignored.md").write_text(VALID_SKILL_FRONTMATTER, encoding="utf-8")

        found = list(vr.iter_component_files(self.tmp_dir))
        found_names = {f.name for f in found}
        self.assertIn("a.md", found_names)
        self.assertNotIn("ignored.md", found_names)
        self.assertNotIn("also_ignored.md", found_names)


class TestValidateReferences(unittest.TestCase):
    """Sesión 4: referencias cruzadas rotas deben detectarse, tanto en
    frontmatter (skills/agents/...) como en menciones en el cuerpo."""

    def setUp(self):
        self.tmp_dir = Path(tempfile.mkdtemp(prefix="apb_validator_test_"))
        (self.tmp_dir / "agents").mkdir()
        (self.tmp_dir / "skills" / "apb-owned").mkdir(parents=True)
        (self.tmp_dir / "skills" / "third_party").mkdir(parents=True)
        (self.tmp_dir / "subagents").mkdir()
        (self.tmp_dir / "workflows").mkdir()
        (self.tmp_dir / "providers").mkdir()
        (self.tmp_dir / "wrappers").mkdir()
        (self.tmp_dir / "adapters").mkdir()

    def tearDown(self):
        shutil.rmtree(self.tmp_dir, ignore_errors=True)

    def test_frontmatter_reference_to_nonexistent_skill_is_an_error(self):
        agent_content = """---
id: "apb-agent-fixture-v1.0"
name: "Agente Fixture"
description: "Agente de prueba."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "orchestration"
autonomy_level: 1
skills:
  - "apb-dev-no-existe-v9.9"
runtime:
  - "claude"
human_review_points:
  - "Revisión humana"
created_date: "2026-06-24"
review_date: "2026-06-24"
---
# Agente Fixture
"""
        (self.tmp_dir / "agents" / "apb-agent-fixture-v1.0.md").write_text(agent_content, encoding="utf-8")

        all_ids = {"apb-agent-fixture-v1.0": "agents/apb-agent-fixture-v1.0.md"}
        result = vr.ValidationResult()
        vr.validate_references(self.tmp_dir, result, all_ids)

        messages = [i.message for i in result.errors]
        self.assertTrue(
            any("apb-dev-no-existe-v9.9" in m for m in messages),
            f"Se esperaba un error de referencia rota; errores encontrados: {messages}",
        )

    def test_body_reference_to_nonexistent_id_is_a_warning_not_error(self):
        # Las referencias rotas detectadas en el cuerpo (no en frontmatter
        # estructurado) son WARNING, no ERROR: pueden ser gaps de catálogo
        # legítimos pendientes de decisión humana (ver Sesión 7, Grupo C).
        skill_content = """---
id: "apb-dev-fixture-v1.0"
name: "Skill Fixture"
description: "Skill de prueba."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 1
inputs:
  - "x"
outputs:
  - "y"
created_date: "2026-06-24"
review_date: "2026-06-24"
---
# Skill Fixture
Usa `apb-agent-no-existe-v1.0` como agente consumidor.
"""
        (self.tmp_dir / "skills" / "apb-owned" / "apb-dev-fixture-v1.0.md").write_text(skill_content, encoding="utf-8")

        all_ids = {"apb-dev-fixture-v1.0": "skills/apb-owned/apb-dev-fixture-v1.0.md"}
        result = vr.ValidationResult()
        vr.validate_references(self.tmp_dir, result, all_ids)

        self.assertEqual(len(result.errors), 0)
        warning_messages = [i.message for i in result.warnings]
        self.assertTrue(any("apb-agent-no-existe-v1.0" in m for m in warning_messages))

    def test_valid_references_produce_no_issues(self):
        agent_content = """---
id: "apb-agent-fixture-v1.0"
name: "Agente Fixture"
description: "Agente de prueba."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "orchestration"
autonomy_level: 1
skills:
  - "apb-dev-fixture-v1.0"
runtime:
  - "claude"
human_review_points:
  - "Revisión humana"
created_date: "2026-06-24"
review_date: "2026-06-24"
---
# Agente Fixture
"""
        skill_content = """---
id: "apb-dev-fixture-v1.0"
name: "Skill Fixture"
description: "Skill de prueba."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 1
inputs:
  - "x"
outputs:
  - "y"
created_date: "2026-06-24"
review_date: "2026-06-24"
---
# Skill Fixture
"""
        (self.tmp_dir / "agents" / "apb-agent-fixture-v1.0.md").write_text(agent_content, encoding="utf-8")
        (self.tmp_dir / "skills" / "apb-owned" / "apb-dev-fixture-v1.0.md").write_text(skill_content, encoding="utf-8")

        all_ids = {
            "apb-agent-fixture-v1.0": "agents/apb-agent-fixture-v1.0.md",
            "apb-dev-fixture-v1.0": "skills/apb-owned/apb-dev-fixture-v1.0.md",
        }
        result = vr.ValidationResult()
        vr.validate_references(self.tmp_dir, result, all_ids)

        self.assertEqual(len(result.errors), 0)
        self.assertEqual(len(result.warnings), 0)


class TestCircularDependencies(unittest.TestCase):
    """Sesión 4: dos skills que se declaran mutuamente como depends_on deben
    reportarse como ERROR exactamente una vez (no duplicado A→B y B→A)."""

    def setUp(self):
        self.tmp_dir = Path(tempfile.mkdtemp(prefix="apb_validator_test_"))
        (self.tmp_dir / "skills" / "apb-owned").mkdir(parents=True)
        (self.tmp_dir / "skills" / "third_party").mkdir(parents=True)

    def tearDown(self):
        shutil.rmtree(self.tmp_dir, ignore_errors=True)

    def _write_skill(self, skill_id: str, depends_on):
        depends_yaml = "\n".join(f'  - "{d}"' for d in depends_on) if depends_on else "[]"
        content = f"""---
id: "{skill_id}"
name: "Fixture {skill_id}"
description: "Skill de prueba para dependencias circulares."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 1
inputs:
  - "x"
outputs:
  - "y"
depends_on:
{depends_yaml}
created_date: "2026-06-24"
review_date: "2026-06-24"
---
# Fixture {skill_id}
"""
        (self.tmp_dir / "skills" / "apb-owned" / f"{skill_id}.md").write_text(content, encoding="utf-8")

    def test_direct_circular_dependency_is_detected_once(self):
        self._write_skill("apb-dev-a-v1.0", ["apb-dev-b-v1.0"])
        self._write_skill("apb-dev-b-v1.0", ["apb-dev-a-v1.0"])

        result = vr.ValidationResult()
        vr.validate_no_circular_dependencies(self.tmp_dir, result)

        self.assertEqual(
            len(result.errors), 1,
            f"Se esperaba exactamente 1 error de circularidad, hubo {len(result.errors)}: "
            f"{[e.message for e in result.errors]}",
        )

    def test_linear_dependency_chain_is_not_circular(self):
        self._write_skill("apb-dev-a-v1.0", ["apb-dev-b-v1.0"])
        self._write_skill("apb-dev-b-v1.0", ["apb-dev-c-v1.0"])
        self._write_skill("apb-dev-c-v1.0", [])

        result = vr.ValidationResult()
        vr.validate_no_circular_dependencies(self.tmp_dir, result)

        self.assertEqual(len(result.errors), 0)


class TestStrictModeExemptions(unittest.TestCase):
    """Sesión 7: --strict no debe fallar solo por warnings 'source_commit:
    unverified' (política deliberada, GOVERNANCE.md §4.2), pero sí debe
    seguir fallando ante cualquier otro tipo de warning."""

    def test_unverified_source_commit_warning_is_exempt(self):
        issue = vr.ValidationIssue(
            level="WARNING",
            file="skills/third_party/example.md",
            message="source_commit pendiente de verificar (revisado manualmente "
                    "el 2026-06-24). Refinar a SHA real cuando haya acceso de red.",
        )
        self.assertTrue(vr.is_policy_exempt_warning(issue))

    def test_missing_folder_warning_is_not_exempt(self):
        issue = vr.ValidationIssue(
            level="WARNING",
            file="docs",
            message="Carpeta recomendada no encontrada: docs/",
        )
        self.assertFalse(vr.is_policy_exempt_warning(issue))

    def test_broken_body_reference_warning_is_not_exempt(self):
        issue = vr.ValidationIssue(
            level="WARNING",
            file="skills/apb-owned/example.md",
            message="Posible referencia rota en el cuerpo del documento: "
                    "'apb-fake-v9.9' no existe en el repo.",
        )
        self.assertFalse(vr.is_policy_exempt_warning(issue))


class TestValidateBidirectionalWiring(unittest.TestCase):
    """Test nº 24 — validate_bidirectional_wiring detecta subagentes huérfanos."""

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        self.repo = Path(self.tmpdir)
        # Estructura mínima de carpetas
        (self.repo / "agents").mkdir()
        (self.repo / "subagents").mkdir()
        (self.repo / "skills" / "apb-owned" / "development").mkdir(parents=True)
        (self.repo / "skills" / "third_party").mkdir(parents=True)
        (self.repo / "workflows").mkdir()
        (self.repo / "providers").mkdir()
        (self.repo / "wrappers").mkdir()
        (self.repo / "adapters").mkdir()
        (self.repo / "catalog").mkdir()
        (self.repo / "context").mkdir()
        (self.repo / "scripts").mkdir()

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmpdir)

    def _write(self, path, content):
        full = self.repo / path
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(content, encoding="utf-8")

    def test_subagent_orphan_warns(self):
        """Subagente declara parent_agent pero padre no lo lista → WARNING."""
        self._write("agents/apb-agent-test-v1.0.md", textwrap.dedent("""\
            ---
            id: "apb-agent-test-v1.0"
            name: "Test Agent"
            description: "Agente de prueba"
            version: "1.0.0"
            status: "draft"
            owner: "test"
            domain: "development"
            autonomy_level: 1
            skills: []
            subagents: []
            runtime: ["claude"]
            human_review_points: ["Revisar output"]
            created_date: "2026-01-01"
            review_date: "2026-07-01"
            ---
            # Test Agent
            ## Marcado IA obligatorio (POLICY_AI_USAGE §6)
            Generado por APB AI Framework.
        """))
        self._write("subagents/apb-sub-test-v1.0.md", textwrap.dedent("""\
            ---
            id: "apb-sub-test-v1.0"
            name: "Test Subagent"
            description: "Subagente de prueba"
            version: "1.0.0"
            status: "draft"
            owner: "test"
            domain: "development"
            autonomy_level: 2
            parent_agent: "apb-agent-test-v1.0"
            runtime: ["claude"]
            human_review_points: ["Revisar output"]
            created_date: "2026-01-01"
            review_date: "2026-07-01"
            ---
            # Test Subagent
            ## 🧠 Prompt de Sistema
            Eres un subagente de prueba.
            ## Marcado IA obligatorio (POLICY_AI_USAGE §6)
            Generado por APB AI Framework.
        """))
        result = vr.ValidationResult()
        vr.validate_bidirectional_wiring(self.repo, result)
        warning_msgs = [i.message for i in result.warnings]
        self.assertTrue(
            any("apb-sub-test-v1.0" in m and "apb-agent-test-v1.0" in m for m in warning_msgs),
            f"Se esperaba WARNING de wiring unidireccional, se obtuvo: {warning_msgs}"
        )

    def test_subagent_wired_no_warning(self):
        """Subagente con parent_agent correctamente listado en agente → sin WARNING."""
        self._write("agents/apb-agent-test-v1.0.md", textwrap.dedent("""\
            ---
            id: "apb-agent-test-v1.0"
            name: "Test Agent"
            description: "Agente de prueba"
            version: "1.0.0"
            status: "draft"
            owner: "test"
            domain: "development"
            autonomy_level: 1
            skills: []
            subagents:
              - "apb-sub-test-v1.0"
            runtime: ["claude"]
            human_review_points: ["Revisar output"]
            created_date: "2026-01-01"
            review_date: "2026-07-01"
            ---
            # Test Agent
            ## Marcado IA obligatorio (POLICY_AI_USAGE §6)
            Generado por APB AI Framework.
        """))
        self._write("subagents/apb-sub-test-v1.0.md", textwrap.dedent("""\
            ---
            id: "apb-sub-test-v1.0"
            name: "Test Subagent"
            description: "Subagente de prueba"
            version: "1.0.0"
            status: "draft"
            owner: "test"
            domain: "development"
            autonomy_level: 2
            parent_agent: "apb-agent-test-v1.0"
            runtime: ["claude"]
            human_review_points: ["Revisar output"]
            created_date: "2026-01-01"
            review_date: "2026-07-01"
            ---
            # Test Subagent
            ## 🧠 Prompt de Sistema
            Eres un subagente de prueba.
            ## Marcado IA obligatorio (POLICY_AI_USAGE §6)
            Generado por APB AI Framework.
        """))
        result = vr.ValidationResult()
        vr.validate_bidirectional_wiring(self.repo, result)
        self.assertEqual(result.warnings, [],
            f"No se esperaba ningún WARNING, se obtuvo: {result.warnings}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
