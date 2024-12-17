from typing import Any, List

from fastapi import APIRouter, status, UploadFile, Form

from src.app.services.feedback import FeedbackService
from src.app.schemas.book import FeedbackFull


router = APIRouter(tags=['Feedback'], prefix='/feedback')


@router.get('/all', status_code=status.HTTP_200_OK, response_model=List[FeedbackFull])
async def get_all_feedback():
    """Получение списка всех отзывов."""
    return await FeedbackService.get_all()


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=FeedbackFull)
async def create_feedback(data: FeedbackFull):
    """Создание отзыва пользователем."""
    return await FeedbackService.add_one(data=data)

