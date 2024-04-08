from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import Group

TEACHER_GROUP_NAME = 'Teacher'
STUDENT_GROUP_NAME = 'Student'
ADMIN_GROUP_NAME = 'Admin'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    email = models.EmailField(max_length=100, unique=True)  # Use unique=True for unique email addresses
    email_token = models.CharField(max_length=100, blank=True, null=True)
    forget_password_token = models.CharField(max_length=100, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance, email=instance.email)


    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"



class CustomGroup(Group):
    class Meta:
        proxy = True

# Then create the groups if not exists
teacher_group, _ = CustomGroup.objects.get_or_create(name=TEACHER_GROUP_NAME)
student_group, _ = CustomGroup.objects.get_or_create(name=STUDENT_GROUP_NAME)
admin_group, _ = CustomGroup.objects.get_or_create(name=ADMIN_GROUP_NAME)
