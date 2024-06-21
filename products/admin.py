from django.contrib import admin
from .models import Product, FreeProduct, GalleryPhoto

admin.site.register(Product)
admin.site.register(FreeProduct)
admin.site.register(GalleryPhoto)