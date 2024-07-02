from rest_framework import serializers

from products import models


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
        ref_name = 'AdminProductSerializer'

    extra_kwargs = {
        'name_uz': {'required': True},
        'name_ru': {'required': True},
        'content_uz': {'required': True},
        'content_ru': {'required': True},
    }


class FreeProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FreeProduct
        fields = '__all__'
        ref_name = 'AdminFreeProductSerializer'

