from django.urls import path
from .  import views
urlpatterns = [
    path('bulk-email/', views.send_bulk_email, name ='bulk-email'),
    path('send_html_email/', views.send_html_bulk_email, name='send_html_bulk_email')
]
