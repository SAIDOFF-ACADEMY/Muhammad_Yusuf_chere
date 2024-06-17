from django.contrib import admin
from .models import Product, Order, FreeProduct, GalleryPhoto

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(FreeProduct)
admin.site.register(GalleryPhoto)