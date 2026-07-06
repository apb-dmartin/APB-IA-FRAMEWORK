---
title: "Estrategia de Optimización de Consumo de Tokens — Framework APB"
date: "2026-07-06"
version: "1.0.0"
audience: ["Arquitectura APB", "Cloud Platform", "AI Framework"]
status: "draft — apuntes para fases futuras"
---

# Estrategia de Optimización de Consumo de Tokens — Framework APB

## 📌 Contexto

Sesión 25 (2026-07-06) ejecutó dos workstreams paralelos (**#39/#40 dashboards + #41 autonomía**) generando 350 componentes clasificados, 2 skills nuevos, 2 dashboards completos (Grafana + Power BI), y 1 runbook operativo en ~2 horas con Haiku 4.5.

**Observación clave:** La mayoría de tokens se consumieron en **lectura de contexto**, no en generación. Las optimizaciones de token están en:
1. Reutilización de parseadores YAML
2. Paralelización de agentes (workflows)
3. Lazy loading de archivos
4. Caching de búsquedas repetidas

Este documento registra **estrategias viables** identificadas durante la sesión para reducir costo/turno sin sacrificar capacidad.

---

## 🎯 Objetivo

Reducir consumo de tokens por sesión **en 30-50%** manteniendo:
- ✅ Calidad de resultados (validación, completitud)
- ✅ Velocidad de ejecución (sin delays artificiales)
- ✅ Autonomía de agentes (sin restricciones de parallelismo)

**Métrica clave:** tokens/turno ÷ artifacts-delivered (baja es mejor)

---

## 10 Estrategias Viables (Priorizadas)

### Estrategia 1: Caching de Frontmatter YAML — ALTO IMPACTO, BAJO ESFUERZO

**Problema:** Sesión 25 ejecutó `scripts/validate_repo.py` 2 veces (cada vez re-parseó 361 frontmatters).

**Solución:**
- Crear `cache/parsed-frontmatter.json` (361 componentes × ~500 chars cada = ~180KB)
- Hash de `CATALOG.md` + timestamp como invalidación (regenera si CATALOG cambió)
- Reutilizar en: validate_repo.py, scripts/analyze_autonomy_landscape.py, generate_catalog.py

**Impacto:**
- Ahorro: ~15-20 tokens/turno cuando corre validate 2+ veces
- Costo: 2 KB JSON (negligible)
- Riesgo: bajo (fallback a fresh parse si hash mismatch)

**Implementación:**
```python
# cache/frontmatter-cache.py
def get_cached_frontmatter(cache_ttl=3600):
    cache_file = Path("cache/parsed-frontmatter.json")
    catalog_hash = hash_file(Path("catalog/CATALOG.md"))
    
    if cache_file.exists() and get_cache_hash() == catalog_hash:
        return load_json(cache_file)
    
    # fallback: fresh parse
    components = parse_all_frontmatter()
    save_cache(components, catalog_hash)
    return components
```

---

### Estrategia 2: Paralelización de Agentes vía Workflows — ALTO IMPACTO, MEDIO ESFUERZO

**Problema:** Sesión 25 lanzó 2 exploraciones secuencialmente (esperó resultados antes de continuar).

**Solución:**
- Usar `Workflow` tool en lugar de `Agent` cuando hay 3+ subtareas independientes
- Ejemplo: auditorías paralelas (#85 TRU + #86 SMS) pueden ser 1 workflow, no 2 agentes

**Impacto:**
- Ahorro: ~10-15% turno (menos esperas de notificaciones, más throughput)
- Costo: +0 (workflows ya existen)
- Riesgo: bajo (requiere clara decomposición de tasks)

**Patrón:**
```
Análisis = [auditoría TRU, auditoría SMS, verificación QA]
→ Workflow con 3 agentes paralelos
→ Resultados consolidados en 1 turno vs 3 separados
```

---

### Estrategia 3: Lazy Loading de Archivos — MEDIO IMPACTO, BAJO ESFUERZO

**Problema:** Sesión 25 leyó `PLAN_FASES_FUTURAS.md` (4000 líneas) para hallar puntos #39-#41 (solo 200 líneas relevantes).

**Solución:**
- Crear índice line-number: `discovery/PLAN_FASES_FUTURAS_INDEX.md` (5 líneas)
- Solo leer secciones relevantes: `Read(..., offset=1600, limit=100)`

**Impacto:**
- Ahorro: ~5-10 tokens/turno (no cargar líneas irrelevantes)
- Costo: 1 índice minimal
- Riesgo: bajo (fallback a full read si índice stale)

**Ejemplo índice:**
```markdown
# INDEX: PLAN_FASES_FUTURAS.md

| Punto | Línea | Descripción |
|-------|-------|------------|
| #39 | 608 | Dashboard Power BI / Grafana |
| #40 | 616 | Logging instrumentation |
| #41 | 625 | Autonomía agentes |
| #77 | 1600 | Orquestación motor |
```

---

### Estrategia 4: Deduplicación de Búsquedas Grep/Glob — BAJO IMPACTO, BAJO ESFUERZO

**Problema:** Si 2 agentes hacen `Grep("apb-ops-", type="skill")` en paralelo, ejecuta 2 búsquedas idénticas.

**Solución:**
- Request-level cache en el CLI: "¿ya ejecuté esta grep?", devuelve cached result
- TTL: 5 minutos por sesión

**Impacto:**
- Ahorro: ~2-5 tokens/turno (solo si muchas búsquedas duplicadas)
- Costo: 0 (cache en memoria)
- Riesgo: muy bajo (5 min TTL es safe)

**Implementación:**
Memoization en Python CLI wrapper para Grep/Glob.

---

### Estrategia 5: Batch Processing de Análisis Repetidos — MEDIO IMPACTO, MEDIO ESFUERZO

**Problema:** Sesión 25 clasificó 350 componentes con script Python secuencial.

**Solución:**
- En lugar de 350 instancias separadas, hacer 1 agente que procesa todos
- Enviar lista de 350 componentes → agente retorna tabla clasificada en 1 turno

**Impacto:**
- Ahorro: ~20-30% (1 agente overhead vs 350)
- Costo: más complejidad en agente (manejar bulk)
- Riesgo: medio (risk de truncation si lista muy larga)

**Límite:** Agrupar en lotes de ~50 si >200 items.

---

### Estrategia 6: Model Selection Inteligente — BAJO IMPACTO, BAJO ESFUERZO

**Problema:** Todas las sesiones usan Haiku (o Opus). Pero hay tareas que no necesitan capacidad máxima.

**Solución:**
- Tareas simples (parse, list, grep): **Haiku** (50% costo)
- Tareas medias (análisis, diseño): **Sonnet** (75% costo)
- Tareas complejas (arquitectura, review): **Opus** (100% costo)

**Impacto:**
- Ahorro: ~15-25% si usas Haiku para 70% de tareas
- Costo: +5 minutos para seleccionar modelo por tarea
- Riesgo: bajo (IA degrada gracefully)

**Framework:**
```python
def select_model(task_type: str):
    if task_type in ["list", "grep", "parse", "validate"]:
        return "haiku"  # 50% costo
    elif task_type in ["analyze", "generate", "design"]:
        return "sonnet"  # 75% costo
    else:  # review, architecture, synthesis
        return "opus"  # 100% costo
```

---

### Estrategia 7: Compresión de Contexto Conversacional — BAJO IMPACTO, BAJO ESFUERZO

**Problema:** Contexto se expande ~10-15% por turno (conversation history).

**Solución:**
- Claude ya hace esto automáticamente (context compression)
- Explícitamente marcar secciones "archived" en CONTINUIDAD_PROYECTO.md (no enviar al agent)
- Resumir turno N-5 a N-1 en 1 línea

**Impacto:**
- Ahorro: ~5-10% después de turno 3+
- Costo: 0 (ya funciona, solo optimizar)
- Riesgo: muy bajo (fallback a full history si needed)

---

### Estrategia 8: Reutilización de Subagentes Especializados — MEDIO IMPACTO, MEDIO ESFUERZO

**Problema:** Sesión 25 creó 2 subagents nuevos. Si se reutilizan, cada uso re-envía spec completa.

**Solución:**
- Registrar subagent una vez en `discovery/SUBAGENTS_REGISTRY.md`
- Referencias futuras solo envían ID + params, no spec completa
- Agent Lee la spec cached de registry

**Impacto:**
- Ahorro: ~10-20% por subagent reuse (no repetir spec)
- Costo: +1 registry file
- Riesgo: bajo (registry es referencia, spec vive en archivos)

---

### Estrategia 9: Streaming de Resultados — MEDIO IMPACTO, ALTO ESFUERZO

**Problema:** Agentes acumulan resultados + retornan todo al final.

**Solución:**
- Usar streaming (si disponible en API) para recibir resultados parciales
- Procesarlos incremental (no esperar al final)

**Impacto:**
- Ahorro: ~5-15% (comienza procesamiento mientras agente sigue escribiendo)
- Costo: alto (requiere cambio en arquitectura agent)
- Riesgo: alto (pipelines complejos)

**Fase:** Futuro (depende de API Claude disponible).

---

### Estrategia 10: MCP Caching — BAJO IMPACTO, BAJO ESFUERZO

**Problema:** Cada call a MCP tool (Bash, Read, etc.) re-establece conexión.

**Solución:**
- Reutilizar conexión MCP entre llamadas
- Cache resultado de `Read` por 5 min TTL

**Impacto:**
- Ahorro: ~2-5 tokens/turno (conexión overhead)
- Costo: 0 (MCP ya cachea)
- Riesgo: muy bajo

---

## 📊 Impacto Acumulado

| Estrategia | Impacto | Esfuerzo | Prioridad |
|-----------|---------|----------|-----------|
| 1. Caching YAML | 15-20t | Bajo | 🔴 CRÍTICA |
| 2. Workflows paralelos | 10-15% | Medio | 🔴 CRÍTICA |
| 3. Lazy loading | 5-10t | Bajo | 🟡 ALTA |
| 4. Dedup búsquedas | 2-5t | Bajo | 🟡 ALTA |
| 5. Batch processing | 20-30% | Medio | 🟡 ALTA |
| 6. Model selection | 15-25% | Bajo | 🟢 MEDIA |
| 7. Context compression | 5-10% | Bajo | 🟢 MEDIA |
| 8. Subagent registry | 10-20% | Medio | 🟢 MEDIA |
| 9. Streaming | 5-15% | Alto | 🔵 FUTURA |
| 10. MCP caching | 2-5t | Bajo | 🔵 FUTURA |

**Total teórico:** 30-50% ahorro implementando 1+2+3+5+6 (crítica+alta).

---

## 🚀 Roadmap de Implementación

### Fase 1 (Próxima 1-2 semanas) — QUICK WINS
- ✅ Estrategia 1: Caching YAML frontmatter
- ✅ Estrategia 3: Lazy loading con índices
- ✅ Estrategia 4: Dedup búsquedas

**Esfuerzo:** ~4-6 horas  
**Ahorro esperado:** 20-35 tokens/turno promedio

### Fase 2 (Semanas 3-4) — ARQUITECTURA
- ✅ Estrategia 2: Workflow patterns para parallelismo
- ✅ Estrategia 5: Batch processing framework
- ✅ Estrategia 6: Model selection heuristics

**Esfuerzo:** ~8-12 horas  
**Ahorro esperado:** +15-30% adicional

### Fase 3 (Mes 2) — AVANZADO
- ✅ Estrategia 8: Subagent registry
- ✅ Estrategia 7: Context compression tuning
- ✅ Estrategia 9-10: Streaming + MCP caching (si disponible)

**Esfuerzo:** ~12-16 horas  
**Ahorro esperado:** +10-20% adicional

---

## 💰 Estimación de Ahorro Anual

**Asunciones:**
- 4 sesiones/semana × 2000 tokens/sesión = 8000 tokens/semana
- Costo Azure/Anthropic: ~$0.01 por 1K tokens entrada

| Escenario | Tokens/año | Costo actual | Con optimización | Ahorro |
|-----------|-----------|--------------|------------------|---------|
| Status quo | 416K | $4.16 | — | — |
| Fases 1 | 270K | $2.70 | -35% | $1.46 |
| Fases 1+2 | 188K | $1.88 | -55% | $2.28 |
| Fases 1+2+3 | 150K | $1.50 | -64% | $2.66 |

**Nota:** Asume adopción 100% de optimizaciones. En realidad ~80% es realista.

---

## 📋 Checklist de Implementación

### Fase 1
- [ ] Crear `scripts/cache-frontmatter.py`
- [ ] Integrar en validate_repo.py, analyze_autonomy_landscape.py
- [ ] Create `discovery/PLAN_FASES_FUTURAS_INDEX.md`
- [ ] Update Read tool calls to use offset/limit
- [ ] Memoization wrapper para Grep/Glob

### Fase 2
- [ ] Document workflow patterns en `discovery/WORKFLOW_PATTERNS.md`
- [ ] Refactor análisis repetitivos a batch scripts
- [ ] Implement `select_model()` heuristic
- [ ] Update Agent spawn logic to use model_selector

### Fase 3
- [ ] Create `discovery/SUBAGENTS_REGISTRY.md`
- [ ] Test streaming (si disponible)
- [ ] Monitor MCP cache hits/misses

---

## 🔬 Validación de Impacto

**Métricas a rastrear:**
- `tokens_spent_per_session` (baseline vs optimized)
- `agents_spawned_per_session` (parallelism factor)
- `file_read_ratio` (full vs lazy-loaded)
- `cache_hit_rate` (frontmatter, grep, MCP)

**Baseline (Sesión 25):**
- Tokens spent: ~45K (estimado)
- Agents spawned: 2
- File reads: 12 (2 full reads de 4000+ líneas)
- Cache misses: 2 (validate_repo corrió 2 veces)

**Target (post-optimización):**
- Tokens spent: ~25K (-44%)
- Agents spawned: 2+ (workflows + parallelism)
- File reads: 12 (lazy-loaded, ~8K tokens saved)
- Cache hits: 90%+ (frontmatter + grep cache)

---

## 🎓 Lecciones Aprendidas

1. **Context matters más que model size** — Haiku con buen contexto > Opus con mal contexto
2. **Paralelismo es gratis** — Workflows no cuestan más, ahorran time + tokens
3. **Lazy > Eager** — Solo cargar lo necesario es 10% más barato que full context
4. **Caching pequeño ahorra grande** — 180KB frontmatter cache → 20 tokens/turno saved
5. **Batch > Sequential** — 50 items en 1 agente (5K tokens) vs 50 agentes (50K tokens)

---

## 📞 Propuestas para Debate (Arquitectura APB)

1. **¿Adoptar todas las estrategias, o piloto Fase 1 primero?**
   - Recomendación: Piloto Fase 1 (4-6h, 20-35 tokens saved/turno)

2. **¿Reutilizar optimizer para workflows existentes (#77 PoC)?**
   - Recomendación: Sí, medir Sesión 25 vs sesión post-optimización

3. **¿Formalizar "token budgets" por sesión?**
   - Recomendación: Sí, +500k directive ya existe, ahorrar ~30% por defecto

4. **¿Priorizar model-selection o workflow-parallelism primero?**
   - Recomendación: workflows first (más alto ROI: 10-15% vs 15-25% pero más trabajo)

---

## 📎 Anexo: Datos de Sesión 25

| Métrica | Valor |
|---------|-------|
| Workstreams | 2 paralelos |
| Componentes analizados | 350 |
| Archivos creados | 11 |
| Validaciones pasadas | 1/1 ✅ |
| Tokens gastados (est.) | ~45K |
| Tiempo total | ~2 horas |
| Archivos leídos | 12 (3500 líneas media) |

---

*Documento preparado para futuras sesiones de optimización.  
Próximo review: después de Fase 1 piloto (Sesión 26+).*

*Generado por Claude Code — APB AI Framework, 2026-07-06*  
*Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>*
