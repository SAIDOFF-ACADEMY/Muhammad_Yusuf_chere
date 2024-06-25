from rest_framework import serializers
from .models import Settings, Page


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = (
            'contact_telegram',
            'contact_phone',
            'longitude',
            'latitude',
            'location_text',
            'working_hours_start',
            'working_hours_end',
            'telegram_bot',
        )


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = (
            'title',
            'slug',
            'content',
        )

