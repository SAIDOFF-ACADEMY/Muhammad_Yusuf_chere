from rest_framework import serializers
from order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['costumer', 'product', 'count', 'free_count', 'longitude', 'latitude', 'status', 'status_change',
                  'product_price', 'total_price']
        read_only_fields = ['created_at', 'updated_at']