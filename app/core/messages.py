"""User-facing message strings, grouped by module."""


class AuthMessages:
    INVALID_CREDENTIALS = "Incorrect email or password."
    INACTIVE_USER = "Inactive user account."
    COULD_NOT_VALIDATE_CREDENTIALS = "Could not validate credentials."


class UserMessages:
    ALREADY_EXISTS = "A user with this email already exists."
    NOT_FOUND = "User not found."


class GeneralMessages:
    UNEXPECTED_ERROR = "An unexpected error occurred."


class OrganizationMessages:
    NOT_FOUND = "Organization not found."
    SLUG_EXISTS = "Organization slug is already taken."
    MEMBER_EXISTS = "User is already a member of this organization."
    MEMBER_NOT_FOUND = "User is not a member of this organization."