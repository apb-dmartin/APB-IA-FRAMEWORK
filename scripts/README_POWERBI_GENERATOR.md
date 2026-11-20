# 🚀 Power BI Dashboard Generator

Script Python reutilizable que genera un dashboard Power BI completo desde la especificación técnica y conexiones a APIs reales (Sonar, GitHub Dependabot, Jira).

## 📋 Requerimientos

### Dependencias Python
```bash
pip install requests pandas openpyxl
```

### Credenciales (solicitadas al ejecutar)
1. **Sonar API Token**
   - URL: `https://tu-sonar.internal/account/security`
   - Generar nuevo token

2. **GitHub Personal Access Token (PAT)**
   - URL: https://github.com/settings/tokens
   - Permisos: `public_repo`, `security_events`

3. **Jira API Token**
   - URL: `https://apb.atlassian.net/secure/ViewProfile.jspa?currentTab=user-profile`
   - Crear API token

---

## 🎯 Uso

### Forma Simple (parámetros en línea)

```bash
cd C:\Users\martinde\OneDrive\ -\ Port\ de\ Barcelona\GitHub-Repos\APB-IA-FRAMEWORK

python scripts/generate_powerbi_dashboard.py \
  --sonar-url https://sonar.apb.internal \
  --sonar-token YOUR_SONAR_TOKEN \
  --github-token YOUR_GITHUB_PAT \
  --jira-url https://apb.atlassian.net \
  --jira-token YOUR_JIRA_TOKEN \
  --output ./powerbi-output
```

### Forma Segura (variables de entorno)

**Windows PowerShell:**
```powershell
$env:SONAR_TOKEN = "tu_token_sonar"
$env:GITHUB_TOKEN = "tu_github_pat"
$env:JIRA_TOKEN = "tu_jira_token"

python scripts/generate_powerbi_dashboard.py `
  --sonar-url https://sonar.apb.internal `
  --sonar-token $env:SONAR_TOKEN `
  --github-token $env:GITHUB_TOKEN `
  --jira-url https://apb.atlassian.net `
  --jira-token $env:JIRA_TOKEN `
  --output ./powerbi-output
```

**Bash/Linux:**
```bash
export SONAR_TOKEN="tu_token_sonar"
export GITHUB_TOKEN="tu_github_pat"
export JIRA_TOKEN="tu_jira_token"

python scripts/generate_powerbi_dashboard.py \
  --sonar-url https://sonar.apb.internal \
  --sonar-token $SONAR_TOKEN \
  --github-token $GITHUB_TOKEN \
  --jira-url https://apb.atlassian.net \
  --jira-token $JIRA_TOKEN \
  --output ./powerbi-output
```

---

## 📤 Salida del Script

El script genera:

1. **`qa_compliance_data.xlsx`**
   - Archivo Excel importable directo en Power BI
   - Hojas: Sonar, Dependabot, Jira
   - Listo para usar

2. **`qa_compliance_*.csv`**
   - Archivos CSV individuales (alternativa)
   - Codificación UTF-8

3. **`INSTRUCCIONES_POWERBI.md`**
   - Guía paso a paso para importar en Power BI Desktop
   - Incluye código DAX, fórmulas, y configuración

---

## ⚡ Ejemplo Completo (Caso Real)

Supongamos que tienes:
- Sonar: `https://sonar.apb.internal`
- Token Sonar: `squ_1234567890abcdef`
- GitHub PAT: `ghp_1234567890abcdefghij`
- Jira: `https://apb.atlassian.net`
- Token Jira: `ATATT3xF1234567890_abcdef`

### Paso 1: Ejecutar el script
```bash
cd "C:\Users\martinde\OneDrive - Port de Barcelona\GitHub-Repos\APB-IA-FRAMEWORK"

python scripts/generate_powerbi_dashboard.py ^
  --sonar-url https://sonar.apb.internal ^
  --sonar-token squ_1234567890abcdef ^
  --github-token ghp_1234567890abcdefghij ^
  --jira-url https://apb.atlassian.net ^
  --jira-token ATATT3xF1234567890_abcdef ^
  --output ./powerbi-output
```

### Paso 2: Output esperado
```
============================================================
🚀 Power BI Dashboard Generator v1.0
============================================================
📊 Descargando datos de Sonar...
✓ Encontrados 15 proyectos en Sonar
✓ 15 registros de Sonar descargados
🔐 Descargando datos de Dependabot (GitHub)...
✓ Datos de Dependabot descargados
🐛 Descargando datos de Jira...
✓ 42 bugs encontrados en Jira
✓ 42 registros de Jira procesados
📝 Generando archivo Excel...
✓ Excel generado: ./powerbi-output/qa_compliance_data.xlsx
📊 Generando CSVs...
✓ qa_compliance_sonar.csv
✓ qa_compliance_dependabot.csv
✓ qa_compliance_jira.csv
📋 Generando instrucciones...
✓ Instrucciones: ./powerbi-output/INSTRUCCIONES_POWERBI.md

============================================================
✅ GENERACIÓN COMPLETADA
============================================================
📊 Datos: ./powerbi-output/qa_compliance_data.xlsx
📋 Instrucciones: ./powerbi-output/INSTRUCCIONES_POWERBI.md

Próximos pasos:
  1. Lee: ./powerbi-output/INSTRUCCIONES_POWERBI.md
  2. Abre Power BI Desktop
  3. Importa: ./powerbi-output/qa_compliance_data.xlsx
  4. Sigue las instrucciones paso a paso
```

### Paso 3: Importar en Power BI
1. Abre **Power BI Desktop**
2. **Home → Get Data → Excel workbook**
3. Selecciona `./powerbi-output/qa_compliance_data.xlsx`
4. Lee las instrucciones en `INSTRUCCIONES_POWERBI.md`
5. Sigue los pasos para crear visualizaciones

---

## 🔧 Troubleshooting

### ❌ "Módulo 'requests' no encontrado"
```bash
pip install requests
```

### ❌ "Token inválido" (401 Unauthorized)
- Verifica que el token sea correcto
- Verifica que no haya espacios en blanco
- Verifica que el token no haya expirado

### ❌ "Conexión rechazada" a Sonar/Jira
- Verifica la URL (ej. `https://` vs `http://`)
- Verifica que las URLs sean accesibles desde tu red
- Comprueba firewall/proxy

### ⚠️ "Usando datos de prueba"
- El script no pudo conectar a una o más APIs
- Pero generó datos de ejemplo para que puedas probar el flujo
- Ejecuta de nuevo cuando las credenciales sean válidas

---

## 📊 Datos Generados (Estructura)

### Tabla Sonar
```
ApplicationKey | ApplicationName | CoveragePct | BugCount | BugCountHigh | ... | MeasuredDate
apb.api.sms    | SMS API         | 0.82        | 3        | 1            | ... | 2026-07-06
apb.tru        | TruckCenter     | 0.75        | 5        | 3            | ... | 2026-07-06
```

### Tabla Dependabot
```
Repository | Dependency      | Severity | CreatedAt          | State
APB.API.SMS| jackson-databind| High     | 2026-07-01 14:23:00| open
APB.TRU    | log4j-core      | Critical | 2026-07-04 09:15:00| open
```

### Tabla Jira
```
IssueKey | Title                      | Component    | Severity | CreatedDate | ClosedDate | DaysToClose
SMS-1001 | NullPointerException       | SMS API      | High     | 2026-06-26  | 2026-07-03 | 7
TRU-2045 | UI rendering lag           | TruckCenter  | Medium   | 2026-07-01  | NULL       | 5
```

---

## 🎓 Qué Hace el Script

1. **Conecta a Sonar** → Descarga cobertura, bugs, deuda técnica
2. **Conecta a GitHub** → Descarga vulnerabilidades Dependabot
3. **Conecta a Jira** → Descarga bugs y tiempo de resolución
4. **Limpia datos** → Valida fechas, normaliza formatos
5. **Exporta a Excel** → Crea un archivo importable directamente
6. **Genera instrucciones** → Paso a paso para Power BI Desktop
7. **Crea CSVs** → Opción alternativa de importación

---

## 🔐 Seguridad

- **Nunca** guardes tokens en scripts o archivos
- Usa variables de entorno para credenciales
- Los tokens en la línea de comandos quedan en el historial
  - En PowerShell: `Clear-History` después
  - En Bash: `history -c`

---

## 📝 Ejemplo de `.env` (Archivo Local, NO commitear)

Si prefieres un archivo `.env`:

```bash
# .env (añade a .gitignore)
SONAR_URL=https://sonar.apb.internal
SONAR_TOKEN=squ_1234567890abcdef
GITHUB_TOKEN=ghp_1234567890abcdefghij
JIRA_URL=https://apb.atlassian.net
JIRA_TOKEN=ATATT3xF1234567890_abcdef
```

Luego modifica el script para leer desde el `.env`:
```python
from dotenv import load_dotenv
import os

load_dotenv()
sonar_token = os.getenv("SONAR_TOKEN")
# ... etc
```

---

## 🚀 Automatización (Próxima Sesión)

Para automatizar ejecución diaria:

**Windows Task Scheduler:**
```powershell
$trigger = New-ScheduledTaskTrigger -Daily -At 02:00AM
$action = New-ScheduledTaskAction -Execute "python" -Argument "scripts/generate_powerbi_dashboard.py --sonar-url ... --sonar-token ..."
Register-ScheduledTask -TaskName "PowerBI-Dashboard-Update" -Trigger $trigger -Action $action
```

**Linux Cron:**
```bash
0 2 * * * cd /path/to/framework && python scripts/generate_powerbi_dashboard.py --sonar-url ... --sonar-token ...
```

---

## ❓ Preguntas Frecuentes

**P: ¿Puedo usar esto sin las APIs reales?**  
R: Sí, el script genera datos de prueba automáticamente si las conexiones fallan.

**P: ¿Cuánto tarda el script?**  
R: ~2-3 minutos (depende de cantidad de datos y latencia de APIs).

**P: ¿Puedo customizar las visualizaciones después?**  
R: Sí, el Excel es un punto de partida. Power BI es 100% personalizable.

**P: ¿Cada vez que ejecuto, sobrescribe los datos anteriores?**  
R: Sí, por defecto. Puedes guardar versiones renombrando el output.

---

## 📞 Soporte

Para problemas:
1. Revisa el log de ejecución (sale en consola)
2. Verifica credenciales y URLs
3. Comprueba conectividad de red
4. Consulta `INSTRUCCIONES_POWERBI.md` generado

---

**Autor:** Claude Code (APB AI Framework)  
**Versión:** 1.0.0  
**Fecha:** 2026-07-06  
**Estado:** Production-Ready
