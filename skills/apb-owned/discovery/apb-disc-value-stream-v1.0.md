---
id: "apb-disc-value-stream-v1.0"
name: "Value Stream Mapping de Procesos Portuarios"
description: "Genera mapas de flujo de valor (Value Stream Maps) para procesos portuarios de APB. Identifica actividades de valor añadido vs. desperdicios (esperas, retrabajo, cuellos de botella), mide los tiempos de ciclo y propone el estado futuro optimizado con los cambios digitales o de proceso necesarios."
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

# Value Stream Mapping de Procesos Portuarios


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Propósito
Analizar y optimizar los procesos del Puerto de Barcelona usando Value Stream Mapping (VSM), una técnica Lean que visualiza el flujo completo de trabajo e información desde que el cliente solicita algo hasta que lo recibe. Identifica las actividades que añaden valor real, los desperdicios (esperas, reprocesos, movimientos innecesarios) y los cuellos de botella, y propone el estado futuro optimizado que una digitalización o mejora de proceso debería alcanzar.

## Contexto de Uso
- Análisis previo a la digitalización de un proceso manual o semi-manual APB.
- Diagnóstico de un proceso que tiene quejas de usuarios o tiempos de resolución elevados.
- Justificación de inversión en un nuevo sistema TI: "¿qué tiempo/coste ahorra digitalizar este proceso?"
- Workshop de mejora de procesos con las áreas de negocio de APB.
- Definición del scope de un nuevo sistema o funcionalidad.

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `process_name` | Texto | Nombre del proceso a mapear (ej. "Cierre de escala marítima y liquidación") | ✅ |
| `process_description` | Texto | Descripción del proceso: qué empieza, qué termina, quiénes intervienen | ✅ |
| `current_steps` | Lista | Pasos actuales del proceso con actor responsable y tiempo estimado | ❌ |
| `pain_points` | Lista | Problemas conocidos: cuellos de botella, esperas, errores frecuentes | ❌ |
| `volume` | Texto | Volumen del proceso: cuántas veces ocurre al día/semana/mes | ❌ |

## Tipos de Desperdicio Lean en Procesos Portuarios

| Desperdicio | Definición | Ejemplo APB |
|---|---|---|
| **Espera** | Tiempo en que nada avanza | Escala esperando validación de Sanidad Marítima |
| **Inventario** | Trabajo acumulado sin procesar | Cola de declaraciones de escala sin revisar |
| **Retrabajo** | Repetir una actividad por errores | Rellenar formulario otra vez por campos incorrectos |
| **Sobreproducción** | Hacer más de lo que el cliente necesita | Generar informes que nadie lee |
| **Movimiento** | Desplazamientos innecesarios | Enviar documentos en papel entre departamentos |
| **Transporte** | Mover información innecesariamente | Email con adjunto PDF en lugar de acceso directo al sistema |
| **Sobre-procesamiento** | Pasos del proceso que no añaden valor | Validación manual de datos que podrían validarse automáticamente |
| **Defectos** | Errores y correcciones | Errores en NIF/CIF de consignatario que retrasan la facturación |

## Estructura del Value Stream Map

```markdown
# Value Stream Map — [Proceso] — Estado Actual

## Información del flujo
- Volumen: [N procesos/día]
- Tiempo de ciclo total (lead time): [N días/horas]
- Tiempo de valor añadido: [N horas]
- Ratio de valor añadido: [%]

## Flujo de Proceso (Estado Actual)

| # | Actividad | Actor | Tiempo (min) | VA/NVA | Sistema | Problemas |
|---|---|---|---|---|---|---|
| 1 | Notificación ETA buque | Consignatario | 5 | VA | GISPEM | — |
| 2 | Revisión documentación | Capitanía | 120 | NVA (espera) | Manual/email | Hasta 4h de espera |
| 3 | Asignación de atraque | Práctico APB | 15 | VA | GISPEM | — |
| ... | | | | | | |

## Desperdicios Identificados
| Desperdicio | Actividad | Tiempo perdido | Impacto |
|---|---|---|---|

## Estado Futuro (propuesta)
[Proceso optimizado con las mejoras propuestas]

## Plan de Mejora
| Mejora | Tipo | Ahorro estimado | Esfuerzo | Prioridad |
|---|---|---|---|---|
```

## Flujo de Trabajo

1. **Definir los límites del proceso**: punto de inicio y punto de fin claros.

2. **Mapear el estado actual**:
   - Listar todos los pasos del proceso con actor responsable y tiempo.
   - Clasificar cada paso: VA (Value Added) o NVA (Non Value Added).
   - Identificar los desperdicios en cada paso.
   - Calcular el lead time total y el tiempo de valor añadido real.

3. **Identificar los cuellos de botella**:
   - El paso con mayor tiempo de espera o mayor variabilidad.
   - El paso más dependiente de factores externos (autoridades, otros sistemas).

4. **Diseñar el estado futuro**:
   - Eliminar pasos NVA que no añaden ningún valor (burocracia pura).
   - Digitalizar pasos manuales donde hay datos disponibles.
   - Paralelizar pasos que hoy son secuenciales sin necesidad de serlo.
   - Automatizar validaciones que hoy son revisiones manuales.

5. **Calcular el impacto** de las mejoras:
   - Tiempo ahorrado por instancia del proceso.
   - Reducción de errores (y retrabajo asociado).
   - Mejora en la experiencia del usuario (menos esperas, menos llamadas).

## Criterios de Calidad
- [ ] Cada paso del proceso tiene actor responsable y tiempo estimado.
- [ ] El ratio de valor añadido está calculado (tiempo VA / lead time total).
- [ ] Las mejoras propuestas están priorizadas por impacto vs. esfuerzo.
- [ ] El estado futuro es realista (no asume tecnología que APB no tiene ni prevé tener).

## Dependencias
- `apb-disc-user-journey-v1.0` — el journey del usuario y el VSM son perspectivas complementarias del mismo proceso
- `apb-disc-poc-guide-v1.0` — las mejoras digitales identificadas pueden requerir un PoC

## Ejemplo de Uso

```
Mapea el proceso de cierre de escala marítima en APB.
El proceso empieza cuando el práctico confirma el desatraque y termina cuando se emite la liquidación de tasas.
Actualmente intervienen: consignatario, Capitanía, APB (liquidación), posiblemente Sanidad Marítima.
Hay quejas de que el proceso puede tardar hasta 5 días laborables.
```

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento B |

## ⚠️ Comportamiento ante inputs incompletos

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `process_name` | Pregunta: "¿Qué proceso quieres mapear?" | Sí |
| `process_description` | Pregunta: "Describe el proceso: ¿qué lo inicia? ¿qué lo termina? ¿quiénes intervienen?" | Sí |
| `current_steps` | Genera la plantilla de estado actual con los pasos deducibles de la descripción; indica que deben validarse | No |
| `pain_points` | Genera el mapa sin pain points predefinidos; los identifica del proceso descrito | No |
| `volume` | Indica que sin datos de volumen no puede calcular el impacto total, solo el por instancia | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** — callout inmediatamente tras el título H1:
  > ⚠️ Borrador generado por IA (APB AI Framework - apb-disc-value-stream-v1.0) — validar los tiempos y pasos con las personas que ejecutan el proceso actualmente.
