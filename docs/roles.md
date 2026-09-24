# Role-Based Access Control (RBAC) Specification

## Roles
1. `SUPER_ADMIN`: System-wide owner managing global organizations.
2. `ORG_ADMIN`: Organization workspace administrator.
3. `MANAGER`: Team lead managing assigned agents and ticket distributions.
4. `AGENT`: Support representative resolving assigned issues.
5. `CUSTOMER`: External client reporting issues and requesting support.

## Permissions Matrix

| Action | Admin | Manager | Agent | Customer |
| :--- | :---: | :---: | :---: | :---: |
| **Create Ticket** | Yes | Yes | Yes | Yes |
| **View Own Tickets** | Yes | Yes | Yes | Yes |
| **View Org Tickets** | Yes | Yes | Yes | No |
| **Assign Ticket** | Yes | Yes | No | No |
| **Update Ticket Priority**| Yes | Yes | Yes | Yes (Own) |
| **Transition Ticket Status**| Yes | Yes | Yes | No |
| **Add Public Comment** | Yes | Yes | Yes | Yes |
| **Add Internal Note** | Yes | Yes | Yes | No |
| **Delete Ticket** | Yes | No | No | No |
| **View Audit Logs** | Yes | Yes | No | No |
| **Manage Users/Teams** | Yes | No | No | No |