from dataclasses import dataclass
from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from src.common.security import hash_password, verify_password

# @dataclass
# class User:
#     first_name: str
#     last_name: str
#     email: str
#     # password_hash: str
#     created_at: datetime
#     updated_at: datetime


class User:
    """The User model."""

    def __init__(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        email: Optional[str] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password: str):
        # self.password_hash = generate_password_hash(password)
        self.password_hash = hash_password(password)

    @staticmethod
    def create(data: dict):
        """Create a new user."""
        user = User()
        user.from_dict(data, partial_update=False)
        return user

    def from_dict(self, data, partial_update=True):
        """Import user data from a dictionary."""
        for field in ["first_name", "last_name", "email", "password"]:
            try:
                setattr(self, field, data[field])
            except KeyError:
                if not partial_update:
                    raise ValueError(f"Cannot setattr for field of {field}")

    def to_dict(self):
        """Export user to a dictionary."""
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
        }

    def to_pydantic(self):
        pass

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        for field in ["first_name", "last_name", "email"]:
            if getattr(self, field) != getattr(other, field):
                return False
        return True
