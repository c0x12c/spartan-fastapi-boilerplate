from __future__ import annotations

from src.domain import model
from src.domain.model import User
from src.service_layer import unit_of_work
from src.common.security import verify_password
from src.common.auth import encode_jwt


class InvalidEmail(Exception):
    pass


class InvalidPassword(Exception):
    pass


def add_user(user: User, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        if uow.users.get(email=user.email):
            raise InvalidEmail(f"Invalid email {user.email}")
        uow.users.add(user)
        uow.commit()
        user_dict = user.to_dict()
    return user_dict


def create_token(email: str, password: str, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        user = uow.users.get(email=email)
        if user is None:
            raise InvalidEmail(f"Invalid email {user.email}")
        if not verify_password(password, user.password_hash):
            raise InvalidPassword(f"Invalid password for {user.email}")

        user_dict = user.to_dict()
        token = encode_jwt(data=user_dict)

    return token, user_dict
