---
id: "apb-arch-api-lifecycle-v1.0"
name: "Gestión del Ciclo de Vida de APIs"
description: "Gestiona el ciclo de vida completo de las APIs REST de APB: estrategia de versionado (URI, header o content negotiation), política de deprecación con sunset period, plan de comunicación a consumidores, y proceso de retirada controlada. Alineado con API-first design y OpenAPI."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "architecture"
autonomy_level: 1
created_date: "2026-06-29"
review_date: "2026-12-29"
---

# Gestión del Ciclo de Vida de APIs

## Propósito
Proporcionar un marco de gobierno para el ciclo de vida de las APIs REST de APB: desde el diseño inicial y publicación, pasando por el versionado semántico de la API, la gestión de breaking changes, la deprecación con sunset period, hasta la retirada definitiva. Garantiza que los consumidores (sistemas internos APB y sistemas externos) tienen tiempo suficiente para migrar y que la comunicación es proactiva y estructurada.

## Contexto de Uso
- Publicación de una nueva versión mayor de una API que tiene breaking changes.
- Planificación de la deprecación de una versión antigua de API que ya tiene sustituta.
- Auditoría del portfolio de APIs APB: ¿cuántas versiones están activas? ¿Alguna está near-end-of-life?
- Diseño de la estrategia de versionado para una nueva API.
- Comunicación formal a consumidores de una API sobre cambios próximos.

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `operation` | Enum | `versionar` / `deprecar` / `retirar` / `auditar-portfolio` | ✅ |
| `api_name` | Texto | Nombre de la API (ej. `gispem-escalas-api`) | ✅ |
| `current_version` | Texto | Versión actual (ej. `v2`) | ✅ |
| `change_description` | Texto | Descripción de los cambios (para `versionar`) | Condicional |
| `consumers` | Lista | Sistemas consumidores de la API conocidos | ❌ |
| `sunset_period_months` | Número | Meses de preaviso antes de retirar una versión | ❌ |

## Política de Versionado APB

### Estrategia: versionado en URI (preferida)
```
/api/v1/escalas     → versión 1 (puede coexistir con v2)
/api/v2/escalas     → versión 2 (versión actual)
```

Alternativa para APIs internas: `Accept: application/vnd.apb.v2+json` (negociación de contenido).

### Cuándo incrementar la versión
| Tipo de cambio | ¿Necesita nueva versión? | Tipo de versión |
|---|---|---|
| Nuevo campo opcional en response | No (additive change) | — |
| Nuevo endpoint | No (additive change) | — |
| Cambio en validación que acepta más valores | No | — |
| Eliminar campo del response | Sí — breaking change | MAJOR (v2 → v3) |
| Cambiar tipo de un campo | Sí — breaking change | MAJOR |
| Cambiar semántica de un campo | Sí — breaking change | MAJOR |
| Cambiar método HTTP de un endpoint | Sí — breaking change | MAJOR |
| Nueva versión menor compatible | Opcional — informativo | MINOR (v2.1) |

## Política de Sunset APB

| Tipo de API | Sunset period mínimo |
|---|---|
| API interna (solo consumidores APB internos) | 6 meses |
| API con consumidores externos (puertos, proveedores) | 12 meses |
| API crítica de infraestructura | 18 meses o más |

## Flujo de Trabajo

### Operación: versionar (nueva versión mayor)

1. **Documentar los breaking changes** en el OpenAPI spec de la nueva versión.
2. **Mantener la versión anterior activa** durante el sunset period.
3. **Añadir header de deprecación** a las respuestas de la versión antigua:
   ```http
   Deprecation: true
   Sunset: Sat, 01 Jan 2028 00:00:00 GMT
   Link: <https://api.apb.es/v3/escalas>; rel="successor-version"
   ```
4. **Notificar a los consumidores conocidos** con el plan de migración.
5. **Publicar guía de migración**: qué cambia y cómo actualizar el código del consumidor.

### Operación: deprecar

1. **Anunciar la deprecación** con la fecha de sunset.
2. **Activar los headers de deprecación** en la versión a retirar.
3. **Monitorizar uso**: ¿siguen llegando llamadas a la versión deprecated?
4. **Contactar activamente** a los consumidores que aún usan la versión deprecated.
5. **Hito de sunset**: si quedan consumidores activos, escalar antes de retirar.

### Operación: retirar

1. Verificar que no hay consumidores activos (logs de Azure API Management / Azure Monitor).
2. Devolver HTTP 410 Gone en los endpoints retirados (no 404 — debe ser explícito).
3. Mantener la documentación OpenAPI histórica accesible (no eliminar).
4. Notificación final a los consumidores registrados.

### Operación: auditar-portfolio

1. Listar todas las versiones activas de cada API.
2. Identificar versiones con >18 meses de antigüedad sin candidato a retirada.
3. Identificar APIs con versiones deprecated cuya fecha de sunset está próxima (<3 meses).
4. Identificar APIs sin documentación OpenAPI actualizada.

## Salida Esperada

```markdown
# Ciclo de Vida de API — {api_name} — [Fecha]
> ⚠️ Borrador generado por IA (APB AI Framework - apb-arch-api-lifecycle-v1.0) — validar con el equipo propietario de la API y comunicar a los consumidores.

## Estado de Versiones
| Versión | Estado | Fecha publicación | Sunset date | Consumidores conocidos |
|---|---|---|---|---|
| v1 | Deprecated | | 2027-01-01 | Sistema de Facturación |
| v2 | Active | | — | Sistema de Facturación, Portal Ciudadano |

## Plan de Comunicación a Consumidores
| Consumidor | Contacto | Fecha de contacto | Estado migración |
|---|---|---|---|

## Guía de Migración v1 → v2
### Cambios breaking
| Endpoint | Cambio | Cómo migrar |
|---|---|---|

## Headers de Deprecación
[Ejemplos de respuesta HTTP con headers]
```

## Criterios de Calidad
- [ ] Todas las versiones activas tienen documentación OpenAPI actualizada.
- [ ] Las versiones deprecated tienen header `Sunset` configurado.
- [ ] Los consumidores conocidos han sido notificados formalmente de la deprecación.
- [ ] No se retira ninguna versión con consumidores activos sin contacto previo.
- [ ] Los endpoints retirados devuelven HTTP 410 Gone, no 404.

## Dependencias
- `apb-arch-context-mapping-v1.0` — los consumidores de una API son los sistemas downstream en el Context Map
- `apb-qa-contract-testing-v1.0` — los contratos Pact ayudan a detectar breaking changes antes del despliegue
- `apb-agent-api-product-manager-v1.0` — agente que gestiona el portfolio completo de APIs APB

## Ejemplo de Uso

```
La API de Escalas de GISPEM (v1) tiene breaking changes en la nueva versión v2.
Los campos "fechaAtraque" y "fechaDesatraque" cambian de string ISO8601 a timestamp Unix.
Consumidores conocidos: Sistema de Facturación y Portal del Ciudadano.
¿Cuál es el plan de deprecación y qué comunicamos a los consumidores?
```

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento B |

## ⚠️ Comportamiento ante inputs incompletos

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `operation` | Pregunta: "¿Qué quieres hacer: versionar (nueva versión), deprecar una versión existente, retirar una versión, o auditar el portfolio de APIs?" | Sí |
| `api_name` | Pregunta: "¿Cuál es el nombre de la API?" | Sí |
| `current_version` | Pregunta: "¿Cuál es la versión actual de la API?" | Sí |
| `change_description` | Solo requerido para `versionar` — pregunta si falta | Condicional |
| `consumers` | Genera plan sin tabla de consumidores; indica que deben identificarse antes de comunicar | No |
| `sunset_period_months` | Aplica la política estándar APB según el tipo de API | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** — callout inmediatamente tras el título H1:
  > ⚠️ Borrador generado por IA (APB AI Framework - apb-arch-api-lifecycle-v1.0) — validar con el equipo propietario de la API y comunicar a los consumidores.
