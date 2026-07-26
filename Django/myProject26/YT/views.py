from django.shortcuts import render
from .models import User
from django.core.cache import cache

def user_list(request):
    users = cache.get('Users_data') # try to get data from cache

    if not users:
        print('cache: missing')
        users  = User.objects.all()
        cache.set('Users_data', users, timeout=60) #cache data for 60 sec

    else:
        print('cache: hit fetching data from cache')

    return render(request, 'user_list.html', {'users':users})

