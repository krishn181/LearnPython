from django.shortcuts import render
from .models import UserProfile
from django.core.cache import cache

def user_profile(request):  
    users_data = cache.get('users_data')
    if  users_data is None:
        print(' fetching data from database')
        users_data = UserProfile.objects.all()
        cache.set('users_data',users_data)
    else:
        print('fetching data form cache')

    return render(request,'user_profile.html',{'users':users_data})
