from pydantic import BaseModel


class BookFull(BaseModel):
    id: int
    title: str
    description: str
    avatar: str
    foto: list[str]
    autor: list[str]

    class Config:
        from_attributes = True


class FotoBookFull(BaseModel):
    id: int
    foto: str
    book_id: int

    class Config:
        from_attributes = True


class AutorBookFull(BaseModel):
    id: int
    title: str
    foto: str
    book_id: int

    class Config:
        from_attributes = True


class FeedbackFull(BaseModel):
    id: int
    autor: str
    text: str

    class Config:
        from_attributes = True

# class CreatedDocument(BaseModel):
#     name: str
#     url: str
