---
id: "apb-qa-anonymize-v1.0"
name: "Anonimización y Generación de Datos de Prueba"
description: "Genera datasets de prueba realistas y anonimiza datos sensibles para entornos de desarrollo, testing y demos, garantizando cumplimiento GDPR mediante técnicas de pseudonimización, generalización, sustitución sintética, ruido diferencial y k-anonimato. Incluye tabla de dominios ficticios APB y scripts concretos por motor (Oracle, SQL Server, Cosmos DB, PostGIS, .NET, TypeScript)."
version: "1.2.0"
status: "draft"
owner: "QA / Ciberseguridad APB <arquitectura@portdebarcelona.cat>"
domain: "qa"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-24"
depends_on:
  - "apb-sec-ens-v1.0"
---

# Anonimización y Generación de Datos de Prueba

> Las secciones 5 (técnicas de anonimización) y 6 (validación) incorporan,
> fusionados y adaptados, contenidos de una skill de terceros bajo licencia
> MIT. Ver sección 9, Procedencia.

> **Fusión Sesión QA (post-Sesión 12):** la sección 11 (Dominios Ficticios APB) y la
> sección 12 (Fixtures Concretos por Motor) incorporan, fusionados y adaptados, el
> contenido de `apb-test-data-rgpd` (repo `apb-ai-skills`), incluyendo su recurso
> `dominios-ficticios.md` con vocabulario específico del dominio portuario (IMO de buques,
> código de atraque). Decisión de Debora: fusionar e incorporar a `APB-IA-FRAMEWORK`, sin
> mantener duplicado en el repo de origen.

## 1. Propósito

Generar conjuntos de datos de prueba realistas y anonimizar datos sensibles
para uso en entornos de desarrollo, testing y demos, garantizando
cumplimiento con GDPR y las políticas de datos de APB.

## 2. Trigger

Se necesitan datos de prueba para tests, se replica un entorno productivo a
no productivo, o se preparan demos con datos reales.

**Cuándo NO usar:** datos sin información personal (usar datos sintéticos
simples), entornos de producción (nunca anonimizar en producción), datos ya
anonimizados (verificar que cumplen k-anonimato antes de reprocesar).

## 3. Input / Output

**Input:** esquema de base de datos, muestra de datos reales (opcional),
requisitos de volumen y variedad, clasificación de datos sensibles (PII,
financieros, médicos), regulaciones aplicables (GDPR, LOPD), motor de BD
destino (Oracle / SQL Server / Cosmos DB / PostgreSQL-PostGIS / .NET / TypeScript).

**Output:** dataset sintético o anonimizado, script de
generación/anonimización, documentación de técnicas aplicadas, certificado
de anonimización para auditoría, validación de irreversibilidad.

## 4. Clasificación de Datos

| Categoría | Ejemplos | Tratamiento |
|---|---|---|
| Identificativos | DNI, NIE, pasaporte, nombre completo | Pseudonimización / Hash |
| Sensibles | Salud, religión, orientación sexual, sindicato | Eliminación / Generalización |
| Contacto | Email, teléfono, dirección | Sustitución sintética |
| Financieros | IBAN, tarjetas, nómina | Sustitución sintética + validación |
| Localización | Coordenadas GPS, dirección postal | Generalización espacial |
| Biométricos | Huella, reconocimiento facial | Eliminación |
| Comportamiento | Historial de navegación, compras | Agregación / ruido diferencial |

## 5. Técnicas de Anonimización

**Pseudonimización** (reversible con clave) — hash HMAC-SHA256 con salt por
dataset:

```python
import hashlib, hmac, secrets

salt = secrets.token_hex(32)

def pseudonymize(value: str) -> str:
    return hmac.new(salt.encode(), value.encode(), hashlib.sha256).hexdigest()[:16]
```

**Generalización** — reducir precisión (edad → rango, coordenadas → zona
aproximada):

```python
def generalize_edad(edad: int) -> str:
    if edad < 18: return "0-17"
    elif edad < 30: return "18-29"
    elif edad < 50: return "30-49"
    elif edad < 65: return "50-64"
    else: return "65+"
```

**Sustitución sintética** — generar valores ficticios pero realistas con
Faker/Bogus:

```python
from faker import Faker
fake = Faker('es_ES')
dni_sintetico = fake.ssn()
nombre_sintetico = fake.name()
email_sintetico = fake.email()
```

**Ruido diferencial** — para estadísticas agregadas, preservando privacidad
diferencial (epsilon-DP):

```python
import numpy as np

def add_laplace_noise(value: float, epsilon: float = 1.0, sensitivity: float = 1.0) -> float:
    scale = sensitivity / epsilon
    return value + np.random.laplace(0, scale)
```

**K-anonimato** — asegurar que cada combinación de quasi-identificadores
aparece al menos `k` veces; generalizar los grupos con menos de `k`
registros en lugar de eliminarlos.

## 6. Validación de Anonimización

**Checklist de cumplimiento:**
- [ ] No quedan datos personales identificativos en texto claro.
- [ ] No es posible reidentificación por combinación de campos.
- [ ] K-anonimato ≥ 5 para quasi-identificadores.
- [ ] Distribuciones estadísticas preservadas (± 5%).
- [ ] Integridad referencial mantenida tras la transformación.
- [ ] Datos sintéticos validados contra reglas de negocio.
- [ ] Documentación de transformaciones aplicadas.
- [ ] Aprobación del DPO.

**Prueba de reidentificación** — la tasa de reidentificación contra un
dataset externo debe ser < 1%:

```python
def test_no_reidentification(anonymized_data, external_data):
    matches = sum(
        1 for r in anonymized_data
        if len(find_matches(r, external_data)) == 1
    )
    assert matches / len(anonymized_data) < 0.01
```

## 7. Proceso

1. **Inventario** — identificar tablas, columnas y tipos de datos.
2. **Clasificación** — etiquetar según sensibilidad (sección 4).
3. **Selección de técnica** — anonimización (sección 5) o generación
   sintética con distribución estadística realista, usando los dominios
   ficticios APB de la sección 11.
4. **Implementación** — crear scripts de transformación/generación (ver
   sección 12 para plantillas concretas por motor).
5. **Validación** — verificar irreversibilidad e integridad referencial
   (sección 6).
6. **Documentación** — técnicas, parámetros y responsable, en un informe
   estructurado (alcance, técnicas aplicadas, validación, cumplimiento).
7. **Entrega** — dataset en entorno seguro, con acceso controlado.

## 8. Reglas y Constraints

- Datos de producción NUNCA se usan en desarrollo sin anonimización previa.
- Las técnicas deben ser irreversibles (no usar cifrado reversible).
- Mantener integridad referencial tras la anonimización.
- Documentar quién tiene acceso a los datos de prueba y con qué propósito.
- Revisar la anonimización periódicamente ante nuevas técnicas de
  re-identificación.
- La anonimización es un proceso legalmente sensible: requiere aprobación
  del DPO.
- Seed determinista: misma semilla = mismos datos, para reproducibilidad.
- Nunca combinar un dato ficticio con un dato real (ej: NIF ficticio + nombre real).
- Credenciales: nunca en el fixture — siempre desde variables de entorno o secretos
  gestionados (Key Vault), incluso en staging.

## 9. Procedencia y Licencia

Las secciones 5 y 6 incorporan contenido adaptado de una skill de terceros
de anonimización de datos, licencia MIT. Las secciones 11 y 12 incorporan
contenido adaptado de `apb-test-data-rgpd` (repo `apb-ai-skills`, propiedad APB).

## 10. Dependencias

- `apb-sec-ens-v1.0`

## 11. Tabla de Dominios Ficticios APB — Referencia RGPD

Usar siempre estos valores ficticios al generar datos de prueba. Nunca usar
datos reales de personas, empresas o sistemas de producción APB.

**Identificadores de persona:**

| Tipo | Valores ficticios a usar |
|---|---|
| Email | `test.{rol}@apb-test.local`, `test.{rol}@test-portuario.local` |
| NIF | `00000000T`, `00000001R`, `00000002W`, `00000003A`, `00000004E` |
| NIE | `X0000000T`, `Y0000000Z` |
| Nombre | `Test User 01`, `Test Admin APB`, `Test Operator APB` |
| Teléfono | `+34 900 000 000` a `+34 900 000 099` (rango no asignado) |

**Identificadores de empresa:**

| Tipo | Valores ficticios a usar |
|---|---|
| CIF | `A00000001`, `B00000002`, `B00000003` |
| Razón social | `Test Naviera APB SL`, `Test Operador Portuario SA` |
| IBAN | `ES0000000000000000000000` |

**Identificadores técnicos:**

| Tipo | Valores ficticios a usar |
|---|---|
| IP | `192.0.2.0/24` (TEST-NET-1, RFC 5737), `198.51.100.0/24` (TEST-NET-2) |
| Dominio | `apb-test.local`, `test-portuario.local` |
| UUID | Prefijo fijo `00000000-0000-0000-000X-XXXXXXXXXXXX` para reproducibilidad |

**Identificadores de dominio portuario (APB específico):**

| Tipo | Valores ficticios a usar |
|---|---|
| IMO (buque) | `9999999`, `9999998`, `9999997` (números IMO no asignados) |
| Código atraque | `M-01-TEST`, `M-02-TEST` |
| Matrícula vehículo | `TEST-0001`, `TEST-0002` |

## 12. Fixtures Concretos por Motor

**Oracle SQL:**
```sql
-- fixtures/oracle/001_users.sql
-- DATOS DE PRUEBA APB — NO CONTIENEN DATOS PERSONALES REALES
-- Seed: APB-TEST-2024

WHENEVER SQLERROR EXIT SQL.SQLCODE;

DELETE FROM APB_AUDIT_LOG WHERE USER_ID LIKE '00000000-0000-0000-%';
DELETE FROM APB_USER_ROLES WHERE USER_ID LIKE '00000000-0000-0000-%';
DELETE FROM APB_USERS WHERE ID LIKE '00000000-0000-0000-%';

INSERT INTO APB_USERS (ID, EMAIL, NOMBRE, NIF, ROL, ACTIVO, FECHA_ALTA)
VALUES ('00000000-0000-0000-0001-000000000001', 'test.admin@apb-test.local',
        'Test Administrador APB', '00000000T', 'ADMIN', 1, SYSDATE);

COMMIT;
```

**Fixtures TypeScript (Playwright / Vitest):**
```typescript
// tests/fixtures/apb-users.fixture.ts
export const APB_TEST_USERS: Record<string, User> = {
  admin: {
    id: '00000000-0000-0000-0001-000000000001',
    email: 'test.admin@apb-test.local',
    name: 'Test Administrador APB',
    nif: '00000000T',
    role: UserRole.ADMIN,
    active: true,
  },
};

// Credenciales para tests E2E (staging únicamente) — nunca en el fixture
export const APB_TEST_CREDENTIALS = {
  admin: { username: 'test.admin@apb-test.local', password: process.env.TEST_ADMIN_PASSWORD! },
};
```

**Fixtures Cosmos DB (JSON documentos):**
```json
[
  {
    "id": "00000000-0000-0001-0001-000000000001",
    "buqueId": "TEST-BUQUE-001",
    "posicion": { "lat": 41.35, "lon": 2.15 },
    "timestamp": "2026-06-01T08:00:00Z",
    "_partitionKey": "TEST-BUQUE-001"
  }
]
```

**Fixtures PostgreSQL/PostGIS (geometrías ficticias, sin referencia a instalaciones reales):**
```sql
-- fixtures/postgis/seed-zonas-test.sql
INSERT INTO apb_zonas_portuarias (id, nombre, tipo, geom) VALUES
('00000000-0000-0002-0001-000000000001', 'Zona Fondeo Test Norte', 'FONDEO',
 ST_GeomFromText('POLYGON((2.10 41.38, 2.15 41.38, 2.15 41.40, 2.10 41.40, 2.10 41.38))', 4326));
```

**AutoFixture factories (.NET):**
```csharp
// tests/fixtures/UserFixtureFactory.cs
public static class UserFixtureFactory
{
    private static readonly Fixture _fixture = new();

    static UserFixtureFactory()
    {
        _fixture.Customize<User>(c => c
            .With(u => u.Email, () => $"test.user.{Guid.NewGuid():N}@apb-test.local")
            .With(u => u.Nif, () => GenerateFakeNif())
            .Without(u => u.PasswordHash));
    }

    public static User CreateTestUser(UserRole role = UserRole.Operator)
        => _fixture.Build<User>().With(u => u.Role, role).With(u => u.Active, true).Create();

    private static string GenerateFakeNif()
    {
        var letters = "TRWAGMYFPDXBNJZSQVHLCKE";
        var number = Random.Shared.Next(0, 100);
        return $"{number:D8}{letters[number % 23]}";
    }
}
```

## 13. Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.1.0 | 2026-06-22 | QA / Ciberseguridad APB | (histórico previo) |
| 1.2.0 | 2026-06-24 | Arquitectura APB | Fusión con `apb-test-data-rgpd` (apb-ai-skills): tabla de dominios ficticios APB (incl. vocabulario portuario IMO/atraque), fixtures concretos Oracle/TypeScript/Cosmos/PostGIS/.NET |

> **Generado por IA:** Claude (Anthropic), Sesión QA del plan de remediación APB-IA-FRAMEWORK.
> **Validado por humano:** _pendiente — completar nombre/rol del validador antes de pasar a `candidate`._


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Codigo generado** - primera linea del bloque: `// [IA-GEN] Generado por APB AI Framework (apb-qa-anonymize-v1.0) - pendiente revision humana`
- **Commit** - prefijo `[ai-gen]` en el mensaje + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`
- **PR asociado** - label `ai-generated` en GitHub + footer en descripcion del PR
