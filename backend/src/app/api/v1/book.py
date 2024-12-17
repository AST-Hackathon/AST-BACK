from typing import Any, List

from fastapi import APIRouter, status, UploadFile, Form

from src.app.services.book import BookService

router = APIRouter(tags=['Book'], prefix='/book')


@router.get('/all', status_code=status.HTTP_200_OK)
async def get_all_book():
    """Получение списка всех книг."""
    return await BookService.get_all()
