from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView

from products import models
from products.landing import serializers


class ProductView(ListAPIView):
    queryset = models.Product.objects.all().filter(is_active=True)
    serializer_class = serializers.ProductsSerializer

