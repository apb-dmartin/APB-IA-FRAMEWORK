---
id: "apb-dev-surgical-changes-v1.0"
name: "Surgical Changes"
description: "Limita cada cambio a tocar exclusivamente lo que el cambio requiere, prohibiendo 'mejoras' no solicitadas de codigo adyacente. Distingue huerfanos generados por el propio cambio (limpiar) de deuda tecnica preexistente (no tocar sin pedirlo)."
version: "1.0.0"
status: "draft"
owner: "Desarrollo APB <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 1
created_date: "2026-06-24"
review_date: "2026-06-24"
---

> Inspirado en: multica-ai/andrej-karpathy-skills (principio "Surgical Changes", licencia MIT).
> Origen: 4 principios operacionales para agentes de codificacion derivados de observaciones
> publicas de Andrej Karpathy sobre fallos tipicos de LLMs al programar. Ver Principio
> Fundamental #11 de README.md.

# Surgical Changes

## Purpose
Limita cada cambio al alcance exacto que el requerimiento pide. Prohibe que un agente o
desarrollador aproveche un PR para "mejorar" estilo, renombrar variables, refactorizar
codigo adyacente, o actualizar dependencias no relacionadas — incluso si esas mejoras son
objetivamente buenas. Cada mejora no solicitada es un PR mas dificil de revisar, un riesgo de
regresion no relacionado con el objetivo, y trabajo que nadie pidio ni priorizo.

## Trigger
- Durante cualquier implementacion, especialmente en codigo legacy
- Cuando el diff de un PR incluye archivos no directamente relacionados con el ticket
- Cuando aparece la tentacion de "ya que estoy aqui, arreglo tambien..."
- Code review: cualquier cambio fuera del alcance declarado del PR

## Input
- Alcance declarado del cambio (ticket, criterios de aceptacion)
- Diff propuesto o real
- Codigo adyacente al area modificada

## Output
- Diff acotado exclusivamente al alcance declarado
- Lista de "tentaciones de mejora" identificadas y diferidas (con ticket nuevo si aplica)
- Lista de huerfanos genuinos del propio cambio, eliminados

## Procedure

### Phase 1: Delimitacion de Alcance
1. ¿Que archivos/funciones requiere tocar el ticket, estrictamente?
2. Cualquier archivo fuera de esa lista necesita justificacion explicita, no "estaba cerca".

### Phase 2: Clasificacion de Hallazgos Colaterales
Durante la implementacion, todo lo que se descubre se clasifica en dos categorias, nunca se
arregla sobre la marcha sin clasificar primero:
3. **Huerfano del propio cambio**: codigo que el cambio actual deja sin uso (ej. una funcion
   que ya no se llama tras refactorizar la que la usaba). Se elimina, es parte del cambio.
4. **Deuda tecnica preexistente**: cualquier cosa que ya estaba mal/desactualizada/fea antes
   de este cambio y seguiria igual si el cambio actual no se hiciera. No se toca aqui.

### Phase 3: Registro de Deuda Detectada
5. Toda deuda preexistente detectada (categoria 4) se documenta como hallazgo (ticket Jira o
   nota dirigida a la futura capacidad de analisis de deuda tecnica cuando exista, ver punto
   #25 del plan de fases) — nunca
   se descarta silenciosamente, pero tampoco se arregla sin que alguien lo priorice.

### Phase 4: Verificacion de Acotamiento
6. El diff final: ¿cada linea modificada es necesaria para el objetivo del ticket?
7. Si la respuesta a la 6 es "no" para alguna linea, revertir esa linea especifica.

## Rules
- Ningun PR mezcla "fix del bug X" con "renombre de variables en archivo Y" sin relacion.
- Actualizar una dependencia no relacionada con el ticket nunca va en el mismo PR.
- Si el codigo adyacente esta mal pero no bloquea el cambio actual, se documenta, no se toca.
- Excepcion explicita: si tocar el codigo adyacente es estrictamente necesario para que el
  cambio compile o pase tests (no por estetica), se permite y se justifica en la descripcion
  del PR.
- "Mientras estaba ahi" no es una justificacion valida para ampliar el alcance.

## Examples

### Example 1: Huerfano genuino vs deuda preexistente
Ticket: "Cambiar el calculo de IVA en `OrderService` para soporte multi-pais".
Durante la implementacion se descubre:
- `CalculateLegacyVat()` deja de llamarse tras el cambio → **huerfano del propio cambio**,
  se elimina, es parte natural del PR.
- `OrderRepository` usa una query N+1 sin relacion con el IVA → **deuda preexistente**, se
  documenta como hallazgo, no se toca en este PR.

### Example 2: Tentacion de mejora diferida
Durante un fix de bug en `PaymentController.cs` se observa que el archivo entero usa
convenciones de naming antiguas (`camelCase` en lugar de `PascalCase` para metodos publicos).
Aplicando Surgical Changes: el fix del bug se entrega acotado a las lineas del bug. La
inconsistencia de naming se registra como hallazgo de calidad para una sesion de limpieza
dedicada (relacionado con `apb-dev-sonar-clean-v1.0`), no se corrige en este PR.

## Integration
- Complementa: `apb-dev-simplicity-first-v1.0` (Surgical Changes evita sobre-tocar;
  Simplicity First evita sobre-construir)
- Relacionado con: `apb-dev-impact-analysis-v1.0` (analisis de alcance antes de tocar)
- Alimenta: la futura capacidad de análisis de deuda técnica todavía no construida
  (propuesta del punto #25 de `PLAN_FASES_FUTURAS.md`, pendiente de decisión de Debora sobre
  si amplía Sesión 11 o es sesión propia — sin ID de componente formal hasta esa decisión)
- Aplicada por: `apb-agent-meta-builder-v1.0` (Sesion 10) al generar o modificar componentes

## Tags
#surgical #scope #pr-discipline #tech-debt #development #karpathy

---

> **Generado por IA:** Claude (Anthropic), Sesión 10 del plan de remediación APB-IA-FRAMEWORK.
> **Validado por humano:** _pendiente — completar nombre/rol del validador antes de pasar a `candidate`._


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-dev-surgical-changes-v1.0) - pendiente validacion humana. No distribuir sin revision.
