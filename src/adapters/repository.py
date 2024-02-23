import abc
from src.domain import model


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, **kwagrs):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, **kwagrs):
        raise NotImplementedError


class UserRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, user: model.User):
        self.session.add(user)

    def get(self, **kwags):
        return self.session.query(model.User).filter_by(**kwags).first()

    def list(self):
        return self.session.query(model.User).all()
