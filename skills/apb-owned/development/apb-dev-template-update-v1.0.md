---
id: "apb-dev-template-update-v1.0"
name: "Cambio de Plantilla Visual Studio"
description: "Actualizar proyectos .NET existentes a nuevas plantillas corporativas de Visual Studio, incluyendo estructura de carpetas, paquetes NuGet, configuraciones y estándares de código."
version: "1.0.0"
status: "draft"
owner: "Desarrollo <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Cambio de Plantilla Visual Studio

---

## 🎯 Propósito

Actualizar proyectos .NET existentes a nuevas plantillas corporativas de Visual Studio, incluyendo estructura de carpetas, paquetes NuGet, configuraciones y estándares de código.

---

## ⚡ Trigger

Cuando se actualiza la plantilla corporativa, o cuando un proyecto legacy necesita alinearse con estándares actuales.

---

## 📥 Input

- Proyecto existente a actualizar
- Nueva plantilla corporativa
- Lista de cambios entre versiones de plantilla
- Reglas de migración (breaking changes, deprecaciones)

---

## 📤 Output

- Proyecto actualizado con nueva plantilla
- Reporte de cambios aplicados
- Lista de conflictos manuales pendientes
- Instrucciones de validación post-migración

---

## 🔄 Proceso

1. **Análisis de diferencias**: Comparar proyecto actual vs nueva plantilla. Identificar gaps.
2. **Backup**: Crear rama de migración, backup del proyecto original.
3. **Actualización de estructura**: Ajustar carpetas, archivos de solución, proyectos.
4. **Actualización de paquetes**: Actualizar NuGet packages, resolver conflictos de versiones.
5. **Actualización de configuración**: appsettings, launchSettings, Dockerfile, pipelines.
6. **Aplicación de estándares**: Formato de código, analyzers, editorconfig.
7. **Compilación**: Resolver errores de compilación.
8. **Tests**: Ejecutar tests existentes, verificar que pasan.
9. **Documentación**: Registrar cambios, breaking changes, acciones manuales requeridas.

---

## 📋 Reglas y Constraints

- Siempre trabajar en rama dedicada; nunca en main/develop directamente.
- Mantener compatibilidad backward cuando sea posible.
- Documentar todos los breaking changes con instrucciones de migración.
- No eliminar funcionalidad sin confirmar que no se usa.
- Validar en entorno de staging antes de mergear.
- Actualizar documentación del proyecto (README, ADRs).

---

## 🛠 Stack Tecnológico Relevante

- Visual Studio 2022
- .NET CLI
- NuGet
- Git
- Azure DevOps / GitHub Actions

---

## 💡 Ejemplos de Uso

**Ejemplo — Actualización a plantilla v2.0:**
> Cambios: Nuevo proyecto de tests de integración, paquetes actualizados (EF Core 8 → 9), nuevo editorconfig.
> Proceso: Branch feature/template-v2, aplicar cambios, resolver 3 conflictos de namespace, ejecutar 150 tests (todo verde).
> Merge a develop tras validación en staging.

---

## 🔗 Dependencias

- `apb-dev-micro-base-v1.0

---

## 📝 Notas

- Automatizar cuando sea posible con scripts de migración.
- Mantener changelog de plantillas para facilitar futuras actualizaciones.

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `Proyecto existente a actualizar` | Pregunta: "¿Puedes proporcionar proyecto existente a actualizar?" | Sí |
| `Nueva plantilla corporativa` | Pregunta: "¿Puedes proporcionar nueva plantilla corporativa?" | Sí |
| `Lista de cambios entre versiones de plantilla` | Pregunta: "¿Puedes proporcionar lista de cambios entre versiones de plantilla?" | Sí |
| `Reglas de migración` | Pregunta: "¿Puedes proporcionar reglas de migración?" | Sí |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Codigo generado** - primera linea del bloque: `// [IA-GEN] Generado por APB AI Framework (apb-dev-template-update-v1.0) - pendiente revision humana`
- **Commit** - prefijo `[ai-gen]` en el mensaje + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`
- **PR asociado** - label `ai-generated` en GitHub + footer en descripcion del PR
