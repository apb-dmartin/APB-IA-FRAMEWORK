---
id: "third-apollographql-api-design-v1.0"
name: "GraphQL & API Design (Apollo)"
description: "Diseña, valida y optimiza APIs GraphQL y REST siguiendo estándares de Apollo, OpenAPI y gRPC: schema design, caching, paginación, federación de schemas."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "development"
created_date: "2026-06-22"
review_date: "2026-06-22"
autonomy_level: 1
source_repo: "https://github.com/apollographql/skills"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
---

# SKILL_DEV_API_STANDARD — API Design & Standards

## 1. Propósito y Alcance

Esta skill unifica el conocimiento de Apollo GraphQL Skills en un framework
completo de diseño de APIs, extendiendo a REST y gRPC para cobertura multi-protocolo.

**Protocolos cubiertos:**
- **GraphQL**: Queries, mutations, subscriptions, federation, caching
- **REST**: OpenAPI/Swagger, HATEOAS, versioning, hypermedia
- **gRPC**: Protobuf, streaming, service definitions, bi-directional
- **WebSocket**: Real-time subscriptions, Socket.io, GraphQL subscriptions

**Casos de uso:**
1. Diseño de schema GraphQL para nuevos servicios
2. Optimización de queries y resolvers (N+1, caching, batching)
3. Implementación de Apollo Federation para microservicios
4. Diseño de APIs REST con OpenAPI 3.0
5. Definición de contratos gRPC entre servicios internos
6. Estándares de error handling y pagination cross-protocol

## 2. GraphQL Schema Design

### 2.1 Principios de Diseño

**Types Hierarchy:**
```graphql
# ✅ Schema bien diseñado: tipos claros, relaciones explícitas
type Query {
  # Single resource by ID (nullable)
  user(id: ID!): User

  # List with pagination (non-nullable list, nullable items)
  users(
    first: Int = 20
    after: String
    filter: UserFilter
    sort: UserSort = CREATED_AT_DESC
  ): UserConnection!

  # Search (always returns connection, even if empty)
  searchUsers(query: String!): UserConnection!
}

type User implements Node {
  id: ID!                    # Global ID (Relay spec)
  email: String!             # Non-nullable for required fields
  name: String              # Nullable for optional fields
  profile: UserProfile      # Nullable for optional relations
  orders(
    first: Int = 10
    after: String
    status: OrderStatus
  ): OrderConnection!       # Non-nullable connection
  createdAt: DateTime!     # Scalar custom para fechas
  updatedAt: DateTime!
}

type UserProfile {
  avatar: URL               # Scalar custom para URLs
  bio: String
  preferences: UserPreferences
}

# ✅ Enums para valores fijos
type UserPreferences {
  theme: Theme!            # LIGHT | DARK | SYSTEM
  language: Language!      # ES | EN | FR | DE
  notifications: NotificationSettings!
}

enum Theme {
  LIGHT
  DARK
  SYSTEM
}

# ✅ Input types para mutations (separar de types de lectura)
input CreateUserInput {
  email: String!
  name: String
  password: String!
  preferences: UserPreferencesInput
}

input UserPreferencesInput {
  theme: Theme
  language: Language
}

# ✅ Payload types para mutations (permitir errores y datos)
type CreateUserPayload {
  user: User
  errors: [UserError!]     # Null si éxito, datos si error
}

type UserError {
  message: String!
  path: [String!]          # Campos afectados
  code: ErrorCode!         # Código machine-readable
}

enum ErrorCode {
  INVALID_INPUT
  DUPLICATE_EMAIL
  WEAK_PASSWORD
  UNAUTHORIZED
}
```

### 2.2 Pagination Patterns

**Cursor-based (Relay spec - RECOMENDADO):**
```graphql
type UserConnection {
  edges: [UserEdge!]!      # Non-nullable list, non-nullable items
  pageInfo: PageInfo!      # Non-nullable metadata
  totalCount: Int           # Nullable (puede ser costoso de calcular)
}

type UserEdge {
  node: User!              # Non-nullable entity
  cursor: String!          # Non-nullable cursor
}

type PageInfo {
  hasNextPage: Boolean!    # Si hay más páginas
  hasPreviousPage: Boolean! # Si hay páginas previas
  startCursor: String       # Cursor de primera página (nullable para empty)
  endCursor: String         # Cursor de última página
}

# Query con cursor
query GetUsers($first: Int = 20, $after: String) {
  users(first: $first, after: $after) {
    edges {
      node {
        id
        name
        email
      }
      cursor
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

**Offset-based (legacy, no recomendado para grandes datasets):**
```graphql
type Query {
  users(offset: Int = 0, limit: Int = 20): [User!]!
}
# Problema: Inconsistente con deletes, costoso en OFFSET grandes
```

### 2.3 Error Handling

**GraphQL Error Spec (2026):**
```graphql
# ✅ Errores como datos (no excepciones)
type Mutation {
  createUser(input: CreateUserInput!): CreateUserPayload!
}

type CreateUserPayload {
  user: User              # Null si hay errores
  errors: [UserError!]     # Null si éxito
}

# ✅ UserError con código machine-readable
type UserError {
  message: String!         # Human-readable
  path: [String!]          # Campos afectados ["input", "email"]
  code: ErrorCode!         # Machine-readable para UI handling
  extensions: JSON          # Datos adicionales (sugerencias, etc.)
}

# ✅ Top-level errors solo para errores de sistema
# (network, auth, internal server error)
# Business logic errors como datos en payload
```

### 2.4 Caching Strategies

**HTTP Caching (GET queries):**
```graphql
# ✅ Queries idempotentes con GET + cache headers
# Apollo Client automatic caching
query GetUser($id: ID!) {
  user(id: $id) {
    id
    name
    email
  }
}
# Cache key: { user(id: "123") } → TTL: 5 min
```

**Entity Caching (Normalized):**
```javascript
// Apollo Client cache config
const cache = new InMemoryCache({
  typePolicies: {
    Query: {
      fields: {
        users: relayStylePagination(), // Pagination helper
      },
    },
    User: {
      keyFields: ['id'], // Cache by ID
      fields: {
        orders: {
          merge(existing, incoming) {
            // Custom merge for lists
            return incoming;
          },
        },
      },
    },
  },
});
```

**Field-level Caching (Server-side):**
```graphql
# @cacheControl directive (Apollo Server)
type User @cacheControl(maxAge: 300) {  # 5 min cache
  id: ID!
  name: String!
  email: String! @cacheControl(maxAge: 0)  # No cache (sensitive)
  orders: [Order!]! @cacheControl(maxAge: 60)  # 1 min cache
}
```

## 3. Apollo Federation

### 3.1 Schema Federation

```graphql
# === User Service ===
type User @key(fields: "id") {
  id: ID!
  email: String!
  name: String
}

type Query {
  user(id: ID!): User
  me: User
}

# === Order Service ===
type Order @key(fields: "id") {
  id: ID!
  total: Float!
  user: User! @provides(fields: "id")  # Reference to User
}

type User @key(fields: "id") @extends {
  id: ID! @external
  orders: [Order!]!  # Extends User with orders field
}

type Query {
  order(id: ID!): Order
  userOrders(userId: ID!): [Order!]!
}

# === Gateway ===
# Composes schemas de múltiples servicios
# Router (Apollo Router) en lugar de Gateway (deprecated)
```

### 3.2 Entity Resolvers

```typescript
// User Service: Resuelve User por ID
const resolvers = {
  Query: {
    user: (_, { id }, { dataSources }) => dataSources.userAPI.getUser(id),
    me: (_, __, { user }) => user, // From auth context
  },
  User: {
    // Reference resolver para federation
    __resolveReference(user, { dataSources }) {
      return dataSources.userAPI.getUser(user.id);
    },
  },
};

// Order Service: Resuelve User reference
const resolvers = {
  Order: {
    user: (order, _, { dataSources }) => 
      dataSources.userAPI.getUser(order.userId), // Batch loading
  },
  User: {
    // Extends User with orders
    orders: (user, _, { dataSources }) => 
      dataSources.orderAPI.getOrdersByUser(user.id),
  },
};
```

### 3.3 Batching y DataLoaders

```typescript
// DataLoader para N+1 prevention
import DataLoader from 'dataloader';

const userLoader = new DataLoader(async (userIds: string[]) => {
  // Batch load: 1 query para N IDs
  const users = await db.users.findMany({
    where: { id: { in: userIds } },
  });
  // Return in same order as keys
  return userIds.map(id => users.find(u => u.id === id));
});

// Resolver usa DataLoader
const resolvers = {
  Order: {
    user: (order, _, { userLoader }) => userLoader.load(order.userId),
  },
};
```

## 4. REST API Standards (OpenAPI 3.0)

### 4.1 Resource Naming

```yaml
# ✅ RESTful resource naming
paths:
  /users:                    # Collection (plural nouns)
    get:                     # List (paginated)
      parameters:
        - name: page
          in: query
          schema: { type: integer, default: 1 }
        - name: per_page
          in: query
          schema: { type: integer, default: 20, maximum: 100 }
    post:                    # Create
      requestBody:
        content:
          application/json:
            schema: { $ref: '#/components/schemas/UserCreate' }
  /users/{id}:               # Single resource
    get:                     # Read
      parameters:
        - name: id
          in: path
          required: true
          schema: { type: string, format: uuid }
    patch:                   # Partial update (preferido sobre PUT)
      parameters:
        - name: id
          in: path
          required: true
          schema: { type: string, format: uuid }
      requestBody:
        content:
          application/json:
            schema: { $ref: '#/components/schemas/UserUpdate' }
    delete:                  # Delete
      parameters:
        - name: id
          in: path
          required: true
          schema: { type: string, format: uuid }
  /users/{id}/orders:        # Sub-resource (nested)
    get:
      parameters:
        - name: id
          in: path
          required: true
          schema: { type: string, format: uuid }
        - name: status
          in: query
          schema: { type: string, enum: [PENDING, SHIPPED, DELIVERED] }
```

### 4.2 HTTP Status Codes

| Code | Uso | Body |
|------|-----|------|
| 200 OK | GET, PUT, PATCH success | Resource updated |
| 201 Created | POST success | Resource created |
| 204 No Content | DELETE success, empty response | Empty |
| 400 Bad Request | Validation error | Error details |
| 401 Unauthorized | Auth missing/invalid | Error message |
| 403 Forbidden | Auth OK, no permission | Error message |
| 404 Not Found | Resource doesn't exist | Error message |
| 409 Conflict | Resource exists (duplicate) | Error details |
| 422 Unprocessable | Business logic violation | Error details |
| 429 Too Many Requests | Rate limit exceeded | Retry-After header |
| 500 Internal Error | Server error | Generic message (no details) |

### 4.3 Error Response Format (RFC 7807 - Problem Details)

```json
{
  "type": "https://api.example.com/errors/invalid-input",
  "title": "Invalid input",
  "status": 400,
  "detail": "The request body contains invalid fields.",
  "instance": "/users/123",
  "errors": [
    {
      "field": "email",
      "message": "Invalid email format",
      "code": "INVALID_FORMAT"
    },
    {
      "field": "password",
      "message": "Must be at least 8 characters",
      "code": "MIN_LENGTH",
      "params": { "min": 8 }
    }
  ]
}
```

### 4.4 Pagination (REST)

**Offset-based (legacy):**
```json
{
  "data": [...],
  "pagination": {
    "page": 2,
    "per_page": 20,
    "total": 150,
    "total_pages": 8
  }
}
```

**Cursor-based (recommended):**
```json
{
  "data": [...],
  "pagination": {
    "has_more": true,
    "next_cursor": "eyJpZCI6MTIzLCJjcmVhdGVkX2F0IjoiMjAyNC0wMS0wMVQwMDowMDowMCJ9",
    "prev_cursor": "eyJpZCI6NDU2LCJjcmVhdGVkX2F0IjoiMjAyMy0xMi0wMVQwMDowMDowMCJ9"
  }
}
```

## 5. gRPC Standards

### 5.1 Service Definition

```protobuf
syntax = "proto3";
package users.v1;

import "google/protobuf/timestamp.proto";
import "google/protobuf/field_mask.proto";

// ✅ Versioned package para backward compatibility
option go_package = "github.com/example/users/v1";

// Service definition
service UserService {
  // CRUD operations
  rpc GetUser(GetUserRequest) returns (User);
  rpc ListUsers(ListUsersRequest) returns (ListUsersResponse);
  rpc CreateUser(CreateUserRequest) returns (User);
  rpc UpdateUser(UpdateUserRequest) returns (User);
  rpc DeleteUser(DeleteUserRequest) returns (google.protobuf.Empty);

  // Streaming (for large datasets or real-time)
  rpc StreamUsers(StreamUsersRequest) returns (stream User);
  rpc BatchCreateUsers(stream CreateUserRequest) returns (stream User);
  rpc Chat(stream ChatMessage) returns (stream ChatMessage); // Bi-directional
}

// Messages
message User {
  string id = 1;
  string email = 2;
  string name = 3;
  google.protobuf.Timestamp created_at = 4;
  google.protobuf.Timestamp updated_at = 5;
}

message GetUserRequest {
  string id = 1;
}

message ListUsersRequest {
  int32 page_size = 1;  // Default: 20, Max: 100
  string page_token = 2; // Cursor-based pagination
  string filter = 3;     // CEL expression: "created_at > '2024-01-01'"
  string order_by = 4;   // "created_at desc"
}

message ListUsersResponse {
  repeated User users = 1;
  string next_page_token = 2;
  int32 total_size = 3;  // Optional, may be expensive
}

message CreateUserRequest {
  string email = 1;
  string name = 2;
  string password = 3;
}

message UpdateUserRequest {
  User user = 1;
  google.protobuf.FieldMask update_mask = 2; // Partial update
}

message DeleteUserRequest {
  string id = 1;
  bool force = 2; // Force delete even with dependencies
}
```

### 5.2 Error Handling (gRPC Status Codes)

| gRPC Code | HTTP Equivalent | Uso |
|-----------|----------------|-----|
| OK | 200 | Success |
| CANCELLED | 499 | Client cancelled |
| UNKNOWN | 500 | Unknown server error |
| INVALID_ARGUMENT | 400 | Bad request (validation) |
| DEADLINE_EXCEEDED | 504 | Timeout |
| NOT_FOUND | 404 | Resource not found |
| ALREADY_EXISTS | 409 | Duplicate |
| PERMISSION_DENIED | 403 | No permission |
| RESOURCE_EXHAUSTED | 429 | Rate limit / quota |
| FAILED_PRECONDITION | 412 | State conflict |
| ABORTED | 409 | Conflict / retry |
| OUT_OF_RANGE | 400 | Invalid pagination |
| UNIMPLEMENTED | 501 | Not implemented |
| INTERNAL | 500 | Internal error |
| UNAVAILABLE | 503 | Service unavailable |
| DATA_LOSS | 500 | Data corruption |
| UNAUTHENTICATED | 401 | Auth missing/invalid |

## 6. API Versioning Strategies

### 6.1 URL Versioning (Recommended for REST)
```
/api/v1/users
/api/v2/users
```

### 6.2 Header Versioning
```
Accept: application/vnd.example.v1+json
Accept-Version: v1
```

### 6.3 GraphQL (No Versioning)
- Schema evolution: deprecate fields, add new fields
- `@deprecated(reason: "Use newField instead")`
- Clients request only fields que necesitan

### 6.4 gRPC (Package Versioning)
```protobuf
package users.v1;  // v2 en package separado
```

## 7. Checklist de API Review

### GraphQL
- [ ] Schema follows Relay spec for pagination (Connection, Edge, PageInfo)
- [ ] Non-nullable fields para datos requeridos, nullable para opcionales
- [ ] Input types separados de types de lectura
- [ ] Error handling como datos (payload), no excepciones
- [ ] Custom scalars para tipos específicos (DateTime, Email, URL, Money)
- [ ] Enums para valores fijos (no strings)
- [ ] Descriptions en todos los types, fields, y arguments
- [ ] N+1 prevention con DataLoader
- [ ] Cache control directives para field-level caching
- [ ] Federation keys definidas para cross-service references

### REST
- [ ] Resource naming plural nouns (/users, not /user)
- [ ] HTTP verbs correctos (GET, POST, PUT, PATCH, DELETE)
- [ ] Status codes apropiados (200, 201, 204, 400, 401, 403, 404, 409, 422, 429, 500)
- [ ] Error format consistente (RFC 7807 Problem Details)
- [ ] Pagination cursor-based para grandes datasets
- [ ] Filtering, sorting, y field selection (sparse fieldsets)
- [ ] Rate limiting headers (X-RateLimit-Remaining, Retry-After)
- [ ] Content negotiation (Accept, Content-Type)
- [ ] HATEOAS links (opcional, para hypermedia)
- [ ] OpenAPI 3.0 spec completa y actualizada

### gRPC
- [ ] Proto3 syntax, versioned packages
- [ ] Well-known types (Timestamp, Duration, Empty, FieldMask)
- [ ] Streaming para large datasets o real-time
- [ ] Error codes gRPC apropiados
- [ ] Deadlines y timeouts configurados
- [ ] Metadata para auth, tracing, request ID
- [ ] Backward compatibility: no renumber fields, only add
- [ ] JSON transcoding para REST gateway (opcional)

## 8. Anti-patrones de API Design (Qué NO hacer)

- **RPC over HTTP**: POST /getUser, POST /deleteUser (usar GET/DELETE)
- **Deep nesting**: /users/123/orders/456/items/789 (máximo 2 niveles)
- **Inconsistent naming**: /users y /Orders (case inconsistency)
- **No pagination**: Retornar arrays sin limit (DoS risk)
- **No filtering**: Cliente filtra en memoria (ineficiente)
- **No error standard**: Cada endpoint retorna errores diferentes
- **No versioning**: Breaking changes sin migración path
- **Exposing internals**: IDs de DB, estructuras internas
- **No rate limiting**: APIs públicas sin protección
- **Over-fetching**: GraphQL queries sin depth limiting
- **N+1 en resolvers**: Sin DataLoader o batching
- **No caching**: Cada request hit a DB (ineficiente)

## 9. Integración con otras Skills APB

- **SKILL_DEV_CODE_BASE**: DDD (entities, value objects) como base de schema design
- **SKILL_DEV_MICRO_BASE**: Microservices communication (REST, gRPC, events)
- **SKILL_DEV_SQL_FIX**: Query optimization para resolvers y repositories
- **SKILL_DEV_REVIEW_ADVANCED**: Contracts-reviewer para API breaking changes
- **SKILL_ARCH_EVENT_DRIVEN**: Event-driven APIs (webhooks, subscriptions)
- **SKILL_PLAT_CICD**: API testing en pipeline (contract tests, Pact)
- **SKILL_OPS_OBSERVABILITY**: API metrics (latency, error rate, throughput)

## 10. Referencias

- [apollographql/skills - Apollo Client](https://github.com/apollographql/skills)
- [Apollo GraphQL Best Practices](https://www.apollographql.com/docs/)
- [GraphQL Spec](https://spec.graphql.org/)
- [Relay Cursor Connections Spec](https://relay.dev/graphql/connections.htm)
- [OpenAPI 3.0 Specification](https://swagger.io/specification/)
- [RFC 7807 - Problem Details](https://tools.ietf.org/html/rfc7807)
- [Google API Design Guide](https://cloud.google.com/apis/design)
- [Microsoft REST API Guidelines](https://github.com/microsoft/api-guidelines)
- [gRPC Best Practices](https://grpc.io/docs/guides/)
- [API Versioning Strategies](https://www.baeldung.com/rest-versioning)
