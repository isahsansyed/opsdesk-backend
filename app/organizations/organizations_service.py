# app/organizations/organizations_service.py

import re
import uuid

from app.core.constants import UserRole
from app.organizations.organizations_exceptions import (
    OrganizationMemberExistsError,
    OrganizationNotFoundError,
    OrganizationSlugExistsError,
)
from app.organizations.organizations_models import Organization, OrganizationMember
from app.organizations.organizations_repository import OrganizationRepository
from app.organizations.organizations_schemas import MemberAdd, OrganizationCreate


class OrganizationService:
    def __init__(self, repo: OrganizationRepository) -> None:
        self.repo = repo

    @staticmethod
    def _slugify(text: str) -> str:
        text = text.lower().strip()
        text = re.sub(r"[^\w\s-]", "", text)
        return re.sub(r"[\s_-]+", "-", text)

    async def create(self, payload: OrganizationCreate, creator_id: uuid.UUID) -> Organization:
        slug = payload.slug or self._slugify(payload.name)
        if await self.repo.get_by_slug(slug) is not None:
            raise OrganizationSlugExistsError(slug=slug)

        try:
            org = await self.repo.create(name=payload.name, slug=slug)
            await self.repo.add_member(
                org_id=org.id, user_id=creator_id, role=UserRole.ADMIN
            )
            await self.repo.session.commit()
        except Exception:
            await self.repo.session.rollback()
            raise
        return org

    async def get(self, org_id: uuid.UUID) -> Organization:
        org = await self.repo.get_by_id(org_id)
        if org is None:
            raise OrganizationNotFoundError(identifier=str(org_id))
        return org

    async def add_member(
        self, org_id: uuid.UUID, payload: MemberAdd
    ) -> OrganizationMember:
        await self.get(org_id)
        if await self.repo.get_member(org_id, payload.user_id) is not None:
            raise OrganizationMemberExistsError()
        return await self.repo.add_member(
            org_id=org_id, user_id=payload.user_id, role=payload.role
        )

    async def list_members(self, org_id: uuid.UUID) -> list[OrganizationMember]:
        await self.get(org_id)
        return await self.repo.list_members(org_id)