---
id: "apb-pm-stakeholder-map-v1.0"
name: "Mapa de Stakeholders (Interés × Influencia)"
description: "Genera el mapa de stakeholders de un proyecto APB usando la matriz interés × influencia. Identifica a los actores clave (internos y externos), su posición respecto al proyecto, la estrategia de comunicación recomendada para cada cuadrante y el plan de gestión de stakeholders."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "pm"
autonomy_level: 1
created_date: "2026-06-29"
review_date: "2026-12-29"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# Mapa de Stakeholders (Interés × Influencia)


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Propósito
Identificar y gestionar proactivamente a todos los actores que tienen interés o influencia sobre un proyecto APB. La matriz de interés × influencia permite priorizar los esfuerzos de comunicación y gestión: los stakeholders con alta influencia y alto interés son los más críticos para el éxito del proyecto. Incluye tanto stakeholders internos de APB (dirección, áreas de negocio, TI) como externos (autoridades, proveedores, usuarios finales).

## Contexto de Uso
- Inicio de un proyecto: identificar a todos los stakeholders antes de arrancar.
- Detección de resistencia al cambio: ¿quién puede bloquear el proyecto?
- Planificación de la comunicación: ¿a quién, con qué frecuencia y con qué detalle?
- Revisión del mapa en proyectos largos (cambian los stakeholders con el tiempo).
- Gestión de un conflicto entre stakeholders.

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `project_name` | Texto | Nombre del proyecto | ✅ |
| `project_description` | Texto | Qué hace el proyecto y a quién afecta | ✅ |
| `known_stakeholders` | Lista | Stakeholders ya identificados | ❌ |
| `project_type` | Enum | `digitalizacion` / `infraestructura-ti` / `normativo` / `nuevo-servicio` | ❌ |

## Matriz Interés × Influencia

```
Alta   | MANTENER SATISFECHOS  | GESTIONAR DE CERCA       |
Influencia | (informar regularmente) | (involucrar activamente)  |
       |------------------------|--------------------------|
Baja   | MONITORIZAR           | MANTENER INFORMADOS      |
       | (mínimo esfuerzo)     | (información periódica)  |
       |--------------------------------------------|
                 Bajo                     Alto
                            Interés
```

| Cuadrante | Estrategia de comunicación |
|---|---|
| **Alta influencia, alto interés** (Gestionar de cerca) | Involucrar en decisiones clave, reuniones frecuentes, validaciones tempranas |
| **Alta influencia, bajo interés** (Mantener satisfechos) | Informar de avances sin sobrecargar; alertar proactivamente si algo les afecta |
| **Baja influencia, alto interés** (Mantener informados) | Newsletter/informe periódico, canales de feedback, hacer que se sientan escuchados |
| **Baja influencia, bajo interés** (Monitorizar) | Mínimo contacto; pueden convertirse en advocates si se les involucra bien |

## Stakeholders Típicos en Proyectos APB

| Stakeholder | Tipo | Proyectos relevantes |
|---|---|---|
| Director de Sistemas / CIO APB | Interno / Alta influencia | Todos los proyectos TI |
| Dirección operaciones portuarias | Interno / Alta influencia | Sistemas operativos |
| Área de Contratación APB | Interno / Alta influencia | Proyectos con licitación LCSP |
| DPO / Protección de Datos | Interno / Alta influencia si hay datos personales | Proyectos con datos personales |
| Jefe de proyecto / PM | Interno / Alta influencia, alto interés | Todos |
| Responsable del sistema (área negocio) | Interno / Alto interés | Sistema específico |
| Usuarios clave (operadores, consignatarios) | Externo / Alto interés | Sistemas operativos |
| Autoridad Portuaria del Estado | Externo / Alta influencia | Proyectos regulados |
| Proveedores TI contratados | Externo / Alto interés | Proyectos con externalización |
| AEPD / Reguladores | Externo / Alta influencia, bajo interés habitual | Proyectos con datos sensibles |

## Flujo de Trabajo

1. **Identificar stakeholders** para el proyecto específico.
2. **Posicionar en la matriz**: evaluar interés e influencia de cada uno (Alto/Bajo).
3. **Identificar la posición respecto al proyecto**: Supportive / Neutral / Resistant / Unknown.
4. **Definir la estrategia de comunicación** para cada cuadrante.
5. **Plan de gestión de stakeholders**:
   - Frecuencia de comunicación por stakeholder.
   - Canal de comunicación preferido.
   - Quién gestiona la relación (PM, responsable técnico, dirección APB).

## Salida Esperada

```markdown
# Mapa de Stakeholders — [Proyecto] — [Fecha]
> ⚠️ Borrador generado por IA (APB AI Framework - apb-pm-stakeholder-map-v1.0) — validar con el project manager y el patrocinador del proyecto.

## Matriz Interés × Influencia

| Stakeholder | Tipo | Influencia | Interés | Cuadrante | Posición | Estrategia |
|---|---|---|---|---|---|---|
| CIO APB | Interno | Alta | Bajo | Mantener satisfecho | Supportive | Briefing mensual |
| Responsable GISPEM | Interno | Media | Alta | Gestionar de cerca | Supportive | Reunión semanal |
| Área Contratación | Interno | Alta | Bajo | Mantener satisfecho | Neutral | Informar en hitos clave |
| Consignatarios | Externo | Baja | Alta | Mantener informados | Desconocido | Newsletter + talleres UAT |

## Plan de Comunicación
| Stakeholder | Frecuencia | Canal | Contenido | Responsable |
|---|---|---|---|---|

## Riesgos de Gestión de Stakeholders
| Stakeholder | Riesgo | Mitigación |
|---|---|---|
```

## Criterios de Calidad
- [ ] Todos los stakeholders con influencia alta están en el cuadrante correcto y tienen estrategia definida.
- [ ] La posición de cada stakeholder (supportive/neutral/resistant) está evaluada, no asumida.
- [ ] El plan de comunicación tiene frecuencia, canal y responsable definidos.
- [ ] El mapa se revisará en proyectos largos al menos trimestralmente.

## Ejemplo de Uso

```
Genera el mapa de stakeholders para el proyecto de digitalización del proceso de cierre de escalas en APB.
El proyecto automatiza un proceso manual que actualmente involucra a: consignatarios, practicaje, facturación APB, y ocasionalmente a Sanidad Marítima y Aduana.
Internamente: la dirección de operaciones portuarias es el patrocinador.
```


## Prompt de Sistema

```
Eres el skill "Mapa de Stakeholders (Interés × Influencia)" (apb-pm-stakeholder-map-v1.0) del APB AI Framework,
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
Genera el mapa de stakeholders de un proyecto APB usando la matriz interés × influencia. Identifica a los actores clave (internos y externos), su posición respecto al proyecto, la estrategia de comunicación recomendada para cada cuadrante y el plan de gestión de stakeholders.

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
| `project_name` | Pregunta: "¿Cuál es el nombre del proyecto?" | Sí |
| `project_description` | Pregunta: "Describe el proyecto: ¿qué hace y a quién afecta?" | Sí |
| `known_stakeholders` | Identifica stakeholders típicos para el tipo de proyecto APB; indica que pueden faltar actores | No |
| `project_type` | Identifica el tipo del proyecto de la descripción e indica la inferencia | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** — callout inmediatamente tras el título H1:
  > ⚠️ Borrador generado por IA (APB AI Framework - apb-pm-stakeholder-map-v1.0) — validar con el project manager y el patrocinador del proyecto.
