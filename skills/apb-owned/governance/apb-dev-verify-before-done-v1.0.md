---
id: "apb-dev-verify-before-done-v1.0"
name: "Verify Before Done"
description: "Establece un checklist de verificacion obligatoria antes de marcar cualquier tarea como completada, evitando el 'done' falso que genera deuda tecnica."
version: "1.0.0"
status: "draft"
owner: "Gobierno TI APB <arquitectura@portdebarcelona.cat>"
domain: "governance"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

> Nota: el ID conserva el prefijo histórico `apb-dev-` aunque el dominio funcional es `governance`; ver discovery/SESSION_2_NOTES.md.

> Inspirado en: skills.sh/superpowers-method (verification discipline) (licencia MIT).

# Verify Before Done

## Purpose
Establece un checklist de verificacion obligatoria antes de marcar cualquier tarea como completada, evitando el "done" falso que genera deuda tecnica.

## Trigger
- Antes de cambiar estado de task a "Done/Completada"
- Antes de crear Pull Request
- Antes de entregar a QA/revision

## Input
- Codigo implementado
- Criterios de aceptacion originales
- Contexto de arquitectura y estandares del proyecto

## Output
- Checklist de verificacion completado (si/no)
- Evidencia de verificacion (logs, screenshots, metricas)
- Decision documentada: APROBADO / RECHAZADO con razon

## Procedure

### Phase 1: Verificacion Funcional
- [ ] Criterios de aceptacion: Cada criterio del ticket/PRD esta cubierto
- [ ] Casos limite: Inputs vacios, nulos, extremos, errores
- [ ] Flujo completo: El usuario puede ir de inicio a fin sin bloqueos
- [ ] Regresion: Funcionalidad existente no rota (tests pasan)

### Phase 2: Verificacion Tecnica
- [ ] Tests: Unitarios presentes y pasando (>80% cobertura en cambios)
- [ ] Integracion: Contratos con servicios downstream respetados
- [ ] Estandares: Lint, formato, naming conventions del proyecto
- [ ] Seguridad: No secrets en codigo, validacion de inputs, sanitizacion

### Phase 3: Verificacion de Documentacion
- [ ] Cambios documentados: README, ADR, o comentarios actualizados
- [ ] Contrato API: Swagger/OpenAPI actualizado si aplica
- [ ] Observabilidad: Logs, metricas, traces configurados si aplica

### Phase 4: Verificacion de Entrega
- [ ] PR descripcion: Que, por que, como probar, screenshots si aplica
- [ ] Tamano: PR < 400 lineas de cambio (ideal < 200)
- [ ] Commits: Historia limpia, mensajes descriptivos
- [ ] Pipeline: Build y tests automatizados pasan

## Rules
- Si un checkbox no aplica, marcar como N/A con justificacion
- Si un checkbox falla, la task NO esta done. Punto.
- "Casi listo" no existe. Es done o no done.
- La verificacion debe ser demostrable, no basada en "creo que si"

## Examples

### Example 1: Feature API
Verificacion:
- [x] Criterios: 3/3 cubiertos (crear, listar, filtrar)
- [x] Casos limite: empty list -> 200 [], invalid filter -> 400
- [x] Flujo: Postman collection ejecutada, 5/5 pasan
- [x] Regresion: 42 tests existentes pasan
- [x] Tests: 8 nuevos, 87% cobertura
- [x] Estandares: dotnet format aplicado, 0 warnings
- [x] Seguridad: input validado, no PII en logs
- [x] PR: 180 lineas, descripcion completa
- [x] Pipeline: verde

Decision: APROBADO

### Example 2: Hotfix Urgente
Verificacion:
- [x] Criterios: bug reproducdo y fix verificado
- [ ] Tests: no hay tiempo, test manual realizado
- [x] Regresion: smoke test pasado
- [ ] PR: 450 lineas (incluye refactor accidental)

Decision: RECHAZADO. Razon: refactor no relacionado debe ir en PR separado. Tests manuales documentados como deuda tecnica con ticket #1234.

## Integration
- Precedido por: Cualquier skill de implementacion
- Relacionado con: apb-dev-grill-before-code-v1.0 (criterios de aceptacion)
- Usa: third-obra-superpowers-method-v1.0 (disciplina de verificacion)

## Tags
#verification #done #quality #governance #checklist #pr


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-dev-verify-before-done-v1.0) - pendiente validacion humana. No distribuir sin revision.
