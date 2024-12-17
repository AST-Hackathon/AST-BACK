from src.app.utils.unitofwork import IUnitOfWork, UnitOfWork


class BookService:
    @classmethod
    async def get_all(cls, uow: IUnitOfWork = UnitOfWork()):
        async with uow:
            result = await uow.book.get_all()
            print(111111111111111111111111111111111111, result)
            return result
