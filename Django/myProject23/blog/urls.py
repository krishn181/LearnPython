from django.urls import path
from . import views
urlpatterns = [
    path('send-email/',views.simple_test_email, name='simple_test_email'),
    path("template-email/", views.simple_template_email, name="simple_template_email")
]
