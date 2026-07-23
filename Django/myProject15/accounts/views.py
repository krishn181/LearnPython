from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .form import RegistrationForm

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Successfull')
            return redirect('login')
        else:
            messages.error(request,'User not register try again')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, ' User Login Successfully')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid User')
    return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)
    messages.success(request,'Logout Successfull')
    return redirect('login')

def dashboard_view(request):
    return render(request,'accounts/dashboard.html')