# OpsDesk Architecture Specification

## 1. Request Flow & Layered Architecture

```
Client (HTTP / WebSocket)
        │
        ▼
FastAPI Routers (Request Parsing & Rate Limiting)
        │
        ▼
Services / Business Logic (Validation, State Machine, Auditing)
        │
        ▼
Repositories / Data Access (Async SQLAlchemy Queries)
        │
        ▼
PostgreSQL Database
```

## 2. Infrastructure Topology

```
        +-------------------+
        |    FastAPI App    |
        +---------+---------+
                  |
     +------------+------------+
     |            |            |
     v            v            v
+----------+  +--------+  +------------+
|PostgreSQL|  | Redis  |  | WebSockets |
| (Data)   |  |(Cache/ |  | (Real-time |
|          |  | PubSub)|  | Broadcast) |
+----------+  +---+----+  +------------+
                  |
                  v
           +-------------+
           | Background  |
           |   Worker    |
           +------+------+
                  |
                  v
           +-------------+
           |Email Provider|
           +-------------+
```

## 3. Key Design Decisions

1. **Modular Monolith:** Domain logic is segregated into cohesive modules
   (`auth`, `tickets`, `organizations`), making future service splits trivial
   while avoiding microservice complexity now.
2. **Repository Pattern:** Separates database access code from core domain
   business rules, making code easier to test using mocks or isolated test
   databases.
3. **Async IO Architecture:** Full async flow from FastAPI controller down to
   `asyncpg` PostgreSQL driver and Redis connection pool ensures maximum
   dynamic concurrency.