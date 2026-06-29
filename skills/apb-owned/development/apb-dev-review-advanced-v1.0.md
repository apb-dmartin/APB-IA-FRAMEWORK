---
id: "apb-dev-review-advanced-v1.0"
name: "Revisión Técnica Avanzada"
description: "Revisión técnica avanzada multi-perspectiva: arquitectura, patrones, escalabilidad, resiliencia, seguridad y calidad, mediante checklists especializados (bugs, seguridad, performance, calidad, contratos, consistencia histórica)."
version: "1.1.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "development"
created_date: "2026-06-20"
review_date: "2026-06-22"
autonomy_level: 1
depends_on:
  - "apb-arch-validate-v1.0"
---

# Revisión Técnica Avanzada

> Esta skill incorpora, fusionados y adaptados, contenidos de la skill de terceros
> `NeoLabHQ/context-engineering-kit` (plugin `review`) bajo licencia MIT. Ver
> sección 9, Procedencia.

## 1. Propósito

Realizar revisiones técnicas de alto nivel enfocadas en arquitectura, patrones
avanzados, escalabilidad, resiliencia, seguridad y calidad — evaluando decisiones
de diseño de largo alcance más allá del code review estándar.

## 2. Trigger

Cambios arquitectónicos significativos, introducción de nuevas tecnologías,
revisiones periódicas de componentes críticos, o código de alto impacto antes
de un release.

## 3. Input / Output

**Input:** documento de arquitectura del cambio, ADRs asociados, código de
referencia, métricas de performance actuales, riesgos técnicos conocidos.

**Output:** informe de revisión avanzada con score general (pass/warn/fail),
findings priorizados por impacto y confianza, métricas (coverage, complejidad,
duplicación, vulnerabilidades), comparativa con baseline, y action items con
prioridad y owner sugerido.

## 4. Checklists por Área de Análisis

### 4.1 Bugs y casos límite
- [ ] Null/None/nil dereferences.
- [ ] Off-by-one en loops y arrays; race conditions en código concurrente.
- [ ] Resource leaks (files, conexiones, memoria).
- [ ] Exception handling incompleto (excepciones silenciadas, catch-all).
- [ ] Integer overflow/underflow; type coercion incorrecto.
- [ ] Errores de propagación (fallos enmascarados como éxito).

### 4.2 Seguridad
- [ ] Inyección (SQL, NoSQL, comandos OS, LDAP, XPath).
- [ ] Autenticación rota (contraseñas débiles, fijación de sesión, problemas JWT).
- [ ] Exposición de datos sensibles (PII, credenciales, cifrado).
- [ ] Control de acceso roto (IDOR, path traversal, escalada de privilegios).
- [ ] Configuración de seguridad insegura (credenciales por defecto, CORS abierto).
- [ ] XSS, deserialización insegura, componentes con vulnerabilidades conocidas (SCA).
- [ ] Logging y monitorización insuficientes.

### 4.3 Performance
- [ ] Complejidad algorítmica (loops anidados, algoritmos exponenciales).
- [ ] Problema N+1 (lazy loading de ORM).
- [ ] Memory leaks (referencias circulares, recursos sin cerrar).
- [ ] I/O bloqueante en contextos async.
- [ ] Estructuras de datos ineficientes; caching ausente en cómputos repetidos.
- [ ] Optimización de queries (índices faltantes, full table scans).

### 4.4 Calidad de código
- [ ] Complejidad ciclomática > 10 por método; complejidad cognitiva > 15.
- [ ] Método > 50 líneas; clase > 500 líneas; > 4 parámetros por método.
- [ ] Duplicación de código > 6 líneas; anidamiento profundo (> 4 niveles).
- [ ] Números/strings mágicos; convenciones de nombres inconsistentes.

### 4.5 Contratos y APIs
- [ ] Estrategia de versionado de API definida.
- [ ] Breaking changes en APIs públicas (campos eliminados, tipos cambiados).
- [ ] Validación de input completa (nulls, vacíos, longitud, formato).
- [ ] Consistencia de respuestas de error; estrategia de paginación.
- [ ] Idempotency keys en operaciones no seguras; compatibilidad backward.

### 4.6 Consistencia histórica
- [ ] Consistencia con patrones existentes en el codebase (DRY).
- [ ] No reintroduce bugs previamente corregidos (revisar historial git).
- [ ] Alineación con ADRs y decisiones arquitectónicas previas.
- [ ] No reintroduce patrones deprecados; considera feedback de reviews previas.

## 5. Proceso

1. **Contexto** — entender el alcance estratégico del cambio.
2. **Análisis de patrones** — ¿son apropiados? ¿hay alternativas mejores?
3. **Escalabilidad** — ¿soporta 10x carga? ¿cuellos de botella?
4. **Resiliencia** — circuit breakers, retries, fallbacks, bulkheads, graceful degradation.
5. **Consistencia y transacciones** — ACID vs. eventual consistency, sagas, compensaciones.
6. **Observabilidad y seguridad** — diagnosticabilidad en producción, threat model.
7. **Coste operativo** — complejidad, mantenimiento, onboarding.
8. **Síntesis** — consolidar findings de las 6 áreas (sección 4), eliminar
   duplicados, priorizar por impacto y confianza (sección 6).
9. **Recomendaciones** — accionables, con prioridad y justificación; documentar
   en ADR si implican cambio de dirección.

## 6. Scoring: Impacto y Confianza

| Impacto | Descripción | Ejemplo | Bloquea merge |
|---|---|---|---|
| CRITICAL | Bug de seguridad, pérdida de datos, crash en producción | SQL injection, race condition en pago | Sí |
| HIGH | Bug funcional, performance severa, breaking change | N+1 en endpoint popular | Sí |
| MEDIUM | Code smell, mantenibilidad, test faltante | Método de 100 líneas | No (con plan) |
| LOW | Estilo, naming, optimización menor | Variable poco descriptiva | No |
| INFO | Sugerencia u observación | "Considerar patrón X" | No |

| Confianza | Descripción | Acción |
|---|---|---|
| CERTAIN | Evidente y reproducible | Fix obligatorio |
| LIKELY | Muy probable, patrón conocido | Fix recomendado |
| POSSIBLE | Requiere verificación manual | Revisar y confirmar |
| UNCERTAIN | Especulativo, depende de contexto | Discutir o ignorar |

Umbral por defecto recomendado: `min_impact: medium`, `min_confidence: likely`.

## 7. Anti-patrones de Review (qué evitar)

- Falsos positivos que reducen la confianza en la herramienta.
- Nitpicking de estilo menor ignorando bugs críticos.
- Aplicar reglas rígidamente sin considerar el contexto de negocio.
- Confiar ciegamente en herramientas automáticas sin verificación humana.
- No comparar con el estado previo del codebase (baseline).
- Generar demasiados findings de bajo impacto (alert fatigue).
- Reportar issues sin verificar después que se corrigieron.

## 8. Reglas y Constraints

- Evaluar trade-offs de forma explícita; no existen arquitecturas perfectas.
- Identificar anti-patrones de sistema (distributed big ball of mud, god
  service, chatty services, shared database).
- Recomendar PoC cuando haya incertidumbre técnica significativa.
- Preferir consistencia eventual a transacciones distribuidas cuando sea posible.
- Esta skill requiere experiencia arquitectónica; su output debe revisarlo un
  arquitecto senior antes de aplicarse — no usar para cambios triviales.

## 9. Procedencia y Licencia

La sección 4 (checklists por área), 6 (scoring) y 7 (anti-patrones) están
adaptadas de la skill `review` de `NeoLabHQ/context-engineering-kit`, licencia
MIT. Referencias adicionales: OWASP Code Review Guide, SonarQube Quality Gates.

## 10. Dependencias

- `apb-arch-validate-v1.0`

## 11. Relacionadas (no son dependencias de ejecución)

- `apb-dev-review-tl-v1.0` — la revisión de Tech Lead se apoya en el output
  de esta skill para la decisión final de aprobación; el sentido de la
  relación es Review TL → Review Advanced, no a la inversa.


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-dev-review-advanced-v1.0) - pendiente validacion humana. No distribuir sin revision.
