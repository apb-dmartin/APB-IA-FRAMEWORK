---
id: "apb-doc-release-notes-v1.0"
name: "Release Notes orientadas al Usuario"
description: "Transforma el changelog técnico de una release APB en notas de versión orientadas al usuario final (ciudadanos, operadores portuarios, empleados). Adapta el lenguaje según el perfil de la audiencia, destaca las mejoras más relevantes y documenta las instrucciones de migración cuando es necesario."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "documentation"
autonomy_level: 1
created_date: "2026-06-29"
review_date: "2026-12-29"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# Release Notes orientadas al Usuario


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Propósito
Transformar el changelog técnico (orientado al equipo de desarrollo) en notas de versión comprensibles para los usuarios finales: operadores portuarios, personal de APB, ciudadanos que acceden a portales, y proveedores. El lenguaje debe ser claro, sin jerga técnica, y destacar el impacto en el trabajo diario del usuario, no los cambios en el código.

## Contexto de Uso
- Comunicación de una nueva release a los usuarios del sistema.
- Publicación en el portal de APB o en los canales de comunicación internos (intranet, Teams).
- Respuesta a usuarios que preguntan "¿qué cambia en la nueva versión?".
- Documentación obligatoria de releases en sistemas con auditoría (contratación pública, gestión portuaria).

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `changelog_entry` | Texto | Entrada del CHANGELOG.md de la versión a comunicar | ✅ |
| `version` | Texto | Número de versión (SemVer) | ✅ |
| `system_name` | Texto | Nombre del sistema o portal | ✅ |
| `audience` | Enum | `operadores` / `ciudadanos` / `empleados-apb` / `proveedores` / `tecnico` | ✅ |
| `release_date` | Fecha | Fecha de despliegue en producción | ❌ |
| `migration_steps` | Texto | Instrucciones de migración o acciones que el usuario debe realizar | ❌ |

## Audiencias y Adaptación de Lenguaje

| Audiencia | Perfil | Tono | Qué incluir |
|---|---|---|---|
| **operadores** | Usuarios técnicos del puerto: practicantes, consignatarios, estibadores | Directo, sin jerga TI | Nuevas funciones en su flujo de trabajo, cambios en formularios, mejoras de velocidad |
| **ciudadanos** | Usuarios del portal ciudadano: solicitudes, trámites | Simple, cordial | Solo cambios que afectan a los trámites que hacen |
| **empleados-apb** | Personal interno APB | Neutro, profesional | Cambios en aplicaciones internas, nuevas funcionalidades |
| **proveedores** | Consignatarios, agentes, transitarios | Directo, con impacto en sus procesos | Cambios en formularios de declaración, APIs que usan |
| **tecnico** | Equipo TI, integradores, desarrolladores | Técnico, completo | Cambios de API, breaking changes, instrucciones de migración |

## Flujo de Trabajo

1. **Traducir entradas del changelog a impacto de usuario**:

   | Changelog técnico | Release note para usuario |
   |---|---|
   | `feat: añadir endpoint GET /api/escalas/activas con paginación` | "Nuevo listado de escalas activas con paginación — la consulta de escalas en curso es ahora más rápida y permite filtrar por tipo de mercancía." |
   | `fix: corregir cálculo de tasas de escala cuando el buque tiene múltiples grúas` | "Corregido un error en el cálculo de tasas para buques con múltiples grúas — si detectabas diferencias en el importe, este error ya está resuelto." |
   | `security: actualizar dependencia vulnerable` | No aparece en release notes de usuario — es información interna |

2. **Estructura de las release notes**:

```markdown
# Novedades en {sistema} v{versión} — {fecha}

## ¿Qué hay de nuevo?
{2-3 frases con las mejoras más relevantes para el usuario}

## Mejoras
- **[Funcionalidad]**: descripción en términos de impacto en el usuario

## Correcciones
- **[Problema resuelto]**: descripción del comportamiento anterior y el nuevo

## Cambios importantes
{Solo si hay cambios que requieren que el usuario haga algo diferente}
- Antes hacías X, ahora debes hacer Y
- El formulario Z ha cambiado: [instrucciones]

## ¿Tienes alguna duda?
Contacta con el servicio de atención al usuario: soporte@portdebarcelona.cat
```

3. **Filtrar información sensible**:
   - No incluir detalles de vulnerabilidades de seguridad en las release notes públicas.
   - No incluir nombres de sistemas internos, nombres de servidores, conexiones de base de datos.
   - Si hay cambios de API breaking, notificar SOLO a la audiencia técnica.

4. **Instrucciones de migración** (cuando aplica):
   - ¿Deben el usuario o los integradores hacer algo antes del despliegue?
   - ¿Hay formularios que cambian y requieren que el usuario revise sus borradores?
   - ¿Hay datos exportados que necesitan reimportarse en el nuevo formato?

## Salida Esperada

```markdown
# Novedades en [Sistema] v[X.Y.Z] — [Fecha]
> ⚠️ Borrador generado por IA (APB AI Framework - apb-doc-release-notes-v1.0) — revisar con el responsable del sistema antes de comunicar.

[Contenido de las release notes adaptado a la audiencia]
```

## Criterios de Calidad
- [ ] Las release notes no contienen jerga técnica (para audiencias no técnicas).
- [ ] Cada punto describe el impacto en el usuario, no el cambio en el código.
- [ ] Las instrucciones de migración son pasos concretos y numerados.
- [ ] Los cambios de seguridad solo aparecen si son visibles al usuario; los internos se omiten.
- [ ] El tono es adecuado para la audiencia declarada.

## Dependencias
- `apb-doc-changelog-v1.0` — el changelog es la fuente de datos para las release notes

## Ejemplo de Uso

```
Genera release notes para los operadores portuarios de la versión 2.4.0 de GISPEM.
Changelog:
- Añade listado de escalas activas con paginación
- Corregido error en cálculo de tasas con múltiples grúas
- Actualiza interfaz de cierre de escala para incluir campo de incidencias
- Mejora del rendimiento del buscador de buques (p95 de 800ms a 200ms)
```

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento B |

## ⚠️ Comportamiento ante inputs incompletos

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `changelog_entry` | Pregunta: "¿Cuál es el contenido del changelog de la versión a comunicar?" | Sí |
| `version` | Pregunta: "¿Cuál es el número de versión?" | Sí |
| `system_name` | Pregunta: "¿De qué sistema o portal son estas release notes?" | Sí |
| `audience` | Pregunta: "¿A quién van dirigidas las release notes: operadores, ciudadanos, empleados APB, proveedores o audiencia técnica?" | Sí |
| `release_date` | Usa la fecha de hoy e indica la asunción | No |
| `migration_steps` | Genera release notes sin sección de migración; indica que debe añadirse si hay pasos requeridos | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos de release notes** — callout inmediatamente tras el título H1:
  > ⚠️ Borrador generado por IA (APB AI Framework - apb-doc-release-notes-v1.0) — revisar con el responsable del sistema antes de comunicar.
