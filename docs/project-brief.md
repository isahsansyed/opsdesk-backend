# Project Brief: OpsDesk Backend

## Project Name
**OpsDesk** — Real-Time Support & Incident Management Platform Backend

## Problem
Modern enterprises and engineering teams need a reliable, real-time platform to receive, prioritize, assign, and resolve customer support requests and critical technical incidents. Most standard CRUD ticketing applications lack real-time synchronization, concurrency safeguards, multi-tenant data isolation, and detailed operational audit trails.

## Target Users
- **Organization Admins:** Manage users, roles, and company-wide settings.
- **Team Managers:** Oversee support teams, assign tickets, and track status.
- **Support Agents:** Resolve tickets, add internal notes, and update statuses.
- **Customers:** Submit support requests, track resolution progress, and comment.

## Main Objective
Build a high-throughput, multi-tenant, production-grade REST and WebSocket backend using FastAPI, SQLAlchemy (Async), PostgreSQL, and Redis that mimics core operational capabilities of Zendesk, PagerDuty, and Slack.

## Core Features
1. **Multi-Tenancy & RBAC:** Strict tenant data isolation with Role-Based Access Control.
2. **Ticket Lifecycle Management:** State-machine enforced transitions with automated state rules.
3. **Real-Time Collaboration:** WebSocket broadcasting via Redis Pub/Sub for live concurrent viewing and updates.
4. **Asynchronous Processing:** Background email notifications and job worker queues.
5. **Audit Trail:** Immutable logging of all state transitions and system actions for compliance.

## Non-Goals (Out of Scope for MVP)
- Frontend client user interfaces (handled via OpenAPI / Swagger / WebSocket clients).
- Payment processing or subscription billing integrations.
- Native mobile client applications.

## Technology Stack
- **Framework:** FastAPI (Python 3.12+)
- **Database:** PostgreSQL (Relational Engine) + Async SQLAlchemy 2.0 ORM
- **Database Migrations:** Alembic
- **Caching & Real-Time Message Broker:** Redis (Rate Limiting, Caching, Pub/Sub)
- **Background Tasks:** ARQ / Celery
- **Containerization & Orchestration:** Docker & Docker Compose
- **Testing Suite:** `pytest` & `httpx` (Async API Integration Tests)

## Success Criteria
- Zero cross-tenant data leaks (100% data isolation).
- Sub-50ms API response latency for cached ticket endpoints.
- Real-time event propagation to connected WebSocket clients in < 100ms.
- Full test coverage over core state machine transitions and authorization logic.