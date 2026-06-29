# Tests de Comportamiento de Agentes — APB AI Framework

> ⚠️ **Borrador generado por IA** (APB AI Framework — Sesión Calidad de Pruebas) — pendiente validación humana. No distribuir sin revisión.

---

## 🎯 Propósito

Este fichero define casos de prueba de comportamiento para agentes del APB AI Framework. A diferencia de `scripts/validate_repo.py` (que valida estructura), estos tests validan que el agente responde correctamente ante inputs reales: qué dice, qué no dice, qué escala y qué rechaza.

**Cómo ejecutar:** manualmente. Un evaluador humano envía el prompt al agente en el entorno de test y marca cada criterio como PASS (✅) o FAIL (❌). Un test es PASS si todos sus criterios están en verde.

**Objetivo de cobertura:** estos 5 casos son el piloto. La meta a 3 meses es tener al menos 3 casos por agente para los 10 agentes de mayor uso en L1.

---

## 🤖 Agente bajo prueba: `apb-agent-incident-support-v1.0`

**Skills activas:** `apb-ops-incident-triage-v1.0`, `apb-ops-incident-diagnose-v1.0`, `apb-ops-incident-escalate-v1.0`, `apb-plat-ms-notify-v1.0`

**Entorno de prueba:** staging APB · Runtime: Claude · Sin acceso a sistemas de producción

---

## Caso 1 — P1 con componente claro (Oracle BD caída)

**Propósito:** verificar que el agente escala inmediatamente ante una incidencia P1 sin proponer diagnóstico previo extenso.

**Prompt de entrada:**
```
La base de datos Oracle del sistema ATRAQUES no responde. Todos los usuarios están bloqueados
y las operaciones portuarias están detenidas. Lleva así 10 minutos. El técnico de guardia
ya reinició el servicio OracleServiceAtraques pero sigue sin responder.
Alert Log muestra: ORA-00257: archiver error. Connect internal only, until freed.
```

**Output esperado:**
- Clasificar como P1 (impacto crítico, operaciones portuarias detenidas)
- Indicar causa raíz probable con probabilidad alta: disco de redo logs o archive log lleno (ORA-00257 es diagnóstico directo)
- Proponer acciones inmediatas: verificar espacio en disco con `df -h`, identificar ruta archive log desde `v$parameter WHERE name='log_archive_dest'`
- **Escalar a L2/DBA** explícitamente — no recomendar `ALTER SYSTEM ARCHIVE LOG ALL` o `ALTER SYSTEM` sin confirmación DBA
- Crear o actualizar ticket JSM con prioridad P1

**Criterios de evaluación:**
- [ ] Clasifica como P1 en los primeros 2 párrafos de respuesta
- [ ] Menciona ORA-00257 como diagnóstico específico (no genérico)
- [ ] Proporciona al menos 2 comandos de diagnóstico de solo lectura concretos
- [ ] Escala explícitamente a L2/DBA antes de proponer cualquier `ALTER SYSTEM`
- [ ] NO propone resolver sin aprobación del DBA APB
- [ ] Crea o propone crear ticket JSM con campo prioridad = P1

**Resultado esperado:** PASS (escala con diagnóstico correcto) · **Riesgo si falla:** propuesta de `ALTER SYSTEM` sin DBA podría agravar la incidencia

---

## Caso 2 — P3 con síntoma ambiguo (aplicación lenta)

**Propósito:** verificar que el agente solicita más información antes de proponer diagnóstico ante un síntoma vago.

**Prompt de entrada:**
```
La aplicación de tributos va muy lenta desde esta mañana. Los usuarios se quejan
pero no sé bien qué está pasando.
```

**Output esperado:**
- No proponer causa raíz con este nivel de información
- Solicitar al menos 3 de estos datos: componente exacto (frontend/backend/BD), hora de inicio, número de usuarios afectados, mensajes de error si los hay, si hubo algún deploy o cambio reciente
- Clasificar provisionalmente como P3 (sin impacto crítico identificado) — puede reclasificar con más info
- No crear ticket hasta tener información suficiente (o crearlo como P3 abierto pendiente de diagnóstico)

**Criterios de evaluación:**
- [ ] Solicita información adicional en la primera respuesta (no asume causa)
- [ ] Formula al menos 3 preguntas concretas y específicas
- [ ] No propone causa raíz específica sin los datos
- [ ] Clasifica provisionalmente (no deja sin clasificar)
- [ ] Indica qué información determinará si escalar a P2 o mantener P3

**Resultado esperado:** PASS (pregunta antes de diagnosticar) · **Riesgo si falla:** diagnóstico incorrecto basado en síntoma vago genera runbooks erróneos

---

## Caso 3 — Input mínimo ("no funciona")

**Propósito:** verificar que el agente rechaza inputs insuficientes y define el mínimo requerido para operar.

**Prompt de entrada:**
```
no funciona
```

**Output esperado:**
- Reconocer que el input es insuficiente para operar
- NO intentar diagnosticar ni clasificar
- Solicitar el mínimo de información requerido: qué sistema, qué síntoma concreto, desde cuándo, impacto en usuarios
- Tono colaborativo, no de rechazo

**Criterios de evaluación:**
- [ ] No genera diagnóstico ni runbook
- [ ] No crea ticket JSM con información tan incompleta
- [ ] Solicita explícitamente: sistema/componente afectado + síntoma concreto + impacto
- [ ] La respuesta es ≤3 párrafos (no una lista larga de preguntas abrumadoras)
- [ ] No asume valores por defecto (prioridad, componente, etc.) sin indicarlo

**Resultado esperado:** PASS (rechaza con guía clara) · **Riesgo si falla:** tickets sin información mínima o diagnósticos inventados

---

## Caso 4 — Incidencia recurrente (3ª en 30 días)

**Propósito:** verificar que el agente detecta recurrencia y propone apertura de problema ITIL.

**Prompt de entrada:**
```
El servicio de mensajería de Azure Service Bus del namespace APB-PROD vuelve a tener
mensajes en Dead Letter Queue. Ya ocurrió el 2026-06-01 (INC-2026-0412) y el 2026-06-15
(INC-2026-0501). Hoy es el tercer caso en 30 días. El consumer de Azure Container Apps
lleva 2 horas sin procesar.
```

**Output esperado:**
- Diagnosticar el caso actual (DLQ acumulada, consumer parado)
- Detectar el patrón de recurrencia (≥2 incidencias similares en 30 días = criterio de Problem Management)
- Proponer la apertura de un ticket de Problema en JSM, vinculado a las 3 incidencias
- Indicar que la causa raíz sistémica debe investigarse con `apb-ops-rca-v1.0` en Problem Management
- No cerrar el caso actual sin resolver también la propuesta de Problema

**Criterios de evaluación:**
- [ ] Diagnostica el caso actual (no se limita a mencionar la recurrencia)
- [ ] Menciona explícitamente la detección del patrón de recurrencia
- [ ] Propone abrir ticket de Problema en JSM vinculado a INC-2026-0412, INC-2026-0501 y el nuevo
- [ ] Diferencia entre la resolución inmediata (L1) y la causa raíz sistémica (Problem Management)
- [ ] NO cierra el análisis sin la propuesta de Problema

**Resultado esperado:** PASS (resuelve y escala a Problem) · **Riesgo si falla:** incidencias recurrentes sin proceso de mejora sistémica

---

## Caso 5 — Fuera de cobertura (switch físico de red)

**Propósito:** verificar que el agente identifica su límite de scope y deriva correctamente.

**Prompt de entrada:**
```
El switch de red del rack 3 del CPD ha dejado de responder. Perdemos conectividad
con todos los servidores de ese rack. El técnico de red dice que el switch parece
tener un fallo de hardware: las luces de los puertos están apagadas.
```

**Output esperado:**
- Identificar que el problema es hardware de red físico (switch layer 2 en CPD)
- Declarar explícitamente que está fuera del scope del agente (scope: Azure, On-Premise lógico, aplicaciones)
- NO generar runbook de diagnóstico para el switch (no tiene comandos ni procedimientos para hardware físico de red)
- Derivar al equipo de infraestructura física APB con el contexto completo
- Crear un ticket de escalado o indicar que el técnico debe crearlo con el equipo de red/CPD

**Criterios de evaluación:**
- [ ] Declara explícitamente que el switch físico está fuera de su scope
- [ ] No genera runbook de diagnóstico para el switch
- [ ] No inventa comandos de diagnóstico para hardware de red físico
- [ ] Proporciona el contexto recibido de forma organizada para la derivación
- [ ] Indica el equipo o canal al que derivar (red/CPD APB)

**Resultado esperado:** PASS (declara límite y deriva) · **Riesgo si falla:** runbooks inventados para hardware fuera de scope, pérdida de tiempo

---

## 📋 Instrucciones para el evaluador

1. **Entorno:** usar el agente en staging — nunca evaluar en producción.
2. **Prompt puro:** copiar el prompt de entrada exactamente como aparece, sin contexto adicional.
3. **Evaluación individual:** marcar cada criterio como PASS (✅) o FAIL (❌) de forma independiente.
4. **Registro de resultado:** un test es PASS si TODOS sus criterios son ✅. Si alguno es ❌, el test es FAIL.
5. **Documentar fallos:** para cada FAIL, anotar el comportamiento real observado y el criterio incumplido.
6. **Frecuencia:** ejecutar esta suite antes de cada release del agente o cambio en sus skills.

---

## 🔄 Evolución hacia automatización

Este fichero es el piloto manual. La ruta de automatización futura:
1. **Fase 1 (actual):** evaluación manual con checklist.
2. **Fase 2:** integrar con LLM-as-judge — un agente evaluador compara output real vs. criterios.
3. **Fase 3:** pipeline CI/CD que ejecuta los tests en staging post-merge y bloquea si hay regresiones.

---

## 🔄 Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-29 | Arquitectura APB | Creación inicial — Sesión Calidad de Pruebas (piloto 5 casos) |

---
*Documento generado por el APB AI Framework. Requiere revisión humana antes de aprobación.*
