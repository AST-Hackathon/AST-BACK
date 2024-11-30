from database.unitofwork import IUnitOfWork, UnitOfWork


class TestService:
    @classmethod
    async def create(cls, uow: IUnitOfWork = UnitOfWork()) -> None:
        async with uow:
            return None