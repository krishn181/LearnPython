from django.db import models

# Create your models here.
class UserProfile(models.Model):

    name = models.CharField(max_length=100)
    email = models.TextField(unique=True)
    subscriber = models.IntegerField(default=0)

    def __str__(self):
        return self.name
