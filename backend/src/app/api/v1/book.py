from typing import Any, List

from fastapi import APIRouter, status, UploadFile, Form, File, Depends

from src.app.services.book import BookService
from src.app.schemas.book import BookFull, BookAllFull
from src.app.utils.ftp_repo import FTPClient
from src.app.utils.ftp_serv import FTPServer
import aiofiles
from src.redisrepo.dependencies import get_ftp_client
import os


router = APIRouter(tags=['Book'], prefix='/book')


@router.get('/all/', status_code=status.HTTP_200_OK, response_model=List[BookAllFull])
async def get_all_book(id: int):
    """Получение списка всех книг кроме текущего, на странице которого находимся. Надо передать её id."""
    return await BookService.get_all(id=id)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=BookFull)
async def get_book(id: int):
    """Получение конкретной книги по id."""
    return await BookService.get_book(id=id)

@router.post('/upload/', status_code=status.HTTP_201_CREATED)
async def upload_file(file: UploadFile = File(...), ftp_client: FTPClient = Depends(get_ftp_client)):
    """Загрузка файла на FTP сервер и возврат ссылки на файл."""
    file_location = f"/uploads/{file.filename}"
    async with aiofiles.open(file.filename, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)
    
    remote_file_path = await ftp_client.upload_file(file.filename, "/uploads", file.filename)
    
    os.remove(file.filename)
    
    return {"file_url": f"http://{ftp_client.server.host}{remote_file_path}"}