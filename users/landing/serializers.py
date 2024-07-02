from rest_framework import serializers

from users import models


class UserContactCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserContactApplication
        fields = (
            'full_name',
            'phone',
            'is_contacted',
        )
