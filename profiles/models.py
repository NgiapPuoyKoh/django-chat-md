from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class UserProfile(models.Model):
    """
    A user profile model for maintaining user profiles
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80,
                            null=True, blank=True)
    email = models.EmailField(max_length=70, blank=True, null=True, unique= True)

    def __str__(self):
        return str(self.name)

