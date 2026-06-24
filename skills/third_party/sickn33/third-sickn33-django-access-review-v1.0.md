---
id: "third-sickn33-django-access-review-v1.0"
name: "Skill: Django Access Control & IDOR Review (antigravity-awesome-skills)"
description: "Metodología de investigación (no pattern-matching) para revisar control de acceso y vulnerabilidades IDOR en vistas Django/DRF, trazando el flujo desde el ID de recurso hasta la consulta ORM para confirmar si existe un control de autorización real, adaptada del repositorio público sickn33/antigravity-awesome-skills."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "qa"
autonomy_level: 1
source_repo: "https://github.com/sickn33/antigravity-awesome-skills"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-24"
created_date: "2026-06-24"
review_date: "2026-06-24"
---

# Skill: Django Access Control & IDOR Review (antigravity-awesome-skills)

---

## Descripción
Adaptación de la skill `django-access-review` del repositorio público
`sickn33/antigravity-awesome-skills`. El contenido incluye una nota de
licencia embebida en el propio fichero de origen que referencia
explícitamente el **OWASP Cheat Sheet Series (CC BY-SA 4.0)** como
material de referencia base, además de la licencia MIT general del
repositorio contenedor para código/tooling. La metodología original
plantea la revisión de control de acceso como una **investigación dirigida
por preguntas**, no como un escaneo de patrones predefinidos: entender cómo
funciona la autorización en el código concreto, trazar el flujo desde el ID
de recurso hasta la consulta de base de datos, y solo reportar hallazgos
confirmados mediante esa traza.

> **Nota de gobernanza:** identificada en la Sesión 9 dentro del agregador
> `sickn33/antigravity-awesome-skills`. Es la skill de mayor relevancia
> directa para APB de las seis incorporadas en esta sesión: el stack GIS de
> APB usa Django/DRF/GeoDjango, y esta skill cubre exactamente ese
> ecosistema. Doble atribución a respetar: MIT (repositorio contenedor) +
> CC BY-SA 4.0 (OWASP Cheat Sheet Series, material de referencia base).

## Capacidades
- Fase 1 — Entender el modelo de autorización real del código (decoradores,
  middleware, clases base, `permission_classes` de DRF, managers
  personalizados) antes de buscar fallos
- Fase 2 — Mapear la superficie de ataque: qué modelos contienen datos de
  usuario, qué endpoints exponen operaciones sobre ellos
- Fase 3 — Investigar cada endpoint sensible respondiendo "si soy el
  Usuario A y conozco el ID de un recurso del Usuario B, ¿puedo acceder a
  él?", trazando el código desde la entrada del ID hasta la consulta
- Fase 4 — Trazar flujos concretos con comandos de investigación (`grep`
  sobre `permission_classes`, `get_queryset`, managers, campos de
  ownership)
- Fase 5 — Reportar únicamente hallazgos confirmados, con niveles de
  confianza (alta/media/baja) y una corrección que **aplique** la
  autorización en código, nunca solo un comentario o docstring

## Inputs
- `codigo_django`: vistas, viewsets DRF, o managers a revisar
- `modelo_ownership`: cómo se modela la propiedad de los datos (usuario,
  organización/tenant, jerárquico)

## Outputs
- `modelo_autorizacion_detectado`: cómo se implementa la autorización en
  el código revisado
- `hallazgos_idor`: lista de hallazgos confirmados con nivel de confianza,
  evidencia, e impacto
- `correcciones_propuestas`: código que aplica autorización real, no solo
  documentación de la carencia

## Restricciones
- La metodología exige confirmación por traza de código antes de reportar
  cualquier hallazgo; no debe usarse como escáner automático de patrones
  sospechosos sin la fase de investigación
- Las correcciones propuestas deben incluir código que fuerce la
  validación (excepción si no autorizado), nunca un comentario indicando
  que "el llamador debe validar"
- No sustituye `apb-sub-dev-django-v1.0` (subagente Django) para el desarrollo
  general; esta skill es específica de revisión de control de acceso/IDOR

## Adaptaciones APB
- Aplicar especialmente sobre el código GeoDjango/GIS de APB, dado que los
  datos geoespaciales (escalas, infraestructura portuaria) pueden tener
  requisitos de visibilidad por organización/rol no triviales
- Los hallazgos confirmados deben registrarse conforme a
  `POLICY_VULNERABILITY_MANAGEMENT_v1.1.md` para trazabilidad ENS
- Conectar como consumidor a `apb-sub-dev-django-v1.0` y `apb-sub-qa-security-v1.0`

## Ejemplo de Uso
```
Invocar: third-sickn33-django-access-review-v1.0
Input: { codigo_django: "EscalaPortuariaViewSet en api/views.py",
         modelo_ownership: "organización (terminal operador)" }
Output: Modelo de autorización detectado (o ausencia confirmada),
        hallazgo IDOR con nivel de confianza y evidencia de traza, y
        corrección de código que aplica el filtro por organización
```

---
*Adaptado por APB AI Framework. Licencias MIT (repositorio) y CC BY-SA 4.0
(OWASP Cheat Sheet Series, material de referencia base) respetadas.*
