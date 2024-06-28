from django.urls import path
from .views import PageList, SettingsList, GalleryPhotoList

urlpatterns = [
    path('', PageList.as_view(), name='page-list'),
    path('settings/', SettingsList.as_view(), name='settings-list'),
    path('photo/', GalleryPhotoList.as_view(), name='photo-list'),
]
