---
id: "apb-ops-runbook-v1.0"
name: "Generación de Runbooks"
description: "Generar runbooks estructurados para operación, troubleshooting y recuperación de servicios. Incluye procedimientos paso a paso, comandos, verificaciones y criterios de escalado, adaptados al stack tecnológico de APB (.NET, Azure, Docker)."
version: "1.0.0"
status: "draft"
owner: "SRE APB <arquitectura@portdebarcelona.cat>"
domain: "operation"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Generación de Runbooks

## Propósito
Generar runbooks estructurados para operación, troubleshooting y recuperación de servicios. Incluye procedimientos paso a paso, comandos, verificaciones y criterios de escalado, adaptados al stack tecnológico de APB (.NET, Azure, Docker).

## Contexto de Uso
- Creación de runbooks para nuevos servicios antes del despliegue a producción.
- Actualización de runbooks tras cambios arquitectónicos o de procedimiento.
- Generación de playbooks de respuesta a incidentes basados en RCAs previos.
- Integración con workflows de operación y gobierno.

## Entradas Requeridas
| Entrada | Tipo | Descripción | Obligatorio |
|---------|------|-------------|-------------|
| `service_description` | Texto / Markdown | Descripción del servicio y componentes | ✅ |
| `scenario` | Enum | `health-check`, `restart`, `failover`, `scale-out`, `troubleshooting`, `recovery` | ✅ |
| `azure_resources` | Lista | Recursos Azure implicados | ✅ |
| `commands_needed` | Boolean | ¿Incluir comandos Azure CLI / PowerShell / kubectl? | ❌ (default: true) |
| `escalation_path` | Lista | Contactos y condiciones de escalado | ❌ |

## Flujo de Trabajo (Pasos)
1. **Análisis de escenario**: Determinar objetivo del runbook y recursos implicados.
2. **Diseño de procedimiento**: Estructurar pasos en secuencia lógica:
   - **Pre-condiciones**: Estado requerido antes de iniciar.
   - **Pasos de ejecución**: Comandos, clicks, verificaciones.
   - **Verificaciones**: Cómo confirmar que cada paso fue exitoso.
   - **Rollback**: Cómo deshacer cambios si algo falla.
   - **Post-condiciones**: Estado esperado al finalizar.
3. **Generación de comandos**: Incluir comandos específicos para Azure CLI, PowerShell, kubectl, etc.
4. **Definición de criterios de escalado**: Cuándo y a quién escalar si el runbook no resuelve el problema.
5. **Validación de seguridad**: Verificar que los comandos no exponen secretos ni datos sensibles.
6. **Generación de runbook**: Documento markdown estructurado con formato corporativo.
7. **Registro de evidencia**: Metadatos para gobierno.

## Salida Esperada
### Estructura del Runbook
```markdown
# Runbook — [Escenario] — [Nombre Servicio]
> ID: RUN-[YYYY]-[NNNN] | Versión: X.Y.Z | Fecha: [YYYY-MM-DD]
> Autor: SRE Agent | Revisado por: [SRE Lead] | Estado: draft

## 1. Objetivo
## 2. Alcance
## 3. Pre-condiciones
## 4. Procedimiento
### Paso 1: [Descripción]
```bash
[comando]
```
**Verificación:** [cómo confirmar éxito]
### Paso 2: ...
## 5. Rollback
## 6. Post-condiciones
## 7. Escalado
| Condición | Contacto | Método | SLA |
## 8. Historial de Cambios
## 9. Evidencia y Metadatos
```

## Criterios de Calidad
- [ ] Cada paso tiene descripción, comando (si aplica) y verificación.
- [ ] El rollback está documentado para cada paso que modifica estado.
- [ ] Los criterios de escalado son claros y actionable.
- [ ] No se incluyen secretos, contraseñas ni connection strings en los comandos.
- [ ] El runbook es ejecutable por un ingeniero de operaciones de guardia sin intervención del agente.
- [ ] Las pre-condiciones y post-condiciones son verificables.

## Stack y Tecnologías
- Azure CLI, Azure PowerShell, kubectl
- Azure Portal paso a paso (screenshots descriptivos)
- Formatos: Markdown, Confluence para almacenamiento

## Dependencias
- `apb-ops-operability-v1.0` — para contexto de operabilidad
- `apb-ops-observability-v1.0` — para queries KQL de troubleshooting
- `apb-ops-rca-v1.0` — para lecciones aprendidas que alimentan runbooks
- `apb-gov-evidence-v1.0` — para generación de evidencia

## Ejemplo de Uso
**Prompt de invocación:**
```
Genera un runbook para failover del microservicio de pagos:
- Servicio: ASP.NET Core 8, Azure Container Apps, Azure SQL (geo-replica)
- Escenario: failover por caída de región primaria (westeurope)
- Recursos: Container App, SQL Database (failover group), Service Bus (geo-redundante)
- Comandos: Azure CLI para failover de SQL, redirección de tráfico en Front Door
- Escalado: Si failover tarda > 10 minutos → escalar a SRE Lead y Arquitecto Cloud
```

## Notas y Advertencias
- **Nivel 1**: El agente genera documentación de runbooks; no ejecuta comandos en entornos de producción.
- **Revisión humana obligatoria** antes de publicar runbook para uso en producción.
- Los runbooks deben probarse en pre-producción antes de su aprobación.
- Los comandos deben validarse contra la versión actual de Azure CLI y recursos.
- El agente no tiene acceso a credenciales; los comandos usan variables y Managed Identities.

## Historial de Cambios
| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-20 | Arquitectura APB | Creación inicial |
