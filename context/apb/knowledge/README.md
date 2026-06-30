# context/apb/knowledge — Contexto Corporativo APB

Este directorio contiene la **base de conocimiento de negocio y tecnológica** de la
Autoritat Portuària de Barcelona, destinada al entrenamiento y contextualización de
los agentes IA del framework.

## Contenido

| Fichero | Descripción |
|---------|-------------|
| [APB_KNOWLEDGE_BASE.md](APB_KNOWLEDGE_BASE.md) | Knowledge base consolidada: negocio portuario, catálogo de aplicaciones (DOCKS y legacy), integraciones, terminología, equipos y mapa Jira |

## Propósito y Límites

El conocimiento aquí documentado **contextualiza** a los agentes sobre:
- El negocio portuario (escalas, atraques, movimientos, tasas, concesiones…)
- Los sistemas existentes, incluyendo legacy (SÒSTRAT, Alfresco, CAS, Oracle…)
- Las integraciones externas (PORTIC/EDI, AGE, AIS, VTS Kongsberg…)
- La terminología trilingüe (CA/ES/EN) propia del sector marítimo-portuario
- Los equipos, proveedores y proyectos Jira de la organización

**Este directorio NO modifica los estándares tecnológicos aprobados.**
Los agentes deben usar este contexto para comprender tickets e integraciones,
pero NUNCA para prescribir tecnologías fuera del stack DOCKS aprobado.

Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Proveedor Asociado

Este directorio es indexado por: `providers/prov-apb-knowledge-v1.0.md`
