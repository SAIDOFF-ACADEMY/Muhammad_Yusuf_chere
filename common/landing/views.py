import random

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.response import Response

from common.models import Settings, Page, GalleryPhoto
from .serializers import SettingsSerializer, PageSerializer, GalleryPhotoSerializer


class SettingsView(GenericAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer

    def get(self, request, *args, **kwargs):
        settings = self.get_queryset().first()
        serializer = self.get_serializer(settings)
        return Response(serializer.data)


class PageView(RetrieveAPIView):
    serializer_class = PageSerializer
    queryset = Page.objects.all()
    lookup_field = 'slug'


class GalleryPhotoView(ListAPIView):
    queryset = GalleryPhoto.objects.all().order_by('?')
    serializer_class = GalleryPhotoSerializer




