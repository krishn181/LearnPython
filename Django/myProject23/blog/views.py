from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponse

def simple_test_email(request):
    subject = 'Welcome to my blog'
    message = 'Thank you'
    from_email = 'singhkrishn704@gmail.com'
    recipent_email = ['krisnpalsingh0506@gmail.com']
    send_mail(subject, message, from_email, recipent_email)
    return HttpResponse('Email sent successfully')

#EmailMessage is used to send a templateemail/html 
def simple_template_email(request):
    subject ='Welcome to BLOG'
    message = render_to_string('template.html',{
        'username':'anish',
        'course':'django'
    })
    email=EmailMessage(
        subject,
        message,
        'singhkrishn704@gmail.com',
        ['singhkrishn704@gmail.com']
    )
    email.content_subtype = 'html'
    email.send()
    return HttpResponse('email sent!')