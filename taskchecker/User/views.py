from pickle import FALSE

from django.db.models.functions import Trunc
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets, status
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    @action(methods=['post'], detail=False) # эта хуета работает только через postman потму что не приниает get запросы
    def registrate(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'post': 'Created user'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserRegistrate(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# class UserCheck(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer



