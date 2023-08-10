from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view

from django.http import Http404

from apps.users.api.serializers import UserSerializer, UserListSerializer
from apps.users.models import User

class ListUsers(APIView):
    def get(self, request):
        users = User.objects.all()
        serialized_users = UserSerializer(users, many=True)
        return Response(serialized_users.data)

    def post(self, request):
        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(user.data, status=status.HTTP_201_CREATED)
        else:
            return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailUser(APIView):
    def get_object(self, pk):
        try:
            return User.objects.filter(id=pk).first()
        
        except:
            return Http404
    
    def get(self, request, pk):
        user = self.get_object(pk)
        user = UserSerializer(user)
        return Response(user.data)
    
###
### FUNCTION BASED VIEWS
### 


@api_view(['GET', 'POST'])
def list_users(request):
    # list
    if request.method == 'GET':
        users = User.objects.all().values('id', 'email', 'first_name', 'last_name', 'phone_number', 'password')
        serialized_users = UserListSerializer(users, many=True)
        return Response(serialized_users.data, status=status.HTTP_200_OK)    
    
    # post
    if request.method == 'POST':
        serialized_user = UserSerializer(data=request.data)
        if serialized_user.is_valid():
            serialized_user.save()
            return Response({'message':'User created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_user.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_user(request, pk):
    user = User.objects.filter(id=pk).first()

    # validation
    if user:

        # retrieve
        if request.method == 'GET':
            serialized_user = UserSerializer(user)
            return Response(serialized_user.data, status=status.HTTP_200_OK)

        # update
        if request.method == 'PUT':
            serialized_user = UserSerializer(user, data=request.data, context=request.data)
            if serialized_user.is_valid():
                serialized_user.save()
                return Response(serialized_user.data, status=status.HTTP_200_OK)
            else:
                return Response(serialized_user.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # delete
        if request.method == 'DELETE':
            user.delete()
            return Response({'message':'User deleted successfully'}, status=status.HTTP_200_OK)
        
    else:
        return Response({'message':'User not found'}, status=status.HTTP_404_NOT_FOUND)
