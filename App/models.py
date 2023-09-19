from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """username(str), email(str), password(str), joinedRooms(int,default=0), createdRooms(int,default=0)"""
    joinedRooms = models.IntegerField(default=0)
    createdRooms = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.username}"
    
class Room(models.Model):
    """name(str), description(str), admin(User), numberUsers(int,default=1)"""
    name = models.CharField(max_length=64,unique=True)
    description = models.CharField(max_length=256)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_admin")
    numberUsers = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.name} created by {self.admin.username}"
