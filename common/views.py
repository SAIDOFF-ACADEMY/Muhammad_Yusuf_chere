from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Settings, Page
from .serializers import SettingsSerializer, PageSerializer


class SettingsListAPIView(ListAPIView):
    serializer_class = SettingsSerializer
    permission_classes = (AllowAny,)
    queryset = Settings.objects.all()


class PageListAPIView(ListAPIView):
    serializer_class = PageSerializer
    permission_classes = (AllowAny,)
    queryset = Page.objects.all()


class PageDetailAPIView(RetrieveAPIView):
    serializer_class = PageSerializer
    permission_classes = (AllowAny,)
    queryset = Page.objects.all()
    lookup_field = 'slug'
