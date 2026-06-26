---
id: "apb-sec-owasp-v1.0"
name: "Requisitos OWASP"
description: "Evaluar aplicaciones web, APIs y servicios contra los requisitos del OWASP Application Security Verification Standard (ASVS). Genera un informe de verificación con nivel de cumplimiento, gaps identificados y recomendaciones de remediación priorizadas."
version: "1.0.0"
status: "draft"
owner: "Ciberseguridad APB <arquitectura@portdebarcelona.cat>"
domain: "security"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Requisitos OWASP

## Propósito
Evaluar aplicaciones web, APIs y servicios contra los requisitos del OWASP Application Security Verification Standard (ASVS). Genera un informe de verificación con nivel de cumplimiento, gaps identificados y recomendaciones de remediación priorizadas.

## Contexto de Uso
- Diseño y desarrollo de aplicaciones web/APIs con requisitos de seguridad definidos.
- Revisiones de código y arquitectura orientadas a seguridad.
- Preparación para auditorías de seguridad de aplicaciones.
- Integración con pipelines de CI/CD para validación de seguridad (shift-left).

## Entradas Requeridas
| Entrada | Tipo | Descripción | Obligatorio |
|---------|------|-------------|-------------|
| `application_description` | Texto / Markdown | Descripción de la aplicación, tecnologías y alcance | ✅ |
| `asvs_level` | Enum | `1` (oportunista), `2` (estándar), `3` (avanzado) | ✅ |
| `architecture_type` | Enum | `web`, `api`, `mobile`, `desktop` | ✅ |
| `code_samples` | Código / Texto | Fragmentos de código críticos (autenticación, autorización, validación de entrada) | ❌ |
| `existing_security_tests` | Lista | Resultados de SAST/DAST/SCA previos | ❌ |

## Flujo de Trabajo (Pasos)
1. **Selección de requisitos ASVS**: Filtrar requisitos aplicables según `asvs_level` y `architecture_type`.
2. **Evaluación por categoría**: Revisar cada una de las 14 categorías ASVS:
   - V1: Arquitectura, Diseño y Modelado de Amenazas
   - V2: Autenticación
   - V3: Gestión de Sesiones
   - V4: Control de Acceso
   - V5: Validación, Sanitización y Codificación
   - V6: Criptografía Almacenada
   - V7: Errores, Logging y Monitoreo
   - V8: Protección de Datos
   - V9: Comunicaciones
   - V10: Código Malicioso
   - V11: Lógica de Negocio
   - V12: Archivos y Recursos
   - V13: API y Web Service
   - V14: Configuración
3. **Verificación de cumplimiento**: Para cada requisito, determinar estado:
   - `cumple` — Implementado y verificable.
   - `parcial` — Implementado parcialmente.
   - `no_cumple` — No implementado.
   - `no_verificado` — No se dispone de evidencia de verificación.
4. **Análisis de gaps**: Identificar requisitos no cumplidos que representan riesgo significativo.
5. **Recomendaciones de remediación**: Proporcionar guías específicas de implementación con ejemplos de código seguro cuando aplique.
6. **Generación de informe**: Documento estructurado con puntuación ASVS, heatmap de cumplimiento y plan de acción.
7. **Integración con gobierno**: Metadatos para trazabilidad y evidencia.

## Salida Esperada
### Estructura del Informe
```markdown
# Informe OWASP ASVS — [Nombre de Aplicación]
> Nivel: [1/2/3] | Fecha: [YYYY-MM-DD] | Autor: Security Architect Agent

## 1. Alcance y Contexto
## 2. Resumen Ejecutivo
## 3. Puntuación ASVS
| Categoría | Total | Cumple | Parcial | No Cumple | % Cumplimiento |
## 4. Detalle por Categoría
### V2: Autenticación
| ID | Requisito | Nivel | Estado | Evidencia | Recomendación |
## 5. Gaps Críticos
## 6. Plan de Remediación
## 7. Ejemplos de Código Seguro
## 8. Trazabilidad a ENS / ISO 27001
## 9. Evidencia y Metadatos
```

## Criterios de Calidad
- [ ] Todos los requisitos del nivel seleccionado están evaluados.
- [ ] Cada gap crítico tiene recomendación específica con ejemplo de implementación.
- [ ] El informe incluye puntuación porcentual de cumplimiento por categoría.
- [ ] Trazabilidad cruzada con ENS cuando el sistema está en ámbito español.
- [ ] Ejemplos de código seguro validados contra el stack tecnológico de APB (.NET, JavaScript).

## Stack y Tecnologías
- Marco de referencia: OWASP ASVS 4.0 (o versión vigente)
- Complementarios: OWASP Top 10, OWASP Testing Guide, OWASP Cheat Sheets
- Formatos: Markdown, integración con SonarQube para seguimiento de issues

## Dependencias
- `apb-sec-threat-model-v1.0` — para contexto de amenazas previo
- `apb-sec-ens-v1.0` — para mapeo cruzado con controles ENS
- `apb-dev-sonar-clean-v1.0` — para integración con análisis estático de calidad
- `apb-gov-evidence-v1.0` — para generación de evidencia

## Ejemplo de Uso
**Prompt de invocación:**
```
Evalúa nuestro API REST de gestión de usuarios contra OWASP ASVS Nivel 2:
- Stack: ASP.NET Core 8, Entity Framework, Azure SQL
- Autenticación: JWT con refresh tokens
- Autorización: RBAC basado en claims
- Endpoints críticos: /api/auth, /api/users, /api/roles
- Código de autenticación: [pegar fragmento]
```

## Notas y Advertencias
- **Nivel 1**: El agente realiza análisis documental y de código estático; no ejecuta pruebas dinámicas (DAST).
- **Revisión humana obligatoria** para requisitos de Nivel 3 y gaps críticos.
- Los ejemplos de código seguro son orientativos; deben adaptarse al contexto específico.
- ASVS se actualiza periódicamente; el agente indica la versión de referencia utilizada.

## Historial de Cambios
| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-20 | Arquitectura APB | Creación inicial |


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-sec-owasp-v1.0) - pendiente validacion humana. No distribuir sin revision.
