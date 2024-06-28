from django.shortcuts import render
from rest_framework import generics
from .models import Product, FreeProduct
from .serializers import ProductSerializer, FreeProductSerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class FreeProductList(generics.ListAPIView):
    queryset = FreeProduct.objects.all()
    serializer_class = FreeProductSerializer
