from django.db import models
from django.urls import reverse

class GeekModel(models.Model):
    title = models.CharField(max_length=50,null=True)
    description = models.TextField()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('home')
    
