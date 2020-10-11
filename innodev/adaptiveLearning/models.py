from django.db import models
from django.urls import reverse

# Create your models here.
class profile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

def get_absolute_url(self):
        return reverse('adaptiveLearning:home')
