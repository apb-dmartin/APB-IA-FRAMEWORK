---
id: "third-lightrag-knowledge-v1.0"
name: "Skill: Knowledge RAG (LightRAG)"
description: "Sistema de Retrieval-Augmented Generation (RAG) ligero para consulta de conocimiento corporativo con grafos de conocimiento y recuperación híbrida."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
source_repo: "https://github.com/hkuds/lightrag"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Skill: Knowledge RAG (LightRAG)

---

## Descripción
Sistema de Retrieval-Augmented Generation (RAG) ligero para consulta de conocimiento corporativo con grafos de conocimiento y recuperación híbrida.

## Capacidades
- Indexación de documentos corporativos
- Recuperación híbrida (vectorial + keyword)
- Grafos de conocimiento para relaciones complejas
- Respuestas fundamentadas con citas

## Inputs
- `query`: consulta del usuario
- `knowledge_base`: base de conocimiento indexada
- `filters`: filtros de dominio/tiempo (opcional)

## Outputs
- `response`: respuesta fundamentada
- `sources`: fuentes consultadas
- `confidence_score`: puntuación de confianza

## Restricciones
- Requiere infraestructura de indexación
- Datos sensibles deben anonimizarse
- No almacena conversaciones en índice

## Adaptaciones APB
- Integración con `prov-apb-knowledge-v1.0`
- Conexión a estándares y políticas APB
- Workflow `apb-wf-legacy-onboarding-v1.0`

## Ejemplo de Uso
```
Invocar: third-lightrag-knowledge-v1.0
Input: { query: "¿Cuál es el estándar de API para microservicios?", kb: "apb-standards" }
Output: Respuesta con referencia a estándar APB y citas
```

---
*Adaptado por APB AI Framework. Licencia MIT original respetada.*
