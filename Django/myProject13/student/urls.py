from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.student_create, name='student_create'),
    path('', views.student_list, name='student_list'),
    path('student-detail/<int:pk>/', views.student_detail, name='student_detail'),

]
