---
id: "third-lambdatest-test-automation-v1.0"
name: "Test Automation (E2E)"
description: "Automatización de tests E2E, adaptada de LambdaTest agent-skills y testdino-hq/playwright-skill."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "qa"
created_date: "2026-06-22"
review_date: "2026-06-22"
autonomy_level: 1
source_repo: "https://github.com/LambdaTest/agent-skills"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
---

# Automatización de Testing para APB

## Overview
Implementación de pruebas automatizadas en el pipeline CI/CD de la APB, cubriendo pruebas unitarias, de integración, E2E con Playwright, y pruebas de contrato API. Incluye patrones de Page Object Model (POM), generación de datos de prueba, y ejecución en paralelo para minimizar tiempo de feedback.

## When to Use
- Crear suite de pruebas automatizadas para nuevo proyecto
- Refactorizar pruebas existentes (legacy tests)
- Migrar pruebas manuales a automatizadas
- Optimizar tiempo de ejecución de suite existente
- Integrar nuevas herramientas de testing en pipeline

**When NOT to use:**
- Pruebas exploratorias (requieren juicio humano)
- Pruebas de usabilidad (requieren observación de usuarios)
- Validación de requisitos ambiguos (requieren clarificación con negocio)

## Core Pattern

### Fase 1: Selección de Herramientas por Stack

#### .NET / C#
| Tipo | Herramienta | Patrón |
|------|-------------|--------|
| Unitario | xUnit / NUnit | Arrange-Act-Assert |
| Mocking | Moq / NSubstitute | Inyección de dependencias |
| Integración | TestServer / WebApplicationFactory | In-memory DB |
| BDD | SpecFlow / Reqnroll | Gherkin scenarios |
| Cobertura | Coverlet + ReportGenerator | Cobertura por proyecto |

#### Django / Python
| Tipo | Herramienta | Patrón |
|------|-------------|--------|
| Unitario | pytest | Fixtures |
| Mocking | unittest.mock / pytest-mock | Patch |
| Integración | pytest-django | Test database |
| API | pytest + requests / DRF test client | CRUD tests |

#### Frontend / DevExtreme
| Tipo | Herramienta | Patrón |
|------|-------------|--------|
| E2E | Playwright | Page Object Model |
| Componente | Testing Library | User-centric queries |
| Visual | Playwright snapshots | Baseline comparison |

### Fase 2: Estructura de Pruebas

```
tests/
├── unit/
│   ├── controllers/
│   ├── services/
│   ├── repositories/
│   └── validators/
├── integration/
│   ├── api/
│   ├── database/
│   └── messaging/
├── e2e/
│   ├── pages/           # Page Objects
│   ├── specs/           # Test scenarios
│   └── fixtures/        # Test data
├── contract/
│   └── consumer-provider/
└── performance/
    └── load-tests/
```

### Fase 3: Patrón Page Object Model (POM)

```csharp
// Ejemplo .NET con Playwright
public class ExpedientesPage
{
    private readonly IPage _page;

    public ExpedientesPage(IPage page) => _page = page;

    // Selectores centralizados
    private ILocator SearchInput => _page.Locator("[data-testid='search-input']");
    private ILocator ResultsTable => _page.Locator("[data-testid='results-table']");
    private ILocator CreateButton => _page.Locator("[data-testid='btn-create']");

    // Acciones reutilizables
    public async Task SearchAsync(string query)
    {
        await SearchInput.FillAsync(query);
        await SearchInput.PressAsync("Enter");
    }

    public async Task<bool> HasResultsAsync() =>
        await ResultsTable.IsVisibleAsync();

    public async Task<CreateExpedientePage> ClickCreateAsync()
    {
        await CreateButton.ClickAsync();
        return new CreateExpedientePage(_page);
    }
}
```

### Fase 4: Generación de Datos de Prueba

#### Datos Sintéticos (Recomendado)
```csharp
// Bogus para .NET
var faker = new Faker<ExpedienteDto>("es")
    .RuleFor(e => e.Numero, f => f.Random.AlphaNumeric(10).ToUpper())
    .RuleFor(e => e.Titulo, f => f.Lorem.Sentence(3))
    .RuleFor(e => e.Fecha, f => f.Date.Past(1))
    .RuleFor(e => e.Estado, f => f.PickRandom<EstadoExpediente>());

var expediente = faker.Generate();
```

#### Datos Anonimizados de Producción
- Usar skill `apb-qa-anonymize-v1.0` para anonimización
- Validar que no quedan datos personales
- Documentar origen y transformación

### Fase 5: Pipeline CI/CD

```yaml
# Ejemplo GitHub Actions
name: Test Suite

on: [push, pull_request]

jobs:
  unit-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup .NET
        uses: actions/setup-dotnet@v4
        with:
          dotnet-version: '8.0.x'
      - name: Restore
        run: dotnet restore
      - name: Build
        run: dotnet build --no-restore
      - name: Test
        run: dotnet test --no-build --verbosity normal
      - name: Coverage
        run: dotnet test --collect:"XPlat Code Coverage"
      - name: Upload to SonarQube
        uses: SonarSource/sonarqube-scan-action@master

  integration-tests:
    needs: unit-tests
    runs-on: ubuntu-latest
    services:
      sqlserver:
        image: mcr.microsoft.com/mssql/server:2022-latest
        env:
          ACCEPT_EULA: Y
          SA_PASSWORD: ${{ secrets.TEST_DB_PASSWORD }}
    steps:
      - uses: actions/checkout@v4
      - name: Run Integration Tests
        run: dotnet test tests/integration --no-build

  e2e-tests:
    needs: integration-tests
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install Playwright
        run: npx playwright install
      - name: Run E2E Tests
        run: npx playwright test
      - name: Upload Report
        uses: actions/upload-artifact@v4
        with:
          name: playwright-report
          path: playwright-report/
```

### Fase 6: Optimización

#### Ejecución en Paralelo
```csharp
// xUnit: paralelismo por colección
[CollectionDefinition("Database", DisableParallelization = false)]
public class DatabaseCollection { }

// Playwright: workers paralelos
// playwright.config.ts
export default defineConfig({
  workers: process.env.CI ? 4 : undefined,
  fullyParallel: true,
});
```

#### Selección Inteligente de Pruebas
- **Pruebas impactadas:** Ejecutar solo pruebas relacionadas con cambios
- **Pruebas flaky:** Identificar y aislar pruebas inestables
- **Pruebas lentas:** Optimizar o mover a suite nocturna

## Quick Reference

| Problema | Solución |
|----------|----------|
| Tests flaky | Aislar, añadir esperas explícitas, evitar dependencias temporales |
| Suite lenta (> 15 min) | Paralelizar, mock de dependencias, test impactados |
| Cobertura baja | Identificar gaps, añadir tests para branches no cubiertas |
| Datos inconsistentes | Usar factories/fixtures, reset de BD entre tests |
| Mantenimiento costoso | POM, data-testid, evitar selectores frágiles (xpath) |

## Implementation

### Checklist de Automatización
```
□ Estructura de carpetas definida
□ Page Objects creados (E2E)
□ Fixtures/factories de datos implementadas
□ Pipeline CI/CD configurado
□ Cobertura reportada a SonarQube
□ Pruebas ejecutan en < 15 min (unit + integración)
□ Reporte de resultados generado
□ Pruebas flaky identificadas y documentadas
```

## Common Mistakes
- **Selectores frágiles:** Usar xpath o clases CSS cambiantes → usar data-testid
- **Tests interdependientes:** Cada test debe ser independiente y aislado
- **Datos hardcodeados:** Usar factories para datos dinámicos
- **No limpiar estado:** Cada test debe dejar el sistema como lo encontró
- **Ignorar tests fallidos:** Los tests fallidos deben corregirse, no saltarse
- **Sobre-automatizar:** No automatizar pruebas que cambian frecuentemente o son exploratorias

## Real-World Impact
- Reducción de 70% en tiempo de regresión
- Detección de 3x más defectos en fase de desarrollo
- Feedback en < 5 min tras push (unit + integración)

---

## Adapted From
- **Source:** LambdaTest/agent-skills + testdino-hq/playwright-skill
- **License:** MIT
- **Attribution:** Patrones de automatización E2E, POM, y configuración de pipeline inspirados en LambdaTest y Playwright skills. Reescrito completamente para stack tecnológico APB (.NET, Django, DevExtreme) y pipeline Azure DevOps/Jenkins.

## References
- Playwright Best Practices
- xUnit Documentation
- pytest Documentation
- context/apb/standards/qa-standards.md
- context/apb/templates/test-template/
