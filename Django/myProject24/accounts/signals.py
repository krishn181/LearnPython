from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        print(f'New created: {instance.username}')
        subject = 'Welcome to Blog'
        message = f'Hi! {instance.username} Thank you for your registration'
        from_email ='singhkrishn704@gmail.com'
        recipent_email =[instance.email]
        send_mail(subject, message, from_email, recipent_email, fail_silently=False)
        print(f'message sent successfully {instance.username}')
