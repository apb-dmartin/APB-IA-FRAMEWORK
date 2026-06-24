---
id: "third-expo-cicd-multiplatform-v1.0"
name: "CI/CD Multi-tecnología"
description: "Diseña, valida y optimiza pipelines CI/CD para proyectos multi-tecnología (mobile, web, backend, IaC): GitHub Actions, GitLab CI, Azure DevOps, Jenkins, CircleCI, EAS Workflows."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
created_date: "2026-06-22"
review_date: "2026-06-22"
autonomy_level: 1
source_repo: "https://github.com/expo/skills"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
---

# SKILL_PLAT_CICD — Continuous Integration & Delivery

## 1. Propósito y Alcance

Esta skill extiende el conocimiento de EAS Workflows (Expo) a un framework
unificado de CI/CD multi-tecnología para el ecosistema APB. Cubre:

- **Mobile**: iOS, Android, React Native (Expo), Flutter
- **Web**: Frontend (React, Angular, Vue), Backend (Node.js, Python, Go, Java)
- **Infraestructura**: Terraform, CloudFormation, ARM, Bicep
- **ML/AI**: Pipelines de training, deployment de modelos, MLOps
- **Multi-platform**: GitHub Actions, GitLab CI, Azure DevOps, Jenkins, CircleCI, ArgoCD, FluxCD

## 2. Principios Core CI/CD (APB)

1. **Automatización total**: Todo proceso repetible debe estar automatizado; cero pasos manuales en pipeline.
2. **Fast feedback**: El pipeline debe fallar rápido (fail fast); tests unitarios primero, luego integración.
3. **Inmutabilidad**: Los artefactos de build son inmutables; se promueven entre entornos, no se re-build.
4. **Seguridad shift-left**: Escaneo de seguridad en etapas tempranas (SAST, DAST, SCA, secrets scanning).
5. **Observabilidad**: Cada pipeline debe generar métricas, logs, y trazabilidad completa.
6. **Cost optimization**: Uso de runners efímeros, caching agresivo, y spot instances para builds.
7. **Reversibilidad**: Todo deployment debe ser reversible (rollback) en < 5 minutos.

## 3. Taxonomía de Pipelines

### 3.1 Por Tecnología
| Tecnología | Build Tool | Test Framework | Deploy Target | Pipeline Type |
|------------|------------|----------------|---------------|---------------|
| React Native | EAS / Metro | Jest, Detox | App Store, Play Store | Mobile CD |
| Flutter | Flutter CLI | Flutter Test | App Store, Play Store | Mobile CD |
| iOS Native | Xcode | XCTest | TestFlight, App Store | Mobile CD |
| Android Native | Gradle | Espresso | Play Store | Mobile CD |
| React Web | Vite/Webpack | Jest, Cypress | CDN, S3, Vercel | Web CD |
| Node.js Backend | npm/yarn/pnpm | Jest, Mocha | ECS, K8s, Lambda | Backend CD |
| Python Backend | pip/poetry | pytest, unittest | ECS, K8s, Cloud Run | Backend CD |
| Go Backend | go modules | go test | ECS, K8s, Lambda | Backend CD |
| Terraform | Terraform CLI | terraform test | Multi-cloud | IaC CD |
| ML/AI | Docker, MLflow | pytest, Great Expectations | SageMaker, Vertex AI | MLOps CD |

### 3.2 Por Estrategia de Deployment
- **Rolling**: Reemplazo gradual de instancias (mínimo downtime, simple rollback)
- **Blue-Green**: Dos entornos idénticos; switch instantáneo, rollback inmediato
- **Canary**: Despliegue a subconjunto de usuarios/instancias; monitoreo antes de full rollout
- **Feature Flags**: Despliegue de código con features desactivadas; activación gradual
- **A/B Testing**: Despliegue de variantes para testing de conversión
- **Recreate**: Destruir y recrear (aceptable para dev/staging, NO para prod)

## 4. Pipeline Estándar Multi-etapa

### 4.1 Fases Obligatorias
```
1. TRIGGER
   └── Push a branch, PR, tag, o schedule
   └── Filtros de path (ejecutar solo si cambió código relevante)

2. ENVIRONMENT SETUP
   └── Checkout de código
   └── Setup de runtime (Node, Python, Go, Java, Flutter, etc.)
   └── Cache de dependencias (npm, pip, gradle, cocoapods)
   └── Setup de secrets (vault, OIDC, service accounts)

3. LINT & FORMAT
   └── ESLint/Prettier (JS), Black/Ruff (Python), gofmt (Go), SwiftLint (iOS)
   └── terraform fmt (IaC)
   └── SonarQube / SonarCloud quality gate

4. STATIC ANALYSIS & SECURITY
   └── SAST (SonarQube, CodeQL, Semgrep)
   └── SCA (Snyk, Dependabot, OWASP Dependency-Check)
   └── Secrets scanning (GitLeaks, TruffleHog)
   └── IaC scanning (tfsec, Checkov, Trivy)
   └── License compliance (FOSSA, ScanCode)

5. BUILD
   └── Compilación/bundle de código
   └── Generación de artefactos versionados
   └── Docker image build (si aplica)
   └── Mobile: Build de .ipa (iOS) y .aab/.apk (Android)

6. UNIT TESTS
   └── Ejecución de tests unitarios con coverage
   └── Coverage mínimo: 80% (lógica de negocio), 60% (infraestructura)
   └── Tests paralelizados por shard

7. INTEGRATION TESTS
   └── Tests de integración con servicios reales o mocks
   └── Contract tests (Pact, Spring Cloud Contract)
   └── Database migration tests (Flyway, Alembic)

8. E2E TESTS (opcional, post-deploy staging)
   └── Cypress/Playwright (web)
   └── Detox/Appium (mobile)
   └── Karate/RestAssured (API)

9. DEPLOY STAGING
   └── Deploy automático a staging/QA
   └── Smoke tests post-deploy
   └── Validación de feature flags

10. APPROVAL GATE (prod only)
    └── Aprobación manual o automática basada en políticas
    └── Notificación a Slack/Teams/Discord

11. DEPLOY PRODUCTION
    └── Estrategia de deployment (blue-green, canary, rolling)
    └── Monitoreo de métricas durante deploy
    └── Health checks y readiness probes
    └── Automated rollback en caso de error

12. POST-DEPLOY
    └── Smoke tests en producción
    └── Verificación de SLOs/SLIs
    └── Notificación de éxito/fallo
    └── Actualización de runbooks y documentación
```

### 4.2 Pipeline Mobile (React Native / Expo)
```yaml
# .github/workflows/mobile-cd.yml
name: Mobile CD

on:
  push:
    branches: [main, release/*]
    tags: ['v*']
  pull_request:
    branches: [main]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - run: npm run lint
      - run: npm run type-check
      - run: npm run test:unit -- --coverage

  build-android:
    needs: validate
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - name: Build Android AAB
        run: |
          cd android
          ./gradlew bundleRelease
      - uses: actions/upload-artifact@v4
        with:
          name: android-aab
          path: android/app/build/outputs/bundle/release/*.aab

  build-ios:
    needs: validate
    runs-on: macos-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - name: Install CocoaPods
        run: cd ios && pod install
      - name: Build iOS
        run: |
          cd ios
          xcodebuild -workspace MyApp.xcworkspace             -scheme MyApp             -configuration Release             -destination 'generic/platform=iOS'             clean archive
      - uses: actions/upload-artifact@v4
        with:
          name: ios-archive
          path: ios/build/*.xcarchive

  deploy-staging:
    needs: [build-android, build-ios]
    runs-on: ubuntu-latest
    environment: staging
    steps:
      - name: Download artifacts
        uses: actions/download-artifact@v4
      - name: Deploy to Firebase App Distribution
        run: |
          # Upload AAB y IPA a Firebase para testing interno
          echo "Deploy to staging environment"

  deploy-production:
    needs: deploy-staging
    runs-on: ubuntu-latest
    environment: production
    if: startsWith(github.ref, 'refs/tags/v')
    steps:
      - name: Download artifacts
        uses: actions/download-artifact@v4
      - name: Deploy to Play Store
        run: |
          # Upload AAB a Google Play Store (production track)
          echo "Deploy Android to Play Store"
      - name: Deploy to App Store
        run: |
          # Upload IPA a App Store Connect
          echo "Deploy iOS to App Store"
```

### 4.3 Pipeline EAS Workflows (Expo - Referencia)
```yaml
# .eas/workflows/build-and-deploy.yml
name: Build and Deploy

on:
  push:
    branches: [main]

jobs:
  lint-and-test:
    steps:
      - uses: eas/checkout
      - uses: eas/install-node-modules
      - run: npm run lint
      - run: npm run test

  build-android:
    needs: [lint-and-test]
    type: build
    params:
      platform: android
      profile: production

  build-ios:
    needs: [lint-and-test]
    type: build
    params:
      platform: ios
      profile: production

  submit-android:
    needs: [build-android]
    type: submit
    params:
      build_id: ${{ jobs.build-android.outputs.build_id }}
      platform: android

  submit-ios:
    needs: [build-ios]
    type: submit
    params:
      build_id: ${{ jobs.build-ios.outputs.build_id }}
      platform: ios
```

## 5. Estrategias de Deployment Avanzadas

### 5.1 Canary Deployment
```yaml
# Ejemplo con Kubernetes + Flagger
steps:
  - name: Deploy Canary
    run: |
      kubectl apply -f k8s/canary/
      # Flagger automáticamente:
      # 1. Deploy 10% del tráfico a nueva versión
      # 2. Monitorea métricas (error rate, latency) por 5 min
      # 3. Si métricas OK, aumenta a 50%, luego 100%
      # 4. Si métricas FAIL, rollback automático a versión anterior
```

### 5.2 Blue-Green con Terraform
```hcl
# modules/blue-green/main.tf
locals {
  blue_weight  = var.active_environment == "blue" ? 100 : 0
  green_weight = var.active_environment == "green" ? 100 : 0
}

resource "aws_lb_target_group" "blue" {
  # ... config
}

resource "aws_lb_target_group" "green" {
  # ... config
}

resource "aws_lb_listener_rule" "main" {
  action {
    type             = "forward"
    target_group_arn = var.active_environment == "blue" ? aws_lb_target_group.blue.arn : aws_lb_target_group.green.arn
  }
}
```

## 6. Seguridad en CI/CD

### 6.1 Secrets Management
- **NUNCA** hardcodear secrets en archivos de pipeline
- Usar secrets nativos del CI/CD (GitHub Secrets, GitLab CI/CD Variables, Azure Key Vault)
- Rotación automática de secrets cada 90 días
- Uso de OIDC para autenticación cloud (evita credenciales de larga duración)

### 6.2 Supply Chain Security
- **SLSA**: Generar provenance attestations para artefactos
- **SBOM**: Generar Software Bill of Materials para cada build
- **Signed commits**: Requerir commits firmados (GPG)
- **Immutable tags**: Tags de imagen Docker inmutables (SHA, no `latest`)

### 6.3 Network Security
- **Private runners**: Para builds que acceden a recursos internos
- **VPN/Zero Trust**: Acceso a recursos privados via ZTNA
- **Egress filtering**: Controlar tráfico saliente de runners

## 7. Optimización de Costos en CI/CD

### 7.1 Caching Estratégico
```yaml
- name: Cache dependencies
  uses: actions/cache@v4
  with:
    path: |
      ~/.npm
      ~/.gradle/caches
      ~/.cocoapods
      ios/Pods
    key: ${{ runner.os }}-${{ hashFiles('**/package-lock.json', '**/Podfile.lock', '**/gradle.lockfile') }}
    restore-keys: |
      ${{ runner.os }}-
```

### 7.2 Runners Efímeros y Spot
- Usar runners self-hosted en Kubernetes (spot instances) para builds no críticas
- Escalar runners a 0 cuando no hay builds (KEDA/Event-driven autoscaling)
- Paralelizar jobs independientes para minimizar tiempo total

### 7.3 Path Filters
```yaml
on:
  push:
    paths:
      - 'src/mobile/**'
      - 'package.json'
      - '.github/workflows/mobile.yml'
```

## 8. Observabilidad en CI/CD

### 8.1 Métricas de Pipeline
- **Lead Time**: Tiempo desde commit hasta deploy en prod
- **Deployment Frequency**: Frecuencia de deploys a producción
- **Mean Time to Recovery (MTTR)**: Tiempo para recuperarse de un fallo
- **Change Failure Rate**: % de deploys que causan fallos
- **Build Duration**: Tiempo de ejecución del pipeline
- **Queue Time**: Tiempo de espera en cola

### 8.2 Dashboards
- DORA Metrics dashboard
- Pipeline status dashboard (por proyecto, por equipo)
- Cost dashboard (costo por build, por proyecto, por mes)

## 9. Workflow de Implementación CI/CD (APB)

```
1. ANÁLISIS
   └── Mapear tecnologías y dependencias del proyecto
   └── Identificar requisitos de compliance y seguridad
   └── Seleccionar plataforma de CI/CD y estrategia de deployment
   └── Definir SLAs/SLOs para el pipeline (tiempo máximo, disponibilidad)

2. DISEÑO
   └── Diseñar pipeline multi-etapa según estándar APB
   └── Definir estrategia de branching (GitFlow, trunk-based, etc.)
   └── Diseñar estrategia de environments (dev, staging, prod, review apps)
   └── Definir gates de aprobación y políticas de rollback

3. IMPLEMENTACIÓN
   └── Crear archivos de pipeline (.yml, .gitlab-ci.yml, Jenkinsfile)
   └── Configurar secrets, service accounts, y OIDC
   └── Implementar caching y optimización de builds
   └── Integrar escaneos de seguridad y quality gates

4. VALIDACIÓN
   └── Ejecutar pipeline end-to-end en entorno de prueba
   └── Medir métricas DORA baseline
   └── Realizar chaos testing en pipeline (simular fallos)
   └── Validar rollback procedures

5. OPERACIÓN
   └── Monitorear métricas de pipeline continuamente
   └── Optimizar tiempos de build y costos
   └── Mantener documentación de runbooks
   └── Revisar y actualizar políticas de seguridad
```

## 10. Integración con otras Skills APB

- **SKILL_PLAT_TERRAFORM**: Pipeline para IaC con validación de plan y costos
- **SKILL_PLAT_FINOPS**: Estimación de costos en pipeline (Infracost)
- **SKILL_OPS_OBSERVABILITY**: Métricas DORA y monitoreo de pipelines
- **SKILL_OPS_RUNBOOKS**: Runbooks de operación para fallos de deploy
- **SKILL_GOV_COMPLIANCE**: Gates de compliance en pipeline (políticas, aprobaciones)
- **SKILL_DEV_CODE_BASE**: Quality gates de código (coverage, linting, SonarQube)

## 11. Anti-patrones CI/CD (Qué NO hacer)

- **Deploy sin tests**: Desplegar a producción sin tests automatizados
- **Long-lived branches**: Branches que viven más de 1-2 días sin merge
- **Manual deploys**: Deploys manuales que no están automatizados
- **Secrets in repo**: Credenciales en archivos de configuración versionados
- **No rollback plan**: Deploy sin plan de rollback documentado y probado
- **Ignoring pipeline failures**: Ignorar fallos en pipeline y deployar manualmente
- **No environment parity**: Diferencias significativas entre entornos (dev ≠ prod)
- **Big bang deploys**: Deploys de grandes cambios sin canary/gradual rollout

## 12. Referencias

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitLab CI/CD Documentation](https://docs.gitlab.com/ee/ci/)
- [Azure DevOps Pipelines](https://docs.microsoft.com/en-us/azure/devops/pipelines/)
- [EAS Workflows Documentation](https://docs.expo.dev/eas-workflows/)
- [DORA Metrics](https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance)
- [SLSA Framework](https://slsa.dev/)
- [Expo CI/CD Workflows Skill](https://github.com/expo/skills/tree/main/skills/expo-cicd-workflows)
- [ArgoCD](https://argo-cd.readthedocs.io/)
- [FluxCD](https://fluxcd.io/)
