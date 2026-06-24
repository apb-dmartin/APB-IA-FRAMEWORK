---
id: "apb-plat-docker-v1.0"
name: "Dockerización Automática"
description: "Generar archivos Docker (Dockerfile, .dockerignore, docker-compose) optimizados para el stack tecnológico de APB. Incluye multi-stage builds, security hardening, non-root users, health checks y configuración para entornos de desarrollo y producción."
version: "1.0.0"
status: "draft"
owner: "DevOps APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Dockerización Automática

## Propósito
Generar archivos Docker (Dockerfile, .dockerignore, docker-compose) optimizados para el stack tecnológico de APB. Incluye multi-stage builds, security hardening, non-root users, health checks y configuración para entornos de desarrollo y producción.

## Contexto de Uso
- Dockerización de nuevos proyectos .NET, Django o frontend.
- Optimización de imágenes Docker existentes (tamaño, seguridad, layers).
- Generación de configuraciones docker-compose para desarrollo local con dependencias (BD, cache, message broker).
- Preparación de imágenes para despliegue en Azure Container Apps o AKS.

## Entradas Requeridas
| Entrada | Tipo | Descripción | Obligatorio |
|---------|------|-------------|-------------|
| `project_type` | Enum | `dotnet-api`, `dotnet-web`, `devexpress-front`, `django-api`, `django-web` | ✅ |
| `project_path` | Texto | Ruta relativa del proyecto en el repo | ✅ |
| `base_image_preference` | Enum | `microsoft-dotnet`, `python`, `nginx`, `custom` | ❌ (default: oficial) |
| `expose_ports` | Lista | Puertos a exponer | ❌ (default: 80, 443) |
| `dependencies` | Lista | Servicios dependientes: `sql`, `redis`, `service-bus` | ❌ |
| `health_check_endpoint` | Texto | Endpoint de health check (e.g., `/health`) | ❌ (default: `/health`) |

## Flujo de Trabajo (Pasos)
1. **Análisis de proyecto**: Determinar runtime, dependencias y estructura de carpetas.
2. **Selección de base image**: Usar imágenes oficiales minimizadas (distroless, alpine, slim) cuando sea posible.
3. **Diseño de multi-stage build**:
   - **Stage build**: Compilación con SDK completo, restore de dependencias.
   - **Stage publish**: Publicación en modo Release.
   - **Stage runtime**: Imagen final mínima con solo runtime necesario.
4. **Security hardening**:
   - Non-root user (`appuser` con UID > 10000).
   - No ejecución como `root`.
   - `read_only` filesystem donde sea posible.
   - Scan de vulnerabilidades con Trivy o Snyk (recomendación en comments).
5. **Health checks**: Configurar `HEALTHCHECK` con endpoint HTTP o comando.
6. **Optimización de layers**: Ordenar instrucciones para maximizar cache de layers.
7. **Generación de .dockerignore**: Excluir archivos innecesarios (bin, obj, .git, secrets, local settings).
8. **Generación de docker-compose.yml**: Si se solicitan dependencias, generar compose con servicios vinculados.
9. **Documentación**: README con instrucciones de build, run, push y troubleshooting.
10. **Registro de evidencia**: Metadatos para gobierno.

## Salida Esperada
### Archivos Generados
```
docker/
├── Dockerfile
├── .dockerignore
├── docker-compose.yml (si aplica)
└── README-docker.md
```

### Estructura del README
```markdown
# Dockerización — [Nombre Proyecto]
> Base image: [imagen] | Multi-stage: [sí/no] | Usuario: [non-root]

## 1. Estructura de la Imagen
## 2. Instrucciones de Build
## 3. Instrucciones de Run
## 4. Docker Compose (desarrollo)
## 5. Health Checks
## 6. Security Hardening
## 7. Optimizaciones Aplicadas
## 8. Troubleshooting
## 9. Evidencia y Metadatos
```

## Criterios de Calidad
- [ ] Multi-stage build con imagen final mínima (distroless/alpine/slim).
- [ ] Non-root user configurado con UID > 10000.
- [ ] `.dockerignore` excluye bin, obj, .git, archivos de configuración local y secretos.
- [ ] `HEALTHCHECK` configurado en Dockerfile.
- [ ] No se incluyen secretos, credenciales ni connection strings en la imagen.
- [ ] Imagen escaneable por Trivy/Snyk sin vulnerabilidades críticas conocidas.
- [ ] Tamaño de imagen optimizado (layers mínimas, cache eficiente).

## Stack y Tecnologías
- Docker, Docker Compose, BuildKit
- Base images: `mcr.microsoft.com/dotnet/aspnet:8.0-alpine`, `python:3.12-slim`, `nginx:alpine`
- Security: Trivy, Snyk, Docker Bench for Security
- Registry: Azure Container Registry

## Dependencias
- `apb-plat-cicd-v1.0` — para integración en pipeline
- `apb-sec-owasp-v1.0` — para validación de seguridad de dependencias
- `apb-gov-standards-v1.0` — para cumplimiento de estándares de contenedores

## Ejemplo de Uso
**Prompt de invocación:**
```
Dockeriza nuestro microservicio de notificaciones:
- Tipo: ASP.NET Core 8 Web API
- Ruta: src/NotificationsService/
- Dependencias: Azure Service Bus, Azure SQL
- Health check: /health/ready
- Requisitos: non-root, multi-stage, imagen mínima
```

## Notas y Advertencias
- **Nivel 1**: El agente genera archivos Docker; no ejecuta builds ni push a registry.
- **Revisión humana obligatoria** antes de mergear Dockerfile a rama principal.
- Las imágenes base deben mantenerse actualizadas; el agente indica la versión usada.
- Los health checks deben alinearse con los endpoints reales de la aplicación.
- El agente no tiene acceso a credenciales; las connection strings se inyectan vía variables de entorno en runtime.

## Historial de Cambios
| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-20 | Arquitectura APB | Creación inicial |
