from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','city','age')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('name',)