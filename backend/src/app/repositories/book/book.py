from sqlalchemy import select
from sqlalchemy.orm import joinedload
from src.app.models.book.book import BookORM
from src.app.schemas.book import BookFull, AuthorBookFull, FotoBookFull, BookAllFull
from src.app.utils.repository import SQLAlchemyRepository


class BookRepository(SQLAlchemyRepository):
    model = BookORM

    async def get_all(self):
        stmt = (
            select(self.model)
        )

        res = await self.session.execute(stmt)
        books = res.scalars().unique().all()
        book_full_list = []
        for book in books:
            book_full = BookAllFull.from_orm(book)
            book_full_list.append(book_full)

        return book_full_list

    async def get_by_id(self, id: int):
        stmt = (
            select(self.model)
            .options(joinedload(self.model.authors))
            .options(joinedload(self.model.fotos))
            .where(self.model.id == id)
        )

        res = await self.session.execute(stmt)

        book = res.scalars().first()

        authors_full = [AuthorBookFull.from_orm(author) for author in book.authors]
        fotos_full = [FotoBookFull.from_orm(foto) for foto in book.fotos]

        book_full = BookFull.from_orm(book)
        book_full.authors = authors_full
        book_full.fotos = fotos_full

        return book_full
