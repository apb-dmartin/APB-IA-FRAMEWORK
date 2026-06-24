---
id: "wrap-mukul-cyber-v1.0"
name: "wrap-mukul-cyber-v1.0"
description: "Adapta el skill de ciberseguridad de mukul975 al stack tecnologico APB (Azure, .NET, Service Bus, CloudEvents), filtrando controles relevantes y anadiendo validacion ENS (Esquema Nacional de Seguridad)."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
wraps: "mukul975/cybersecurity-arsenal"
source_repo: "https://github.com/mukul975/cybersecurity-arsenal"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# wrap-mukul-cyber-v1.0

## Purpose
Adapta el skill de ciberseguridad de mukul975 al stack tecnologico APB (Azure, .NET, Service Bus, CloudEvents), filtrando controles relevantes y anadiendo validacion ENS (Esquema Nacional de Seguridad).

## Filter Rules
- Solo incluir tecnicas aplicables a Azure / cloud-native
- Excluir controles especificos de AWS/GCP a menos que sean transversales
- Anadir mapeo ENS para cada control
- Validar que las tecnicas sean compatibles con CloudEvents (no Avro/Protobuf)

## Mappings

### Azure-Specific Controls
| Control | Source Skill | ENS Mapping | APB Adaptation |
|---------|------------|-------------|----------------|
| MFA | mukul-cyber | CCN-STIC-619 | Azure AD PIM + Conditional Access |
| Encryption | mukul-cyber | CCN-STIC-610 | Azure Key Vault CMK |
| Network Segmentation | mukul-cyber | CCN-STIC-630 | NSG + Azure Firewall |
| Logging | mukul-cyber | CCN-STIC-640 | Azure Monitor + Log Analytics |

### Stack APB Validation
- [ ] Compatible con Azure Service Bus (no requiere Kafka/RabbitMQ)
- [ ] Compatible con JSON/CloudEvents (no Avro/Protobuf)
- [ ] Compatible con DevExpress JS (no React/TS dependencias)
- [ ] Documentado en espanol para equipo APB

## Usage
```
Skill: apb-sec-mitre-mapping-v1.0
  -> Wrapper: wrap-mukul-cyber-v1.0
    -> Source: third-mukul-cybersecurity-arsenal-v1.0
```

## Tags
#wrapper #security #mukul975 #azure #ens #compliance
