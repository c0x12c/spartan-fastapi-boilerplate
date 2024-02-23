from sqlalchemy import Table, MetaData, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import registry

from src.domain import model
from src.common import utils


mapper_registry = registry()


users = Table(
    "users",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("first_name", String(60), nullable=False),
    Column("last_name", String(60), nullable=False),
    Column("email", String(256), nullable=False, unique=True),
    Column("password_hash", String(256), nullable=False),
    Column("created_at", Integer, default=utils.timestamp),
    Column("updated_at", Integer, default=utils.timestamp, onupdate=utils.timestamp),
)


def start_mappers():
    users_mapper = mapper_registry.map_imperatively(model.User, users)
