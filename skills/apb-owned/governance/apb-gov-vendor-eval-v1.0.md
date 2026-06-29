---
id: "apb-gov-vendor-eval-v1.0"
name: "Evaluación Técnica de Proveedores"
description: "Genera la ficha de evaluación técnica de un proveedor tecnológico: capacidad técnica, solvencia económica, historial de seguridad, SLAs ofrecidos vs. requisitos APB, plan de continuidad y riesgo de lock-in. Input directo al PPT de una licitación LCSP."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "governance"
autonomy_level: 1
created_date: "2026-06-29"
review_date: "2026-12-29"
---

# Evaluación Técnica de Proveedores

## Propósito
Proporcionar un marco estructurado para evaluar técnicamente a proveedores tecnológicos antes de adjudicarles un contrato. Genera una ficha comparativa que cubre la capacidad técnica, solvencia, SLAs, seguridad, continuidad de negocio y riesgo de lock-in. Diseñado para alimentar el Pliego de Prescripciones Técnicas (PPT) de licitaciones LCSP y para Due Diligence de nuevos proveedores estratégicos.

## Contexto de Uso
- Evaluación de candidatos en una licitación tecnológica (criterios de adjudicación técnicos).
- Due Diligence antes de adoptar un nuevo proveedor de servicios cloud o SaaS.
- Revisión periódica de proveedores existentes (renovación de contrato, incidentes de servicio).
- Análisis de riesgo de concentración en proveedores críticos.

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `vendor_name` | Texto | Nombre del proveedor a evaluar | ✅ |
| `service_description` | Texto | Servicio o solución a contratar | ✅ |
| `apb_requirements` | Lista | Requisitos técnicos y de servicio que APB necesita cubrir | ✅ |
| `vendor_proposal` | Documento/Texto | Propuesta técnica del proveedor (si disponible) | ❌ |
| `criticality` | Enum | Criticidad para APB: `low` / `medium` / `high` / `critical` | ❌ |
| `alternatives` | Lista | Lista de proveedores alternativos para comparativa | ❌ |

## Flujo de Trabajo

1. **Capacidad técnica**:
   - Años de experiencia en el servicio ofertado.
   - Referencias de clientes similares (sector público, puertos, infraestructuras críticas).
   - Certificaciones relevantes: ISO 27001, ISO 9001, ENS, SOC 2, CSA STAR.
   - Stack tecnológico declarado y compatibilidad con el ecosistema APB (.NET, Azure, Jenkins).

2. **Solvencia económica**:
   - Facturación anual en los últimos 3 ejercicios.
   - Riesgo de insolvencia: indicadores de estabilidad financiera.
   - Dependencia de APB como cliente (si APB representa >20% de su facturación, riesgo de discontinuidad).

3. **SLAs ofrecidos vs. requisitos APB**:

   | Dimensión | Requerido por APB | Ofertado por proveedor | Brecha |
   |---|---|---|---|
   | Disponibilidad | ≥99.5% | | |
   | RTO ante incidente crítico | <4h | | |
   | RPO ante pérdida de datos | <1h | | |
   | Tiempo de respuesta L1 | <15 min | | |
   | Tiempo de resolución P1 | <4h | | |

4. **Seguridad y cumplimiento**:
   - Certificaciones de seguridad (ISO 27001, ENS, SOC 2 Type II).
   - Historial de brechas de seguridad en los últimos 3 años.
   - Política de gestión de vulnerabilidades y tiempos de parcheo.
   - Ubicación de los datos (dentro/fuera de la UE — impacto RGPD y ENS).
   - Cláusulas de auditoría y derecho de inspección del cliente.

5. **Plan de continuidad del proveedor**:
   - Plan de continuidad de negocio propio (BCP/DRP).
   - Subcontratistas críticos y sus propias garantías.
   - Plan de salida: portabilidad de datos, período de transición, formato de exportación.

6. **Riesgo de lock-in**:
   - ¿Usa estándares abiertos o formatos propietarios?
   - ¿Los datos son exportables en formatos estándar sin coste adicional?
   - ¿Existe dependencia de APIs propietarias sin equivalente en el mercado?
   - Coste estimado de migración a un proveedor alternativo.

7. **Puntuación agregada** (si se evalúan múltiples proveedores):
   - Tabla comparativa con pesos por dimensión.
   - Recomendación razonada: proveedor recomendado y condiciones de adjudicación sugeridas.

8. **⚠️ CHECKPOINT HUMANO**: Dirección TI / Contratación APB debe validar la evaluación y la recomendación antes de incluirla en el expediente de licitación.

## Salida Esperada

```markdown
# Evaluación Técnica — [Proveedor] — [Fecha]
> ⚠️ Borrador generado por IA (APB AI Framework - apb-gov-vendor-eval-v1.0) — pendiente validación humana. No usar en expediente sin revisión de Dirección TI y Contratación.

## Resumen Ejecutivo
| Dimensión | Puntuación (1-5) | Comentario |
|---|---|---|
| Capacidad técnica | | |
| Solvencia económica | | |
| Cumplimiento de SLAs | | |
| Seguridad y cumplimiento | | |
| Plan de continuidad | | |
| Riesgo de lock-in | | |
| **TOTAL** | | |

## Análisis Detallado por Dimensión
[...]

## Brechas detectadas respecto a requisitos APB
| Requisito | Estado | Mitigación propuesta |
|---|---|---|

## Riesgos Identificados
| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|

## Recomendación
```

## Criterios de Calidad
- [ ] Todos los requisitos APB declarados tienen respuesta explícita del proveedor o gap documentado.
- [ ] Los SLAs ofertados se comparan numéricamente con los requeridos (no solo cualitativamente).
- [ ] El riesgo de lock-in está cuantificado (coste estimado de salida).
- [ ] La ubicación de los datos está confirmada (dentro/fuera UE).

## Dependencias
- `apb-gov-lcsp-check-v1.0` — el procedimiento de contratación encuadra esta evaluación
- `apb-sec-risk-analysis-v1.0` — la evaluación de seguridad del proveedor es input para el análisis de riesgos

## Ejemplo de Uso

```
Evalúa al proveedor Microsoft para el contrato de licencias Microsoft 365 E3 para APB.
Requisitos: disponibilidad 99.9%, soporte 24x7, datos en región Europa, cumplimiento ENS medio.
Criticidad: high (afecta a toda la organización).
```

## Notas y Advertencias
- Esta evaluación no es vinculante — es una herramienta de soporte a la decisión. La adjudicación final sigue los criterios establecidos en el PCAP.
- Para proveedores de infraestructura crítica (ENS Alto), considerar auditoría de seguridad independiente adicional.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento B |

## ⚠️ Comportamiento ante inputs incompletos

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `vendor_name` | Pregunta: "¿Qué proveedor se va a evaluar?" | Sí |
| `service_description` | Pregunta: "¿Qué servicio o solución ofrece este proveedor a APB?" | Sí |
| `apb_requirements` | Pregunta: "¿Cuáles son los requisitos técnicos y de servicio mínimos que APB necesita?" | Sí |
| `vendor_proposal` | Genera estructura de evaluación con campos vacíos para completar | No |
| `criticality` | Asume `medium` e indica la asunción explícitamente | No |
| `alternatives` | Genera evaluación de proveedor único sin comparativa | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** — callout inmediatamente tras el título H1:
  > ⚠️ Borrador generado por IA (APB AI Framework - apb-gov-vendor-eval-v1.0) — pendiente validación humana. No usar en expediente sin revisión de Dirección TI y Contratación.
