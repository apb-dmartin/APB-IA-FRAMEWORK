---
id: "third-anthropic-business-discovery-v1.0"
name: "Skill: Business Discovery (Anthropic)"
description: "Skill de terceros para facilitar sesiones de descubrimiento de negocio mediante entrevistas estructuradas. Extrae requisitos funcionales, identifica stakeholders y genera documentación preliminar de dominio."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
source_repo: "https://github.com/anthropics/skills"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Skill: Business Discovery (Anthropic)

---

## Descripción
Skill de terceros para facilitar sesiones de descubrimiento de negocio mediante entrevistas estructuradas. Extrae requisitos funcionales, identifica stakeholders y genera documentación preliminar de dominio.

## Capacidades
- Entrevista guiada con prompts estructurados
- Extracción automática de requisitos desde conversación
- Generación de user stories iniciales
- Identificación de riesgos de negocio

## Inputs
- `transcript` o `interview_notes`: notas de la entrevista
- `domain_context`: contexto del dominio de negocio
- `stakeholder_list`: lista de interlocutores

## Outputs
- `business_requirements.md`
- `user_stories_draft.md`
- `risk_register_business.md`

## Restricciones
- No sustituye al análisis funcional humano
- Requiere validación por Business Analyst Agent
- Datos sensibles deben anonimizarse previamente

## Adaptaciones APB
- Formato de salida adaptado a plantilla `apb-disc-business-v1.0`
- Integración con workflow `apb-wf-legacy-onboarding-v1.0`
- Metadatos ENS añadidos para trazabilidad

## Ejemplo de Uso
```
Invocar: third-anthropic-business-discovery-v1.0
Input: { interview_notes: "...", domain: "Seguros" }
Output: business_requirements.md adaptado a formato APB
```

---
*Adaptado por APB AI Framework. Licencia MIT original respetada.*
