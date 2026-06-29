---
id: "apb-dev-openspec-review-v1.0"
name: "Revisión Automática OpenSpec"
description: "Validar automáticamente especificaciones técnicas contra estándares OpenAPI, contratos de eventos y políticas corporativas. Detecta inconsistencias, omisiones y desviaciones de estándares."
version: "1.0.0"
status: "draft"
owner: "QA <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 2
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Revisión Automática OpenSpec

---

## 🎯 Propósito

Validar automáticamente especificaciones técnicas contra estándares OpenAPI, contratos de eventos y políticas corporativas. Detecta inconsistencias, omisiones y desviaciones de estándares.

---

## ⚡ Trigger

Al generar o modificar una especificación OpenAPI, contrato de evento, o documento de especificación técnica.

---

## 📥 Input

- Especificación OpenAPI 3.0+ o AsyncAPI
- Esquemas de eventos (CloudEvents)
- Estándares corporativos de API y eventos
- Reglas de validación personalizadas APB

---

## 📤 Output

- Informe de validación con hallazgos
- Puntuación de conformidad
- Sugerencias de corrección automática (si aplica)
- Lista de checks pasados/fallidos
- Diferencias con versiones anteriores

---

## 🔄 Proceso

1. **Parseo de especificación**: Cargar OpenAPI/AsyncAPI y validar sintaxis.
2. **Validación estructural**: Verificar que todos los endpoints tienen: operación, parámetros, request body, responses, ejemplos.
3. **Validación de estándares**: URLs correctas, versionado, naming conventions, headers obligatorios.
4. **Validación de seguridad**: Auth definido, scopes, HTTPS obligatorio.
5. **Validación de esquemas**: JSON Schema válido, tipos correctos, campos requeridos.
6. **Validación de eventos**: CloudEvents compliance, campos obligatorios, formato de tipo de evento.
7. **Comparación con baseline**: Detectar breaking changes vs versión anterior.
8. **Generación de informe**: Resumen ejecutivo + detalle por regla.

---

## 📋 Reglas y Constraints

- Toda API debe tener documentación de error (RFC 7807).
- Todos los campos de fecha deben ser string con formato ISO 8601.
- Los enums deben tener descripción de cada valor.
- Breaking changes bloquean el pipeline hasta aprobación explícita.
- Las respuestas 2xx deben tener schema definido.
- Los parámetros de path deben tener ejemplos.
- No se permiten campos sin tipo ni descripción.

---

## 🛠 Stack Tecnológico Relevante

- OpenAPI 3.0+
- AsyncAPI
- CloudEvents 1.0
- Spectral (linting)
- Azure DevOps / GitHub Actions

---

## 💡 Ejemplos de Uso

**Ejemplo — Validación de spec:**
> Hallazgo: Endpoint POST /orders no define response 400.
> Corrección: Añadir schema de error 400 con Problem Details.
> Hallazgo: Campo 'status' es string sin enum ni descripción.
> Corrección: Definir enum [pending, confirmed, shipped, delivered] con descripciones.

---

## 🔗 Dependencias

- `apb-arch-api-contract-v1.0`
- `apb-doc-swagger-v1.0`
- `third-openspec-spec-gen-v1.0

---

## 📝 Notas

- Integrar en pipeline CI para validación automática en cada PR.
- Mantener reglas de validación versionadas junto con los estándares.

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `Especificación OpenAPI 3.0+ o AsyncAPI` | Pregunta: "¿Puedes proporcionar especificación openapi 3.0+ o asyncapi?" | Sí |
| `Esquemas de eventos` | Pregunta: "¿Puedes proporcionar esquemas de eventos?" | Sí |
| `Estándares corporativos de API y eventos` | Pregunta: "¿Puedes proporcionar estándares corporativos de api y eventos?" | Sí |
| `Reglas de validación personalizadas APB` | Pregunta: "¿Puedes proporcionar reglas de validación personalizadas apb?" | Sí |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **YAML/spec generado** - primera linea: `# [IA-GEN] Generado por APB AI Framework (apb-dev-openspec-review-v1.0) - pendiente revision humana`
- **Campo OpenAPI si aplica**: `info.x-ai-generated: true` + `info.x-ai-skill: "apb-dev-openspec-review-v1.0"`
- **Commit** - prefijo `[ai-gen]` + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`
