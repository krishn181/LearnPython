from django.shortcuts import render
from datetime import datetime

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def home(request):
    context = {
        'name': 'anish',
        'age': 23,
        'user': User('Anish', 24),
        'blog': {
            'title': 'Django basics',
            'content': 'this is dummy content',
            'author': 'name',
            'created_at': datetime(2026, 7, 8, 12, 24)
        },
        'empty_value': 'none'
    }
    return render(request, "templates/blog/home.html", context)