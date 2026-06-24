---
id: "wrap-hkuds-lightrag-v1.0"
name: "wrap-hkuds-lightrag-v1.0"
description: "Adapta LightRAG para integracion con Azure AI Search, anadiendo RBAC, clasificacion de datos y cumplimiento con politicas de seguridad APB."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
wraps: "hkuds/LightRAG"
source_repo: "https://github.com/hkuds/LightRAG"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# wrap-hkuds-lightrag-v1.0

## Purpose
Adapta LightRAG para integracion con Azure AI Search, anadiendo RBAC, clasificacion de datos y cumplimiento con politicas de seguridad APB.

## Azure AI Search Integration
- Index: apb-knowledge-graph-[env]
- Tier: Standard S2 (minimo para graph RAG)
- Semantic Search: Habilitado
- Vector Search: Habilitado (Azure OpenAI embeddings)

## RBAC Configuration
- Reader: Agentes de consulta (solo lectura)
- Contributor: Agentes de ingestion (CRUD en indices)
- Owner: Admin framework (full control)
- Excluded: Guest users, external identities

## Data Classification
- Public: Documentacion general, guias
- Internal: Arquitecturas, decisiones tecnicas
- Confidential: Credenciales, tokens, datos PII
- Restricted: Informacion de seguridad, incidentes

## Security Controls
- [ ] Encryption at rest: CMK en AKV
- [ ] Encryption in transit: TLS 1.3
- [ ] Private endpoint: VNet integration
- [ ] Diagnostic logs: 90 dias retencion
- [ ] Backup: Geo-redundante

## Usage
```
Skill: apb-dev-impact-analysis-v1.0
  -> Wrapper: wrap-hkuds-lightrag-v1.0
    -> Source: third-lightrag-knowledge-v1.0
```

## Tags
#wrapper #knowledge-graph #lightrag #azure-ai-search #rbac #security
