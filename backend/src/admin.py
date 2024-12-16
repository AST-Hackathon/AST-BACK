from typing import Union

import wtforms
from fastapi.openapi.models import Response

from sqladmin import Admin
from sqladmin import ModelView
from sqladmin.authentication import AuthenticationBackend
from fastapi import Request, Response



class MyBackend(AuthenticationBackend):

    async def login(self, request: Request) -> Union[bool, str]:
        form = await request.form()
        username, password = form["username"], form["password"]

        # token = await UserService.login_user(response, username, password)
        #
        # if not token:
        #     return "Invalid username or password"
        #
        # user = await UserService.get_user_by_id(token.user_id)
        #
        # if user.role != UserRole.SuperUserRole:
        #     return "User is not a Super User"

        request.session["token"] = "token.access_token"
        return True

    async def logout(self, request: Request) -> Union[bool, str]:
        request.session.clear()
        return "Logged out successfully"

    async def authenticate(self, request: Request) -> bool:
        return "token" in request.session




def create_admin(app, engine):
    authentication_backend = MyBackend(secret_key="...")

    admin = Admin(
        app,
        engine,
        title="SmileAI",
        authentication_backend=authentication_backend,
    )

    return admin
