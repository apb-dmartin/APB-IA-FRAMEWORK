---
id: "apb-doc-changelog-v1.0"
name: "Generación de Changelog Semántico"
description: "Genera y mantiene el CHANGELOG.md de un proyecto APB siguiendo el estándar Keep a Changelog y versionado semántico (SemVer). A partir de los commits desde la última release, clasifica los cambios en Added, Changed, Deprecated, Removed, Fixed, Security y propone el número de versión siguiente."
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

# Generación de Changelog Semántico


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Propósito
Automatizar la generación y mantenimiento del CHANGELOG.md de proyectos APB siguiendo el estándar [Keep a Changelog](https://keepachangelog.com) y [SemVer](https://semver.org). A partir del historial de commits desde la última release, clasifica los cambios por tipo, filtra los commits que no aportan información al usuario (refactors internos, fixes de CI), y propone el número de versión siguiente según si los cambios son breaking, features o fixes.

## Contexto de Uso
- Preparación de una nueva release: generar el changelog antes de tagear.
- Auditoría del changelog existente: verificar que está al día y bien formateado.
- Comunicación a stakeholders: transformar commits técnicos en lenguaje de usuario.
- Compliance: algunos sistemas APB requieren historial de cambios para auditorías.

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `git_log` | Texto | Output de `git log --oneline` o `git log --format="%H %s %b"` desde la última release | ✅ |
| `project_name` | Texto | Nombre del proyecto | ✅ |
| `current_version` | Texto | Versión actual del proyecto (SemVer) | ✅ |
| `release_date` | Fecha | Fecha de la release (YYYY-MM-DD) | ❌ |
| `existing_changelog` | Texto | Contenido del CHANGELOG.md actual (para añadir en lugar de sobreescribir) | ❌ |

## Convención de Commits APB

APB usa Conventional Commits + prefijo `[ai-gen]` cuando el commit es generado por IA:

| Prefijo | Tipo de cambio | SemVer |
|---|---|---|
| `feat:` | Nueva funcionalidad | MINOR ↑ |
| `fix:` | Corrección de bug | PATCH ↑ |
| `feat!:` / `BREAKING CHANGE:` | Cambio que rompe compatibilidad | MAJOR ↑ |
| `docs:` | Solo documentación | Sin release (a criterio) |
| `refactor:` | Refactor sin cambio funcional | Sin release (a criterio) |
| `perf:` | Mejora de rendimiento | PATCH ↑ |
| `security:` | Fix de seguridad | PATCH ↑ (o MINOR si es nuevo control) |
| `chore:` / `ci:` | Mantenimiento CI/CD | No aparece en changelog |
| `[ai-gen]` | Generado por IA | Prefijo adicional, no afecta SemVer |

## Flujo de Trabajo

1. **Parsear el historial de commits**:
   - Clasificar cada commit en la categoría correspondiente (Added, Changed, Fixed, Security, etc.).
   - Filtrar commits de mantenimiento (`chore:`, `ci:`, `build:`) que no son relevantes para el usuario.
   - Identificar breaking changes (`feat!:` o `BREAKING CHANGE:` en el cuerpo).

2. **Determinar el tipo de release**:
   - Si hay breaking changes → incrementar MAJOR.
   - Si hay `feat:` sin breaking → incrementar MINOR.
   - Si solo hay `fix:`, `perf:`, `security:` → incrementar PATCH.

3. **Generar la entrada del changelog**:

```markdown
## [X.Y.Z] — YYYY-MM-DD

### Added
- [Funcionalidad nueva 1] — breve descripción orientada al usuario

### Changed
- [Cambio en funcionalidad existente]

### Fixed
- [Bug corregido] — describe el comportamiento corregido, no el código

### Security
- [Fix de seguridad] — descripción sin revelar detalles de la vulnerabilidad

### Deprecated
- [Funcionalidad que se retirará en la próxima versión mayor]

### Removed
- [Funcionalidad eliminada]
```

4. **Reglas de escritura del changelog**:
   - Orientado al usuario: "El usuario puede ahora X" en lugar de "Se refactorizó el módulo Y".
   - Presente en las entradas de Added: "Añade soporte para…", "Permite ahora…"
   - Pasado en Fixed: "Corregido el error que causaba…"
   - No incluir hashes de commit ni nombres de archivos (son ruido para el usuario).

5. **Fusionar con el changelog existente** si `existing_changelog` está presente:
   - Insertar la nueva entrada justo debajo de `## [Unreleased]` si existe, o al inicio.
   - No modificar entradas anteriores.

## Salida Esperada

```markdown
# Changelog — {project_name}

Todos los cambios notables en este proyecto están documentados aquí.
Formato: [Keep a Changelog](https://keepachangelog.com) | Versioning: [SemVer](https://semver.org)

> ⚠️ Borrador generado por IA (APB AI Framework - apb-doc-changelog-v1.0) — revisar antes de publicar.

## [Unreleased]

## [X.Y.Z] — YYYY-MM-DD

### Added
...
```

## Criterios de Calidad
- [ ] El número de versión propuesto sigue las reglas de SemVer correctamente.
- [ ] Cada entrada del changelog está orientada al usuario, no al código.
- [ ] Las entradas de seguridad no revelan detalles técnicos de la vulnerabilidad.
- [ ] Los commits de CI/CD y refactors internos no aparecen en el changelog.
- [ ] La sección `[Unreleased]` está presente para futuros cambios.

## Dependencias
- `apb-doc-release-notes-v1.0` — el changelog técnico se transforma en release notes de usuario
- `apb-plat-environment-promotion-v1.0` — el changelog se genera como parte del gate de release

## Ejemplo de Uso

```
Genera el changelog para la versión siguiente de GISPEM-API.
Versión actual: 2.3.1
git log desde la última release:
  feat: añadir endpoint GET /api/escalas/activas con paginación
  fix: corregir cálculo de tasas de escala cuando el buque tiene múltiples grúas
  security: actualizar dependencia Newtonsoft.Json vulnerable a CVE-2024-XXXX
  chore: actualizar pipeline GitHub Actions a ubuntu-24.04
  docs: actualizar README con instrucciones de despliegue AKS
```


## Prompt de Sistema

```
Eres el skill "Generación de Changelog Semántico" (apb-doc-changelog-v1.0) del APB AI Framework,
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
Genera y mantiene el CHANGELOG.md de un proyecto APB siguiendo el estándar Keep a Changelog y versionado semántico (SemVer). A partir de los commits desde la última release, clasifica los cambios en Added, Changed, Deprecated, Removed, Fixed, Security y propone el número de versión siguiente.

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
| `git_log` | Pregunta: "Necesito el historial de commits desde la última release. Ejecuta: `git log v{version}..HEAD --oneline`" | Sí |
| `project_name` | Pregunta: "¿Cuál es el nombre del proyecto?" | Sí |
| `current_version` | Pregunta: "¿Cuál es la versión actual del proyecto?" | Sí |
| `release_date` | Usa la fecha de hoy (2026-06-29) e indica la asunción | No |
| `existing_changelog` | Genera solo la nueva entrada sin fusionarla | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **CHANGELOG.md** — callout en la nueva entrada:
  > ⚠️ Borrador generado por IA (APB AI Framework - apb-doc-changelog-v1.0) — revisar antes de publicar.
