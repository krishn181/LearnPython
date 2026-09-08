from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .models import Employee
def index(request):
    if request.user.is_authenticated:
        return HttpResponse(f"""<h2>Welcom {request.user.username},</h2> <br><h2>Tenant Schema:- {request.tenant.schema_name} page </h2> <br> 
                            <a href = "/logout/">Logout</a>""")
    return HttpResponse("<h2> not login </h2>")

def login_view(request):
    if request.method == "POST":    
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        return HttpResponse("<h3> Invalid username or password </h3>")
    return render(request,"login.html")

def logout_view(request):
    logout(request)
    return redirect ( "login")

@login_required
def create_employee(request, name):
    employee = Employee(name=name)
    employee.save()
    return HttpResponse(f"<h2> {request.tenant} employee</h2>")