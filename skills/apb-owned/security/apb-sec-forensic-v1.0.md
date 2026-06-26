---
id: "apb-sec-forensic-v1.0"
name: "Análisis Forense + Informe"
description: "Asistir en la investigación forense de incidentes de seguridad analizando logs, trazas de ejecución, artefactos de sistema y evidencias digitales. Genera un informe forense estructurado que documenta la cadena de custodia, timeline de eventos, indicadores de compromiso (IoC) y recomendaciones de ..."
version: "1.0.0"
status: "draft"
owner: "Ciberseguridad APB <arquitectura@portdebarcelona.cat>"
domain: "security"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Análisis Forense + Informe

## Propósito
Asistir en la investigación forense de incidentes de seguridad analizando logs, trazas de ejecución, artefactos de sistema y evidencias digitales. Genera un informe forense estructurado que documenta la cadena de custodia, timeline de eventos, indicadores de compromiso (IoC) y recomendaciones de contención y erradicación.

## Contexto de Uso
- Respuesta a incidentes de seguridad (brechas de datos, accesos no autorizados, malware).
- Análisis post-incidente para determinar alcance y root cause.
- Preparación de evidencia para procedimientos legales o regulatorios.
- Integración con workflows de operación (RCA) y gobierno (evidencias).

## Entradas Requeridas
| Entrada | Tipo | Descripción | Obligatorio |
|---------|------|-------------|-------------|
| `incident_description` | Texto | Descripción del incidente, fecha/hora de detección, sistemas afectados | ✅ |
| `log_sources` | Lista | Fuentes de logs disponibles: WAF, app, sistema, red, AD, etc. | ✅ |
| `log_samples` | Texto / Archivo | Muestras de logs relevantes (anonimizados si contienen PII) | ✅ |
| `system_artifacts` | Lista | Artefactos disponibles: memory dumps, disk images, registry, procesos | ❌ |
| `iocs_known` | Lista | Indicadores de compromiso conocidos previamente | ❌ |

## Flujo de Trabajo (Pasos)
1. **Ingesta y preservación**: Documentar fuentes de evidencia, integridad y cadena de custodia inicial.
2. **Timeline reconstruction**: Reconstruir cronología de eventos a partir de timestamps en logs y artefactos.
3. **Análisis de logs**: Correlacionar eventos entre diferentes fuentes de log (WAF, aplicación, sistema, red).
4. **Identificación de IoCs**: Extraer indicadores de compromiso: IPs, hashes, patrones de comportamiento, cuentas comprometidas.
5. **Determinación de alcance**: Identificar sistemas, datos y usuarios potencialmente afectados.
6. **Análisis de root cause**: Determinar vector de ataque, vulnerabilidad explotada y mecanismo de compromiso.
7. **Recomendaciones de respuesta**: Proponer acciones de contención, erradicación y recuperación.
8. **Generación de informe forense**: Documento estructurado con cadena de custodia, timeline, IoCs y conclusiones.
9. **Registro de evidencia**: Metadatos para gobierno y posible acción legal.

## Salida Esperada
### Estructura del Informe
```markdown
# Informe Forense — Incidente [ID]
> Fecha: [YYYY-MM-DD] | Investigador: Security Architect Agent | Clasificación: Confidencial

## 1. Resumen Ejecutivo
## 2. Alcance y Objetivos
## 3. Cadena de Custodia
| Evidencia | Fuente | Hash SHA-256 | Recolectado por | Fecha/Hora |
## 4. Timeline de Eventos
| Timestamp | Fuente | Evento | Severidad | Notas |
## 5. Análisis de Logs
## 6. Indicadores de Compromiso (IoCs)
| Tipo | Valor | Confianza | Primera Aparición |
## 7. Alcance del Impacto
## 8. Root Cause Analysis
## 9. Recomendaciones de Respuesta
### 9.1 Contención
### 9.2 Erradicación
### 9.3 Recuperación
## 10. Lecciones Aprendidas
## 11. Evidencia y Metadatos
```

## Criterios de Calidad
- [ ] Timeline cronológico completo con fuentes verificables.
- [ ] Todos los IoCs documentados con nivel de confianza y primera aparición.
- [ ] Cadena de custodia trazable desde la recolección hasta el informe.
- [ ] Recomendaciones de respuesta priorizadas por urgencia y riesgo residual.
- [ ] El informe es presentable a autoridades o auditores sin edición adicional.
- [ ] Datos personales anonimizados según GDPR/LOPD.

## Stack y Tecnologías
- Fuentes de logs: Azure Monitor, Application Insights, WAF logs, Windows Event Log, syslog
- Análisis: KQL (Kusto Query Language), regex, correlación temporal
- Formatos: Markdown, PDF, CSV para IoCs
- Referencias: NIST SP 800-61 (Computer Security Incident Handling Guide)

## Dependencias
- `apb-ops-rca-v1.0` — para análisis de causa raíz post-incidente
- `apb-gov-evidence-v1.0` — para gestión de evidencias y cadena de custodia
- `apb-sec-risk-analysis-v1.0` — para evaluación de riesgo residual

## Ejemplo de Uso
**Prompt de invocación:**
```
Analiza el siguiente incidente de seguridad:
- Detección: 2026-06-18 03:15 UTC, alerta WAF de tráfico anómalo
- Sistema afectado: API de facturación (ASP.NET Core, Azure App Service)
- Logs disponibles: WAF (Azure Front Door), Application Insights, Azure AD sign-ins
- Hallazgo inicial: Múltiples intentos de inyección SQL desde IP 198.51.100.42
- Muestras de logs: [adjuntar logs anonimizados]
```

## Notas y Advertencias
- **Nivel 1**: El agente asiste en el análisis documental y de logs; no realiza adquisición forense de disco/memoria ni análisis de malware en sandbox.
- **Revisión humana obligatoria** antes de presentar el informe como evidencia legal.
- La cadena de custodia digital debe ser validada por personal forense cualificado.
- Los logs deben ser anonimizados previamente si contienen datos personales; el agente no procesa PII sin anonimización previa.

## Historial de Cambios
| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-20 | Arquitectura APB | Creación inicial |


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-sec-forensic-v1.0) - pendiente validacion humana. No distribuir sin revision.
