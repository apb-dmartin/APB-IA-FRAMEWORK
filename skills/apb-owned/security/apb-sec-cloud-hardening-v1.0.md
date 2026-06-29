---
id: "apb-sec-cloud-hardening-v1.0"
name: "Cloud Hardening"
description: "Aplica controles de endurecimiento (hardening) a recursos cloud siguiendo el CIS Benchmark y mejores prácticas del proveedor, con foco en Azure (adaptable a AWS/GCP)."
version: "1.0.0"
status: "draft"
owner: "Ciberseguridad APB <arquitectura@portdebarcelona.cat>"
domain: "security"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Cloud Hardening

## Purpose
Aplica controles de endurecimiento (hardening) a recursos cloud siguiendo el CIS Benchmark y mejores practicas del proveedor, con foco en Azure (adaptable a AWS/GCP).

## Trigger
- Despliegue de nuevo recurso cloud
- Auditoria de seguridad trimestral
- Post-incidente: endurecimiento preventivo
- Migracion de recursos on-prem a cloud

## Input
- Inventario de recursos cloud (Azure Resource Graph)
- Configuracion actual (ARM templates, Terraform state)
- Requisitos de compliance (ENS, ISO27001, SOC2)

## Output
- Reporte de hardening con scoring por recurso
- Lista de controles aplicados / pendientes
- Scripts/Terraform para remediacion automatizada
- Evidencia de compliance

## Procedure

### Phase 1: Inventario y Clasificacion
1. Identificar recursos: VMs, Storage, Databases, Networking, Identity
2. Clasificar criticidad: Tier 1 (critico), Tier 2 (sensible), Tier 3 (general)
3. Mapear a compliance: Que controles aplica a cada recurso

### Phase 2: Evaluacion de Controles (CIS Azure)
Por categoria:

Identity & Access:
- MFA habilitado para todos los usuarios administrativos
- PIM para roles privilegiados
- Password policies + bloqueo de cuentas

Storage:
- Encryption at rest (CMK vs platform-managed)
- Network access: Private endpoints, firewall rules
- Soft delete, versioning, immutability

Compute:
- Disk encryption (Azure Disk Encryption / Confidential computing)
- JIT access, NSGs, Azure Firewall
- Defender for Cloud activado

Networking:
- Segmentation (VNets, subnets)
- DDoS Protection Standard
- Application Gateway WAF

Data:
- SQL: TDE, auditing, private link
- Cosmos DB: IP firewall, managed identity
- Key Vault: RBAC, soft delete, purge protection

### Phase 3: Remediacion
- Priorizar por riesgo (critico -> alto -> medio)
- Automatizar donde sea posible (Azure Policy, Terraform)
- Documentar excepciones con justificacion de riesgo aceptado

### Phase 4: Validacion y Monitoreo
- Re-ejecutar evaluacion post-remediacion
- Configurar alertas para drift de configuracion
- Programar re-evaluacion trimestral

## Rules
- Nunca dejar storage publico sin justificacion documentada
- Siempre usar managed identities en lugar de secrets
- Cada excepcion debe tener: riesgo aceptado, fecha de revision, owner
- Defender for Cloud Secure Score debe ser >80%

## Examples

### Example 1: Storage Account Hardening
Recurso: stgappprod001 (Tier 1)

Evaluacion:
- [x] Encryption at rest: AES-256, CMK en AKV
- [x] Network: Private endpoint, no public access
- [x] Soft delete: 7 dias habilitado
- [ ] Immutability: NO (riesgo: ransomware)
- [x] Firewall: IPs de VNet permitidas unicamente

Score: 4/5 (80%)
Accion: Habilitar immutability con retencion 30 dias
Script: Set-AzStorageBlobImmutabilityPolicy

### Example 2: VM Hardening
Recurso: vm-web-prod-01 (Tier 2)

Evaluacion:
- [x] Disk encryption: ADE con KEK en AKV
- [x] JIT access: habilitado, 3h maximo
- [ ] NSG: Puerto 3389 abierto a Internet
- [x] Defender: Endpoint protection activo
- [x] Updates: Automatic OS updates

Score: 3/5 (60%)
Accion: Cerrar 3389, usar Bastion + JIT
Script: Update-AzNetworkSecurityGroupRule

## Integration
- Usa: third-mukul-cybersecurity-arsenal-v1.0 (wrapper con stack Azure)
- Relacionado con: apb-sec-mitre-mapping-v1.0 (priorizacion de amenazas)
- Genera input para: Auditorias ENS, informes de compliance

## Tags
#cloud #hardening #security #azure #cis #compliance #ens


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-sec-cloud-hardening-v1.0) - pendiente validacion humana. No distribuir sin revision.
