---
id: "third-clear-solutions-unit-test-gen-v1.0"
name: "Unit Test Generation"
description: "Generación de tests unitarios y casos de prueba, adaptada de clear-solutions/unit-tests-skills."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "qa"
created_date: "2026-06-22"
review_date: "2026-06-22"
autonomy_level: 1
source_repo: "https://github.com/clear-solutions/unit-tests-skills"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
---

# Generación de Pruebas Unitarias para APB

## Overview
Generación automatizada de pruebas unitarias con cobertura mínima del 80%, aplicando principios de Arrange-Act-Assert, inyección de dependencias, mocking apropiado y patrones de TDD (Test-Driven Development) cuando se genera código nuevo. Adaptado al stack tecnológico APB (.NET xUnit/NUnit/Moq, pytest) y a los estándares de calidad corporativos.

## When to Use
- Generación de tests para código nuevo (TDD: RED-GREEN-REFACTOR)
- Añadir tests a código legacy sin cobertura
- Alcanzar umbral de cobertura requerido (≥ 80%)
- Refactorización de tests existentes (flaky, lentos, frágiles)
- Bugfix: crear test que reproduzca el bug antes de corregir

**When NOT to use:**
- Tests de integración (usar skill apb-qa-test-auto-v1.0)
- Tests E2E (usar skill apb-qa-test-auto-v1.0)
- Código sin lógica (DTOs puros, getters/setters triviales)
- Código que será eliminado en próxima iteración

## Core Pattern

### Patrón Arrange-Act-Assert (AAA)

```csharp
// .NET / xUnit
[Fact]
public async Task CreateExpediente_WithValidData_ReturnsCreated()
{
    // Arrange
    var command = new CreateExpedienteCommand
    {
        Titulo = "Test Expediente",
        Tipo = TipoExpediente.Administrativo
    };
    var handler = new CreateExpedienteCommandHandler(
        _mockRepository.Object,
        _mockUnitOfWork.Object,
        _mockMapper.Object);

    // Act
    var result = await handler.Handle(command, CancellationToken.None);

    // Assert
    result.Should().NotBeNull();
    result.Id.Should().BeGreaterThan(0);
    _mockUnitOfWork.Verify(u => u.SaveChangesAsync(It.IsAny<CancellationToken>()), Times.Once);
}
```

```python
# Python / pytest
def test_create_expediente_with_valid_data_returns_created():
    # Arrange
    expediente_data = {
        "titulo": "Test Expediente",
        "tipo": "administrativo"
    }
    mock_repo = Mock(spec=ExpedienteRepository)
    mock_repo.create.return_value = Expediente(id=1, **expediente_data)
    service = ExpedienteService(mock_repo)

    # Act
    result = service.create(expediente_data)

    # Assert
    assert result is not None
    assert result.id == 1
    mock_repo.create.assert_called_once()
```

### Patrón TDD (RED-GREEN-REFACTOR)

Cuando se genera código nuevo:

1. **RED:** Escribir test que falla
   ```csharp
   [Fact]
   public void CalculateTotal_WithEmptyList_ReturnsZero()
   {
       var calculator = new InvoiceCalculator();
       var result = calculator.CalculateTotal(new List<LineItem>());
       result.Should().Be(0); // Falla: método no existe
   }
   ```

2. **GREEN:** Implementar código mínimo para pasar
   ```csharp
   public decimal CalculateTotal(List<LineItem> items)
   {
       return items.Sum(i => i.Quantity * i.UnitPrice);
   }
   ```

3. **REFACTOR:** Mejorar código manteniendo tests verdes
   ```csharp
   public decimal CalculateTotal(List<LineItem> items)
   {
       if (items == null || !items.Any())
           return 0;

       return items.Sum(i => i.Quantity * i.UnitPrice);
   }
   ```

### Principios de Diseño de Tests

#### 1. Un test, una responsabilidad
```csharp
// ❌ MAL: Un test con múltiples asserts no relacionados
[Fact]
public void CreateExpediente_ValidatesEverything()
{
    var result = _service.Create(new ExpedienteDto());
    result.Should().NotBeNull();
    result.Id.Should().BeGreaterThan(0);
    result.FechaCreacion.Should().BeCloseTo(DateTime.UtcNow, TimeSpan.FromSeconds(1));
    result.Estado.Should().Be(EstadoExpediente.Borrador);
}

// ✅ BIEN: Tests separados por comportamiento
[Fact]
public void CreateExpediente_WithValidData_ReturnsExpedienteWithId()
{
    var result = _service.Create(new ExpedienteDto { Titulo = "Test" });
    result.Id.Should().BeGreaterThan(0);
}

[Fact]
public void CreateExpediente_WithValidData_SetsInitialStateToBorrador()
{
    var result = _service.Create(new ExpedienteDto { Titulo = "Test" });
    result.Estado.Should().Be(EstadoExpediente.Borrador);
}
```

#### 2. Nombres descriptivos
```csharp
// Patrón: MethodName_StateUnderTest_ExpectedBehavior
[Fact]
public void CalculateTotal_WithNegativeQuantity_ThrowsArgumentException()
[Fact]
public void GetExpedienteById_WithNonExistingId_ReturnsNull()
[Fact]
public async Task UpdateExpedienteAsync_WithConcurrentModification_ThrowsConflictException()
```

#### 3. Mocking apropiado
```csharp
// Mockar dependencias externas, NO la unidad bajo test
[Fact]
public async Task ProcessPayment_WithValidCard_CallsPaymentGateway()
{
    // Arrange
    var mockGateway = new Mock<IPaymentGateway>();
    var mockLogger = new Mock<ILogger<PaymentService>>();
    var service = new PaymentService(mockGateway.Object, mockLogger.Object);

    mockGateway.Setup(g => g.ChargeAsync(It.IsAny<PaymentRequest>()))
               .ReturnsAsync(new PaymentResult { Success = true });

    // Act
    await service.ProcessPayment(new PaymentRequest { Amount = 100 });

    // Assert
    mockGateway.Verify(g => g.ChargeAsync(It.Is<PaymentRequest>(
        r => r.Amount == 100)), Times.Once);
}
```

#### 4. Datos de prueba con Bogus (faker)
```csharp
private readonly Faker<ExpedienteDto> _expedienteFaker = new Faker<ExpedienteDto>("es")
    .RuleFor(e => e.Titulo, f => f.Lorem.Sentence(3))
    .RuleFor(e => e.Descripcion, f => f.Lorem.Paragraph())
    .RuleFor(e => e.Tipo, f => f.PickRandom<TipoExpediente>())
    .RuleFor(e => e.FechaLimite, f => f.Date.Future(1));

[Fact]
public void CreateExpediente_WithRandomValidData_Succeeds()
{
    var dto = _expedienteFaker.Generate();
    var result = _service.Create(dto);
    result.Should().NotBeNull();
}
```

### Cobertura Objetivo

| Nivel | Cobertura | Qué cubrir |
|-------|-----------|------------|
| **Líneas** | ≥ 80% | Todas las líneas ejecutables |
| **Branches** | ≥ 70% | Todas las ramas condicionales |
| **Methods** | ≥ 90% | Todos los métodos públicos |
| **Classes** | 100% | Todas las clases con lógica |

### Anti-patrones a evitar

| Anti-patrón | Problema | Solución |
|-------------|----------|----------|
| **Test de implementación** | Test falla al refactorizar | Testar comportamiento, no estructura interna |
| **Mock excesivo** | Test no valida integración real | Usar integración para interacciones complejas |
| **Datos hardcodeados** | Test frágil, no representativo | Usar factories/faker |
| **Tests interdependientes** | Orden de ejecución importa | Cada test aislado, cleanup en teardown |
| **Assert múltiple** | Difícil identificar qué falló | Un assert por test o usar fluent assertions |
| **Sin cleanup** | Estado residual afecta otros tests | Dispose, teardown, reset de mocks |

## Quick Reference

| Escenario | Técnica | Ejemplo |
|-----------|---------|---------|
| Excepción esperada | Assert.Throws / pytest.raises | `Assert.Throws<ArgumentException>(() => service.Method(null))` |
| Async/await | async Task / async def | `await service.MethodAsync()` |
| Colecciones | Should().Contain / assert in | `result.Should().Contain(x => x.Id == 1)` |
| Fechas | BeCloseTo / approx | `result.Fecha.Should().BeCloseTo(expected, TimeSpan.FromSeconds(1))` |
| Mock verification | Verify / assert_called | `mock.Verify(m => m.Method(), Times.Once)` |

## Implementation

### Estructura de proyecto .NET
```
tests/
├── UnitTests/
│   ├── Application/
│   │   ├── Commands/
│   │   │   └── CreateExpedienteCommandHandlerTests.cs
│   │   └── Queries/
│   │       └── GetExpedienteByIdQueryHandlerTests.cs
│   ├── Domain/
│   │   ├── Entities/
│   │   │   └── ExpedienteTests.cs
│   │   └── ValueObjects/
│   │       └── NifTests.cs
│   └── Infrastructure/
│       └── Repositories/
│           └── ExpedienteRepositoryTests.cs
└── Shared/
    └── Factories/
        └── ExpedienteFactory.cs
```

### Estructura de proyecto Python
```
tests/
├── unit/
│   ├── test_services.py
│   ├── test_repositories.py
│   └── test_domain.py
├── factories/
│   └── expediente_factory.py
├── conftest.py
└── __init__.py
```

## Common Mistakes
- **Generar tests sin entender el código:** Los tests deben validar el comportamiento esperado, no solo ejecutar el código
- **Ignorar edge cases:** Null, vacío, valores límite, excepciones
- **Tests lentos:** Evitar I/O, base de datos, llamadas externas en unit tests
- **No mantener tests:** Tests obsoletos generan desconfianza y falsos positivos
- **Cobertura como objetivo final:** 100% cobertura con tests malos es peor que 80% con tests buenos
- **Olvidar teardown:** Estado residual entre tests causa flaky tests
- **Testear getters/setters:** No aportan valor, consumen tiempo de ejecución

## Real-World Impact
- Aumento de 3x en detección de defectos en fase de desarrollo
- Reducción de 50% en tiempo de debugging
- Confianza en refactorizaciones con suite de tests verde

---

## Adapted From
- **Source:** clear-solutions/unit-tests-skills — skills `generate-tests` y `generate-test-cases`
- **License:** MIT
- **Attribution:** Patrones de generación de tests unitarios, estructura AAA, y principios de diseño de tests inspirados en clear-solutions/unit-tests-skills. Reescrito completamente para stack tecnológico APB (.NET xUnit/Moq, pytest) y estándares de cobertura corporativos.

## Also Inspired By
- **Source:** obra/superpowers — skill `test-driven-development`
- **License:** MIT
- **Attribution:** Patrón RED-GREEN-REFACTOR y filosofía TDD inspirados en obra/superpowers.

## References
- xUnit Documentation
- Moq Documentation
- pytest Documentation
- Bogus Documentation
- context/apb/standards/development-standards.md
- context/apb/standards/qa-standards.md
