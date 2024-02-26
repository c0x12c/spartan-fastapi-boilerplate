# pylint: disable=attribute-defined-outside-init
from __future__ import annotations
import abc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.session import Session


from src.config import Config
from src.adapters import repository


class AbstractUnitOfWork(abc.ABC):
    users: repository.UserRepository

    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError


DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        Config.SQLALCHEMY_DATABASE_URI,
    )
)


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = scoped_session(session_factory)

    def __enter__(self):
        self.session = self.session_factory()  # type: Session
        self.users = repository.UserRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session_factory.remove()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
