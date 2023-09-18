from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """username(str), email(str), password(str), joinedRooms(int,default=0), createdRooms(int,default=0)"""
    joinedRooms = models.IntegerField(default=0)
    createdRooms = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.username}"
    
