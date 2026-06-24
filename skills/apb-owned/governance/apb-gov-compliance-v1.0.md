---
id: "apb-gov-compliance-v1.0"
name: "Validación de Cumplimiento Arquitectónico"
description: "Validar que diseños de arquitectura, decisiones técnicas y especificaciones cumplen con los estándares, políticas y patrones de arquitectura de referencia de APB. Genera un informe de compliance con hallazgos, severidad y plan de remediación."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "governance"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Validación de Cumplimiento Arquitectónico

## Propósito
Validar que diseños de arquitectura, decisiones técnicas y especificaciones cumplen con los estándares, políticas y patrones de arquitectura de referencia de APB. Genera un informe de compliance con hallazgos, severidad y plan de remediación.

## Contexto de Uso
- Gate de arquitectura antes de aprobación de diseños.
- Revisión de compliance en code reviews de arquitectura.
- Validación de modernizaciones y migraciones contra arquitectura de referencia.
- Integración con workflows de gobierno y excepciones de riesgo.

## Entradas Requeridas
| Entrada | Tipo | Descripción | Obligatorio |
|---------|------|-------------|-------------|
| `architecture_document` | Texto / Markdown | Documento de arquitectura o diseño a validar | ✅ |
| `compliance_scope` | Lista | Estándares y políticas a validar: `architecture`, `security`, `performance`, `data` | ✅ |
| `architecture_ref_version` | Texto | Versión de la arquitectura de referencia APB | ❌ (usa última versión) |
| `exception_requests` | Lista | Excepciones previas solicitadas para este sistema | ❌ |

## Flujo de Trabajo (Pasos)
1. **Carga de estándares**: Obtener estándares y arquitectura de referencia vigentes.
2. **Análisis del diseño**: Parsear el documento de arquitectura (diagramas, decisiones, componentes).
3. **Validación por dimensión**:
   - **Arquitectura**: Patrones aprobados, separación de responsabilidades, anti-patterns prohibidos.
   - **Seguridad**: Cifrado, autenticación, autorización, principio de mínimo privilegio.
   - **Performance**: Caching, escalabilidad, latencia, throughput.
   - **Datos**: Modelo de datos, gobierno de datos, retención, privacidad.
   - **Operación**: Observabilidad, recoverability, configuración.
4. **Identificación de no-cumplimientos**: Para cada estándar no cumplido, documentar:
   - ID del estándar/política.
   - Severidad: Crítica / Alta / Media / Baja.
   - Descripción del hallazgo.
   - Recomendación de remediación.
   - Alternativa: solicitud de excepción con justificación.
5. **Evaluación de excepciones**: Si existen excepciones previas, verificar que siguen siendo válidas.
6. **Generación de informe**: Documento estructurado con puntuación de compliance y plan de acción.
7. **Registro de evidencia**: Metadatos para gobierno y trazabilidad.

## Salida Esperada
### Estructura del Informe
```markdown
# Informe de Cumplimiento Arquitectónico — [Nombre Sistema]
> Fecha: [YYYY-MM-DD] | Autor: Governance Agent | Ref: [versión arquitectura de referencia]

## 1. Alcance y Contexto
## 2. Estándares Evaluados
## 3. Resumen de Compliance
| Dimensión | Total Checks | Cumple | No Cumple | Excepción | % Compliance |
## 4. Hallazgos Detallados
| ID | Estándar | Dimensión | Severidad | Hallazgo | Recomendación | Excepción |
## 5. Plan de Remediación
## 6. Excepciones Vigentes
## 7. Recomendaciones
## 8. Evidencia y Metadatos
```

## Criterios de Calidad
- [ ] Todos los estándares del scope están evaluados.
- [ ] Cada hallazgo tiene severidad, recomendación y referencia al estándar violado.
- [ ] Excepciones vigentes validadas y vinculadas.
- [ ] Puntuación de compliance por dimensión con tendencia histórica si aplica.
- [ ] El informe es presentable al Comité de Arquitectura sin edición adicional.
- [ ] No se incluyen secretos ni datos sensibles del sistema evaluado.

## Stack y Tecnologías
- Arquitectura de referencia: `context/apb/standards/architecture-ref.md`
- Estándares: `context/apb/standards/`
- Parseo: Markdown AST, diagramas Mermaid/PlantUML
- Formatos: Markdown, Excel para matriz detallada

## Dependencias
- `apb-gov-standards-v1.0` — para acceso a estándares vigentes
- `apb-gov-arch-ref-v1.0` — para validación contra arquitectura de referencia
- `apb-gov-policy-check-v1.0` — para validación de políticas
- `apb-gov-evidence-v1.0` — para generación de evidencia
- `apb-wf-risk-exception-v1.0` — para gestión de excepciones

## Ejemplo de Uso
**Prompt de invocación:**
```
Valida el cumplimiento arquitectónico de nuestro diseño para el microservicio de notificaciones:
- Documento: docs/architecture/notifications-service.md
- Scope: architecture, security, performance
- Arquitectura de referencia: v2.1.0
- Excepciones previas: EXC-ARCH-003 (uso de Redis en lugar de Azure Cache for Redis por coste)
```

## Notas y Advertencias
- **Nivel 1**: El agente valida documentalmente; no realiza pruebas técnicas de performance ni seguridad.
- **Revisión humana obligatoria** antes de aprobar o rechazar un diseño basado en este informe.
- Los hallazgos críticos bloquean la aprobación de arquitectura hasta su resolución o excepción formal.
- El agente no modifica el documento de arquitectura; solo genera el informe de validación.

## Historial de Cambios
| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-20 | Arquitectura APB | Creación inicial |
