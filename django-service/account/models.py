from django.conf import settings
from django.db import models
from khapi.auth_system.models import ApiUser


class CustomUser(ApiUser):
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.email
