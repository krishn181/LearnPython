from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login_view/', views.login_view, name="login"),
    path('create_employee/<name>/', views.create_employee, name='create_employee'),
    path("logout/", views.logout_view, name="logout"),
]
