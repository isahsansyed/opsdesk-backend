# REST API Surface & Endpoint Specification

## Authentication (`/auth`)
- `POST /auth/register` — Register new organization admin and workspace
- `POST /auth/login` — Authenticate and receive JWT access token
- `GET  /auth/me` — Retrieve current authenticated user profile

## Response Envelope

Every endpoint returns this shape, success or failure:

{
  "success": bool,
  "data": object | null,
  "error": {
    "code": string,
    "message": string,
    "details": array | null
  } | null,
  "meta": object | null
}

### Error codes (stable, for client branching)

- VALIDATION_ERROR — 422
- UNAUTHENTICATED — 401
- INVALID_CREDENTIALS — 401
- INACTIVE_USER — 403
- FORBIDDEN — 403
- NOT_FOUND — 404
- USER_NOT_FOUND — 404
- CONFLICT — 409
- USER_ALREADY_EXISTS — 409
- BAD_REQUEST — 400
- HTTP_ERROR — any (FastAPI/Starlette built-ins)
- INTERNAL_ERROR — 500

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