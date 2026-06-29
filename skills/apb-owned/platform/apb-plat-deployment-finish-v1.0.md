---
id: "apb-plat-deployment-finish-v1.0"
name: "Finalización y Despliegue de Rama"
description: "Verifica tests, presenta opciones de merge/deploy y ejecuta la elección del usuario al completar trabajo en una rama de desarrollo. Incluye despliegue de microservicios con health checks y rolling updates."
version: "1.0.0"
status: "draft"
owner: "Platform Engineering APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
consumed_by:
  - "apb-agent-release-manager-v1.0"
created_date: "2026-06-20"
review_date: "2026-06-24"
---

> Procedencia: adaptado de obra/superpowers (finishing-a-development-branch)
> y wshobson/agents (deployment-strategies), licencia MIT.

# APB Deployment: Finalización y Despliegue

## Visión General

Al completar trabajo en una rama de desarrollo, verificar tests, presentar opciones de merge/deploy, y ejecutar la elección del usuario.

**Anunciar al inicio:** "Estoy usando el skill apb-deployment para completar este trabajo."

## El Proceso

### Paso 1: Verificación Pre-Merge

1. Ejecutar todos los tests:
```bash
npm test
```

2. Verificar linter:
```bash
npm run lint
```

3. Verificar build:
```bash
npm run build
```

4. Verificar tests de integración de eventos:
```bash
npm run test:integration
```

5. Verificar DLQs:
```bash
npm run check:dlq
```

6. Verificar schemas:
```bash
npm run validate:schemas
```

**Si cualquier verificación falla:** Corregir antes de proceder.

### Paso 2: Presentar Opciones

```
Trabajo completo. Aquí están tus opciones:

1. **Merge a main** — Merge directo con commit de merge
2. **Squash merge** — Un solo commit limpio con todo el trabajo
3. **Rebase + merge** — Historial lineal, requiere force push
4. **Crear PR** — Para revisión humana antes de merge
5. **Deploy a staging** — Desplegar a ambiente de pruebas primero
6. **Deploy a producción** — Despliegue directo (requiere confirmación)

Recomendación: [basada en política del proyecto]
```

### Paso 3: Despliegue de Microservicios

#### Health Checks

Antes de desplegar, verificar health checks:

```javascript
// Health check endpoint (obligatorio para cada microservicio)
app.get('/health', async (req, res) => {
  const checks = {
    database: await checkDatabase(),
    serviceBus: await checkServiceBus(),
    eventConsumer: await checkEventConsumer(),
    deadLetterQueue: await checkDLQ()
  };

  const allHealthy = Object.values(checks).every(c => c.status === 'healthy');

  res.status(allHealthy ? 200 : 503).json({
    status: allHealthy ? 'healthy' : 'unhealthy',
    checks,
    timestamp: new Date().toISOString()
  });
});
```

#### Rolling Update

```yaml
# Kubernetes deployment strategy
spec:
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 0
      maxSurge: 1
  template:
    spec:
      containers:
        - name: microservice
          readinessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 10
            periodSeconds: 5
            failureThreshold: 3
          livenessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 30
            periodSeconds: 10
            failureThreshold: 3
```

#### Verificación Post-Deploy

```bash
# 1. Verificar que el servicio está healthy
curl -f http://servicio:8080/health

# 2. Verificar que consume eventos correctamente
# (monitorear métricas de Service Bus)

# 3. Verificar que publica eventos correctamente
# (enviar evento de prueba y verificar)

# 4. Verificar que DLQ está limpia
az servicebus topic subscription show   --namespace-name sb-apb-prod   --topic-name topic-orders   --subscription-name sub-inventory-service   --resource-group rg-apb   --query "countDetails.activeMessageCount"

# 5. Verificar distributed tracing
# (buscar traces en Application Insights)
```

### Paso 4: Documentación

Actualizar documentación:

```markdown
## Changelog

### [Versión] - [Fecha]

#### Eventos Nuevos
- `orders.order-created.v1` — Publicado por OrderService
- `inventory.reservation-confirmed.v1` — Publicado por InventoryService

#### Cambios en Schemas
- `payments.payment-completed.v1` — Añadido campo `transactionFee`

#### Topología Service Bus
- Nuevo topic: `topic-shipping`
- Nueva subscription: `sub-shipping-service`

#### Breaking Changes
- Ninguno (backward compatible)

#### Deprecaciones
- `orders.order-created.v0` — Deprecado, usar v1
```

## Rollback Strategy

```bash
# Si el despliegue falla:

# 1. Revertir a versión anterior
kubectl rollout undo deployment/microservicio

# 2. Verificar health después del rollback
curl -f http://servicio:8080/health

# 3. Verificar que eventos siguen fluyendo
# (monitorear métricas)

# 4. Documentar incidente
# (crear post-mortem si aplica)
```


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-plat-deployment-finish-v1.0) - pendiente validacion humana. No distribuir sin revision.
