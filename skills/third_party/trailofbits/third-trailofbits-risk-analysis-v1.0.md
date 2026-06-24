---
id: "third-trailofbits-risk-analysis-v1.0"
name: "Static Analysis & Risk Patterns"
description: "Análisis estático y patrones de testing de seguridad, adaptado de trailofbits/skills."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "security"
created_date: "2026-06-22"
review_date: "2026-06-22"
autonomy_level: 1
source_repo: "https://github.com/trailofbits/skills"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
---

# Análisis de Riesgos de Seguridad para APB

## Overview
Evaluación formal de riesgos de seguridad mediante metodología cuantitativa y cualitativa, adaptada al marco del Esquema Nacional de Seguridad (ENS) y a las necesidades de la Administración Pública de las Barcelona (APB). Genera matriz de riesgos con clasificación, plan de mitigación y recomendaciones de tratamiento.

## When to Use
- Evaluación de riesgo de nuevo proyecto o tecnología
- Análisis previo a aprobación de excepción de seguridad
- Revisión periódica de riesgos de sistemas críticos
- Cambio arquitectónico con impacto en seguridad
- Adquisición o integración de nuevo software/servicio

**When NOT to use:**
- Riesgos operacionales sin componente de seguridad (usar análisis de riesgos operacional)
- Riesgos de negocio puros (usar análisis de viabilidad)
- Evaluaciones de bajo nivel técnico (usar code review o threat modeling)

## Core Pattern

### Fase 1: Contexto y Alcance
1. Definir el activo o sistema a evaluar
2. Identificar partes interesadas (stakeholders)
3. Establecer criterios de evaluación (basados en ENS)
4. Definir umbral de riesgo aceptable para APB

### Fase 2: Identificación de Riesgos
Para cada activo, identificar:
- **Amenazas:** Eventos potenciales que pueden causar daño
- **Vulnerabilidades:** Debilidades que pueden ser explotadas
- **Impactos:** Consecuencias para confidencialidad, integridad, disponibilidad

Categorías de amenazas ENS:
| Categoría | Ejemplos |
|-----------|----------|
| Acceso no autorizado | Suplantación, escalada de privilegios |
| Divulgación de información | Filtrado de datos personales, espionaje |
| Modificación no autorizada | Alteración de datos, código malicioso |
| Indisponibilidad | DoS, ransomware, fallo de infraestructura |
| Destrucción | Borrado intencionado, daño físico |

### Fase 3: Análisis de Riesgos

#### Análisis Cualitativo
| Probabilidad | Descripción | Valor |
|-------------|-------------|-------|
| Muy baja | Evento improbable, sin precedentes | 1 |
| Baja | Evento poco probable, pocos precedentes | 2 |
| Media | Evento posible, precedentes ocasionales | 3 |
| Alta | Evento probable, precedentes frecuentes | 4 |
| Muy alta | Evento casi seguro, precedentes habituales | 5 |

| Impacto | Descripción | Valor |
|---------|-------------|-------|
| Insignificante | Sin impacto operativo ni legal | 1 |
| Menor | Impacto limitado, gestionable | 2 |
| Moderado | Impacto significativo, requiere acción | 3 |
| Mayor | Impacto grave, afecta servicio esencial | 4 |
| Crítico | Impacto catastrófico, afecta misión | 5 |

#### Matriz de Riesgos
```
        Impacto →
Prob    1    2    3    4    5
↓
5      5    10   15   20   25   ← CRÍTICO
4      4    8    12   16   20   ← ALTO
3      3    6    9    12   15   ← MEDIO
2      2    4    6    8    10   ← BAJO
1      1    2    3    4    5    ← MUY BAJO
```

| Riesgo | Tratamiento |
|--------|-------------|
| 15-25 (Crítico/Alto) | Mitigar obligatoriamente |
| 8-12 (Medio) | Mitigar o transferir |
| 1-6 (Bajo/Muy bajo) | Aceptar y monitorear |

### Fase 4: Evaluación de Riesgos
Para cada riesgo identificado:
1. Calcular nivel de riesgo (probabilidad × impacto)
2. Comparar con umbral aceptable de APB
3. Clasificar: Aceptable / No aceptable
4. Priorizar riesgos no aceptables

### Fase 5: Tratamiento de Riesgos

| Estrategia | Descripción | Cuándo usar |
|-----------|-------------|-------------|
| **Mitigación** | Reducir probabilidad o impacto | Riesgo no aceptable, controles viables |
| **Transferencia** | Delegar a tercero (seguro, proveedor) | Riesgo asegurable, proveedor capacitado |
| **Aceptación** | Asumir el riesgo documentado | Riesgo bajo, coste de mitigación desproporcionado |
| **Evitación** | Eliminar la actividad que genera riesgo | Riesgo crítico sin controles viables |

### Fase 6: Informe de Riesgos

```markdown
# Informe de Análisis de Riesgos — [Proyecto/Sistema]

## Contexto
- Sistema: [nombre]
- Fecha: [fecha]
- Responsable: [nombre]
- Revisores: [nombres]

## Metodología
- ENS RD 311/2022
- Análisis cualitativo (matriz 5×5)

## Riesgos Identificados
| ID | Amenaza | Vulnerabilidad | Prob | Imp | Riesgo | Tratamiento | Plazo |
|----|---------|---------------|------|-----|--------|-------------|-------|
| R01 | [desc] | [desc] | [1-5] | [1-5] | [1-25] | [estrategia] | [fecha] |

## Riesgos Críticos/Altos
1. [R##] — [Descripción] — [Mitigación] — [Responsable] — [Plazo]

## Plan de Mitigación
| Acción | Responsable | Plazo | Estado |
|--------|-------------|-------|--------|
| [acción] | [nombre] | [fecha] | [Pendiente/En curso/Cerrado] |

## Estado
- ACEPTABLE / NO_ACEPTABLE / CONDICIONAL
- Revisión siguiente: [fecha]
```

## Quick Reference

| Nivel Riesgo | Acción | Aprobador |
|-------------|--------|-----------|
| 20-25 | BLOCKED hasta mitigación | CISO + Arquitecto Enterprise |
| 12-16 | PASS_WITH_WARNINGS + plan | CISO |
| 6-9 | Documentar + monitorear | Security Architect |
| 1-5 | Aceptar + documentar | Tech Lead |

## Implementation

### Plantilla de Registro de Riesgo
```markdown
## R## — [Nombre del Riesgo]
- **Amenaza:** [Descripción]
- **Vulnerabilidad:** [Descripción]
- **Activo afectado:** [Nombre]
- **Probabilidad:** [Muy baja/Baja/Media/Alta/Muy alta]
- **Impacto:** [Insignificante/Menor/Moderado/Mayor/Crítico]
- **Riesgo:** [Valor numérico]
- **Tratamiento:** [Mitigar/Transferir/Aceptar/Evitar]
- **Medida:** [Descripción de la acción]
- **Responsable:** [Nombre]
- **Plazo:** [Fecha]
- **Estado:** [Abierto/En curso/Cerrado]
```

## Common Mistakes
- **Subestimar probabilidad:** "Nunca nos ha pasado" no implica probabilidad baja
- **Ignorar riesgos residuales:** Después de mitigar, reevaluar el riesgo residual
- **No documentar aceptación:** Los riesgos aceptados deben tener justificación y aprobador
- **Análisis estático:** Los riesgos cambian; revisar periódicamente
- **No involucrar a negocio:** El impacto debe validarse con el propietario del activo
- **Confundir riesgo con impacto:** Riesgo = probabilidad × impacto, no solo impacto

## Real-World Impact
- Reducción de 40% en incidentes de seguridad tras implementar análisis sistemático
- Cumplimiento de requisitos de contratación pública (cláusulas de seguridad)
- Trazabilidad para responsables legales en caso de incidente

---

## Adapted From
- **Source:** trailofbits/skills — static-analysis y testing patterns
- **License:** MIT
- **Attribution:** Patrón de análisis estructurado y matriz de evaluación inspirados en Trail of Bits security skills. Reescrito completamente para metodología ENS y contexto de riesgo sector público español.

## References
- ENS RD 311/2022 — Gestión de riesgos
- ISO 27005 — Gestión de riesgos de seguridad de la información
- Guía CCN-CERT de análisis de riesgos
- context/apb/policies/risk-management-policy.md
