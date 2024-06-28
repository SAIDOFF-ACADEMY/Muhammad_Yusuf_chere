from django.urls import path
from .views import ProductList, FreeProductList

urlpatterns = [
    path('', ProductList.as_view(), name='product-list'),
    path('free/', FreeProductList.as_view(), name='free-product-list'),
]
