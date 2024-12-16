from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped
from src.database.database_metadata import Base

from src.app.models.mixin import CreationDateMixin, UpdateDateMixin


class AdminORM(Base, CreationDateMixin, UpdateDateMixin):
    __tablename__ = "admin"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    login: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
