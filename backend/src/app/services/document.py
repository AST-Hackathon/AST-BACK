import os
from typing import List

import cyrtranslit
from fastapi import UploadFile, Form, HTTPException, status

from src.app.schemas.document import DocumentData
from src.app.utils.unitofwork import IUnitOfWork, UnitOfWork
from src.s3repo.DocumentS3Repo import document_storage

MAX_FILE_NAME_LENGTH = 32


class DocumentService:

    @classmethod
    async def create_document(
        cls,
        document: UploadFile,
        name: str = Form(...),
        uow: IUnitOfWork = UnitOfWork(),
    ) -> DocumentData:

        _, file_extension = os.path.splitext(document.filename)
        latin_name = cyrtranslit.to_latin(name, "ru")
        sanitized_name = "-".join(latin_name.split())[
            : MAX_FILE_NAME_LENGTH - len(file_extension)
        ]

        file_name = f"{sanitized_name}{file_extension}"

        if len(file_name) > MAX_FILE_NAME_LENGTH:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail="The file name exceeds the maximum allowed length of 32 characters.",
            )
        document_url = await document_storage.send_to_storage(
            document.file, file_name
        )

        if document_url.data is None:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail=document_url.message,
            )

        async with uow:
            result = await uow.document.add_one(
                data=dict(name=file_name, url=document_url.data)
            )
            await uow.commit()
        return result
