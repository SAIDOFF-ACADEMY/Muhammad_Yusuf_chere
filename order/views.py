from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from order import serializers
from order import models


class OrderListAPIView(ListAPIView):
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()
    permission_classes = [IsAdminUser]


class OrderCreateAPIView(CreateAPIView):
    serializer_class = serializers.OrderSerializer
    permission_classes = [IsAdminUser]
    queryset = models.Order.objects.all()


class OrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.OrderSerializer
    permission_classes = [IsAdminUser]
    queryset = models.Order.objects.all()
    lookup_field = 'id'
