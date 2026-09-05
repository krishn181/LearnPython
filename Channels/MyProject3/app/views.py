from django.shortcuts import render

# def index(request):
#     return render(request, 'index.html')

#dynamic url for each group
def index(request, group_name):
    return render(request, 'index.html', {'groupname':group_name})