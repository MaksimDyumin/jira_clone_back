from django.shortcuts import render
from django.http import HttpResponse

def detail(request):
    return HttpResponse("You're looking at question.")
# Create your views here.
