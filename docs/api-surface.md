# REST API Surface & Endpoint Specification

## Authentication (`/auth`)
- `POST /auth/register` — Register new organization admin and workspace
- `POST /auth/login` — Authenticate and receive JWT access token
- `GET  /auth/me` — Retrieve current authenticated user profile

## Organizations & Teams (`/organizations`, `/teams`)
- `GET  /organizations/me` — Fetch tenant metadata
- `POST /teams` — Create functional team
- `GET  /teams` — List tenant teams
- `POST /teams/{id}/members` — Assign user to team

## Tickets (`/tickets`)
- `POST   /tickets` — Create support ticket
- `GET    /tickets` — Search & paginate tickets (filter by status, priority, assignee)
- `GET    /tickets/{id}` — Fetch ticket details
- `PATCH  /tickets/{id}/status` — Transition ticket state
- `PATCH  /tickets/{id}/assign` — Assign or reassign ticket

## Comments & Auditing (`/tickets/{id}/comments`, `/audit`)
- `POST /tickets/{id}/comments` — Add public comment or internal note
- `GET  /tickets/{id}/comments` — List ticket comment thread
- `GET  /tickets/{id}/audit-logs` — Fetch immutable history log

## Real-Time (`/ws`)
- `WS /ws/tickets/{id}` — WebSocket stream for live updates on ticket events