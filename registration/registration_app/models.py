from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # your fields here

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # change 'customuser_set' to any name you prefer
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
