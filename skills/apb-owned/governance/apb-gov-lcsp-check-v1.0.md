---
id: "apb-gov-lcsp-check-v1.0"
name: "Verificación LCSP en Contratación Tecnológica"
description: "Verifica que un procedimiento de contratación tecnológica cumple la Ley de Contratos del Sector Público (LCSP). Determina el tipo de procedimiento según la cuantía, los criterios de adjudicación admisibles y la documentación requerida para el expediente."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "governance"
autonomy_level: 1
created_date: "2026-06-29"
review_date: "2026-12-29"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# Verificación LCSP en Contratación Tecnológica


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Propósito
Asegurar que los procedimientos de contratación de tecnología (software, hardware, servicios TI, consultoría) que APB como organismo del sector público debe seguir cumplen con la LCSP (Ley 9/2017). Determina el procedimiento correcto según la cuantía estimada, valida los criterios de adjudicación y genera el checklist de documentación requerida para el expediente de contratación.

## Contexto de Uso
- Inicio de un proceso de compra de software, servicios cloud o consultoría TI.
- Revisión previa al inicio del expediente de contratación para evitar impugnaciones.
- Soporte al responsable del contrato para elegir el procedimiento correcto.
- Preparación de la documentación del expediente (PCAP, PPT, memoria justificativa).

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `contract_object` | Texto | Objeto del contrato: qué se compra y para qué | ✅ |
| `estimated_value` | Número | Valor estimado del contrato en euros (sin IVA, todo el periodo incluidas prórrogas) | ✅ |
| `contract_type` | Enum | Tipo: `servicios` / `suministros` / `obras` / `concesion` | ✅ |
| `duration_months` | Número | Duración del contrato en meses, incluidas prórrogas | ✅ |
| `urgency` | Booleano | ¿Existe urgencia justificada que permita tramitación urgente? | ❌ |
| `framework_agreement` | Booleano | ¿Existe acuerdo marco o sistema dinámico de adquisición vigente para este objeto? | ❌ |

## Flujo de Trabajo

1. **Clasificación del contrato**:
   - Determinar tipo de contrato según objeto (servicios TI → contrato de servicios; hardware → suministros).
   - Calcular el valor estimado total incluyendo todas las prórrogas y opciones.

2. **Procedimiento aplicable según cuantía** (umbrales LCSP actualizados):

   | Cuantía (sin IVA) | Procedimiento | Plazo mínimo publicación |
   |---|---|---|
   | < 15.000 € | Contrato menor (servicios/suministros) | Sin publicidad |
   | 15.000 € – 100.000 € | Procedimiento abierto simplificado abreviado | 10 días |
   | 100.000 € – umbral europeo* | Procedimiento abierto simplificado | 20 días |
   | > umbral europeo* | Procedimiento abierto ordinario | 35 días (DOUE) |

   *Umbrales europeos (revisión bienal): servicios ~221.000 € para entidades del sector público no Administración General del Estado.

3. **Criterios de adjudicación admisibles**:
   - Precio: obligatorio, pero no puede ser el único criterio salvo en procedimientos simplificados abreviados por objeto estandarizado.
   - Criterios cualitativos: experiencia del equipo, metodología, calidad técnica, plan de proyecto.
   - Criterios sujetos a juicio de valor: máximo 50% de la puntuación total en procedimiento abierto ordinario.
   - Criterios automáticos (fórmulas): precio, plazo de entrega, características técnicas cuantificables.

4. **Checklist de documentación del expediente**:
   - Memoria justificativa de la necesidad y no disponibilidad interna.
   - Pliego de Cláusulas Administrativas Particulares (PCAP).
   - Pliego de Prescripciones Técnicas (PPT).
   - Informe de insuficiencia de medios propios (si aplica).
   - Certificado de existencia de crédito (intervención).
   - Documento de aprobación del gasto.

5. **Alertas de riesgo legal**:
   - Fraccionamiento del contrato para eludir umbrales (art. 99.2 LCSP) — detectar si el objeto puede ser parte de una necesidad mayor.
   - Criterios de adjudicación discriminatorios o no vinculados al objeto del contrato.
   - Modificaciones posteriores que superen el 20% del precio inicial (requieren nueva licitación).

6. **⚠️ CHECKPOINT HUMANO**: El responsable del contrato y el departamento jurídico/contratación de APB deben validar el procedimiento antes de iniciar el expediente.

## Salida Esperada

```markdown
# Verificación LCSP — [Objeto del contrato] — [Fecha]
> ⚠️ Borrador generado por IA (APB AI Framework - apb-gov-lcsp-check-v1.0) — pendiente validación humana. No iniciar expediente sin validación de Contratación APB.

## Clasificación del Contrato
| Atributo | Valor |
|---|---|
| Tipo de contrato | |
| Valor estimado total | |
| Procedimiento aplicable | |
| Publicidad obligatoria | |
| Plazo mínimo de publicación | |

## Criterios de Adjudicación Propuestos
| Criterio | Tipo | Peso (%) | Admisible LCSP |
|---|---|---|---|

## Checklist de Documentación
- [ ] Memoria justificativa
- [ ] PCAP borrador
- [ ] PPT borrador
- [ ] Informe insuficiencia medios propios
- [ ] Certificado existencia crédito
- [ ] Aprobación del gasto

## Alertas de Riesgo Legal
| Riesgo | Descripción | Recomendación |
|---|---|---|
```

## Criterios de Calidad
- [ ] El procedimiento está determinado por el valor estimado total (incluyendo prórrogas), no por el valor anual.
- [ ] Los criterios de adjudicación están vinculados al objeto del contrato.
- [ ] No se detecta fraccionamiento del objeto para eludir umbrales.
- [ ] La duración propuesta no supera los límites LCSP (máximo 4 años incluidas prórrogas para servicios).

## Dependencias
- `apb-gov-vendor-eval-v1.0` — la evaluación técnica de proveedores es el contenido del PPT
- `apb-gov-evidence-v1.0` — generación de evidencias del expediente de contratación

## Ejemplo de Uso

```
Queremos contratar un servicio de mantenimiento y soporte de la plataforma Azure DevOps para APB.
Duración: 2 años + 1 año de prórroga. Precio estimado: 45.000 € anuales.
¿Qué procedimiento LCSP debemos seguir y qué documentación necesitamos?
```

## Notas y Advertencias
- Los umbrales europeos se actualizan cada 2 años — verificar los vigentes en el BOE o la plataforma de contratación del sector público.
- APB puede estar sujeta a umbrales distintos según su clasificación como poder adjudicador — consultar con Contratación.
- Esta skill orienta sobre el procedimiento; la decisión final es siempre del responsable del contrato y el área jurídica.


## Prompt de Sistema

```
Eres el skill "Verificación LCSP en Contratación Tecnológica" (apb-gov-lcsp-check-v1.0) del APB AI Framework,
operando para la Autoritat Portuària de Barcelona (APB).

## Contexto Corporativo APB
Carga context/apb/knowledge/APB_KNOWLEDGE_BASE.md (provider: prov-apb-knowledge-v1.0)
antes de ejecutar cualquier tarea.

Contiene: negocio portuario (escalas, atraques, movimientos, tasas, concesiones),
catálogo de aplicaciones (ARGOS, SÒSTRAT, APIs DOCKS), integraciones (PORTIC/EDI,
AGE, AIS, VTS Kongsberg), terminología trilingüe CA/ES/EN y mapa de equipos/Jira.

Úsalo para entender el dominio, usar terminología correcta e identificar sistemas
y equipos involucrados. El legacy (SÒSTRAT/Java/Oracle/CAS/Alfresco) es contexto
informacional — nunca prescribas tecnologías fuera del stack aprobado.
Stack aprobado: context/apb/standards/STANDARD_ARCHITECTURE.md

## Misión
Verifica que un procedimiento de contratación tecnológica cumple la Ley de Contratos del Sector Público (LCSP). Determina el tipo de procedimiento según la cuantía, los criterios de adjudicación admisibles y la documentación requerida para el expediente.

## Inputs Esperados
(no especificado)

## Instrucciones
(no especificado)

## Restricciones
- Stack DOCKS únicamente: .NET, Azure SQL, EntraID, Service Bus, Redis, APIM,
  SharePoint — aunque el sistema analizado use Java/Oracle/CAS/Alfresco.
- Sin secretos ni credenciales en ningún output.
- Autonomy Level 1: todo output es borrador — requiere aprobación humana.
- Trazabilidad: skill_id/agent_id + usuario + fecha en todo output.

## Formato de Salida
(no especificado)
```

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento B |

## ⚠️ Comportamiento ante inputs incompletos

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `contract_object` | Pregunta: "¿Qué se va a contratar exactamente y para qué finalidad?" | Sí |
| `estimated_value` | Pregunta: "¿Cuál es el valor estimado total incluyendo prórrogas, sin IVA?" | Sí |
| `contract_type` | Pregunta: "¿Es un contrato de servicios, suministros u obras?" | Sí |
| `duration_months` | Pregunta: "¿Cuántos meses dura el contrato incluyendo todas las prórrogas previstas?" | Sí |
| `urgency` | Asume `false` (sin urgencia) | No |
| `framework_agreement` | Asume que no existe acuerdo marco vigente | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** — callout inmediatamente tras el título H1:
  > ⚠️ Borrador generado por IA (APB AI Framework - apb-gov-lcsp-check-v1.0) — pendiente validación humana. No iniciar expediente sin validación de Contratación APB.
- **Tickets Jira**: label `ia-generado` + footer en descripción.
