---
id: "apb-plat-environment-promotion-v1.0"
name: "Promoción de Entornos dev → staging → prod"
description: "Define y ejecuta el proceso de promoción de cambios entre entornos en APB (dev → staging → prod). Genera la checklist de gates de calidad por entorno, el pipeline de promoción en GitHub Actions/Jenkins y el runbook de rollback si la promoción falla."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
created_date: "2026-06-29"
review_date: "2026-12-29"
---

# Promoción de Entornos dev → staging → prod

## Propósito
Estandarizar el proceso de promoción de código entre los entornos de APB (desarrollo, preproducción/staging, producción) con gates de calidad obligatorios. Genera la checklist de aprobación por entorno, el pipeline CI/CD en GitHub Actions y/o Jenkins para automatizar los gates, y el runbook de rollback si la promoción a producción causa regresiones.

## Contexto de Uso
- Configuración del pipeline de despliegue de una nueva aplicación APB.
- Revisión de un proceso de promoción existente para añadir gates de calidad faltantes.
- Preparación del checklist de aprobación antes de una promoción a producción.
- Incidente post-despliegue: ejecutar el rollback según el runbook.

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `system_name` | Texto | Nombre del sistema cuyo pipeline se define | ✅ |
| `tech_stack` | Lista | Stack tecnológico: lenguajes, frameworks, tipo de artefacto (Docker, NuGet, etc.) | ✅ |
| `operation` | Enum | `generar-pipeline` / `generar-checklist` / `runbook-rollback` | ✅ |
| `ci_tool` | Enum | `github-actions` / `jenkins` / `ambos` | ❌ |
| `deployment_target` | Enum | `aks` / `app-service` / `function-app` / `static-web-app` | ❌ |

## Gates de Calidad por Entorno

### Dev → Staging
| Gate | Obligatorio | Herramienta |
|---|---|---|
| Build sin errores | ✅ | MSBuild / pip / npm |
| Tests unitarios (cobertura ≥70%) | ✅ | xUnit / pytest |
| SAST (análisis estático) | ✅ | SonarQube + `apb-sec-sast-v1.0` |
| Análisis de dependencias (CVEs) | ✅ | Dependabot / OWASP |
| Lint y formato de código | ✅ | dotnet format / pylint / ESLint |
| Imagen Docker sin vulnerabilidades HIGH/CRITICAL | ✅ | Trivy / Defender for Containers |

### Staging → Prod
| Gate | Obligatorio | Herramienta |
|---|---|---|
| Tests de integración | ✅ | Playwright + `apb-sub-qa-e2e-v1.0` |
| Tests de performance (p95 < umbral) | Recomendado | k6 + `apb-qa-performance-v1.0` |
| Review manual del tech lead | ✅ | Pull Request approval |
| Aprobación del responsable del sistema | ✅ | Manual (cambios que impactan negocio) |
| Smoke test en staging (funcionalidades críticas) | ✅ | Playwright headless |
| Revisión de secretos y configuración de entorno | ✅ | Checklist manual |
| Change window respetada | ✅ | Sin despliegues en prod viernes tarde o vísperas de festivos |

## Flujo de Trabajo

### Generación del pipeline GitHub Actions

```yaml
# Estructura del pipeline de promoción APB
name: CI/CD — {system_name}

on:
  push:
    branches: [main]
  pull_request:
    branches: [main, release/*]

jobs:
  build-and-test:
    # Build, unit tests, SAST, dependency check
    
  deploy-dev:
    needs: build-and-test
    environment: dev
    # Deploy automático a dev tras merge a main
    
  gate-to-staging:
    needs: deploy-dev
    # Tests de integración, smoke tests en dev
    
  deploy-staging:
    needs: gate-to-staging
    environment: staging
    # Deploy automático a staging
    
  gate-to-prod:
    needs: deploy-staging
    environment: staging-approval
    # Aprobación manual requerida
    # Tests de performance, revisión de responsable
    
  deploy-prod:
    needs: gate-to-prod
    environment: production
    # Deploy con estrategia blue-green o rolling
```

### Runbook de rollback en producción

```markdown
## Runbook: Rollback de despliegue en producción

**Tiempo objetivo: <15 minutos desde detección del problema**

### Criterios para activar rollback
- Error rate > 5% en las primeras 30 min post-despliegue
- Tiempo de respuesta p95 > 2x el baseline
- Funcionalidad crítica de negocio no disponible

### Pasos de rollback (AKS)
1. [ ] Confirmar la versión anterior del Deployment (kubectl rollout history)
2. [ ] Ejecutar rollback: `kubectl rollout undo deployment/{app-name} -n apb-prod`
3. [ ] Verificar que los pods de la versión anterior están Running
4. [ ] Confirmar que los smoke tests pasan en la versión revertida
5. [ ] Notificar al equipo y al responsable del sistema
6. [ ] Abrir ticket de incidente con causa raíz
```

## Salida Esperada

Pipeline YAML listo para usar + checklist de gates en formato Markdown + runbook de rollback.

## Criterios de Calidad
- [ ] Todos los gates obligatorios están implementados o tienen excepción documentada.
- [ ] La aprobación manual de staging→prod requiere al menos 2 personas (tech lead + responsable del sistema).
- [ ] El rollback está automatizable y probado (no solo documentado).
- [ ] No hay despliegues directos a producción sin pasar por staging.

## Dependencias
- `apb-plat-k8s-v1.0` — los manifiestos de despliegue son el artefacto que se promueve
- `apb-sec-sast-v1.0` — gate de seguridad en el pipeline
- `apb-qa-performance-v1.0` — gate de performance antes de prod

## Ejemplo de Uso

```
Genera el pipeline de promoción para el sistema GISPEM (API .NET 8 + Django backend, desplegado en AKS).
Queremos usar GitHub Actions. 
Actualmente no tenemos ningún pipeline y hacemos despliegues manuales.
```

## Notas y Advertencias
- Los entornos de GitHub Actions (`environment:`) requieren configuración previa de reviewers en el repositorio GitHub APB.
- La ventana de cambio en producción APB excluye: viernes después de las 15:00, vísperas de festivos nacionales y locales (Barcelona), y período de alta operativa portuaria (Semana Santa, agosto).
- Un rollback de base de datos es mucho más complejo que un rollback de aplicación — si el despliegue incluye migraciones de BD irreversibles, el rollback requiere restauración de backup.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento B |

## ⚠️ Comportamiento ante inputs incompletos

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `system_name` | Pregunta: "¿Para qué sistema se define el pipeline?" | Sí |
| `tech_stack` | Pregunta: "¿Qué lenguajes y frameworks usa el sistema?" | Sí |
| `operation` | Pregunta: "¿Qué necesitas: generar el pipeline, la checklist de gates o el runbook de rollback?" | Sí |
| `ci_tool` | Asume GitHub Actions (herramienta principal APB) e indica la asunción | No |
| `deployment_target` | Asume AKS e indica la asunción | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** — callout inmediatamente tras el título H1:
  > ⚠️ Borrador generado por IA (APB AI Framework - apb-plat-environment-promotion-v1.0) — pendiente revisión del equipo de plataforma APB.
- **YAML de pipelines** — comentario en cabecera:
  ```yaml
  # ⚠️ Generado por APB AI Framework (apb-plat-environment-promotion-v1.0) — revisar antes de activar en producción.
  ```
