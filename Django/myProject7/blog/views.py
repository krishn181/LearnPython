from django.shortcuts import render

def home (request):
    return render(request, 'home.html')
def blog ( request):
    student_list = [
        {'name':'Hello','age':12},
        {'name':'mello','age':22},
        {'name':'cello','age':14}
    ]
    return render(request, 'blog/blog.html', {'student':student_list})