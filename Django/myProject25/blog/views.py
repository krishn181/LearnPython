from django.shortcuts import render
from django.core.mail import send_mass_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.http import HttpResponse

def send_bulk_email(request):
    message1 = ('welcome user 1','hello user 1, welcome to our platform','singhkrishn704@gmail.com',['singhkrishn704@gmail.com'],)
                # Subject, message, sender, receiver
    message2 = ('welcome user 2','hello user 2 welcome to our platform','singhkrishn704@gmail.com',['singhkrishn704@gmail.com'],)
    send_mass_mail((message1, message2), fail_silently=False)
    return HttpResponse('send bulk mail')

def send_html_bulk_email(request):
    subject = 'Welcome to the blog'
    from_email='singhkrishn704@gmail.com'
    recipent_email=['singhkrishn704@gmail.com','singhkrishn@gmail.com']
    html_content = render_to_string('welcome_email.html',{'username':'anish'})
    msg = EmailMultiAlternatives(subject,'',from_email,recipent_email)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
    return HttpResponse('send bulk mail')