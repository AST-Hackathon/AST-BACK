from fastapi import APIRouter

from src.app_config.config_api import settings

from .v1.book import router as book_v1

router = APIRouter(prefix=settings.APP_PREFIX)

router.include_router(book_v1)
