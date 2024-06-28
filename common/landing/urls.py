from django.urls import path

from common.landing import views

urlpatterns = [
    path('settings/', views.SettingsView.as_view()),
    path('page/<slug:slug>/', views.PageView.as_view()),
    path('photos/', views.GalleryPhotoView.as_view()),
    path('photo/<int:id>/', views.GalleryPhotoDetail.as_view()),
]