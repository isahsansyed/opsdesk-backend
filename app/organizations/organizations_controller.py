# app/organizations/organizations_controller.py 

import uuid

from app.core.response import ApiResponse
from app.organizations.organizations_schemas import (
    MemberAdd,
    MemberResponse,
    OrganizationCreate,
    OrganizationResponse,
)
from app.organizations.organizations_service import OrganizationService
from app.users.users_models import User


class OrganizationController:
    def __init__(self, service: OrganizationService) -> None:
        self.service = service

    async def create(
        self, payload: OrganizationCreate, current_user: User
    ) -> ApiResponse[OrganizationResponse]:
        org = await self.service.create(payload=payload, creator_id=current_user.id)
        return ApiResponse.ok(OrganizationResponse.model_validate(org))

    async def get(self, org_id: uuid.UUID) -> ApiResponse[OrganizationResponse]:
        org = await self.service.get(org_id)
        return ApiResponse.ok(OrganizationResponse.model_validate(org))

    async def add_member(
        self, org_id: uuid.UUID, payload: MemberAdd
    ) -> ApiResponse[MemberResponse]:
        member = await self.service.add_member(org_id=org_id, payload=payload)
        return ApiResponse.ok(MemberResponse.model_validate(member))

    async def list_members(
        self, org_id: uuid.UUID
    ) -> ApiResponse[list[MemberResponse]]:
        members = await self.service.list_members(org_id)
        return ApiResponse.ok([MemberResponse.model_validate(m) for m in members])