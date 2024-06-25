from rest_framework import serializers
from .models import Product, FreeProduct, GalleryPhoto


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'content',
            'price',
        )


class FreeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeProduct
        fields = (
            'id',
            'product',
            'count',
            'free_count',
        )


class GalleryPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryPhoto
        fields = (
            'id',
            'photo',
        )