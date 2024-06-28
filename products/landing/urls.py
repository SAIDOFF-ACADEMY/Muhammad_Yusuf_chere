from django.urls import path

from products.landing import views

urlpatterns = [
    path('products/', views.ProductView.as_view()),
    path('product/<int:id>/', views.ProductDetailView.as_view()),
    path('free_product/<int:id>/', views.FreeProductView.as_view()),
]