from typing import List

from sqlalchemy import insert, select

from src.app.models.document.document import DocumentORM
from src.app.schemas.document import DocumentData
from src.app.utils.repository import SQLAlchemyRepository


class DocumentRepository(SQLAlchemyRepository):
    model = DocumentORM
    document = DocumentORM

    # async def add_document(self, create_data) -> DocumentData:
    #     stmt = insert(self.book).values(**create_data).returning(self.book)
    #     result = await self.session.execute(stmt)
    #     new_document = result.scalar_one()
    #     return new_document.get_schema()
