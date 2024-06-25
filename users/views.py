from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from users.models import User, UserContactApplication
from users.serializers import UserSerializer, UserContactApplicationSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'id'


class UserAppliancesListAPIView(ListAPIView):
    queryset = UserContactApplication.objects.all()
    serializer_class = UserContactApplicationSerializer
    permission_classes = (AllowAny,)


class UserAppliancesDetailAPIView(RetrieveAPIView):
    queryset = UserContactApplication.objects.all()
    serializer_class = UserContactApplicationSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'id'


class UserAppliancesCreateView(CreateAPIView):
    queryset = UserContactApplication.objects.all()
    serializer_class = UserContactApplicationSerializer
    permission_classes = (AllowAny,)


