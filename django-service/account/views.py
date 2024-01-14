from khapi import views as api_views
from khapi.auth_system import views as auth_views

from .models import CustomUser


class UserRegister(auth_views.RegisterAPI):
    model = CustomUser
    register_group = "User"


class StreamerRegister(auth_views.RegisterAPI):
    model = CustomUser
    register_group = "Streamer"


class Login(auth_views.LoginAPI):
    model = CustomUser


class UserRetrieveByIDAPI(api_views.GetByIdAPI):
    model = CustomUser


class UsersAPI(api_views.ListAPI):
    model = CustomUser
