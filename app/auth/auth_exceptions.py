from app.core.exceptions import AuthenticationError, PermissionDeniedError
from app.core.messages import AuthMessages


class InvalidCredentialsError(AuthenticationError):
    code = "INVALID_CREDENTIALS"
    default_message = AuthMessages.INVALID_CREDENTIALS


class InactiveUserError(PermissionDeniedError):
    code = "INACTIVE_USER"
    default_message = AuthMessages.INACTIVE_USER