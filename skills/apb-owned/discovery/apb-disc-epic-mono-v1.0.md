---
id: "apb-disc-epic-mono-v1.0"
name: "Definición de Épicas para Transformación de Monolito"
description: "Definir épicas de transformación que guíen la migración gradual de un monolito a microservicios, alineando valor de negocio, riesgo técnico y dependencias arquitectónicas."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "discovery"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Definición de Épicas para Transformación de Monolito

---

## 🎯 Propósito

Definir épicas de transformación que guíen la migración gradual de un monolito a microservicios, alineando valor de negocio, riesgo técnico y dependencias arquitectónicas.

---

## ⚡ Trigger

Cuando se inicia un proyecto de modernización de monolito y se necesita estructurar el trabajo en épicas manejables con entregables de valor.

---

## 📥 Input

- Análisis de arquitectura actual (monolito)
- Mapa de bounded contexts identificados
- Análisis de dependencias entre módulos
- Roadmap de modernización
- Capacidad del equipo
- Objetivos de negocio de la transformación

---

## 📤 Output

- Épicas de transformación definidas y priorizadas
- Justificación de valor por épica
- Dependencias entre épicas
- Criterios de éxito por épica
- Estimación de esfuerzo y riesgo
- Roadmap de épicas con milestones

---

## 🔄 Proceso

1. **Identificación de candidatos**: Basado en bounded contexts, identificar módulos candidatos a extracción.
2. **Evaluación de valor/riesgo**: Matriz de valor de negocio vs riesgo técnico. Priorizar quick wins.
3. **Definición de épicas**: Cada épica representa un paso de transformación (extracción de microservicio, migración de datos, etc.).
4. **Dependencias**: Mapear qué épicas dependen de otras (ej: infraestructura base antes de extracciones).
5. **Criterios de éxito**: Definir qué significa 'terminado' para cada épica (paridad funcional, métricas de rendimiento, etc.).
6. **Estimación**: T-shirt sizing o story points a nivel de épica.
7. **Roadmap**: Secuenciar épicas en fases lógicas.
8. **Validación**: Revisar con stakeholders técnicos y de negocio.

---

## 📋 Reglas y Constraints

- Cada épica debe entregar valor medible; evitar 'épicas de infraestructura pura' sin entregable de negocio.
- La primera épica debe ser de bajo riesgo y alto valor (quick win) para generar confianza.
- Documentar decisiones de secuenciación; no es arbitraria.
- Considerar épica de 'foundation' (CI/CD, observabilidad, scaffold) si no existe infraestructura base.
- Cada épica de extracción debe incluir: diseño, implementación, migración de datos, tests, deploy, validación.
- No planificar extracciones en paralelo que compartan datos o dependencias críticas.
- Mantener monolito operativo durante toda la transformación.

---

## 🛠 Stack Tecnológico Relevante

- Jira / Azure DevOps
- Mermaid (roadmap visual)
- Excel (matriz valor/riesgo)
- C4 Model (arquitectura de referencia)

---

## 💡 Ejemplos de Uso

**Ejemplo — Transformación de monolito de e-commerce:**
> Épica 0: Foundation — CI/CD, observabilidad, API Gateway. (4 semanas)
> Épica 1: Extracción Catálogo — Bajo riesgo, alto valor. (6 semanas)
> Épica 2: Extracción Inventario — Depende de Épica 1 para eventos de stock. (4 semanas)
> Épica 3: Extracción Pagos — Core domain, alto riesgo. (8 semanas)
> Épica 4: Extracción Pedidos — Depende de 1, 2, 3. (6 semanas)
> Épica 5: Retiro de monolito — Depende de todas las anteriores. (4 semanas)

---

## 🔗 Dependencias

- `apb-arch-decompose-v1.0`
- `apb-disc-ddd-legacy-v1.0`
- `apb-disc-backlog-v1.0`

---

## 📝 Notas

- Las épicas de transformación son más complejas que épicas de desarrollo nuevo; incluyen migración y coexistencia.
- Considerar 'pilot épica' para validar enfoque antes de escalar.
- Métrica clave: time-to-deploy del nuevo microservicio debe ser < 15 min al final de cada épica.

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Label Jira**: `ia-generado` — campo _Labels_ del ticket
- **Footer en descripción del ticket**:
  `_Generado por IA (APB AI Framework — apb-disc-epic-mono-v1.0). Requiere validación humana antes de ejecutar._`
