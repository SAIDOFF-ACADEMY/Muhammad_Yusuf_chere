from rest_framework import serializers
from .models import Product, FreeProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'content', 'price']
        read_only_fields = ['created_at', 'updated_at']


class FreeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeProduct
        fields = ['product', 'count', 'free_products']
        read_only_fields = ['created_at', 'updated_at']
