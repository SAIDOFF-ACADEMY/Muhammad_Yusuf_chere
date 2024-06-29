from django.contrib.auth import get_user
from rest_framework import serializers

from order import models


class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = (
            'status',
        )
        ref_name = 'AdminOrderSerializer'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'
