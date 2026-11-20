# 🔧 Configuración Manual del GitHub Environment `human-checkpoint`

**Válido para repo:** `apb-dmartin/APB-IA-FRAMEWORK` (y luego migrar a `portdebarcelona/APB-IA-FRAMEWORK`)

## Paso 1 — Ir a Settings del Repositorio

1. Ve a: https://github.com/apb-dmartin/APB-IA-FRAMEWORK/settings/environments
2. O desde el repo → **Settings** (tab superior) → **Environments** (sidebar izquierdo)

## Paso 2 — Crear o Actualizar Environment

1. Click en **"New environment"** (o busca `human-checkpoint` si ya existe)
2. Nombre: `human-checkpoint`
3. Click **"Configure environment"**

## Paso 3 — Configurar Required Reviewers

En la página de configuración del environment:

1. Marca: **"Require reviewers for deployments to this environment"** (checkbox)
2. En **"Required reviewers"**, añade:
   - `deboramv` (tu usuario)
   - `arquitectura-apb` (equipo, si existe; si no, añade usuarios específicos)

3. Click **"Save protection rules"**

## Paso 4 — Verificar Configuración

El environment debe mostrar:
- ✅ Environment name: `human-checkpoint`
- ✅ Deployment branches: "All branches" (default)
- ✅ Required reviewers: `deboramv`, `arquitectura-apb` (o quiénes decidas)
- ✅ Deployment protection rules configured

## Paso 5 — Probar la PoC

Una vez configurado, prueba el workflow:

1. Ve a **Actions** → **Human Checkpoint PoC**
2. Click **"Run workflow"** (dropdown a la derecha)
3. Input: `workflow_id` = `apb-wf-sdd-full-v1.0` (default)
4. Click **"Run workflow"**

El workflow debería:
- ✅ Generar el checkpoint block
- ⏸️ **PAUSAR** en "human-review-gate" (esperando aprobación)
- 📋 Mostrar en UI: "Waiting for review" (si reviewers configurados)

5. Para simular: click **"Review deployments"** → Approve/Reject
6. Workflow continúa o se cancela según tu decisión

## Paso 6 — Migración a Repo Oficial (futuro)

Cuando pases a `portdebarcelona/APB-IA-FRAMEWORK`, repite Pasos 1–4 en:
https://github.com/portdebarcelona/APB-IA-FRAMEWORK/settings/environments

O usa el script (si tienes `gh` CLI + token):
```bash
python scripts/setup_github_environment.py \
  --repo portdebarcelona/APB-IA-FRAMEWORK \
  --environment human-checkpoint \
  --reviewers "arquitectura-apb-team" \
  --token $GITHUB_TOKEN
```

---

**Preguntas:**
- ¿Quiénes son los revisores requeridos? (ej. solo tú, o el equipo de arquitectura)
- ¿Cuántos revisores se requieren para aprobar? (default: 1)

Una vez configurado, avísame y pasamos a las auditorías #85 y #86.
