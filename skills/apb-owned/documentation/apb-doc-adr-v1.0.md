---
id: "apb-doc-adr-v1.0"
name: "Generación de ADRs (Architecture Decision Records)"
description: "Generar Architecture Decision Records (ADRs) estructurados siguiendo el formato de decisiones de arquitectura de APB. Documenta decisiones técnicas significativas con contexto, opciones consideradas, decisión, consecuencias y estado."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "documentation"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Generación de ADRs (Architecture Decision Records)

## Propósito
Generar Architecture Decision Records (ADRs) estructurados siguiendo el formato de decisiones de arquitectura de APB. Documenta decisiones técnicas significativas con contexto, opciones consideradas, decisión, consecuencias y estado.

## Contexto de Uso
- Documentación de decisiones arquitectónicas durante el diseño de sistemas.
- Registro de decisiones de modernización, migración o refactorización.
- Trazabilidad de decisiones para auditorías y onboarding de nuevo equipo.
- Integración con gobierno y arquitectura de referencia.

## Entradas Requeridas
| Entrada | Tipo | Descripción | Obligatorio |
|---------|------|-------------|-------------|
| `decision_title` | Texto | Título de la decisión arquitectónica | ✅ |
| `context` | Texto / Markdown | Contexto que motiva la decisión | ✅ |
| `options_considered` | Lista | Opciones evaluadas con pros y contras | ✅ |
| `decision` | Texto | Decisión tomada | ✅ |
| `consequences` | Texto | Consecuencias positivas y negativas | ✅ |
| `related_decisions` | Lista | ADRs relacionados | ❌ |

## Flujo de Trabajo (Pasos)
1. **Análisis de contexto**: Comprender el problema, restricciones y stakeholders.
2. **Estructuración de opciones**: Para cada opción, documentar:
   - Descripción técnica.
   - Pros: ventajas alineadas con objetivos.
   - Contras: riesgos, costes, deuda técnica.
   - Requisitos de compliance afectados.
3. **Documentación de la decisión**: Justificación clara de por qué se eligió la opción seleccionada.
4. **Análisis de consecuencias**:
   - **Positivas**: Beneficios esperados.
   - **Negativas**: Costes, riesgos, deuda técnica, trade-offs.
   - **Neutras**: Cambios en procesos o habilidades requeridas.
5. **Validación de compliance**: Verificar que la decisión no viola estándares ni políticas corporativas.
6. **Generación de ADR**: Documento markdown con formato estándar.
7. **Registro en índice de ADRs**: Actualizar el índice de decisiones del proyecto/sistema.
8. **Registro de evidencia**: Metadatos para gobierno.

## Salida Esperada
### Estructura del ADR
```markdown
# ADR-[NNNN]: [Título de la Decisión]
> Fecha: [YYYY-MM-DD] | Estado: [proposed/accepted/deprecated/superseded]
> Decisor: [Rol/Equipo] | Autor: Documentation Agent

## Contexto
## Opciones Consideradas
### Opción 1: [Nombre]
- **Descripción:**
- **Pros:**
- **Contras:**
### Opción 2: [Nombre]
...
## Decisión
## Consecuencias
### Positivas
### Negativas
### Neutral
## Compliance
## ADRs Relacionados
## Notas
## Evidencia y Metadatos
```

## Criterios de Calidad
- [ ] Cada opción considerada tiene descripción, pros y contras documentados.
- [ ] La decisión está justificada con criterios objetivos, no preferencias subjetivas.
- [ ] Las consecuencias negativas están documentadas honestamente (no solo beneficios).
- [ ] El ADR es revisable por un arquitecto externo sin intervención del agente.
- [ ] Trazabilidad a estándares, políticas y ADRs relacionados.
- [ ] Estado del ADR claramente indicado (proposed → accepted → deprecated/superseded).

## Stack y Tecnologías
- Formato: Markdown con plantilla corporativa
- Índice: `docs/adr/README.md` o `adr/index.md`
- Referencias: MADR (Markdown Any Decision Records), ADR-001 de APB

## Dependencias
- `apb-gov-evidence-v1.0` — para evidencia de decisión
- `apb-gov-standards-v1.0` — para validación de estándares
- `apb-gov-arch-ref-v1.0` — para validación contra arquitectura de referencia
- `apb-gov-policy-check-v1.0` — para validación de políticas

## Ejemplo de Uso
**Prompt de invocación:**
```
Genera un ADR para la decisión de usar Azure Container Apps en lugar de AKS:
- Contexto: Necesitamos desplegar 15 microservicios pequeños con baja complejidad operativa
- Opciones: Azure Container Apps, AKS, Azure App Service
- Decisión: Azure Container Apps
- Consecuencias: Menor overhead operativo, pero menos control sobre networking avanzada
```

## Notas y Advertencias
- **Nivel 1**: El agente genera el documento ADR; no toma decisiones arquitectónicas autónomas.
- **Revisión humana obligatoria** antes de aceptar un ADR; el estado inicial es siempre `proposed`.
- Los ADRs deprecados deben indicar el ADR que los sustituye.
- El agente no modifica ADRs aceptados sin solicitud explícita de revisión.

## Historial de Cambios
| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-20 | Arquitectura APB | Creación inicial |


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** — callout inmediatamente tras el título H1:
  > ⚠️ **Borrador generado por IA** (APB AI Framework — apb-doc-adr-v1.0) — pendiente validación humana. No distribuir sin revisión.
