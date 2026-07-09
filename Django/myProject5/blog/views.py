from django.shortcuts import render
from datetime import datetime

def blog_list(request):
    blog =[{"title":"DjangoLearning", "is_featured":True, "author":"HelloWorld"},
           {"title":"PythonLearning", "is_featured":False, "author":"World"}]
    context = {
        "blogs":blog,
        "created_at": datetime.now(),
        "htmlCode":"<h1>Welcome to html code </h1>"
    }
    return render( request, 'blog/home.html', context)
