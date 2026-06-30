---
id: "third-lum1104-knowledge-graph-v1.0"
name: "Knowledge Graph Builder (Lum1104/Understand-Anything)"
description: "Skill third-party para construir grafos de conocimiento a partir de documentos no estructurados. Basada en el repo Lum1104/Understand-Anything."
version: "1.0.0"
status: "watchlist"
block_reason: "Licencia no verificada — el repo Lum1104/Understand-Anything no tiene archivo LICENSE confirmado. No usar en producción hasta verificación manual directa."
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "governance"
autonomy_level: 1
source: "https://github.com/Lum1104/Understand-Anything"
source_commit: "unverified"
verified_date: "2026-06-30"
license: "UNVERIFIED"
created_date: "2026-06-30"
review_date: "2026-06-30"
---

# Knowledge Graph Builder (Lum1104/Understand-Anything)

> ⚠️ Borrador generado por IA (APB AI Framework - stub BUG-08) — pendiente validación humana. No distribuir sin revisión.

> ⛔ **BLOQUEADO** — Licencia de la fuente original no verificada. Ver `block_reason` en frontmatter.

---

## 🎯 Propósito

Skill third-party para construir grafos de conocimiento a partir de documentos no estructurados, basada en el repositorio externo `Lum1104/Understand-Anything`.

**Estado:** Bloqueada hasta que el equipo de Arquitectura APB confirme que la licencia del repo fuente permite el uso corporativo.

## 🔒 Bloqueo de licencia

| Campo | Valor |
|-------|-------|
| Repo fuente | `https://github.com/Lum1104/Understand-Anything` |
| Fork evaluado | `Egonex-AI/Understand-Anything` |
| Archivo LICENSE | ⚠️ No encontrado / no confirmado |
| Decisión | Pendiente de revisión manual por Arquitectura APB |

## ✅ Acción requerida para desbloqueo

1. Acceder al repo fuente y verificar la existencia y tipo de licencia.
2. Validar que la licencia permite uso corporativo interno (APB).
3. Actualizar este archivo: cambiar `status: blocked` → `status: draft`, añadir `license: <tipo>` y `source_commit: <hash>`.
4. Ejecutar `validate_repo.py --strict` para confirmar que el componente pasa validación.

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado usando esta skill debe incluir marca de origen IA:

- **Documentos Markdown**: `> ⚠️ Borrador generado por IA (APB AI Framework - third-lum1104-knowledge-graph-v1.0) — pendiente validación humana.`
- **Código**: `// [IA-GEN] Generado por APB AI Framework (third-lum1104-knowledge-graph-v1.0) — pendiente revisión humana`
- **Commits**: prefijo `[ai-gen]` + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`
