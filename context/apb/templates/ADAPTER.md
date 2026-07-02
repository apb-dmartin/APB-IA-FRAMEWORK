# {name}

> **ID:** `{id}`
> **Versión:** {version}
> **Estado:** {status}
> **Runtime Target:** {runtime}
> **Owner:** {owner}

---

## 🎯 Propósito

{purpose}

## 🔧 Runtime Soportado

{runtime_details}

## 📦 Componentes Adaptados

| Tipo | Componente | ID | Estado |
|------|-----------|-----|--------|
{components_table}

## 🔌 Interface de Adaptación

{interface}

## ⚙️ Configuración

{configuration}

## 🔄 Mapeo de Capacidades

{capability_mapping}

## 📥 Formato de Input

{input_format}

## 📤 Formato de Output

{output_format}

## 🚫 Limitaciones del Runtime

{runtime_limitations}

## 🔒 Seguridad

{security}

## 📝 Ejemplo de Uso

```yaml
adapter: {id}
runtime: {runtime}
config:
{usage_example}
```

## 🔄 Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| {version} | {date} | Arquitectura APB | Creación inicial |

---

## 🧭 Estándar de Prompting (PROMPTING_STANDARD v1.0) — secciones aplicables

> El adapter traduce componentes al runtime; debe **preservar** el bloque Estándar de Prompting
> de los componentes que adapta. Ver [`PROMPTING_STANDARD`](../standards/PROMPTING_STANDARD.md) §5.

### Objetivo
{Criterio de éxito verificable: el componente adaptado conserva prompt de sistema, gates y estándar de prompting en el runtime destino.}

### Qué NO hacer
- No omitir ni degradar las secciones del Estándar de Prompting al adaptar un componente.
- No introducir capacidades específicas del runtime que violen las restricciones del componente original.
- Las 11 prohibiciones de [`PROMPTING_STANDARD §2`](../standards/PROMPTING_STANDARD.md) aplican al output adaptado.

### Separación SISTEMA / USUARIO
El adapter garantiza que el runtime destino mantenga la separación: instrucciones del componente (SISTEMA) vs. contenido del usuario (USUARIO).

---
*Documento generado por el APB AI Framework. Requiere revisión humana antes de aprobación.*
