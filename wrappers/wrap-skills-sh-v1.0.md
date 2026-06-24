---
id: "wrap-skills-sh-v1.0"
name: "skills.sh"
description: "Wrapper para gestionar la integración de skills de skills.sh con el APB AI Framework. Gestiona suscripción, valida uso interno y adapta skills propietarias al ecosistema APB."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
wraps: "skills.sh"
source_repo: "https://github.com/skills.sh"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# skills.sh

## Descripción
Wrapper para gestionar la integración de skills de skills.sh con el APB AI Framework. Gestiona suscripción, valida uso interno y adapta skills propietarias al ecosistema APB.

## Funciones del Wrapper

### 1. Gestión de Suscripción
- Verificación de suscripción activa
- Tracking de uso y límites
- Renovación automática (configurable)

### 2. Validación de Uso Interno
- Confirmación de uso autorizado
- Restricción de redistribución
- Cumplimiento de términos de servicio

### 3. Adaptación de Skills
- Conversión de formato skills.sh → APB
- Mapeo de componentes DevExpress
- Alineación con estándares de diseño APB

### 4. Filtrado de Capacidades
- Identificación de capacidades no corporativas
- Aplicación de políticas de seguridad
- Restricción de acceso a datos sensibles

## Skills Cubiertos
| Skill Tercero | Skill APB Relacionada | Estado |
|---------------|----------------------|--------|
| `third-skills-sh-frontend-v1.0` | `apb-dev-devexpress-front-v1.0` | draft |
| `third-obra-superpowers-method-v1.0` | `apb-agent-domain-architect-v1.0` | draft |

## Configuración
```json
{
  "wrapper_id": "wrap-skills-sh-v1.0",
  "source": "skills.sh",
  "license": "Propietaria",
  "subscription_check": true,
  "usage_limits": {
    "daily_requests": 1000,
    "concurrent_sessions": 10
  },
  "runtimes": ["copilot", "claude"]
}
```

## Inputs
- `raw_skill`: skill de skills.sh en formato original
- `subscription_token`: token de suscripción (AKV)
- `target_runtime`: runtime objetivo

## Outputs
- `adapted_skill`: skill adaptado al formato APB
- `usage_report`: informe de uso
- `subscription_status`: estado de suscripción

## Restricciones
- Licencia propietaria: uso restringido a entorno APB
- No redistribución permitida
- Requiere suscripción activa
- Datos corporativos no salen del entorno APB

## Ejemplo de Uso
```
Invocar: wrap-skills-sh-v1.0
Input: { raw_skill: "skills-sh-frontend", target_runtime: "copilot" }
Output: Skill adaptado con validación de suscripción y uso
```

---
*Wrapper APB AI Framework.*
