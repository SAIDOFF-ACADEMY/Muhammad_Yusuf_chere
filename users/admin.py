from django.contrib import admin
from .models import CustomUser, UserContactApplication


admin.site.register(CustomUser)
admin.site.register(UserContactApplication)