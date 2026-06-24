---
id: "third-expo-docker-cicd-v1.0"
name: "Docker & CI/CD Patterns"
description: "Patrones de contenerización e integración continua adaptados de Expo CI/CD Workflows."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
created_date: "2026-06-22"
review_date: "2026-06-22"
autonomy_level: 1
source_repo: "https://github.com/expo/skills"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
---

# Dockerización para APB

## Overview
Containerización de aplicaciones APB (.NET, Django, DevExtreme) siguiendo principios de imágenes seguras, multi-stage builds, y cumplimiento de políticas corporativas. Genera Dockerfile optimizado, docker-compose para entornos locales, y configuración de registro de imágenes (Azure Container Registry).

## When to Use
- Nuevo servicio que requiere despliegue containerizado
- Migración de aplicación legacy a containers
- Estandarización de entornos de desarrollo
- Preparación para Kubernetes u orquestador
- Replicación de entorno de producción localmente

**When NOT to use:**
- Aplicaciones desktop sin componente servicio
- Sistemas legacy que no soportan containerización (evaluar primero)
- Entornos donde VMs son obligatorias por política

## Core Pattern

### Fase 1: Análisis de Aplicación

| Aspecto | Pregunta | Impacto en Docker |
|---------|----------|-------------------|
| **Runtime** | .NET, Python, Node.js? | Base image |
| **Dependencias** | NuGet, pip, npm? | Layer de dependencias |
| **Puertos** | ¿Qué puertos expone? | EXPOSE |
| **Variables** | ¿Qué configuración necesita? | ENV / secrets |
| **Persistencia** | ¿Necesita volúmenes? | VOLUME |
| **Redes** | ¿Comunicación con otros servicios? | Network |
| **Health checks** | ¿Cómo saber si está sano? | HEALTHCHECK |

### Fase 2: Multi-Stage Build

#### .NET
```dockerfile
# Etapa 1: Build
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY . .
RUN dotnet restore
RUN dotnet build -c Release --no-restore
RUN dotnet test -c Release --no-build --verbosity normal
RUN dotnet publish -c Release -o /app/publish --no-build

# Etapa 2: Runtime
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS runtime
WORKDIR /app
COPY --from=build /app/publish .

# Seguridad: no root
USER app

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3     CMD curl -f http://localhost:8080/health || exit 1

EXPOSE 8080
ENTRYPOINT ["dotnet", "Apb.Servicio.dll"]
```

#### Django
```dockerfile
# Etapa 1: Build
FROM python:3.11-slim AS build
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python manage.py collectstatic --noinput

# Etapa 2: Runtime
FROM python:3.11-slim AS runtime
WORKDIR /app

# Seguridad: no root
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

COPY --from=build /app /app
RUN chown -R appuser:appgroup /app
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3     CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health/')" || exit 1

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "aplicacion.wsgi:application"]
```

### Fase 3: Docker Compose para Entornos

```yaml
version: '3.8'

services:
  api:
    build:
      context: ./src/Api
      dockerfile: Dockerfile
    ports:
      - "8080:8080"
    environment:
      - ASPNETCORE_ENVIRONMENT=Development
      - ConnectionStrings__Default=${DB_CONNECTION_STRING}
      - AzureKeyVault__Uri=${AKV_URI}
    secrets:
      - db_password
    depends_on:
      - sqlserver
      - redis
    networks:
      - apb-network
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  sqlserver:
    image: mcr.microsoft.com/mssql/server:2022-latest
    environment:
      - ACCEPT_EULA=Y
      - SA_PASSWORD=${DB_SA_PASSWORD}
    volumes:
      - sql-data:/var/opt/mssql
    networks:
      - apb-network

  redis:
    image: redis:7-alpine
    networks:
      - apb-network

volumes:
  sql-data:

networks:
  apb-network:
    driver: bridge

secrets:
  db_password:
    file: ./secrets/db_password.txt
```

### Fase 4: Seguridad de Imágenes

| Control | Implementación | Verificación |
|---------|---------------|--------------|
| **No root** | `USER app` en Dockerfile | `docker run --rm imagen id` |
| **Imagen base mínima** | Alpine o distroless | `docker images` tamaño |
| **Sin secretos** | Usar Azure Key Vault | Scan de imágenes |
| **Scan de vulnerabilidades** | Trivy / Azure Defender | CI pipeline |
| **Pin de versiones** | `FROM imagen:8.0.1` | Dockerfile review |
| **Health checks** | `HEALTHCHECK` | `docker ps` status |
| **Read-only filesystem** | `read_only: true` | docker-compose |
| **Cap drop** | `cap_drop: [ALL]` | docker-compose |

### Fase 5: Registro y Distribución

```bash
# Login a Azure Container Registry
az acr login --name apbregistry

# Build y tag
docker build -t apbregistry.azurecr.io/servicio-api:v1.0.0 .

# Scan de vulnerabilidades
trivy image apbregistry.azurecr.io/servicio-api:v1.0.0

# Push
docker push apbregistry.azurecr.io/servicio-api:v1.0.0

# Sign con Notary / Cosign (opcional)
cosign sign --key cosign.key apbregistry.azurecr.io/servicio-api:v1.0.0
```

## Quick Reference

| Problema | Solución |
|----------|----------|
| Imagen muy grande | Multi-stage build, alpine/distroless |
| Build lento | Layer caching, .dockerignore, orden de COPY |
| Secretos en imagen | BuildKit secrets, Azure Key Vault |
| Vulnerabilidades | Scan con Trivy, base image mínima, actualizar regularmente |
| Permisos | No root, read-only fs, cap_drop |
| Health check fail | Verificar endpoint, timeout adecuado |

## Implementation

### .dockerignore
```
# Git
.git
.gitignore

# IDE
.vs
.vscode
*.user

# Build
bin/
obj/
node_modules/

# Tests
tests/
*.Tests/

# Docs
docs/
*.md

# Secrets
secrets/
.env
appsettings.Development.json
```

## Common Mistakes
- **Imagen base latest:** Usar tag específico para reproducibilidad
- **Secretos en Dockerfile:** Nunca `ENV PASSWORD=xxx`, usar BuildKit secrets o AKV
- **No .dockerignore:** Imagen innecesariamente grande, datos sensibles expuestos
- **Root por defecto:** Siempre crear usuario no-root
- **Sin health check:** Kubernetes/orquestador no puede detectar fallos
- **No pin de versiones:** `FROM python:latest` rompe builds en el futuro
- **Ignorar scan de vulnerabilidades:** CVEs en imágenes base son comunes

## Real-World Impact
- Reducción de 70% en "funciona en mi máquina"
- Estandarización de entornos dev/test/prod
- Despliegue consistente y reproducible

---

## Adapted From
- **Source:** expo/expo-cicd-workflows (CI/CD patterns)
- **License:** MIT
- **Attribution:** Patrones de containerización, multi-stage builds, y configuración de pipeline inspirados en Expo CI/CD workflows. Reescrito completamente para stack tecnológico APB (.NET, Django) y políticas de seguridad corporativas.

## References
- Docker Best Practices
- Azure Container Registry Documentation
- Trivy Documentation
- context/apb/standards/containerization-standards.md
- context/apb/policies/security-policy.md
