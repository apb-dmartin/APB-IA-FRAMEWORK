---
id: "apb-plat-doc-to-markdown-v1.0"
name: "Document to Markdown Normalizer"
description: "Convierte cualquier adjunto ofimatico (Word, Excel, PowerPoint, PDF) recibido como input por un agente, skill o subagente a Markdown antes de su consumo, bajo el principio de que todo componente del framework trabaja internamente en Markdown."
version: "1.0.0"
status: "draft"
owner: "Plataforma APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
created_date: "2026-06-24"
review_date: "2026-06-24"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

> Decision de Debora (Sesion 9, punto #31 de PLAN_FASES_FUTURAS.md, asignada a Sesion 10):
> todo input ofimatico se normaliza a Markdown antes de ser consumido por cualquier
> componente del framework. Ver Principio Fundamental #12 de README.md.

# Document to Markdown Normalizer


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Purpose
Cuando un agente, skill o subagente recibe como input un adjunto en formato ofimatico
(`.docx`, `.xlsx`, `.pptx`, `.pdf`), esta skill lo convierte a Markdown antes de que el
componente consumidor lo procese. El principio de fondo: todos los componentes del framework
razonan y generan en Markdown por eficiencia y consistencia, independientemente del formato
en que el usuario aporte la informacion de entrada.

## Trigger
- Cualquier agente/skill/subagente recibe un `file_path` cuya extension es
  `.docx`, `.dotx`, `.xlsx`, `.xlsm`, `.pptx`, `.potx` o `.pdf` como input directo
- El input declarado de la skill consumidora es de tipo `text` o `markdown` pero el archivo
  real aportado es ofimatico

## Input
| Nombre | Tipo | Obligatorio | Descripcion |
|--------|------|-------------|-------------|
| `source_file` | file_path | Si | Ruta al archivo ofimatico original |
| `source_format` | enum | Si | `docx`, `xlsx`, `pptx`, `pdf` |
| `preserve_tables` | bool | No | Mantener tablas como Markdown tables (default: true) |
| `extract_images` | bool | No | Extraer imagenes embebidas a archivos separados (default: false, salvo que el consumidor las necesite) |

## Output
| Nombre | Tipo | Descripcion |
|--------|------|-------------|
| `markdown_content` | markdown | Contenido normalizado, listo para el componente consumidor |
| `conversion_report` | markdown | Que se perdio o aproximo en la conversion (formato visual, macros, animaciones, formulas complejas) |
| `extracted_assets` | list[file_path] | Imagenes o adjuntos extraidos, si `extract_images: true` |

## Procedure

### Phase 1: Deteccion de Formato
1. Identificar `source_format` por extension real del archivo, no por declaracion del usuario.
2. Si el formato no esta soportado (ej. `.odt`, `.rtf`), reportar explicitamente y no inventar
   una conversion aproximada sin avisar.

### Phase 2: Conversion
3. **Word (`.docx`/`.dotx`):** texto, encabezados (`#`/`##`/...), listas, tablas → Markdown.
   Tracked changes y comentarios se reportan en `conversion_report`, no se pierden
   silenciosamente — se resumen como nota al pie del Markdown si son relevantes para el
   contexto de uso.
4. **Excel (`.xlsx`/`.xlsm`):** cada hoja relevante → tabla Markdown. Formulas se convierten a
   su valor calculado, no a la formula en si, salvo que el consumidor declare necesitarla
   explicitamente (en cuyo caso se incluye ambas: valor y formula entre parentesis).
5. **PowerPoint (`.pptx`/`.potx`):** cada slide → seccion Markdown (`## Slide N: {titulo}`),
   con el contenido de texto y notas de orador si existen. Layout visual no se preserva
   (no es relevante para razonamiento de texto).
6. **PDF:** si es texto nativo, extraccion directa a Markdown preservando estructura de
   encabezados donde sea detectable. Si es escaneado/imagen, se reporta como tal: esta skill
   NO hace OCR (delega a la skill `pdf` del framework si OCR es necesario).

### Phase 3: Validacion de Perdida de Informacion
7. Generar `conversion_report`: que elementos del original no tienen equivalente en Markdown
   (graficos complejos, macros, animaciones, formato condicional de Excel, etc.).
8. Si la perdida de informacion es material para el proposito declarado del consumidor,
   marcar el output como `requires_human_review: true`.

## Rules
- Nunca se descarta informacion silenciosamente: toda perdida se documenta en
  `conversion_report`.
- No se hace OCR aqui; PDFs escaneados se delegan a la skill `pdf` (ver SKILL.md publico).
- Tablas siempre se preservan como tablas Markdown, nunca se aplanan a texto corrido.
- El Markdown resultante es la unica fuente que el componente consumidor procesa; el archivo
  original se mantiene como referencia trazable pero no se reprocesa dos veces.

## Examples

### Example 1: Briefing de licitacion en Word
Input: `briefing-licitacion.docx` aportado para `apb-agent-spec-engineer-v1.0` (punto #36
del plan, agentes de licitacion).
Conversion: encabezados de seccion → `##`, tabla de requisitos → tabla Markdown, anexos
referenciados → lista con nombre de archivo. `conversion_report`: "2 imagenes decorativas no
extraidas (no aportan contenido funcional)".

### Example 2: Excel con formulas de COSMIC
Input: `historico-cosmic.xlsx` para el punto #8 (entrenar valoracion COSMIC con historico
real de horas).
Conversion: cada hoja → tabla Markdown con valores calculados. `conversion_report`: "Columna
'Horas estimadas' contenia formulas VLOOKUP; se preservan ambos: valor resultante y formula
entre parentesis, por relevancia para el analisis de conversion puntos↔horas."

## Integration
- Consumida por: cualquier agente/skill/subagente que declare `accepts_office_input: true`
- Precede a: el procesamiento real de cualquier componente consumidor
- Relacionado con: skill publica `docx`/`xlsx`/`pptx`/`pdf` (capacidades de creacion, distinto
  de esta skill que es de normalizacion de *entrada*)
- Aplicada por: `apb-agent-meta-builder-v1.0` (Sesion 10) — cualquier componente que genere
  debe declarar si acepta adjuntos ofimaticos y, si es asi, depender de esta skill

## Tags
#markdown #normalization #office #docx #xlsx #pptx #pdf #platform

---

> **Generado por IA:** Claude (Anthropic), Sesión 10 del plan de remediación APB-IA-FRAMEWORK.
> **Validado por humano:** _pendiente — completar nombre/rol del validador antes de pasar a `candidate`._


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-plat-doc-to-markdown-v1.0) - pendiente validacion humana. No distribuir sin revision.
- **Word/PPT** - pie de pagina: `[IA-GEN] Generado por APB AI Framework - pendiente validacion humana`
