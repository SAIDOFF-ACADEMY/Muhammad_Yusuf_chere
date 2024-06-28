from django.contrib import admin
from .models import Product
from modeltranslation.admin import TranslationAdmin


# @admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('name', 'content', 'price')
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Product, ProductAdmin)
