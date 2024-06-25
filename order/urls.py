from django.urls import path

from .views import OrderListAPIView, OrderDetailAPIView

urlpatterns = [
    path('orders/', OrderListAPIView.as_view()),
    path('order/<int:pk>/', OrderDetailAPIView.as_view()),
]