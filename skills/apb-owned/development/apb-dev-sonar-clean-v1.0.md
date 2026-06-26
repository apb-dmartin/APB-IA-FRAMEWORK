---
id: "apb-dev-sonar-clean-v1.0"
name: "Mejora de Código para Cumplimiento Sonar"
description: "Analizar hallazgos de SonarQube y aplicar correcciones automáticas o sugerir fixes para alcanzar los umbrales de calidad definidos (cobertura, deuda técnica, vulnerabilidades, code smells)."
version: "1.0.0"
status: "draft"
owner: "QA / Desarrollo <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 2
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Mejora de Código para Cumplimiento Sonar

---

## 🎯 Propósito

Analizar hallazgos de SonarQube y aplicar correcciones automáticas o sugerir fixes para alcanzar los umbrales de calidad definidos (cobertura, deuda técnica, vulnerabilidades, code smells).

---

## ⚡ Trigger

Cuando SonarQube reporta incumplimiento de quality gate, o en revisión periódica de calidad de código.

---

## 📥 Input

- Reporte de SonarQube (issues, hotspots, coverage)
- Código fuente del proyecto
- Quality gate definido (umbrales)
- Historial de deuda técnica

---

## 📤 Output

- Código corregido (diff)
- Informe de issues resueltos vs pendientes
- Justificación de issues aceptados (wontfix/false positive)
- Métricas de mejora (deuda técnica reducida, coverage aumentado)

---

## 🔄 Proceso

1. **Análisis de issues**: Categorizar por severidad (blocker, critical, major, minor, info).
2. **Priorización**: Blocker/Critical primero. Luego security hotspots.
3. **Corrección automática**: Aplicar fixes seguros (typos, variables no usadas, simplificaciones).
4. **Corrección manual**: Issues que requieren refactorización o decisión de diseño.
5. **Revisión de hotspots**: Security hotspots requieren análisis manual; documentar decisión.
6. **Verificación**: Re-ejecutar análisis SonarQube. Verificar quality gate.
7. **Documentación**: Registrar issues aceptados con justificación.

---

## 📋 Reglas y Constraints

- No marcar issues como false positive sin justificación técnica documentada.
- Security hotspots deben ser revisados por security champion.
- Cobertura mínima: 80% para nuevo código, 60% para legacy.
- Deuda técnica máxima: 5 días por 1000 líneas de código.
- Duplicación máxima: 3%.
- Vulnerabilidades: 0 en código nuevo.
- Code smells: reducir 10% por sprint.

---

## 🛠 Stack Tecnológico Relevante

- SonarQube / SonarCloud
- .NET 8/9, C#
- Azure DevOps / GitHub Actions
- xUnit / NUnit

---

## 💡 Ejemplos de Uso

**Ejemplo — Corrección de code smells:**
> Issue: Método tiene 120 líneas (cognitive complexity 25).
> Corrección: Extraer 3 métodos privados, reducir a 30 líneas, complexity 8.
> Issue: Variable 'i' no descriptiva.
> Corrección: Renombrar a 'orderIndex'.

---

## 🔗 Dependencias

- `apb-dev-code-review-v1.0`
- `apb-qa-test-auto-v1.0`

---

## 📝 Notas

- Nivel 2: puede aplicar fixes automáticos de bajo riesgo. Fixes de alto riesgo requieren aprobación.
- Integrar en pipeline CI para feedback inmediato.

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-dev-sonar-clean-v1.0) - pendiente validacion humana. No distribuir sin revision.
