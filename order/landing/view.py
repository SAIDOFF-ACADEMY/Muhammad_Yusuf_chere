from rest_framework.generics import GenericAPIView
from order.landing.serializers import OrderLandingSerializer
from order.models import Order
from rest_framework.response import Response


class OrderView(GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderLandingSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
    def get(self, request, *args, **kwargs):
        order = self.get_object().first()
        serializer = self.get_serializer(order)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        order = self.get_object().first()
        serializer = self.get_serializer(order, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        order = self.get_object().first()
        serializer = self.get_serializer(order, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
