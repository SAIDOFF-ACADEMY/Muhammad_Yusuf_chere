from django.db import models
from product.models import Product
from common.models import BaseModel
from user.models import User


class Order(BaseModel):
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

    def __str__(self):
        return self.costumer.name
