from abc import ABC, abstractmethod
from typing import Type

from src.database.database import database_accessor
from ..repositories.user.user import AdminRepository
from ..repositories.book.book import BookRepository

from ...database.db_accessor import DatabaseAccessor


# https://github1s.com/cosmicpython/code/tree/chapter_06_uow
class IUnitOfWork(ABC):
    """Interface for Unit of Work pattern."""

    admin: Type[AdminRepository]
    book: Type[BookRepository]

    @abstractmethod
    def __init__(self):
        """Initialize the Unit of Work instance."""

    @abstractmethod
    async def __aenter__(self):
        """Enter the context manager."""

    @abstractmethod
    async def __aexit__(self, *args):
        """Exit the context manager."""

    @abstractmethod
    async def commit(self):
        """Commit changes."""

    @abstractmethod
    async def rollback(self):
        """Rollback changes."""


class UnitOfWork:
    def __init__(self, database_accessor_p: None | DatabaseAccessor = None):
        if database_accessor_p is None:
            database_accessor_p = database_accessor
        self.session_fabric = database_accessor_p.get_async_session_maker()

    async def __aenter__(self):
        """Enter the context manager."""
        self.session = self.session_fabric()

        self.admin = AdminRepository(self.session)
        self.book = BookRepository(self.session)

    async def __aexit__(self, *args) -> None:
        await self.rollback()
        await self.session.close()

    async def commit(self) -> None:
        await self.session.commit()

    async def rollback(self) -> None:
        await self.session.rollback()
