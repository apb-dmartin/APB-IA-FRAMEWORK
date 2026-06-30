---
id: "apb-arch-decompose-v1.0"
name: "Descomposición Monolito → Microservicios"
description: "Planificar y diseñar la migración gradual de aplicaciones monolíticas a arquitectura de microservicios, minimizando riesgos operativos y maximizando la entrega de valor. Incluye identificación de bounded contexts, estrategias de desacoplamiento y roadmap de transformación."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "architecture"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# Descomposición Monolito → Microservicios


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

---

## 🎯 Propósito

Planificar y diseñar la migración gradual de aplicaciones monolíticas a arquitectura de microservicios, minimizando riesgos operativos y maximizando la entrega de valor. Incluye identificación de bounded contexts, estrategias de desacoplamiento y roadmap de transformación.

---

## ⚡ Trigger

Cuando se decide modernizar una aplicación monolítica legacy, o cuando el monolito actual presenta problemas de escalabilidad, mantenibilidad o time-to-market que justifiquen la descomposición.

---

## 📥 Input

- Código fuente del monolito y su estructura
- Documentación existente (si hay)
- Métricas de uso y dependencias entre módulos
- Mapa de dominio de negocio
- Restricciones de tiempo, presupuesto y riesgo
- Requisitos no funcionales objetivo

---

## 📤 Output

- Análisis de acoplamiento y cohesión del monolito
- Propuesta de bounded contexts y microservicios candidatos
- Estrategia de desacoplamiento (strangler fig, branch by abstraction, anti-corruption layer)
- Roadmap de migración por fases con priorización
- Análisis de riesgos y mitigaciones
- Estimación de esfuerzo por fase

---

## 🔄 Proceso

1. **Análisis estático del código**: Identificar dependencias entre módulos, clases y capas. Usar herramientas de análisis de código (SonarQube, NDepend, dependencia visual).
2. **Identificación de bounded contexts**: Aplicar DDD para mapear dominios y subdominios del negocio sobre el código existente.
3. **Matriz de acoplamiento**: Crear heatmap de dependencias. Identificar 'big balls of mud' y módulos altamente acoplados.
4. **Definición de microservicios candidatos**: Agrupar funcionalidades coherentes. Evaluar tamaño (no demasiado grande ni demasiado pequeño).
5. **Estrategia de extracción**: Seleccionar el primer microservicio a extraer (criterio: alto valor, bajo riesgo, bajo acoplamiento).
6. **Diseño de anti-corruption layer**: Definir cómo el nuevo microservicio se integrará con el monolito durante la transición.
7. **Diseño de datos**: Decidir estrategia de BBDD (compartida temporal, replicación, migración gradual).
8. **Roadmap**: Definir fases, milestones, criterios de éxito por fase.
9. **Validación**: Revisar con stakeholders técnicos y de negocio.

---

## 📋 Reglas y Constraints

- NUNCA realizar 'big bang' migration. Siempre descomposición incremental.
- El primer microservicio extraído debe ser de bajo riesgo y alto valor (quick win).
- Mantener el monolito operativo durante toda la migración; no romper funcionalidad existente.
- La BBDD compartida es aceptable SOLO como estado transitorio; documentar plan de separación.
- Cada microservicio debe tener su propio ciclo de vida independiente (CI/CD, despliegue, escalado).
- Documentar decisiones en ADRs formales.
- Evaluar coste operativo: N microservicios = N pipelines, N monitores, N logs. Justificar ROI.
- No extraer un microservicio sin definir su contrato API y eventos primero.

---

## 🛠 Stack Tecnológico Relevante

- .NET 8/9
- Azure Service Bus (comunicación entre monolito y microservicios)
- Azure API Management (fachada unificada)
- Docker / AKS
- Entity Framework Core (migraciones)
- Terraform / Bicep
- SonarQube (análisis de dependencias)

---

## 💡 Ejemplos de Uso

**Ejemplo 1 — Monolito de gestión de clientes:**
> Módulos: CRM, Facturación, Soporte, Marketing.
> Primera extracción: Módulo de Facturación (alto valor, APIs bien definidas).
> Estrategia: Strangler Fig. API Gateway redirige /api/invoices al nuevo microservicio.
> Anti-corruption layer traduce modelo de datos legacy al nuevo modelo de dominio.

**Ejemplo 2 — Monolito VB6 de nómina:**
> No es viable extraer directamente. Estrategia: Branch by Abstraction.
> Crear fachada .NET que encapsula lógica VB6. Extraer gradualmente casos de uso a .NET.
> Mantener BBDB legacy con vistas/materializadas hasta migración completa.

---

## 🔗 Dependencias

- `apb-disc-ddd-legacy-v1.0` (análisis DDD del legacy)
- `apb-arch-ddd-v1.0` (identificación de dominios)
- `apb-arch-event-driven-v1.0` (comunicación entre servicios)
- `apb-dev-legacy-mapper-v1.0` (mapeo legacy → moderno)
- `apb-wf-legacy-onboarding-v1.0` (workflow completo)
- `prov-azure-v1.0`

---

## 📝 Notas

- La descomposición no es un fin en sí mismo. Si el monolito modular satisface los requisitos, no forzar microservicios.
- Considerar monolito modular (modular monolith) como paso intermedio si la complejidad operativa es alta.
- Métrica de éxito: time-to-deploy del microservicio extraído < 15 minutos.

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `Código fuente del monolito y su estructura` | Pregunta: "¿Puedes proporcionar código fuente del monolito y su estructura?" | Sí |
| `Documentación existente` | Continúa con la información disponible — indica qué asumió | No |
| `Métricas de uso y dependencias entre módulos` | Pregunta: "¿Puedes proporcionar métricas de uso y dependencias entre módulos?" | Sí |
| `Mapa de dominio de negocio` | Pregunta: "¿Puedes proporcionar mapa de dominio de negocio?" | Sí |
| `Restricciones de tiempo` | Pregunta: "¿Puedes proporcionar restricciones de tiempo?" | Sí |
| `Requisitos no funcionales objetivo` | Pregunta: "¿Puedes proporcionar requisitos no funcionales objetivo?" | Sí |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-arch-decompose-v1.0) - pendiente validacion humana. No distribuir sin revision.
