from django.contrib import admin
from .models import Task
# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','created_at','completed')
    list_filter = ('title','created_at')
    search_fields = ('title',)
    ordering = ('-created_at',)
