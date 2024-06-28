from django.shortcuts import render
from rest_framework import generics
from .models import Page, GalleryPhoto, Settings
from .serializers import PageSerializer, GalleryPhotoSerializer, SettingsSerializer


class PageList(generics.ListAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class GalleryPhotoList(generics.ListAPIView):
    queryset = GalleryPhoto.objects.all()
    serializer_class = GalleryPhotoSerializer


class SettingsList(generics.ListAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer
