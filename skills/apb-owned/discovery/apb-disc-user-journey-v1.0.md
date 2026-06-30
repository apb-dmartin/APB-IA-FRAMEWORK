---
id: "apb-disc-user-journey-v1.0"
name: "Mapas de Viaje del Usuario"
description: "Genera mapas de viaje del usuario (User Journey Maps) para los portales y servicios digitales de APB. Documenta las etapas del proceso, las acciones del usuario, los puntos de dolor, las emociones y las oportunidades de mejora. Orientado a diseño centrado en el usuario para servicios portuarios y ciudadanos."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "discovery"
autonomy_level: 1
created_date: "2026-06-29"
review_date: "2026-12-29"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# Mapas de Viaje del Usuario


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Propósito
Documentar la experiencia completa de un usuario al interactuar con un servicio digital APB, desde que tiene una necesidad hasta que la resuelve. Los User Journey Maps revelan los puntos de dolor (donde el usuario se frustra o abandona), los momentos de éxito, y las oportunidades de mejora que no son visibles analizando solo los datos de uso. Son la base del diseño centrado en el usuario (UCD) para los portales APB.

## Contexto de Uso
- Diseño de un nuevo portal o funcionalidad digital APB.
- Diagnóstico de problemas de usabilidad en un portal existente (alta tasa de abandono, quejas de usuarios).
- Priorización del backlog: ¿qué mejoras tienen mayor impacto en la experiencia del usuario?
- Presentación a stakeholders de negocio para explicar el impacto de una mejora UX.
- Input para auditoría de accesibilidad (`apb-qa-accessibility-v1.0`): los puntos de dolor pueden ser barreras de accesibilidad.

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `persona_name` | Texto | Nombre de la persona/perfil de usuario (ej. "Consignatario de un buque de carga") | ✅ |
| `persona_description` | Texto | Descripción del perfil: quién es, qué motivaciones tiene, contexto de uso | ✅ |
| `journey_scenario` | Texto | El escenario específico: qué quiere conseguir el usuario en este journey | ✅ |
| `touchpoints` | Lista | Puntos de contacto conocidos: formularios, emails, llamadas, portales web | ❌ |
| `existing_pain_points` | Lista | Puntos de dolor conocidos o quejas recibidas de usuarios | ❌ |

## Personas Tipo APB

| Persona | Perfil | Contexto de uso APB |
|---|---|---|
| **Consignatario** | Representa al armador del buque en el puerto. Gestiona escalas, trámites y servicios portuarios. | Portal de escalas marítimas, declaración de mercancías, liquidación de tasas. |
| **Transitario/Agente de aduanas** | Tramita la documentación aduanera de la mercancía. | Portal de documentación, comunicación con aduana. |
| **Ciudadano** | Persona que necesita un trámite administrativo con el Puerto de Barcelona. | Portal ciudadano APB, solicitudes de acceso, información pública. |
| **Empleado APB** | Trabajador interno que gestiona sistemas o procesos administrativos. | Aplicaciones internas, intranet, sistemas de RRHH. |
| **Operador logístico** | Gestiona el movimiento de mercancías dentro del puerto. | Sistemas de control de acceso, gestión de terminales. |

## Estructura del User Journey Map

```markdown
# User Journey Map — [Persona] — [Escenario]

## Persona
**Nombre:** [Persona]
**Perfil:** [Descripción]
**Objetivo:** [Qué quiere conseguir en este journey]

## Etapas del Journey

| Etapa | 1. Conciencia | 2. Inicio | 3. Proceso | 4. Resolución | 5. Post-servicio |
|---|---|---|---|---|---|
| **¿Qué hace?** | | | | | |
| **¿Qué piensa?** | | | | | |
| **¿Cómo se siente?** | 😐 | 🤔 | 😤 | 😊 | 😌 |
| **Puntos de contacto** | | | | | |
| **Puntos de dolor** | | | | | |
| **Oportunidades** | | | | | |

## Curva Emocional
[Descripción de cómo varía el estado emocional a lo largo del journey]

## Top 3 Oportunidades de Mejora
1. [Mayor impacto en la experiencia del usuario]
2. [Segunda prioridad]
3. [Tercera prioridad]
```

## Flujo de Trabajo

1. **Definir la persona y el escenario** con precisión — un journey demasiado genérico no revela nada útil.

2. **Mapear las etapas** (adaptar según el servicio):
   - Conciencia: ¿cómo sabe el usuario que necesita hacer algo?
   - Inicio: ¿cómo accede al servicio? (¿sabe a dónde ir?)
   - Proceso: ¿qué pasos sigue? ¿dónde se atasca?
   - Resolución: ¿consigue lo que necesita? ¿está satisfecho?
   - Post-servicio: ¿tiene que hacer seguimiento? ¿recibe notificaciones?

3. **Identificar puntos de dolor** en cada etapa:
   - Información difícil de encontrar.
   - Formularios complejos o que piden datos redundantes.
   - Tiempos de espera sin feedback.
   - Errores sin mensajes claros.
   - Necesidad de llamar por teléfono porque el portal no resuelve.

4. **Priorizar oportunidades** por impacto en el usuario y esfuerzo de implementación.

## Salida Esperada

```markdown
# User Journey Map — [Persona] — [Escenario] — [Fecha]
> ⚠️ Borrador generado por IA (APB AI Framework - apb-disc-user-journey-v1.0) — validar con usuarios reales antes de tomar decisiones de diseño.

[Tabla del journey completa + curva emocional + oportunidades]
```

## Criterios de Calidad
- [ ] El journey está basado en datos reales o supuestos explícitamente marcados como hipótesis.
- [ ] Las emociones del usuario reflejan la realidad del servicio, no el ideal.
- [ ] Las oportunidades de mejora están priorizadas por impacto al usuario.
- [ ] El journey tiene al menos 4 etapas claramente diferenciadas.

## Dependencias
- `apb-disc-value-stream-v1.0` — el value stream mapping complementa el journey a nivel de proceso interno
- `apb-qa-accessibility-v1.0` — los puntos de dolor pueden revelar barreras de accesibilidad
- `apb-design-wcag-patterns-v1.0` — los patrones accesibles son la solución a muchos puntos de dolor

## Ejemplo de Uso

```
Genera el User Journey Map para un consignatario que necesita declarar la escala de un buque de carga en GISPEM.
El consignatario recibe la notificación del ETA del buque con 24h de antelación y debe preparar toda la documentación.
Sabemos que tiene problemas en el paso de declaración de mercancías peligrosas.
```

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento B |

## ⚠️ Comportamiento ante inputs incompletos

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `persona_name` | Pregunta: "¿Para qué perfil de usuario quieres el journey? (consignatario, ciudadano, empleado APB...)" | Sí |
| `persona_description` | Pregunta: "Describe el perfil: quién es, qué motivaciones tiene y en qué contexto usa el servicio" | Sí |
| `journey_scenario` | Pregunta: "¿Qué quiere conseguir el usuario en este journey específico?" | Sí |
| `touchpoints` | Genera el journey con los touchpoints deducibles del escenario; indica que pueden faltar | No |
| `existing_pain_points` | Genera el journey sin pain points predefinidos; indica que deben validarse con usuarios reales | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** — callout inmediatamente tras el título H1:
  > ⚠️ Borrador generado por IA (APB AI Framework - apb-disc-user-journey-v1.0) — validar con usuarios reales antes de tomar decisiones de diseño.
