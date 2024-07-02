from rest_framework.generics import ListAPIView

from products import models
from products.landing import serializers


class ProductView(ListAPIView):
    queryset = models.Product.objects.all().filter(is_active=True)
    serializer_class = serializers.ProductsSerializer

