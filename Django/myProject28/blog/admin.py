from django.contrib import admin
from .models import UserList
# Register your models here.
@admin.register(UserList)
class UserAdmin(admin.ModelAdmin):
    list_display=['name','email']