# from database.db_metadata import Base
# from database.models.mixin import IsActiveMixin
# from pydantic import BaseModel
# from sqlalchemy import Integer, String, ForeignKey
# from sqlalchemy.orm import Mapped, mapped_column, relationship


# class ORM(Base, IsActiveMixin):
#     __tablename__ = ""

#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     : Mapped[] = mapped_column()
#     : Mapped[] = mapped_column()
#     : Mapped[] = mapped_column( ,ForeignKey("", ondelete="CASCADE"))
#     : Mapped[] = mapped_column( ,ForeignKey("", ondelete="CASCADE"))
#     : Mapped[] = relationship("", back_populates="")
#     : Mapped[] = relationship("", back_populates="")


#     def get_schema(self) -> :
#         return (
#             id=self.id,
#         )
