from django.shortcuts import render
from django.contrib import messages
def show_msg(request):
    messages.debug(request, 'This is a debug message')
    messages.info(request, 'This is an info message')
    messages.warning(request,'This is warning message')
    messages.success(request,'This is success message')
    return render(request,'show_msg.html')