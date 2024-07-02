from django.urls import path

from order.landing import views


urlpatterns = [
    path('order/create/', views.OrderCreateAPIView.as_view()),
    path('order/<int:id>/', views.OrderRetrieveAPIView.as_view()),
]