---
id: "apb-doc-event-specs-v1.0"
name: "Document Processing"
description: "Generaci\xF3n de documentaci\xF3n t\xE9cnica del APB AI Framework: specs CloudEvents,\
  \ AsyncAPI, manuales de operaci\xF3n, y reportes de arquitectura en DOCX y PDF."
version: "1.0.0"
status: "draft"
owner: "Documentation Agent APB <arquitectura@portdebarcelona.cat>"
domain: "documentation"
autonomy_level: 1
consumed_by:
  - "apb-agent-documentation-v1.0"
created_date: "2026-06-20"
review_date: "2026-06-24"
---

> Procedencia: Adaptado de anthropics/skills (docx + pdf) (licencia MIT).

# APB Document Processing: Documentación Técnica del Framework

## Visión General

Generar documentación técnica del APB AI Framework en formatos profesionales (DOCX, PDF). Incluye specs de eventos, documentación AsyncAPI, manuales de operación, y reportes de arquitectura.

## Cuándo Usar

- Generar documentación de eventos (AsyncAPI spec)
- Crear manuales de operación de Service Bus
- Producir reportes de arquitectura para stakeholders
- Documentar schemas CloudEvents en formato legible
- Cuando el usuario dice "generar documentación" o "reporte en PDF/DOCX"

## Tipos de Documentos

### 1. AsyncAPI Specification (YAML → DOCX/PDF)

```javascript
// scripts/generate-asyncapi-doc.js
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
        HeadingLevel, AlignmentType, BorderStyle } = require('docx');
const yaml = require('js-yaml');
const fs = require('fs');

class AsyncAPIDocumentGenerator {
  async generate(asyncapiYamlPath, outputPath) {
    const spec = yaml.load(fs.readFileSync(asyncapiYamlPath, 'utf8'));

    const doc = new Document({
      sections: [{
        properties: {},
        children: [
          this.createTitle(spec.info.title, spec.info.version),
          this.createDescription(spec.info.description),
          this.createServersTable(spec.servers),
          this.createChannelsSection(spec.channels),
          this.createSchemasSection(spec.components.schemas),
          this.createSecuritySection(spec.security)
        ]
      }]
    });

    const buffer = await Packer.toBuffer(doc);
    fs.writeFileSync(outputPath, buffer);
  }

  createTitle(title, version) {
    return new Paragraph({
      text: `${title} v${version}`,
      heading: HeadingLevel.TITLE,
      alignment: AlignmentType.CENTER
    });
  }

  createChannelsSection(channels) {
    const rows = [];

    // Header
    rows.push(new TableRow({
      children: [
        new TableCell({ children: [new Paragraph("Channel")] }),
        new TableCell({ children: [new Paragraph("Operation")] }),
        new TableCell({ children: [new Paragraph("Message")] }),
        new TableCell({ children: [new Paragraph("Bindings")] })
      ]
    }));

    // Data
    for (const [channelName, channel] of Object.entries(channels)) {
      const operation = channel.publish || channel.subscribe;
      rows.push(new TableRow({
        children: [
          new TableCell({ children: [new Paragraph(channelName)] }),
          new TableCell({ children: [new Paragraph(channel.publish ? "Publish" : "Subscribe")] }),
          new TableCell({ children: [new Paragraph(operation.message.$ref.split('/').pop())] }),
          new TableCell({ children: [new Paragraph(JSON.stringify(channel.bindings))] })
        ]
      }));
    }

    return new Table({ rows });
  }

  createSchemasSection(schemas) {
    const sections = [];

    for (const [schemaName, schema] of Object.entries(schemas)) {
      sections.push(new Paragraph({
        text: schemaName,
        heading: HeadingLevel.HEADING_2
      }));

      sections.push(new Paragraph({
        text: JSON.stringify(schema, null, 2),
        style: "Code"
      }));
    }

    return sections;
  }
}
```

### 2. Event Catalog (JSON → DOCX)

```javascript
// scripts/generate-event-catalog.js
class EventCatalogGenerator {
  async generate(eventCatalog, outputPath) {
    const doc = new Document({
      sections: [{
        children: [
          new Paragraph({
            text: "APB Event Catalog",
            heading: HeadingLevel.TITLE
          }),
          new Paragraph({
            text: `Generated: ${new Date().toISOString()}`,
            alignment: AlignmentType.RIGHT
          }),
          ...this.createEventSections(eventCatalog.events)
        ]
      }]
    });

    const buffer = await Packer.toBuffer(doc);
    fs.writeFileSync(outputPath, buffer);
  }

  createEventSections(events) {
    const sections = [];

    for (const event of events) {
      // Event Header
      sections.push(new Paragraph({
        text: event.type,
        heading: HeadingLevel.HEADING_1
      }));

      // Metadata Table
      sections.push(new Table({
        rows: [
          new TableRow({
            children: [
              new TableCell({ children: [new Paragraph("Field")] }),
              new TableCell({ children: [new Paragraph("Value")] })
            ]
          }),
          new TableRow({
            children: [
              new TableCell({ children: [new Paragraph("Version")] }),
              new TableCell({ children: [new Paragraph(event.version)] })
            ]
          }),
          new TableRow({
            children: [
              new TableCell({ children: [new Paragraph("Source")] }),
              new TableCell({ children: [new Paragraph(event.source)] })
            ]
          }),
          new TableRow({
            children: [
              new TableCell({ children: [new Paragraph("Producer")] }),
              new TableCell({ children: [new Paragraph(event.producer)] })
            ]
          }),
          new TableRow({
            children: [
              new TableCell({ children: [new Paragraph("Consumers")] }),
              new TableCell({ children: [new Paragraph(event.consumers.join(", "))] })
            ]
          }),
          new TableRow({
            children: [
              new TableCell({ children: [new Paragraph("Topic")] }),
              new TableCell({ children: [new Paragraph(event.topic)] })
            ]
          }),
          new TableRow({
            children: [
              new TableCell({ children: [new Paragraph("DLQ")] }),
              new TableCell({ children: [new Paragraph(event.dlq)] })
            ]
          })
        ]
      }));

      // Schema
      sections.push(new Paragraph({
        text: "Schema",
        heading: HeadingLevel.HEADING_2
      }));

      sections.push(new Paragraph({
        text: JSON.stringify(event.schema, null, 2),
        style: "Code"
      }));

      // Example
      sections.push(new Paragraph({
        text: "Example",
        heading: HeadingLevel.HEADING_2
      }));

      sections.push(new Paragraph({
        text: JSON.stringify(event.example, null, 2),
        style: "Code"
      }));

      // Page break
      sections.push(new Paragraph({ text: "", pageBreakBefore: true }));
    }

    return sections;
  }
}
```

### 3. Reporte de Arquitectura (Markdown → PDF)

```javascript
// scripts/generate-architecture-report.js
const { PdfReader, PdfWriter } = require('pypdf'); // o usar puppeteer para HTML→PDF

class ArchitectureReportGenerator {
  async generate(architectureMarkdown, outputPath) {
    // Convertir markdown a HTML con estilos
    const html = this.markdownToHTML(architectureMarkdown);

    // Usar puppeteer para generar PDF
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.setContent(html);
    await page.pdf({
      path: outputPath,
      format: 'A4',
      margin: { top: '2cm', right: '2cm', bottom: '2cm', left: '2cm' },
      displayHeaderFooter: true,
      headerTemplate: `
        <div style="font-size: 9px; width: 100%; text-align: center;">
          APB AI Framework — Architecture Report
        </div>
      `,
      footerTemplate: `
        <div style="font-size: 9px; width: 100%; text-align: center;">
          Page <span class="pageNumber"></span> of <span class="totalPages"></span>
        </div>
      `
    });
    await browser.close();
  }

  markdownToHTML(markdown) {
    // Usar marked.js para convertir markdown a HTML
    const marked = require('marked');
    const html = marked.parse(markdown);

    return `
      <!DOCTYPE html>
      <html>
      <head>
        <style>
          body { font-family: 'Segoe UI', sans-serif; line-height: 1.6; }
          h1 { color: #2c3e50; border-bottom: 2px solid #3498db; }
          h2 { color: #34495e; border-bottom: 1px solid #bdc3c7; }
          table { border-collapse: collapse; width: 100%; }
          th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
          th { background-color: #f2f2f2; }
          code { background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px; }
          pre { background-color: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto; }
        </style>
      </head>
      <body>${html}</body>
      </html>
    `;
  }
}
```

### 4. Manual de Operación (DOCX)

```javascript
// scripts/generate-operations-manual.js
class OperationsManualGenerator {
  async generate(outputPath) {
    const doc = new Document({
      sections: [{
        children: [
          // Portada
          new Paragraph({ text: "APB AI Framework", heading: HeadingLevel.TITLE }),
          new Paragraph({ text: "Manual de Operación", heading: HeadingLevel.HEADING_1 }),
          new Paragraph({ text: `Versión: 1.0 | Fecha: ${new Date().toISOString().split('T')[0]}` }),

          // Tabla de contenidos
          new Paragraph({ text: "Tabla de Contenidos", heading: HeadingLevel.HEADING_1 }),
          new Paragraph({ text: "1. Arquitectura de Eventos" }),
          new Paragraph({ text: "2. Monitoreo de Service Bus" }),
          new Paragraph({ text: "3. Gestión de Dead Letter Queues" }),
          new Paragraph({ text: "4. Operación de Sagas" }),
          new Paragraph({ text: "5. Troubleshooting" }),
          new Paragraph({ text: "6. Escalamiento" }),

          // Capítulos
          ...this.createOperationsContent()
        ]
      }]
    });

    const buffer = await Packer.toBuffer(doc);
    fs.writeFileSync(outputPath, buffer);
  }

  createOperationsContent() {
    return [
      // Capítulo 1
      new Paragraph({ text: "1. Arquitectura de Eventos", heading: HeadingLevel.HEADING_1 }),
      new Paragraph({ text: "El APB AI Framework utiliza Azure Service Bus como broker de eventos..." }),

      // Capítulo 2
      new Paragraph({ text: "2. Monitoreo de Service Bus", heading: HeadingLevel.HEADING_1 }),
      new Paragraph({ text: "Métricas clave a monitorear:" }),
      new Paragraph({ text: "- Active messages por subscription", bullet: { level: 0 } }),
      new Paragraph({ text: "- Dead letter count", bullet: { level: 0 } }),
      new Paragraph({ text: "- Transfer dead letter messages", bullet: { level: 0 } }),
      new Paragraph({ text: "- Message throughput", bullet: { level: 0 } }),

      // Capítulo 3
      new Paragraph({ text: "3. Gestión de Dead Letter Queues", heading: HeadingLevel.HEADING_1 }),
      new Paragraph({ text: "Procedimiento de reintento:" }),
      new Paragraph({ text: "1. Identificar mensaje en DLQ", numbering: { level: 0 } }),
      new Paragraph({ text: "2. Verificar causa del fallo", numbering: { level: 0 } }),
      new Paragraph({ text: "3. Corregir problema subyacente", numbering: { level: 0 } }),
      new Paragraph({ text: "4. Reintentar mensaje", numbering: { level: 0 } }),
      new Paragraph({ text: "5. Verificar procesamiento exitoso", numbering: { level: 0 } }),

      // ... más capítulos
    ];
  }
}
```

## Plantillas de Documentos

### Plantilla: Spec de Evento

```markdown
# Event Specification: [type]

## Metadata
| Field | Value |
|-------|-------|
| Type | [namespace].[event].v[version] |
| Source | [URI] |
| Producer | [Service] |
| Consumers | [Service1], [Service2] |
| Topic | [topic-name] |
| DLQ | [dlq-name] |

## Schema
\`\`\`json
[Schema JSON]
\`\`\`

## Example
\`\`\`json
[Example event]
\`\`\`

## Business Rules
- [Rule 1]
- [Rule 2]

## Error Handling
- [Error scenario 1]: [Handling]
- [Error scenario 2]: [Handling]

## Version History
| Version | Date | Changes |
|---------|------|---------|
| v1.0 | [Date] | Initial version |
```

## Integración con el Flujo APB

```
[documento necesario] → apb:document-processing → [DOCX/PDF generado] → [distribución]
```


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **YAML/spec generado** - primera linea: `# [IA-GEN] Generado por APB AI Framework (apb-doc-event-specs-v1.0) - pendiente revision humana`
- **Campo OpenAPI si aplica**: `info.x-ai-generated: true` + `info.x-ai-skill: "apb-doc-event-specs-v1.0"`
- **Commit** - prefijo `[ai-gen]` + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`
