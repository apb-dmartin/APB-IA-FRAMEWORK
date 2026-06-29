---
id: "apb-dev-legacy-mapper-v1.0"
name: "Mapper Legacy → Moderno"
description: "Diseñar e implementar mapeadores que traduzcan datos y comportamientos entre sistemas legacy y modernos. Facilita la migración gradual minimizando el impacto en operaciones."
version: "1.0.0"
status: "draft"
owner: "Desarrollo <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Mapper Legacy → Moderno

---

## 🎯 Propósito

Diseñar e implementar mapeadores que traduzcan datos y comportamientos entre sistemas legacy y modernos. Facilita la migración gradual minimizando el impacto en operaciones.

---

## ⚡ Trigger

Durante la modernización de un sistema legacy que debe coexistir con el nuevo sistema durante un período de transición.

---

## 📥 Input

- Modelo de datos legacy
- Modelo de datos moderno
- Reglas de negocio legacy
- Puntos de integración identificados
- Estrategia de migración (big bang, strangler fig, etc.)

---

## 📤 Output

- Clases/funciones de mapeo
- Tests de mapeo (bidireccional si aplica)
- Documentación de discrepancias entre modelos
- Estrategia de sincronización de datos
- Plan de eliminación del mapper (fase final)

---

## 🔄 Proceso

1. **Análisis de modelos**: Comparar estructuras legacy y moderno. Identificar campos equivalentes, transformaciones necesarias.
2. **Identificación de discrepancias**: Campos sin equivalente, semánticas diferentes, reglas de negocio incompatibles.
3. **Diseño del mapper**: Decidir estrategia (AutoMapper profiles, custom mappers, anti-corruption layer).
4. **Implementación**: Crear mapeos con validación. Manejar casos nulos, defaults, conversiones.
5. **Testing**: Verificar que mapeo preserva integridad de datos. Tests con datos reales anonimizados.
6. **Documentación**: Registrar decisiones de mapeo, campos calculados, asumptions.
7. **Plan de eliminación**: Definir cuándo el mapper ya no será necesario.

---

## 📋 Reglas y Constraints

- El mapper debe ser unidireccional por defecto; bidireccional solo si es estrictamente necesario.
- No propagar deuda técnica legacy al nuevo modelo; documentar y justificar cada compromiso.
- Los mapeos deben ser testeables y tener cobertura 100% (son críticos para migración).
- Documentar campos que no tienen mapeo directo y cómo se resuelven.
- Mantener mapper en capa de infraestructura, no en dominio.
- Planificar eliminación del mapper; no debe ser permanente.

---

## 🛠 Stack Tecnológico Relevante

- AutoMapper / manual mappers
- .NET 8/9
- xUnit, FluentAssertions
- Entity Framework Core (para persistencia)
- Azure Service Bus (para sincronización)

---

## 💡 Ejemplos de Uso

**Ejemplo — Mapeo cliente legacy a moderno:**
> Legacy: Cliente tiene campos Nombre, Apellido1, Apellido2 en tablas separadas.
> Moderno: Cliente tiene FullName calculado.
> Mapper: Concatena Apellido1 + ' ' + Apellido2 + ', ' + Nombre.
> Test: Verifica que 'García, Juan' se mapea correctamente y viceversa.

---

## 🔗 Dependencias

- `apb-arch-decompose-v1.0`
- `apb-disc-reverse-code-v1.0`

---

## 📝 Notas

- El mapper es una solución temporal; su objetivo es desaparecer.
- Para datos complejos, considerar ETL (Azure Data Factory) en lugar de mapeo en código.

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `Modelo de datos legacy` | Pregunta: "¿Puedes proporcionar modelo de datos legacy?" | Sí |
| `Modelo de datos moderno` | Pregunta: "¿Puedes proporcionar modelo de datos moderno?" | Sí |
| `Reglas de negocio legacy` | Pregunta: "¿Puedes proporcionar reglas de negocio legacy?" | Sí |
| `Puntos de integración identificados` | Pregunta: "¿Puedes proporcionar puntos de integración identificados?" | Sí |
| `Estrategia de migración` | Pregunta: "¿Puedes proporcionar estrategia de migración?" | Sí |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Codigo generado** - primera linea del bloque: `// [IA-GEN] Generado por APB AI Framework (apb-dev-legacy-mapper-v1.0) - pendiente revision humana`
- **Commit** - prefijo `[ai-gen]` en el mensaje + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`
- **PR asociado** - label `ai-generated` en GitHub + footer en descripcion del PR
