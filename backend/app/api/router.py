from fastapi import APIRouter

from config.api import settings
#from app.api.v1.example import router as example_router

router = APIRouter(prefix=settings.APP_PREFIX)


#router.include_router(example_router)
