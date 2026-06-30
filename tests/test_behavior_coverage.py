"""
Tests de cobertura de comportamiento — APB AI Framework.
Valida que los agentes críticos tienen al menos 1 caso documentado
en tests/test_agent_behavior.md.
"""
import os
import re
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AGENTS_DIR = os.path.join(REPO_ROOT, "agents")
BEHAVIOR_FILE = os.path.join(REPO_ROOT, "tests", "test_agent_behavior.md")

CRITICAL_AGENTS = [
    "apb-agent-incident-support-v1.0",
    "apb-agent-qa-auto-v1.0",
    "apb-agent-governance-v1.0",
    "apb-agent-implementer-v1.0",
    "apb-agent-technical-architect-v1.0",
    "apb-agent-release-manager-v1.0",
]


def _read_behavior_file():
    with open(BEHAVIOR_FILE, encoding="utf-8") as f:
        return f.read()


def _extract_covered_agents(content):
    """Extrae los IDs de agentes mencionados en secciones 'Agente bajo prueba'."""
    return set(re.findall(r"Agente bajo prueba: `(apb-agent-[\w.-]+)`", content))


def _extract_cases(content):
    """Extrae los títulos de caso del archivo de behavior tests."""
    return re.findall(r"^## Caso \d+", content, re.MULTILINE)


class TestBehaviorCoverage(unittest.TestCase):

    def test_behavior_file_exists(self):
        """El archivo de tests de comportamiento debe existir."""
        self.assertTrue(
            os.path.isfile(BEHAVIOR_FILE),
            f"No se encontró {BEHAVIOR_FILE}",
        )

    def test_behavior_file_has_at_least_one_case(self):
        """El archivo debe tener al menos 1 caso documentado."""
        content = _read_behavior_file()
        cases = _extract_cases(content)
        self.assertGreater(
            len(cases),
            0,
            "test_agent_behavior.md no contiene ningún caso (busca '## Caso N')",
        )

    def test_critical_agents_have_coverage(self):
        """Todos los agentes críticos deben tener al menos 1 caso en test_agent_behavior.md."""
        content = _read_behavior_file()
        covered = _extract_covered_agents(content)
        missing = [a for a in CRITICAL_AGENTS if a not in covered]
        self.assertEqual(
            missing,
            [],
            f"Los siguientes agentes críticos no tienen casos de comportamiento: {missing}",
        )

    def test_golden_output_file_exists(self):
        """El archivo de Golden Output Tests debe existir."""
        got_file = os.path.join(REPO_ROOT, "tests", "golden_output_tests.md")
        self.assertTrue(
            os.path.isfile(got_file),
            "No se encontró tests/golden_output_tests.md",
        )

    def test_non_critical_agents_coverage_warning(self):
        """Emite WARNING (no ERROR) para agentes no críticos sin cobertura."""
        content = _read_behavior_file()
        covered = _extract_covered_agents(content)

        all_agent_ids = set()
        if os.path.isdir(AGENTS_DIR):
            for fname in os.listdir(AGENTS_DIR):
                if fname.endswith(".md"):
                    m = re.match(r"^(apb-agent-[\w-]+)\.md$", fname)
                    if m:
                        all_agent_ids.add(m.group(1))

        uncovered = all_agent_ids - covered - set(CRITICAL_AGENTS)
        if uncovered:
            import warnings
            warnings.warn(
                f"{len(uncovered)} agentes sin cobertura de comportamiento "
                f"(no críticos — WARNING, no error): {sorted(uncovered)}",
                UserWarning,
            )
        # No falla — solo informa. El test siempre pasa.
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
