from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.IntegerField(primary_key=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_login = models.IntegerField(default=0)
    email = models.CharField(max_length=128)

