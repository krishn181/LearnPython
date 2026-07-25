from django.shortcuts import render
from django.http import HttpResponse

def set_cookies(request):
    response = HttpResponse('Cookies set successfully')
    response.set_cookie('username','anish',max_age=60*60*24)
    response.set_cookie('course','python',max_age=60*60*24)
    return response

def get_cookies(request):
    username = request.COOKIES.get('username','Guest')
    course = request.COOKIES.get('course','not enrolled')
    return HttpResponse(f'Welcome {username} your learning {course}' )

def delete_cookies(request):
    response = HttpResponse('Cookies Deleted Successfully')
    response.delete_cookie('username')
    response.delete_cookie('course')
    return response