---
id: "third-hashicorp-terraform-governance-v1.0"
name: "Terraform Multi-cloud con Gobernanza"
description: "Consolidación de skills oficiales de Terraform (style guide, testing, stacks, refactor de módulos, módulos verificados de Azure) con extensión a gobernanza enterprise y security-first."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
created_date: "2026-06-22"
review_date: "2026-06-22"
autonomy_level: 1
source_repo: "https://github.com/hashicorp/agent-skills"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
---

# SKILL_PLAT_TERRAFORM — Infrastructure as Code with Terraform

## 1. Propósito y Alcance

Esta skill consolida el conocimiento de múltiples skills oficiales de HashiCorp
en un único skill unificado para el framework APB, extendiendo el alcance a:
- **Multi-cloud**: AWS, Azure, GCP (no solo Azure como en AVM)
- **Enterprise governance**: Políticas organizacionales, compliance, cost controls
- **Security-first**: Seguridad integrada en el diseño desde el inicio
- **Observability**: Integración con herramientas de monitoreo y logging

**Casos de uso principales:**
1. Generación de código Terraform HCL siguiendo convenciones oficiales
2. Refactorización de configuraciones monolíticas en módulos reutilizables
3. Implementación de Terraform Stacks para multi-entorno/multi-región
4. Desarrollo de providers personalizados con Plugin Framework
5. Testing de infraestructura con terraform test (.tftest.hcl)
6. Importación de recursos existentes a estado Terraform

## 2. Principios Core de Terraform (APB)

1. **Infrastructure as Code**: Toda la infraestructura debe ser definida, versionada,
   y gestionada como código.
2. **Idempotencia**: Aplicaciones repetidas del mismo código producen el mismo estado.
3. **Inmutabilidad**: Preferir reemplazo sobre modificación in-place cuando sea posible.
4. **Modularidad**: Configuraciones organizadas en módulos reutilizables y composables.
5. **Seguridad por diseño**: Secrets nunca en código; uso de vaults, KMS, y variables sensibles.
6. **Observabilidad**: Todo cambio trazable, auditable, y con impacto conocido.
7. **Cost awareness**: Tags/labels obligatorios para atribución de costos; uso de instancias spot donde aplique.

## 3. Estructura de Proyecto Terraform (Estándar APB)

```
terraform/
├── modules/                    # Módulos reutilizables
│   ├── networking/
│   ├── compute/
│   ├── database/
│   ├── security/
│   └── monitoring/
├── environments/               # Configuraciones por entorno
│   ├── dev/
│   ├── staging/
│   └── prod/
├── stacks/                     # Terraform Stacks (HCP Terraform/Enterprise)
│   ├── stack.hcl
│   └── deployments/
├── policies/                   # Sentinel/OPA policies
│   ├── cost-limits.sentinel
│   ├── security.sentinel
│   └── tagging.sentinel
├── tests/                      # Tests .tftest.hcl
│   ├── networking.tftest.hcl
│   └── compute.tftest.hcl
├── docs/                       # Documentación generada
├── backend.tf                  # Configuración de backend remoto
├── provider.tf                 # Configuración de providers
├── versions.tf                 # Constraints de versiones
└── variables.tf                # Variables globales
```

## 4. Convenciones de Estilo HCL (Consolidado HashiCorp)

### 4.1 Formato y Estilo
- Usar `terraform fmt` obligatoriamente antes de cada commit (pre-commit hook)
- Indentación: 2 espacios (no tabs)
- Líneas máximo 80 caracteres (preferiblemente)
- Nombres de recursos: `snake_case` (ej: `aws_instance`, `azurerm_resource_group`)
- Nombres de variables: descriptivos, en `snake_case`
- Descripciones obligatorias para todas las variables y outputs

### 4.2 Estructura de Archivos
```hcl
# provider.tf
terraform {
  required_version = ">= 1.9.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# variables.tf
variable "environment" {
  description = "Entorno de despliegue (dev, staging, prod)"
  type        = string
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "El entorno debe ser dev, staging o prod."
  }
}

# main.tf
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type

  tags = {
    Name        = "web-server-${var.environment}"
    Environment = var.environment
    CostCenter  = var.cost_center
    ManagedBy   = "terraform"
  }
}
```

### 4.3 Módulos - Best Practices
- **Tamaño**: Módulos enfocados en un propósito único (SRP)
- **Inputs**: Variables con tipos estrictos, validaciones, y defaults sensibles
- **Outputs**: Outputs mínimos necesarios; evitar exponer datos sensibles
- **Versionado**: Módulos versionados con tags semánticos (v1.0.0, v1.1.0)
- **Documentación**: README.md generado con terraform-docs en cada módulo

### 4.4 Estado y Backend
- **Backend remoto obligatorio**: S3 + DynamoDB (AWS), GCS + Cloud SQL (GCP), Azure Storage + CosmosDB (Azure)
- **State locking**: Habilitado siempre para prevenir corrupción concurrente
- **State encryption**: Habilitado en reposo y en tránsito
- **Workspace strategy**: Un workspace por entorno O un backend separado por entorno (preferido para prod)

## 5. Seguridad en Terraform (Security-First)

### 5.1 Gestión de Secrets
- **NUNCA** hardcodear secrets en archivos .tf
- Usar variables sensibles (`sensitive = true`)
- Integrar con HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, GCP Secret Manager
- Usar data sources para leer secrets en runtime

### 5.2 IAM y RBAC
- Principio de mínimo privilegio en roles de ejecución de Terraform
- Service accounts dedicadas por entorno
- OIDC para autenticación CI/CD (no credenciales de larga duración)

### 5.3 Static Analysis
- **tflint**: Linter para Terraform
- **tfsec/trivy**: Escaneo de seguridad de IaC
- **checkov**: Policy-as-code para Terraform
- **terrascan**: Escaneo de compliance

### 5.4 Policy as Code
- **Sentinel** (HCP Terraform/Enterprise): Políticas de costo, seguridad, y tagging
- **OPA/Rego**: Alternativa open-source para policy enforcement

## 6. Testing de Infraestructura

### 6.1 Terraform Test (.tftest.hcl)
```hcl
# tests/compute.tftest.hcl
run "validate_instance_type" {
  command = plan
  assert {
    condition     = aws_instance.web.instance_type == "t3.micro"
    error_message = "El tipo de instancia debe ser t3.micro para dev."
  }
}

run "validate_tags" {
  command = plan
  assert {
    condition     = length(aws_instance.web.tags) >= 4
    error_message = "La instancia debe tener al menos 4 tags (Name, Environment, CostCenter, ManagedBy)."
  }
}
```

### 6.2 Estrategia de Testing
1. **Unit tests**: Tests de módulos individuales con mocks
2. **Integration tests**: Tests de stacks completos en entornos efímeros
3. **Contract tests**: Validación de interfaces entre módulos
4. **Security tests**: Escaneo de vulnerabilidades en la infraestructura planificada

## 7. Terraform Stacks (Multi-entorno/Multi-región)

### 7.1 Conceptos
- **Stack**: Unidad de despliegue que agrupa componentes relacionados
- **Deployment**: Instancia de un stack en un entorno/región específica
- **Component**: Unidad de infraestructura (similar a un módulo root)

### 7.2 Ejemplo de Stack
```hcl
# stack.hcl
stack "platform" {
  description = "Plataforma base APB"

  component "networking" {
    source = "./components/networking"
  }

  component "compute" {
    source = "./components/compute"
    depends_on = [component.networking]
  }
}

# deployments/prod.hcl
deployment "prod_us" {
  stack = stack.platform

  variables = {
    region = "us-east-1"
    environment = "prod"
  }
}

deployment "prod_eu" {
  stack = stack.platform

  variables = {
    region = "eu-west-1"
    environment = "prod"
  }
}
```

## 8. CI/CD para Terraform

### 8.1 Pipeline Estándar
```
1. VALIDATE
   └── terraform fmt -check
   └── tflint
   └── terraform validate
   └── tfsec/trivy scan

2. PLAN
   └── terraform plan -out=plan.tfplan
   └── Infracost (estimación de costos)
   └── Sentinel/OPA policy check
   └── Post PR comment con diff de costos

3. APPLY (manual approval para prod)
   └── terraform apply plan.tfplan
   └── Smoke tests post-deploy
   └── Update documentation

4. DESTROY (para entornos efímeros)
   └── terraform destroy (automático para dev/review apps)
```

### 8.2 GitOps con Atlantis
- Webhook-based Terraform execution
- Plan automático en PR
- Apply con aprobación en PR
- Locks de estado por PR

## 9. Multi-Cloud Patterns

### 9.1 Abstracción de Provider
```hcl
# modules/compute/main.tf (multi-cloud)
locals {
  is_aws   = var.cloud_provider == "aws"
  is_azure = var.cloud_provider == "azure"
  is_gcp   = var.cloud_provider == "gcp"
}

resource "aws_instance" "this" {
  count = local.is_aws ? 1 : 0
  # ... AWS-specific config
}

resource "azurerm_linux_virtual_machine" "this" {
  count = local.is_azure ? 1 : 0
  # ... Azure-specific config
}

resource "google_compute_instance" "this" {
  count = local.is_gcp ? 1 : 0
  # ... GCP-specific config
}
```

### 9.2 Networking Multi-Cloud
- **Interconnect**: Cloud Interconnect (GCP), Direct Connect (AWS), ExpressRoute (Azure)
- **VPN**: Site-to-site VPN entre nubes y on-premise
- **DNS**: Route53 (AWS), Cloud DNS (GCP), Azure DNS - con fallback multi-cloud

## 10. Troubleshooting y Debugging

### 10.1 Problemas Comunes
- **State lock**: `terraform force-unlock` (con precaución)
- **Drift detection**: `terraform plan` muestra diferencias; usar `terraform refresh` con cuidado
- **Resource tainted**: `terraform taint` para forzar recreación
- **Import**: `terraform import` para traer recursos existentes al estado

### 10.2 Debugging
- `TF_LOG=DEBUG terraform plan` para logs detallados
- `terraform state list` para listar recursos en estado
- `terraform state show <resource>` para ver detalle de un recurso

## 11. Workflow de Implementación (APB)

```
1. DISEÑO
   └── Definir arquitectura objetivo con SKILL_ARCH_CLOUD_INFRA
   └── Seleccionar providers y módulos base
   └── Definir estrategia de estado y backend
   └── Establecer convenciones de tagging (costos, seguridad)

2. DESARROLLO
   └── Implementar módulos según convenciones de estilo
   └── Ejecutar tests unitarios (.tftest.hcl)
   └── Ejecutar análisis estático (tflint, tfsec)
   └── Documentar con terraform-docs

3. REVISIÓN
   └── Peer review del código HCL
   └── Validar plan con estimación de costos (Infracost)
   └── Verificar compliance con políticas Sentinel/OPA
   └── Aprobar PR con evidencia de tests pasados

4. DESPLIEGUE
   └── Ejecutar plan en staging
   └── Validar smoke tests
   └── Aplicar en producción con aprobación manual
   └── Verificar drift post-deploy

5. OPERACIÓN
   └── Monitorear costos con SKILL_PLAT_FINOPS
   └── Gestionar estado y locks
   └── Planificar upgrades de providers/versiones
   └── Documentar runbooks de operación
```

## 12. Integración con otras Skills APB

- **SKILL_PLAT_FINOPS**: Tags obligatorios para costos; estimación en CI/CD
- **SKILL_ARCH_CLOUD_INFRA**: Diseño de arquitectura que se implementa en Terraform
- **SKILL_OPS_OBSERVABILITY**: Integración de métricas/logs en infraestructura desplegada
- **SKILL_GOV_COMPLIANCE**: Políticas Sentinel/OPA para compliance
- **SKILL_DEV_CODE_BASE**: Módulos de infraestructura como código base

## 13. Anti-patrones Terraform (Qué NO hacer)

- **Monolitos**: Configuraciones root monolíticas sin modularización
- **Hardcoded values**: Valores hardcodeados en lugar de variables
- **Secrets en repo**: Credenciales, passwords, o tokens en archivos .tf
- **State local**: Uso de estado local en equipos de desarrollo
- **Manual changes**: Modificaciones manuales en consola sin importar al estado
- **Provider version unconstrained**: No fijar versiones de providers
- **Ignoring drift**: No ejecutar plan regularmente para detectar drift
- **Over-permissioned**: Roles de ejecución con permisos excesivos

## 14. Referencias

- [HashiCorp Terraform Best Practices](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/terraform-best-practices)
- [Terraform Style Guide](https://developer.hashicorp.com/terraform/language/style)
- [Terraform Testing Framework](https://developer.hashicorp.com/terraform/language/tests)
- [Terraform Stacks](https://developer.hashicorp.com/terraform/language/stacks)
- [Terraform Plugin Framework](https://developer.hashicorp.com/terraform/plugin/framework)
- [TerraShark Skill (Community)](https://github.com/LukasNiessen/terrashark)
- [TFLint](https://github.com/terraform-linters/tflint)
- [Tfsec](https://github.com/aquasecurity/tfsec)
- [Infracost](https://www.infracost.io/)
