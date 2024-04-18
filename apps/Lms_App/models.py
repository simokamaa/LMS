# models.py
from django.db import models
from django.contrib.auth.models import User

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    # Add other fields as needed

class Menu(models.Model):
    name = models.CharField(max_length=100)
    items = models.ManyToManyField(MenuItem)

class App(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='apps')
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)


