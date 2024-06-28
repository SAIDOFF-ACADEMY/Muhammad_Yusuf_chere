from django.contrib import admin
from .models import Order
from modeltranslation.admin import TranslationAdmin


@admin.register(Order)
class OrderAdmin(TranslationAdmin):
    list_display = ('costumer', 'count')
    list_display_links = ('costumer', 'count')
    readonly_fields = ('created_at', 'updated_at')
