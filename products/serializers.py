from rest_framework import serializers

from products import models


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
        ref_name = 'AdminProductSerializer'


class FreeProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FreeProduct
        fields = '__all__'
        ref_name = 'AdminFreeProductSerializer'

