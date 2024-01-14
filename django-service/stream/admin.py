from django.contrib import admin
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from khapi.cache_system.dict_manager import DictManager

from .models import Hashtag, Video


class VideoAdmin(admin.ModelAdmin):
    """
    Admin class for managing Video model in the Django admin interface.
    """

    list_display = ("title", "created_at")
    search_fields = ("title", "created_at")

    @receiver(post_save, sender=Video)
    def video_post_save(sender, instance, created, **kwargs):
        if created:
            my_model_manager = DictManager("Video")
            my_model_manager.create(instance.id, instance)

    @receiver(post_delete, sender=Video)
    def video_post_delete(sender, instance, **kwargs):
        my_model_manager = DictManager("Video")
        my_model_manager.delete(instance.id)


class HashtagAdmin(admin.ModelAdmin):
    """
    Admin class for managing Hashtag model in the Django admin interface.
    """

    list_display = ("name", "created_at")
    search_fields = ("name", "created_at")

    @receiver(post_save, sender=Hashtag)
    def hashtag_post_save(sender, instance, created, **kwargs):
        if created:
            my_model_manager = DictManager("Hashtag")
            my_model_manager.create(instance.id, instance)

    @receiver(post_delete, sender=Hashtag)
    def hashtag_post_delete(sender, instance, **kwargs):
        my_model_manager = DictManager("Hashtag")
        my_model_manager.delete(instance.id)


admin.site.register(Video, VideoAdmin)
admin.site.register(Hashtag, HashtagAdmin)
