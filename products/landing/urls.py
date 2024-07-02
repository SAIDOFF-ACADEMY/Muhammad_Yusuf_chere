from django.urls import path

from products.landing import views

urlpatterns = [
    path('products/', views.ProductView.as_view()),

]