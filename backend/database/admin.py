from sqladmin import Admin
from sqladmin import ModelView
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from .models import (
    ThemeORM,
    AuthorORM,
    ArticleORM,
    ContentBlockORM,
    ThemeToArticleORM,
    AuthorToArticleORM,
)


class BaseModelView(ModelView):
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    can_export = True
    page_size = 100
    
    
def create_admin(app, engine):

    admin = Admin(app, engine, title="ADMINHAHTON")
    return admin