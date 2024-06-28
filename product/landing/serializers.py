from rest_framework import serializers
from product.models import Product, FreeProduct


class ProductLandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'content', 'price']
        read_only_fields = ['created_at', 'updated_at']


class FreeProductLandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeProduct
        fields = ['product', 'count', 'free_products']
        read_only_fields = ['created_at', 'updated_at']
