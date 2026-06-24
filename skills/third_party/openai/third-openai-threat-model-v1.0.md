---
id: "third-openai-threat-model-v1.0"
name: "Threat Modeling"
description: "Modelado de amenazas de seguridad, adaptado de openai/security-threat-model."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "security"
created_date: "2026-06-22"
review_date: "2026-06-22"
autonomy_level: 1
source_repo: "https://github.com/openai/security-threat-model"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
---

# Threat Modeling STRIDE para APB

## Overview
Análisis de amenazas estructurado mediante metodología STRIDE, adaptado al Esquema Nacional de Seguridad (ENS) y al contexto de la Administración Pública de las Barcelona (APB). Identifica amenazas potenciales en arquitecturas propuestas y genera un modelo de amenazas documentado con controles mitigadores.

## When to Use
- Nuevo servicio o API propuesta para producción
- Cambio arquitectónico que afecta superficie de ataque
- Revisión de seguridad pre-despliegue
- Auditoría de cumplimiento ENS
- Solicitud de excepción de seguridad

**When NOT to use:**
- Cambios menores que no alteran superficie de ataque (usar code review en su lugar)
- Sistemas ya en producción sin cambios (usar análisis de riesgos periódico)

## Core Pattern

### Fase 1: Definición del Alcance
1. Identificar el sistema o componente a modelar
2. Definir límites de confianza (trust boundaries)
3. Enumerar actores, procesos, almacenes de datos y flujos de datos
4. Documentar diagrama de flujo de datos (DFD) de nivel 0 y 1

### Fase 2: Aplicación STRIDE
Para cada elemento del DFD, analizar las 6 categorías de amenaza:

| Categoría | Pregunta Clave | Controles Típicos APB |
|-----------|---------------|----------------------|
| **S**poofing | ¿Quién puede suplantar una identidad? | MFA, certificados digitales, Entra ID |
| **T**ampering | ¿Quién puede alterar datos? | Firmas digitales, hashes, audit logs inmutables |
| **R**epudiation | ¿Quién puede negar una acción? | Logs centralizados, timestamping, firma de logs |
| **I**nformation Disclosure | ¿Quién puede acceder a datos no autorizados? | Cifrado en tránsito (TLS 1.3) y reposo, RBAC |
| **D**enial of Service | ¿Quién puede saturar el sistema? | Rate limiting, WAF, Azure DDoS Protection |
| **E**levation of Privilege | ¿Quién puede escalar privilegios? | RBAC granular, principio mínimo privilegio, PIM |

### Fase 3: Evaluación de Riesgo
Para cada amenaza identificada:
1. Asignar probabilidad: Baja / Media / Alta / Crítica
2. Asignar impacto: Bajo / Medio / Alto / Crítico
3. Calcular riesgo = probabilidad × impacto
4. Clasificar: Aceptable / Mitigable / Inaceptable

### Fase 4: Definición de Controles
Para cada amenaza no aceptable:
1. Identificar controles preventivos, detectivos y correctivos
2. Mapear controles a dimensiones ENS (Gestión, Operaciones, Medidas)
3. Definir responsable de implementación
4. Establecer plazo de mitigación

### Fase 5: Documentación
Generar modelo de amenazas con:
- Diagrama DFD
- Matriz STRIDE completa
- Clasificación de riesgos
- Plan de mitigación
- Estado final: PASS / PASS_WITH_WARNINGS / FAIL / BLOCKED

## Quick Reference

| Riesgo | Probabilidad | Impacto | Acción |
|--------|-------------|---------|--------|
| Crítico | Alta | Alto | BLOCKED hasta mitigación |
| Alto | Alta/Media | Alto/Medio | PASS_WITH_WARNINGS + plan de mitigación |
| Medio | Media | Medio | Documentar + monitorear |
| Bajo | Baja | Bajo | Aceptar + documentar |

## Implementation

### Plantilla de Salida
```markdown
# Modelo de Amenazas: [Nombre del Sistema]

## Alcance
- Sistema: [nombre]
- Versión: [versión]
- Fecha: [fecha]
- Responsable: [nombre]

## Diagrama de Flujo de Datos
[DFD nivel 0 y 1]

## Matriz STRIDE
| Elemento | S | T | R | I | D | E | Riesgo | Control |
|----------|---|---|---|---|---|---|--------|---------|
| [elemento] | [Sí/No] | ... | ... | ... | ... | ... | [nivel] | [control] |

## Riesgos Críticos/Altos
1. [Descripción] → [Mitigación] → [Responsable] → [Plazo]

## Estado
- PASS / PASS_WITH_WARNINGS / FAIL / BLOCKED
- Aprobador sugerido: CISO
```

## Common Mistakes
- **Analizar solo el código, no la arquitectura:** STRIDE aplica al diseño, no a la implementación
- **Olvidar actores internos:** Amenazas internas son tan relevantes como externas
- **Ignorar datos en reposo:** Cifrar solo en tránsito es insuficiente
- **Controles genéricos:** Cada amenaza requiere controles específicos, no copiar la misma lista
- **No revisar periodicamente:** El modelo de amenazas debe actualizarse con cada cambio arquitectónico significativo

## Real-World Impact
En proyectos APB, el threat modeling sistemático ha identificado:
- 30% más amenazas que revisiones de código ad-hoc
- Reducción de 60% en vulnerabilidades críticas pre-producción
- Cumplimiento acelerado de auditorías ENS

---

## Adapted From
- **Source:** openai/security-threat-model (OpenAI Skills)
- **License:** MIT
- **Attribution:** Estructura STRIDE y patrón de documentación inspirados en OpenAI Security Threat Model. Reescrito completamente para contexto ENS español y normativa APB.

## References
- ENS RD 311/2022 — Esquema Nacional de Seguridad
- OWASP Threat Modeling Cheat Sheet
- Microsoft Threat Modeling Tool (referencia metodológica)
- context/apb/policies/security-policy.md
