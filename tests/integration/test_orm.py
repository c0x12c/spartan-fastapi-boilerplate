import pytest
from src.domain import model
from datetime import datetime
from sqlalchemy.sql import text


pytestmark = pytest.mark.usefixtures("mappers")


def test_users_mapper_can_load_users(sqlite_session_factory):
    session = sqlite_session_factory()

    session.execute(
        text(
            "INSERT INTO users (first_name, last_name, email, password_hash) VALUES "
            '("f1", "l1", "e1@example.com", "p1"),'
            '("f2", "l2", "e2@example.com", "p2"),'
            '("f3", "l3", "e3@example.com", "p3")'
        )
    )

    expected = [
        model.User("f1", "l1", "e1@example.com"),
        model.User("f2", "l2", "e2@example.com"),
        model.User("f3", "l3", "e3@example.com"),
    ]
    assert session.query(model.User).all() == expected
