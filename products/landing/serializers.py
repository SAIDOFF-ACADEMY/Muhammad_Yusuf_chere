from rest_framework import serializers

from products import models


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = (
            'name',
            'content',
            'price',
        )


class FreeProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FreeProduct
        fields = (
            'product.name',
            'count',
            'free_count',
        )
