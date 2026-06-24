---
id: "apb-doc-generate-word-v1.0"
name: "Generate Word Document"
description: "Genera documentos Word (.docx) profesionales a partir de estructuras de datos o markdown, con plantillas corporativas, estilos consistentes y contenido dinamico."
version: "1.0.0"
status: "draft"
owner: "Documentation Agent APB <arquitectura@portdebarcelona.cat>"
domain: "documentation"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

> Inspirado en: Anthropic Skills (document generation patterns) (licencia MIT).

# Generate Word Document

## Purpose
Genera documentos Word (.docx) profesionales a partir de estructuras de datos o markdown, con plantillas corporativas, estilos consistentes y contenido dinamico.

## Trigger
- Generacion de informes tecnicos, propuestas, o documentacion formal
- Exportacion de datos a formato editable para stakeholders
- Creacion de documentos de compliance (politicas, procedimientos)

## Input
- Contenido estructurado (markdown, JSON, o datos tabulares)
- Plantilla corporativa (opcional: .dotx o estilos definidos)
- Metadatos del documento (autor, titulo, version, fecha)

## Output
- Archivo .docx con formato profesional
- Indice automatico (TOC)
- Estilos consistentes (Heading 1-4, Normal, Quote, Code)
- Numeracion de paginas, encabezado/pie corporativo

## Procedure

### Step 1: Preparar Contenido
Convertir input a estructura intermedia con secciones, headings, tablas, imagenes.

### Step 2: Aplicar Plantilla
- Cargar plantilla .dotx o crear estilos programaticamente
- Definir: fuentes (Calibri/Corporate), tamanios, colores
- Configurar: margenes, orientacion, numeracion

### Step 3: Generar Documento
- Crear secciones con estilos correspondientes
- Insertar tablas con formato corporativo
- Insertar imagenes con caption
- Generar TOC automatico
- Aplicar numeracion de paginas

### Step 4: Aplicar Metadatos
- Propiedades del documento: titulo, autor, empresa, version
- Fecha de generacion
- Marca de agua "BORRADOR" si aplica

## Rules
- Siempre usar estilos, nunca formato directo (seleccionar parrafo + estilo)
- Tablas: encabezados con fondo corporativo, alternar filas
- Codigo: fuente monoespaciada, fondo gris claro, sin sangria excesiva
- Imagenes: maximo ancho de pagina, centrado, caption debajo

## Examples

### Example 1: Informe Tecnico
Input: Markdown con secciones de analisis de arquitectura

Generacion:
- Titulo: "Analisis de Arquitectura - Proyecto X"
- Secciones: 1. Resumen Ejecutivo, 2. Contexto, 3. Analisis, 4. Recomendaciones
- Tablas: Matriz de tecnologias, comparativa de opciones
- TOC: 3 niveles de profundidad
- Metadatos: Autor: APB Framework, Version: 1.0

### Example 2: Documento de Politica
Input: JSON con estructura de politica de seguridad

Generacion:
- Plantilla: corporate-policy.dotx
- Secciones numeradas: 1. Objetivo, 2. Alcance, 3. Definiciones...
- Tablas: Roles y responsabilidades, matriz RACI
- Marca de agua: "CONFIDENCIAL"
- Footer: "Pagina X de Y | Politica de Seguridad v2.1"

## Integration
- Usa: third-anthropic-document-skills-v1.0 (wrapper con estilos APB)
- Input de: apb-dev-impact-analysis-v1.0 (reportes de impacto)
- Relacionado con: apb-doc-generate-ppt-v1.0 (presentaciones)

## Tags
#word #docx #documentation #report #template #generation
