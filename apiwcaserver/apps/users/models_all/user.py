from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    email = models.EmailField(blank=True, unique=True)
    phone = models.CharField(max_length=12, null=True)
