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
        ref_name = 'LandingProductSerializer'



