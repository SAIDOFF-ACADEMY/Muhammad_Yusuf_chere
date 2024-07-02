from rest_framework import serializers
from common import models


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Settings
        fields = '__all__'
        ref_name = 'AdminSettingsSerializer'


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Page
        fields = '__all__'
        ref_name = 'AdminPageSerializer'


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GalleryPhoto
        fields = ('photo', )
        ref_name = 'AdminPhotoSerializer'
