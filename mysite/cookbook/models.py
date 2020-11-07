from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Cookbook(models.Model):
    foodName = models.CharField(max_length=100)
    prep = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=200)
    image = models.ImageField(default='G:\programmingProjects\pyProjects\mysite\templates\RedApple_300x300.jpg')
    datetime = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    
        
