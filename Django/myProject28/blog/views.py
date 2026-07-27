from django.shortcuts import render
from .models import UserList
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.http import HttpResponse

@cache_page(30) # Cache on a view for 30 seconds
def user_list(request):
    print('fetching data from database')
    users = UserList.objects.all()
    return render(request, 'user_list.html',{'users':users})

def clear_cache(request):
    cache.clear()
    return HttpResponse('Cache clear successfully')

