from app.core.exceptions import ConflictError, NotFoundError
from app.core.messages import UserMessages


class UserAlreadyExistsError(ConflictError):
    code = "USER_ALREADY_EXISTS"
    default_message = UserMessages.ALREADY_EXISTS


class UserNotFoundError(NotFoundError):
    code = "USER_NOT_FOUND"
    default_message = UserMessages.NOT_FOUND