from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Users(AbstractUser):
    name= models.CharField(max_length=200)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=255, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Task(models.Model):
    name = models.CharField(max_length=255)
    date_time = models.CharField(max_length=255,null=True)
    assigned_to = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.name