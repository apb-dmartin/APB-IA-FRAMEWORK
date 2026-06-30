---
id: "apb-disc-cosmic-v1.0"
name: "Estimación COSMIC Function Points"
description: "Estimar el tamaño funcional de software utilizando el método COSMIC (ISO/IEC 19761), proporcionando métricas objetivas para planificación, benchmarking y gestión de proyectos."
version: "1.0.0"
status: "draft"
owner: "Análisis Funcional <arquitectura@portdebarcelona.cat>"
domain: "discovery"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# Estimación COSMIC Function Points


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

---

## 🎯 Propósito

Estimar el tamaño funcional de software utilizando el método COSMIC (ISO/IEC 19761), proporcionando métricas objetivas para planificación, benchmarking y gestión de proyectos.

---

## ⚡ Trigger

Al inicio de un proyecto para estimar esfuerzo, al comparar productividad entre equipos, o cuando se requiere una métrica estándar de tamaño funcional.

---

## 📥 Input

- Especificación funcional detallada
- Modelo de datos identificado
- Flujos de datos funcionales
- Alcance del software a medir

---

## 📤 Output

- Tamaño funcional en COSMIC Function Points (CFP)
- Desglose por proceso funcional
- Matriz de movimientos de datos (E, X, R, W)
- Informe de medición con trazabilidad
- Comparativa con proyectos anteriores (si disponible)

---

## 🔄 Proceso

1. **Identificación de proceso funcional**: Un proceso funcional es un conjunto de datos procesados de forma cohesiva, iniciado por un evento.
2. **Identificación de subprocesos**: Dividir el proceso en subprocesos elementales.
3. **Identificación de movimientos de datos**:
   - E (Entry): Movimiento de datos desde usuario/sistema hacia el software medido.
   - X (Exit): Movimiento de datos desde el software medido hacia usuario/sistema.
   - R (Read): Movimiento de datos desde persistent storage hacia el software.
   - W (Write): Movimiento de datos desde el software hacia persistent storage.
4. **Conteo**: Cada movimiento de datos = 1 CFP. Sumar por subproceso y proceso funcional.
5. **Agregación**: Total CFP = suma de todos los procesos funcionales.
6. **Documentación**: Registrar cada movimiento con su justificación.
7. **Validación**: Revisar con otro medidor COSMIC (si disponible) para calibración.

---

## 📋 Reglas y Constraints

- Seguir estándar COSMIC ISO/IEC 19761 rigurosamente.
- Un movimiento de datos se cuenta una vez por proceso funcional, independientemente de la complejidad del dato.
- No contar movimientos técnicos (logs, configuración, mensajes de error genéricos) salvo que sean requisito funcional explícito.
- Documentar supuestos de medición explícitamente.
- La medición debe ser repetible; otro medidor debe llegar al mismo resultado.
- Usar CFP para estimar esfuerzo solo con histórico de productividad del equipo (CFP/persona-día).
- No comparar CFP entre proyectos con contextos muy diferentes sin ajustar.

---

## 🛠 Stack Tecnológico Relevante

- Estándar COSMIC ISO/IEC 19761
- Plantilla de medición APB
- Excel / herramienta de medición
- Especificación funcional

---

## 💡 Ejemplos de Uso

**Ejemplo — Proceso 'Crear Pedido':**
> Subprocesos:
> 1. Validar cliente: Entry (datos cliente) + Read (cliente de BBDD) = 2 CFP
> 2. Validar productos: Entry (líneas de pedido) + Read (productos de BBDD) = 2 CFP
> 3. Calcular total: Read (precios de BBDD) = 1 CFP
> 4. Guardar pedido: Write (pedido a BBDD) + Exit (confirmación) = 2 CFP
> Total proceso: 7 CFP
> Si hay 10 procesos funcionales similares → ~70 CFP total.

---

## 🔗 Dependencias

- `apb-disc-spec-gen-v1.0`
- `apb-disc-enrich-req-v1.0`

---

## 📝 Notas

- COSMIC es más adecuado para software orientado a eventos y microservicios que FP tradicional.
- Requiere formación específica; los resultados mejoran con la experiencia del medidor.
- Usar como métrica de tamaño, no como única base de estimación de esfuerzo.

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `Especificación funcional detallada` | Pregunta: "¿Puedes proporcionar especificación funcional detallada?" | Sí |
| `Modelo de datos identificado` | Pregunta: "¿Puedes proporcionar modelo de datos identificado?" | Sí |
| `Flujos de datos funcionales` | Pregunta: "¿Puedes proporcionar flujos de datos funcionales?" | Sí |
| `Alcance del software a medir` | Pregunta: "¿Puedes proporcionar alcance del software a medir?" | Sí |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-disc-cosmic-v1.0) - pendiente validacion humana. No distribuir sin revision.
