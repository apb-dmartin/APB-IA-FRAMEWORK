---
id: "apb-dev-devexpress-front-v1.0"
name: "Desarrollo Frontend DevExpress"
description: "Desarrollar interfaces de usuario con DevExpress/DevExtreme usando JavaScript puro, siguiendo estándares corporativos de APB. Incluye grids, formularios, dashboards y componentes personalizados."
version: "1.0.0"
status: "draft"
owner: "Desarrollo <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# Desarrollo Frontend DevExpress


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

---

## 🎯 Propósito

Desarrollar interfaces de usuario con DevExpress/DevExtreme usando JavaScript puro, siguiendo estándares corporativos de APB. Incluye grids, formularios, dashboards y componentes personalizados.

---

## ⚡ Trigger

Cuando se requiere implementar o modificar una interfaz de usuario en aplicaciones que utilizan DevExpress como framework UI corporativo.

---

## 📥 Input

- Mockup estructurado de `apb-agent-ux-mockup-v1.0` (canal preferido: ya incluye selección de componentes validada)
- O especificación de UI equivalente (diseño funcional, wireframe, ticket Jira)
- Datos y esquemas de API asociados
- Estándares de diseño corporativos
- Plantillas de proyecto DevExpress disponibles

---

## 📤 Output

- Código JavaScript de componentes DevExtreme
- Templates HTML asociados
- Configuración de DataSource
- Tests de UI (si aplica)
- Documentación de componentes personalizados

---

## 🔄 Proceso

1. **Análisis de requisitos UI**: Entender flujo de usuario, validaciones, estados. Si el input es un mockup de `apb-agent-ux-mockup-v1.0`, la selección de componentes ya está hecha — pasar directamente al paso 3.
2. **Selección de componentes**: Si no hay mockup previo, usar `apb-dev-devexpress-selector-v1.0` para elegir el componente correcto antes de implementar (DataGrid, Form, Chart, etc.).
3. **Configuración de DataSource**: Definir origen de datos (API REST, array local, OData).
4. **Implementación**: Desarrollar componente con JavaScript puro, sin frameworks adicionales.
5. **Validaciones**: Implementar validaciones client-side y server-side.
6. **Estilos**: Aplicar tema corporativo, responsive design.
7. **Testing**: Verificar en navegadores soportados, validar accesibilidad básica.
8. **Documentación**: Documentar props, eventos y uso del componente.

---

## 📋 Reglas y Constraints

- Usar JavaScript puro (ES6+); no introducir React, Vue ni Angular sin aprobación de Arquitectura.
- No TypeScript; el stack corporativo usa JavaScript puro para frontend DevExpress.
- Separar lógica de presentación; no mezclar business logic en event handlers.
- Manejar errores de API de forma graceful (mensajes al usuario, estados de carga).
- Optimizar rendimiento: virtual scrolling para grids grandes, lazy loading.
- Seguir guía de estilo corporativa para colores, tipografía, espaciado.
- Accessible: ARIA labels, navegación por teclado, contraste de colores.

---

## 🛠 Stack Tecnológico Relevante

- DevExtreme (JavaScript) — componentes: https://js.devexpress.com/jQuery/Demos/WidgetsGallery/
- jQuery (si requerido por versión legacy)
- HTML5, CSS3
- REST APIs
- Azure CDN (assets estáticos)
- Tema corporativo basado en Generic Light: https://devexpress.github.io/ThemeBuilder/master/generic/light

---

## 💡 Ejemplos de Uso

**Ejemplo 1 — Grid de pedidos:**
> DataGrid con virtual scrolling, filtros, sorting, export a Excel.
> DataSource: REST API /api/v1/orders con paginación server-side.
> Custom column: Estado con color-coded badges.

**Ejemplo 2 — Formulario de alta:**
> Form con validaciones: email (regex), teléfono (formato), campos obligatorios.
> Submit vía AJAX POST, manejo de errores 400/500 con mensajes traducidos.

---

## 🔗 Dependencias

- `apb-dev-devexpress-selector-v1.0` (predecesor cuando no hay mockup funcional)
- `apb-dev-implement-v1.0`
- `apb-dev-api-standard-v1.0`
- `apb-sub-dev-devexpress-v1.0`

---

## 📝 Notas

- DevExpress es el stack corporativo aprobado para aplicaciones administrativas.
- Para proyectos nuevos, evaluar migración a Blazor (subagente correspondiente).
- Mantener compatibilidad con versiones LTS de DevExtreme.

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `Mockup estructurado de `apb-agent-ux-mockup-v1.0`` | Pregunta: "¿Puedes proporcionar mockup estructurado de `apb-agent-ux-mockup-v1.0`?" | Sí |
| `O especificación de UI equivalente` | Pregunta: "¿Puedes proporcionar o especificación de ui equivalente?" | Sí |
| `Datos y esquemas de API asociados` | Pregunta: "¿Puedes proporcionar datos y esquemas de api asociados?" | Sí |
| `Estándares de diseño corporativos` | Pregunta: "¿Puedes proporcionar estándares de diseño corporativos?" | Sí |
| `Plantillas de proyecto DevExpress disponibles` | Pregunta: "¿Puedes proporcionar plantillas de proyecto devexpress disponibles?" | Sí |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Codigo generado** - primera linea del bloque: `// [IA-GEN] Generado por APB AI Framework (apb-dev-devexpress-front-v1.0) - pendiente revision humana`
- **Commit** - prefijo `[ai-gen]` en el mensaje + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`
- **PR asociado** - label `ai-generated` en GitHub + footer en descripcion del PR
