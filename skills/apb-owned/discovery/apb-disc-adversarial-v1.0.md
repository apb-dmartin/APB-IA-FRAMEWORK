---
id: "apb-disc-adversarial-v1.0"
name: "Validación Adversaria de Especificación"
description: "Revisar especificaciones técnicas desde una perspectiva crítica y adversaria, buscando ambigüedades, inconsistencias, casos no cubiertos, riesgos y suposiciones no validadas. Mejora la calidad antes de que el código sea escrito."
version: "1.0.0"
status: "draft"
owner: "QA / Arquitectura <arquitectura@portdebarcelona.cat>"
domain: "discovery"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Validación Adversaria de Especificación

---

## 🎯 Propósito

Revisar especificaciones técnicas desde una perspectiva crítica y adversaria, buscando ambigüedades, inconsistencias, casos no cubiertos, riesgos y suposiciones no validadas. Mejora la calidad antes de que el código sea escrito.

---

## ⚡ Trigger

Tras generarse una especificación técnica, antes de su aprobación formal. También en revisiones periódicas de specs existentes.

---

## 📥 Input

- Especificación técnica a validar
- Requisitos de negocio originales
- ADRs asociados
- Estándares corporativos
- Experiencia de proyectos similares

---

## 📤 Output

- Informe de validación adversaria
- Lista de hallazgos (ambigüedades, inconsistencias, gaps, riesgos)
- Preguntas sin respuesta
- Recomendaciones de mejora
- Estado: Aprobado / Aprobado con observaciones / Rechazado

---

## 🔄 Proceso

1. **Lectura completa**: Entender el alcance, objetivo y contexto de la especificación.
2. **Validación de requisitos**: ¿Todos los requisitos de negocio están cubiertos? ¿Hay requisitos 'perdidos en traducción'?
3. **Detección de ambigüedades**: Identificar términos vagos ('rápido', 'mucho', 'a veces'), números sin justificación, rangos sin límites.
4. **Detección de inconsistencias**: Contradicciones entre secciones, entre spec y ADRs, entre spec y estándares.
5. **Identificación de gaps**: Casos no cubiertos (errores, edge cases, estados no definidos).
6. **Análisis de riesgos**: ¿Qué podría salir mal? ¿Hay suposiciones no validadas?
7. **Validación de trazabilidad**: ¿Cada requisito tiene criterio de aceptación? ¿Cada decisión tiene ADR?
8. **Preguntas**: Formular preguntas que el equipo de especificación debe responder.
9. **Informe**: Documentar hallazgos con severidad y recomendaciones.

---

## 📋 Reglas y Constraints

- Ser constructivamente crítico; el objetivo es mejorar, no bloquear.
- Citar ubicación exacta del hallazgo (sección, párrafo, diagrama).
- Distinguir entre 'no me gusta' y 'esto es incorrecto/riesgoso'.
- No aprobar specs con ambigüedades no resueltas en requisitos críticos.
- Registrar preguntas sin respuesta; no asumir respuesta.
- Involucrar a QA desde esta fase; es más barato que encontrar problemas en testing.
- La validación adversaria es obligatoria para specs de proyectos > 3 meses.

---

## 🛠 Stack Tecnológico Relevante

- Markdown (review comments)
- Plantilla de validación adversaria APB
- Checklist de revisión
- Jira / Azure DevOps (seguimiento de hallazgos)

---

## 💡 Ejemplos de Uso

**Ejemplo — Hallazgos en spec de pedidos:**
> Ambigüedad: 'El sistema debe ser rápido' → No medible. Recomendación: 'El 95% de las operaciones de creación de pedido deben completarse en < 2s.'
> Inconsistencia: Sección 3.2 dice máximo 100 líneas por pedido; sección 5.1 dice sin límite.
> Gap: No se define comportamiento cuando el cliente tiene crédito insuficiente.
> Riesgo: Dependencia de API externa de inventario sin plan de fallback.

---

## 🔗 Dependencias

- `apb-disc-spec-gen-v1.0`
- `apb-gov-standards-v1.0`

---

## 📝 Notas

- La validación adversaria es una técnica probada para reducir defectos en etapas tempranas.
- Rotar el rol de 'adversario' entre miembros del equipo para diversificar perspectivas.

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-disc-adversarial-v1.0) - pendiente validacion humana. No distribuir sin revision.
