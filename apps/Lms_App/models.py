# models.py
from django.db import models
from django.contrib.auth.models import User


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    badge_color = models.CharField(max_length=20, null=True, blank=True)
    badge_count = models.IntegerField(null=True, blank=True)
    url = models.CharField(max_length=100, null=True, blank=True)
    external = models.BooleanField(default=False)
    permission = models.CharField(max_length=100, null=True, blank=True)
    target = models.CharField(max_length=20, null=True, blank=True)

    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)

    def __str__(self):
        return self.name

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
