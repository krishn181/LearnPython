from django.shortcuts import render
from datetime import datetime

def blog_details(request):
    post = {
        "title":"learn Django",
        "description":"this is blog detail page",
        "author":None,
        "created_at" : datetime.now(),
        "price":100,
        "Number":2,
    }
    return render(request, 'blog/blog_detail.html', {"post":post})