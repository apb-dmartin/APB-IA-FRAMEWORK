---
id: "third-neolabhq-ddd-clean-architecture-v1.0"
name: "DDD, Clean Architecture y SOLID Multi-lenguaje"
description: "Reglas consolidadas de Domain-Driven Development, Clean Architecture, SOLID y patrones funcionales, con ejemplos en Python, Java, TypeScript, Go, C# y Rust, más guías enterprise."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "development"
created_date: "2026-06-22"
review_date: "2026-06-22"
autonomy_level: 1
source_repo: "https://github.com/NeoLabHQ/context-engineering-kit"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
---

# SKILL_DEV_CODE_BASE — Code Quality Foundations

## 1. Propósito y Alcance

Esta skill consolida las reglas de calidad de código del plugin DDD de NeoLabHQ
en un framework unificado para APB, extendiendo el alcance a:
- **Multi-lenguaje**: Python, Java, TypeScript/JavaScript, Go, C#, Java/Kotlin, Rust, C++
- **Multi-paradigma**: OOP, Funcional, Procedural, Híbrido
- **Enterprise**: Guidelines para equipos grandes, code reviews, y onboarding
- **Legacy**: Patrones para modernizar código existente sin reescritura total

**Casos de uso principales:**
1. Establecer estándares de calidad de código para nuevos proyectos
2. Refactorizar código legacy aplicando DDD y Clean Architecture
3. Definir arquitecturas de software mantenibles y testables
4. Onboarding de nuevos desarrolladores con guidelines claros
5. Code reviews consistentes con criterios objetivos

## 2. Principios Core de Calidad de Código (APB)

### 2.1 SOLID (Aplicado universalmente)

**S - Single Responsibility Principle (SRP)**
- Cada clase/módulo/función debe tener una única razón para cambiar
- Máximo 5 métodos públicos por clase (regla guía)
- Funciones: máximo 20 líneas (preferiblemente 10)
- Separar lógica de negocio, lógica de infraestructura, y lógica de presentación

**O - Open/Closed Principle (OCP)**
- Abierto para extensión, cerrado para modificación
- Usar polimorfismo, composición, y strategy patterns en lugar de if/else extensos
- Evitar modificar código existente para añadir funcionalidad

**L - Liskov Substitution Principle (LSP)**
- Clases hijas deben ser sustituibles por clases padres sin alterar comportamiento
- Validar con tests de contrato (precondiciones, postcondiciones, invariantes)
- Evitar overrides que vacíen métodos padre o cambien significado

**I - Interface Segregation Principle (ISP)**
- Preferir interfaces pequeñas y específicas sobre interfaces grandes
- Ningún cliente debe depender de métodos que no usa
- Split interfaces cuando un cliente implemente métodos vacíos

**D - Dependency Inversion Principle (DIP)**
- Depender de abstracciones, no de concreciones
- Inyección de dependencias obligatoria para lógica de negocio
- No instanciar dependencias directamente (usar factories, DI containers, o inyección constructor)

### 2.2 Clean Architecture (Onion Architecture)

```
┌─────────────────────────────────────┐
│           Presentation              │  ← UI, API Controllers, CLI
│         (Frameworks/Drivers)        │
├─────────────────────────────────────┤
│         Application Services        │  ← Use Cases, DTOs, Mappers
│            (Use Cases)              │
├─────────────────────────────────────┤
│          Domain Services            │  ← Lógica de negocio pura
│         (Business Rules)            │
├─────────────────────────────────────┤
│         Domain Entities             │  ← Entidades, Value Objects, Aggregates
│            (Enterprise)             │
├─────────────────────────────────────┤
│         Domain Events               │  ← Eventos de dominio, Policies
│            (Enterprise)             │
└─────────────────────────────────────┘
```

**Reglas de dependencia:**
- Las capas internas NO conocen las capas externas
- Las dependencias apuntan siempre hacia el centro (Domain)
- Las capas externas se adaptan a las interfaces definidas por las internas
- Domain NO tiene dependencias de frameworks, ORMs, o librerías externas

### 2.3 Domain-Driven Design (DDD) - Patrones Tácticos

**Value Objects**
- Inmutables, sin identidad, definidos por sus atributos
- Validación en constructor/factory; nunca en estado inválido
- Ejemplos: Money, Email, Address, DateRange, Quantity
- Implementar `equals()` y `hashCode()` basado en atributos

**Entities**
- Identidad única que persiste a través de cambios de estado
- Validación de invariantes en métodos de dominio
- No exponer setters públicos; usar métodos de dominio semánticos
- Ejemplo: `Order.cancel()` en lugar de `Order.setStatus("CANCELLED")`

**Aggregates**
- Cluster de entidades y value objects con un root entity
- Root entity controla acceso a miembros internos
- Transacciones solo a nivel de aggregate; no modificar múltiples aggregates en una transacción
- Máximo 1 nivel de profundidad en relaciones (evitar árboles profundos)

**Domain Events**
- Eventos que representan hechos del dominio (pasado: `OrderPlaced`, `PaymentReceived`)
- Inmutables; nombre en pasado
- Publicados por aggregates; consumidos por subscribers/handlers
- No usar para comunicación entre bounded contexts (usar integration events)

**Repositories**
- Abstracción de persistencia para aggregates
- Una por aggregate root; no exponer queries ad-hoc
- Métodos: `save()`, `findById()`, `findByCriteria()` (específicos de dominio)
- Implementación en capa de infraestructura (adaptador)

**Domain Services**
- Lógica de negocio que no pertenece a ninguna entidad o value object
- Stateless; operan sobre múltiples aggregates
- Ejemplo: `PricingService.calculateDiscount()`, `TransferService.execute()`

**Factories**
- Encapsulan lógica de creación compleja
- Validación de precondiciones antes de crear
- Métodos estáticos o clases dedicadas (no lógica en constructores complejos)

**Policies**
- Encapsulan reglas de negocio que varían o son complejas
- Strategy pattern para diferentes implementaciones
- Ejemplo: `ShippingPolicy`, `DiscountPolicy`, `TaxPolicy`

### 2.4 Functional Core / Imperative Shell (Arquitectura Funcional)

```
┌─────────────────────────────────────┐
│         Imperative Shell            │  ← I/O, DB, HTTP, UI, Side Effects
│         (Side Effects)              │
├─────────────────────────────────────┤
│          Functional Core            │  ← Pure Functions, Business Logic
│         (Pure Functions)            │
│   Input → [Pure Logic] → Output     │
│   No side effects, no state mutable │
└─────────────────────────────────────┘
```

**Reglas:**
- Core funcional: funciones puras (misma entrada → misma salida, no side effects)
- Shell imperativo: coordina I/O, persiste resultados, maneja efectos
- Separar claramente; testear core funcional sin mocks
- Shell testeable con integration tests; core con unit tests simples

### 2.5 Command-Query Separation (CQS)

- **Commands**: Mutan estado, no retornan valores (void), pueden lanzar excepciones
- **Queries**: No mutan estado, retornan valores, no lanzan excepciones (null/empty en su lugar)
- **No mezclar**: Un método que muta y retorna datos viola CQS
- Excepción: CQRS (separar modelos de lectura y escritura físicamente)

## 3. Reglas de Estilo por Lenguaje

### 3.1 Python
```python
# ✅ CORRECTO - Value Object con validación
from dataclasses import dataclass
from typing import NewType
import re

Email = NewType('Email', str)

@dataclass(frozen=True)  # Inmutable
class Money:
    amount: int  # Centavos para evitar floats
    currency: str  # ISO 4217

    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("Amount cannot be negative")
        if len(self.currency) != 3:
            raise ValueError("Currency must be ISO 4217 code")

    def add(self, other: 'Money') -> 'Money':
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        return Money(self.amount + other.amount, self.currency)

# ✅ CORRECTO - Entity con métodos de dominio
from uuid import UUID, uuid4
from dataclasses import dataclass, field
from datetime import datetime
from typing import List

@dataclass
class Order:
    id: UUID = field(default_factory=uuid4)
    items: List['OrderItem'] = field(default_factory=list)
    status: str = "PENDING"
    created_at: datetime = field(default_factory=datetime.now)

    def add_item(self, product_id: UUID, quantity: int, unit_price: Money) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if self.status != "PENDING":
            raise ValueError("Cannot modify non-pending order")

        self.items.append(OrderItem(product_id, quantity, unit_price))

    def cancel(self) -> None:
        if self.status == "SHIPPED":
            raise ValueError("Cannot cancel shipped order")
        self.status = "CANCELLED"

    def total(self) -> Money:
        if not self.items:
            return Money(0, "USD")
        total = sum(item.total().amount for item in self.items)
        return Money(total, self.items[0].unit_price.currency)

# ❌ INCORRECTO - Anemic Domain Model
@dataclass
class BadOrder:
    id: UUID
    items: List[dict]  # Diccionarios sin tipo
    status: str
    # Lógica de negocio en Service externo (anemic model)
```

### 3.2 TypeScript/JavaScript
```typescript
// ✅ CORRECTO - Value Object inmutable
export class Email {
    private constructor(private readonly value: string) {}

    static create(email: string): Result<Email, ValidationError> {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!regex.test(email)) {
            return Result.fail(new ValidationError("Invalid email format"));
        }
        return Result.ok(new Email(email.toLowerCase()));
    }

    toString(): string { return this.value; }
    equals(other: Email): boolean { return this.value === other.value; }
}

// ✅ CORRECTO - Entity con Aggregate Root
export class Order extends AggregateRoot<OrderId> {
    private items: OrderItem[] = [];
    private status: OrderStatus = OrderStatus.PENDING;

    addItem(productId: ProductId, quantity: Quantity, unitPrice: Money): void {
        if (this.status !== OrderStatus.PENDING) {
            throw new DomainError("Cannot modify non-pending order");
        }

        const item = new OrderItem(productId, quantity, unitPrice);
        this.items.push(item);
        this.addDomainEvent(new OrderItemAdded(this.id, item));
    }

    cancel(): void {
        if (this.status === OrderStatus.SHIPPED) {
            throw new DomainError("Cannot cancel shipped order");
        }
        this.status = OrderStatus.CANCELLED;
        this.addDomainEvent(new OrderCancelled(this.id));
    }

    getTotal(): Money {
        return this.items.reduce((sum, item) => sum.add(item.getTotal()), Money.zero());
    }
}

// ✅ CORRECTO - Repository Interface (Domain)
export interface OrderRepository {
    save(order: Order): Promise<void>;
    findById(id: OrderId): Promise<Order | null>;
    findPending(): Promise<Order[]>;
}

// ✅ CORRECTO - Repository Implementation (Infrastructure)
export class PostgresOrderRepository implements OrderRepository {
    constructor(private readonly db: Knex) {}

    async save(order: Order): Promise<void> {
        // Implementación con ORM/Query Builder
    }

    async findById(id: OrderId): Promise<Order | null> {
        // Implementación
    }

    async findPending(): Promise<Order[]> {
        // Implementación
    }
}
```

### 3.3 Java
```java
// ✅ CORRECTO - Value Object inmutable
public final class Money {
    private final BigDecimal amount;
    private final Currency currency;

    private Money(BigDecimal amount, Currency currency) {
        this.amount = amount;
        this.currency = currency;
    }

    public static Money of(BigDecimal amount, String currencyCode) {
        if (amount.compareTo(BigDecimal.ZERO) < 0) {
            throw new IllegalArgumentException("Amount cannot be negative");
        }
        return new Money(amount.setScale(2, RoundingMode.HALF_UP), 
                        Currency.getInstance(currencyCode));
    }

    public Money add(Money other) {
        if (!this.currency.equals(other.currency)) {
            throw new IllegalArgumentException("Cannot add different currencies");
        }
        return new Money(this.amount.add(other.amount), this.currency);
    }

    // equals, hashCode, toString basados en atributos
}

// ✅ CORRECTO - Entity con Aggregate Root
public class Order extends AggregateRoot<OrderId> {
    private final List<OrderItem> items = new ArrayList<>();
    private OrderStatus status = OrderStatus.PENDING;

    public void addItem(ProductId productId, Quantity quantity, Money unitPrice) {
        if (status != OrderStatus.PENDING) {
            throw new DomainException("Cannot modify non-pending order");
        }
        OrderItem item = new OrderItem(productId, quantity, unitPrice);
        items.add(item);
        registerEvent(new OrderItemAdded(this.getId(), item));
    }

    public void cancel() {
        if (status == OrderStatus.SHIPPED) {
            throw new DomainException("Cannot cancel shipped order");
        }
        this.status = OrderStatus.CANCELLED;
        registerEvent(new OrderCancelled(this.getId()));
    }

    public Money getTotal() {
        return items.stream()
            .map(OrderItem::getTotal)
            .reduce(Money.zero(currency), Money::add);
    }
}
```

### 3.4 Go
```go
// ✅ CORRECTO - Value Object inmutable
type Money struct {
    amount   int64  // Centavos
    currency string // ISO 4217
}

func NewMoney(amount int64, currency string) (Money, error) {
    if amount < 0 {
        return Money{}, errors.New("amount cannot be negative")
    }
    if len(currency) != 3 {
        return Money{}, errors.New("currency must be ISO 4217 code")
    }
    return Money{amount: amount, currency: strings.ToUpper(currency)}, nil
}

func (m Money) Add(other Money) (Money, error) {
    if m.currency != other.currency {
        return Money{}, errors.New("cannot add different currencies")
    }
    return NewMoney(m.amount+other.amount, m.currency)
}

func (m Money) Equals(other Money) bool {
    return m.amount == other.amount && m.currency == other.currency
}

// ✅ CORRECTO - Entity con métodos de dominio
type Order struct {
    id     uuid.UUID
    items  []OrderItem
    status OrderStatus
}

func (o *Order) AddItem(productID uuid.UUID, quantity int, unitPrice Money) error {
    if o.status != StatusPending {
        return errors.New("cannot modify non-pending order")
    }
    if quantity <= 0 {
        return errors.New("quantity must be positive")
    }
    o.items = append(o.items, OrderItem{productID, quantity, unitPrice})
    return nil
}

func (o *Order) Cancel() error {
    if o.status == StatusShipped {
        return errors.New("cannot cancel shipped order")
    }
    o.status = StatusCancelled
    return nil
}
```

## 4. Anti-patrones de Calidad de Código (Qué NO hacer)

### 4.1 Anemic Domain Model
- Entidades con solo getters/setters (data bags)
- Lógica de negocio en Services procedurales
- Violación de SRP; acoplamiento entre data y behavior
- **Solución**: Mover lógica de negocio a entidades y value objects

### 4.2 God Class / God Object
- Clase con múltiples responsabilidades (>500 líneas, >20 métodos)
- Conocimiento excesivo del sistema
- **Solución**: Extraer clases cohesivas, aplicar SRP

### 4.3 Feature Envy
- Método que usa más datos de otra clase que de la suya
- **Solución**: Mover método a la clase que tiene los datos

### 4.4 Primitive Obsession
- Uso de tipos primitivos (String, int) para conceptos de dominio
- Ejemplo: `String email` en lugar de `Email email`
- **Solución**: Crear Value Objects para conceptos del dominio

### 4.5 Null References / Null Pointer Exceptions
- Retornar null para indicar ausencia de valor
- **Solución**: Usar Option/Maybe/Result types, Null Object pattern

### 4.6 Magic Numbers / Strings
- Valores hardcodeados sin contexto
- **Solución**: Constantes con nombres descriptivos, Value Objects

### 4.7 Deep Nesting / Arrow Code
- Múltiples niveles de if/else anidados
- **Solución**: Early returns, guard clauses, extract methods, polymorphism

### 4.8 Tight Coupling
- Dependencias directas entre clases concretas
- **Solución**: Inversión de dependencias, interfaces, eventos

## 5. Métricas de Calidad de Código

| Métrica | Herramienta | Target | Descripción |
|---------|-------------|--------|-------------|
| Cyclomatic Complexity | SonarQube, CodeClimate | < 10 por método | Número de caminos independientes |
| Cognitive Complexity | SonarQube | < 15 por método | Dificultad de comprensión |
| Code Coverage | pytest, Jest, JUnit | > 80% lógica de negocio | % de código cubierto por tests |
| Duplication | SonarQube, PMD | < 3% | Código duplicado |
| Technical Debt Ratio | SonarQube | < 5% | Tiempo de refactorización vs. tiempo de desarrollo |
| Method Length | Checkstyle, ESLint | < 20 líneas | Longitud de métodos |
| Class Length | Checkstyle, ESLint | < 200 líneas | Longitud de clases |
| Parameters per Method | Pylint, ESLint | < 4 | Número de parámetros |
| Dependencies per Class | JDepend | < 10 | Acoplamiento aferente/eferente |

## 6. Checklist de Code Review

### 6.1 Diseño y Arquitectura
- [ ] ¿Sigue los principios SOLID?
- [ ] ¿Las entidades tienen comportamiento (no solo datos)?
- [ ] ¿Los value objects son inmutables y validados?
- [ ] ¿Las dependencias apuntan hacia el dominio?
- [ ] ¿No hay acoplamiento circular?
- [ ] ¿Los aggregates tienen root claro y límites definidos?

### 6.2 Calidad de Código
- [ ] ¿Nombres descriptivos (variables, funciones, clases)?
- [ ] ¿Funciones cortas y enfocadas (< 20 líneas)?
- [ ] ¿Sin código duplicado?
- [ ] ¿Sin magic numbers/strings?
- [ ] ¿Manejo de errores explícito (no silencioso)?
- [ ] ¿Sin comentarios que expliquen "qué" (el código debe ser autoexplicativo)?

### 6.3 Testing
- [ ] ¿Tests unitarios para lógica de negocio?
- [ ] ¿Tests de integración para repositories?
- [ ] ¿Tests de contrato para APIs?
- [ ] ¿Coverage > 80% para lógica de negocio?
- [ ] ¿Tests nombrados descriptivamente (given_when_then)?
- [ ] ¿Sin tests que dependan de estado externo?

### 6.4 Seguridad
- [ ] ¿No hay secrets hardcodeados?
- [ ] ¿Validación de inputs en boundaries?
- [ ] ¿Sanitización de outputs?
- [ ] ¿Principio de mínimo privilegio en permisos?
- [ ] ¿No hay SQL injection / XSS vulnerabilities?

## 7. Workflow de Implementación (APB)

```
1. ANÁLISIS DE DOMINIO
   └── Identificar bounded contexts y subdomains
   └── Definir ubiquitous language con stakeholders
   └── Mapear aggregates, entities, y value objects
   └── Identificar domain events y policies

2. DISEÑO DE ARQUITECTURA
   └── Definir capas (Domain, Application, Infrastructure, Presentation)
   └── Diseñar interfaces de repositories (ports)
   └── Definir contratos de APIs (DTOs, serializers)
   └── Seleccionar patrones de integración (events, RPC, REST)

3. IMPLEMENTACIÓN
   └── Implementar domain layer primero (entities, value objects, domain services)
   └── Implementar application layer (use cases, DTOs, mappers)
   └── Implementar infrastructure layer (repositories, external services)
   └── Implementar presentation layer (controllers, views, CLI)
   └── Aplicar TDD: test primero, luego implementación

4. REFACTORIZACIÓN
   └── Identificar code smells con herramientas estáticas
   └── Aplicar refactorings catalog (Martin Fowler)
   └── Extraer value objects de primitivos
   └── Mover lógica de services a entidades
   └── Simplificar condicionales con polimorfismo

5. VALIDACIÓN
   └── Ejecutar suite de tests completa
   └── Verificar métricas de calidad (SonarQube, CodeClimate)
   └── Realizar code review con checklist
   └── Documentar decisiones arquitectónicas (ADRs)
```

## 8. Integración con otras Skills APB

- **SKILL_DEV_MICRO_BASE**: Extensión de DDD para microservicios (context mapping, integration events)
- **SKILL_DEV_IMPLEMENT**: Implementación específica con Spec-Driven Development
- **SKILL_DEV_AUTOCORRECT**: Reflexión y auto-corrección de código
- **SKILL_DEV_REVIEW_TL**: Code review por tech leads con foco en arquitectura
- **SKILL_DEV_REVIEW_ADVANCED**: Code review avanzado con análisis estático
- **SKILL_ARCH_DDD**: Diseño arquitectónico con DDD estratégico
- **SKILL_ARCH_EVENT_STORMING**: Descubrimiento de dominio con event storming

## 9. Referencias

- [NeoLabHQ/context-engineering-kit - DDD Plugin](https://github.com/NeoLabHQ/context-engineering-kit)
- [Domain-Driven Design - Eric Evans](https://www.domainlanguage.com/)
- [Implementing Domain-Driven Design - Vaughn Vernon](https://www.dddcommunity.org/book/vernon/)
- [Clean Architecture - Robert C. Martin](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [SOLID Principles](https://en.wikipedia.org/wiki/SOLID)
- [Refactoring - Martin Fowler](https://refactoring.com/)
- [Functional Core, Imperative Shell - Gary Bernhardt](https://www.destroyallsoftware.com/screencasts/catalog/functional-core-imperative-shell)
- [Python DDD Example - github.com/cosmicpython](https://github.com/cosmicpython/code)
