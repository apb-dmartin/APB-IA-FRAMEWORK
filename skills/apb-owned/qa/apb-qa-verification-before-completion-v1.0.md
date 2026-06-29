---
id: "apb-qa-verification-before-completion-v1.0"
name: "Verification"
description: "Usar cuando est\xE1s a punto de declarar que el trabajo est\xE1 completo, arreglado,\
  \ o pasando, antes de commitear o crear PRs \u2014 requiere ejecutar comandos de\
  \ verificaci\xF3n y confirmar output antes de hacer cualquier afirmaci\xF3n de \xE9\
  xito; evidencia antes de afirmaciones siempre."
version: "1.0.0"
status: "draft"
owner: "QA APB <arquitectura@portdebarcelona.cat>"
domain: "qa"
autonomy_level: 1
consumed_by:
  - "apb-agent-qa-auto-v1.0"
created_date: "2026-06-20"
review_date: "2026-06-24"
---

> Procedencia: Adaptado de obra/superpowers (verification-before-completion) (licencia MIT). Contenido adaptado y
> generalizado para el APB AI Framework.

# APB Verification Before Completion

## Visión General

Declarar que el trabajo está completo sin verificación es deshonestidad, no eficiencia.

**Principio fundamental:** Evidencia antes de afirmaciones, siempre.

**Violar la letra de esta regla es violar el espíritu de esta regla.**

## La Ley de Hierro

```
NO AFIRMACIONES DE COMPLETITUD SIN EVIDENCIA FRESH DE VERIFICACIÓN
```

Si no has ejecutado el comando de verificación en este mensaje, no puedes afirmar que pasa.

## La Función de Puerta

```
ANTES de afirmar cualquier estado o expresar satisfacción:

1. IDENTIFICAR: ¿Qué comando prueba esta afirmación?
2. EJECUTAR: Ejecutar el comando COMPLETO (fresh, completo)
3. LEER: Output completo, chequear exit code, contar fallas
4. VERIFICAR: ¿El output confirma la afirmación?
   - Si NO: Declarar estado actual con evidencia
   - Si SÍ: Declarar afirmación CON evidencia
5. SOLO ENTONCES: Hacer la afirmación

Saltar cualquier paso = mentir, no verificar
```

## Verificaciones Específicas de Event-Driven

### Tests de Integración

```bash
# Verificar que todos los tests de integración pasan
npm test -- --testPathPattern="integration"

# Requerido: 0 fallas
# Requerido: Todos los eventos se publican/consumen correctamente
```

### Verificación de Topología

```bash
# Verificar que topics y subscriptions existen
az servicebus topic list --namespace-name sb-apb-prod --resource-group rg-apb
az servicebus topic subscription list --namespace-name sb-apb-prod --topic-name topic-orders --resource-group rg-apb

# Requerido: Todos los topics del spec existen
# Requerido: Todas las subscriptions están configuradas
```

### Verificación de Dead Letter Queues

```bash
# Verificar que DLQs están vacías (o monitoreadas)
az servicebus topic subscription show   --namespace-name sb-apb-prod   --topic-name topic-orders   --subscription-name sub-inventory-service   --resource-group rg-apb   --query "countDetails.activeMessageCount"

# Alerta si > 0 mensajes en DLQ sin procesar
```

### Verificación de Schemas

```bash
# Validar que todos los eventos cumplen CloudEvents 1.0
npm run validate:cloud-events

# Requerido: 0 eventos inválidos
# Requerido: Todos los campos obligatorios presentes
```

### Verificación de Idempotencia

```bash
# Ejecutar tests de idempotencia
npm test -- --testPathPattern="idempotency"

# Requerido: Eventos duplicados no causan efectos secundarios
```

### Verificación de Saga

```bash
# Ejecutar tests de saga (compensación)
npm test -- --testPathPattern="saga"

# Requerido: Compensaciones funcionan correctamente
# Requerido: Estado final consistente después de compensación
```

## Fallas Comunes

| Afirmación | Requiere | No Es Suficiente |
|------------|----------|-----------------|
| Tests pasan | Output de test: 0 fallas | Ejecución anterior, "debería pasar" |
| Linter limpio | Output de linter: 0 errores | Chequeo parcial, extrapolación |
| Build exitoso | Build command: exit 0 | Linter pasando, logs se ven bien |
| Bug arreglado | Test del síntoma original: pasa | Código cambiado, asumido arreglado |
| Evento publicado | Verificación en Service Bus | Código ejecutado sin error |
| DLQ limpia | Query de DLQ: 0 mensajes | No revisado recientemente |
| Schema válido | Validación CloudEvents: pass | Asumido por estructura similar |

## Banderas Rojas — DETENER

- Usar "debería", "probablemente", "parece que"
- Expresar satisfacción antes de verificación ("¡Genial!", "¡Perfecto!", "¡Listo!", etc.)
- A punto de commitear/pushear/PR sin verificación
- Confiar en reportes de éxito de agentes
- Depender en verificaciones parciales
- Asumir que "funcionó antes" sigue funcionando


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-qa-verification-before-completion-v1.0) - pendiente validacion humana. No distribuir sin revision.
