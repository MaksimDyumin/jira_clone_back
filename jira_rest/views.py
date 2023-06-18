from django.shortcuts import render

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .models import User, Room, Desk, Task
from .serializers import (
    RegisterUserSerializer, ProfileUserSerializer, ProfilePictureSerializer, 
    UserRoomSerializer, UserDesksSerializer, UserTasksSerializer
)



class DetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        res = {'text': 'Test view class'}
        return Response(res)


class RegistrationView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer


class UserProfileView(RetrieveAPIView):
    serializer_class = ProfileUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserProfilePictureView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        instance = request.user
        serializer = ProfilePictureSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status':'ok'})


class UserRoomsListView(ListCreateAPIView):
    serializer_class = UserRoomSerializer
    permission_classes = [IsAuthenticated]
    

    def get_queryset(self):
        return self.request.user.rooms.all()
    
    def perform_create(self, serializer):
        author = self.request.user
        instance = serializer.save(author=author)
        instance.users.add(author)
        instance.save()
    


class UserRoomsViewSet(viewsets.ModelViewSet):
    serializer_class = UserRoomSerializer

    def get_queryset(self):
        return self.request.user.rooms.all()
    
    def perform_create(self, serializer):
        author = self.request.user
        instance = serializer.save(author=author)
        instance.users.add(author)
        instance.save()

class UserDesksViewSet(viewsets.ModelViewSet):
    serializer_class = UserDesksSerializer
    # queryset = Room.objects.all()

    def get_queryset(self):
        return Desk.objects.filter(room=self.kwargs['room_pk'])
    
    def perform_create(self, serializer):
        room = self.kwargs['room_pk']
        serializer.save(room_id=room)


class UserTasksViewSet(viewsets.ModelViewSet):
    serializer_class = UserTasksSerializer

    def get_queryset(self):
        return Task.objects.filter(desk=self.kwargs['desk_pk'])
    
    def perform_create(self, serializer):
        desk = self.kwargs['desk_pk']
        serializer.save(desk_id=desk)