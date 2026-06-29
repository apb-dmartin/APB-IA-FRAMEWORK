---
id: "apb-ops-incident-diagnose-v1.0"
name: "Diagnóstico Técnico de Incidencias"
description: "Genera el diagnóstico técnico de una incidencia APB a partir del síntoma clasificado y los logs/evidencias disponibles. Produce un árbol de causa raíz probable y un runbook de resolución paso a paso adaptado al stack tecnológico APB (Azure, Oracle, IIS, Apache, Firewall, DNS)."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "operation"
autonomy_level: 2
created_date: "2026-06-26"
review_date: "2026-06-26"
---

# Diagnóstico Técnico de Incidencias

---

## 🎯 Propósito

Analizar la evidencia técnica de una incidencia (logs, mensajes de error, métricas, descripción del síntoma) y producir un diagnóstico estructurado con causa raíz probable y runbook de resolución.

> **Diferencia clave con `apb-ops-rca-v1.0`:**
> Esta skill es **táctica e inmediata** — se ejecuta **durante** el incidente activo (minutos, no horas). Su objetivo es proporcionar al técnico L1 un runbook accionable lo antes posible para restaurar el servicio.
> `apb-ops-rca-v1.0` es un análisis **post-incidente profundo** (5-Whys, Ishikawa, timeline completo) que se realiza después de que el servicio está restaurado, con el objetivo de eliminar la causa raíz y evitar recurrencia. El diagnóstico incluye porcentaje de confianza y alternativas si existen múltiples causas posibles. El runbook es accionable por el técnico resolutor sin necesidad de interpretación adicional.

---

## ⚡ Trigger

Cuando `apb-ops-incident-triage-v1.0` ha clasificado la incidencia y determinado que puede tratarse en L1 o L2, y se dispone de al menos la descripción del síntoma.

---

## 📥 Input

- Clasificación de triaje (prioridad, categoría, componente)
- Descripción del síntoma en lenguaje natural
- Logs o mensajes de error (texto plano, Event Log, syslog, Application Insights, etc.)
- Métricas de rendimiento si están disponibles (CPU, memoria, tiempos de respuesta)
- Historial de cambios recientes en el sistema afectado (si se conoce)
- Incidencias similares previas (referencia a tickets JSM anteriores)

---

## 📤 Output

- **Árbol de causa raíz:** causas ordenadas por probabilidad (%)
- **Diagnóstico principal:** descripción técnica de la causa más probable
- **Runbook de resolución:** pasos ordenados, con comandos específicos donde corresponda
- **Criterios de resolución:** cómo verificar que la incidencia está resuelta
- **Indicadores de recaída:** qué monitorizar tras la resolución para detectar reaparición
- **Propuesta de problema:** si la incidencia es recurrente (≥2 veces en 30 días), proponer apertura de ticket de Problema en JSM

---

## 🔄 Proceso

1. **Análisis de evidencia:** parsear logs y mensajes de error; identificar patrones, códigos de error y timestamps
2. **Correlación con stack APB:** cruzar síntoma con comportamientos conocidos de cada tecnología

### Patrones de diagnóstico por tecnología

**Oracle DB:**
- ORA-00060 (deadlock) → contención de recursos, revisar sesiones activas y locks
- ORA-01555 (snapshot too old) → UNDO tablespace insuficiente o query larga
- ORA-04031 (shared pool) → memoria compartida agotada, reiniciar pool o aumentar SGA
- Tablespace al >90% → ampliar datafile o purgar datos históricos
- Sesiones bloqueadas → identificar sesión bloqueante y evaluar kill session

**Apache HTTPD / Tomcat:**
- Error 502/503 → backend caído o pool de threads agotado
- Error 504 → timeout entre Apache y Tomcat (ajustar ProxyTimeout)
- OutOfMemoryError en Tomcat → heap insuficiente (ajustar -Xmx en JVM_OPTS)
- Too many open files → límite de descriptores de fichero del SO

**IIS:**
- Worker process crash (503) → revisar Event Log Application, App Pool recycling
- High memory / application pool → memory limit hit, revisar configuración de reciclado
- 401 Unauthorized → Kerberos/NTLM misconfiguration, revisar SPN

**DNS:**
- NXDOMAIN → registro inexistente o zona no propagada
- Timeout → servidor DNS inaccesible o sobrecargado
- Resolución incorrecta → caché DNS obsoleta, forzar flush

**Firewall (Fortinet/Cisco):**
- Conexiones rechazadas → política denegada, revisar logs de firewall
- Latencia alta → session table llena o QoS mal configurado
- VPN caída → certificado expirado o cambio de IP pública

**Azure:**
- App Service 5xx → instancia caída, revisar Application Insights y Diagnose & Solve
- Storage throttling → límite de IOPS alcanzado, revisar tier de la cuenta
- AKS pod crash → OOMKilled o liveness probe fallida
- NSG blocking → revisar reglas de entrada/salida, usar Network Watcher

3. **Construcción del árbol de causas:** ordenar de mayor a menor probabilidad con justificación
4. **Generación del runbook:** pasos concretos para el técnico resolutor
5. **Definición de criterios de resolución y monitorización post-resolución**

---

## 📋 Reglas y Constraints

- El runbook siempre indica el riesgo de cada paso (Bajo / Medio / Alto) antes de ejecutarlo
- Los pasos de Alto riesgo (reinicio de servicios en producción, kill de sesiones BD) requieren confirmación humana explícita antes de ejecutarse
- Si la confianza del diagnóstico principal es <50%, presentar los tres primeros candidatos sin recomendar uno solo
- Los comandos del runbook se adaptan al SO del servidor afectado (Linux bash vs. Windows PowerShell)
- Nunca incluir credenciales en el runbook — referenciar siempre a Key Vault APB o al gestor de contraseñas APB

---

## 🛠 Stack Tecnológico Relevante

- Oracle Database 19c / 21c
- Apache HTTPD 2.4, Apache Tomcat 9/10
- Microsoft IIS 10
- DNS (Windows Server DNS / BIND)
- Fortinet FortiGate, Cisco ASA/FTD
- Azure (App Service, AKS, Storage, Application Insights, NSG, Network Watcher)
- Linux (RHEL/CentOS/Ubuntu) y Windows Server 2019/2022
- Jira Service Management (para referencia de incidencias previas)

---

## 💡 Ejemplos de Uso

**Ejemplo — Diagnóstico Oracle:**
> Log aportado: `ORA-00060: deadlock detected while waiting for resource`
> 
> Diagnóstico: Deadlock entre sesiones concurrentes (95% confianza)  
> Runbook: (1) Identificar sesiones involucradas con `v$session` y `v$lock` [Riesgo Bajo], (2) Verificar la transacción bloqueante [Riesgo Bajo], (3) Evaluar `ALTER SYSTEM KILL SESSION` si es seguro [Riesgo Medio — confirmación humana requerida], (4) Revisar la lógica de la transacción para evitar recurrencia [Riesgo Bajo]

**Ejemplo — Diagnóstico IIS:**
> Log aportado: `Application Event Log: The worker process for app pool 'ConcesionesPool' has encountered an unhandled exception`
>
> Diagnóstico: Excepción no controlada en la aplicación provoca crash del worker process (90% confianza)  
> Runbook: (1) Revisar Application Event Log completo [Riesgo Bajo], (2) Revisar logs de aplicación en `C:\inetpub\logs\` [Riesgo Bajo], (3) Reiniciar el App Pool manualmente [Riesgo Bajo], (4) Capturar memory dump si el crash se repite [Riesgo Bajo], (5) Derivar el dump al equipo de desarrollo

---

## 🔗 Dependencias

- `apb-ops-incident-triage-v1.0` — proporciona la clasificación previa
- `apb-ops-incident-escalate-v1.0` — siguiente skill si el diagnóstico supera capacidad L1
- `apb-sub-ops-oracle-v1.0` — subagente especializado Oracle (delegación automática si componente = Oracle)
- `apb-sub-ops-iis-apache-v1.0` — subagente especializado IIS/Apache
- `apb-sub-ops-network-v1.0` — subagente especializado DNS/Firewall/Red
- `apb-sub-ops-azure-v1.0` — subagente especializado Azure

---

## 📝 Notas

- El catálogo de patrones de diagnóstico debe ampliarse con cada incidencia resuelta (proceso de mejora continua)
- Las incidencias resueltas con runbook nuevo deben generar un artículo en la base de conocimiento JSM

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `Clasificación de triaje` | Pregunta: "¿Puedes proporcionar clasificación de triaje?" | Sí |
| `Descripción del síntoma en lenguaje natural` | Pregunta: "¿Puedes proporcionar descripción del síntoma en lenguaje natural?" | Sí |
| `Logs o mensajes de error` | Pregunta: "¿Puedes proporcionar logs o mensajes de error?" | Sí |
| `Métricas de rendimiento si están disponibles` | Pregunta: "¿Puedes proporcionar métricas de rendimiento si están disponibles?" | Sí |
| `Historial de cambios recientes en el sistema afectado` | Continúa con la información disponible — indica qué asumió | No |
| `Incidencias similares previas` | Pregunta: "¿Puedes proporcionar incidencias similares previas?" | Sí |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-ops-incident-diagnose-v1.0) - pendiente validacion humana. No distribuir sin revision.
