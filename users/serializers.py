from rest_framework import serializers
from .models import User, UserContactApplication


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'is_superuser',
            'is_staff',
            'telegram_id',
            'full_name',
            'phone',
            'email',
            'lang',
        )


class UserContactApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContactApplication
        fields = (
            'id',
            'full_name',
            'phone',
            'user',
        )