from django.shortcuts import render
from .models import Post
from django.db.models import Q

def post_list(request):
    query = request.GET.get('q') # search keyword 
    category = request.GET.get('category')
    post = Post.objects.all()
    if query:
        posts = post.filter(
            Q(title__icontains = query) |
            Q(content__icontains = query)
        )
    if category:
            posts = post.filter(category__iexact = category)
    return render(request, 'post_list.html', {'post':post, 'query':query, 'category':category})
        