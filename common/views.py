from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveUpdateAPIView, CreateAPIView, \
    RetrieveUpdateDestroyAPIView

from common import serializers
from common import models


# Settings API for Settings model
class SettingsView(GenericAPIView):
    serializer_class = serializers.SettingsSerializer
    queryset = models.Settings.objects.all()
    permission_classes = [IsAdminUser, ]

    def get(self, request, *args, **kwargs):
        settings = self.get_queryset().first()
        serializer = self.get_serializer(settings)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        settings = self.get_queryset().first()
        serializer = self.get_serializer(settings, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        settings = self.get_queryset().first()
        serializer = self.get_serializer(settings, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# Page API for Page model
class PageView(ListAPIView):
    queryset = models.Page.objects.all()
    serializer_class = serializers.PageSerializer
    permission_classes = [IsAdminUser, ]


class PageDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = models.Page.objects.all()
    serializer_class = serializers.PageSerializer
    permission_classes = [IsAdminUser, ]
    lookup_field = 'slug'


class PageCreateView(CreateAPIView):
    queryset = models.Page.objects.all()
    serializer_class = serializers.PageSerializer
    permission_classes = [IsAdminUser, ]


# GalleryPhoto API for GalleryPhoto model
class GalleryView(ListAPIView):
    serializer_class = serializers.GallerySerializer
    permission_classes = [IsAdminUser, ]
    queryset = models.GalleryPhoto.objects.all()


class GalleryDetailUpdateView(RetrieveUpdateAPIView):
    queryset = models.GalleryPhoto.objects.all()
    serializer_class = serializers.GallerySerializer
    permission_classes = [IsAdminUser, ]
    lookup_field = 'id'

