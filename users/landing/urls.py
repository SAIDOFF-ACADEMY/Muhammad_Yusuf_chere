from django.urls import path

from users.landing import views


urlpatterns = [
    path('user_contacts/create/', views.UserContactCreate.as_view()),
]
