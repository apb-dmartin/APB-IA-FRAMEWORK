---
id: "apb-plat-secret-rotation-v1.0"
name: "Rotación de Secretos con Azure Key Vault"
description: "Diseña e implementa la política de rotación automática de secretos en Azure Key Vault para APB. Genera el plan de rotación (90 días máx. para secretos de producción), la lógica de función Azure para rotación automática, alertas de expiración y el runbook de rotación manual de emergencia."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
created_date: "2026-06-29"
review_date: "2026-12-29"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# Rotación de Secretos con Azure Key Vault


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Propósito
Asegurar que todos los secretos de los sistemas APB (connection strings, API keys, certificados, contraseñas de servicio) se rotan automáticamente conforme a la política de seguridad APB (máximo 90 días para secretos de producción, alineado con ENS Alto). Genera la configuración de Key Vault, la función de rotación automática (Azure Function + Event Grid) y las alertas de expiración para que ningún secreto expire silenciosamente.

## Contexto de Uso
- Alta de un nuevo sistema: definir los secretos que necesita y su política de rotación.
- Revisión periódica del estado de secretos en un Key Vault existente.
- Diseño de la función de rotación automática para un tipo de secreto (ej. Azure SQL, Storage Account).
- Incidente: un secreto ha expirado en producción — runbook de recuperación rápida.
- Auditoría ENS: verificar que la política de rotación se cumple y está documentada.

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `operation` | Enum | `disenar-politica` / `configurar-rotacion` / `revisar-estado` / `runbook-emergencia` | ✅ |
| `secret_type` | Texto | Tipo de secreto: `azure-sql` / `storage-account` / `service-bus` / `api-key` / `certificate` | ✅ |
| `system_name` | Texto | Sistema propietario del secreto | ✅ |
| `rotation_period_days` | Número | Período de rotación en días (máx. 90 para prod) | ❌ |
| `keyvault_name` | Texto | Nombre del Key Vault donde se almacena el secreto | ❌ |

## Política de Rotación APB

| Tipo de secreto | Período máximo | Rotación automática | Alertas |
|---|---|---|---|
| Connection strings DB prod | 90 días | Recomendada | 30 días antes, 7 días antes, día de expiración |
| API keys externas | 90 días | Manual (depende del proveedor externo) | 30 días antes, 7 días antes |
| Certificados TLS | 365 días (renovar con 60 días de margen) | Automática via Key Vault | 60 días antes, 30 días antes |
| Managed Identity credentials | No expiran | N/A — usar MI en lugar de secretos cuando sea posible | N/A |
| SAS tokens de corta duración | <24h | Por diseño (generar bajo demanda) | No aplica |

### Principio rector
**Usar Managed Identity siempre que el servicio Azure lo soporte.** Los secretos en Key Vault son para servicios externos o casos donde MI no es viable.

## Flujo de Trabajo

### Diseño de política de rotación

1. **Inventario de secretos del sistema**:
   - Listar todos los secretos necesarios por el sistema.
   - Para cada secreto: tipo, período de rotación, si admite rotación automática.

2. **Nomenclatura de secretos en Key Vault APB**:
   ```
   {sistema}-{entorno}-{tipo}-{sufijo}
   Ejemplos:
     gispem-prod-db-connectionstring
     gispem-prod-servicebus-sender-key
     portal-prod-sendgrid-apikey
   ```

3. **Configuración de rotación automática en Key Vault**:
   - Para secretos de Azure SQL y Storage Account: usar la función de rotación integrada de Key Vault + Event Grid.
   - Configurar `expiryTime` en el secreto al crearlo.
   - Suscribir al evento `Microsoft.KeyVault.SecretNearExpiry` para alertas.

4. **Azure Function de rotación** (para secretos sin rotación nativa de Key Vault):
   ```csharp
   // Trigger: Event Grid (SecretNearExpiry)
   // 1. Obtener secreto actual de Key Vault
   // 2. Generar nuevo valor (rotar en el servicio destino)
   // 3. Escribir nueva versión del secreto en Key Vault
   // 4. Marcar versión anterior como expirada
   // 5. Notificar al equipo ops (email/Teams)
   ```

5. **Alertas de expiración** (Azure Monitor + Action Group):
   - Alerta 30 días antes: informativa, equipo de plataforma.
   - Alerta 7 días antes: urgente, equipo de plataforma + responsable del sistema.
   - Alerta día de expiración: crítica, escalado automático a on-call.

### Runbook de emergencia (secreto expirado en producción)

```markdown
## Runbook: Secreto expirado en producción

**Tiempo objetivo de resolución: <30 minutos**

1. [ ] Identificar el secreto expirado: nombre en Key Vault, sistema afectado
2. [ ] Rotar el secreto manualmente en el servicio origen (Azure SQL, API externa...)
3. [ ] Actualizar el secreto en Key Vault con el nuevo valor y nueva fecha de expiración
4. [ ] Si la aplicación cachea el secreto: reiniciar pods/instancias afectadas
5. [ ] Verificar que el sistema ha recuperado operatividad normal
6. [ ] Abrir incidente post-mortem: cómo llegó el secreto a expirar sin alerta previa
7. [ ] Configurar alerta para que no vuelva a ocurrir
```

## Salida Esperada

```markdown
# Plan de Rotación de Secretos — [Sistema] — [Fecha]
> ⚠️ Borrador generado por IA (APB AI Framework - apb-plat-secret-rotation-v1.0) — pendiente revisión del equipo de plataforma APB.

## Inventario de Secretos
| Nombre en Key Vault | Tipo | Período rotación | Rotación automática | Próxima expiración |
|---|---|---|---|---|

## Configuración de Alertas
| Alerta | Anticipación | Canal | Destinatarios |
|---|---|---|---|

## Código de Rotación Automática
[Azure Function + Bicep de infraestructura]

## Runbook de Emergencia
[...]
```

## Criterios de Calidad
- [ ] Ningún secreto de producción tiene período de rotación >90 días.
- [ ] Todos los secretos tienen fecha de expiración configurada en Key Vault.
- [ ] Hay al menos una alerta configurada antes de la expiración.
- [ ] Los secretos nunca se almacenan en variables de entorno en claro en AKS — siempre via CSI Secret Store.
- [ ] Los Managed Identity están configurados en todos los servicios Azure donde es posible.

## Dependencias
- `apb-plat-k8s-v1.0` — los manifiestos AKS referencian secretos de Key Vault via CSI Secret Store
- `apb-plat-azure-servicebus-v1.0` — los SAS keys de Service Bus siguen esta política

## Ejemplo de Uso

```
Diseña la política de rotación de secretos para el sistema GISPEM en producción.
Secretos necesarios: connection string Azure SQL, SAS key Azure Service Bus (sender), API key proveedor AIS.
Key Vault: kv-apb-prod.
```

## Notas y Advertencias
- La rotación de connection strings de Azure SQL requiere que la aplicación soporte reconexión automática — verificar el pool de conexiones de Entity Framework/Django.
- Las API keys de proveedores externos (ej. AIS maritime data) pueden tener procesos de rotación propios — coordinar con el proveedor.
- NUNCA poner secretos en código fuente, variables de entorno de Dockerfile, o logs.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento B |

## ⚠️ Comportamiento ante inputs incompletos

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `operation` | Pregunta: "¿Qué necesitas: diseñar política, configurar rotación automática, revisar estado o runbook de emergencia?" | Sí |
| `secret_type` | Pregunta: "¿Qué tipo de secreto es: connection string de BD, API key, SAS key, certificado?" | Sí |
| `system_name` | Pregunta: "¿Para qué sistema es este secreto?" | Sí |
| `rotation_period_days` | Usa 90 días (máximo política APB) e indica la asunción | No |
| `keyvault_name` | Usa `kv-apb-{env}` como convención APB e indica la asunción | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** — callout inmediatamente tras el título H1:
  > ⚠️ Borrador generado por IA (APB AI Framework - apb-plat-secret-rotation-v1.0) — pendiente revisión del equipo de plataforma APB.
- **Código C# / Bicep** — comentario en cabecera del archivo.
