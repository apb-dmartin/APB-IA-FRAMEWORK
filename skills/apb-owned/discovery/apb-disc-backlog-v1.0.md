---
id: "apb-disc-backlog-v1.0"
name: "Generación de Backlog Agile"
description: "Transformar especificaciones técnicas y requisitos en un backlog de producto estructurado, priorizado y estimable, listo para ser consumido por equipos de desarrollo ágil."
version: "1.0.0"
status: "draft"
owner: "Análisis Funcional <arquitectura@portdebarcelona.cat>"
domain: "discovery"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Generación de Backlog Agile

---

## 🎯 Propósito

Transformar especificaciones técnicas y requisitos en un backlog de producto estructurado, priorizado y estimable, listo para ser consumido por equipos de desarrollo ágil.

---

## ⚡ Trigger

Tras aprobarse la especificación técnica, o cuando se necesita planificar un nuevo sprint/release.

---

## 📥 Input

- Especificación técnica aprobada
- Requisitos priorizados (MoSCoW o similar)
- Estimaciones de esfuerzo (si disponibles)
- Capacidad del equipo
- Dependencias técnicas identificadas

---

## 📤 Output

- Backlog de producto en herramienta de gestión
- Épicas y user stories estructuradas
- Criterios de aceptación por story
- Estimaciones iniciales (story points o horas)
- Roadmap de releases
- Identificación de dependencias entre stories

---

## 🔄 Proceso

1. **Descomposición en épicas**: Agrupar funcionalidad relacionada en épicas alineadas con objetivos de negocio.
2. **Descomposición en stories**: Dividir épicas en user stories INVEST.
3. **Definición de criterios de aceptación**: Cada story debe tener criterios verificables.
4. **Estimación**: Story points con equipo (planning poker). Refinar en backlog refinement.
5. **Priorización**: Ordenar backlog por valor de negocio, riesgo técnico, dependencias.
6. **Identificación de dependencias**: Mapear qué stories bloquean a otras.
7. **Definición de DOD**: Definition of Done aplicable a todas las stories.
8. **Roadmap**: Agrupar stories en releases/sprints con objetivos claros.
9. **Validación**: Revisar con Product Owner y equipo técnico.

---

## 📋 Reglas y Constraints

- Stories deben ser INVEST (Independent, Negotiable, Valuable, Estimable, Small, Testable).
- No story > 13 story points; si es más grande, dividir.
- Cada story debe entregar valor de usuario; evitar 'stories técnicas puras' (usar tasks en su lugar).
- Priorizar por valor de negocio, pero considerar riesgo técnico y dependencias.
- Mantener backlog refinado (ready) para al menos 2 sprints adelante.
- Documentar supuestos y dependencias en cada story.
- El backlog es propiedad del Product Owner; el equipo técnico colabora en refinamiento.

---

## 🛠 Stack Tecnológico Relevante

- Jira / Azure DevOps
- Confluence (documentación)
- Planning poker tools
- Excel / Sheets (roadmap inicial)

---

## 💡 Ejemplos de Uso

**Ejemplo — Épica 'Gestión de Pedidos':**
> Story 1: Como usuario, quiero crear un pedido para gestionar mi compra. (5 pts)
> Story 2: Como usuario, quiero ver el estado de mi pedido para hacer seguimiento. (3 pts)
> Story 3: Como administrador, quiero cancelar pedidos para gestionar incidencias. (5 pts)
> Story 4: Como sistema, quiero emitir evento de pedido creado para integraciones. (3 pts)
> Dependencias: Story 4 depende de Story 1.

---

## 🔗 Dependencias

- `apb-disc-spec-gen-v1.0`
- `apb-disc-cosmic-v1.0`

---

## 📝 Notas

- El backlog es un artefacto vivo; se actualiza continuamente.
- Considerar usar story mapping para visualizar el backlog completo.
- Para proyectos híbridos (agile + fixed scope), gestionar expectativas de scope vs tiempo.

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Label Jira**: `ia-generado` — campo _Labels_ del ticket
- **Footer en descripción del ticket**:
  `_Generado por IA (APB AI Framework — apb-disc-backlog-v1.0). Requiere validación humana antes de ejecutar._`
