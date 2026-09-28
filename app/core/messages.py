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