from django.urls import path

from order import views

urlpatterns = [
    path('orders/', views.OrderListAPIView.as_view()),
    path('orders/<int:id>/', views.OrderRetrieveUpdateView.as_view()),
]