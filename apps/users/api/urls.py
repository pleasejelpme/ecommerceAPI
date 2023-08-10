from django.urls import path
from apps.users.api.api import ListUsers, DetailUser, list_users, detail_user

urlpatterns = [
    path('users/', list_users, name='users'),    
    path('users/<str:pk>/', detail_user, name='user'),

]
