from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser

from users import models
from users import serializers


class UserList(ListAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    permission_classes = [IsAdminUser]


class UserDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    permission_classes = [IsAdminUser]
    lookup_field = 'id'


class UserCreate(CreateAPIView):
    serializer_class = serializers.UserCreateSerializer
    queryset = models.User.objects.all()
    permission_classes = [IsAdminUser]


class UserContactView(ListAPIView):
    serializer_class = serializers.UserContactSerializer
    queryset = models.UserContactApplication.objects.all()
    permission_classes = [IsAdminUser]


class UserContactDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.UserContactSerializer
    lookup_field = 'id'
    queryset = models.UserContactApplication.objects.all()
    permission_classes = [IsAdminUser]


class UserContactCreate(CreateAPIView):
    serializer_class = serializers.UserContactSerializer
    queryset = models.UserContactApplication
    permission_classes = [IsAdminUser]