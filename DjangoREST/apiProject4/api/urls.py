from django.urls import path
from .views import StudentUpdateRetrieveDeleteAPI, StudentListCreateAPI

urlpatterns = [
        path('students/', StudentListCreateAPI.as_view()), # Get all data post
        path('students/<int:pk>/', StudentUpdateRetrieveDeleteAPI.as_view())
]
