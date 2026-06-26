---
id: "apb-plat-cicd-v1.0"
name: "Generación de Pipelines CI/CD"
description: "Generar pipelines de integración continua y despliegue continuo (CI/CD) adaptadas al stack tecnológico de APB (.NET, Azure, Docker). La skill produce archivos de pipeline (Jenkinsfile, GitHub Actions, Azure DevOps YAML) con stages de build, test, security scan, quality gate y deploy, incluyendo v..."
version: "1.0.0"
status: "draft"
owner: "DevOps APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Generación de Pipelines CI/CD

## Propósito
Generar pipelines de integración continua y despliegue continuo (CI/CD) adaptadas al stack tecnológico de APB (.NET, Azure, Docker). La skill produce archivos de pipeline (Jenkinsfile, GitHub Actions, Azure DevOps YAML) con stages de build, test, security scan, quality gate y deploy, incluyendo validación de estándares corporativos.

## Contexto de Uso
- Onboarding de nuevos proyectos/microservicios al sistema de CI/CD corporativo.
- Modernización de pipelines legacy a formatos y prácticas actuales.
- Integración de nuevas herramientas de seguridad o calidad en pipelines existentes.
- Generación de pipelines multi-entorno (dev, staging, production) con gates de aprobación.

## Entradas Requeridas
| Entrada | Tipo | Descripción | Obligatorio |
|---------|------|-------------|-------------|
| `project_type` | Enum | `dotnet-api`, `dotnet-web`, `devexpress-front`, `django-api`, `terraform` | ✅ |
| `repo_url` | Texto | URL del repositorio de código | ✅ |
| `ci_platform` | Enum | `jenkins`, `github-actions`, `azure-devops` | ✅ |
| `environments` | Lista | Entornos de despliegue: `dev`, `staging`, `prod` | ✅ |
| `containerization` | Boolean | ¿Requiere build y push de imagen Docker? | ❌ (default: true) |
| `security_scan` | Boolean | ¿Incluir SonarQube, SAST, dependency check? | ❌ (default: true) |
| `test_framework` | Enum | `xunit`, `nunit`, `pytest`, `playwright` | ❌ |
| `deployment_target` | Enum | `azure-app-service`, `azure-aks`, `azure-container-apps`, `on-prem` | ✅ |

## Flujo de Trabajo (Pasos)
1. **Análisis de requisitos**: Determinar stages obligatorios según tipo de proyecto, plataforma CI y entornos.
2. **Definición de stages base**:
   - **Checkout** — Clonado del repositorio con shallow clone.
   - **Build** — Compilación con configuración Release, versión semántica.
   - **Unit Tests** — Ejecución de tests unitarios con cobertura mínima 80%.
   - **Security Scan** — SonarQube analysis, dependency check (OWASP Dependency-Check), secret scanning.
   - **Quality Gate** — Validación de umbral de calidad SonarQube; fallo si no pasa.
   - **Package** — Generación de artefacto (DLL, ZIP, Docker image).
   - **Push Artifact** — Publicación en registry corporativo (Azure Container Registry, Artifactory).
   - **Deploy** — Despliegue en entorno target con estrategia (rolling, blue-green, canary).
3. **Configuración de entornos**: Definir variables, secrets (referencias a Azure Key Vault), y gates de aprobación para staging/prod.
4. **Generación de pipeline**: Crear archivo de pipeline en formato nativo de la plataforma CI seleccionada.
5. **Validación de estándares**: Verificar que el pipeline cumple estándares corporativos de DevOps (nomenclatura, timeouts, retry policies, notificaciones).
6. **Documentación**: Generar README de pipeline con instrucciones de uso, troubleshooting y diagrama de flujo.
7. **Registro de evidencia**: Metadatos para gobierno y catálogo de pipelines.

## Salida Esperada
### Archivos Generados
```
pipeline/
├── Jenkinsfile / .github/workflows/ci.yml / azure-pipelines.yml
├── pipeline-config.json          # Variables y parámetros
├── docker/
│   └── Dockerfile (si aplica)
└── README-pipeline.md            # Documentación de uso
```

### Estructura del README
```markdown
# Pipeline CI/CD — [Nombre Proyecto]
> Plataforma: [Jenkins/GitHub Actions/Azure DevOps] | Entornos: [dev/staging/prod]

## 1. Diagrama de Flujo
## 2. Stages
| Stage | Descripción | Timeout | Condición de Fallo |
## 3. Variables de Entorno
## 4. Secrets y Key Vault
## 5. Quality Gates
## 6. Estrategia de Despliegue
## 7. Rollback
## 8. Troubleshooting
## 9. Evidencia y Metadatos
```

## Criterios de Calidad
- [ ] Pipeline incluye stages de build, test, security scan, quality gate y deploy.
- [ ] Cobertura de tests unitarios ≥ 80% como condición de fallo.
- [ ] SonarQube quality gate como gate obligatorio antes de deploy.
- [ ] No hay secretos hardcodeados; todos usan referencias a Azure Key Vault.
- [ ] Timeouts definidos en cada stage para evitar builds colgadas.
- [ ] Estrategia de rollback documentada para entornos de producción.
- [ ] Pipeline validada contra estándares corporativos de DevOps.

## Stack y Tecnologías
- CI/CD: Jenkins, GitHub Actions, Azure DevOps Pipelines
- Contenedores: Docker, Azure Container Registry
- Seguridad: SonarQube, OWASP Dependency-Check, GitLeaks / TruffleHog
- Testing: xUnit, NUnit, Playwright, pytest
- Despliegue: Azure App Service, AKS, Azure Container Apps
- IaC: Terraform, ARM templates
- Secrets: Azure Key Vault (referencias, nunca valores)

## Dependencias
- `apb-plat-docker-v1.0` — para dockerización automática
- `apb-dev-sonar-clean-v1.0` — para integración con análisis de calidad
- `apb-qa-test-auto-v1.0` — para automatización de testing en pipeline
- `apb-sec-owasp-v1.0` — para validación de seguridad en pipeline
- `apb-gov-standards-v1.0` — para validación de estándares corporativos

## Ejemplo de Uso
**Prompt de invocación:**
```
Genera un pipeline GitHub Actions para nuestro microservicio de pagos:
- Proyecto: ASP.NET Core 8 Web API
- Repo: https://github.com/apb/payments-service
- Entornos: dev, staging, prod
- Docker: sí, imagen multi-stage
- Tests: xUnit con cobertura mínima 80%
- Security: SonarQube + OWASP Dependency-Check
- Deploy: Azure Container Apps
- Secrets: Azure Key Vault
```

## Notas y Advertencias
- **Nivel 1**: El agente genera el descriptor de pipeline; no ejecuta el pipeline ni tiene acceso a entornos de producción.
- **Revisión humana obligatoria** antes de mergear pipeline a rama principal.
- Los secrets nunca se incluyen en el código de pipeline; se usan variables de entorno o referencias a Key Vault.
- Las pipelines de producción requieren aprobación manual configurada en el stage de deploy.
- El agente no tiene acceso a credenciales ni entornos reales; todas las configuraciones son plantillas parametrizables.

## Historial de Cambios
| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-20 | Arquitectura APB | Creación inicial |


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Primera línea del fichero**: `# [IA-GEN] Generado por APB AI Framework (apb-plat-cicd-v1.0) — revisar ANTES de aplicar en producción`
- **Commit** — prefijo `[ai-gen]` + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`

> ⚠️ Para IaC el marcado es especialmente crítico: ningún fichero generado por IA debe ejecutarse en producción sin revisión humana explícita.
