from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    user_type_choices = [
        ('patient', 'Patient'),
        ('provider', 'Healthcare Provider'),
    ]
    user_type = models.CharField(max_length=20, choices=user_type_choices)
