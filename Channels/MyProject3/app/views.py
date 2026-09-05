from django.shortcuts import render
from .models import Chat, Group
# def index(request):
#     return render(request, 'index.html')

#dynamic url for each group
def index(request, group_name):
    group = Group.objects.filter(name = group_name).first()
    chat = []
    if group is not None:
        chat = Chat.objects.filter(group=group)
    else:
        group = Group(name = group_name)
        group.save()
    return render(request, 'index.html', {'groupname':group_name, 'chats':chat})