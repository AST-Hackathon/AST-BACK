from fastapi import APIRouter, status, UploadFile, File, Depends

from src.app.utils.ftp_repo import FTPClient
import aiofiles
from src.redisrepo.dependencies import get_ftp_client
import os

router = APIRouter(tags=["UploadFileOnFTP"], prefix="/file")


@router.post("/upload/", status_code=status.HTTP_201_CREATED)
async def upload_file(file: UploadFile = File(...), ftp_client: FTPClient = Depends(get_ftp_client)):
    """Загрузка файла на FTP сервер и возврат ссылки на файл."""
    file_location = f"/uploads/{file.filename}"
    async with aiofiles.open(file.filename, "wb") as out_file:
        content = await file.read()
        await out_file.write(content)

    remote_file_path = await ftp_client.upload_file(file.filename, "/uploads", file.filename)

    os.remove(file.filename)

    return {"file_url": f"http://{ftp_client.server.host}{remote_file_path}"}
