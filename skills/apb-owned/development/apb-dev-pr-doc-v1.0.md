---
id: "apb-dev-pr-doc-v1.0"
name: "Preparación y Documentación de Pull Request"
description: "Estructurar y documentar Pull Requests de forma clara, completa y alineada con estándares corporativos. Facilita la revisión de código y el seguimiento de cambios."
version: "1.0.0"
status: "draft"
owner: "Desarrollo <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# Preparación y Documentación de Pull Request


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

---

## 🎯 Propósito

Estructurar y documentar Pull Requests de forma clara, completa y alineada con estándares corporativos. Facilita la revisión de código y el seguimiento de cambios.

---

## ⚡ Trigger

Cuando un desarrollador finaliza una tarea y necesita crear una PR para mergear cambios.

---

## 📥 Input

- Código implementado (git diff)
- Ticket/Jira asociado
- Especificación técnica
- Tests ejecutados
- Notas de implementación del desarrollador

---

## 📤 Output

- Descripción estructurada de la PR
- Checklist de calidad completada
- Enlace a documentación relevante
- Instrucciones de testing para revisores
- Notas de deploy (si aplica)

---

## 🔄 Proceso

1. **Título**: Formato estándar: `[TIPO-123] Descripción breve y clara`.
2. **Descripción**: Qué cambia, por qué, cómo. Incluir contexto de negocio si aplica.
3. **Cambios técnicos**: Lista de archivos modificados con justificación.
4. **Tests**: Evidencia de ejecución (screenshots, logs), cobertura.
5. **Checklist**: Verificar estándares (tests, docs, sin secretos, sin código comentado).
6. **Notas de deploy**: Migrations, variables de entorno, cambios en infraestructura.
7. **Reviewers**: Asignar revisores apropiados (mínimo 2).
8. **Relacionados**: Enlaces a tickets, PRs relacionadas, documentación.

---

## 📋 Reglas y Constraints

- Título máximo 72 caracteres.
- Descripción debe permitir entender el cambio sin leer el código.
- Incluir screenshots para cambios UI.
- Checklist obligatorio: tests pasan, cobertura ≥ 80%, sin secretos, documentación actualizada.
- Si hay breaking changes, documentar explícitamente con plan de migración.
- PRs > 400 líneas deben justificar por qué no se pueden dividir.
- No mergear sin al menos 2 aprobaciones (1 técnico, 1 funcional si aplica).

---

## 🛠 Stack Tecnológico Relevante

- Git / GitHub / Azure DevOps
- Jira / Azure Boards
- SonarQube / Code Coverage

---

## 💡 Ejemplos de Uso

**Ejemplo — PR de feature:**
> Título: `[ORD-456] Añadir endpoint de cancelación de pedidos`
> Descripción: Implementa POST /api/v1/orders/{id}/cancel. Valida estado del pedido, emite evento OrderCancelled, actualiza inventario.
> Tests: 12 unit tests, cobertura 92%. Screenshot de ejecución adjunto.
> Deploy: Requiere migration AddCancellationReason. Variable CANCEL_TIMEOUT_HOURS=24.

---

## 🔗 Dependencias

- `apb-dev-implement-v1.0`
- `apb-dev-code-review-v1.0`

---

## 📝 Notas

- Una buena PR reduce tiempo de revisión en 50%.
- Automatizar checklist cuando sea posible (CI checks).

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `Código implementado` | Pregunta: "¿Puedes proporcionar código implementado?" | Sí |
| `Ticket/Jira asociado` | Pregunta: "¿Puedes proporcionar ticket/jira asociado?" | Sí |
| `Especificación técnica` | Pregunta: "¿Puedes proporcionar especificación técnica?" | Sí |
| `Tests ejecutados` | Pregunta: "¿Puedes proporcionar tests ejecutados?" | Sí |
| `Notas de implementación del desarrollador` | Pregunta: "¿Puedes proporcionar notas de implementación del desarrollador?" | Sí |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Label GitHub**: `ai-generated` — añadir al crear el PR
- **Footer en descripción** (antes de cerrar el texto):
  > ⚠️ **Generado por IA** (APB AI Framework — apb-dev-pr-doc-v1.0) — revisado y validado por [nombre] antes de publicar este PR.
- **Commit origen** — prefijo `[ai-gen]` + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`
