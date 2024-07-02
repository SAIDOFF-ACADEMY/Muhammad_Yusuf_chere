from rest_framework.generics import CreateAPIView

from users import models
from users.landing import serializers


class UserContactCreate(CreateAPIView):
    serializer_class = serializers.UserContactCreateSerializer
    queryset = models.UserContactApplication
