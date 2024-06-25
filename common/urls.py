from django.urls import path

from .views import SettingsListAPIView, PageListAPIView, PageDetailAPIView

app_name = 'common'

urlpatterns = [
    path('settings/', SettingsListAPIView.as_view()),
    path('pages/', PageListAPIView.as_view()),
    path('page/<slug:slug>/', PageDetailAPIView.as_view()),

]