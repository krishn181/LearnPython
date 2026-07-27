from django.urls import path
from .views import StudentApi

urlpatterns = [
    path('student/',StudentApi.as_view()),#get, post all data k liye
    path('student/<int:pk>/',StudentApi.as_view()) # get(single) , put, delete
]
