from pydantic import BaseModel


class FotoBookFull(BaseModel):
    foto: str

    class Config:
        from_attributes = True


class AuthorBookFull(BaseModel):
    title: str
    foto: str

    class Config:
        from_attributes = True


class BookFull(BaseModel):
    id: int
    title: str
    description: str
    avatar: str
    fotos: list[FotoBookFull] = []
    authors: list[AuthorBookFull] = []

    class Config:
        from_attributes = True


class BookAllFull(BaseModel):
    id: int
    title: str
    photo_preview: str | None

    class Config:
        from_attributes = True


class FeedbackFull(BaseModel):
    id: int
    autor: str
    text: str

    class Config:
        from_attributes = True
