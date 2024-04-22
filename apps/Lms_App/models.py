# models.py
from django.db import models
from django.contrib.auth.models import User

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=255, null=True, blank=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    badge = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=200)
    # Add other fields as needed

class SubMenu(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255, null=True, blank=True)
    items = models.ManyToManyField(MenuItem)

class App(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='apps')
    menu = models.ForeignKey(MenuItem, on_delete=models.SET_NULL, null=True)
