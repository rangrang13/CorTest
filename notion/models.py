
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Notion(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    

    def __str__(self):
        return self.title
    


class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    productTitle = models.CharField(max_length=100)
    productContent = models.TextField()
    productImage = models.ImageField(null=True, blank=True)
    productOption = models.TextField()
    prodctPrice = models.CharField(max_length=100)
    

    def __str__(self):
        return self.productTitle