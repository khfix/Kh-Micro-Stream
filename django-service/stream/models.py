from django.conf import settings
from django.db import models
from khapi.methods import khapi_upload_path


class Hashtag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file_path = models.FileField(upload_to=khapi_upload_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hashtags = models.ManyToManyField(Hashtag, related_name="videos")

    def __str__(self):
        return self.title
