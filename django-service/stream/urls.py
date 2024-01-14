from django.urls import path

from . import views

urlpatterns = [
    path("hashtags/", views.HashtagsAPI.as_api(), name="hashtags"),
    path(
        "hashtag/value/<str:value>/",
        views.HashtagRetrieveByValueAPI.as_api(),
        name="hashtag-retrieve-by-value",
    ),
    path(
        "video/id/<int:pk>/",
        views.VideoRetrieveByIDAPI.as_api(),
        name="video-retrieve-by-id",
    ),
    path(
        "video/uploader/<int:uploader>/",
        views.VideoRetrieveByUploaderAPI.as_api(),
        name="video-retrieve-by-uploader",
    ),
    path(
        "video/hashtag/value/<str:value>/",
        views.VideoRetrieveByHashtagAPI.as_api(),
        name="video-retrieve-by-hashtag",
    ),
    path("videos/", views.VideosAPI.as_api(), name="videos"),
    path("video/create/", views.VideoCreateAPI.as_api(), name="video-create"),
]
