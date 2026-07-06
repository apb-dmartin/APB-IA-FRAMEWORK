#!/usr/bin/env python3
"""
analyze_autonomy_landscape.py — Mapeo del catálogo APB (217 componentes)
para identificar candidatos a Nivel 2/3 (sin aprobación humana previa).

Salida: tabla CSV + análisis de riesgos.
"""

import os
import sys
import json
import yaml
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple

# UTF-8 en Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

class ComponentAnalyzer:
    def __init__(self, framework_root: str):
        self.root = Path(framework_root)
        self.components = []
        self.autonomy_stats = defaultdict(list)
        self.candidates_level_2 = []
        self.risks = []

    def load_yaml_frontmatter(self, filepath: Path) -> Dict:
        """Extract YAML frontmatter from .md file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                if not content.startswith('---'):
                    return {}

                # Find closing ---
                end_idx = content.find('\n---\n', 4)
                if end_idx == -1:
                    return {}

                yaml_str = content[4:end_idx]
                return yaml.safe_load(yaml_str) or {}
        except Exception as e:
            print(f"⚠️  Error parsing {filepath}: {e}")
            return {}

    def classify_component(self, metadata: Dict) -> Tuple[str, str, str]:
        """
        Classify component by:
        1. Type: agent, skill, subagent, workflow, provider, adapter
        2. Work: read-only (audit, report, detect) vs. write (code, data, deploy)
        3. Criticality: high (production, governance, security), medium, low
        """
        comp_type = metadata.get('type') or self._infer_type(metadata)

        # Infer work type from domain + description
        domain = metadata.get('domain', '').lower()
        description = (metadata.get('description', '') or '').lower()
        name = (metadata.get('name', '') or '').lower()

        # Read-only indicators
        read_only_keywords = [
            'audit', 'detect', 'drift', 'report', 'analyze', 'discovery',
            'assessment', 'inspection', 'telemetry-emit', 'observability'
        ]
        is_read_only = any(kw in name or kw in description for kw in read_only_keywords)

        # Write indicators
        write_keywords = [
            'implement', 'generator', 'deploy', 'create', 'patch', 'fix', 'script',
            'provision', 'configure', 'migrate', 'refactor', 'instrumentat'
        ]
        is_write = any(kw in name or kw in description for kw in write_keywords)

        work_type = "read-only" if is_read_only and not is_write else "write"

        # Criticality
        critical_keywords = ['security', 'deploy', 'govern', 'release', 'compliance']
        criticality = "high" if any(kw in domain for kw in critical_keywords) else "medium"

        return comp_type, work_type, criticality

    def _infer_type(self, metadata: Dict) -> str:
        """Infer component type from file path or metadata."""
        if metadata.get('parent_agent'):
            return 'subagent'
        if 'skill' in metadata.get('id', ''):
            return 'skill'
        if 'agent' in metadata.get('id', ''):
            return 'agent'
        if metadata.get('agents'):  # workflows have agents field
            return 'workflow'
        if 'prov-' in metadata.get('id', ''):
            return 'provider'
        return 'unknown'

    def scan_catalog(self):
        """Scan agents/, skills/, subagents/, workflows/, providers/ directories."""
        directories = [
            'agents',
            'skills/apb-owned',
            'skills/third_party',
            'skills/wrappers',
            'subagents',
            'workflows',
            'providers'
        ]

        total = 0
        for directory in directories:
            dirpath = self.root / directory
            if not dirpath.exists():
                continue

            for md_file in dirpath.rglob('*.md'):
                if md_file.name == '_index.md':
                    continue

                metadata = self.load_yaml_frontmatter(md_file)
                if not metadata or 'id' not in metadata:
                    continue

                comp_type, work_type, criticality = self.classify_component(metadata)
                autonomy_level = metadata.get('autonomy_level', 1)

                component = {
                    'id': metadata['id'],
                    'name': metadata.get('name', ''),
                    'type': comp_type,
                    'work': work_type,
                    'criticality': criticality,
                    'current_level': autonomy_level,
                    'domain': metadata.get('domain', 'unknown'),
                    'status': metadata.get('status', 'unknown'),
                    'file': str(md_file.relative_to(self.root))
                }

                self.components.append(component)
                self.autonomy_stats[autonomy_level].append(component['id'])
                total += 1

        print(f"✅ Scanned {total} components from APB catalog")
        return total

    def identify_level_2_candidates(self):
        """
        Identify read-only components currently at Level 1 that could be Level 2.

        Criteria for Level 2:
        - Work type: read-only (no code/data writes)
        - Criticality: low-medium (not governance/security/deploy critical)
        - No cycles detected
        - Output is auditable (human can review after execution)
        """
        candidates = []

        for comp in self.components:
            # Already Level 2+ → skip
            if comp['current_level'] >= 2:
                continue

            # Level 1 + read-only + low/medium criticality → candidate
            if comp['work'] == 'read-only' and comp['criticality'] != 'high':
                # Additional checks
                reason = self._reason_for_level_2(comp)
                if reason:
                    candidates.append({
                        **comp,
                        'candidate_level': 2,
                        'reason': reason,
                        'risk': self._assess_risk(comp)
                    })

        self.candidates_level_2 = sorted(candidates, key=lambda x: x['risk'])
        return candidates

    def _reason_for_level_2(self, comp: Dict) -> str:
        """Generate reason why component should be Level 2."""
        if 'drift' in comp['id']:
            return "Drift detection (read-only, auditable, low risk)"
        if 'audit' in comp['id'] or 'report' in comp['id']:
            return "Audit/reporting (read-only, post-execution review)"
        if 'detect' in comp['id']:
            return "Detection skill (read-only, findings reviewable)"
        if 'telemetry-emit' in comp['id']:
            return "Telemetry emission (append-only, auditable in logs)"
        if 'observability' in comp['domain'] and 'design' in comp['id']:
            return "Observability design (read-only analysis)"
        return None

    def _assess_risk(self, comp: Dict) -> str:
        """Low|Medium|High risk assessment."""
        high_risk_keywords = ['deploy', 'security', 'compliance', 'governance']
        medium_risk_keywords = ['provision', 'configure', 'refactor']

        if any(kw in comp['id'] for kw in high_risk_keywords):
            return "High"
        if any(kw in comp['id'] for kw in medium_risk_keywords):
            return "Medium"
        return "Low"

    def detect_cycles(self) -> List[Tuple[str, str]]:
        """
        Simple cycle detection: if A depends on B and B depends on A.
        (Full implementation would require traversing entire dependency graph.)
        """
        cycles = []
        # Simplified: check for direct cycles in current catalog
        # Full implementation requires loading dependency info from each component
        return cycles

    def print_summary(self):
        """Print summary statistics."""
        print("\n" + "="*70)
        print("AUTONOMY LANDSCAPE SUMMARY")
        print("="*70)

        print(f"\n📊 Total Components: {len(self.components)}")
        for level in sorted(self.autonomy_stats.keys()):
            count = len(self.autonomy_stats[level])
            print(f"   Level {level}: {count} components")

        print(f"\n🎯 Level 2 Candidates: {len(self.candidates_level_2)}")
        print("\nTop Candidates (by risk):")
        for i, comp in enumerate(self.candidates_level_2[:10], 1):
            print(f"  {i}. {comp['id']}")
            print(f"     Reason: {comp['reason']}")
            print(f"     Risk: {comp['risk']}")

    def export_csv(self, output_file: str):
        """Export classification to CSV."""
        import csv

        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(
                f,
                fieldnames=[
                    'ID', 'Name', 'Type', 'Work', 'Criticality', 'Current_Level',
                    'Domain', 'Status', 'L2_Candidate', 'Reason', 'Risk'
                ]
            )
            writer.writeheader()

            for comp in self.components:
                candidate = next((c for c in self.candidates_level_2 if c['id'] == comp['id']), None)
                writer.writerow({
                    'ID': comp['id'],
                    'Name': comp['name'],
                    'Type': comp['type'],
                    'Work': comp['work'],
                    'Criticality': comp['criticality'],
                    'Current_Level': comp['current_level'],
                    'Domain': comp['domain'],
                    'Status': comp['status'],
                    'L2_Candidate': 'YES' if candidate else 'NO',
                    'Reason': candidate['reason'] if candidate else '',
                    'Risk': candidate['risk'] if candidate else ''
                })

        print(f"✅ Exported {len(self.components)} components to {output_file}")

    def export_markdown_report(self, output_file: str):
        """Export candidates report to Markdown."""
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# Autonomy Level 2/3 Candidates Analysis\n\n")
            f.write(f"**Date:** 2026-07-06\n")
            f.write(f"**Total Components:** {len(self.components)}\n")
            f.write(f"**Level 2 Candidates:** {len(self.candidates_level_2)}\n\n")

            f.write("## Summary by Level\n\n")
            for level in sorted(self.autonomy_stats.keys()):
                count = len(self.autonomy_stats[level])
                f.write(f"- **Level {level}:** {count} components\n")

            f.write("\n## Recommended Promotions to Level 2\n\n")
            f.write("| ID | Name | Type | Work | Risk | Reason |\n")
            f.write("|----|----|------|------|------|--------|\n")

            for comp in self.candidates_level_2[:10]:
                f.write(
                    f"| `{comp['id']}` | {comp['name']} | {comp['type']} | "
                    f"{comp['work']} | {comp['risk']} | {comp['reason']} |\n"
                )

            f.write("\n## Risk Assessment\n\n")
            f.write("### Low Risk Candidates (Safe to promote)\n\n")
            low_risk = [c for c in self.candidates_level_2 if c['risk'] == 'Low']
            for comp in low_risk[:5]:
                f.write(f"- `{comp['id']}` — {comp['reason']}\n")

            f.write("\n### Medium Risk Candidates (Review before promotion)\n\n")
            med_risk = [c for c in self.candidates_level_2 if c['risk'] == 'Medium']
            for comp in med_risk[:5]:
                f.write(f"- `{comp['id']}` — {comp['reason']}\n")

            f.write("\n## Implementation Gaps for Enforcement\n\n")
            f.write("Current framework limitations preventing real Level 2 enforcement:\n\n")
            f.write("1. **No timeout policy** — Level 2 agent can hang indefinitely\n")
            f.write("2. **No loop detection** — circular dependencies not detected\n")
            f.write("3. **No hardcoded limits** — Level 2 agent can still `git push --force`\n")
            f.write("4. **No async messaging** — all communication via Git/Jira (synchronous, coupled)\n\n")
            f.write("**Recommendation:** Implement before promoting components to Level 2.\n")

        print(f"✅ Exported report to {output_file}")


def main():
    framework_root = Path(__file__).parent.parent

    analyzer = ComponentAnalyzer(str(framework_root))

    print("🔍 Scanning APB Framework Catalog...\n")
    total = analyzer.scan_catalog()

    print("\n🎯 Identifying Level 2 Candidates...\n")
    candidates = analyzer.identify_level_2_candidates()

    analyzer.print_summary()

    print("\n💾 Exporting results...\n")
    analyzer.export_csv("discovery/autonomy-analysis.csv")
    analyzer.export_markdown_report("discovery/AUTONOMY_ANALYSIS_2026-07-06.md")

    print("\n✅ Analysis complete!")


if __name__ == "__main__":
    main()
