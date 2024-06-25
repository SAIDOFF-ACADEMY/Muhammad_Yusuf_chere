from django.contrib import admin
from .models import Settings, Page
from modeltranslation.admin import TranslationAdmin

admin.site.register(Page)


@admin.register(Settings)
class SettingsAdmin(TranslationAdmin):
    def has_add_permission(self, request):
        if Settings.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False