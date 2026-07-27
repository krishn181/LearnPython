from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('clear/', views.clear_cache, name='clear_cache')
]
