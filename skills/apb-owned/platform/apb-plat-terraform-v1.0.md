---
id: "apb-plat-terraform-v1.0"
name: "Generación de Infraestructura Terraform"
description: "Generar código Terraform (HCL) para provisionar infraestructura en Azure siguiendo las mejores prácticas de Infrastructure as Code (IaC). Incluye módulos reutilizables, variables parametrizables, remote state, y validación de compliance con políticas corporativas."
version: "1.0.0"
status: "draft"
owner: "DevOps APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Generación de Infraestructura Terraform

## Propósito
Generar código Terraform (HCL) para provisionar infraestructura en Azure siguiendo las mejores prácticas de Infrastructure as Code (IaC). Incluye módulos reutilizables, variables parametrizables, remote state, y validación de compliance con políticas corporativas.

## Contexto de Uso
- Provisión de infraestructura para nuevos proyectos o entornos.
- Standardización de recursos Azure mediante módulos Terraform corporativos.
- Migración de infraestructura manual a IaC.
- Integración con pipelines CI/CD para despliegue automatizado de infraestructura.

## Entradas Requeridas
| Entrada | Tipo | Descripción | Obligatorio |
|---------|------|-------------|-------------|
| `architecture_diagram` | Texto / Diagrama | Diagrama o descripción de la infraestructura deseada | ✅ |
| `azure_services` | Lista | Servicios Azure a desplegar: `app-service`, `sql-database`, `aks`, `service-bus`, etc. | ✅ |
| `environments` | Lista | Entornos: `dev`, `staging`, `prod` | ✅ |
| `compliance_requirements` | Lista | ENS, ISO 27001, GDPR — afecta configuración de cifrado, networking, logging | ❌ |
| `existing_modules` | Lista | Módulos Terraform corporativos existentes a reutilizar | ❌ |

## Flujo de Trabajo (Pasos)
1. **Análisis de requisitos**: Determinar servicios, dependencias y requisitos de compliance.
2. **Diseño de estructura de módulos**:
   - Módulo de networking (VNet, subnets, NSG, peering).
   - Módulo de compute (App Service, AKS, VM scale sets).
   - Módulo de datos (SQL Database, PostgreSQL, Storage Account, Redis).
   - Módulo de integración (Service Bus, Event Grid, API Management).
   - Módulo de seguridad (Key Vault, Managed Identity, Private Endpoints).
   - Módulo de observabilidad (App Insights, Log Analytics, Alerts).
3. **Generación de código Terraform**:
   - `main.tf` — Recursos principales.
   - `variables.tf` — Variables parametrizables por entorno.
   - `outputs.tf` — Outputs para integración con otros módulos.
   - `backend.tf` — Configuración de remote state (Azure Storage Account con locking).
   - `providers.tf` — Version pinning de providers.
   - `terraform.tfvars` — Valores por entorno.
4. **Security hardening**:
   - Private Endpoints para servicios PaaS.
   - Managed Identities (no connection strings en variables).
   - Cifrado en reposo y en tránsito por defecto.
   - NSG rules mínimas (principio de mínimo privilegio).
5. **Validación de compliance**: Verificar configuraciones contra requisitos ENS/ISO (logging, backup, cifrado).
6. **Documentación**: README con diagrama de arquitectura, instrucciones de despliegue y variables.
7. **Registro de evidencia**: Metadatos para gobierno y catálogo de infraestructura.

## Salida Esperada
### Archivos Generados
```
terraform/
├── main.tf
├── variables.tf
├── outputs.tf
├── backend.tf
├── providers.tf
├── terraform.tfvars
├── modules/
│   ├── networking/
│   ├── compute/
│   ├── data/
│   ├── integration/
│   ├── security/
│   └── observability/
└── README-terraform.md
```

### Estructura del README
```markdown
# Infraestructura Terraform — [Nombre Proyecto]
> Entornos: [dev/staging/prod] | Azure Region: [westeurope/northeurope]

## 1. Diagrama de Arquitectura
## 2. Módulos
## 3. Variables
## 4. Backend y State
## 5. Instrucciones de Despliegue
## 6. Security Hardening
## 7. Compliance
## 8. Troubleshooting
## 9. Evidencia y Metadatos
```

## Criterios de Calidad
- [ ] Código Terraform validado con `terraform validate` y `terraform plan` (conceptualmente).
- [ ] Remote state configurado en Azure Storage Account con blob locking.
- [ ] No hay secrets ni connection strings en el código; se usan Managed Identities o Key Vault references.
- [ ] Módulos reutilizables con interfaces claras (variables/outputs documentadas).
- [ ] Version pinning en providers y módulos para reproducibilidad.
- [ ] Configuración de compliance (cifrado, logging, backup) validada contra requisitos.
- [ ] Documentación suficiente para que un ingeniero de plataforma despliegue sin intervención del agente.

## Stack y Tecnologías
- Terraform 1.5+, HCL
- Azure Provider for Terraform
- Módulos: Azure Verified Modules (AVM) como referencia
- Backend: Azure Storage Account (state) + Azure Key Vault (secrets)
- Validación: `terraform validate`, `tflint`, `checkov` / `tfsec` para security scanning
- Formatos: HCL, Markdown

## Dependencias
- `apb-arch-cloud-infra-v1.0` — para diseño de arquitectura cloud
- `apb-plat-cicd-v1.0` — para integración en pipeline de despliegue
- `apb-sec-ens-v1.0` — para validación de requisitos de seguridad
- `apb-gov-standards-v1.0` — para cumplimiento de estándares de IaC

## Ejemplo de Uso
**Prompt de invocación:**
```
Genera la infraestructura Terraform para nuestro nuevo microservicio de facturación:
- Servicios: Azure Container Apps, Azure SQL Database, Azure Service Bus, Azure Key Vault
- Entornos: dev, staging, prod
- Networking: VNet con subnets separadas, Private Endpoints para SQL y Service Bus
- Seguridad: Managed Identities, cifrado TDE, NSG mínimas
- Observabilidad: Application Insights, Log Analytics Workspace
- Compliance: ENS Media
```

## Notas y Advertencias
- **Nivel 1**: El agente genera código HCL; no ejecuta `terraform apply` ni tiene acceso a suscripciones de Azure.
- **Revisión humana obligatoria** con `terraform plan` antes de cualquier despliegue.
- El remote state debe configurarse previamente (Storage Account y container existentes).
- Los módulos generados deben alinearse con el catálogo de módulos corporativos existentes.
- El agente no tiene acceso a credenciales de Azure; el código usa variables y Managed Identities.

## Historial de Cambios
| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-20 | Arquitectura APB | Creación inicial |


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Primera línea del fichero**: `# [IA-GEN] Generado por APB AI Framework (apb-plat-terraform-v1.0) — revisar ANTES de aplicar en producción`
- **Commit** — prefijo `[ai-gen]` + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`

> ⚠️ Para IaC el marcado es especialmente crítico: ningún fichero generado por IA debe ejecutarse en producción sin revisión humana explícita.
