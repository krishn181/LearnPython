from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('public/', views.public_view, name='public_view'),
    path('private/',views.private_view, name='private_view'),
    path('blog/', views.blog_list, name='blog_list'),

    path('user-profile/', views.user_profile, name='user_profile'),
    path('get-token/', obtain_auth_token, name='api_token_auth'),
    path('admin-panel/', views.admin_pannel, name='admin_pannel')
]
