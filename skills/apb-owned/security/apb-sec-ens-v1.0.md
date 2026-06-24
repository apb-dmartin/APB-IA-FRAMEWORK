---
id: "apb-sec-ens-v1.0"
name: "Requisitos ENS (Esquema Nacional de Seguridad)"
description: "Analizar sistemas, arquitecturas o procesos y determinar el grado de cumplimiento con los requisitos del Esquema Nacional de Seguridad (ENS) español. Genera un informe de gap analysis con controles aplicables, medidas de seguridad y plan de remediación. Incluye tablas operativas de controles concretos por nivel y formato de auditoría de hallazgos con severidad."
version: "1.1.0"
status: "draft"
owner: "Ciberseguridad APB <arquitectura@portdebarcelona.cat>"
domain: "security"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-24"
---

> **Fusión Sesión QA (post-Sesión 12):** esta skill incorpora, fusionado y adaptado, el
> contenido de `apb-ens-security-audit` (repo `apb-ai-skills`) — las tablas operativas de
> controles concretos por nivel Alto/Medio con verificación específica, el cruce con OWASP
> Top 10, y el formato de informe de hallazgos con severidad y plazo de remediación.
> Decisión de Debora: fusionar e incorporar a `APB-IA-FRAMEWORK`, sin mantener duplicado en
> el repo de origen. Nota de nomenclatura: esta skill usa la terminología ENS de 3 niveles
> (`básica`/`media`/`alta`, RD 311/2022); las tablas operativas fusionadas usan la
> abreviatura habitual en contexto APB ("ENS Alto"/"ENS Medio") — ambas conviven, "alta" y
> "ENS Alto" son el mismo nivel.

# Requisitos ENS (Esquema Nacional de Seguridad)

## Propósito
Analizar sistemas, arquitecturas o procesos y determinar el grado de cumplimiento con los requisitos del Esquema Nacional de Seguridad (ENS) español. Genera un informe de gap analysis con controles aplicables, medidas de seguridad y plan de remediación.

## Contexto de Uso
- Evaluación de cumplimiento ENS para sistemas de categoría Básica, Media o Alta.
- Preparación para auditorías de certificación o acreditación.
- Diseño de arquitecturas que deben cumplir ENS desde su concepción (security by design).
- Integración con workflows de gobierno y gestión de excepciones de riesgo.
- **Auditoría operativa de código/release**: revisión de código nuevo, preparación de
  auditoría ENS, evaluación de un sistema antes de un release, o respuesta a un hallazgo de
  seguridad (uso táctico, complementario al gap analysis estratégico de las secciones
  anteriores).

## Entradas Requeridas
| Entrada | Tipo | Descripción | Obligatorio |
|---------|------|-------------|-------------|
| `system_description` | Texto / Markdown | Descripción del sistema, alcance y funcionalidad | ✅ |
| `ens_level` | Enum | `básica`, `media`, `alta` | ✅ |
| `system_category` | Enum | `sistema de información`, `servicio`, `infraestructura` | ✅ |
| `existing_controls` | Lista | Controles de seguridad actualmente implementados | ❌ |
| `audit_scope` | Lista | Dimensiones a evaluar: `op`, `mp.sw`, `mp.hw`, `mp.com`, `mp.info` | ❌ (default: todas) |
| `source_code` | file_path | Código a auditar, cuando el uso es de auditoría operativa táctica | ❌ |
| `processes_personal_data` | bool | Si el sistema procesa datos personales (activa cruce con RGPD) | ❌ |

## Flujo de Trabajo (Pasos)
1. **Clasificación del sistema**: Determinar dimensiones ENS aplicables según categoría y nivel.
2. **Mapeo de requisitos**: Listar todos los requisitos ENS obligatorios para el nivel indicado.
3. **Evaluación de cumplimiento**: Para cada requisito, evaluar estado:
   - `cumple` — Control implementado y documentado.
   - `parcial` — Control parcial, requiere completar.
   - `no_cumple` — Control ausente.
   - `no_aplica` — Requisito no aplicable al alcance (justificar).
4. **Gap analysis**: Identificar brechas entre estado actual y requisitos obligatorios.
5. **Plan de remediación**: Para cada gap, proponer medida de seguridad, responsable y plazo estimado.
6. **Generación de informe**: Documento estructurado con trazabilidad, evidencias y firma de revisión.
7. **Registro de evidencia**: Metadatos para integración con gobierno y auditorías.

### 7bis. Tablas Operativas de Controles Concretos por Nivel

Cuando el uso es de auditoría operativa táctica (revisión de código/release), aplicar
directamente estas tablas de verificación concreta:

**ENS Alto (sistemas críticos APB) — controles adicionales respecto a nivel Medio:**

| Dominio | Control | Verificación |
|---|---|---|
| Autenticación | MFA obligatorio para todos los accesos | Revisar configuración IdP |
| Cifrado | AES-256 en reposo, TLS 1.3 en tránsito | Revisar configuración TLS, cifrado BD |
| Auditoría | Log inmutable de TODOS los accesos y operaciones | Revisar logging, integridad de logs |
| Gestión de secretos | HSM o Key Vault — nunca en código ni variables planas | Revisar código, configuración CI/CD |
| Segmentación | Red segmentada, acceso mínimo privilegio | Revisar arquitectura de red |
| Continuidad | RTO < 4h, RPO < 1h documentado y probado | Revisar plan de continuidad |
| Vulnerabilidades | Escaneo semanal, parche en < 72h para críticos | Revisar proceso de parcheo |

**ENS Medio (sistemas estándar APB):**

| Dominio | Control | Verificación |
|---|---|---|
| Autenticación | Contraseñas robustas + 2FA para admin | Revisar política de contraseñas |
| Cifrado | TLS 1.2+ en tránsito, cifrado datos sensibles en reposo | Revisar config TLS |
| Auditoría | Log de accesos a datos sensibles y operaciones críticas | Revisar logging |
| Gestión de secretos | Sin secretos en código ni repositorio | Revisar código y commits |
| Vulnerabilidades | Escaneo mensual, parche en < 7 días para críticos | Revisar proceso |

### 7ter. Formato de Informe de Auditoría Operativa (hallazgos con severidad)

Para el uso táctico de revisión de código/release, el output es un informe de hallazgos,
distinto del informe de gap analysis estratégico de la sección anterior:

```markdown
# Informe de Auditoría de Seguridad ENS
**Sistema:** [nombre]
**Nivel ENS:** Alto / Medio
**Fecha:** [fecha]
**Revisor:** [nombre]

## Resumen ejecutivo
- Críticos: X
- Altos: X
- Medios: X
- Bajos: X
- Informativos: X

## Hallazgos

### [SEC-001] [Título] — CRÍTICO
**Descripción:** ...
**Evidencia:** [archivo:línea o screenshot]
**Normativa:** ENS [control] / OWASP [A0X]
**Impacto:** ...
**Remediación:** ...
**Plazo:** 72h (ENS Alto) / 7 días (ENS Medio)
```

## Salida Esperada
### Estructura del Informe (gap analysis estratégico)
```markdown
# Informe de Cumplimiento ENS — [Nombre del Sistema]
> Nivel: [básica/media/alta] | Fecha: [YYYY-MM-DD] | Autor: Security Architect Agent

## 1. Alcance y Clasificación
## 2. Dimensiones Evaluadas
## 3. Matriz de Cumplimiento
| ID ENS | Requisito | Dimensión | Estado | Evidencia | Gap | Medida Propuesta | Plazo |
## 4. Resumen de Gaps
## 5. Plan de Remediación
## 6. Trazabilidad a OWASP / ISO 27001 (si aplica)
## 7. Recomendaciones
## 8. Evidencia y Metadatos
```

## Criterios de Calidad
- [ ] Todos los requisitos obligatorios para el nivel indicado están evaluados.
- [ ] Cada `no_aplica` tiene justificación técnica documentada.
- [ ] 100% de gaps tienen medida de remediación con plazo y responsable sugerido.
- [ ] Trazabilidad cruzada con OWASP ASVS cuando el sistema es web/API.
- [ ] El informe es revisable por un auditor ENS sin intervención del agente.
- [ ] Si es auditoría operativa táctica: checklist de controles ENS cubiertos/pendientes incluido.

## Stack y Tecnologías
- Marco de referencia: ENS (Real Decreto 311/2022, actualizado)
- Dimensiones: op (organización), mp.sw (medidas de protección software), mp.hw (hardware), mp.com (comunicaciones), mp.info (información)
- OWASP Top 10 (para cruce en auditoría operativa táctica)
- Formatos: Markdown, DOCX vía plantilla corporativa

## Dependencias
- `apb-sec-threat-model-v1.0` — para análisis de amenazas previo
- `apb-sec-owasp-v1.0` — para mapeo cruzado con controles OWASP
- `apb-gov-evidence-v1.0` — para generación de evidencia
- `apb-gov-policy-check-v1.0` — para validación de políticas
- `apb-qa-anonymize-v1.0` — cuando `processes_personal_data` está activo, para cruce con RGPD

## Ejemplo de Uso
**Prompt de invocación (gap analysis estratégico):**
```
Evalúa el cumplimiento ENS para nuestro sistema de gestión de expedientes:
- Categoría: sistema de información
- Nivel: media
- Arquitectura: monolito .NET + Azure SQL + Azure Service Bus
- Autenticación: Azure AD (OAuth2/OIDC)
- Datos: información personal de ciudadanos (LOPD/GDPR)
- Controles existentes: cifrado en reposo, backups diarios, WAF en API Gateway
```

**Prompt de invocación (auditoría operativa táctica):**
```
Audita el código de PaymentController.cs antes del release v2.3:
- Nivel ENS: Alto
- Procesa datos personales: Sí
- Genera informe de hallazgos con severidad y plazo de remediación
```

## Notas y Advertencias
- **Nivel 1**: El agente evalua cumplimiento documental y arquitectónico, no realiza pruebas técnicas de intrusión.
- **Revisión humana obligatoria** antes de presentar el informe a auditoría.
- La normativa ENS puede actualizarse; el agente usa la versión vigente a fecha de generación.
- Los requisitos ENS de nivel Alto incluyen controles adicionales de criptografía, separación de roles y trazabilidad avanzada.

## Historial de Cambios
| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-20 | Arquitectura APB | Creación inicial |
| 1.1.0 | 2026-06-24 | Arquitectura APB | Fusión con `apb-ens-security-audit` (apb-ai-skills): tablas operativas de controles por nivel, cruce OWASP, formato de informe de hallazgos con severidad |

> **Generado por IA:** Claude (Anthropic), Sesión QA del plan de remediación APB-IA-FRAMEWORK.
> **Validado por humano:** _pendiente — completar nombre/rol del validador antes de pasar a `candidate`._
