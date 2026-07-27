from django.urls import path
from . import views
urlpatterns = [
    path('', views.get_student, name='get_student'),
    path('add/', views.create_student, name='create_student'),
    path("update/<int:pk>/", views.update_student, name="update_student"),
    path('delete/<int:pk>/', views.delete_student, name='delete_student')
]
