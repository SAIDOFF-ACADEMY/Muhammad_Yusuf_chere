from rest_framework.serializers import ModelSerializer
from order.models import Order

"""
    costumer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    free_count = models.IntegerField(default=0)
    longitude = models.FloatField()
    latitude = models.FloatField()
    status = models.BooleanField(default=False)
    status_change = models.BigIntegerField()
    product_price = models.BigIntegerField()
    total_price = models.BigIntegerField()

"""


class OrderLandingSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['costumer', 'product', 'count', 'free_count', 'longitude', 'latitude', 'status', 'status_change',
                  'product_price', 'total_price']
        read_only_fields = ['created_at', 'updated_at']
