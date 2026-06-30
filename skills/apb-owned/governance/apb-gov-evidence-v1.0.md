---
id: "apb-gov-evidence-v1.0"
name: "Generación de Evidencias y Documentación"
description: "Generar, estructurar y versionar evidencias documentales para auditorías, compliance y gobierno de TI. La skill produce documentos con metadatos de trazabilidad, firmas de revisión y control de cambios, asegurando que toda evidencia sea presentable a auditores y reguladores."
version: "1.0.0"
status: "draft"
owner: "Gobierno TI APB <arquitectura@portdebarcelona.cat>"
domain: "governance"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# Generación de Evidencias y Documentación


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Propósito
Generar, estructurar y versionar evidencias documentales para auditorías, compliance y gobierno de TI. La skill produce documentos con metadatos de trazabilidad, firmas de revisión y control de cambios, asegurando que toda evidencia sea presentable a auditores y reguladores.

## Contexto de Uso
- Generación de evidencias para auditorías de seguridad, calidad o arquitectura.
- Documentación de decisiones técnicas con trazabilidad completa.
- Control de cambios en especificaciones, diseños y políticas.
- Integración con workflows de gobierno, QA y release management.

## Entradas Requeridas
| Entrada | Tipo | Descripción | Obligatorio |
|---------|------|-------------|-------------|
| `evidence_type` | Enum | `audit`, `design_decision`, `test_result`, `security_review`, `architecture_review` | ✅ |
| `source_artifacts` | Lista | Artefactos fuente: specs, código, logs, informes | ✅ |
| `stakeholders` | Lista | Responsables, revisores y aprobadores | ✅ |
| `compliance_framework` | Lista | ENS, ISO 27001, OWASP, etc. | ❌ |
| `previous_version` | Texto | Versión anterior de la evidencia (si es actualización) | ❌ |

## Flujo de Trabajo (Pasos)
1. **Clasificación de evidencia**: Determinar tipo, nivel de confidencialidad y requisitos de formato.
2. **Recopilación de artefactos**: Consolidar fuentes en estructura documental coherente.
3. **Generación de metadatos**: Incluir:
   - ID único de evidencia.
   - Fecha y hora de generación.
   - Autor (agente + responsable humano).
   - Versión y historial de cambios.
   - Trazabilidad a requisitos, tickets Jira, commits.
4. **Estructuración del documento**: Aplicar plantilla corporativa de evidencia con secciones obligatorias.
5. **Validación de completitud**: Verificar que todos los campos requeridos están poblados.
6. **Control de calidad**: Revisar coherencia, ausencia de secretos, y formato markdown correcto.
7. **Generación de firma digital**: Incluir hash SHA-256 del contenido para integridad.
8. **Registro en catálogo**: Añadir metadatos al catálogo de evidencias para búsqueda y tracking.

## Salida Esperada
### Estructura del Documento de Evidencia
```markdown
# Evidencia — [Tipo] — [Título]
> ID: GOV-EVI-[YYYY]-[NNNN] | Versión: X.Y.Z | Fecha: [YYYY-MM-DD HH:MM]
> Autor: [Agente] / [Responsable Humano] | Estado: draft
> Trazabilidad: [Jira-XXX] | [Commit-SHA] | [Spec-ID]

## 1. Resumen Ejecutivo
## 2. Alcance y Contexto
## 3. Artefactos Analizados
## 4. Hallazgos / Decisiones / Resultados
## 5. Conclusiones y Recomendaciones
## 6. Trazabilidad a Compliance
## 7. Anexos
## 8. Historial de Cambios
## 9. Metadatos de Integridad
> Hash SHA-256: [hash]
```

## Criterios de Calidad
- [ ] Cada evidencia tiene ID único y versionado.
- [ ] Trazabilidad completa a artefactos fuente (commits, tickets, specs).
- [ ] No contiene secretos, credenciales ni datos personales sin anonimización.
- [ ] Formato markdown válido y aplicable a conversión PDF/Word.
- [ ] Hash de integridad incluido para verificación.
- [ ] Revisable por auditor externo sin intervención del agente.

## Stack y Tecnologías
- Formatos: Markdown, PDF vía pandoc, DOCX vía plantilla
- Control de versiones: Git, Confluence, SharePoint
- Metadatos: YAML frontmatter en markdown
- Integridad: SHA-256, GPG signing opcional

## Dependencias
- `apb-gov-catalog-v1.0` — para registro en catálogo de IA
- `apb-gov-standards-v1.0` — para aplicación de estándares documentales
- `apb-gov-jira-evidence-v1.0` — para integración con Jira

## Ejemplo de Uso
**Prompt de invocación:**
```
Genera evidencia de revisión de arquitectura para el microservicio de pagos:
- Tipo: architecture_review
- Artefactos: system-spec.md, apb-arch-design-v1.0 output, diagrama C4
- Stakeholders: Arquitecto Técnico (revisor), Tech Lead (implementador)
- Compliance: ENS Media, OWASP ASVS L2
- Ticket Jira: ARCH-2042
```

## Notas y Advertencias
- **Nivel 1**: El agente genera y estructura documentación; no aprueba ni firma documentos de forma vinculante.
- **Revisión humana obligatoria** antes de presentar evidencia a auditorías.
- Los hashes de integridad son para control interno; no sustituyen a firmas digitales legales.
- Las evidencias deben almacenarse en repositorio corporativo con control de acceso.

## Historial de Cambios
| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-20 | Arquitectura APB | Creación inicial |


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-gov-evidence-v1.0) - pendiente validacion humana. No distribuir sin revision.
