from django.urls import path,include
from .views import StudentViewSets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('students', StudentViewSets, basename='students')
urlpatterns = [
    path('',include(router.urls))
]
