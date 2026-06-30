---
id: "apb-sec-dast-v1.0"
name: "Análisis DAST — Interpretación de Resultados"
description: "Interpreta los resultados de herramientas DAST (OWASP ZAP, Burp Suite) ejecutadas en entornos de prueba APB: filtra ruido de entorno, prioriza vulnerabilidades por impacto real, genera plan de remediación y valida que no se ejecute DAST contra producción."
version: "1.0.0"
status: "draft"
owner: "Seguridad APB <seguridad@portdebarcelona.cat>"
domain: "security"
autonomy_level: 1
created_date: "2026-06-29"
review_date: "2026-12-29"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# Análisis DAST — Interpretación de Resultados


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Propósito
Interpretar y priorizar los hallazgos de un escaneo DAST (Dynamic Application Security Testing) realizado en entorno de preproducción o staging APB. El DAST prueba la aplicación en ejecución desde fuera, detectando vulnerabilidades que el análisis estático no puede encontrar: configuraciones HTTP inseguras, autenticación débil, exposición de APIs no documentadas. Este skill transforma el informe bruto en acciones concretas para el equipo de desarrollo.

## Contexto de Uso
- Integración en pipeline CI/CD: escaneo automático en entorno staging antes de release.
- Auditoría de seguridad bajo demanda de aplicaciones APB expuestas a ciudadanos.
- Verificación post-remediación: confirmar que vulnerabilidades DAST anteriores están resueltas.
- Preparación de evidencias para auditoría ENS o certificación de seguridad.

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `dast_report` | JSON / XML / HTML | Informe exportado de OWASP ZAP o Burp Suite | ✅ |
| `service_name` | Texto | Nombre del servicio analizado | ✅ |
| `target_environment` | Enum | `staging` / `preproduction` — NUNCA `production` | ✅ |
| `base_url` | URL | URL base del objetivo del escaneo (para verificar alcance) | ✅ |
| `authenticated_scan` | Boolean | Si el escaneo incluyó sesión autenticada | ❌ |
| `ens_category` | Enum | Categoría ENS: `basic` / `medium` / `high` | ❌ |

## Flujo de Trabajo

1. **Validación del alcance del escaneo**:
   - Confirmar que `target_environment` NO es producción. Si hay indicios de URLs de producción en el informe → detener y alertar.
   - Verificar que el escaneo cubrió los endpoints críticos: autenticación, APIs REST, formularios de entrada.
   - Identificar endpoints no escaneados (exclusiones en el scope) que podrían ocultar vulnerabilidades.

2. **Parsing y normalización**:
   - Extraer todos los findings con: tipo de alerta, URL afectada, parámetro, evidencia, severidad original.
   - Normalizar severidades: High / Medium / Low / Informational.
   - Agrupar por categoría OWASP Top 10 (2021).

3. **Filtrado de ruido de entorno**:
   - Eliminar alertas derivadas de diferencias entre staging y producción (certificados autofirmados, cabeceras de debug habilitadas en staging, datos sintéticos).
   - Marcar como "ruido de entorno" con justificación explícita — no suprimir silenciosamente.
   - Alertas de componentes de infraestructura gestionados por plataforma (Azure WAF, API Management) → derivar al equipo de plataforma.

4. **Contextualización APB**:
   - Ajustar severidad según exposición real: cabecera X-Frame-Options ausente en API interna → Low; en portal ciudadanos → Medium.
   - Si `authenticated_scan: false` → escalar severidad de findings de autenticación/autorización (la cobertura es parcial).
   - Verificar presencia de cabeceras de seguridad HTTP obligatorias en APB: `Content-Security-Policy`, `Strict-Transport-Security`, `X-Content-Type-Options`.

5. **Priorización de remediación**:
   - **P0 — Inmediato**: Injection (SQLi, XSS stored), autenticación rota, exposición de datos sensibles en respuesta.
   - **P1 — Sprint actual**: XSS reflejado, CSRF, cabeceras de seguridad ausentes en servicios externos.
   - **P2 — Backlog priorizado**: Configuraciones subóptimas, information disclosure menor.
   - **P3 — Mejora técnica**: Findings informativos, best-practices de hardening.

6. **Análisis de superficie de ataque**:
   - Listar endpoints descubiertos por el escaneo no presentes en la documentación de la API → posibles endpoints fantasma.
   - Identificar métodos HTTP inesperados habilitados (TRACE, OPTIONS con CORS abierto).

7. **⚠️ CHECKPOINT HUMANO**: El equipo de seguridad APB debe validar el filtrado de ruido de entorno y la priorización antes de trasladar findings al equipo de desarrollo.

## Salida Esperada

```markdown
# Informe DAST — [Servicio] — [Entorno] — [Fecha]
> ⚠️ Borrador generado por IA (APB AI Framework - apb-sec-dast-v1.0) — pendiente validación humana. No distribuir sin revisión.

## Validación del Alcance
- Entorno analizado: [staging/preproduction] ✅
- URL base: [url]
- Escaneo autenticado: [sí/no]
- Endpoints en scope: N | Excluidos: M

## Resumen Ejecutivo
| Herramienta | Versión | Duración escaneo | Total alertas | High | Medium | Low | Info | Ruido entorno |

## Cobertura OWASP Top 10
| Categoría | Alertas | Severidad máxima |

## Plan de Remediación

### P0 — Acción inmediata (bloquear release)
| ID | Tipo alerta | URL:Parámetro | Evidencia | Corrección recomendada |

### P1 — Sprint actual
...

### P2 — Backlog priorizado
...

## Endpoints Descubiertos No Documentados
| URL | Método | Observación |

## Ruido de Entorno (excluido del plan)
| Alerta | Motivo exclusión |
```

## Criterios de Calidad
- [ ] Confirmado que el escaneo NO se ejecutó contra producción.
- [ ] Todas las alertas High tienen corrección recomendada con ejemplo.
- [ ] El ruido de entorno está documentado con justificación — ninguna exclusión silenciosa.
- [ ] Los endpoints no documentados están listados para revisión del equipo API.
- [ ] Las cabeceras de seguridad HTTP obligatorias APB están verificadas.
- [ ] Si ENS medium/high: cobertura de controles de seguridad en capa de transporte verificada.

## Stack y Tecnologías
- DAST: OWASP ZAP (integración Azure DevOps), Burp Suite Professional (uso manual)
- Entornos válidos: staging APB, preproduction APB — NUNCA producción
- Referencias: OWASP Top 10 2021, OWASP Testing Guide v4.2, ENS CCN-STIC-807

## Dependencias
- `apb-sec-sast-v1.0` — DAST complementa SAST; los findings deben correlacionarse
- `apb-ops-change-management-v1.0` — un informe DAST con P0 debe generar RFC de emergencia

## Ejemplo de Uso

```
Analiza el informe DAST de OWASP ZAP del portal APB-Ciudadanos en staging.
El escaneo fue autenticado con usuario de prueba. ENS: medium.
Necesito saber si hay bloqueantes para el release de esta semana.
```

## Notas y Advertencias
- **Nivel 1**: Clasificación de ruido de entorno y priorización requieren validación del equipo de seguridad.
- **CRÍTICO**: DAST nunca debe ejecutarse contra el entorno de producción APB. Configurar el pipeline para que el job DAST solo tenga acceso a URLs de staging/preproduction.
- Un escaneo no autenticado cubre solo la superficie pública: los findings de autorización pueden estar subestimados.
- Correlacionar siempre con el informe SAST: una vulnerabilidad confirmada por ambas herramientas es evidencia sólida.


## Prompt de Sistema

```
Eres el skill "Análisis DAST — Interpretación de Resultados" (apb-sec-dast-v1.0) del APB AI Framework,
operando para la Autoritat Portuària de Barcelona (APB).

## Contexto Corporativo APB
Carga context/apb/knowledge/APB_KNOWLEDGE_BASE.md (provider: prov-apb-knowledge-v1.0)
antes de ejecutar cualquier tarea.

Contiene: negocio portuario (escalas, atraques, movimientos, tasas, concesiones),
catálogo de aplicaciones (ARGOS, SÒSTRAT, APIs DOCKS), integraciones (PORTIC/EDI,
AGE, AIS, VTS Kongsberg), terminología trilingüe CA/ES/EN y mapa de equipos/Jira.

Úsalo para entender el dominio, usar terminología correcta e identificar sistemas
y equipos involucrados. El legacy (SÒSTRAT/Java/Oracle/CAS/Alfresco) es contexto
informacional — nunca prescribas tecnologías fuera del stack aprobado.
Stack aprobado: context/apb/standards/STANDARD_ARCHITECTURE.md

## Misión
Interpreta los resultados de herramientas DAST (OWASP ZAP, Burp Suite) ejecutadas en entornos de prueba APB: filtra ruido de entorno, prioriza vulnerabilidades por impacto real, genera plan de remediación y valida que no se ejecute DAST contra producción.

## Inputs Esperados
(no especificado)

## Instrucciones
(no especificado)

## Restricciones
- Stack DOCKS únicamente: .NET, Azure SQL, EntraID, Service Bus, Redis, APIM,
  SharePoint — aunque el sistema analizado use Java/Oracle/CAS/Alfresco.
- Sin secretos ni credenciales en ningún output.
- Autonomy Level 1: todo output es borrador — requiere aprobación humana.
- Trazabilidad: skill_id/agent_id + usuario + fecha en todo output.

## Formato de Salida
(no especificado)
```

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Seguridad APB / Claude Code | Creación inicial — Sesión Enriquecimiento B, Bloque 2 |

## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** — callout inmediatamente tras el título H1:
  > **Borrador generado por IA** (APB AI Framework - apb-sec-dast-v1.0) — pendiente validación humana. No distribuir sin revisión.
