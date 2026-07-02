from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("shop home page")
def product(request):
    return HttpResponse ("shop product page")