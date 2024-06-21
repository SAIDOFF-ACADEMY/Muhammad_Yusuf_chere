from django.contrib import admin
from .models import Settings, Page

admin.site.register(Page)
admin.site.register(Settings)