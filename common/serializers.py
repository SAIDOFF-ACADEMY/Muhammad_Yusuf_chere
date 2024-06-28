from rest_framework import serializers
from common import models


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Settings
        fields = '__all__'


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Page
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GalleryPhoto
        fields = '__all__'