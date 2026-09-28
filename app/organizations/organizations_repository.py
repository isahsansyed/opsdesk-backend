# app/organizations/organizations_repository.py

import uuid
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.constants import UserRole
from app.organizations.organizations_models import Organization, OrganizationMember

class OrganizationRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_by_id(self, org_id: uuid.UUID) -> Organization | None:
        result = await self.session.execute(
            select(Organization).where(Organization.id == org_id)
        )
        return result.scalar_one_or_none()

    async def get_by_slug(self, slug: str) -> Organization | None:
        result = await self.session.execute(
            select(Organization).where(Organization.slug == slug)
        )
        return result.scalar_one_or_none()

    async def create(self, name: str, slug: str) -> Organization:
        org = Organization(name=name, slug=slug)
        self.session.add(org)
        await self.session.flush() # <- NOT commit
        await self.session.refresh(org)
        return org

    async def add_member(
        self, org_id: uuid.UUID, user_id: uuid.UUID, role: UserRole
    ) -> OrganizationMember:
        member = OrganizationMember(
            organization_id=org_id, user_id=user_id, role=role
        )
        self.session.add(member)
        await self.session.flush() # <- NOT commit
        await self.session.refresh(member)
        return member

    async def get_member(
        self, org_id: uuid.UUID, user_id: uuid.UUID
    ) -> OrganizationMember | None:
        result = await self.session.execute(
            select(OrganizationMember).where(
                OrganizationMember.organization_id == org_id,
                OrganizationMember.user_id == user_id,
            )
        )
        return result.scalar_one_or_none()

    async def list_members(self, org_id: uuid.UUID) -> list[OrganizationMember]:
        result = await self.session.execute(
            select(OrganizationMember).where(
                OrganizationMember.organization_id == org_id
            )
        )
        return list(result.scalars().all())