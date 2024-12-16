from fastapi import APIRouter

from src.app_config.config_api import settings

from .v1.document import router as document_v1

router = APIRouter(prefix=settings.APP_PREFIX)

router.include_router(document_v1)
