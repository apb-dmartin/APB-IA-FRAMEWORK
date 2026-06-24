---
id: "wrap-thedotmack-mem-v1.0"
name: "wrap-thedotmack-mem-v1.0"
description: "Adapta el sistema de memoria persistente de thedotmack para cumplir con requisitos de cifrado, Azure Key Vault (AKV) y auditoria del framework APB."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
wraps: "thedotmack/claude-mem"
source_repo: "https://github.com/thedotmack/claude-mem"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# wrap-thedotmack-mem-v1.0

## Purpose
Adapta el sistema de memoria persistente de thedotmack para cumplir con requisitos de cifrado, Azure Key Vault (AKV) y auditoria del framework APB.

## Encryption
- Algorithm: AES-256-GCM
- Key Management: Azure Key Vault (software HSM)
- Key Rotation: Automatica cada 90 dias
- Data Classification: Cifrado por nivel (Public/Internal/Confidential/Restricted)

## Azure Key Vault Integration
- Vault: apb-mem-kv-[env]
- SKU: Standard
- Purge Protection: Habilitado
- Soft Delete: 90 dias
- Access Policy: RBAC (no legacy access policies)

## Audit Requirements
- Log destination: Azure Log Analytics workspace
- Retention: 1 ano (compliance ENS)
- Events logged: Read, Write, Delete, Key rotation
- Alerting: Failed access attempts -> Azure Monitor Alert

## Memory Schema
```json
{
  "memory_id": "uuid",
  "session_id": "uuid",
  "agent_id": "string",
  "content": "encrypted_string",
  "classification": "Public|Internal|Confidential|Restricted",
  "timestamp": "ISO8601",
  "ttl": "days|null",
  "tags": ["string"]
}
```

## Usage
```
Agent: cualquier agente APB
  -> Wrapper: wrap-thedotmack-mem-v1.0
    -> Source: third-thedotmack-memory-persistence-v1.0
```

## Tags
#wrapper #memory #persistence #encryption #akv #audit #security
