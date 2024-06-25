from django.urls import path
from .views import ProductListAPIView, ProductDetailAPIView, FreeProductListAPIView, FreeProductDetailAPIView, \
                   GalleryPhotoListAPIView, GalleryPhotoDetailAPIView

urlpatterns = [
    path('products/', ProductListAPIView.as_view()),
    path('product/<int:id>/', ProductDetailAPIView.as_view()),
    path('freeproducts/', FreeProductListAPIView.as_view()),
    path('freeproduct/<int:id>/', FreeProductDetailAPIView.as_view()),
    path('galleryphotos/', GalleryPhotoListAPIView.as_view()),
    path('galleryphoto/<int:id>/', GalleryPhotoDetailAPIView.as_view()),
]