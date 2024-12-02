from sqladmin import Admin
from sqladmin import ModelView


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
