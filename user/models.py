from django.db import models
from django.contrib.auth.models import AbstractUser
from api.models import Resturant

class User(AbstractUser):
    ROLE_CHOICES = (
        ('owner', 'Owner'),
        ('employee', 'Employee'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')
    resturent = models.ForeignKey(Resturant, on_delete=models.CASCADE, null=True, blank=True)

