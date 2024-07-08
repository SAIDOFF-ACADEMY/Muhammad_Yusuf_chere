from django.contrib import admin
from .models import User, UserContactApplication
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy


@admin.register(User)
class UserAdmin(UserAdmin):
    search_fields = ("email", "full_name")
    list_display = ("email", "is_staff")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (gettext_lazy("Personal info"), {"fields": ("full_name", "phone")}),
        (
            gettext_lazy("Permissions"),
            {
                "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions",),
            },
        ),
        (gettext_lazy("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    ordering = ("email",)


admin.site.register(UserContactApplication)
