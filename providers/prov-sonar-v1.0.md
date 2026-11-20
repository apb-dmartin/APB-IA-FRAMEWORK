---
id: "prov-sonar-v1.0"
name: "Provider: SonarQube (MCP oficial SonarSource)"
description: "Proveedor de acción de solo lectura para análisis de calidad de código con SonarQube. Consulta métricas, issues, security hotspots y estado de quality gate de la instancia real de APB a través del servidor MCP oficial de SonarSource."
version: "2.2.0"
status: "candidate"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
provider_type: "action"
access_mode: "read-only"
created_date: "2026-06-20"
review_date: "2026-07-09"
---

# Provider: SonarQube (MCP oficial SonarSource)

---

> **Nota de reescritura (v2.0.0, 2026-07-09, a petición de Débora):** la v1.0.0
> era puramente aspiracional (`endpoint` de ejemplo, mecanismo "MCP" sin
> implementación real detrás, `permissions` incluía `"analysis"` sin sentido
> real — ejecutar un análisis requiere `sonar-scanner`, no una llamada de API
> con token). Esta versión documenta la conexión real: instancia SonarQube
> APB en `http://gisplanolpre.port.apb.es:9001` (entorno pre-producción según
> el propio nombre del host — pendiente confirmar si existe una URL de
> producción separada), y el mecanismo real: el **servidor MCP oficial de
> SonarSource** (`sonarsource/sonarqube-mcp`,
> [SonarSource/sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server)),
> no un mecanismo custom. Alcance acotado a solo lectura.
>
> **Estado de verificación (2026-07-10): completada.** La conexión REST directa
> contra la instancia real está verificada (autenticación con User Token vía
> Basic Auth, usada por
> [`generate_powerbi_dashboard.py`](../scripts/generate_powerbi_dashboard.py)).
> Nota: `api/projects/search` pagina a 100 resultados por defecto — el total
> real de proyectos en la instancia es 224 (`ps=500` sin paginar), confirmado
> en el cruce de project keys de `HANDOFF_TECNICOS.md` QA3-3.
> El servidor MCP oficial también está verificado en vivo en modo
> `streamable-http`: handshake `initialize`, `tools/list` y una llamada real a
> `search_my_sonarqube_projects` devolvieron datos reales (`APB.API.AGE`) desde
> Windows y desde WSL.
>
> **Detalle de infraestructura real (importante para reproducir):** el
> contenedor **no** corre sobre el motor de Docker Desktop directamente — se
> instaló Docker Engine nativo dentro de la distro **Ubuntu de WSL2**
> (`sudo apt-get install docker.io`). Motivo: la subred de bridge por defecto
> de Docker **choca con una ruta real de la VPN corporativa de APB** que
> contiene la instancia de Sonar — cualquier tráfico del contenedor hacia esa
> subred se enrutaba mal y fallaba con `NoRouteToHostException`, tanto en
> Docker Desktop (bridge y `--network host`, con "Enable host networking"
> activado) como en el Docker nativo antes de reconfigurar la subred. Se
> resolvió cambiando el bridge de Docker a un rango privado no usado por la
> VPN (identificado revisando `ip route` en la distro WSL) vía
> `/etc/docker/daemon.json` (`bip` + `default-address-pools`), recreando
> `docker0`. Ver checklist completo más abajo si hay que reproducir esto en
> otra máquina/servidor (las subredes concretas usadas no se documentan aquí
> por política de no exponer direccionamiento interno — confirmar con el
> equipo de Arquitectura/IT de APB el rango correcto para cada red).

## Descripción

Proveedor de acción de solo lectura para SonarQube: consulta de proyectos,
métricas de calidad (cobertura, bugs, vulnerabilidades, code smells, deuda
técnica), issues por severidad, security hotspots y estado de quality gate.
No ejecuta análisis (eso es responsabilidad de `sonar-scanner` en el pipeline
CI/CD, un mecanismo distinto y fuera del alcance de este provider).

## Capacidades

| Acción | Descripción | Gate humano |
|--------|-------------|--------------|
| `list_projects` | Lista los proyectos/componentes registrados en la instancia | No |
| `get_project_measures` | Métricas de un proyecto (cobertura, bugs, vulnerabilidades, code smells, deuda técnica) | No |
| `get_project_issues` | Issues de un proyecto, filtrables por tipo y severidad | No |
| `get_quality_gate_status` | Estado del quality gate de un proyecto/rama | No |
| `get_security_hotspots` | Security hotspots pendientes de revisión | No |

Todas las acciones son de solo lectura — sin gate humano porque no modifican
estado en SonarQube ni en ningún otro sistema.

## Mecanismo real

**Servidor MCP oficial de SonarSource** (`sonarsource/sonarqube-mcp`), no un
servidor custom del framework. Se distribuye únicamente como imagen de
contenedor (Docker/Podman/cualquier runtime OCI) — no hay alternativa `npx`
ni binario. Transporte `streamable-http` para que cualquier consumidor del
framework (Claude Code, Copilot, Rovo, scripts propios) pueda conectarse al
mismo endpoint, no solo un proceso local lanzado por un único cliente vía
stdio.

Licencia del servidor: SONAR Source-Available License v1.0, uso permitido
para "Non-Competitive Purpose" — aplicable a uso interno de APB.

## Configuración

```json
{
  "provider_id": "prov-sonar-v1.0",
  "type": "action",
  "mechanism": "mcp",
  "mcp_image": "sonarsource/sonarqube-mcp",
  "mcp_transport": "streamable-http",
  "endpoint": "http://gisplanolpre.port.apb.es:9001",
  "auth": "user_token",
  "token_ref": "AKV://sonar-token",
  "rate_limit": "unlimited",
  "permissions": ["read"]
}
```

> **Nota de aprovisionamiento:**
> 1. Generar un **User Token** (no Global/Project Analysis Token — esos son
>    para que `sonar-scanner` suba análisis, no para consultar datos vía Web
>    API) desde `<endpoint>/account/security` → "Generate Tokens".
> 2. Idealmente, generarlo desde una **cuenta de servicio** dedicada
>    (ej. `svc-apb-ia-framework`) con permiso "Browse" sobre los proyectos a
>    exponer, en vez de una cuenta personal.
> 3. Para esta fase de prueba (2026-07-09), el token vive como **variable de
>    entorno de usuario persistente** en la máquina de Débora (`SONARQUBE_TOKEN`
>    para el contenedor MCP, `SONAR_TOKEN` para `generate_powerbi_dashboard.py`,
>    más `SONARQUBE_URL` con el endpoint) — vía `setx`, no en ningún fichero del
>    repo ni como argumento CLI persistido. Nota: `setx` solo aplica a terminales
>    *nuevas*, no a la sesión donde se ejecutó.
> 4. **Handoff pendiente antes de producción — migración a Azure Key Vault:**
>    - [ ] Crear (o confirmar) el Key Vault de APB donde vivirán los secretos
>      del framework.
>    - [ ] Crear el secreto `sonar-token` en ese Key Vault con el valor del
>      User Token de la cuenta de servicio (no el personal usado en pruebas).
>    - [ ] Conceder acceso de lectura vía Managed Identity al proceso/servicio
>      que orqueste el contenedor MCP (`prov-akv-v1.0` documenta el mecanismo).
>    - [ ] El orquestador resuelve `AKV://sonar-token` en tiempo de arranque e
>      inyecta el valor al contenedor — nunca hardcodeado en el comando
>      `docker run` ni en variables de entorno de usuario persistentes.
>    - [ ] Revocar/rotar el User Token usado durante esta fase de pruebas una
>      vez la cuenta de servicio esté operativa.
> 5. Arranque del servidor MCP (modo remoto multi-cliente, verificado 2026-07-10):
>    - Si el motor de contenedores tiene ruta directa a la red de la VPN de APB
>      (`172.17.x.x`), esto basta:
>      ```
>      docker run -d --name sonar-mcp --init --restart unless-stopped -p 8765:8080 \
>        -e SONARQUBE_TRANSPORT=http \
>        -e SONARQUBE_HTTP_HOST=0.0.0.0 \
>        -e SONARQUBE_HTTP_PORT=8080 \
>        -e SONARQUBE_TOKEN=<User Token> \
>        -e SONARQUBE_URL=http://gisplanolpre.port.apb.es:9001 \
>        sonarsource/sonarqube-mcp
>      ```
>    - Si falla con `NoRouteToHostException` (choque de subred Docker/VPN, como
>      en la máquina de Débora): reconfigurar el bridge de Docker antes del
>      `docker run` de arriba:
>      ```
>      # /etc/docker/daemon.json — sustituir <N> por un segundo octeto 172.<N>.0.0/16
>      # que NO aparezca en la salida de "ip route" dentro de la distro/host
>      {"bip": "172.<N>.0.1/24", "default-address-pools": [{"base": "172.<N>.0.0/16", "size": 24}]}
>      ```
>      ```
>      sudo systemctl stop docker docker.socket && sudo ip link delete docker0 && sudo systemctl start docker
>      ```
>      (revisar `ip route` primero para confirmar qué subred /16 está realmente
>      libre en cada red — el rango libre puede variar entre máquinas).
>    - En Windows con Docker Desktop + VPN corporativa, puede hacer falta además:
>      WSL2 en modo `networkingMode=mirrored` (`%USERPROFILE%\.wslconfig`) y/o
>      instalar Docker Engine nativo dentro de una distro WSL (no el motor de
>      Docker Desktop) si el problema persiste — ver nota de infraestructura
>      real arriba.
>    - Verificación rápida (handshake MCP):
>      ```
>      curl -X POST http://localhost:8765/mcp \
>        -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" \
>        -H "Authorization: Bearer <User Token>" \
>        -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}}}'
>      ```

## Inputs

- `action`: nombre de la acción (tabla de Capacidades)
- `project_key`: clave del proyecto (p. ej. `APB.API.AGE`)
- `branch`: rama a consultar (opcional, por defecto la rama principal)
- `severities`: filtro de severidad para `get_project_issues` (`BLOCKER`, `CRITICAL`, `MAJOR`, `MINOR`, `INFO`)
- `types`: filtro de tipo de issue (`BUG`, `VULNERABILITY`, `CODE_SMELL`)

## Outputs

- `list_projects`: array de `{key, name}`
- `get_project_measures`: `{coverage, bugs, vulnerabilities, code_smells, sqale_index}`
- `get_project_issues`: array de issues con `{key, severity, type, message, component}`
- `get_quality_gate_status`: `{status: "OK"|"ERROR", conditions[]}`
- `get_security_hotspots`: array de hotspots con `{key, status, vulnerabilityProbability, component}`

## Dependencias

- `prov-akv-v1.0` — destino final del `token_ref` antes de producción
- `apb-dev-sonar-clean-v1.0` (skill APB)
- `apb-plat-ci-qa-gate-v1.0` (skill — consume `get_quality_gate_status` para el veredicto GO/NO-GO)
- `apb-wf-code-review-v1.0` (workflow)
- [`scripts/generate_powerbi_dashboard.py`](../scripts/generate_powerbi_dashboard.py) — consumidor REST directo (no vía MCP) para el dashboard de compliance

## Restricciones

- Token gestionado en Azure Key Vault en producción (`prov-akv-v1.0`); variable
  de entorno local solo durante desarrollo/pruebas.
- Solo lectura — no ejecuta análisis, no modifica quality profiles ni
  configuración del servidor.
- Los umbrales concretos del quality gate (cobertura mínima, tiers) deben
  confirmarse con QA APB antes de que `apb-plat-ci-qa-gate-v1.0` los use en
  un veredicto de despliegue.

## Ejemplo de Uso

```
Invocar: prov-sonar-v1.0
Action: get_project_measures
ProjectKey: "APB.API.AGE"
→ { coverage: 0.183, bugs: 117, vulnerabilities: 1, code_smells: 326, sqale_index_days: 2.85 }
```

```
Invocar: prov-sonar-v1.0
Action: get_quality_gate_status
ProjectKey: "APB.API.APPS"
→ { status: "OK", conditions: [...] }
```

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-20 | Arquitectura APB | Creación inicial (aspiracional, sin mecanismo real) |
| 2.0.0 | 2026-07-09 | Claude (Anthropic), a petición de Débora | Reescritura completa: endpoint real (`gisplanolpre.port.apb.es:9001`), mecanismo real (MCP oficial SonarSource, no custom), alcance acotado a solo lectura (`permissions: ["read"]`, se retira `"analysis"`), tabla de acciones con gates humanos, nota de aprovisionamiento, verificación REST directa confirmada con datos reales |
| 2.1.0 | 2026-07-10 | Claude (Anthropic), a petición de Débora | `status` pasa a `candidate`: servidor MCP oficial verificado en vivo (`initialize`, `tools/list`, `search_my_sonarqube_projects` con datos reales). Documentado el hallazgo de infraestructura: la subred de bridge de Docker por defecto choca con una ruta real de la VPN de APB — solución documentada (subred alternativa + Docker Engine nativo en WSL en vez del motor de Docker Desktop). Registrado en `.mcp.json` (`sonar`, `type: http`) |
| 2.2.0 | 2026-11-20 | Claude (Anthropic), a petición de Débora | Puerto publicado del contenedor `sonar-mcp` pasa de 8080 a 8765 (en Windows el 8080 lo ocupa otro proceso local y `localhost:8080/mcp` devolvía 404); `.mcp.json` actualizado y handshake `initialize` verificado en el nuevo puerto |

---
*Registrado en APB AI Framework.*
