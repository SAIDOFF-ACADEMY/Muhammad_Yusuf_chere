from rest_framework.generics import ListAPIView,  RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser
from products import models
from products import serializers


class ProductListView(ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductsSerializer
    permission_classes = [IsAdminUser]


class ProductDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductsSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'


class ProductCreateView(CreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductsSerializer
    permission_classes = [IsAdminUser]


class FreeProductListView(ListAPIView):
    queryset = models.FreeProduct.objects.all()
    serializer_class = serializers.FreeProductsSerializer
    permission_classes = [IsAdminUser]


class FreeProductDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = models.FreeProduct.objects.all()
    serializer_class = serializers.FreeProductsSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'


class FreeProductCreateView(CreateAPIView):
    queryset = models.FreeProduct.objects.all()
    serializer_class = serializers.FreeProductsSerializer
    permission_classes = [IsAdminUser]