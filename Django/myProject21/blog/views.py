from django.shortcuts import render
from django.http import HttpResponse

def set_session(request):
    request.session['username']='Anish'
    request.session['course']='django full course'
    return HttpResponse('session data saved successfully')

def get_session(request):
    username = request.session.get('username','Guest')
    course = request.session.get('course','Not enrolled')
    return HttpResponse(f'Welcome: {username}, you are learning: {course}')

def delete_session(request):
    request.session.flush()# it delete all the session 
    return HttpResponse ('All session Data are successully deleted')