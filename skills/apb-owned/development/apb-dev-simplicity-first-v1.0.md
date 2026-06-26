---
id: "apb-dev-simplicity-first-v1.0"
name: "Simplicity First"
description: "Obliga a generar el codigo minimo que resuelve el problema solicitado, sin abstracciones, configuracion ni flexibilidad que nadie pidio. Complementa apb-dev-surgical-changes-v1.0."
version: "1.0.0"
status: "draft"
owner: "Desarrollo APB <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 1
created_date: "2026-06-24"
review_date: "2026-06-24"
---

> Inspirado en: multica-ai/andrej-karpathy-skills (principio "Simplicity First", licencia MIT).
> Origen: 4 principios operacionales para agentes de codificacion derivados de observaciones
> publicas de Andrej Karpathy sobre fallos tipicos de LLMs al programar. Ver Principio
> Fundamental #11 de README.md.

# Simplicity First

## Purpose
Obliga a generar el codigo minimo que resuelve el problema solicitado, sin abstracciones,
capas de configuracion, ni flexibilidad "por si acaso" que nadie pidio. Contrarresta la
tendencia de los LLM a sobre-disenar: anadir interfaces, factories, parametros opcionales o
generalizaciones especulativas que aumentan superficie de mantenimiento sin valor presente.

## Trigger
- Antes de implementar cualquier solucion tras `apb-dev-grill-before-code-v1.0`
- Cuando el output propuesto incluye mas de una forma de hacer lo mismo
- Cuando se anaden parametros, flags o interfaces sin un caso de uso actual que los requiera
- Code review: cualquier PR que introduce abstraccion nueva

## Input
- Requerimiento clarificado (output de `apb-dev-grill-before-code-v1.0`)
- Propuesta de diseno o codigo borrador
- Casos de uso actuales conocidos (no futuros hipoteticos)

## Output
- Version simplificada del diseno/codigo (si aplica)
- Lista de abstracciones eliminadas y justificacion
- Registro explicito de "YAGNI" (You Aren't Gonna Need It) aplicado

## Procedure

### Phase 1: Auditoria de Necesidad
1. Cada clase/interfaz/funcion nueva: ¿la pidio el requerimiento o la anadi yo?
2. Cada parametro opcional: ¿hay un caso de uso real hoy, o es "por flexibilidad futura"?
3. Cada capa de indireccion (factory, strategy, plugin): ¿hay mas de una implementacion real
   hoy, o solo una con preparacion especulativa para una segunda que no existe?

### Phase 2: Poda
4. Eliminar toda abstraccion sin segundo caso de uso real.
5. Eliminar configuracion que nunca cambia en la practica (hardcodear si es estable).
6. Preferir la solucion mas directa que pase los tests, no la mas "elegante" o generica.

### Phase 3: Validacion de Minimo Viable
7. ¿El codigo resultante resuelve exactamente el problema, ni mas ni menos?
8. ¿Anadir el siguiente caso de uso real (cuando aparezca) seria un cambio quirurgico
   razonable, no una reescritura? Si la respuesta es no, revisar diseno (no sobre-disenar
   ahora, pero tampoco bloquear extension futura razonable).

## Rules
- No crear una interfaz para una unica implementacion sin caso de uso real de una segunda.
- No anadir parametros "para configurabilidad futura" sin un consumidor actual.
- No generalizar un caso especifico en un framework interno sin que APB lo haya pedido.
- "Podria servir para..." no es un caso de uso. Un caso de uso es una historia real, hoy.
- Simplicidad no es ausencia de calidad: tests, manejo de errores y seguridad nunca se omiten
  por "simplificar" — esto aplica solo a abstraccion y flexibilidad estructural.

## Examples

### Example 1: Sobre-ingenieria evitada
Input: "Necesito guardar el estado de una sesion en cache"
Propuesta inicial (rechazada): `ICacheProvider` con implementaciones `RedisCacheProvider`,
`MemoryCacheProvider`, `NullCacheProvider` + factory + configuracion por DI.
Aplicando Simplicity First: APB usa Azure Cache for Redis en todos los entornos (`STANDARD_ARCHITECTURE.md`).
No hay un segundo proveedor real. Solucion: clase concreta `SessionCache` que envuelve el
cliente Redis directamente. Si en el futuro aparece un segundo proveedor real, se extrae la
interfaz entonces (cambio quirurgico, no preparacion especulativa hoy).

### Example 2: Parametro sin consumidor
Input: PR anade `bool enableLegacyMode = false` a un metodo de validacion.
Grill: ¿Que codigo llama con `true`? Respuesta: ninguno, "por si en el futuro hace falta".
Aplicando Simplicity First: se elimina el parametro. Si aparece la necesidad real, se anade
en ese momento con su caso de uso concreto documentado.

## Integration
- Precedido por: `apb-dev-grill-before-code-v1.0`, `apb-dev-atomic-plan-v1.0`
- Complementa: `apb-dev-surgical-changes-v1.0` (Simplicity First evita sobre-construir;
  Surgical Changes evita sobre-tocar)
- Seguido por: `apb-dev-verify-before-done-v1.0`
- Aplicada por: `apb-agent-meta-builder-v1.0` (Sesion 10) al generar todo componente nuevo

## Tags
#simplicity #yagni #over-engineering #development #karpathy

---

> **Generado por IA:** Claude (Anthropic), Sesión 10 del plan de remediación APB-IA-FRAMEWORK.
> **Validado por humano:** _pendiente — completar nombre/rol del validador antes de pasar a `candidate`._


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-dev-simplicity-first-v1.0) - pendiente validacion humana. No distribuir sin revision.
