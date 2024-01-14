from django.contrib import admin
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from khapi.cache_system.dict_manager import DictManager

from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    """
    Admin class for managing CustomUser model in the Django admin interface.
    """

    list_display = ("email", "created_at")
    search_fields = ("email", "created_at")

    @receiver(post_save, sender=CustomUser)
    def account_post_save(sender, instance, created, **kwargs):
        if created:
            my_model_manager = DictManager("CustomUser")
            my_model_manager.create(instance.id, instance)

    @receiver(post_delete, sender=CustomUser)
    def account_post_delete(sender, instance, **kwargs):
        my_model_manager = DictManager("CustomUser")
        my_model_manager.delete(instance.id)


admin.site.register(CustomUser, CustomUserAdmin)
