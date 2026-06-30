---
id: "apb-disc-reverse-doc-v1.0"
name: "Ingeniería Inversa desde Documentación"
description: "Reconstruir el modelo de dominio, procesos de negocio y requisitos funcionales a partir de documentación existente de sistemas legacy. Transforma documentación desestructurada en artefactos estructurados del framework APB."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "discovery"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# Ingeniería Inversa desde Documentación


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

---

## 🎯 Propósito

Reconstruir el modelo de dominio, procesos de negocio y requisitos funcionales a partir de documentación existente de sistemas legacy. Transforma documentación desestructurada en artefactos estructurados del framework APB.

---

## ⚡ Trigger

Cuando se necesita comprender un sistema legacy que tiene documentación pero carece de especificaciones técnicas modernas, o cuando la documentación está desactualizada o fragmentada.

---

## 📥 Input

- Documentación existente (manuales, especificaciones antiguas, diagramas)
- Registros de procesos de negocio
- Documentación de usuario
- Notas técnicas y runbooks
- Entrevistas con usuarios clave (transcripciones)

---

## 📤 Output

- Mapa de procesos de negocio
- Glosario de términos (ubiquitous language preliminar)
- Lista de funcionalidades identificadas
- Diagrama de casos de uso
- Identificación de gaps en documentación
- Propuesta de especificaciones a generar

---

## 🔄 Proceso

1. **Recopilación**: Centralizar toda la documentación disponible en repositorio único.
2. **Clasificación**: Categorizar por tipo (negocio, técnica, usuario, proceso).
3. **Extracción de procesos**: Identificar flujos de negocio, actores, entradas, salidas, reglas.
4. **Extracción de funcionalidades**: Listar capacidades del sistema desde perspectiva de usuario.
5. **Identificación de términos**: Extraer vocabulario de negocio, detectar ambigüedades.
6. **Validación cruzada**: Contrastar información de múltiples fuentes. Resolver conflictos.
7. **Identificación de gaps**: Documentar lo que falta, es inconsistente o está desactualizado.
8. **Síntesis**: Generar artefactos estructurados del framework APB.
9. **Validación**: Revisar con stakeholders de negocio.

---

## 📋 Reglas y Constraints

- Documentar la fuente de cada requisito extraído para trazabilidad.
- Marcar explícitamente información contradictoria entre fuentes.
- No asumir comportamiento no documentado; marcar como 'requiere validación'.
- Priorizar funcionalidades por valor de negocio y frecuencia de uso.
- Mantener registro de documentación descartada y por qué.
- No inventar requisitos; si no está en documentación, requerir entrevista.

---

## 🛠 Stack Tecnológico Relevante

- Procesamiento de documentos (PDF, Word, OCR si es escaneado)
- Mermaid / PlantUML (diagramas)
- Excel / Sheets (inventario)
- Herramientas de colaboración (Teams, Confluence)

---

## 💡 Ejemplos de Uso

**Ejemplo — Sistema de gestión documental legacy:**
> Documentación: 5 manuales de usuario, 2 especificaciones técnicas de 2010, diagramas de flujo escaneados.
> Procesos identificados: Alta de documento, Clasificación, Aprobación, Archivado, Búsqueda.
> Gaps: No documenta proceso de borrado lógico, permisos granulares no están claros.
> Output: 12 funcionalidades identificadas, 3 requieren validación con usuario.

---

## 🔗 Dependencias

- `apb-disc-business-v1.0`
- `apb-disc-spec-gen-v1.0`

---

## 📝 Notas

- La calidad del output depende directamente de la calidad de la documentación de entrada.
- Para documentación muy antigua, validar con usuarios actuales antes de considerarla vigente.

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `Documentación existente` | Pregunta: "¿Puedes proporcionar documentación existente?" | Sí |
| `Registros de procesos de negocio` | Pregunta: "¿Puedes proporcionar registros de procesos de negocio?" | Sí |
| `Documentación de usuario` | Pregunta: "¿Puedes proporcionar documentación de usuario?" | Sí |
| `Notas técnicas y runbooks` | Pregunta: "¿Puedes proporcionar notas técnicas y runbooks?" | Sí |
| `Entrevistas con usuarios clave` | Pregunta: "¿Puedes proporcionar entrevistas con usuarios clave?" | Sí |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-disc-reverse-doc-v1.0) - pendiente validacion humana. No distribuir sin revision.
