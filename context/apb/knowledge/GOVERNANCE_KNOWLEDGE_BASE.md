---
id: "prov-apb-knowledge-governance-v1.0"
name: "Gobernanza de APB_KNOWLEDGE_BASE"
description: >
  Proceso de gobernanza para el mantenimiento, actualización y validación de
  APB_KNOWLEDGE_BASE.md — la base de conocimiento corporativo que alimenta a
  todos los agentes y skills del APB AI Framework.
version: "1.0.0"
status: "approved"
owner: "Debora Martin <deboramv@gmail.com>"
domain: "governance"
created_date: "2026-06-30"
review_date: "2026-06-30"
---

# Gobernanza de APB_KNOWLEDGE_BASE

> ⚠️ Borrador generado por IA — revisado y aprobado por Debora Martin (Tech&Ops, APB).

---

## 1. Propósito

`APB_KNOWLEDGE_BASE.md` es el fichero que dota a todos los agentes IA del framework de
contexto corporativo (negocio portuario, sistemas, integraciones, terminología).
Una knowledge base desactualizada produce respuestas incorrectas con alta confianza:
peor que no tener contexto.

Este documento define quién puede actualizarla, cuándo, cómo y quién aprueba.

---

## 2. Propietario y Revisores

| Rol | Persona | Responsabilidad |
|-----|---------|-----------------|
| **Propietario (Owner)** | Debora Martin (Tech&Ops / CTO) | Aprobación final de cualquier cambio |
| **Revisor Funcional** | Responsables funcionales por dominio (ver §5) | Validar exactitud del contenido de negocio |
| **Revisor Técnico** | Arquitectura APB (Alina Suros / Manuel Villalonga) | Validar exactitud del stack tecnológico y APIs |
| **Contribuidor** | Cualquier miembro del equipo SSI | Propone cambios vía PR |

---

## 3. Triggers de Actualización

La knowledge base **debe** actualizarse cuando ocurre cualquiera de estos eventos:

### 3.1. Obligatorio (bloqueante — actualizar antes del próximo sprint)

| Evento | Sección afectada |
|--------|-----------------|
| Nueva aplicación entra en producción | §4 Catálogo de Aplicaciones |
| API nueva registrada en APIM | §4.4 APIs del Framework ARQ |
| Cambio de equipo responsable de un sistema | §10 Tabla Jira/Equipo/GitHub |
| Nuevo proyecto Jira creado para un sistema | §13 Mapa de proyectos |
| Cambio en el stack aprobado (STANDARD_ARCHITECTURE) | §3 Arquitectura DOCKS |
| Nuevo término de negocio portuario incorporado | §12 Diccionario |
| Cambio en el modelo de contratación | §8 Modelo de Contratación |

### 3.2. Recomendado (actualizar en el sprint siguiente)

| Evento | Sección afectada |
|--------|-----------------|
| Aplicación legacy dada de baja | §4 (marcar como retirada o eliminar) |
| Cambio de proveedor | §8.1 Proveedores Principales |
| Nueva integración con sistema externo | §5 Integraciones |
| Actualización de política de migración GoToCloud | §6 Estrategia GoToCloud |
| Cambio significativo en la estructura organizativa SSI | §1.3 Departamento SSI |

### 3.3. Revisión periódica (trimestral)

- Verificar que todos los equipos y personas listados siguen siendo correctos.
- Revisar el estado de las migraciones en curso (§6.2).
- Actualizar la fecha `review_date` del frontmatter.
- Ejecutar `validate_repo.py` tras cualquier cambio.

---

## 4. Proceso de Actualización

### 4.1. Flujo estándar (cambios de contenido)

```
1. Identificar el trigger (§3)
2. Crear rama: knowledge/update-{descripcion-corta}
3. Editar APB_KNOWLEDGE_BASE.md — solo la sección afectada
4. Actualizar review_date en el frontmatter
5. Abrir PR con:
   - Título: "[knowledge] {descripción del cambio}"
   - Label: "knowledge-base"
   - Descripción: trigger que motivó el cambio + secciones modificadas
   - Reviewer: Propietario + Revisor del dominio afectado (ver §5)
6. Revisión humana (mínimo 1 aprobación del Propietario o Revisor Técnico)
7. Merge en main
8. Ejecutar generate_catalog.py + validate_repo.py
```

### 4.2. Flujo urgente (corrección de error factual)

Si un agente IA produce una respuesta incorrecta porque la knowledge base tiene un error:

```
1. Abrir issue Jira en proyecto ARQ con label "knowledge-base-error"
2. Fix directo en rama hotfix/knowledge-{descripcion}
3. PR con aprobación exprés del Propietario (SLA: 24h)
4. Merge + notificación al equipo
```

### 4.3. Proceso de aportación desde equipos funcionales

Los equipos de negocio (ARGOS, SÒSTRAT, AE, GIS…) pueden aportar contexto sin acceso directo al repo:

1. Abrir ticket Jira en ARQ con label `knowledge-base-update`.
2. Adjuntar la información nueva/corregida en formato libre.
3. El equipo de Arquitectura transforma el contenido al formato del fichero y abre el PR.
4. El equipo funcional valida el contenido antes del merge.

---

## 5. Revisores por Dominio

| Dominio | Revisor Funcional |
|---------|------------------|
| Operaciones Marítimas (ARGOS/MDE) | Alberto Ponseti |
| SÒSTRAT / Escalas / Facturación | Xavier Estebanell |
| Mercancías / PORTIC / EDI | Enrique Salinas |
| Ferrocarril | Toni Estrada |
| Concesiones | Elisabeth Fernandez |
| Administración Electrónica | Manuel Martinez |
| GIS / Plano del Puerto | (responsable GIS APB) |
| Seguridad / Policía Portuaria | Albert Prats |
| Infraestructura / Cloud | Israel Perez |
| Arquitectura DOCKS | Alina Suros / Manuel Villalonga |
| Contratación / Proveedores | (responsable OSMA) |

---

## 6. Restricciones de Contenido

**Lo que SÍ debe estar en APB_KNOWLEDGE_BASE.md:**

- Procesos y conceptos de negocio portuario (escalas, atraques, tasas, EDI…)
- Catálogo de aplicaciones con su estado real (incluido legacy)
- Terminología técnica y de negocio con definiciones precisas
- Equipos, proyectos Jira y repos GitHub por dominio
- Integraciones con sistemas externos (PORTIC, AGE, AIS, VTS…)
- Estrategia GoToCloud y migraciones en curso

**Lo que NO debe estar en APB_KNOWLEDGE_BASE.md:**

| Tipo de contenido | Dónde va |
|-------------------|----------|
| Estándares tecnológicos aprobados | `context/apb/standards/STANDARD_ARCHITECTURE.md` |
| Políticas de seguridad | `context/apb/policies/security/` |
| Políticas QA | `context/apb/policies/quality/POLICY_QA_v1.0.md` |
| Credenciales, tokens, secrets | Nunca en el repo — Azure Key Vault |
| Datos personales de empleados (más allá de nombre/rol) | Nunca en el repo |
| Código fuente o fragmentos de implementación | Repos GitHub correspondientes |
| Contenido clasificado (ENS nivel ALTO/CRÍTICO) | Canales seguros APB |

---

## 7. Versionado y Changelog

El fichero usa versionado semántico en el frontmatter:

| Tipo de cambio | Incremento |
|----------------|-----------|
| Corrección de error factual (nombre, fecha, estado) | `patch`: 1.0.0 → 1.0.1 |
| Adición de nueva aplicación, equipo o integración | `minor`: 1.0.0 → 1.1.0 |
| Reestructuración de secciones o cambio de modelo | `major`: 1.0.0 → 2.0.0 |

Mantener un `## Changelog` al final del fichero con las últimas 5 entradas:

```markdown
## Changelog

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-30 | Debora Martin | Versión inicial consolidada (v1+v2+v3) |
```

---

## 8. Validación Automática

El script `validate_repo.py` incluye estas comprobaciones sobre APB_KNOWLEDGE_BASE.md:

| Check | Fallo si… |
|-------|-----------|
| Frontmatter válido | Campos obligatorios ausentes o mal formados |
| `review_date` reciente | Fecha > 90 días sin actualización → WARNING |
| Sin secretos | El fichero contiene patrones de token/password → ERROR |
| Secciones obligatorias | Faltan secciones 1-14 → WARNING |

---

## 9. Relación con Otros Documentos

| Documento | Relación |
|-----------|----------|
| `STANDARD_ARCHITECTURE.md` | Fuente de verdad del stack aprobado. La KB describe lo que existe; el estándar prescribe lo que debe usarse. Nunca entran en conflicto: si un sistema legacy usa Java, la KB lo documenta y el estándar sigue prohibiendo Java para nuevos desarrollos. |
| `POLICY_ARCHITECTURE_BASE.md` | Políticas que los agentes deben aplicar. La KB da contexto; las políticas dan reglas. |
| `prov-apb-knowledge-v1.0.md` | Provider que indexa este directorio para los agentes. Se actualiza si cambia la estructura de carpetas. |
| `validate_repo.py` | Debe incluir las comprobaciones del §8. |

---

## 10. SLA de Actualización

| Tipo de cambio | SLA |
|----------------|-----|
| Error factual crítico (agente produce dato incorrecto) | 24 horas |
| Nuevo sistema en producción | 1 sprint (2 semanas) |
| Cambio de equipo o responsable | 1 sprint |
| Revisión periódica trimestral | Tercer mes de cada trimestre |

---

*Documento generado el 2026-06-30. Propietario: Debora Martin (Tech&Ops, APB).*
