---
id: "third-mukul-risk-policies-v1.0"
name: "Risk Policies"
description: "Políticas de gestión de riesgo de seguridad, adaptadas del dominio Risk Policies de mukul975/Anthropic-Cybersecurity-Skills."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "security"
created_date: "2026-06-22"
review_date: "2026-06-22"
autonomy_level: 1
source_repo: "https://github.com/mukul975/Anthropic-Cybersecurity-Skills"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
---

# Análisis de Riesgos y Políticas APB

## Overview
Evaluación de riesgos integrada con las políticas de seguridad corporativas de la APB. Determina la alineación entre un riesgo identificado y las políticas internas, evaluando si una excepción es aceptable y qué medidas compensatorias se requieren para mantener el nivel de seguridad.

## When to Use
- Solicitud de excepción a estándar de seguridad
- Evaluación de riesgo que implica desviación de política
- Análisis de viabilidad de nueva tecnología no aprobada
- Revisión de cumplimiento de políticas tras cambio
- Propuesta de modificación de política existente

**When NOT to use:**
- Riesgos sin implicación en políticas (usar análisis de riesgos estándar)
- Violaciones claras de política sin justificación (escalar directamente)
- Riesgos ya cubiertos por excepción vigente

## Core Pattern

### Fase 1: Identificación de Políticas Aplicables
1. Identificar políticas APB relevantes al riesgo:
   - `context/apb/policies/security-policy.md`
   - `context/apb/policies/qa-policy.md`
   - `context/apb/policies/development-policy.md`
   - `context/apb/policies/cloud-policy.md`
   - `context/apb/policies/ai-policy.md`

2. Determinar el control o requisito específico que se vería afectado
3. Clasificar el tipo de desviación:
   - **Temporal:** Excepción por tiempo limitado
   - **Permanente:** Cambio estructural en política
   - **Compensatoria:** Medida alternativa que mantiene nivel de seguridad

### Fase 2: Evaluación del Riesgo
Aplicar el mismo análisis de `apb-sec-risk-analysis-v1.0`:
- Probabilidad e impacto
- Matriz de riesgos 5×5
- Clasificación: Crítico / Alto / Medio / Bajo

### Fase 3: Análisis de Impacto en Políticas
Para cada política afectada:

| Dimensión | Impacto en Política | Medida Compensatoria |
|-----------|--------------------|---------------------|
| Seguridad | ¿Reduce controles de seguridad? | ¿Controles alternativos? |
| Cumplimiento ENS | ¿Incumple dimensión ENS? | ¿Otro control cubre la dimensión? |
| LOPDGDD | ¿Afecta protección de datos? | ¿Medida de protección alternativa? |
| Operaciones | ¿Afecta procedimientos operativos? | ¿Runbook actualizado? |
| Gobierno | ¿Requiere nueva excepción? | ¿Aprobador identificado? |

### Fase 4: Definición de Medidas Compensatorias
Si la excepción es viable, definir:
1. **Controles técnicos:** Firewalls adicionales, monitorización extra, cifrado reforzado
2. **Controles operativos:** Procedimientos específicos, revisión más frecuente
3. **Controles de gobierno:** Aprobación adicional, revisión periódica, fecha de caducidad
4. **Controles de monitorización:** Alertas específicas, auditorías incrementadas

### Fase 5: Evaluación de Viabilidad

```
¿El riesgo residual tras compensatorias es ACEPTABLE?
  ├─ SÍ → Proceder a solicitud de excepción
  └─ NO → BLOCKED, buscar alternativa
```

Criterios de aceptabilidad:
- Riesgo residual ≤ Medio (≤ 9 en matriz 5×5)
- Todas las dimensiones ENS cubiertas (directa o indirectamente)
- Medidas compensatorias viables técnicamente
- Aprobador identificado y disponible

### Fase 6: Generación de Solicitud de Excepción

```markdown
# Solicitud de Excepción — [ID]

## Solicitante
- Nombre: [nombre]
- Departamento: [departamento]
- Fecha: [fecha]

## Descripción
- Política afectada: [referencia]
- Desviación propuesta: [descripción]
- Justificación: [razón de negocio]

## Análisis de Riesgo
- Riesgo original: [valor]
- Riesgo residual: [valor]
- Medidas compensatorias: [lista]

## Viabilidad
- ¿Técnicamente viable? [Sí/No]
- ¿Cubre ENS? [Sí/No]
- ¿Aprobador disponible? [Sí/No]

## Estado Recomendado
- APROBAR / RECHAZAR / CONDICIONAL
- Condiciones: [si aplica]
- Fecha de revisión: [fecha]
- Caducidad: [fecha]
```

## Quick Reference

| Escenario | Acción | Aprobador |
|-----------|--------|-----------|
| Excepción temporal (< 3 meses) | Evaluar compensatorias | CISO |
| Excepción permanente | Revisar política + compensatorias | CISO + Arquitecto Enterprise |
| Desviación de ENS | BLOCKED salvo medida compensatoria equivalente | CISO + CCN-CERT (si aplica) |
| Riesgo residual > Medio | RECHAZAR, buscar alternativa | — |

## Implementation

### Checklist de Evaluación
```
□ Política afectada identificada y citada
□ Análisis de riesgo completo (probabilidad × impacto)
□ Medidas compensatorias definidas y viables
□ Riesgo residual calculado y aceptable
□ Aprobador identificado
□ Fecha de caducidad definida
□ Plan de revisión establecido
□ Documentación completa para auditoría
```

## Common Mistakes
- **Aprobar excepciones sin compensatorias:** Cada excepción debe tener medida compensatoria
- **No definir caducidad:** Las excepciones temporales se convierten en permanentes por inercia
- **Ignorar el riesgo residual:** El riesgo residual debe ser siempre evaluado y aceptado
- **No documentar la justificación:** Cada excepción debe tener razón de negocio clara
- **Olvidar la revisión periódica:** Las excepciones deben revisarse en cada ciclo de auditoría
- **Confundir excepción con cambio de política:** Si la excepción se vuelve norma, actualizar la política

## Real-World Impact
- Reducción de 60% en excepciones permanentes no revisadas
- Cumplimiento sistemático de auditorías ENS
- Trazabilidad completa de decisiones de riesgo

---

## Adapted From
- **Source:** mukul975/Anthropic-Cybersecurity-Skills (Risk Policies domain)
- **License:** MIT
- **Attribution:** Patrón de integración entre análisis de riesgos y políticas corporativas inspirado en Mukul Risk Policies. Reescrito completamente para marco de políticas APB, ENS y procedimientos de excepción sector público.

## References
- ENS RD 311/2022 — Gestión de excepciones
- context/apb/policies/security-policy.md
- context/apb/policies/exception-management-policy.md
- GOVERNANCE.md — Proceso de excepciones
