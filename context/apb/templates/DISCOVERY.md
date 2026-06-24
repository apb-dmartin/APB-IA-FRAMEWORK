# Template: Evidencia de Discovery

> **Uso:** Documentar la revisión de alternativas antes de crear una skill APB propia.
> **Ubicación:** `discovery/`
> **Convención de nombre:** `discovery-{dominio}-{nombre}-YYYY-MM-DD.md`

---

## 1. Metadatos

```yaml
---
id: "discovery-{dominio}-{nombre}-YYYY-MM-DD"
skill_proposed: "apb-{dominio}-{nombre}-v{major}.{minor}"
author: "Nombre Apellido <arquitectura@portdebarcelona.cat>"
date: "YYYY-MM-DD"
domain: "{architecture | development | qa | platform | pm | security | governance | orchestration}"
---
```

## 2. Necesidad de Negocio

Describir la necesidad que motiva la creación de esta skill. ¿Qué problema resuelve? ¿Por qué no existe una solución satisfactoria en el framework actual?

## 3. Alternativas Revisadas

### 3.1 MCP Oficiales

| MCP | Descripción | Estado de revisión | Conclusión |
|-----|-------------|-------------------|------------|
| GitHub MCP | {Descripción} | ✅ Revisado | {Descartado / Referenciado / Adaptado} |
| Azure MCP | {Descripción} | ⏳ Pendiente | {Conclusión} |
| Microsoft Learn | {Descripción} | ❌ No aplica | {Conclusión} |
| DevExpress | {Descripción} | {Estado} | {Conclusión} |
| Playwright | {Descripción} | {Estado} | {Conclusión} |
| Sonar | {Descripción} | {Estado} | {Conclusión} |
| Atlassian | {Descripción} | {Estado} | {Conclusión} |
| k6 | {Descripción} | {Estado} | {Conclusión} |

### 3.2 Skills Oficiales

| Skill | Fuente | Estado de revisión | Conclusión |
|-------|--------|-------------------|------------|
| Anthropic Skills | Anthropic | {Estado} | {Conclusión} |
| OpenSpec | OpenSpec | {Estado} | {Conclusión} |

### 3.3 Comunidad

| Skill / Framework | Fuente | Licencia | Estado de revisión | Conclusión |
|-------------------|--------|----------|-------------------|------------|
| skills.sh | skills.sh | {Licencia} | {Estado} | {Conclusión} |
| Composio | Composio | {Licencia} | {Estado} | {Conclusión} |
| SuperClaude | SuperClaude | {Licencia} | {Estado} | {Conclusión} |
| Mukul Cybersecurity Skills | GitHub | {Licencia} | {Estado} | {Conclusión} |
| LightRAG | GitHub | {Licencia} | {Estado} | {Conclusión} |
| Graphify | GitHub | {Licencia} | {Estado} | {Conclusión} |
| Rowboat | Rowboat | {Licencia} | {Estado} | {Conclusión} |
| LIDR | GitHub | {Licencia} | {Estado} | {Conclusión} |
| UI UX Pro Max | {Fuente} | {Licencia} | {Estado} | {Conclusión} |

## 4. Análisis Comparativo

| Criterio | Alternativa 1 | Alternativa 2 | Alternativa 3 | Skill APB Propuesta |
|----------|--------------|--------------|--------------|---------------------|
| Cobertura funcional | {Nota} | {Nota} | {Nota} | {Nota} |
| Compatibilidad APB | {Nota} | {Nota} | {Nota} | {Nota} |
| Licencia | {Nota} | {Nota} | {Nota} | {Nota} |
| Mantenimiento | {Nota} | {Nota} | {Nota} | {Nota} |
| Curva de aprendizaje | {Nota} | {Nota} | {Nota} | {Nota} |
| Integración con framework | {Nota} | {Nota} | {Nota} | {Nota} |

## 5. Decisión

| Atributo | Valor |
|----------|-------|
| **Decisión** | Crear skill APB propia / Reutilizar tercero / Adaptar tercero |
| **Justificación** | {Razón de la decisión} |
| **Skill resultante** | `apb-{dominio}-{nombre}-v{major}.{minor}` |
| **Dependencias de terceros** | {Si aplica} |
| **Wrapper requerido** | {Sí/No — ID del wrapper} |

## 6. Riesgos Identificados

| Riesgo | Mitigación |
|--------|------------|
| {Riesgo 1} | {Mitigación} |
| {Riesgo 2} | {Mitigación} |

## 7. Aprobación

| Rol | Nombre | Fecha | Estado |
|-----|--------|-------|--------|
| Arquitecto de Referencia | {Nombre} | YYYY-MM-DD | ✅ Aprobado / ⏳ Pendiente |
| QA Lead | {Nombre} | YYYY-MM-DD | ✅ Aprobado / ⏳ Pendiente |

---

## Checklist de Discovery

- [ ] MCP oficiales revisados.
- [ ] Skills oficiales revisadas.
- [ ] Alternativas de comunidad revisadas.
- [ ] Análisis comparativo documentado.
- [ ] Decisión justificada.
- [ ] Riesgos identificados y mitigados.
- [ ] Aprobación de Arquitectura (si aplica).
