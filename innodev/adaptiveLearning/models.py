from django.db import models
from django.urls import reverse
from django import forms


# Create your models here.
class Addition(models.Model):
    questions = models.CharField(max_length=100)
    answers = models.CharField(max_length=100)
    ans = models.CharField(max_length=100)


class profile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)


def __str__(self):
    return self.password


class EmailForm(forms.ModelForm):
    class Meta:
        fields = ('email',)
    widgets = {
        'email', forms.TextInput(attrs={'class': 'form-control'})
    }
