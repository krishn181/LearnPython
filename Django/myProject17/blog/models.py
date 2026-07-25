from django.db import models

class Post(models.Model):
    title= models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=100, blank=True, null=True)
        
    def __str__(self):
        return self.title