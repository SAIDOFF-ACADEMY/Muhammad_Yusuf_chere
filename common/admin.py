from django.contrib import admin
from .models import Settings, Page, GalleryPhoto
from modeltranslation.admin import TranslationAdmin


@admin.register(Page)
class PageAdmin(TranslationAdmin):
    pass


@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(TranslationAdmin):
    pass


@admin.register(Settings)
class SettingsAdmin(TranslationAdmin):
    def has_add_permission(self, request):
        if Settings.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False
