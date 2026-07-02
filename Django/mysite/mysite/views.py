from django.http import HttpResponse

def index(request):
    return HttpResponse(''' <a href ="https://www.google.com">Google </a>''')

def hello(request):
    return HttpResponse(''' <a href="https://www.facebook.com">facebook</a>''')