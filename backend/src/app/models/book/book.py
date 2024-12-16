from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.app.schemas.book import BookFull, FotoBookFull, AutorBookFull, FeedbackFull
from src.database.database_metadata import Base

from src.app.models.mixin import IsActiveMixin, CreationDateMixin, UpdateDateMixin


class BookORM(Base, CreationDateMixin, UpdateDateMixin):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    avatar: Mapped[str] = mapped_column(String, nullable=False)
    foto: Mapped[list["FotoBookORM"]] = relationship(
        "FotoBookORM", back_populates="foto", cascade="all, delete-orphan"
    )
    autor: Mapped[list["AutorBookORM"]] = relationship(
        "AutorBookORM", back_populates="autor", cascade="all, delete-orphan"
    )

    def get_schema(self) -> BookFull:
        return BookFull.from_orm(self)


class FotoBookORM(Base, IsActiveMixin, CreationDateMixin, UpdateDateMixin):
    __tablename__ = "foto_book"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    foto: Mapped[str] = mapped_column(String, nullable=False)
    book_id: Mapped["BookORM"] = relationship(
        "BookORM", back_populates="book"
    )

    def get_schema(self) -> FotoBookFull:
        return FotoBookFull.from_orm(self)


class AutorBookORM(Base, IsActiveMixin, CreationDateMixin, UpdateDateMixin):
    __tablename__ = "autor_book"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    foto: Mapped[str] = mapped_column(String, nullable=False)
    book_id: Mapped["BookORM"] = relationship(
        "BookORM", back_populates="book"
    )

    def get_schema(self) -> AutorBookFull:
        return AutorBookFull.from_orm(self)


class FeedbackORM(Base, IsActiveMixin, CreationDateMixin, UpdateDateMixin):
    __tablename__ = "feedback"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    autor: Mapped[str] = mapped_column(String, nullable=False)
    text: Mapped[str] = mapped_column(String, nullable=False)

    def get_schema(self) -> FeedbackFull:
        return FeedbackFull.from_orm(self)
