from pydantic import BaseModel


class FotoBookFull(BaseModel):
    id: int
    foto: str
    book_id: int

    class Config:
        from_attributes = True


class AuthorBookFull(BaseModel):
    id: int
    title: str
    foto: str
    book_id: int

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


class FeedbackFull(BaseModel):
    id: int
    autor: str
    text: str

    class Config:
        from_attributes = True
