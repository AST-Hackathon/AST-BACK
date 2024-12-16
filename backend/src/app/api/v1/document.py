from typing import Any, List

from fastapi import APIRouter, status, UploadFile, Form

from src.app.schemas.document import DocumentData
from src.app.services.document import DocumentService

router = APIRouter(prefix="/document", tags=["Document"])


@router.post(
    "/document",
    status_code=status.HTTP_200_OK,
    response_model=DocumentData,
)
async def add_document(
    document: UploadFile,
    name: str = Form(...),
) -> Any:
    result = await DocumentService.create_document(
        document=document, name=name
    )
    return result
