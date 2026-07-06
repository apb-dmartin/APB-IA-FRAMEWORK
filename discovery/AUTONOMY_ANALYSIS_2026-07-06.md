# Autonomy Level 2/3 Candidates Analysis

**Date:** 2026-07-06
**Total Components:** 350
**Level 2 Candidates:** 3

## Summary by Level

- **Level 0:** 1 components
- **Level 1:** 318 components
- **Level 2:** 31 components

## Recommended Promotions to Level 2

| ID | Name | Type | Work | Risk | Reason |
|----|----|------|------|------|--------|
| `apb-agent-accessibility-auditor-v1.0` | Accessibility Auditor | agent | read-only | Low | Audit/reporting (read-only, post-execution review) |
| `apb-ops-dependency-audit-v1.0` | Auditoría de Dependencias y Vulnerabilidades | unknown | read-only | Low | Audit/reporting (read-only, post-execution review) |
| `apb-wf-accessibility-audit-v1.0` | Accessibility Audit | workflow | read-only | Low | Audit/reporting (read-only, post-execution review) |

## Risk Assessment

### Low Risk Candidates (Safe to promote)

- `apb-agent-accessibility-auditor-v1.0` — Audit/reporting (read-only, post-execution review)
- `apb-ops-dependency-audit-v1.0` — Audit/reporting (read-only, post-execution review)
- `apb-wf-accessibility-audit-v1.0` — Audit/reporting (read-only, post-execution review)

### Medium Risk Candidates (Review before promotion)


## Implementation Gaps for Enforcement

Current framework limitations preventing real Level 2 enforcement:

1. **No timeout policy** — Level 2 agent can hang indefinitely
2. **No loop detection** — circular dependencies not detected
3. **No hardcoded limits** — Level 2 agent can still `git push --force`
4. **No async messaging** — all communication via Git/Jira (synchronous, coupled)

**Recommendation:** Implement before promoting components to Level 2.
