---
id: "third-sickn33-screen-reader-testing-v1.0"
name: "Skill: Screen Reader Testing (antigravity-awesome-skills)"
description: "Guía práctica para validar accesibilidad de aplicaciones web con lectores de pantalla (VoiceOver, NVDA, JAWS, TalkBack): comandos esenciales, checklists de prueba, patrones comunes de ARIA/focus, y problemas frecuentes con su corrección, adaptada del repositorio público sickn33/antigravity-awesome-skills."
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

# Skill: Screen Reader Testing (antigravity-awesome-skills)

---

## Descripción
Adaptación de la skill `screen-reader-testing` del repositorio público
`sickn33/antigravity-awesome-skills` (MIT para código/tooling; contenido sin
atribución externa adicional, autoría `community`). El contenido original
es una guía práctica de testing de accesibilidad con los lectores de
pantalla principales (VoiceOver/macOS-iOS, NVDA/Windows, JAWS/Windows,
TalkBack/Android), con comandos esenciales por lector, checklists de
prueba por categoría (navegación, formularios, contenido dinámico, tablas),
y patrones HTML/ARIA de corrección para problemas comunes (modales, live
regions, interfaces de pestañas).

> **Nota de gobernanza:** identificada en la Sesión 9 dentro del agregador
> `sickn33/antigravity-awesome-skills`. **Cubre un gap real del framework**:
> APB tiene como requisito explícito el cumplimiento de **WCAG 2.1 AA**
> (`proyecto.md` §2), pero no existía hasta ahora ninguna skill, propia ni
> de terceros, dedicada específicamente a testing con lectores de pantalla.
> El `SKILL.md` superficial del agregador es un placeholder mínimo; el
> contenido sustantivo reside en su `resources/implementation-playbook.md`
> asociado, que es lo que se ha adaptado aquí.

## Capacidades
- Tabla de cuota de uso y combinación recomendada navegador/lector
  (NVDA+Firefox, VoiceOver+Safari como cobertura mínima; JAWS+Chrome,
  TalkBack+Chrome, Narrator+Edge para cobertura exhaustiva)
- Comandos esenciales de navegación, lectura e interacción por lector de
  pantalla (VoiceOver, NVDA, JAWS, TalkBack)
- Checklists de prueba estructuradas: carga de página, navegación por
  encabezados/landmarks, formularios, contenido dinámico, tablas
- Patrones de corrección HTML/ARIA para problemas frecuentes: botones sin
  nombre accesible, contenido dinámico no anunciado (`aria-live`), errores
  de formulario no leídos (`aria-describedby`, `role="alert"`)
- Patrones completos de componentes accesibles: modal con foco atrapado,
  live regions (`polite`/`assertive`/`log`), interfaz de pestañas con
  navegación por teclado

## Inputs
- `componente_a_validar`: vista, formulario, o componente DevExpress/
  Blazor a validar
- `lector_objetivo`: lector(es) de pantalla prioritarios para la prueba

## Outputs
- `checklist_aplicado`: checklist de prueba ejecutado con resultado por
  ítem
- `incidencias_detectadas`: problemas de accesibilidad encontrados con su
  patrón de corrección
- `script_prueba`: guion de prueba paso a paso para el lector elegido

## Restricciones
- Es una guía de **testing manual** con lectores de pantalla reales; no
  sustituye herramientas automáticas de auditoría (axe, Lighthouse) que
  detectan un subconjunto de problemas pero no la experiencia real de
  navegación
- Los patrones de corrección HTML/ARIA deben verificarse contra el
  comportamiento real de los componentes DevExpress/DevExtreme de APB, que
  pueden requerir ajustes específicos de `elementAttr` para exponer los
  atributos ARIA correctos
- No sustituye `apb-sub-qa-e2e-v1.0` ni la configuración de Playwright
  existente para testing automatizado; esta skill cubre específicamente la
  validación manual con asistencia tecnológica real

## Adaptaciones APB
- Aplicar como paso de validación dentro de `apb-wf-qa-evidence-v1.0` para
  componentes de cara al usuario final (portal, formularios de gestión)
  antes de cierre de sprint, dado el requisito WCAG 2.1 AA
- Verificar específicamente los popups/modales de DevExtreme (que
  renderizan fuera del árbol DOM del padre, según el patrón ya documentado
  para Playwright) con las checklists de modal/focus trap de esta skill
- Conectar con `apb-sub-qa-e2e-v1.0` como consumidor para integrar hallazgos
  en el ciclo de testing E2E

## Ejemplo de Uso
```
Invocar: third-sickn33-screen-reader-testing-v1.0
Input: { componente_a_validar: "Formulario de alta de escala portuaria
         (DevExtreme)", lector_objetivo: "NVDA + Firefox" }
Output: Checklist de formulario ejecutado, incidencias detectadas (ej.
        campo obligatorio no anunciado) con patrón de corrección ARIA, y
        guion de prueba NVDA paso a paso
```

---
*Adaptado por APB AI Framework. Licencia MIT original respetada.*
