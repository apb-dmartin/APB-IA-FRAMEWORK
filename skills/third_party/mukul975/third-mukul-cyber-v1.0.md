---
id: "third-mukul-cyber-v1.0"
name: "Skill: Cybersecurity Skills (Mukul)"
description: "Conjunto de skills de ciberseguridad para análisis de vulnerabilidades, pentesting automatizado y generación de informes de seguridad."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
source_repo: "https://github.com/mukul975/Anthropic-Cybersecurity-Skills"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Skill: Cybersecurity Skills (Mukul)

---

## Descripción
Conjunto de skills de ciberseguridad para análisis de vulnerabilidades, pentesting automatizado y generación de informes de seguridad.

## Capacidades
- Análisis estático de seguridad (SAST)
- Identificación de vulnerabilidades OWASP Top 10
- Generación de informes de pentesting
- Recomendaciones de mitigación

## Inputs
- `source_code`: código fuente a analizar
- `tech_stack`: stack tecnológico
- `compliance_framework`: marco de cumplimiento (ENS, ISO 27001)

## Outputs
- `security_report.md`
- `vulnerability_assessment.md`
- `mitigation_plan.md`

## Restricciones
- No ejecuta exploits reales
- Análisis estático únicamente
- Requiere validación por Security Architect Agent

## Adaptaciones APB
- Integración con `apb-sec-owasp-v1.0`
- Alineación con `apb-sec-ens-v1.0`
- Workflow `apb-wf-risk-exception-v1.0`

## Ejemplo de Uso
```
Invocar: third-mukul-cyber-v1.0
Input: { source_code: "/repos/app", tech_stack: ".NET", compliance: "ENS" }
Output: security_report.md con vulnerabilidades y mitigaciones APB
```

---
*Adaptado por APB AI Framework. Licencia MIT original respetada.*
