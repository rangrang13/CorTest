
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Notion(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    

    def __str__(self):
        return self.title
    
