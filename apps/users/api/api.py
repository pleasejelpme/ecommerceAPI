from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.http import Http404

from apps.users.api.serializers import UserSerializer
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
            return User.objects.get(id=pk)
        
        except:
            return Http404
    
    def get(self, request, pk):
        user = self.get_object(pk)
        user = UserSerializer(user)
        return Response(user.data)
        