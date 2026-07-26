from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(unique=True)
    subscribers = models.IntegerField(default=0)

    def __str__(self):
        return self.name