from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Product, FreeProduct, GalleryPhoto
from .serializers import ProductSerializer, FreeProductSerializer, GalleryPhotoSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'


class FreeProductListAPIView(ListAPIView):
    queryset = FreeProduct.objects.all()
    serializer_class = FreeProductSerializer
    permission_classes = [AllowAny]


class FreeProductDetailAPIView(RetrieveAPIView):
    queryset = FreeProduct.objects.all()
    serializer_class = FreeProductSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'


class GalleryPhotoListAPIView(ListAPIView):
    queryset = GalleryPhoto.objects.all()
    serializer_class = GalleryPhotoSerializer
    permission_classes = [AllowAny]


class GalleryPhotoDetailAPIView(RetrieveAPIView):
    queryset = GalleryPhoto.objects.all()
    serializer_class = GalleryPhotoSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'