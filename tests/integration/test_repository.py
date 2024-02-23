import pytest
from src.domain import model
from src.adapters import repository
from datetime import datetime
from sqlalchemy.sql import text


pytestmark = pytest.mark.usefixtures("mappers")


def test_repository_can_save_an_user(sqlite_session_factory):
    session = sqlite_session_factory()
    user = model.User.create(
        {
            "first_name": "Anh",
            "last_name": "Tra",
            "email": "anh.tra@example.com",
            "password": "12345678",
        }
    )

    repo = repository.UserRepository(session)
    repo.add(user)
    session.commit()

    rows = session.execute(text('SELECT first_name, last_name, email FROM "users"'))
    assert list(rows) == [("Anh", "Tra", "anh.tra@example.com")]
