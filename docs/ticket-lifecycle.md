# Ticket State Machine & Lifecycle Specification

## Ticket States
- `OPEN`: Ticket created, awaiting triage or initial agent response.
- `IN_PROGRESS`: Agent actively working on resolution.
- `PENDING_CUSTOMER`: Waiting for customer input or verification.
- `RESOLVED`: Resolution provided by agent; awaiting confirmation or closure.
- `CLOSED`: Final state. Ticket is archived and immutable.
- `CANCELLED`: Ticket closed without action (e.g., duplicate or spam).

## State Transition Diagram

[OPEN] ───────────► [IN_PROGRESS] ───────────► [RESOLVED] ───────────► [CLOSED]
│                      │                        ▲
│                      ├────────────────────────┘
▼                      ▼
[CANCELLED]      [PENDING_CUSTOMER]


## Allowed Transitions Rules
1. `OPEN` $\rightarrow$ `IN_PROGRESS`, `PENDING_CUSTOMER`, `CANCELLED`
2. `IN_PROGRESS` $\rightarrow$ `PENDING_CUSTOMER`, `RESOLVED`, `OPEN`
3. `PENDING_CUSTOMER` $\rightarrow$ `IN_PROGRESS` (Auto-triggered when customer replies), `RESOLVED`
4. `RESOLVED` $\rightarrow$ `CLOSED`, `IN_PROGRESS` (Reopened if customer replies within 48h)
5. `CLOSED` $\rightarrow$ *None (Immutable terminal state)*