from django.db import models


class blog(models.Model):
    title = models.CharField(max_length=20)
    des = models.TextField()
    def __str__(self):
        return self.title
    
