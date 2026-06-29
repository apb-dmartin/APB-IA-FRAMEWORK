---
id: "apb-dev-grill-before-code-v1.0"
name: "Grill Before Code"
description: "Aplica un interrogatorio sistematico (grill) antes de escribir cualquier linea de codigo, asegurando que los requisitos, el dominio y las restricciones esten completamente claros."
version: "1.0.0"
status: "draft"
owner: "Desarrollo APB <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

> Inspirado en: mattpocock/grill-prd-issues + skills.sh/superpowers-method (licencia MIT).

# Grill Before Code

## Purpose
Aplica un interrogatorio sistematico (grill) antes de escribir cualquier linea de codigo, asegurando que los requisitos, el dominio y las restricciones esten completamente claros.

## Trigger
- Antes de iniciar implementacion de feature, bugfix o refactor
- Cuando el PRD/user story parece ambiguo o incompleto
- Cuando hay multiples interpretaciones posibles del requerimiento

## Input
- Descripcion del requerimiento (PRD, ticket, conversacion)
- Contexto tecnico actual (stack, arquitectura)
- Restricciones conocidas (tiempo, recursos, compliance)

## Output
- Lista de preguntas respondidas (minimo 5)
- Decisiones explicitas documentadas
- Riesgos identificados antes de codificar

## Procedure

### Phase 1: Clarificacion del Problema
1. Que problema resolvemos? No la solucion, el problema real.
2. Para quien? Usuario final, sistema downstream, operador.
3. Que pasa si no lo hacemos? Costo de oportunidad / riesgo.

### Phase 2: Interrogatorio Tecnico
4. Donde encaja? En la arquitectura actual, que toca.
5. Que asumimos? Lista explicita de asunciones.
6. Que no sabemos? Incertidumbres que requieren spike.
7. Cual es el scope minimo viable? Linea de corte para MVP.

### Phase 3: Validacion de Comprension
8. Puedo explicarlo en 2 minutos? Test de claridad.
9. El output esperado esta definido? Criterios de aceptacion concretos.
10. Hay dependencias bloqueantes? Identificar antes de empezar.

## Rules
- NO escribir codigo hasta que al menos 5 preguntas esten respondidas
- Las respuestas deben ser explicitas, no implicitas
- Si una pregunta no tiene respuesta clara: spike, no codigo
- Documentar las respuestas en el mismo thread/contexto

## Examples

### Example 1: Feature Ambigua
Input: "Necesitamos un dashboard de metricas"
Grill:
- Que metricas? -> Latencia, throughput, errores 4xx/5xx
- Para quien? -> Equipo SRE, alertas automaticas
- Donde encaja? -> Modulo observability existente, nuevo endpoint /metrics
- Que asumimos? -> Datos en Azure Monitor, retencion 30 dias
- Scope minimo? -> Tabla con 3 metricas, refresh manual

Output: Decisiones documentadas, spike de 2h para validar queries de Monitor

### Example 2: Bug Report Vago
Input: "A veces falla el login"
Grill:
- Que significa "a veces"? -> Frecuencia, condiciones
- Que error devuelve? -> 401, 500, timeout
- Cuando empezo? -> Regresion o nuevo feature
- Hay logs? -> Correlacion con trace IDs

Output: Checklist de informacion faltante antes de tocar codigo

## Integration
- Precede a: apb-dev-atomic-plan-v1.0, cualquier skill de implementacion
- Usa: `third-mattpocock-grill-prd-issues-v1.0` (wrapper con filtro APB) — ⚠️ **PENDIENTE**: fuente citada (mattpocock/grill-prd-issues) sin descriptor formal creado todavía. Ver Sesión 5.
- Relacionado con: apb-dev-impact-analysis-v1.0 (para evaluar alcance)

## Tags
#grill #requirements #clarification #before-code #development


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-dev-grill-before-code-v1.0) - pendiente validacion humana. No distribuir sin revision.
