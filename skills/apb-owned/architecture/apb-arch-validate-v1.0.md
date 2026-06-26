---
id: "apb-arch-validate-v1.0"
name: "Validación de Arquitectura"
description: "Validar propuestas de arquitectura contra estándares corporativos, principios de diseño, requisitos no funcionales y mejores prácticas de la industria. Actúa como gate de calidad antes de la aprobación formal."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "architecture"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Validación de Arquitectura

---

## 🎯 Propósito

Validar propuestas de arquitectura contra estándares corporativos, principios de diseño, requisitos no funcionales y mejores prácticas de la industria. Actúa como gate de calidad antes de la aprobación formal.

---

## ⚡ Trigger

Cuando se completa una propuesta de arquitectura y se requiere revisión formal antes de aprobación. También en revisiones periódicas de arquitecturas existentes.

---

## 📥 Input

- Documento de arquitectura a validar
- ADRs asociados
- Requisitos no funcionales del proyecto
- Estándares corporativos APB vigentes
- Arquitecturas de referencia aplicables
- Resultados de análisis de riesgos

---

## 📤 Output

- Informe de validación con estado (aprobado / aprobado con observaciones / rechazado)
- Lista de hallazgos categorizados (crítico, mayor, menor, informativo)
- Recomendaciones de mejora con prioridad
- Matriz de cumplimiento contra estándares
- Riesgos residuales no mitigados
- Condiciones para aprobación (si aplica)

---

## 🔄 Proceso

1. **Revisión de completitud**: Verificar que el documento incluye todos los componentes requeridos (contexto, contenedores, componentes, datos, seguridad, operabilidad).
2. **Validación contra RNF**: Verificar que cada RNF tiene solución arquitectónica explícita (ej: disponibilidad 99.9% → multi-AZ + health checks).
3. **Validación contra estándares**: Revisar cumplimiento de estándares APB (naming, seguridad, observabilidad, APIs, eventos).
4. **Análisis de riesgos**: Verificar que todos los riesgos técnicos tienen mitigación. Evaluar riesgos residuales.
5. **Revisión de decisiones**: Validar ADRs: ¿La decisión está justificada? ¿Se evaluaron alternativas? ¿Hay impacto en otros sistemas?
6. **Revisión de costes**: Validar que la estimación de infraestructura es razonable y optimizada.
7. **Revisión de dependencias**: Verificar que todas las dependencias externas están identificadas y gestionadas.
8. **Revisión de seguridad**: Validar threat model, controles de seguridad, cumplimiento ENS/OWASP.
9. **Generación de informe**: Documentar hallazgos con severidad y recomendaciones.
10. **Seguimiento**: Si hay observaciones, definir plan de remediación y revalidación.

---

## 📋 Reglas y Constraints

- Un hallazgo CRÍTICO bloquea la aprobación (ej: datos sensibles sin encriptación, single point of failure sin mitigación).
- Un hallazgo MAYOR requiere plan de remediación antes del go-live, pero no bloquea aprobación si hay mitigación temporal.
- Los hallazgos MENOR e INFORMATIVO se registran como deuda técnica a gestionar.
- La validación debe ser objetiva; citar estándar o práctica de referencia para cada hallazgo.
- No aprobar arquitecturas que no consideren observabilidad desde el diseño.
- No aprobar arquitecturas con dependencias no gestionadas (ej: 'esperamos que el equipo X haga Y').
- El informe debe ser actionable; cada hallazgo debe tener recomendación específica.
- Mantener registro de todas las validaciones para auditoría.

---

## 🛠 Stack Tecnológico Relevante

- Estándares APB (documentos de referencia)
- Azure Well-Architected Framework
- OWASP ASVS
- ENS (Esquema Nacional de Seguridad)
- C4 Model (revisión de diagramas)

---

## 💡 Ejemplos de Uso

**Ejemplo 1 — Hallazgo CRÍTICO:**
> La arquitectura propone almacenar credenciales de BBDD en appsettings.json.
> Recomendación: Usar Azure Key Vault con Managed Identity. Bloquea aprobación.

**Ejemplo 2 — Hallazgo MAYOR:**
> No se define estrategia de rate limiting en APIs públicas.
> Recomendación: Implementar Azure API Management con políticas de throttling. Plan de remediación en 2 semanas.

**Ejemplo 3 — Aprobado con observaciones:**
> Arquitectura sólida. Observación: Considerar Azure CDN para assets estáticos. No bloqueante.

---

## 🔗 Dependencias

- `apb-gov-standards-v1.0` (estándares corporativos)
- `apb-gov-compliance-v1.0` (cumplimiento)
- `apb-sec-threat-model-v1.0

---

## 📝 Notas

- La validación no reemplaza la revisión humana; es un asistente que acelera y estandariza el proceso.
- Para proyectos críticos, requerir revisión por arquitecto de referencia humano además de esta skill.
- Mantener un registro histórico de validaciones para identificar patrones de incumplimiento recurrentes.

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-arch-validate-v1.0) - pendiente validacion humana. No distribuir sin revision.
