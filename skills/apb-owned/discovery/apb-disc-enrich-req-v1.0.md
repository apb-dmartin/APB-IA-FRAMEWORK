---
id: "apb-disc-enrich-req-v1.0"
name: "Enriquecimiento de Requisitos"
description: "Transformar requisitos de negocio de alto nivel en requisitos técnicos detallados, completos y verificables. Añade criterios de aceptación, casos de uso, reglas de validación y dependencias."
version: "1.0.0"
status: "draft"
owner: "Análisis Funcional <arquitectura@portdebarcelona.cat>"
domain: "discovery"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# Enriquecimiento de Requisitos


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

---

## 🎯 Propósito

Transformar requisitos de negocio de alto nivel en requisitos técnicos detallados, completos y verificables. Añade criterios de aceptación, casos de uso, reglas de validación y dependencias.

---

## ⚡ Trigger

Tras la fase de discovery de negocio, cuando se tienen requisitos iniciales que necesitan ser detallados para su implementación.

---

## 📥 Input

- Requisitos de negocio (user stories, necesidades)
- Modelo de dominio preliminar
- Arquitectura de referencia
- Estándares de especificación APB
- Stakeholders disponibles para clarificación

---

## 📤 Output

- Requisitos funcionales detallados
- Criterios de aceptación por requisito
- Reglas de negocio identificadas y documentadas
- Casos de uso o escenarios
- Matriz de trazabilidad (negocio → técnico)
- Identificación de dependencias entre requisitos

---

## 🔄 Proceso

1. **Análisis de requisitos originales**: Comprender intención, detectar ambigüedades.
2. **Descomposición**: Dividir requisitos grandes en requisitos atómicos (INVEST).
3. **Definición de criterios de aceptación**: Given-When-Then o checklist verificable.
4. **Identificación de reglas de negocio**: Extraer reglas implícitas, validaciones, cálculos.
5. **Identificación de casos edge**: Escenarios límite, errores, excepciones.
6. **Análisis de dependencias**: Qué requisitos dependen de otros, orden de implementación.
7. **Validación técnica**: Verificar viabilidad con arquitecto/desarrollador.
8. **Documentación**: Estructurar en formato estándar APB.
9. **Revisión con negocio**: Validar que el enriquecimiento no altera intención original.

---

## 📋 Reglas y Constraints

- Todo requisito debe ser SMART (Specific, Measurable, Achievable, Relevant, Time-bound).
- Criterios de aceptación deben ser verificables automáticamente cuando sea posible.
- No asumir comportamiento no especificado; requerir clarificación.
- Documentar reglas de negocio con identificador único (RB-001, etc.) para trazabilidad.
- Identificar requisitos no funcionales asociados (rendimiento, seguridad, UX).
- Mantener trazabilidad bidireccional: requisito de negocio ↔ requisito técnico.
- Los requisitos deben ser independientes; si hay dependencia fuerte, considerar unificar.

---

## 🛠 Stack Tecnológico Relevante

- Jira / Azure DevOps
- Confluence / SharePoint (documentación)
- Excel (matriz de trazabilidad)
- BDD/Gherkin (criterios de aceptación)
- Plantillas de especificación APB

---

## 💡 Ejemplos de Uso

**Ejemplo — Enriquecimiento de 'Usuario puede crear pedido':**
> Original: 'Como usuario, quiero crear pedidos para gestionar mis compras.'
> Enriquecido:
> - RF-001: El sistema permite crear pedidos con 1-N líneas.
> - RF-002: Cada línea requiere producto, cantidad (>0), precio unitario.
> - RB-001: El precio unitario debe ser el precio vigente del catálogo.
> - CA-001: Given usuario autenticado, When añade producto válido al carrito and confirma pedido, Then pedido se crea con estado 'Pendiente' and stock se reserva.
> - Edge: Producto sin stock → mensaje de error 'Producto no disponible'.
> - NFR: Creación de pedido < 2s para < 100 líneas.

---

## 🔗 Dependencias

- `apb-disc-business-v1.0`
- `apb-disc-spec-gen-v1.0`
- `apb-disc-adversarial-v1.0`

---

## 📝 Notas

- El enriquecimiento es un proceso colaborativo; requiere interacción con negocio y técnico.
- No sobre-especificar; dejar margen de implementación al equipo técnico.

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `Requisitos de negocio` | Pregunta: "¿Puedes proporcionar requisitos de negocio?" | Sí |
| `Modelo de dominio preliminar` | Pregunta: "¿Puedes proporcionar modelo de dominio preliminar?" | Sí |
| `Arquitectura de referencia` | Pregunta: "¿Puedes proporcionar arquitectura de referencia?" | Sí |
| `Estándares de especificación APB` | Pregunta: "¿Puedes proporcionar estándares de especificación apb?" | Sí |
| `Stakeholders disponibles para clarificación` | Pregunta: "¿Puedes proporcionar stakeholders disponibles para clarificación?" | Sí |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-disc-enrich-req-v1.0) - pendiente validacion humana. No distribuir sin revision.
