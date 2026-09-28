# app/organizations/organizations_exceptions.py

from app.core.exceptions import ConflictError, NotFoundError
from app.core.messages import OrganizationMessages


class OrganizationNotFoundError(NotFoundError):
    code = "ORGANIZATION_NOT_FOUND"
    default_message = OrganizationMessages.NOT_FOUND

    def __init__(self, identifier: str) -> None:
        super().__init__(message=f"Organization '{identifier}' was not found.")


class OrganizationSlugExistsError(ConflictError):
    code = "ORGANIZATION_SLUG_EXISTS"
    default_message = OrganizationMessages.SLUG_EXISTS

    def __init__(self, slug: str) -> None:
        super().__init__(message=f"Organization slug '{slug}' is already taken.")


class OrganizationMemberExistsError(ConflictError):
    code = "ORGANIZATION_MEMBER_EXISTS"
    default_message = OrganizationMessages.MEMBER_EXISTS


class OrganizationMemberNotFoundError(NotFoundError):
    code = "ORGANIZATION_MEMBER_NOT_FOUND"
    default_message = OrganizationMessages.MEMBER_NOT_FOUND