from sqladmin import Admin
from sqladmin import ModelView

from src.app.models.book.book import BookORM, FotoBookORM, AuthorBookORM, FeedbackORM
from src.app.models.theme_page.theme_page import ThemePageORM


class BaseModelView(ModelView):
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    can_export = True
    page_size = 100

    form_excluded_columns = [
        'creation_date',
        'update_date',
    ]

    form_widget_args = {
        'creation_date': {
            'readonly': True,
        },
        'update_date': {
            'readonly': True,
        },
    }

    BASE_LIST = [
        'id',
        'creation_date',
        'update_date'
    ]


class BookAdmin(BaseModelView, model=BookORM):
    name = "Книга"
    name_plural = "Книги"

    BASE_LIST = [BaseModelView.BASE_LIST[0]] + [
        BookORM.title,
        BookORM.url,
        BookORM.avatar,
        BookORM.photo_preview,
        BookORM.description,
    ] + BaseModelView.BASE_LIST[1:]

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
        BookORM.url: "Ссылка на книгу",
        BookORM.creation_date: "Дата создания",
        BookORM.update_date: "Дата обновления"
    }


class FotoBookAdmin(BaseModelView, model=FotoBookORM):
    name = "Фото книги"
    name_plural = "Фото книг"

    BASE_LIST = [BaseModelView.BASE_LIST[0]] + [
        FotoBookORM.foto,
        FotoBookORM.book_id,
        FotoBookORM.book
    ] + BaseModelView.BASE_LIST[1:]

    column_sortable_list = BASE_LIST
    column_list = BASE_LIST

    column_labels = {
        FotoBookORM.id: "ID",
        FotoBookORM.foto: "Фото",
        FotoBookORM.book_id: "ID Книги",
        FotoBookORM.book: "Книга",
        FotoBookORM.creation_date: "Дата создания",
        FotoBookORM.update_date: "Дата обновления"
    }


class AutorBookAdmin(BaseModelView, model=AuthorBookORM):
    name = "Автор книги"
    name_plural = "Авторы книг"

    BASE_LIST = [BaseModelView.BASE_LIST[0]] + [
        AuthorBookORM.title,
        AuthorBookORM.foto,
        AuthorBookORM.book_id,
        AuthorBookORM.book
    ] + BaseModelView.BASE_LIST[1:]

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
        AuthorBookORM.book: "Книга",
        AuthorBookORM.creation_date: "Дата создания",
        AuthorBookORM.update_date: "Дата обновления"
    }


class FeedbackAdmin(BaseModelView, model=FeedbackORM):
    name = "Отзыв"
    name_plural = "Отзывы"

    BASE_LIST = [BaseModelView.BASE_LIST[0]] + [
        FeedbackORM.is_active,
        FeedbackORM.author,
        FeedbackORM.text
    ] + BaseModelView.BASE_LIST[1:]

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
        FeedbackORM.is_active: "Активный",
        FeedbackORM.creation_date: "Дата создания",
        FeedbackORM.update_date: "Дата обновления"
    }


class ThemePageAdmin(BaseModelView, model=ThemePageORM):
    name = "Тема главной страницы"
    name_plural = "Темы главной страницы"

    BASE_LIST = [BaseModelView.BASE_LIST[0]] + [
        ThemePageORM.is_active,
        ThemePageORM.title,
    ] + BaseModelView.BASE_LIST[1:]

    column_searchable_list = [
        ThemePageORM.title,
    ]

    column_sortable_list = BASE_LIST
    column_list = BASE_LIST

    column_labels = {
        ThemePageORM.id: "ID",
        ThemePageORM.title: "Название темы",
        ThemePageORM.header: "Фото шапки",
        ThemePageORM.foto_1: "Фото №1",
        ThemePageORM.foto_2: "Фото №2",
        ThemePageORM.foto_3: "Фото №3",
        ThemePageORM.foto_4: "Фото №4",
        ThemePageORM.foto_5: "Фото №5",
        ThemePageORM.foto_6: "Фото №6",
        ThemePageORM.foto_7: "Фото №7",
        ThemePageORM.foto_8: "Фото №8",
        ThemePageORM.foto_9: "Фото №9",
        ThemePageORM.foto_10: "Фото №10",
        ThemePageORM.foto_11: "Фото №11",
        ThemePageORM.footer_bg: "Фото футера",
        ThemePageORM.footer_logo: "Логотип футера",
        ThemePageORM.is_active: "Действующая",
        ThemePageORM.creation_date: "Дата создания",
        ThemePageORM.update_date: "Дата обновления"
    }


def create_admin(app, engine):
    admin = Admin(app, engine, title="ACT")
    admin.add_view(BookAdmin)
    admin.add_view(FotoBookAdmin)
    admin.add_view(AutorBookAdmin)
    admin.add_view(FeedbackAdmin)
    admin.add_view(ThemePageAdmin)
    return admin
