from django.urls import path
from order.landing.view import OrderView

urlpatterns = [
    path('order/', OrderView.as_view(), name='landing'),
]