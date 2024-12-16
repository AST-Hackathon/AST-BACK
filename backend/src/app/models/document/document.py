from sqlalchemy import Integer
from sqlalchemy.orm import mapped_column, Mapped

from src.app.schemas.document import DocumentData
from src.database.database_metadata import Base


class DocumentORM(Base):
    __tablename__ = "document"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    url: Mapped[str] = mapped_column(nullable=False)

    def get_schema(self) -> DocumentData:
        return DocumentData.from_orm(self)
