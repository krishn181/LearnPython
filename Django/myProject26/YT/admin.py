from django.contrib import admin
from django.core.cache import cache
from . models import User
from django.contrib import messages

@admin.action(description='ClearUserCache')
def clear_user_cache(modeladmin, request, queryset):
    cache.delete('user_data')
    messages.success(request,"user cache cleared successfully")

@admin.register(User)
class adminUser(admin.ModelAdmin):
    list_display = ('name','email','subscribers')
    search_fields = ('name','email')
    list_filter = ('subscribers',)
    actions =[clear_user_cache]