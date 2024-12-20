from pydantic import BaseModel


class ThemePageFull(BaseModel):
    title: str
    header: str
    foto_1: str
    foto_2: str
    foto_3: str
    foto_4: str
    foto_5: str
    foto_6: str
    foto_7: str
    foto_8: str
    foto_9: str
    foto_10: str
    foto_11: str
    footer_bg: str
    footer_logo: str

    class Config:
        from_attributes = True
