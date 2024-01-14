from django.shortcuts import render
from khapi import views as api_views

from .models import Hashtag, Video


class HashtagRetrieveByValueAPI(api_views.ListByValueAPI):
    model = Hashtag
    exclude_fields = ["created_at", "updated_at"]


class HashtagsAPI(api_views.ListAPI):
    model = Hashtag
    exclude_fields = ["created_at", "updated_at"]


class VideoRetrieveByIDAPI(api_views.GetByIdAPI):
    model = Video
    exclude_fields = ["updated_at"]


class VideoRetrieveByUploaderAPI(api_views.ListByValueAPI):
    model = Video
    exclude_fields = ["updated_at"]


class VideoRetrieveByHashtagAPI(api_views.ListByValueAPI):
    model = Video
    exclude_fields = ["updated_at"]


class VideosAPI(api_views.ListAPI):
    model = Video
    exclude_fields = ["updated_at"]


class VideoCreateAPI(api_views.CreateAPI):
    model = Video
    exclude_fields = ["id", "updated_at", "created_at"]
