# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    preferred_currency = models.CharField(max_length=10, default='INR')
