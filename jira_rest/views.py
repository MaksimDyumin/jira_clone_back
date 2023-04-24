from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def detail(request):
    return Response({'text': "You're looking at question."})
# Create your views here.
