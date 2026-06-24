---
id: "apb-dev-frontend-devexpress-events-v1.0"
name: "Frontend Integration"
description: "Dise\xF1o e integraci\xF3n de UI con DevExpress y JavaScript puro para monitoreo\
  \ de eventos, dashboards de sagas, y visualizaci\xF3n de topolog\xEDa de Service\
  \ Bus. No React, no TypeScript."
version: "1.0.0"
status: "draft"
owner: "Desarrollo APB <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 1
consumed_by:
  - "apb-agent-implementer-v1.0"
created_date: "2026-06-20"
review_date: "2026-06-24"
---

> Procedencia: Adaptado de anthropics/skills (frontend-design + web-artifacts-builder) (licencia MIT).

# APB Frontend Integration: UI con DevExpress + JavaScript Puro

## Visión General

Diseño e implementación de interfaces de usuario para monitorear y operar arquitecturas orientadas a eventos usando **DevExpress con JavaScript puro**. **No React. No TypeScript.**

**Stack confirmado del usuario:** DevExpress + JavaScript puro.

## Cuándo Usar

- Crear dashboards de monitoreo de eventos
- Diseñar vistas de estado de sagas
- Implementar grids de visualización de DLQ
- Construir formularios de publicación de eventos de prueba
- Cuando el usuario necesita UI para operar el framework

## Principios de Diseño para Event-Driven

### 1. Dashboard de Eventos en Tiempo Real

```javascript
// components/EventMonitorDashboard.js
class EventMonitorDashboard {
  constructor(containerId, eventHub) {
    this.containerId = containerId;
    this.eventHub = eventHub; // WebSocket o Server-Sent Events
    this.grid = null;
    this.chart = null;
    this.stats = null;
  }

  init() {
    this.initGrid();
    this.initChart();
    this.initStats();
    this.startEventStream();
  }

  initGrid() {
    $(`#${this.containerId}-grid`).dxDataGrid({
      dataSource: new DevExpress.data.CustomStore({
        key: "id",
        load: () => this.eventHub.getRecentEvents(100),
        insert: (values) => this.eventHub.publishEvent(values)
      }),
      columns: [
        { 
          dataField: "time", 
          caption: "Timestamp", 
          dataType: "datetime",
          format: "yyyy-MM-dd HH:mm:ss.SSS",
          width: 180
        },
        { 
          dataField: "type", 
          caption: "Event Type",
          groupIndex: 0,
          cellTemplate: (container, options) => {
            const type = options.value;
            const color = this.getEventTypeColor(type);
            container.append(
              `<span class="event-badge" style="background:${color}">${type}</span>`
            );
          }
        },
        { dataField: "source", caption: "Source Service", width: 150 },
        { 
          dataField: "status", 
          caption: "Status",
          cellTemplate: (container, options) => {
            const status = options.value;
            const colors = {
              processed: "#28a745",
              failed: "#dc3545",
              pending: "#ffc107",
              retrying: "#17a2b8"
            };
            container.append(
              `<span style="color:${colors[status] || '#666'}">${status}</span>`
            );
          }
        },
        { 
          dataField: "deliveryCount", 
          caption: "Retries",
          cellTemplate: (container, options) => {
            const count = options.value;
            const color = count > 5 ? '#dc3545' : count > 2 ? '#ffc107' : '#28a745';
            container.append(`<span style="color:${color}">${count}</span>`);
          }
        },
        { 
          dataField: "latency", 
          caption: "Latency (ms)",
          dataType: "number",
          cellTemplate: (container, options) => {
            const ms = options.value;
            const color = ms > 5000 ? '#dc3545' : ms > 1000 ? '#ffc107' : '#28a745';
            container.append(`<span style="color:${color}">${ms}ms</span>`);
          }
        },
        {
          dataField: "data",
          caption: "Payload",
          cellTemplate: (container, options) => {
            const data = JSON.stringify(options.value, null, 2);
            container.append(`<pre class="event-payload">${data}</pre>`);
          }
        }
      ],
      grouping: { autoExpandAll: false },
      sorting: { mode: "multiple" },
      filterRow: { visible: true },
      searchPanel: { visible: true },
      paging: { pageSize: 50 },
      scrolling: { mode: "virtual" },
      masterDetail: {
        enabled: true,
        template: (container, info) => {
          this.renderEventDetail(container, info.data);
        }
      },
      onRowClick: (e) => {
        this.showEventTrace(e.data);
      }
    });
  }

  initChart() {
    $(`#${this.containerId}-chart`).dxChart({
      dataSource: this.eventHub.getEventMetrics(),
      series: [
        { valueField: "published", name: "Published", color: "#28a745" },
        { valueField: "consumed", name: "Consumed", color: "#007bff" },
        { valueField: "failed", name: "Failed", color: "#dc3545" },
        { valueField: "dlq", name: "DLQ", color: "#ffc107" }
      ],
      argumentAxis: {
        argumentType: "datetime",
        tickInterval: { minutes: 5 }
      },
      legend: { verticalAlignment: "bottom", horizontalAlignment: "center" },
      tooltip: { enabled: true }
    });
  }

  initStats() {
    $(`#${this.containerId}-stats`).dxTileView({
      items: [
        { text: "Events/sec", value: 0, type: "throughput" },
        { text: "Active DLQ", value: 0, type: "dlq" },
        { text: "Active Sagas", value: 0, type: "sagas" },
        { text: "Avg Latency", value: "0ms", type: "latency" }
      ],
      itemTemplate: (itemData, itemIndex, itemElement) => {
        itemElement.append(`
          <div class="stat-card stat-${itemData.type}">
            <div class="stat-value">${itemData.value}</div>
            <div class="stat-label">${itemData.text}</div>
          </div>
        `);
      }
    });
  }

  startEventStream() {
    this.eventHub.onEvent((event) => {
      this.grid.getDataSource().store().insert(event);
      this.grid.refresh();
      this.updateStats();
    });
  }

  getEventTypeColor(type) {
    const colors = {
      'orders': '#e74c3c',
      'payments': '#27ae60',
      'inventory': '#3498db',
      'shipping': '#f39c12',
      'sagas': '#9b59b6'
    };
    const domain = type.split('.')[0];
    return colors[domain] || '#95a5a6';
  }

  renderEventDetail(container, eventData) {
    container.append(`
      <div class="event-detail">
        <h4>Event Trace</h4>
        <div class="trace-timeline">
          ${this.renderTraceTimeline(eventData.trace)}
        </div>
        <h4>Schema Validation</h4>
        <pre>${JSON.stringify(eventData.validation, null, 2)}</pre>
        <h4>Related Events</h4>
        <div class="related-events">
          ${this.renderRelatedEvents(eventData.related)}
        </div>
      </div>
    `);
  }

  showEventTrace(event) {
    // Mostrar modal con traza distribuida completa
    DevExpress.ui.dialog.custom({
      title: `Event Trace: ${event.id}`,
      messageHtml: this.renderTraceHtml(event),
      buttons: [{ text: "Close" }]
    });
  }
}
```

### 2. Vista de Saga

```javascript
// components/SagaVisualizer.js
class SagaVisualizer {
  constructor(containerId) {
    this.containerId = containerId;
  }

  init() {
    $(`#${this.containerId}`).dxDiagram({
      nodes: {
        dataSource: this.getSagaNodes(),
        keyExpr: "id",
        textExpr: "name",
        typeExpr: "type",
        customDataExpr: "data"
      },
      edges: {
        dataSource: this.getSagaEdges(),
        keyExpr: "id",
        fromExpr: "from",
        toExpr: "to"
      },
      toolbox: { visible: false },
      propertiesPanel: { visible: false },
      onItemClick: (e) => {
        if (e.item.type === "step") {
          this.showStepDetails(e.item);
        }
      }
    });
  }

  getSagaNodes() {
    return [
      { id: "start", name: "Start", type: "start" },
      { id: "reserve", name: "Reserve Inventory", type: "step", status: "completed" },
      { id: "payment", name: "Process Payment", type: "step", status: "in-progress" },
      { id: "ship", name: "Create Shipment", type: "step", status: "pending" },
      { id: "complete", name: "Complete", type: "end" },
      { id: "comp-reserve", name: "Release Inventory", type: "compensation", status: "pending" },
      { id: "comp-payment", name: "Refund Payment", type: "compensation", status: "pending" }
    ];
  }

  getSagaEdges() {
    return [
      { id: 1, from: "start", to: "reserve" },
      { id: 2, from: "reserve", to: "payment" },
      { id: 3, from: "payment", to: "ship" },
      { id: 4, from: "ship", to: "complete" },
      { id: 5, from: "payment", to: "comp-reserve" },
      { id: 6, from: "ship", to: "comp-payment" }
    ];
  }
}
```

### 3. Grid de Dead Letter Queue

```javascript
// components/DLQManager.js
class DLQManager {
  constructor(containerId, serviceBusClient) {
    this.containerId = containerId;
    this.serviceBusClient = serviceBusClient;
  }

  init() {
    $(`#${this.containerId}`).dxDataGrid({
      dataSource: new DevExpress.data.CustomStore({
        key: "messageId",
        load: (loadOptions) => this.loadDLQMessages(loadOptions),
        byKey: (key) => this.getMessageById(key)
      }),
      columns: [
        { dataField: "messageId", caption: "Message ID", width: 280 },
        { dataField: "enqueuedTime", caption: "DLQ Time", dataType: "datetime" },
        { dataField: "deliveryCount", caption: "Retries" },
        { dataField: "deadLetterReason", caption: "Reason" },
        { dataField: "deadLetterErrorDescription", caption: "Error" },
        {
          dataField: "body",
          caption: "Event",
          cellTemplate: (container, options) => {
            const event = JSON.parse(options.value);
            container.append(`<code>${event.type}</code>`);
          }
        },
        {
          type: "buttons",
          buttons: [
            {
              name: "retry",
              icon: "refresh",
              hint: "Retry message",
              onClick: (e) => this.retryMessage(e.row.data)
            },
            {
              name: "delete",
              icon: "trash",
              hint: "Delete message",
              onClick: (e) => this.deleteMessage(e.row.data)
            },
            {
              name: "inspect",
              icon: "info",
              hint: "Inspect full payload",
              onClick: (e) => this.inspectMessage(e.row.data)
            }
          ]
        }
      ],
      editing: { mode: "row", allowUpdating: false, allowDeleting: false },
      toolbar: {
        items: [
          {
            widget: "dxButton",
            options: {
              text: "Retry All",
              icon: "refresh",
              onClick: () => this.retryAll()
            }
          },
          {
            widget: "dxButton",
            options: {
              text: "Purge DLQ",
              icon: "clear",
              type: "danger",
              onClick: () => this.purgeDLQ()
            }
          }
        ]
      }
    });
  }

  async retryMessage(message) {
    const result = await DevExpress.ui.dialog.confirm(
      `Retry message ${message.messageId}?`,
      "Confirm Retry"
    );
    if (result) {
      await this.serviceBusClient.retryMessage(message);
      this.grid.refresh();
    }
  }
}
```

## Anti-Patrón: "AI Slop" en Dashboards de Eventos

```
❌ EVITAR:
- Layouts centrados excesivos
- Gradientes púrpura genéricos
- Esquinas redondeadas uniformes
- Fuente Inter por defecto
- Gráficos de donut sin propósito
- Números grandes con etiquetas pequeñas ("01 / 02 / 03")

✅ HACER:
- Layouts que reflejen el flujo de datos (izquierda → derecha)
- Colores que codifiquen el dominio (orders=rojo, payments=verde)
- Tipografía que encode información (monospace para IDs, sans para labels)
- Estructura que refleje la arquitectura (servicios como nodos, eventos como edges)
- Números significativos ("47 eventos/seg" no "01 throughput")
```

## Integración con el Flujo APB

```
[operador necesita dashboard] → apb:frontend-integration → [DevExpress UI] → [monitoreo en tiempo real]
```
