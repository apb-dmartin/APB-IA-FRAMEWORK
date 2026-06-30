---
id: "apb-sec-threat-model-v1.0"
name: "Threat Modeling (STRIDE)"
description: "Generar un modelo de amenazas estructurado basado en la metodología STRIDE para identificar, clasificar y priorizar riesgos de seguridad en aplicaciones, arquitecturas y flujos de datos. La skill produce un informe actionable con controles mitigadores y trazabilidad hacia requisitos ENS y OWASP."
version: "1.0.0"
status: "draft"
owner: "Ciberseguridad APB <arquitectura@portdebarcelona.cat>"
domain: "security"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# Threat Modeling (STRIDE)


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Propósito
Generar un modelo de amenazas estructurado basado en la metodología STRIDE para identificar, clasificar y priorizar riesgos de seguridad en aplicaciones, arquitecturas y flujos de datos. La skill produce un informe actionable con controles mitigadores y trazabilidad hacia requisitos ENS y OWASP.

> **Diferencia con `apb-sec-risk-analysis-v1.0`:** Esta skill analiza **amenazas técnicas por componente arquitectónico** (STRIDE: Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation). Úsala en **diseño de sistemas** para identificar vectores de ataque concretos. `apb-sec-risk-analysis-v1.0` analiza **riesgos por activo de negocio** (ISO 27005/MAGERIT): probabilidad × impacto a nivel organizativo. Úsala en **auditorías de cumplimiento** y evaluaciones periódicas.

## Contexto de Uso
- Diseño de nuevas aplicaciones o microservicios antes del despliegue.
- Revisiones de arquitectura existente durante auditorías de seguridad.
- Validación de cumplimiento de requisitos de seguridad corporativos.
- Integración con workflows de gobierno y excepciones de riesgo.

## Entradas Requeridas
| Entrada | Tipo | Descripción | Obligatorio |
|---------|------|-------------|-------------|
| `system_description` | Texto / Markdown | Descripción del sistema, arquitectura o flujo de datos a modelar | ✅ |
| `data_flow_diagram` | Diagrama / Texto | DFD (Data Flow Diagram) en formato texto, Mermaid, imagen o descripción narrativa | ✅ |
| `trust_boundaries` | Lista | Límites de confianza identificados (red, proceso, almacenamiento) | ✅ |
| `compliance_scope` | Lista | Marcos de cumplimiento aplicables: ENS, OWASP, ISO 27001 | ❌ |
| `existing_controls` | Lista | Controles de seguridad ya implementados | ❌ |

## Flujo de Trabajo (Pasos)
1. **Ingesta y validación**: Verificar que el DFD y la descripción del sistema son coherentes. Solicitar aclaraciones si faltan trust boundaries.
2. **Decomposición STRIDE**: Para cada elemento del DFD (proceso, flujo de datos, almacén, entidad externa), aplicar las 6 categorías STRIDE:
   - **Spoofing** (Suplantación)
   - **Tampering** (Manipulación)
   - **Repudiation** (Repudio)
   - **Information Disclosure** (Divulgación de información)
   - **Denial of Service** (Denegación de servicio)
   - **Elevation of Privilege** (Elevación de privilegios)
3. **Identificación de amenazas**: Generar amenazas específicas con formato: `[STRIDE] <Amenaza> en <Elemento DFD>`.
4. **Clasificación de riesgo**: Asignar severidad (Crítica / Alta / Media / Baja) usando matriz de riesgo corporativa (probabilidad × impacto).
5. **Controles mitigadores**: Para cada amenaza de severidad Alta o Crítica, proponer controles técnicos, organizativos o de proceso.
6. **Generación de informe**: Estructurar el resultado en formato markdown con tablas, diagramas de trazabilidad y checklist de verificación.
7. **Registro de evidencia**: Incluir metadatos de trazabilidad para integración con gobierno y auditorías.

## Salida Esperada
### Estructura del Informe
```markdown
# Threat Model Report — [Nombre del Sistema]
> Fecha: [YYYY-MM-DD] | Autor: Security Architect Agent | Estado: draft

## 1. Alcance y Contexto
## 2. Data Flow Diagram (DFD)
## 3. Trust Boundaries
## 4. Matriz STRIDE
| Elemento DFD | Spoofing | Tampering | Repudiation | Info Disclosure | DoS | EoP |
## 5. Amenazas Identificadas
| ID | Amenaza | Elemento | Categoría STRIDE | Severidad | Control Propuesto | Estado |
## 6. Resumen de Riesgos
## 7. Trazabilidad a Compliance
## 8. Recomendaciones y Próximos Pasos
## 9. Evidencia y Metadatos
```

## Criterios de Calidad
- [ ] Todos los elementos del DFD tienen al menos una amenaza identificada.
- [ ] 100% de amenazas Críticas/Altas tienen control mitigador propuesto.
- [ ] Trazabilidad explícita a ENS/OWASP cuando `compliance_scope` está definido.
- [ ] El informe es revisable por un auditor de seguridad sin intervención del agente.
- [ ] No se incluyen secretos, credenciales ni datos sensibles reales en el modelo.

## Stack y Tecnologías
- Metodología: STRIDE (Microsoft SDL)
- Frameworks de referencia: OWASP ASVS, ENS (Esquema Nacional de Seguridad)
- Diagramas: Mermaid.js para DFD, PlantUML opcional
- Formatos de salida: Markdown, PDF vía pandoc

## Dependencias
- `apb-sec-ens-v1.0` — para validación de controles ENS
- `apb-sec-owasp-v1.0` — para mapeo a categorías OWASP
- `apb-gov-evidence-v1.0` — para generación de evidencia documental
- `apb-gov-policy-check-v1.0` — para validación de políticas de seguridad

## Ejemplo de Uso
**Prompt de invocación:**
```
Genera un threat model STRIDE para el siguiente microservicio de pagos:
- Recibe órdenes de pago vía API REST (HTTPS)
- Valida token JWT emitido por Identity Provider corporativo
- Persiste transacciones en Azure SQL (encriptado en reposo)
- Publica evento "PaymentCompleted" a Azure Service Bus
- Trust boundaries: Internet → API Gateway → Microservicio → BD → Event Bus
Compliance scope: ENS Alto, OWASP ASVS Nivel 2
```

## Notas y Advertencias
- **Nivel 1**: El agente identifica amenazas pero no ejecuta pruebas de penetración ni modifica código.
- **Revisión humana obligatoria** para amenazas clasificadas como Críticas antes de su aceptación.
- No sustituye a un pentest profesional; es una actividad de diseño seguro (security by design).
- Los diagramas DFD deben validarse contra la arquitectura real; el agente asume la corrección de la entrada.

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
  > **Borrador generado por IA** (APB AI Framework - apb-sec-threat-model-v1.0) - pendiente validacion humana. No distribuir sin revision.
