---
id: "apb-doc-manual-v1.0"
name: "Generación de Manual del Sistema"
description: "Generar manuales de sistema completos orientados a usuarios finales, administradores y equipos de soporte. Incluye guías de uso, procedimientos, troubleshooting, FAQ y referencia de funcionalidades, adaptado al contexto de negocio de APB."
version: "1.0.0"
status: "draft"
owner: "Análisis Funcional APB <arquitectura@portdebarcelona.cat>"
domain: "documentation"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Generación de Manual del Sistema

## Propósito
Generar manuales de sistema completos orientados a usuarios finales, administradores y equipos de soporte. Incluye guías de uso, procedimientos, troubleshooting, FAQ y referencia de funcionalidades, adaptado al contexto de negocio de APB.

## Contexto de Uso
- Entrega de manuales de usuario para nuevos sistemas.
- Actualización de manuales tras cambios funcionales significativos.
- Generación de guías de administración para equipos de soporte.
- Integración con gobierno y gestión de conocimiento.

## Entradas Requeridas
| Entrada | Tipo | Descripción | Obligatorio |
|---------|------|-------------|-------------|
| `system_description` | Texto / Markdown | Descripción funcional del sistema | ✅ |
| `user_roles` | Lista | Roles de usuario y permisos | ✅ |
| `features` | Lista | Funcionalidades principales con descripción | ✅ |
| `screenshots` | Lista | Descripciones de pantallas o flujos (texto) | ❌ |
| `procedures` | Lista | Procedimientos de uso común | ❌ |
| `target_audience` | Enum | `end-user`, `admin`, `support`, `all` | ✅ |

## Flujo de Trabajo (Pasos)
1. **Análisis de audiencia**: Determinar nivel de detalle y lenguaje según target audience.
2. **Estructuración del manual**:
   - **Introducción**: Propósito del sistema, audiencia, convenciones.
   - **Guía de inicio rápido**: Primeros pasos para usuarios nuevos.
   - **Funcionalidades por rol**: Descripción de features accesibles por cada rol.
   - **Procedimientos detallados**: Paso a paso para tareas comunes.
   - **Troubleshooting**: Problemas comunes y soluciones.
   - **FAQ**: Preguntas frecuentes.
   - **Glosario**: Términos técnicos y de negocio.
   - **Anexos**: Referencias, enlaces, contactos de soporte.
3. **Generación de contenido**: Redactar secciones con lenguaje claro y estructurado.
4. **Validación de completitud**: Verificar que todas las funcionalidades están documentadas.
5. **Control de calidad**: Revisar coherencia, ausencia de ambigüedades y formato.
6. **Generación de índice y navegación**: Tabla de contenidos, enlaces internos, referencias cruzadas.
7. **Registro de evidencia**: Metadatos para gobierno.

## Salida Esperada
### Estructura del Manual
```markdown
# Manual del Sistema — [Nombre Sistema]
> Versión: [X.Y.Z] | Fecha: [YYYY-MM-DD] | Audiencia: [target_audience]
> Autor: Documentation Agent | Revisado por: [Analista Funcional]

## Tabla de Contenidos
## 1. Introducción
## 2. Guía de Inicio Rápido
## 3. Funcionalidades
### 3.1 [Feature 1]
### 3.2 [Feature 2]
## 4. Procedimientos
## 5. Troubleshooting
## 6. FAQ
## 7. Glosario
## 8. Anexos
## 9. Evidencia y Metadatos
```

## Criterios de Calidad
- [ ] Todas las funcionalidades del sistema están documentadas.
- [ ] Cada procedimiento tiene pasos numerados, verificaciones y resultados esperados.
- [ ] El lenguaje es apropiado para la audiencia target (técnico vs usuario final).
- [ ] El troubleshooting cubre al menos los 5 problemas más comunes.
- [ ] El manual tiene índice navegable y referencias cruzadas.
- [ ] No se incluyen secretos, credenciales ni datos sensibles de producción.
- [ ] El manual es revisable por el equipo de soporte sin intervención del agente.

## Stack y Tecnologías
- Formatos: Markdown, PDF vía pandoc, DOCX vía plantilla
- Diagramas: Mermaid para flujos, placeholders para screenshots
- Herramientas: MkDocs, Docusaurus para publicación web

## Dependencias
- `apb-disc-spec-gen-v1.0` — para especificaciones funcionales
- `apb-gov-evidence-v1.0` — para evidencia documental
- `apb-gov-knowledge-v1.0` — para registro en base de conocimiento

## Ejemplo de Uso
**Prompt de invocación:**
```
Genera el manual de usuario para el sistema de gestión de expedientes:
- Audiencia: end-user (funcionarios públicos)
- Roles: Solicitante, Revisor, Administrador
- Features: Crear expediente, Adjuntar documentos, Seguimiento de estado, Notificaciones, Informes
- Procedimientos: Alta de nuevo expediente, Resolución de expediente, Generación de informe mensual
- Idioma: español
```

## Notas y Advertencias
- **Nivel 1**: El agente genera contenido textual; no captura screenshots ni accede a entornos reales.
- **Revisión humana obligatoria** antes de publicar como manual oficial.
- Los screenshots deben añadirse manualmente desde el entorno real.
- El manual debe actualizarse con cada release que incluya cambios funcionales.
- El agente no tiene acceso a datos de producción; los ejemplos son ilustrativos.

## Historial de Cambios
| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-20 | Arquitectura APB | Creación inicial |
