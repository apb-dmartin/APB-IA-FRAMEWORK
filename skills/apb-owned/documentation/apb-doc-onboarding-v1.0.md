---
id: "apb-doc-onboarding-v1.0"
name: "Guía de Onboarding para Desarrolladores"
description: "Genera la guía de onboarding técnico para desarrolladores nuevos en un proyecto APB. Cubre la configuración del entorno local (herramientas, accesos, repos), la arquitectura del sistema, las convenciones del equipo y los primeros pasos para contribuir. Reduce el tiempo hasta primera contribución de semanas a días."
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

# Guía de Onboarding para Desarrolladores


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Propósito
Acelerar la incorporación de nuevos desarrolladores a proyectos APB reduciendo el tiempo hasta la primera contribución productiva. Genera una guía estructurada que cubre la configuración del entorno local, la arquitectura del sistema, las convenciones del equipo, los procesos de desarrollo (Git flow, PR, CI/CD) y las primeras tareas sugeridas para ganar contexto.

## Contexto de Uso
- Incorporación de un nuevo desarrollador al equipo de un proyecto APB.
- Actualización de la guía de onboarding cuando el entorno o las convenciones cambian significativamente.
- Base de conocimiento para personal temporal o proveedores externos con acceso al código.
- Auditoría del README del proyecto: ¿está al día para que alguien externo pueda arrancar?

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `project_name` | Texto | Nombre del proyecto | ✅ |
| `tech_stack` | Lista | Stack tecnológico: lenguajes, frameworks, bases de datos, servicios Azure | ✅ |
| `repo_structure` | Texto | Descripción de la estructura de carpetas del repositorio | ✅ |
| `team_conventions` | Texto | Convenciones del equipo: Git flow, naming, PR checklist, etc. | ❌ |
| `local_dependencies` | Lista | Herramientas a instalar localmente (Docker, Node, .NET SDK, etc.) | ❌ |
| `access_requirements` | Lista | Accesos necesarios: repos GitHub, Azure, Jira, etc. | ❌ |

## Estructura de la Guía de Onboarding APB

### 1. Bienvenida al proyecto
- Qué es el sistema, para qué sirve, quiénes lo usan.
- Contactos del equipo y canales de comunicación (Teams/Slack).
- Documentación de referencia clave (Confluence, Wiki, Jira proyecto).

### 2. Prerequisitos y accesos
Checklist para el primer día:
- [ ] Acceso a GitHub APB (organización `portdebarcelona`)
- [ ] Acceso a Azure Portal (subscription del proyecto)
- [ ] Acceso a Jira (proyecto del sistema)
- [ ] Acceso a Confluence (espacio del equipo)
- [ ] Cuenta en Azure DevOps (si aplica)
- [ ] VPN APB configurada

### 3. Configuración del entorno local

```markdown
## Herramientas necesarias
- .NET 8 SDK: [instrucciones]
- Node.js 20 LTS: [instrucciones]
- Docker Desktop: [instrucciones]
- Azure CLI: [instrucciones]
- Git configurado con email corporativo APB

## Clonar el repositorio
```bash
git clone https://github.com/portdebarcelona/{repo-name}
cd {repo-name}
```

## Configurar variables de entorno locales
```bash
cp .env.example .env.local
# Editar .env.local con los valores de desarrollo (NO los de producción)
# Los secretos de dev están en Azure Key Vault apb-dev — solicitar acceso al tech lead
```

## Arrancar el entorno local
```bash
docker compose up -d  # Base de datos, cache, servicios externos mockeados
dotnet restore
dotnet run --project src/Api
```
```

### 4. Arquitectura del sistema
- Diagrama de componentes (C4 Level 2 si existe).
- Flujos principales del dominio (ej. "ciclo de vida de una escala marítima").
- Integraciones con otros sistemas APB.
- Bases de datos y responsabilidades de cada una.

### 5. Convenciones de desarrollo
- **Git flow APB**: `main` (producción), `develop` (staging), `feature/`, `hotfix/`.
- **Commits**: Conventional Commits + prefijo `[ai-gen]` si es generado por IA.
- **Pull Requests**: mínimo 1 reviewer técnico + checks de CI en verde.
- **Naming**: kebab-case para APIs, PascalCase para clases C#, snake_case para Python.
- **Tests**: todo nuevo código debe tener tests unitarios (xUnit/.NET, pytest/Python).

### 6. Pipeline CI/CD
- Qué pipeline corre en cada PR.
- Cómo interpretar los resultados de SonarQube.
- Proceso de despliegue: dev (automático en merge) → staging (automático) → prod (manual).

### 7. Primeros pasos sugeridos
1. Leer el README del proyecto y este onboarding completo.
2. Configurar el entorno local y ejecutar los tests: `dotnet test`.
3. Revisar los últimos 10 PRs mergeados para entender el estilo de código.
4. Tomar una tarea de "good first issue" en Jira.
5. Hacer un PR pequeño de "onboarding" (ej. mejorar este mismo documento).

## Salida Esperada

```markdown
# Onboarding — {project_name} — Actualizado {fecha}
> ⚠️ Borrador generado por IA (APB AI Framework - apb-doc-onboarding-v1.0) — revisar y completar con el tech lead del proyecto.

[Guía completa de onboarding]
```

## Criterios de Calidad
- [ ] Un desarrollador nuevo puede arrancar el entorno local siguiendo la guía sin ayuda adicional.
- [ ] Los comandos están probados y funcionan en el entorno actual.
- [ ] La guía incluye los contactos de a quién acudir cuando algo falla.
- [ ] Hay una sección de troubleshooting con los errores más comunes al arrancar.

## Dependencias
- `apb-arch-c4-model-v1.0` — los diagramas de arquitectura son parte del onboarding

## Ejemplo de Uso

```
Genera la guía de onboarding para el proyecto GISPEM-API.
Stack: .NET 8, Entity Framework, Azure SQL, Azure Service Bus.
Repositorio con estructura: src/Api, src/Domain, src/Infrastructure, tests/.
Necesito que cubra desde la configuración local hasta el proceso de PR.
```

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento B |

## ⚠️ Comportamiento ante inputs incompletos

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `project_name` | Pregunta: "¿Cuál es el nombre del proyecto?" | Sí |
| `tech_stack` | Pregunta: "¿Qué tecnologías usa el proyecto (lenguajes, frameworks, bases de datos, servicios Azure)?" | Sí |
| `repo_structure` | Pregunta: "¿Cuál es la estructura de carpetas del repositorio?" | Sí |
| `team_conventions` | Usa las convenciones estándar APB (Conventional Commits, Git flow APB, PR con 1 reviewer) | No |
| `local_dependencies` | Incluye las herramientas estándar del stack indicado | No |
| `access_requirements` | Incluye los accesos estándar APB (GitHub, Azure, Jira) | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** — callout inmediatamente tras el título H1:
  > ⚠️ Borrador generado por IA (APB AI Framework - apb-doc-onboarding-v1.0) — revisar y completar con el tech lead del proyecto.
