from rest_framework import serializers

from users import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'
        ref_name = 'AdminUserSerializer'


class UserContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserContactApplication
        fields = '__all__'
        ref_name = 'AdminUserContactSerializer'


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            'email',
            'full_name',
            'password',
        )
        ref_name = 'AdminUserCreateSerializer'
