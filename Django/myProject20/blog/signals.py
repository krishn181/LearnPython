from django.db.models.signals import post_save, pre_save 
from django.dispatch import receiver
from .models import Blog

# trigger before saving a blog
@receiver(pre_save, sender=Blog)
def before_blog_save(sender, instance, **kwargs):
    print(f"About to pre_save : {instance.title}")

@receiver(post_save, sender=Blog)
def after_blog_save(sender, instance, created, **kwargs):
    if created:
        print(f'New blog created[post-save]: {instance.title}')
    else:
        print(f"blog updated post save  {instance.title}")