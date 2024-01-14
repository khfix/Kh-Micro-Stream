from django.urls import path
from khapi.khapi_start import khapi_cache_start

from . import views

khapi_cache_start()

urlpatterns = [
    path("register/user/", views.UserRegister.as_api(), name="uregister"),
    path("register/streamer/", views.StreamerRegister.as_api(), name="sregister"),
    path("login/", views.Login.as_api(), name="login"),
    path(
        "user/id/<int:pk>/",
        views.UserRetrieveByIDAPI.as_api(),
        name="user-retrieve-by-id",
    ),
    path("users/", views.UsersAPI.as_api(), name="users"),
]
