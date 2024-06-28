from django.urls import path
from product.landing.view import ProductView, FreeProductView

urlpatterns = [
    path('product/', ProductView.as_view(), name='landing'),
    path('free/', FreeProductView.as_view(), name='free'),
]
