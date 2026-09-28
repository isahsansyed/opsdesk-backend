# app/organizations/organizations_dependencies.py

import uuid

from fastapi import Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.auth_dependencies import get_current_user
from app.core.constants import UserRole
from app.core.exceptions import PermissionDeniedError
from app.db.session import get_db
from app.organizations.organizations_controller import OrganizationController
from app.organizations.organizations_exceptions import OrganizationMemberNotFoundError
from app.organizations.organizations_models import OrganizationMember
from app.organizations.organizations_repository import OrganizationRepository
from app.organizations.organizations_service import OrganizationService
from app.users.users_models import User


# ---------- Layer providers ----------

def get_organization_repository(
    db: AsyncSession = Depends(get_db),
) -> OrganizationRepository:
    return OrganizationRepository(db)


def get_organization_service(
    repo: OrganizationRepository = Depends(get_organization_repository),
) -> OrganizationService:
    return OrganizationService(repo)


def get_organization_controller(
    service: OrganizationService = Depends(get_organization_service),
) -> OrganizationController:
    return OrganizationController(service)


# ---------- Membership + RBAC ----------

async def get_current_org_member(
    org_id: uuid.UUID = Path(...),
    current_user: User = Depends(get_current_user),
    repo: OrganizationRepository = Depends(get_organization_repository),
) -> OrganizationMember:
    """Return the OrganizationMember row for the current user in this org.

    Raises 404 if the user is not a member. Deliberately does NOT distinguish
    'org does not exist' from 'user not a member' — that prevents leaking
    which orgs exist to non-members.
    """
    member = await repo.get_member(org_id=org_id, user_id=current_user.id)
    if member is None:
        raise OrganizationMemberNotFoundError()
    return member


class RequireRole:
    """Dependency that asserts the current member's role is in an allowed set."""

    def __init__(self, *allowed_roles: UserRole) -> None:
        self.allowed_roles = set(allowed_roles)

    async def __call__(
        self,
        member: OrganizationMember = Depends(get_current_org_member),
    ) -> OrganizationMember:
        if member.role not in self.allowed_roles:
            raise PermissionDeniedError(
                message=(
                    f"Role '{member.role}' does not have permission "
                    f"for this action."
                )
            )
        return member