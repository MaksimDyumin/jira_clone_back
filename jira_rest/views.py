from django.shortcuts import render

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import RegisterUserSerializer, ProfileUserSerializer, ProfilePictureSerializer

class DetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        res = {'text': 'Test view class'}
        return Response(res)
    
class RegistrationView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer

    def perform_create(self, serializer):
        serializer.save()

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