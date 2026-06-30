---
id: "apb-design-wcag-patterns-v1.0"
name: "Patrones de Componentes Accesibles con DevExtreme"
description: "Proporciona patrones de implementación accesible (WCAG 2.1 AA) para componentes DevExtreme usados en los portales APB. Cubre ARIA roles y atributos, navegación por teclado, gestión del foco, mensajes de error accesibles y anuncios a lectores de pantalla para los componentes más usados: DataGrid, Form, DateBox, Popup, SelectBox."
version: "1.0.0"
status: "deprecated"
deprecated_reason: "Consolidado en apb-qa-accessibility-v1.0 (decision Arquitectura APB 2026-06-30)"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "design"
autonomy_level: 1
created_date: "2026-06-29"
review_date: "2026-12-29"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# Patrones de Componentes Accesibles con DevExtreme


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Propósito
Proporcionar patrones concretos de implementación accesible para los componentes DevExtreme/DevExpress usados en los portales APB. DevExtreme incluye soporte de accesibilidad en muchos de sus componentes, pero requiere configuración correcta de ARIA, gestión del foco y mensajes de error para cumplir WCAG 2.1 AA (obligatorio para APB como organismo del sector público según RD 1112/2018).

## Contexto de Uso
- Desarrollo de un nuevo portal o funcionalidad con componentes DevExtreme.
- Corrección de incidencias de accesibilidad detectadas en auditoría (`apb-qa-accessibility-v1.0`).
- Revisión de código de un componente DevExtreme antes del PR: ¿es accesible?
- Onboarding de desarrolladores en los patrones de accesibilidad APB.
- Preparación de la Declaración de Accesibilidad: los patrones de esta skill soportan el cumplimiento WCAG.

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `component` | Texto | Componente DevExtreme a implementar o corregir | ✅ |
| `use_case` | Texto | Caso de uso específico del componente en el portal APB | ✅ |
| `issue_description` | Texto | Problema de accesibilidad a corregir (para correcciones) | ❌ |
| `wcag_criterion` | Texto | Criterio WCAG específico que falla (si se conoce) | ❌ |

## Patrones por Componente

### DxDataGrid — Tabla de datos accesible

```typescript
// ⚠️ Generado por APB AI Framework (apb-design-wcag-patterns-v1.0) — adaptar al caso de uso.
<DxDataGrid
  [dataSource]="escalas"
  [showBorders]="true"
  [focusedRowEnabled]="true"
  [keyboardNavigation]="{ enabled: true, enterKeyAction: 'startEdit', editOnKeyPress: true }"
  aria-label="Listado de escalas marítimas activas">
  
  <!-- Columna de acciones: usar botones con aria-label descriptivo -->
  <dxi-column
    cellTemplate="actionTemplate"
    [allowSorting]="false"
    caption="Acciones">
  </dxi-column>
  
  <div *dxTemplate="let cell of 'actionTemplate'">
    <dx-button
      [attr.aria-label]="'Ver detalle de escala ' + cell.data.numeroEscala"
      icon="search"
      (onClick)="verDetalle(cell.data)">
    </dx-button>
  </div>
</DxDataGrid>
```

**Puntos clave de accesibilidad para DxDataGrid**:
- `aria-label` en el grid con descripción del contenido.
- `focusedRowEnabled: true` para visibilidad del foco.
- Columnas de acción con botones que tienen `aria-label` descriptivo (no solo icono).
- Si hay paginación: el cambio de página debe anunciarse (`aria-live`).

### DxForm con validación accesible

```typescript
<DxForm
  [formData]="escalaData"
  (onFieldDataChanged)="onFieldChanged($event)">
  
  <dxi-item dataField="buque" [label]="{ text: 'Nombre del buque' }">
    <dxi-validation-rule
      type="required"
      message="El nombre del buque es obligatorio">
    </dxi-validation-rule>
  </dxi-item>
  
  <!-- Mensajes de error: DevExtreme los gestiona con role="alert" automáticamente -->
  <!-- PERO: el mensaje debe ser descriptivo, no solo "Campo requerido" -->
</DxForm>
```

**Puntos clave para DxForm**:
- Labels asociados correctamente a cada campo (DevExtreme lo gestiona si se usa `label.text`).
- Mensajes de error descriptivos: "El NIF del consignatario debe tener 9 caracteres" en lugar de "Valor inválido".
- Al enviar con errores: el foco debe ir al primer campo con error.
- No usar solo color para indicar error — usar también icono o texto.

### DxPopup (modal) accesible

```typescript
<DxPopup
  [visible]="popupVisible"
  title="Confirmar cierre de escala"
  [dragEnabled]="false"
  [closeOnOutsideClick]="false"
  [showCloseButton]="true"
  (onShown)="onPopupShown()"
  (onHidden)="onPopupHidden()">
```

```typescript
onPopupShown() {
  // Mover el foco al primer elemento interactivo del popup
  setTimeout(() => {
    const firstFocusable = document.querySelector('.dx-popup-content button, .dx-popup-content input');
    (firstFocusable as HTMLElement)?.focus();
  }, 100);
}

onPopupHidden() {
  // Devolver el foco al elemento que abrió el popup
  this.triggerElement?.focus();
}
```

**Puntos clave para DxPopup**:
- `role="dialog"` y `aria-labelledby` apuntando al título — DevExtreme lo gestiona si se usa `title`.
- Al abrir: mover foco al interior del popup.
- Al cerrar: devolver foco al elemento disparador.
- Trap de foco dentro del popup: Tab no debe salir del popup mientras está abierto.

### DxSelectBox accesible

```typescript
<DxSelectBox
  [dataSource]="tiposMercancia"
  displayExpr="nombre"
  valueExpr="id"
  placeholder="Selecciona el tipo de mercancía"
  [attr.aria-label]="'Tipo de mercancía'"
  [searchEnabled]="true"
  [searchMode]="'contains'">
</DxSelectBox>
```

**Puntos clave para DxSelectBox**:
- `aria-label` cuando el label visible está separado del componente.
- `searchEnabled: true` permite filtrar con teclado — buena práctica para listas largas.
- El valor seleccionado debe anunciarse correctamente al lector de pantalla.

### Gestión del color y contraste

```css
/* Variables de color APB que cumplen WCAG 2.1 AA */
:root {
  --apb-color-primary: #005587;      /* Texto sobre blanco: ratio 7.5:1 ✅ */
  --apb-color-error: #c0392b;         /* Texto error sobre blanco: ratio 5.2:1 ✅ */
  --apb-color-success: #1e7e34;       /* Texto éxito sobre blanco: ratio 5.1:1 ✅ */
  --apb-color-text-secondary: #595959; /* Texto secundario sobre blanco: ratio 7.0:1 ✅ */
  
  /* EVITAR: colores que no cumplen el contraste mínimo */
  /* --apb-color-warning-text: #ffc107 */ /* ❌ Ratio 1.1:1 sobre blanco — cambiar a #856404 */
}
```

## Patrones Generales de Accesibilidad APB

### Manejo de focus trap en modales
```typescript
// Función reutilizable para trap de foco
trapFocus(element: HTMLElement) {
  const focusableElements = element.querySelectorAll(
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
  );
  const firstFocusable = focusableElements[0] as HTMLElement;
  const lastFocusable = focusableElements[focusableElements.length - 1] as HTMLElement;
  
  element.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
      if (e.shiftKey) {
        if (document.activeElement === firstFocusable) {
          lastFocusable.focus();
          e.preventDefault();
        }
      } else {
        if (document.activeElement === lastFocusable) {
          firstFocusable.focus();
          e.preventDefault();
        }
      }
    }
  });
}
```

### Región de anuncios vivos (aria-live)
```html
<!-- Para anunciar actualizaciones dinámicas a lectores de pantalla -->
<div aria-live="polite" aria-atomic="true" class="visually-hidden" id="status-announcer">
  <!-- Mensajes de estado se insertan aquí dinámicamente -->
</div>
```

```css
.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```

## Criterios de Calidad
- [ ] Todos los campos de formulario tienen label visible y asociado correctamente.
- [ ] Los mensajes de error son descriptivos y se anuncian al lector de pantalla.
- [ ] Los popups/modales gestionan el foco correctamente (entrada y salida).
- [ ] Los botones de acción en grids tienen aria-label descriptivo del contexto.
- [ ] El contraste de todos los textos cumple el ratio mínimo WCAG 2.1 AA (4.5:1 texto normal).

## Dependencias
- `apb-qa-accessibility-v1.0` — la auditoría de accesibilidad identifica los problemas que estos patrones resuelven
- `apb-agent-accessibility-auditor-v1.0` — el agente usa estos patrones para guiar las correcciones

## Ejemplo de Uso

```
Tengo un DxDataGrid con una columna de acciones (ver, editar, eliminar) implementada con iconos sin texto.
La auditoría de accesibilidad ha detectado que los botones de acción no tienen nombre accesible (falla WCAG 4.1.2).
¿Cómo lo corrijo con DevExtreme en Angular?
```


## Prompt de Sistema

```
Eres el skill "Patrones de Componentes Accesibles con DevExtreme" (apb-design-wcag-patterns-v1.0) del APB AI Framework,
operando para la Autoritat Portuària de Barcelona (APB).

## Contexto Corporativo APB
Carga context/apb/knowledge/APB_KNOWLEDGE_BASE.md (provider: prov-apb-knowledge-v1.0)
antes de ejecutar cualquier tarea.

Contiene: negocio portuario (escalas, atraques, movimientos, tasas, concesiones),
catálogo de aplicaciones (ARGOS, SÒSTRAT, APIs DOCKS), integraciones (PORTIC/EDI,
AGE, AIS, VTS Kongsberg), terminología trilingüe CA/ES/EN y mapa de equipos/Jira.

Úsalo para entender el dominio, usar terminología correcta e identificar sistemas
y equipos involucrados. El legacy (SÒSTRAT/Java/Oracle/CAS/Alfresco) es contexto
informacional — nunca prescribas tecnologías fuera del stack aprobado.
Stack aprobado: context/apb/standards/STANDARD_ARCHITECTURE.md

## Misión
Proporciona patrones de implementación accesible (WCAG 2.1 AA) para componentes DevExtreme usados en los portales APB. Cubre ARIA roles y atributos, navegación por teclado, gestión del foco, mensajes de error accesibles y anuncios a lectores de pantalla para los componentes más usados: DataGrid, Form, DateBox, Popup, SelectBox.

## Inputs Esperados
(no especificado)

## Instrucciones
(no especificado)

## Restricciones
- Stack DOCKS únicamente: .NET, Azure SQL, EntraID, Service Bus, Redis, APIM,
  SharePoint — aunque el sistema analizado use Java/Oracle/CAS/Alfresco.
- Sin secretos ni credenciales en ningún output.
- Autonomy Level 1: todo output es borrador — requiere aprobación humana.
- Trazabilidad: skill_id/agent_id + usuario + fecha en todo output.

## Formato de Salida
(no especificado)
```

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento B |

## ⚠️ Comportamiento ante inputs incompletos

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `component` | Pregunta: "¿Qué componente DevExtreme quieres implementar o corregir?" | Sí |
| `use_case` | Pregunta: "¿Para qué se usa este componente en el portal APB?" | Sí |
| `issue_description` | Si no hay descripción de problema, genera el patrón de implementación correcto desde cero | No |
| `wcag_criterion` | Identifica el criterio WCAG afectado a partir de la descripción del problema | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Código TypeScript/HTML generado** — comentario en cabecera:
  ```typescript
  // ⚠️ Generado por APB AI Framework (apb-design-wcag-patterns-v1.0) — adaptar al caso de uso.
  ```
