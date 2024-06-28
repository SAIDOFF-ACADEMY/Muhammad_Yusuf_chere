from rest_framework import serializers
from .models import Page, GalleryPhoto, Settings


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['slug', 'title', 'content']
        read_only_fields = ['created_at', 'updated_at']


class GalleryPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryPhoto
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ['contact_telegram', 'contact_phone', 'longitude', 'latitude', 'locations_text', 'working_horse_start',
                  'working_horse_end', 'telegram_bot']
