from django.shortcuts import render
from .models import UserProfile
from django.core.cache import cache

def user_list(request):
    users = cache.get('user_list')
    if not users :
        print('Cache miss: quering database for users.')
        users = UserProfile.objects.all()
        cache.set('user_list',users,30)
    else:
        print('Cache hit: retrived users from cache.')
        
    return render(request, 'user.html',{'users':users})


    
