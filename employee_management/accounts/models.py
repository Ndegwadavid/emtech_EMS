from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Admin(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='admin_users'  
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='admin_users'  
    )

    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'

