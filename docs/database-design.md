# Database Design & Entity Relationships

## Core Tables

1. **`organizations`**: Multi-tenant workspace entities.
2. **`users`**: Platform users scoped to organizations.
3. **`teams`**: Functional sub-groups within an organization.
4. **`team_members`**: Junction table mapping users to teams.
5. **`tickets`**: Core support incidents owned by an organization.
6. **`comments`**: Communication threads on tickets.
7. **`audit_logs`**: Immutable event history tracking all system mutations.

## Relational Hierarchy

```
[organizations] ───< [teams] ───< [team_members] >─── [users]
       │                                                  │
       └─────────────────< [tickets] >────────────────────┘
                             │
              ┌──────────────┴──────────────┐
              ▼                             ▼
         [comments]                    [audit_logs]
```