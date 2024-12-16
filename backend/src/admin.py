from typing import Union

import wtforms
from fastapi.openapi.models import Response

from sqladmin import Admin
from sqladmin import ModelView
from sqladmin.authentication import AuthenticationBackend
from fastapi import Request, Response

from src.app.models.book.book import BookORM, FotoBookORM, AuthorBookORM, FeedbackORM


class BaseModelView(ModelView):
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    can_export = True
    page_size = 100


class BookAdmin(BaseModelView, model=BookORM):
    name = "Книга"
    name_plural = "Книги"

    column_list = [
        BookORM.id,
        BookORM.title,
        BookORM.description,
        BookORM.avatar,
        BookORM.fotos,
        BookORM.authors
    ]


class FotoBookAdmin(BaseModelView, model=FotoBookORM):
    name = "Фото книги"
    name_plural = "Фото книг"

    column_list = [
        FotoBookORM.id,
        FotoBookORM.foto,
        FotoBookORM.book_id,
        FotoBookORM.book
    ]


class AutorBookAdmin(BaseModelView, model=AuthorBookORM):
    name = "Автор книги"
    name_plural = "Авторы книг"

    column_list = [
        AuthorBookORM.id,
        AuthorBookORM.title,
        AuthorBookORM.foto,
        AuthorBookORM.book_id,
        AuthorBookORM.book
    ]


class FeedbackAdmin(BaseModelView, model=FeedbackORM):
    name = "Отзыв"
    name_plural = "Отзывы"

    column_list = [
        FeedbackORM.id,
        FeedbackORM.autor,
        FeedbackORM.text,
    ]


def create_admin(app, engine):
    admin = Admin(app, engine, title="ACT")
    admin.add_view(BookAdmin)
    admin.add_view(FotoBookAdmin)
    admin.add_view(AutorBookAdmin)
    admin.add_view(FeedbackAdmin)
    return admin
