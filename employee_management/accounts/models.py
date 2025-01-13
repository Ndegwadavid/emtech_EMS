from django.contrib.auth.models import AbstractUser
from django.db import models

class Admin(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
