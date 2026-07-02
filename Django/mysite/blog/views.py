from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Blog home page")
def about(request):
    return HttpResponse ("blog about page")