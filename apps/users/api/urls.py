from django.urls import path
from apps.users.api.api import ListUsers, DetailUser

urlpatterns = [
    path('users/', ListUsers.as_view(), name='users'),    
    path('users/<str:pk>/', DetailUser.as_view(), name='user'),

]
