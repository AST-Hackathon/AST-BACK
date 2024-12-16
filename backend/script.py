import asyncio

from pydantic_settings import BaseSettings, SettingsConfigDict

# from src.app.schemas.auth import UserCreate
from src.app.services.user import UserService
from src.app.utils.unitofwork import UnitOfWork
from src.app_config.config_db import DBSettings

from src.database.database_metadata import Base
from src.database.db_accessor import DatabaseAccessor


# class AdminSettings(BaseSettings):
#     model_config = SettingsConfigDict(
#         env_file=".env",
#         env_file_encoding="utf-8",
#         extra="ignore",
#         case_sensitive=False,
#         env_prefix="ADMIN__",
#     )
#     LOGIN: str
#     PASSWORD: str


async def add_user_to_db():
    try:
        # admin_settings = AdminSettings()
        db_settings = DBSettings()
        db_accessor = DatabaseAccessor(db_settings)
        await db_accessor.run()
        await db_accessor.init_db(Base)

        uow = UnitOfWork(database_accessor_p=db_accessor)

        async with uow:
            await UserService.create_admin(id=1, login='admin', email='admin@admin.com', password='admin')

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    asyncio.run(add_user_to_db())
