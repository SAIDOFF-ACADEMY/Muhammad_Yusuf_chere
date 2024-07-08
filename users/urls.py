from django.urls import path
from users import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:id>/', views.UserDetail.as_view(), name='user_detail'),
    path('users/<int:id>/update/', views.UserUpdateView.as_view(), name='user_update'),
    path('users/<int:id>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
    path('users/create/', views.UserCreate.as_view(), name='user_create'),
    path('users/login/', views.UserLoginView.as_view(), name='user_login'),
    path('users/logout/', views.UserLogOutView.as_view(), name='user_logout'),

    path('user_contacts/', views.UserContactView.as_view(), name='user_contact_list'),
    path('user_contact/<int:id>/', views.UserContactDetail.as_view(), name='user_contact_detail'),
    path('user_contact/<int:id>/update/', views.UserContactUpdate.as_view(), name='user_contact_update'),
]
