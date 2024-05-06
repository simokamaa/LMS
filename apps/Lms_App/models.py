from django.db import models
from django.contrib.auth.models import User,Group


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, blank=True, null=True)
    slug = models.CharField(max_length=100, blank=True, null=True)
    badge_color = models.CharField(max_length=20, null=True, blank=True)
    badge = models.IntegerField(null=True, blank=True)
    url = models.CharField(max_length=100, null=True, blank=True)
    external = models.BooleanField(default=False)
    permission = models.CharField(max_length=100, null=True, blank=True)
    target = models.CharField(max_length=20, null=True, blank=True)

    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)

    def __str__(self):
        return self.name

    # Add other fields as needed

class SubMenuItem(models.Model):
    menu_item = models.ForeignKey(MenuItem, related_name='submenu', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    external = models.BooleanField(default=False)
    target = models.CharField(max_length=100, blank=True, null=True)
    badge_color = models.CharField(max_length=20, null=True, blank=True)
    badge_count = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class App(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    users = models.ManyToManyField(Group, related_name='apps')
    menu = models.ForeignKey(MenuItem, on_delete=models.SET_NULL, null=True,blank=True)
    SubMenuItem = models.ForeignKey(SubMenuItem, on_delete=models.CASCADE,blank=True, null=True)
