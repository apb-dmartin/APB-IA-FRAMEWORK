---
id: "apb-gov-dpia-v1.0"
name: "Evaluación de Impacto de Protección de Datos (DPIA/EIPD)"
description: "Conduce una Evaluación de Impacto de Protección de Datos (DPIA, art. 35 RGPD) para sistemas de APB que tratan datos de alto riesgo. Genera el informe completo: descripción del tratamiento, necesidad y proporcionalidad, riesgos identificados, medidas de mitigación y recomendación final."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "governance"
autonomy_level: 1
created_date: "2026-06-29"
review_date: "2026-12-29"
---

# Evaluación de Impacto de Protección de Datos (DPIA/EIPD)

## Propósito
Automatizar la elaboración del borrador de la Evaluación de Impacto en la Protección de Datos (DPIA o EIPD en terminología española) según el artículo 35 del RGPD y las directrices del Grupo de Trabajo del artículo 29 (WP248). Obligatoria cuando el tratamiento es susceptible de entrañar un alto riesgo para los derechos y libertades de las personas físicas. Produce un informe estructurado listo para revisión del DPO y consulta previa a la AEPD si es necesario.

## Contexto de Uso
- Nuevo sistema que usa tecnologías de vigilancia, biometría, geolocalización o perfilado a gran escala.
- Tratamiento de datos de categoría especial (salud, ideología, origen étnico) a gran escala.
- Sistemas automatizados de toma de decisiones con efecto jurídico sobre personas.
- Revisión de sistemas existentes ante cambio significativo en el tratamiento.
- La DPIA es obligatoria cuando concurren 2 o más de los 9 criterios del CEPD.

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `system_name` | Texto | Nombre del sistema o tratamiento | ✅ |
| `treatment_description` | Texto | Descripción detallada del tratamiento: qué datos, para qué, quién, cómo | ✅ |
| `legal_basis` | Texto | Base jurídica del tratamiento (art. 6 o 9.2 RGPD) | ✅ |
| `data_classification` | Documento | Output de `apb-gov-data-classification-v1.0` (si disponible) | ❌ |
| `data_volume` | Número | Número estimado de interesados afectados | ❌ |
| `automated_decisions` | Booleano | ¿El sistema toma decisiones automatizadas con efecto jurídico? | ❌ |

## Flujo de Trabajo

1. **Verificación de obligatoriedad** (criterios CEPD WP248):
   Marcar los criterios que aplican al sistema — si ≥2, la DPIA es obligatoria:
   - [ ] Evaluación o puntuación de personas (scoring, perfilado)
   - [ ] Decisiones automatizadas con efecto legal
   - [ ] Supervisión sistemática (videovigilancia, seguimiento de comportamiento)
   - [ ] Datos sensibles o de naturaleza muy personal
   - [ ] Tratamiento a gran escala (>10.000 interesados o datos de menores)
   - [ ] Combinación de conjuntos de datos de múltiples fuentes
   - [ ] Tratamiento de datos de personas vulnerables (menores, empleados, pacientes)
   - [ ] Uso innovador o aplicación de nuevas tecnologías (IA, biometría, IoT)
   - [ ] Transferencias internacionales de datos

2. **Descripción sistemática del tratamiento**:
   - Naturaleza de los datos (qué tipos se tratan).
   - Alcance y contexto (cuántos interesados, con qué frecuencia, en qué geografía).
   - Finalidades y medios (para qué y cómo).
   - Responsable del tratamiento y encargados (proveedores con acceso).

3. **Evaluación de necesidad y proporcionalidad**:
   - ¿La finalidad es legítima y explícita?
   - ¿Los datos recogidos son los mínimos necesarios (minimización)?
   - ¿La base jurídica es adecuada para el nivel de riesgo?
   - ¿Existen alternativas menos intrusivas para la privacidad?

4. **Identificación y evaluación de riesgos**:

   | Riesgo | Descripción | Probabilidad (1-3) | Impacto (1-3) | Riesgo bruto |
   |---|---|---|---|---|
   | Acceso no autorizado | Brecha de seguridad que expone datos personales | | | |
   | Uso indebido de datos | Tratamiento para finalidades distintas a las declaradas | | | |
   | Exactitud / calidad | Datos incorrectos usados en decisiones que afectan a interesados | | | |
   | Transferencia ilegal | Datos enviados a terceros sin base jurídica | | | |
   | Perfilado discriminatorio | Decisiones automatizadas sesgadas por origen, género, edad | | | |

5. **Medidas previstas para mitigar los riesgos**:
   - Técnicas: cifrado, seudonimización, control de acceso, auditoría.
   - Organizativas: formación, políticas de acceso, contratos con encargados.
   - Jurídicas: cláusulas contractuales, bases jurídicas adecuadas.

6. **Riesgo residual y recomendación**:
   - Si el riesgo residual tras medidas sigue siendo alto → consulta previa obligatoria a la AEPD (art. 36 RGPD).
   - Si el riesgo residual es aceptable → aprobación del DPO + Dirección APB.

7. **⚠️ CHECKPOINT HUMANO**: El DPO de APB debe revisar y firmar el informe DPIA antes de iniciar el tratamiento. Si se requiere consulta previa a la AEPD, la dirección APB debe aprobarlo.

## Salida Esperada

```markdown
# DPIA/EIPD — [Sistema] — [Fecha]
> ⚠️ Borrador generado por IA (APB AI Framework - apb-gov-dpia-v1.0) — pendiente revisión y firma del DPO. No iniciar el tratamiento sin este informe completado.

## 1. Descripción del Tratamiento
### 1.1 Naturaleza de los datos
### 1.2 Alcance y contexto
### 1.3 Finalidades
### 1.4 Responsable y encargados

## 2. Necesidad y Proporcionalidad
| Criterio | Evaluación | Observaciones |
|---|---|---|

## 3. Riesgos Identificados y Medidas
| Riesgo | Riesgo bruto | Medidas | Riesgo residual |
|---|---|---|---|

## 4. Recomendación
[ ] Puede iniciarse el tratamiento con las medidas indicadas
[ ] Requiere consulta previa a la AEPD (art. 36 RGPD)
[ ] No puede iniciarse — riesgo residual inaceptable

## 5. Aprobaciones
| Rol | Nombre | Fecha | Firma |
|---|---|---|---|
| DPO APB | | | |
| Responsable del sistema | | | |
```

## Criterios de Calidad
- [ ] La obligatoriedad de la DPIA está justificada con los criterios CEPD aplicables.
- [ ] Todos los encargados del tratamiento (proveedores con acceso a datos) están identificados.
- [ ] Cada riesgo tiene al menos una medida de mitigación propuesta.
- [ ] El riesgo residual está calculado para cada riesgo tras aplicar las medidas.
- [ ] Si el riesgo residual es alto, se indica explícitamente la necesidad de consulta previa.

## Dependencias
- `apb-gov-data-classification-v1.0` — el inventario de datos es prerequisito de la DPIA
- `apb-sec-risk-analysis-v1.0` — los riesgos de seguridad son parte de la DPIA

## Ejemplo de Uso

```
Realiza una DPIA para el sistema de control de acceso biométrico (huella dactilar) 
que APB quiere instalar en las zonas de acceso restringido del puerto.
Afecta a aproximadamente 2.000 empleados y trabajadores portuarios.
Base jurídica: interés legítimo del responsable (seguridad de instalaciones críticas).
```

## Notas y Advertencias
- Los datos biométricos son categoría especial del art. 9 RGPD — la base jurídica de interés legítimo no es suficiente; se requiere una de las excepciones del art. 9.2.
- APB, como organismo del sector público, puede tener obligaciones adicionales según la normativa española de protección de datos (LOPDGDD).
- Esta DPIA es un borrador — el DPO de APB es el único que puede aprobarla.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento B |

## ⚠️ Comportamiento ante inputs incompletos

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `system_name` | Pregunta: "¿Cuál es el nombre del sistema o tratamiento a evaluar?" | Sí |
| `treatment_description` | Pregunta: "Describe el tratamiento: qué datos se tratan, para qué, quién los trata y cómo" | Sí |
| `legal_basis` | Pregunta: "¿Cuál es la base jurídica del tratamiento (art. 6 o 9.2 RGPD)?" | Sí |
| `data_classification` | Conduce la clasificación internamente como paso previo a la DPIA | No |
| `data_volume` | Asume "volumen desconocido" e indica que debe completarse para la sección de riesgo | No |
| `automated_decisions` | Asume `false` e indica la asunción explícitamente | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** — callout inmediatamente tras el título H1:
  > ⚠️ Borrador generado por IA (APB AI Framework - apb-gov-dpia-v1.0) — pendiente revisión y firma del DPO.
