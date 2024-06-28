from rest_framework.response import Response
from rest_framework import generics
from product import models
from product.landing.serializers import ProductLandingSerializer, FreeProductLandingSerializer


# class ProductView(generics.GenericAPIView):
#     queryset = models.Product.objects.all()
#     serializer_class = ProductSerializer
#
#     def get(self, request, *args, **kwargs):
#         products = models.Product.objects.all().first()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

    # def post(self, request, *args, **kwargs):
    #     serializer = ProductSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #
    # def put(self, request, *args, **kwargs):
    #     product = self.get_object()
    #     serializer = ProductSerializer(product, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
    #
    # def delete(self, request, *args, **kwargs):
    #     product = self.get_object()
    #     product.delete()


# class FreeProductView(generics.GenericAPIView):
#     queryset = models.FreeProduct.objects.all()
#     serializer_class = FreeProductSerializer

    # def post(self, request, *args, **kwargs):
    #     serializer = FreeProductSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    # def get(self, request, *args, **kwargs):
#     products = models.FreeProduct.objects.all().first()
#     serializer = FreeProductSerializer(products, many=True)
#     return Response(serializer.data)

    # def put(self, request, *args, **kwargs):
    #     product = self.get_object()
    #     serializer = FreeProductSerializer(product, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
    #
    # def delete(self, request, *args, **kwargs):
    #     product = self.get_object()
    #     product.delete()

class ProductView(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = ProductLandingSerializer


class FreeProductView(generics.ListCreateAPIView):
    queryset = models.FreeProduct.objects.all()
    serializer_class = FreeProductLandingSerializer
