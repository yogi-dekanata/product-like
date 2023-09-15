from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    status = models.CharField(max_length=100)

    class Meta:
        db_table = 'users'
