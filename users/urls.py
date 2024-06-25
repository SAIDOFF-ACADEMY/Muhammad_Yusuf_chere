from django.urls import path
from .views import UserListAPIView, UserDetailView, UserAppliancesListAPIView, UserAppliancesDetailAPIView, \
                   UserAppliancesCreateView

urlpatterns = [
    path('users/', UserListAPIView.as_view()),
    path('user/<int:id>/', UserDetailView.as_view()),
    path('appliances/', UserAppliancesListAPIView.as_view()),
    path('appliance/<int:id>/', UserAppliancesDetailAPIView.as_view()),
    path('appliance/create/', UserAppliancesCreateView.as_view()),

]