---
id: "apb-gov-tech-radar-v1.0"
name: "Radar Tecnológico APB"
description: "Genera y mantiene el Radar Tecnológico de APB siguiendo el formato ThoughtWorks. Clasifica tecnologías del stack en cuatro anillos (Adoptar, Probar, Evaluar, Descartar) y cuatro cuadrantes (Lenguajes/Frameworks, Plataformas, Herramientas, Técnicas). Soporta decisiones de adquisición tecnológica y deuda técnica."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "governance"
autonomy_level: 1
created_date: "2026-06-29"
review_date: "2026-12-29"
---

# Radar Tecnológico APB

## Propósito
Proporcionar una visión estructurada del estado tecnológico de APB usando el formato del Radar Tecnológico de ThoughtWorks. Ayuda a Arquitectura APB a comunicar las decisiones tecnológicas, identificar tecnologías a adoptar o descartar, detectar deuda técnica emergente y orientar las decisiones de contratación y formación del equipo.

## Contexto de Uso
- Actualización semestral del radar tecnológico APB.
- Evaluación de una nueva tecnología para decidir si merece entrar en el radar.
- Preparación de documentación para una decisión de arquitectura que involucra tecnologías nuevas.
- Onboarding de nuevos desarrolladores: qué tecnologías están en uso y cuáles están descartadas.
- Input para el plan de formación del equipo.

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `operation` | Enum | `generar-radar` / `evaluar-tecnologia` / `actualizar-entrada` | ✅ |
| `technology_name` | Texto | Nombre de la tecnología a evaluar o actualizar (para `evaluar-tecnologia`) | Condicional |
| `current_radar` | JSON/Markdown | Estado actual del radar (para `actualizar-entrada`) | Condicional |
| `context` | Texto | Contexto de uso en APB: qué sistemas lo usan, desde cuándo, experiencia del equipo | ❌ |

## Cuadrantes del Radar APB

| Cuadrante | Qué incluye |
|---|---|
| **Lenguajes y Frameworks** | C#/.NET, Python, Django, TypeScript, SQL, Bicep, Terraform |
| **Plataformas** | Azure (AKS, Service Bus, Key Vault, etc.), PostgreSQL, Cosmos DB, Azure SQL, GitHub Actions |
| **Herramientas** | Jenkins, DevExpress/DevExtreme, Playwright, k6, SonarQube, Dependabot |
| **Técnicas** | API-first, C4 Model, DDD, CI/CD GitOps, DPIA, RBAC, Zero-trust |

## Anillos del Radar

| Anillo | Significado para APB |
|---|---|
| **Adoptar** | Usar con confianza en producción. Elección por defecto para nuevos proyectos. |
| **Probar** | Viable para usar en proyectos específicos. Adquirir experiencia controlada. |
| **Evaluar** | Vale la pena investigar, pero sin uso en producción todavía. |
| **Descartar** | No usar en proyectos nuevos. Migrar fuera en proyectos existentes. |

## Flujo de Trabajo

### Operación: generar-radar

1. Listar el stack tecnológico APB completo por cuadrante.
2. Asignar anillo a cada tecnología según criterios:
   - **Adoptar**: uso extendido en APB, equipo experimentado, soporte a largo plazo confirmado.
   - **Probar**: 1-2 proyectos piloto con buenos resultados, documentación disponible.
   - **Evaluar**: PoC o exploración en curso, sin proyectos de producción.
   - **Descartar**: tecnología legacy, fin de vida, sustituida por alternativa en Adoptar.
3. Añadir nota de cambio si la tecnología ha cambiado de anillo respecto a la edición anterior.
4. Identificar las 3-5 "señales de cambio" del semestre: tecnologías que merecen atención especial.

### Operación: evaluar-tecnologia

1. Analizar la tecnología propuesta:
   - Madurez: ¿está en producción en empresas similares? ¿Tiene versión LTS?
   - Compatibilidad: ¿encaja con el stack APB (.NET, Azure, PostgreSQL)?
   - Seguridad: ¿tiene track record de vulnerabilidades gestionadas?
   - Licencia: ¿es compatible con uso en sector público?
   - Soporte: ¿hay proveedor con SLA o comunidad activa?
2. Proponer anillo de entrada y justificación.
3. Identificar tecnologías actuales que podría sustituir.

### ⚠️ CHECKPOINT HUMANO
El Comité de Arquitectura APB debe aprobar los cambios de anillo en el radar antes de publicarlo.

## Salida Esperada

```markdown
# Radar Tecnológico APB — Edición [Semestre/Año]
> ⚠️ Borrador generado por IA (APB AI Framework - apb-gov-tech-radar-v1.0) — pendiente validación del Comité de Arquitectura APB.

## Señales de cambio este semestre
1. [Tecnología X]: sube de Probar a Adoptar — justificación
2. [Tecnología Y]: baja de Adoptar a Descartar — justificación

## Cuadrante: Lenguajes y Frameworks
| Tecnología | Anillo | Cambio | Notas |
|---|---|---|---|
| .NET 8 / C# | Adoptar | → | Plataforma principal APB |
| Python 3.12 | Adoptar | → | Backend Django/GeoDjango |
| ...

## Cuadrante: Plataformas
[...]

## Cuadrante: Herramientas
[...]

## Cuadrante: Técnicas
[...]
```

## Estado Actual del Stack APB (referencia)

**Adoptar**: .NET 8, C#, Python 3.12, Django/DRF, GeoDjango, TypeScript, Azure AKS, PostgreSQL/PostGIS, Azure SQL, Azure Service Bus, Azure Key Vault, GitHub Actions, Playwright, WCAG 2.1 AA, C4 Model, API-first design, RBAC, ENS compliance.

**Probar**: Bicep/Terraform IaC, Cosmos DB, k6 load testing, Pact contract testing, AI-assisted development (APB AI Framework), Zero-trust networking.

**Evaluar**: Azure Container Apps, Semantic Kernel, Vector databases para RAG, OpenTelemetry, FinOps practices.

**Descartar**: .NET Framework <6, jQuery, WCF, SOAP/XML-RPC, Jenkins para nuevos proyectos (migrar a GitHub Actions), On-premise bare metal para nuevos sistemas.

## Criterios de Calidad
- [ ] Cada tecnología en el radar tiene justificación de su anillo asignado.
- [ ] Las tecnologías en "Descartar" tienen plan de migración o fecha límite de uso.
- [ ] La edición del radar está fechada y versionada.
- [ ] Los cambios de anillo respecto a la edición anterior están marcados explícitamente.

## Dependencias
- `apb-gov-vendor-eval-v1.0` — la evaluación de proveedores alimenta las entradas de Plataformas
- `apb-disc-tech-eval-v1.0` — la evaluación técnica de tecnologías precede a la entrada en el radar

## Ejemplo de Uso

```
Evalúa la tecnología Azure Container Apps para el radar APB.
Actualmente usamos AKS. ¿Merece entrar en el radar y en qué anillo?
Contexto: estamos analizando si simplificar la capa de orquestación para servicios pequeños.
```

## Notas y Advertencias
- El radar es una herramienta de comunicación, no una normativa — las excepciones justificadas son válidas, pero deben documentarse.
- Las tecnologías en "Descartar" NO implican que deban migrarse inmediatamente — depende del riesgo y coste de la migración.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento B |

## ⚠️ Comportamiento ante inputs incompletos

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `operation` | Pregunta: "¿Quieres generar el radar completo, evaluar una tecnología concreta o actualizar una entrada?" | Sí |
| `technology_name` | Solo requerido para `evaluar-tecnologia` — pregunta el nombre si falta en ese caso | Condicional |
| `current_radar` | Genera radar desde el estado de referencia documentado en esta skill | No |
| `context` | Genera evaluación con información general del stack APB; indica qué contexto adicional mejoraría el análisis | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** — callout inmediatamente tras el título H1:
  > ⚠️ Borrador generado por IA (APB AI Framework - apb-gov-tech-radar-v1.0) — pendiente validación del Comité de Arquitectura APB.
