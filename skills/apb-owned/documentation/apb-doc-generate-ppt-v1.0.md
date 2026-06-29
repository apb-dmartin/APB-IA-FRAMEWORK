---
id: "apb-doc-generate-ppt-v1.0"
name: "Generate PowerPoint Presentation"
description: "Genera presentaciones PowerPoint (.pptx) a partir de estructuras de contenido, con disenio corporativo, layouts consistentes y narrativa clara para stakeholders tecnicos y no tecnicos."
version: "1.0.0"
status: "draft"
owner: "Documentation Agent APB <arquitectura@portdebarcelona.cat>"
domain: "documentation"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

> Inspirado en: Anthropic Skills (presentation generation patterns) (licencia MIT).

# Generate PowerPoint Presentation

## Purpose
Genera presentaciones PowerPoint (.pptx) a partir de estructuras de contenido, con disenio corporativo, layouts consistentes y narrativa clara para stakeholders tecnicos y no tecnicos.

## Trigger
- Presentaciones de arquitectura a comite tecnico
- Demos de sprint a producto/negocio
- Propuestas tecnicas con visualizaciones
- Workshops de disenio con diagramas

## Input
- Contenido estructurado (slides con titulo, bullets, notas)
- Tema corporativo (colores, fuentes, logo)
- Tipo de presentacion (tecnica, ejecutiva, workshop)

## Output
- Archivo .pptx con disenio profesional
- Master slides configurados
- Layouts optimizados por tipo de contenido
- Notas del presentador incluidas

## Procedure

### Step 1: Definir Narrativa
Estructurar la historia:
- Opening: Problema / Contexto (1 slide)
- Body: 3-5 puntos clave, 1 idea por slide
- Closing: Conclusion / Next steps / Call to action

Regla: 10-20-30 (10 slides, 20 minutos, 30pt fuente minima)

### Step 2: Disenar Slides
Por tipo de contenido:

Titulo:
- Titulo grande, subtitulo, autor, fecha
- Fondo corporativo, logo

Contenido:
- Titulo arriba, bullets maximo 5 por slide
- Una idea por slide, no parrafos completos
- Iconos para conceptos clave

Diagrama:
- SmartArt o shapes para arquitecturas
- Colores consistentes por capa (API=azul, DB=verde, etc.)
- Leyenda si es necesario

Comparativa:
- Tabla o columnas lado a lado
- Highlight de la opcion recomendada

Codigo:
- Fuente monoespaciada grande (14pt+)
- Fondo oscuro, sintaxis resaltada si es posible
- Maximo 10 lineas por slide

### Step 3: Aplicar Tema
- Colores corporativos (primario, secundario, acento)
- Fuentes: titulos (Corporate Bold), cuerpo (Corporate Regular)
- Fondo: blanco o degradado sutil
- Logo: esquina inferior derecha, 80% opacidad

### Step 4: Anadir Notas
- Notas del presentador para cada slide
- Datos de respaldo, fuentes, preguntas esperadas
- Timing sugerido por slide

## Rules
- Nunca mas de 5 bullets por slide
- Nunca fuente menor a 18pt en contenido
- Una sola idea central por slide
- Diagramas > texto siempre que sea posible
- Numeracion de slides opcional para referencia

## Examples

### Example 1: Arquitectura Tecnica
Input: Descripcion de microservicios con Azure

Slides:
1. Titulo: "Arquitectura de Plataforma de Eventos"
2. Contexto: 3 bullets de problema actual
3. Diagrama: API Gateway -> Service Bus -> 3 Workers -> Cosmos DB
4. Decisiones: Tabla de tecnologias elegidas vs alternativas
5. Roadmap: Timeline Q1-Q4 con milestones
6. Riesgos: 3 bullets con mitigaciones
7. Q&A: Contacto, repositorio, documentacion

Notas:
- Slide 3: "Mencionar que Service Bus usa topics para pub/sub"
- Slide 4: "Si preguntan por Kafka, decir que evaluado pero complejidad innecesaria"

### Example 2: Demo Sprint
Input: Features completadas en sprint 12

Slides:
1. Titulo: "Sprint 12 Demo - Equipo Platform"
2. Objetivos: 3 goals del sprint
3. Feature A: Screenshot + 2 bullets de valor
4. Feature B: Video corto (embedded) + metricas
5. Feature C: Antes/Despues comparativa
6. Metricas: Burndown, velocity, defectos
7. Next: Sprint 13 priorities

Notas:
- Slide 3: "Preparar ambiente de demo con datos de produccion anonimizados"
- Slide 6: "Si velocity bajo, explicar que fue por onboarding de 2 devs"

## Integration
- Usa: third-anthropic-document-skills-v1.0 (wrapper con disenio APB)
- Input de: apb-dev-grill-before-code-v1.0 (presentar decisiones)
- Relacionado con: apb-doc-generate-word-v1.0 (documentos complementarios)

## Tags
#powerpoint #pptx #presentation #documentation #slides #corporate


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-doc-generate-ppt-v1.0) - pendiente validacion humana. No distribuir sin revision.
- **Word/PPT** - pie de pagina: `[IA-GEN] Generado por APB AI Framework - pendiente validacion humana`
