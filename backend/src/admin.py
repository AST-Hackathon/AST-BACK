from sqladmin import Admin
from sqladmin import ModelView

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

    BASE_LIST = [
        BookORM.id,
        BookORM.title,
        BookORM.url,
        BookORM.avatar,
        BookORM.photo_preview,
        BookORM.description
    ]

    column_searchable_list = [
        BookORM.title,
        BookORM.description
    ]

    column_sortable_list = BASE_LIST
    column_list = BASE_LIST

    column_labels = {
        BookORM.id: "ID",
        BookORM.title: "Название",
        BookORM.description: "Описание",
        BookORM.avatar: "Аватар",
        BookORM.fotos: "Фото",
        BookORM.photo_preview: "Предпросмотр фото",
        BookORM.authors: "Авторы",
        BookORM.url: "Ссылка на книгу"
    }


class FotoBookAdmin(BaseModelView, model=FotoBookORM):
    name = "Фото книги"
    name_plural = "Фото книг"

    BASE_LIST = [
        FotoBookORM.id,
        FotoBookORM.foto,
        FotoBookORM.book_id,
        FotoBookORM.book
    ]

    column_sortable_list = BASE_LIST
    column_list = BASE_LIST

    column_labels = {
        FotoBookORM.id: "ID",
        FotoBookORM.foto: "Фото",
        FotoBookORM.book_id: "ID Книги",
        FotoBookORM.book: "Книга"
    }


class AutorBookAdmin(BaseModelView, model=AuthorBookORM):
    name = "Автор книги"
    name_plural = "Авторы книг"

    BASE_LIST = [
        AuthorBookORM.id,
        AuthorBookORM.title,
        AuthorBookORM.foto,
        AuthorBookORM.book_id,
        AuthorBookORM.book
    ]

    column_searchable_list = [
        AuthorBookORM.title,
    ]

    column_sortable_list = BASE_LIST
    column_list = BASE_LIST

    column_labels = {
        AuthorBookORM.id: "ID",
        AuthorBookORM.title: "ФИО автора",
        AuthorBookORM.foto: "Фото",
        AuthorBookORM.book_id: "ID Книги",
        AuthorBookORM.book: "Книга"
    }


class FeedbackAdmin(BaseModelView, model=FeedbackORM):
    name = "Отзыв"
    name_plural = "Отзывы"

    BASE_LIST = [
        FeedbackORM.id,
        FeedbackORM.is_active,
        FeedbackORM.author,
        FeedbackORM.text
    ]

    column_searchable_list = [
        FeedbackORM.author,
        FeedbackORM.text
    ]

    column_sortable_list = BASE_LIST
    column_list = BASE_LIST

    column_labels = {
        FeedbackORM.id: "ID",
        FeedbackORM.author: "Пользователь",
        FeedbackORM.text: "Текст",
        FeedbackORM.is_active: "Активный"
    }


def create_admin(app, engine):
    admin = Admin(app, engine, title="ACT")
    admin.add_view(BookAdmin)
    admin.add_view(FotoBookAdmin)
    admin.add_view(AutorBookAdmin)
    admin.add_view(FeedbackAdmin)
    return admin
