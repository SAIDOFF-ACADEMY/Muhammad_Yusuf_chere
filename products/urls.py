from django.urls import path

from products import views

urlpatterns = [
    path('products/', views.ProductListView.as_view()),
    path('product/<int:id>/', views.ProductDetailUpdateDeleteView.as_view()),
    path('product/create/', views.ProductCreateView.as_view()),
    path('free_products/', views.FreeProductListView.as_view()),
    path('free_product/<int:id>/', views.FreeProductDetailUpdateDeleteView.as_view()),
    path('free_product/create/', views.FreeProductCreateView.as_view()),
]