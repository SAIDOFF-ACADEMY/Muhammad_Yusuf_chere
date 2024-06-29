from django.urls import path

from common import views


urlpatterns = [
    path('settings/', views.SettingsView.as_view()),
    # pages
    path('pages/', views.PageView.as_view()),
    path('page/<slug:slug>/', views.PageDetailUpdateDeleteView.as_view()),
    path('pages/add/', views.PageCreateView.as_view()),
    # gallery photos
    path('photos/', views.GalleryView.as_view()),
    path('photo/create/', views.GalleryCreateView.as_view()),
    path('photo/<int:id>/', views.GalleryDeleteView.as_view()),
]