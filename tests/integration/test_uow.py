import pytest
from sqlalchemy import text
from src.domain import model
from src.service_layer import unit_of_work
from src.common.security import verify_password

pytestmark = pytest.mark.usefixtures("mappers")


def insert_user(session, first_name, last_name, email, password_hash):
    session.execute(
        text(
            "INSERT INTO users (first_name, last_name, email, password_hash)"
            " VALUES (:first_name, :last_name, :email, :password_hash)"
        ),
        dict(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password_hash=password_hash,
        ),
    )


def get_password_hash_by_email(session, email):
    [[password_hash]] = session.execute(
        text("SELECT password_hash FROM users WHERE email=:email"),
        dict(email=email),
    )
    return password_hash


def test_uow(sqlite_session_factory):
    session = sqlite_session_factory()
    insert_user(session, "Anh", "Tra", "anh.tra@example.com", "pw_hash")
    session.commit()

    uow = unit_of_work.SqlAlchemyUnitOfWork(sqlite_session_factory)
    with uow:
        user = uow.users.get(email="anh.tra@example.com")
        user.password = "new_password"
        uow.commit()

    password_hash = get_password_hash_by_email(session, "anh.tra@example.com")
    assert verify_password("new_password", password_hash)
