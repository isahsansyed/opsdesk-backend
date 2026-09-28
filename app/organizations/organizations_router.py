# app/organizations/organizations_router.py

import uuid

from fastapi import APIRouter, Depends, status

from app.auth.auth_dependencies import get_current_user
from app.core.constants import UserRole
from app.core.response import ApiResponse
from app.organizations.organizations_controller import OrganizationController
from app.organizations.organizations_dependencies import (
    RequireRole,
    get_current_org_member,
    get_organization_controller,
)
from app.organizations.organizations_schemas import (
    MemberAdd,
    MemberResponse,
    OrganizationCreate,
    OrganizationResponse,
)
from app.users.users_models import User

router = APIRouter(prefix="/organizations", tags=["Organizations"])


@router.post(
    "",
    response_model=ApiResponse[OrganizationResponse],
    status_code=status.HTTP_201_CREATED,
)
async def create_organization(
    payload: OrganizationCreate,
    current_user: User = Depends(get_current_user),
    controller: OrganizationController = Depends(get_organization_controller),
) -> ApiResponse[OrganizationResponse]:
    """Any authenticated user can create an organization; they become ADMIN."""
    return await controller.create(payload, current_user)


@router.get(
    "/{org_id}",
    response_model=ApiResponse[OrganizationResponse],
    dependencies=[Depends(get_current_org_member)],
)
async def get_organization(
    org_id: uuid.UUID,
    controller: OrganizationController = Depends(get_organization_controller),
) -> ApiResponse[OrganizationResponse]:
    """Any active member of the org can read it."""
    return await controller.get(org_id)


@router.post(
    "/{org_id}/members",
    response_model=ApiResponse[MemberResponse],
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(RequireRole(UserRole.ADMIN, UserRole.MANAGER))],
)
async def add_member(
    org_id: uuid.UUID,
    payload: MemberAdd,
    controller: OrganizationController = Depends(get_organization_controller),
) -> ApiResponse[MemberResponse]:
    """Only ADMIN or MANAGER can add members."""
    return await controller.add_member(org_id, payload)


@router.get(
    "/{org_id}/members",
    response_model=ApiResponse[list[MemberResponse]],
    dependencies=[Depends(get_current_org_member)],
)
async def list_members(
    org_id: uuid.UUID,
    controller: OrganizationController = Depends(get_organization_controller),
) -> ApiResponse[list[MemberResponse]]:
    """Any active member can list members."""
    return await controller.list_members(org_id)