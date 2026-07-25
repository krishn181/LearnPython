from django.shortcuts import render
from . import views
from django.http import HttpResponse

def home_view(request):
    return HttpResponse('Welcome to the page')