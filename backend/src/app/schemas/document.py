from pydantic import BaseModel


class DocumentData(BaseModel):
    id: int
    name: str
    url: str

    class Config:
        from_attributes = True


class CreatedDocument(BaseModel):
    name: str
    url: str
