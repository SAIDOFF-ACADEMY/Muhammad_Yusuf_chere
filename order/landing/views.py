from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from order.landing import serializers
from order import models


class OrderCreateAPIView(CreateAPIView):
    serializer_class = serializers.OrderSerializer
    permission_classes = (IsAuthenticated,)
    queryset = models.Order.objects.all()


class OrderRetrieveAPIView(RetrieveAPIView):
    serializer_class = serializers.OrderSerializer
    permission_classes = (IsAuthenticated,)
    queryset = models.Order.objects.all()
    lookup_field = 'id'